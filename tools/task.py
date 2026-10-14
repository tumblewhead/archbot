#!/usr/bin/env python3
"""Validate, preview, or execute a reusable Progressive Concretization task.

A task references a role, playbook and architecture spine. It does not approve
architecture, discharge obligations, or validate mathematics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
OP_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")


class TaskError(ValueError):
    """A task is invalid, missing required context, or unsafe to resolve."""


def _file(root: Path, relative: str, subdirectory: str | None = None) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise TaskError("Expected a nonempty repository-relative path")
    base = root if subdirectory is None else root / subdirectory
    base = base.resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(base):
        raise TaskError("Task path escapes its authorized directory: " + relative)
    if not path.is_file():
        raise TaskError("Required task input is missing: " + relative)
    return path


def validate(root: Path, manifest: str) -> dict:
    """Validate manifest controls, never a review/selection verdict."""
    root = root.resolve()
    manifest_file = _file(root, manifest, "process/tasks")
    data = yaml.safe_load(manifest_file.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != "pc-task/v1":
        raise TaskError("Manifest must be a pc-task/v1 mapping")
    task_id = data.get("id")
    role = data.get("role")
    operation = data.get("operation")
    if not isinstance(task_id, str) or not ID_PATTERN.fullmatch(task_id):
        raise TaskError("Invalid task ID")
    if not isinstance(role, str) or not ID_PATTERN.fullmatch(role):
        raise TaskError("Invalid role identifier")
    if not isinstance(operation, str) or not OP_PATTERN.fullmatch(operation):
        raise TaskError("Invalid operation")
    _file(root, "agents/" + role + ".md", "agents")
    registry = yaml.safe_load(_file(root, "process/operations.yaml").read_text(encoding="utf-8"))
    if not isinstance(registry, dict) or not isinstance(registry.get("operations"), dict):
        raise TaskError("Operation registry is missing or malformed")
    op_spec = registry["operations"].get(operation)
    if not isinstance(op_spec, dict):
        raise TaskError("Operation is not registered: " + operation)
    if op_spec.get("role") != role or op_spec.get("playbook") != data.get("playbook"):
        raise TaskError("Manifest role/playbook conflicts with the registered operation")
    views = yaml.safe_load(_file(root, "process/views.yaml").read_text(encoding="utf-8"))
    if not isinstance(views, dict) or role not in views.get("roles", {}):
        raise TaskError("Role has no context-traversal policy: " + role)
    playbook = _file(root, data.get("playbook"), "process/playbooks")
    if playbook.suffix != ".md":
        raise TaskError("Playbook must be Markdown")

    spine_ref = data.get("spine")
    if not isinstance(spine_ref, str) or not spine_ref.startswith("/"):
        raise TaskError("Spine must be a knowledge-root absolute reference (/architecture/...)")
    knowledge = (root / "knowledge").resolve()
    spine = (knowledge / spine_ref.lstrip("/")).resolve()
    if not spine.is_relative_to(knowledge) or spine.suffix != ".md" or not spine.is_file():
        raise TaskError("Spine reference missing, unsafe, or not a Markdown file")

    trigger = data.get("trigger")
    if not isinstance(trigger, dict) or not isinstance(trigger.get("kind"), str):
        raise TaskError("Task trigger.kind required")
    if trigger.get("reference"):
        trigger_path = _file(root, trigger["reference"])
    else:
        trigger_path = None
    if trigger["kind"] == "CONTRACT_UNRESOLVED_SUBMITTED":
        if operation != "REVIEW_CON" or trigger_path is None or trigger_path.suffix != ".md":
            raise TaskError("Unresolved contract review requires REVIEW_CON and a draft contract spine")
        inputs = data.get("context", {}).get("artifact_inputs", {})
        receipt_ref = inputs.get("submission_receipt") if isinstance(inputs, dict) else None
        if (not isinstance(inputs, dict)
                or inputs.get("primary_concept") != trigger["reference"]
                or not isinstance(receipt_ref, str)):
            raise TaskError("Unresolved contract review must identify exact spine and authoring receipt")
        receipt = json.loads(_file(root, receipt_ref, "reviews").read_text(encoding="utf-8"))
        if (not isinstance(receipt, dict)
                or receipt.get("schema") != "pc-con-authoring-receipt/v1"
                or receipt.get("operation") != "DEFINE_CON"
                or receipt.get("gate_status") != "CONTRACTS_UNRESOLVED"
                or not isinstance(receipt.get("unresolved"), list)
                or not receipt["unresolved"]
                or trigger["reference"] not in receipt.get("changed_artifacts", [])):
            raise TaskError("Unresolved contract submission lacks matching bounded receipt")
        header = trigger_path.read_text(encoding="utf-8")
        if not header.startswith("---\n") or "\n---\n" not in header:
            raise TaskError("Submitted contract spine is not a versioned OKF concept")
        concept = yaml.safe_load(header.split("\n---\n", 1)[0][4:])
        if not isinstance(concept, dict) or concept.get("type") != "Contract Spine":
            raise TaskError("Submitted concept is not a Contract Spine")
        contracts = inputs.get("related_concepts")
        if not isinstance(contracts, list) or not contracts:
            raise TaskError("Unresolved contract review must name draft contracts")
        for contract in contracts:
            if contract not in receipt["changed_artifacts"]:
                raise TaskError("Contract not in submitted receipt: " + str(contract))
            contract_text = _file(root, contract, "knowledge").read_text(encoding="utf-8")
            if not contract_text.startswith("---\n") or "\n---\n" not in contract_text:
                raise TaskError("Submitted contract lacks OKF frontmatter")
            contract_meta = yaml.safe_load(contract_text.split("\n---\n", 1)[0][4:])
            if not isinstance(contract_meta, dict) or contract_meta.get("type") != "Design Contract":
                raise TaskError("Unresolved review includes a noncontract concept")
        source_task_ref = "process/tasks/" + str(receipt.get("task_id")) + ".yaml"
        original = yaml.safe_load(_file(root, source_task_ref, "process/tasks").read_text(encoding="utf-8"))
        if (not isinstance(original, dict) or original.get("operation") != "DEFINE_CON"
                or original.get("trigger", {}).get("kind") != "BASELINE_ACTIVATED"):
            raise TaskError("Submitted contracts do not originate from active-baseline authoring")
        baseline_ref = original["trigger"].get("reference")
        from active_baseline import ActiveBaselineError, verify
        try:
            verify(root, baseline_ref)
        except (ActiveBaselineError, OSError, ValueError, KeyError) as exc:
            raise TaskError("Unresolved contract review lacks verified baseline: " + str(exc)) from exc
    if trigger["kind"] == "IMPLEMENTATION_DRAFT_SUBMITTED":
        if operation != "REVIEW_IMPLEMENTATION" or trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("Implementation review requires a versioned authoring receipt")
        receipt = json.loads(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(receipt, dict)
                or receipt.get("schema") != "pc-implementation-authoring-receipt/v1"
                or receipt.get("operation") != "IMPLEMENT_DE"
                or receipt.get("gate") != "IMPLEMENTATION_REVIEW"
                or receipt.get("gate_status") != "IMPLEMENTATION_READY_FOR_INDEPENDENT_REVIEW"):
            raise TaskError("Implementation review lacks ready authoring receipt")
        source_id = receipt.get("task_id")
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            raise TaskError("Implementation receipt lacks valid source task")
        original = yaml.safe_load(_file(
            root, "process/tasks/" + source_id + ".yaml", "process/tasks"
        ).read_text(encoding="utf-8"))
        if (not isinstance(original, dict) or original.get("operation") != "IMPLEMENT_DE"
                or original.get("spine") != spine_ref
                or original.get("trigger", {}).get("kind") != "DESIGN_ACCEPTED_FOR_IMPLEMENTATION"
                or original.get("trigger", {}).get("reference") != receipt.get("trigger")):
            raise TaskError("Implementation authoring does not belong to this reviewed project")
        context = data.get("context", {})
        review_inputs = context.get("review_inputs", {}) if isinstance(context, dict) else {}
        if (not isinstance(review_inputs, dict)
                or review_inputs.get("independent_review") != trigger["reference"]):
            raise TaskError("Implementation review task does not bind its authoring receipt")
        pins = receipt.get("source_sha256")
        if not isinstance(pins, dict) or not pins:
            raise TaskError("Implementation receipt lacks source hashes")
        changed = receipt.get("changed_artifacts")
        if not isinstance(changed, list):
            raise TaskError("Implementation receipt lacks changed artifact list")
        for ref, digest in pins.items():
            if ref not in changed or not isinstance(digest, str):
                raise TaskError("Implementation source hash not declared in changed artifacts")
            actual = hashlib.sha256(_file(root, ref, "implementation").read_bytes()).hexdigest()
            if actual != digest:
                raise TaskError("Implementation source changed after authoring: " + ref)
        for ref in changed:
            if (isinstance(ref, str) and ref.startswith("implementation/")
                    and ref.endswith(".md")):
                _file(root, ref, "implementation")
        if not any(isinstance(ref, str) and ref.endswith(".md")
                   and "BRIEFING" in ref.upper() for ref in changed):
            raise TaskError("Implementation review lacks an Engineering Briefing")
        if not any(isinstance(ref, str) and ref.endswith(".md")
                   and "REVIEW" in ref.upper() for ref in changed):
            raise TaskError("Implementation review lacks independent review request")
    if trigger["kind"] == "DESIGN_ACCEPTED_FOR_IMPLEMENTATION":
        if (operation != "IMPLEMENT_DE" or trigger_path is None
                or trigger_path.suffix != ".json"):
            raise TaskError("Implementation requires IMPLEMENT_DE and independent DE review")
        review = json.loads(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(review, dict)
                or review.get("schema") != "pc-de-review/v1"
                or review.get("gate") != "DE_REVIEW"
                or review.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
                or review.get("next_stage_recommendation")
                    != "DE_ACCEPTABLE_FOR_GUARDED_IMPLEMENTATION_TASK"
                or review.get("independent_of_authoring_invocation") is not True
                or any(isinstance(finding, dict) and finding.get("severity") == "blocking"
                       for finding in review.get("findings", []))):
            raise TaskError("Implementation lacks favorable independent DE acceptance")
        context = data.get("context", {})
        inputs = context.get("review_inputs", {}) if isinstance(context, dict) else {}
        if (not isinstance(inputs, dict)
                or inputs.get("independent_review") != trigger["reference"]):
            raise TaskError("Implementation manifest must reference exact DE review")
        source_id = review.get("task_id")
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            raise TaskError("DE review has invalid source task identity")
        reviewer = yaml.safe_load(_file(
            root, "process/tasks/" + source_id + ".yaml", "process/tasks"
        ).read_text(encoding="utf-8"))
        if (not isinstance(reviewer, dict) or reviewer.get("operation") != "REVIEW_DE"
                or reviewer.get("spine") != spine_ref
                or reviewer.get("trigger", {}).get("kind") != "DE_DRAFT_SUBMITTED"):
            raise TaskError("Implementation DE review belongs to another project or stage")
        review_context = reviewer.get("context", {}).get("artifact_inputs", {})
        de_spine = review_context.get("primary_concept") if isinstance(review_context, dict) else None
        elements = review_context.get("related_concepts") if isinstance(review_context, dict) else None
        if (not isinstance(de_spine, str) or not isinstance(elements, list)
                or not elements or reviewer.get("trigger", {}).get("reference") != de_spine):
            raise TaskError("DE review lacks complete design-element package")
        pins = review.get("reviewed_input_sha256")
        if not isinstance(pins, dict):
            raise TaskError("DE review lacks reviewed source hashes")
        for ref in [de_spine, *elements]:
            if hashlib.sha256(_file(root, ref, "knowledge").read_bytes()).hexdigest() != pins.get(ref):
                raise TaskError("DE artifact changed after independent review: " + ref)
        active_refs = [ref for ref in pins if isinstance(ref, str)
                       and ref.startswith("process/baselines/")
                       and ref.endswith("-active.yaml")]
        if len(active_refs) != 1:
            raise TaskError("DE review must pin exactly one active baseline")
        active_ref = active_refs[0]
        from active_baseline import ActiveBaselineError, verify
        try:
            verify(root, active_ref)
        except (ActiveBaselineError, OSError, ValueError, KeyError) as exc:
            raise TaskError("Implementation active baseline invalid: " + str(exc)) from exc
        if hashlib.sha256(_file(root, active_ref, "process/baselines").read_bytes()).hexdigest() != pins[active_ref]:
            raise TaskError("Active baseline changed after DE review")
        if (not isinstance(data.get("outputs"), dict)
                or "implement_firmware" in data["outputs"].get("prohibited", [])
                or "implementation_source" not in data["outputs"].get("allowed", [])):
            raise TaskError("Implementation task lacks explicitly permitted source output")
    if trigger["kind"] == "DE_DRAFT_SUBMITTED":
        if operation != "REVIEW_DE" or trigger_path is None or trigger_path.suffix != ".md":
            raise TaskError("DE review requires REVIEW_DE and a versioned DE spine")
        inputs = data.get("context", {}).get("artifact_inputs", {})
        if not isinstance(inputs, dict) or inputs.get("primary_concept") != trigger["reference"]:
            raise TaskError("DE review must identify its exact submitted spine")
        receipt_ref = inputs.get("submission_receipt")
        receipt = json.loads(_file(root, receipt_ref, "reviews").read_text(encoding="utf-8"))
        if (not isinstance(receipt, dict)
                or receipt.get("schema") != "pc-de-authoring-receipt/v1"
                or receipt.get("operation") != "DECOMPOSE_DE"
                or receipt.get("gate") != "DE_REVIEW"
                or receipt.get("gate_status") != "DE_READY_FOR_INDEPENDENT_REVIEW"
                or trigger["reference"] not in receipt.get("changed_artifacts", [])):
            raise TaskError("DE review lacks matching ready authoring receipt")
        source_task = receipt.get("task_id")
        if not isinstance(source_task, str) or not ID_PATTERN.fullmatch(source_task):
            raise TaskError("DE receipt has invalid source task identity")
        author = yaml.safe_load(_file(
            root, "process/tasks/" + source_task + ".yaml", "process/tasks"
        ).read_text(encoding="utf-8"))
        if (not isinstance(author, dict) or author.get("operation") != "DECOMPOSE_DE"
                or author.get("spine") != spine_ref
                or author.get("trigger", {}).get("kind") != "CONTRACT_ACCEPTED_FOR_DE"):
            raise TaskError("DE review source task is not authorized for this project")
        if not isinstance(inputs.get("related_concepts"), list) or not inputs["related_concepts"]:
            raise TaskError("DE review requires at least one design element")
        for ref, expected_type in [
            (trigger["reference"], "Design Element Spine"),
            *[(ref, "Design Element") for ref in inputs.get("related_concepts", [])],
        ]:
            if ref not in receipt["changed_artifacts"]:
                raise TaskError("Submitted DE concept missing from authoring receipt: " + ref)
            content = _file(root, ref, "knowledge").read_text(encoding="utf-8")
            if not content.startswith("---\n") or "\n---\n" not in content:
                raise TaskError("DE submission lacks OKF frontmatter: " + ref)
            meta = yaml.safe_load(content.split("\n---\n", 1)[0][4:])
            if not isinstance(meta, dict) or meta.get("type") != expected_type:
                raise TaskError("DE submission concept type mismatch: " + ref)
    if trigger["kind"] == "CONTRACT_ACCEPTED_FOR_DE":
        if operation != "DECOMPOSE_DE" or trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("DE refinement requires DECOMPOSE_DE and an independent CON review")
        review = json.loads(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(review, dict)
                or review.get("schema") != "pc-contract-review/v1"
                or review.get("gate") != "CONTRACT_REVIEW"
                or review.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
                or review.get("next_stage_recommendation") != "CON_ACCEPTABLE_FOR_DE_REFINEMENT"
                or review.get("independent_of_authoring_invocation") is not True
                or any(isinstance(item, dict) and item.get("severity") == "blocking"
                       for item in review.get("findings", []))):
            raise TaskError("DE refinement lacks favorable independent CON acceptance")
        inputs = data.get("context", {}).get("review_inputs", {})
        if not isinstance(inputs, dict) or inputs.get("independent_review") != trigger["reference"]:
            raise TaskError("DE refinement manifest must bind the exact independent CON review")
        source_id = review.get("task_id")
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            raise TaskError("CON review has no valid source task ID")
        reviewed_task = yaml.safe_load(_file(
            root, "process/tasks/" + source_id + ".yaml", "process/tasks"
        ).read_text(encoding="utf-8"))
        if not isinstance(reviewed_task, dict) or reviewed_task.get("operation") != "REVIEW_CON":
            raise TaskError("Accepted CON review has no independent REVIEW_CON task")
        if reviewed_task.get("spine") != spine_ref:
            raise TaskError("DE task and reviewed contract belong to different project spines")
        reviewed_context = reviewed_task.get("context", {}).get("artifact_inputs", {})
        contract_spine = reviewed_context.get("primary_concept") if isinstance(reviewed_context, dict) else None
        contracts = reviewed_context.get("related_concepts") if isinstance(reviewed_context, dict) else None
        if (not isinstance(contract_spine, str)
                or reviewed_task.get("trigger", {}).get("reference") != contract_spine
                or not isinstance(contracts, list) or not contracts):
            raise TaskError("Accepted CON review does not identify a complete contract package")
        pins = review.get("reviewed_input_sha256")
        if not isinstance(pins, dict):
            raise TaskError("Accepted CON review has no source hash evidence")
        for ref in [contract_spine, *contracts]:
            source = _file(root, ref, "knowledge")
            if hashlib.sha256(source.read_bytes()).hexdigest() != pins.get(ref):
                raise TaskError("Reviewed contract bytes changed or are unpinned: " + ref)
        active_refs = [name for name in pins
                       if isinstance(name, str) and name.startswith("process/baselines/")
                       and name.endswith("-active.yaml")]
        if len(active_refs) != 1:
            raise TaskError("DE refinement requires exactly one reviewed active baseline")
        active_ref = active_refs[0]
        authority_inputs = data.get("context", {}).get("authority_inputs", {})
        if (isinstance(authority_inputs, dict)
                and authority_inputs.get("active_baseline") not in (None, active_ref)):
            raise TaskError("DE refinement manifest conflicts with reviewed active baseline")
        from active_baseline import ActiveBaselineError, verify
        try:
            verify(root, active_ref)
        except (ActiveBaselineError, OSError, ValueError, KeyError) as exc:
            raise TaskError("DE refinement lacks verified active baseline: " + str(exc)) from exc
        if hashlib.sha256(_file(root, active_ref, "process/baselines").read_bytes()).hexdigest() != pins[active_ref]:
            raise TaskError("Active baseline changed since independent CON review")
    if trigger["kind"] == "CONTRACT_REVIEW_REVISION_REQUIRED":
        if trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("Contract revision requires a JSON independent-review receipt")
        try:
            review = json.loads(trigger_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise TaskError("Contract revision receipt is invalid JSON") from exc
        if (not isinstance(review, dict) or review.get("gate") != "CONTRACT_REVIEW"
                or review.get("disposition") != "REVISE"
                or review.get("next_stage_recommendation") != "CON_REVISION_REQUIRED"
                or review.get("independent_of_authoring_invocation") is not True
                or not any(f.get("severity") == "blocking" for f in review.get("findings", [])
                           if isinstance(f, dict))):
            raise TaskError("Contract revision trigger lacks an independent blocking REVISE finding")
    if trigger["kind"] == "STAGE_EVIDENCE_UNRESOLVED":
        if trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("Scope audit requires a versioned evidence-planning receipt")
        try:
            evidence = json.loads(trigger_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise TaskError("Invalid scope-audit evidence receipt") from exc
        if (not isinstance(evidence, dict)
                or evidence.get("schema") != "pc-gate-receipt/v1"
                or evidence.get("gate") != "EVIDENCE_PLANNING"
                or evidence.get("status") != "EVIDENCE_STILL_UNRESOLVED"
                or not isinstance(evidence.get("unresolved"), list)
                or not evidence["unresolved"]):
            raise TaskError("Scope audit requires an unresolved evidence-plan receipt")
    if trigger["kind"] == "STAGE_EVIDENCE_REQUIRED":
        if trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("Evidence planning requires a versioned JSON blocking receipt")
        try:
            blocked = json.loads(trigger_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise TaskError("Invalid evidence-blocker receipt") from exc
        if (not isinstance(blocked, dict)
                or blocked.get("schema") != "pc-gate-receipt/v1"
                or not isinstance(blocked.get("status"), str)
                or not blocked["status"].endswith("_UNRESOLVED")
                or not isinstance(blocked.get("unresolved"), list)
                or not blocked["unresolved"]):
            raise TaskError("Evidence planning requires a nonempty unresolved list")
    if trigger["kind"] == "EVIDENCE_PLAN_READY":
        if trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("Revision after evidence planning requires a JSON plan receipt")
        try:
            plan = json.loads(trigger_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise TaskError("Invalid evidence-plan receipt") from exc
        if (not isinstance(plan, dict) or plan.get("schema") != "pc-evidence-plan/v1"
                or plan.get("status") != "EVIDENCE_PLAN_READY_FOR_REVISION"
                or not isinstance(plan.get("plan_artifacts"), list)
                or not plan["plan_artifacts"]):
            raise TaskError("Evidence plan is not ready for revision")
        for plan_ref in plan["plan_artifacts"]:
            _file(root, plan_ref)
    if trigger["kind"] == "AS_REVISION_SUBMITTED":
        if operation != "REVIEW_AS" or trigger_path is None or trigger_path.suffix != ".md":
            raise TaskError("AS submission review requires REVIEW_AS and a candidate Markdown concept")
        authoring = data.get("context", {}).get("artifact_inputs", {})
        if (not isinstance(authoring, dict)
                or authoring.get("primary_concept") != trigger["reference"]
                or not isinstance(authoring.get("submission_receipt"), str)):
            raise TaskError("AS review must identify the exact candidate and authoring receipt")
        source_receipt = json.loads(_file(
            root, authoring["submission_receipt"], "reviews"
        ).read_text(encoding="utf-8"))
        if (not isinstance(source_receipt, dict)
                or source_receipt.get("schema") != "pc-gate-receipt/v1"
                or source_receipt.get("gate") != "AS_REVIEW"
                or source_receipt.get("status") != "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW"
                or not isinstance(source_receipt.get("changed_artifacts"), list)
                or not (
                    trigger["reference"] in source_receipt["changed_artifacts"]
                    or (
                        source_receipt.get("review_subject") == trigger["reference"]
                        and any(isinstance(item, str)
                                and item.startswith("knowledge/")
                                and item.endswith(".md")
                                and _file(root, item, "knowledge")
                                for item in source_receipt["changed_artifacts"])
                    )
                )):
            raise TaskError("AS revision submission lacks a matching ready receipt")
        candidate_content = trigger_path.read_text(encoding="utf-8")
        if (not candidate_content.startswith("---\n")
                or "\n---\n" not in candidate_content):
            raise TaskError("AS candidate lacks a versioned concept header")
        concept = yaml.safe_load(candidate_content.split("\n---\n", 1)[0][4:])
        if (not isinstance(concept, dict)
                or concept.get("type") != "Architecture Statement"
                or concept.get("status") != "draft"
                or not concept.get("id")):
            raise TaskError("AS review requires a draft Architecture Statement concept")
    if trigger["kind"] == "AS_REVIEW_REVISION_REQUIRED":
        if operation != "REVISE_AS" or trigger_path is None or trigger_path.suffix != ".json":
            raise TaskError("AS correction after review requires REVISE_AS and independent JSON review")
        review = json.loads(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(review, dict)
                or review.get("schema") != "pc-as-review/v1"
                or review.get("gate") != "AS_REVIEW"
                or review.get("disposition") != "REVISE"
                or (review.get("gate_status") != "AS_REVISION_REQUIRED"
                    and review.get("next_stage_recommendation") != "AS_REVISION_REQUIRED")
                or review.get("independent_of_authoring_invocation") is not True
                or not any(isinstance(f, dict) and f.get("severity") == "blocking"
                           for f in review.get("findings", []))):
            raise TaskError("AS correction lacks independent blocking review finding")
    if trigger["kind"] == "AS_SCOPE_CORRECTION_APPROVED":
        if trigger_path is None or trigger_path.suffix not in (".yaml", ".yml"):
            raise TaskError("Protected AS revision requires a YAML authority record")
        accepted = yaml.safe_load(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(accepted, dict)
                or accepted.get("schema") != "pc-as-authority/v1"
                or accepted.get("status") != "approved"
                or accepted.get("decision") != "APPROVE_SCOPED_AS_REVISION"
                or accepted.get("authorizes") != "VERSIONED_AS_VP_VO_CORRECTION_FOR_INDEPENDENT_REVIEW"
                or not accepted.get("approved_by")
                or not accepted.get("source_request")
                or not accepted.get("independent_scope_review")
                or not accepted.get("authority_evidence")
                or not isinstance(accepted.get("accepted_scope"), dict)):
            raise TaskError("Protected AS revision is missing explicit accepted scope authority")
        inputs = data.get("context", {}).get("authority_inputs", {})
        if (not isinstance(inputs, dict)
                or inputs.get("accepted_scope") != trigger["reference"]):
            raise TaskError("AS revision manifest must identify exact accepted scope receipt")
        _file(root, accepted["source_request"], "process/decisions")
        _file(root, accepted["independent_scope_review"], "reviews")
        evidence = _file(root, accepted["authority_evidence"], "process/decisions")
        if evidence.suffix != ".md":
            raise TaskError("AS scope authority evidence must be Markdown")
        if (accepted["accepted_scope"].get("fixed_1ms_requirement")
                != "superseded_subject_to_versioned_AS_review"
                or accepted["accepted_scope"].get("publisher_responsibility")
                != "uninterrupted_ordered_sample_delivery"):
            raise TaskError("AS scope authority does not match approved producer boundary")
    if trigger["kind"] == "BASELINE_RECONCILIATION_REQUESTED":
        if operation != "REVIEW_BASELINE" or trigger_path is None or trigger_path.suffix not in (".yaml", ".yml"):
            raise TaskError("Baseline review requires REVIEW_BASELINE and a YAML package")
        candidate = yaml.safe_load(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(candidate, dict)
                or candidate.get("schema") != "pc-baseline-candidate/v1"
                or candidate.get("status") != "pending_independent_baseline_review"
                or candidate.get("review_required_before_activation") is not True):
            raise TaskError("Baseline candidate is not pending independent review")
        inputs = data.get("context", {}).get("authority_inputs", {})
        if (not isinstance(inputs, dict)
                or inputs.get("baseline_candidate") != trigger["reference"]):
            raise TaskError("Task and baseline authority references disagree")
        authority = candidate.get("authority", {})
        if not isinstance(authority, dict):
            raise TaskError("Baseline lacks source authority")
        ap_path = _file(root, authority.get("provisional_ap"), "process/decisions")
        scope_path = _file(root, authority.get("scope"), "process/decisions")
        ap = yaml.safe_load(ap_path.read_text(encoding="utf-8"))
        scope = yaml.safe_load(scope_path.read_text(encoding="utf-8"))
        if (not isinstance(ap, dict) or ap.get("status") != "approved"
                or ap.get("decision") != "PROVISIONALLY_SELECTED"
                or ap.get("authorizes") != "CON_FIRST_DECOMPOSITION_AFTER_BASELINE_RECONCILIATION"
                or not ap.get("authority_evidence")
                or not isinstance(scope, dict) or scope.get("status") != "approved"):
            raise TaskError("Baseline does not have accepted scope and AP authority")
        _file(root, ap["authority_evidence"], "process/decisions")
        as_path = candidate.get("candidate_active_as")
        vp_path = candidate.get("candidate_active_verification_plan")
        vo_path = candidate.get("candidate_active_vo_004")
        for candidate_path in (as_path, vp_path, vo_path):
            _file(root, candidate_path, "knowledge")
        if candidate.get("effective_relation_overrides"):
            # Baseline projection must be deterministic and backed by the
            # accepted review. Do not rewrite historical OKF relations.
            from baseline_relations import BaselineRelationError, resolve
            try:
                resolve(root, trigger["reference"])
            except BaselineRelationError as exc:
                raise TaskError("Invalid effective baseline relations: " + str(exc)) from exc
        review_ref = candidate.get("independent_as_review", {}).get("receipt")
        review = json.loads(_file(root, review_ref, "reviews").read_text(encoding="utf-8"))
        if (not isinstance(review, dict) or review.get("gate") != "AS_REVIEW"
                or review.get("independent_of_authoring_invocation") is not True
                or review.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")):
            raise TaskError("Baseline lacks favorable independent AS review")
        reviewed = {x.get("path") for x in review.get("candidate_artifacts", [])
                    if isinstance(x, dict)}
        if not {as_path, vp_path, vo_path}.issubset(reviewed):
            raise TaskError("Baseline references artifacts not in independent AS review")
        ledger_path = candidate.get("candidate_active_vo_ledger")
        proposed = yaml.safe_load(_file(root, ledger_path, "process/ledgers").read_text(encoding="utf-8"))
        if (not isinstance(proposed, dict) or proposed.get("status") != "pending_independent_baseline_review"
                or not isinstance(proposed.get("obligations"), list)):
            raise TaskError("Baseline VO ledger proposal is missing or not pending")
        original = yaml.safe_load(_file(root, proposed.get("base_ledger"), "process/ledgers").read_text(encoding="utf-8"))
        if not isinstance(original, dict) or not isinstance(original.get("obligations"), list):
            raise TaskError("Original VO ledger is missing")
        orig = {x["id"]: x for x in original["obligations"] if isinstance(x, dict) and x.get("id")}
        dest = {x["id"]: x for x in proposed["obligations"] if isinstance(x, dict) and x.get("id")}
        if len(orig) != len(original["obligations"]) or len(dest) != len(proposed["obligations"]) or set(orig) != set(dest):
            raise TaskError("Baseline must preserve every VO identity without duplicates")
        authorized = {x["id"]: x for x in ap.get("authorized_vo_supersessions", [])
                      if isinstance(x, dict) and x.get("id")}
        for vid in orig:
            old, new = orig[vid], dest[vid]
            if (new.get("state") != old.get("state")
                    or new.get("evidence_receipt") != old.get("evidence_receipt")
                    or new.get("requirement") != old.get("requirement")
                    or new.get("owner") != old.get("owner")):
                raise TaskError("Baseline attempts to change VO authority or discharge: " + vid)
            if new.get("due_stage") != old.get("due_stage"):
                change = authorized.get(vid)
                if (not change or change.get("from_due_stage") != old.get("due_stage")
                        or change.get("to_due_stage") != new.get("due_stage")
                        or change.get("preserved_state") != new.get("state")):
                    raise TaskError("Baseline changes VO due stage without explicit authority: " + vid)
    if trigger["kind"] == "BASELINE_ACTIVATED":
        if operation != "DEFINE_CON" or trigger_path is None or trigger_path.suffix not in (".yaml", ".yml"):
            raise TaskError("Active-baseline contract authoring requires DEFINE_CON and a YAML active baseline")
        inputs = data.get("context", {}).get("authority_inputs", {})
        if not isinstance(inputs, dict) or inputs.get("active_baseline") != trigger["reference"]:
            raise TaskError("CON authoring manifest does not identify exact active baseline")
        from active_baseline import ActiveBaselineError, verify
        try:
            active_check = verify(root, trigger["reference"])
        except (ActiveBaselineError, OSError, ValueError, KeyError) as exc:
            raise TaskError("CON authoring blocked by invalid active baseline: " + str(exc)) from exc
        if inputs.get("vo_ledger") != active_check["vo_ledger"]:
            raise TaskError("CON authoring must consume active reviewed VO ledger")
        if inputs.get("architecture_statement") != active_check["architecture"]:
            raise TaskError("CON authoring must consume active reviewed AS")
        if inputs.get("verification_plan") != active_check["verification_plan"]:
            raise TaskError("CON authoring must consume active reviewed VP")
    if trigger["kind"] == "AP_PROVISIONALLY_SELECTED":
        if trigger_path is None or trigger_path.suffix not in (".yaml", ".yml"):
            raise TaskError("Protected AP selection requires a YAML authority record")
        authority = yaml.safe_load(trigger_path.read_text(encoding="utf-8"))
        if (not isinstance(authority, dict) or authority.get("status") != "approved"
                or authority.get("decision") != "PROVISIONALLY_SELECTED"
                or not authority.get("selected_candidate")
                or authority.get("authorizes") != "CON_FIRST_DECOMPOSITION"
                or not authority.get("approved_by")
                or not authority.get("authority_evidence")):
            raise TaskError("Protected AP selection is missing accepted authority")
        proof_path = _file(root, authority["authority_evidence"])
        if proof_path.suffix != ".md":
            raise TaskError("Authority evidence must be a reviewable Markdown decision")
        inputs = data.get("context", {}).get("authority_inputs", {})
        if not isinstance(inputs, dict) or inputs.get("accepted_selection") != trigger["reference"]:
            raise TaskError("Task authority_inputs must identify the selected AP receipt")
        debt_record = inputs.get("ad_ledger")
        if not isinstance(debt_record, str):
            raise TaskError("Protected selection requires the applicable AD ledger")
        debts = yaml.safe_load(_file(root, debt_record).read_text(encoding="utf-8"))
        debt_map = {d.get("id"): d for d in debts.get("items", []) if isinstance(d, dict)} if isinstance(debts, dict) else {}
        for debt_id in authority.get("accepted_architectural_debt", []):
            debt = debt_map.get(debt_id)
            if not debt or debt.get("state") != "accepted" or debt.get("accepted_decision") != trigger["reference"]:
                raise TaskError("Selection references unaccepted architectural debt: " + str(debt_id))
        vo_record = inputs.get("vo_ledger")
        if not isinstance(vo_record, str):
            raise TaskError("Protected selection requires the applicable VO ledger")
        vo_doc = yaml.safe_load(_file(root, vo_record).read_text(encoding="utf-8"))
        vo_map = {v.get("id"): v for v in vo_doc.get("obligations", []) if isinstance(v, dict)} if isinstance(vo_doc, dict) else {}
        for vo_id in authority.get("carried_verification_obligations", []):
            vo = vo_map.get(vo_id)
            if vo is None or vo.get("state") != "open":
                raise TaskError("Selected AP must carry an open verification obligation: " + str(vo_id))
    outputs = data.get("outputs")
    if not isinstance(outputs, dict) or not isinstance(outputs.get("allowed"), list) or not outputs["allowed"]:
        raise TaskError("Task requires nonempty outputs.allowed")
    gate = data.get("gate")
    if not isinstance(gate, dict) or not isinstance(gate.get("kind"), str):
        raise TaskError("Task gate.kind required")
    if gate.get("on_missing_evidence") != "UNRESOLVED":
        raise TaskError("Missing evidence must be UNRESOLVED")

    return {
        "id": task_id, "role": role, "operation": operation,
        "manifest": manifest_file.relative_to(root).as_posix(),
        "spine": spine_ref,
        "playbook": playbook.relative_to(root).as_posix(),
        "gate": gate["kind"],
        "trigger": trigger["kind"],
    }


def make_prompt(root: Path, task: dict) -> str:
    generic = _file(root, "prompts/generic-task.md").read_text(encoding="utf-8")
    preface = (
        "# Assigned task manifest\n\n"
        f"- Task ID: {task['id']}\n"
        f"- Manifest: {task['manifest']}\n"
        f"- Role: {task['role']}\n"
        f"- Operation: {task['operation']}\n"
        f"- Architecture spine: {task['spine']}\n"
        f"- Playbook: {task['playbook']}\n\n"
        "The manifest and accepted repository artifacts control this run. "
        "Do not infer authority from this prompt.\n\n---\n\n"
    )
    return preface + generic


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect", "render", "run"))
    parser.add_argument("--manifest", required=True, help="Path under process/tasks/")
    args = parser.parse_args(argv)
    try:
        task = validate(ROOT, args.manifest)
    except (TaskError, OSError, yaml.YAMLError) as exc:
        print("TASK_INVALID:", exc, file=sys.stderr)
        return 2
    if args.command == "inspect":
        print(json.dumps(task, indent=2))
        return 0
    prompt = make_prompt(ROOT, task)
    if args.command == "render":
        sys.stdout.write(prompt)
        return 0
    outdir = ROOT / "runs" / "task-prompts"
    outdir.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", prefix=task["id"] + "-",
        suffix=".md", dir=outdir, delete=False
    ) as handle:
        handle.write(prompt)
        task_prompt = Path(handle.name)
    print(f"TASK={task['id']} MANIFEST={task['manifest']} ROLE={task['role']}", flush=True)
    return subprocess.run(
        [sys.executable, str(ROOT / "tools/telemetry.py"),
         "run", "--role", task["role"], "--prompt", str(task_prompt),
         "--label", task["id"]],
        cwd=ROOT, check=False
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
