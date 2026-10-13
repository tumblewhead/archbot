#!/usr/bin/env python3
"""Create the next task manifest from a versioned workflow receipt.

This plans work. It never runs an agent, approves a gate, or modifies evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


class LoopError(ValueError):
    pass


def source(root: Path, name: str, directory: str) -> Path:
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise LoopError("Expected a relative repository path")
    path = (root / name).resolve()
    if not path.is_relative_to((root / directory).resolve()) or not path.is_file():
        raise LoopError("Missing or out-of-scope path: " + name)
    return path


def yaml_doc(path: Path) -> dict:
    obj = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise LoopError("Expected YAML mapping")
    return obj


def concept_type(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text:
        raise LoopError("Invalid OKF concept: " + str(path))
    meta = yaml.safe_load(text.split("\n---\n", 1)[0][4:])
    if not isinstance(meta, dict):
        raise LoopError("Invalid OKF frontmatter")
    return meta.get("type", "")


def decision(root: Path, ref: str) -> dict:
    receipt_path = source(root, ref, "reviews")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LoopError("Invalid JSON receipt") from exc
    if not isinstance(receipt, dict):
        raise LoopError("Invalid receipt")
    ident = receipt.get("task_id")
    if not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", ident):
        raise LoopError("Receipt must name the source task_id")
    task_ref = "process/tasks/" + ident + ".yaml"
    prior = yaml_doc(source(root, task_ref, "process/tasks"))
    if prior.get("id") != ident:
        raise LoopError("Receipt and source task do not correspond")
    rules = yaml_doc(source(root, "process/loop_transitions.yaml", "process"))
    matched = [
        t for t in rules.get("transitions", [])
        if t.get("receipt_schema") == receipt.get("schema")
        and all(receipt.get(k) == v for k, v in t.get("requires", {}).items())
        and (not t.get("require_blocking_finding")
             or any(isinstance(f, dict) and f.get("severity") == "blocking"
                    for f in receipt.get("findings", [])))
    ]
    if len(matched) != 1:
        raise LoopError("No unique permissible transition for this receipt")
    rule = matched[0]
    operations = yaml_doc(source(root, "process/operations.yaml", "process"))
    op = operations.get("operations", {}).get(rule["operation"])
    if not isinstance(op, dict):
        raise LoopError("Next operation is not registered")
    source(root, op["playbook"], "process/playbooks")
    contracts = []
    if rule["target"] == "receipt":
        trigger_ref = ref
    elif rule["target"] == "changed_contract_spine":
        spines = []
        for filename in receipt.get("changed_artifacts", []):
            if not isinstance(filename, str) or not filename.startswith("knowledge/") or not filename.endswith(".md"):
                continue
            ctype = concept_type(source(root, filename, "knowledge"))
            if ctype == "Contract Spine":
                spines.append(filename)
            elif ctype == "Design Contract":
                contracts.append(filename)
        if len(spines) != 1 or not contracts:
            raise LoopError("Submission must identify one new Contract Spine and its contracts")
        trigger_ref = spines[0]
    else:
        raise LoopError("Unknown transition target")

    existing = []
    for filename in (root / "process/tasks").glob("*.yaml"):
        item = yaml_doc(filename)
        trigger = item.get("trigger", {})
        if (item.get("operation") == rule["operation"] and isinstance(trigger, dict)
                and trigger.get("kind") == rule["trigger_kind"]
                and trigger.get("reference") == trigger_ref):
            existing.append(filename.relative_to(root).as_posix())
    if len(existing) > 1:
        raise LoopError("Conflicting existing task manifests")
    digest = hashlib.sha256(
        (rule["id"] + "\n" + ref + "\n" + receipt_path.read_text(encoding="utf-8")).encode("utf-8")
    ).hexdigest()[:12]
    next_id = rule["operation"] + "-" + digest
    next_path = "process/tasks/" + next_id + ".yaml"
    context = {
        "selection": "role_policy",
        "mandatory_dependency_closure": True,
        "include_raw_data_by_default": False,
        "workflow_provenance": {
            "transition": rule["id"], "receipt": ref,
            "source_task_manifest": task_ref,
            "source_revision": receipt.get("input_revision"),
        },
    }
    if rule["target"] == "receipt":
        context["review_inputs"] = {
            "independent_review": ref,
            "finding_ids": [f["id"] for f in receipt.get("findings", [])
                            if isinstance(f, dict) and f.get("severity") in ("blocking", "unresolved")
                            and isinstance(f.get("id"), str)],
            "prior_task_context": prior.get("context", {}),
        }
    else:
        context["authority_inputs"] = {
            "contract_spine": trigger_ref, "current_contracts": contracts,
            "submission_receipt": ref, "prior_task_context": prior.get("context", {}),
        }
    manifest = {
        "schema": "pc-task/v1", "id": next_id, "role": op["role"],
        "operation": rule["operation"], "spine": prior["spine"],
        "trigger": {"kind": rule["trigger_kind"], "reference": trigger_ref,
                    "revision": receipt.get("input_revision") or "recorded_in_receipt"},
        "playbook": op["playbook"], "context": context,
        "outputs": {
            "allowed": ["new_versioned_stage_artifact", "review_receipt", "finding_resolution"],
            "prohibited": ["overwrite_accepted_artifacts", "approve_own_gate",
                           "modify_approved_AS_AP_or_F", "discharge_VO",
                           "accept_AD", "implement_firmware"],
        },
        "gate": {"kind": rule["gate"], "on_missing_evidence": "UNRESOLVED",
                 "require_independent_review": True},
    }
    return {"status": "ALREADY_PLANNED" if existing else "NEW",
            "path": existing[0] if existing else next_path,
            "manifest": manifest, "transition": rule["id"]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("inspect", "emit"))
    ap.add_argument("--receipt", required=True)
    args = ap.parse_args()
    try:
        result = decision(ROOT, args.receipt)
        if args.command == "emit" and result["status"] == "NEW":
            target = ROOT / result["path"]
            with target.open("x", encoding="utf-8") as out:
                yaml.safe_dump(result["manifest"], out, sort_keys=False)
        print(json.dumps(result if args.command == "inspect" else {
            "status": result["status"], "manifest_path": result["path"],
            "transition": result["transition"]}, indent=2))
    except (LoopError, OSError, KeyError, TypeError, yaml.YAMLError) as exc:
        print("LOOP_BLOCKED:", exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
