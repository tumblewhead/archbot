"""Verification slice VK-001: explicit inputs -> ERS -> plan -> model evidence.

The kernel checks provenance and result scope. It does not formalize arbitrary
English, prove backend soundness, accept its own artifacts, or close product VOs.
Project use is gated by real independent review records. Fixture use is isolated.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import sys
import tempfile

from verification_models import ModelError, evaluate

SCHEMA = "pc-verification/v1"
INPUT_SCHEMA = "pc-verification-input/v1"
AUTHORS = {"DERIVE_ERS": "ERS", "DESIGN_VERIFICATION_LADDER": "PLAN",
           "EXECUTE_VERIFICATION_LADDER": "EVIDENCE"}
REVIEWS = {"REVIEW_ERS": "ERS", "REVIEW_VERIFICATION_LADDER": "PLAN",
           "REVIEW_VERIFICATION_RUNG": "EVIDENCE"}
REVIEW_FOR = {value: key for key, value in REVIEWS.items()}
OPERATIONS = set(AUTHORS) | set(REVIEWS)
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,100}$")
HASH = re.compile(r"^[0-9a-f]{64}$")
ROOT = Path(__file__).resolve().parents[1]


class VerificationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def object_(value, name):
    require(isinstance(value, dict), name + " must be an object")
    return value


def array(value, name, nonempty=False):
    require(isinstance(value, list) and (bool(value) or not nonempty), name + " must be a list")
    return value


def ident(value, name="id"):
    require(isinstance(value, str) and bool(ID.fullmatch(value)), "Invalid " + name)
    return value


def canonical(value):
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                          allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise VerificationError("Object is not finite JSON") from exc


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_path(root, ref, prefix=None, exists=True):
    require(isinstance(ref, str) and ref and not Path(ref).is_absolute(),
            "Repository-relative path required")
    require(".." not in Path(ref).parts, "Parent traversal forbidden")
    base = root.resolve() if prefix is None else (root / prefix).resolve()
    require(base.is_relative_to(root.resolve()), "Authorized directory escapes repository")
    target = (root / ref).resolve()
    require(target.is_relative_to(base), "Path escapes authorized directory: " + ref)
    if exists:
        require(target.is_file(), "Missing input: " + ref)
        require(target.stat().st_size <= 2000000, "Input exceeds bounded reader limit: " + ref)
    return target


def _unique(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise VerificationError("Duplicate JSON key: " + key)
        obj[key] = value
    return obj


def load(root, ref, prefix=None):
    try:
        data = json.loads(safe_path(root, ref, prefix).read_text(encoding="utf-8"),
                          object_pairs_hook=_unique,
                          parse_constant=lambda value: (_ for _ in ()).throw(
                              VerificationError("Nonfinite JSON: " + value)))
        return object_(data, ref)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError("Invalid JSON: " + ref) from exc


def check_pins(root, pins):
    object_(pins, "source_sha256")
    require(bool(pins), "At least one source pin is required")
    for ref, sha in pins.items():
        require(isinstance(sha, str) and HASH.fullmatch(sha), "Invalid source SHA-256")
        require(file_hash(safe_path(root, ref)) == sha, "Stale source: " + ref)


def pin(root, ref):
    return {"path": ref, "sha256": file_hash(safe_path(root, ref))}


def read_pin(root, pointer):
    object_(pointer, "artifact pointer")
    path = pointer.get("path")
    expected = pointer.get("sha256")
    require(file_hash(safe_path(root, path)) == expected, "Artifact pointer is stale")
    return load(root, path)


def project_fields(doc):
    ident(doc.get("project_id"), "project_id")
    require(isinstance(doc.get("spine"), str) and doc["spine"].startswith("/"),
            "Knowledge-root spine required")
    object_(doc.get("subject"), "subject")
    for key in ("id", "semantics", "scope"):
        require(isinstance(doc["subject"].get(key), str) and doc["subject"][key],
                "Subject needs " + key)


def validate_package(root, package, fixture=False):
    require(package.get("schema") == INPUT_SCHEMA, "Wrong input package schema")
    project_fields(package)
    require(package.get("mode") == ("FIXTURE" if fixture else "PROJECT"),
            "Fixture/project isolation violation")
    safe_path(root, "knowledge/" + package["spine"].lstrip("/"), "knowledge")
    check_pins(root, package.get("source_sha256"))
    requirements = array(package.get("requirements"), "requirements", True)
    claims = array(package.get("claims"), "claims", True)
    reqs, ids = {}, set()
    for req in requirements:
        object_(req, "requirement")
        rid = ident(req.get("id"), "requirement id")
        require(rid not in reqs, "Duplicate requirement id")
        require(req.get("source") in package["source_sha256"], "Requirement source is unpinned")
        require(isinstance(req.get("selector"), str) and req["selector"], "Requirement selector missing")
        require(isinstance(req.get("statement"), str) and req["statement"], "Requirement statement missing")
        source_text = safe_path(root, req["source"]).read_text(encoding="utf-8")
        require(req["selector"] in source_text, "Requirement selector absent from source")
        reqs[rid] = req
    covered = set()
    for claim in claims:
        object_(claim, "claim")
        cid = ident(claim.get("id"), "claim id")
        require(cid not in ids, "Duplicate claim id")
        ids.add(cid)
        rid = claim.get("requirement_id")
        require(rid in reqs, "Orphan claim: " + cid)
        require(claim.get("statement") == reqs[rid]["statement"],
                "Normative claim changed while projecting requirement: " + cid)
        require(claim.get("quantifier") in ("universal", "finite", "statistical"), "Claim quantifier missing")
        for field in ("domain", "horizon", "due_stage", "owner"):
            require(isinstance(claim.get(field), str) and claim[field], "Claim needs " + field)
        array(claim.get("assumptions"), "assumptions")
        covered.add(rid)
    require(covered == set(reqs), "Source obligation missing from ERS projection")
    # Observations are explicitly separate annotations, not normative authority.
    observed = array(package.get("observed_requirement_ids", []), "observed_requirement_ids")
    require(all(x in reqs for x in observed), "Observation names unknown obligation")
    array(package.get("rungs"), "rungs")
    array(package.get("non_claims"), "non_claims", True)
    if not fixture:
        baseline = package.get("active_baseline")
        review_ref = package.get("implementation_review")
        require(baseline in package["source_sha256"] and review_ref in package["source_sha256"],
                "Project input needs pinned active baseline and implementation review")
        from active_baseline import verify
        verify(root, baseline)
        review = load(root, review_ref, "reviews")
        require(review.get("schema") == "pc-implementation-review/v1"
                and review.get("gate") == "IMPLEMENTATION_REVIEW"
                and review.get("disposition") in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
                and review.get("independent_of_authoring_invocation") is True,
                "No favorable independent implementation review")
        reviewed = object_(review.get("reviewed_source_sha256"), "reviewed sources")
        require(bool(reviewed), "Implementation review has no source pins")
        for ref, sha in reviewed.items():
            require(package["source_sha256"].get(ref) == sha,
                    "Implementation sources do not match reviewed subject")
    return package


def envelope(package, kind, task_id, inputs, payload):
    doc = {"schema": SCHEMA, "kind": kind, "project_id": package["project_id"],
           "spine": package["spine"], "subject": copy.deepcopy(package["subject"]),
           "mode": package["mode"], "task_id": ident(task_id),
           "source_sha256": dict(inputs), "review_state": "PENDING",
           "product_verified": False, "vo_discharged": [], "payload": payload}
    doc["content_sha256"] = digest(doc)
    return doc


def check_artifact(root, doc, kind=None, fixture=False):
    require(doc.get("schema") == SCHEMA and doc.get("kind") in ("ERS", "PLAN", "EVIDENCE"),
            "Not a verification artifact")
    if kind is not None:
        require(doc["kind"] == kind, "Wrong artifact stage")
    project_fields(doc)
    require(doc.get("mode") == ("FIXTURE" if fixture else "PROJECT"), "Fixture/project isolation violation")
    require(doc.get("review_state") == "PENDING" and doc.get("product_verified") is False
            and doc.get("vo_discharged") == [], "Authoring artifact claims unauthorized acceptance")
    material = {k: v for k, v in doc.items() if k != "content_sha256"}
    require(doc.get("content_sha256") == digest(material), "Artifact content digest mismatch")
    check_pins(root, doc.get("source_sha256"))
    return doc


def derive(root, package, task_id, inputs, fixture=False):
    validate_package(root, package, fixture)
    covered = set(package.get("observed_requirement_ids", []))
    gaps = [r["id"] for r in package["requirements"] if r["id"] not in covered]
    return envelope(package, "ERS", task_id, inputs, {
        "requirements": copy.deepcopy(package["requirements"]),
        "claims": copy.deepcopy(package["claims"]),
        "implementation_observation_gaps": gaps,
        "observation_status": "ANNOTATIONS_NOT_SEMANTIC_CODE_PROOF",
        "candidate_rungs": copy.deepcopy(package["rungs"]),
        "open_obligations": copy.deepcopy(package.get("open_obligations", [])),
        "non_claims": copy.deepcopy(package["non_claims"]),
        "questions": copy.deepcopy(package.get("questions", [])),
        "coverage_limit": "Complete only against the declared obligation inventory; independent source review required.",
    })


def order_rungs(rungs, claims):
    by_id = {}
    require(len(array(rungs, "rungs")) <= 32, "VK-001 supports at most 32 rungs per plan")
    for rung in rungs:
        object_(rung, "rung")
        rid = ident(rung.get("id"), "rung id")
        require(rid not in by_id, "Duplicate rung id")
        require(rung.get("claim_id") in claims, "Rung names unknown claim")
        for field in ("theme", "method", "reason", "model_scope"):
            require(isinstance(rung.get(field), str) and rung[field], "Rung needs " + field)
        require(rung.get("binding") == "MODEL_ONLY", "Only explicit model-only adapters are supported in VK-001")
        require(rung.get("maximum_conclusion") == "MODEL_EVIDENCE", "Unsupported conclusion strength")
        object_(rung.get("parameters"), "parameters")
        budget = rung.get("max_cases")
        require(type(budget) is int and 1 <= budget <= 1000000, "Invalid rung budget")
        array(rung.get("scheduled_after_result", []), "scheduling dependencies")
        for dep in array(rung.get("requires_established_claim", []), "premise dependencies"):
            object_(dep, "premise")
            require(isinstance(dep.get("rung_id"), str) and dep.get("evidence_kind") == "FINITE_MODEL_CHECK",
                    "Unsupported premise rule; VK-001 only admits exact finite-model checks")
            require(isinstance(dep.get("model_sha256"), str) and HASH.fullmatch(dep["model_sha256"]),
                    "Premise requires an exact model fingerprint")
        array(rung.get("hyperedges", []), "hyperedges")
        for edge in rung.get("hyperedges", []):
            object_(edge, "hyperedge")
            require(len(array(edge.get("parameters"), "edge parameters", True)) >= 2,
                    "Interaction needs at least two parameters")
            require(all(x in rung["parameters"] for x in edge["parameters"]), "Unknown interaction parameter")
            for field in ("formula", "admissibility", "origin"):
                require(isinstance(edge.get(field), str) and edge[field], "Hyperedge needs " + field)
        by_id[rid] = rung
    require(sum(r["max_cases"] for r in rungs) <= 1000000, "Total plan budget exceeds VK-001 limit")
    for rung in rungs:
        for dep in rung.get("requires_established_claim", []):
            source = by_id.get(dep["rung_id"])
            require(source is not None, "Missing premise source")
            require(dep["model_sha256"] == digest({"method": source["method"], "parameters": source["parameters"]}),
                    "Premise scope/model fingerprint mismatch")
    ordered, pending = [], dict(by_id)
    while pending:
        ready = []
        for rid, rung in pending.items():
            deps = list(rung.get("scheduled_after_result", [])) + [d["rung_id"] for d in rung.get("requires_established_claim", [])]
            require(all(d in by_id and d != rid for d in deps), "Missing or self-referential rung dependency")
            if all(d in ordered for d in deps):
                ready.append(rid)
        require(bool(ready), "Rung dependency cycle")
        for rid in sorted(ready):
            ordered.append(rid)
            del pending[rid]
    return ordered


def plan(root, ers, task_id, inputs, fixture=False):
    check_artifact(root, ers, "ERS", fixture)
    payload = ers["payload"]
    claims = {x["id"]: x for x in payload["claims"]}
    rungs = copy.deepcopy(payload["candidate_rungs"])
    ordered = order_rungs(rungs, claims)
    targeted = {x["claim_id"] for x in rungs}
    return envelope(ers, "PLAN", task_id, inputs, {
        "claims": copy.deepcopy(payload["claims"]), "rungs": rungs, "order": ordered,
        "unplanned_claim_ids": sorted(set(claims)-targeted),
        "open_obligations": copy.deepcopy(payload["open_obligations"]),
        "non_claims": copy.deepcopy(payload["non_claims"]),
        "questions": copy.deepcopy(payload["questions"]),
        "planning_method": "validated hand-authored candidates; no automatic model discovery",
    })


def execute(root, planned, task_id, inputs, fixture=False):
    check_artifact(root, planned, "PLAN", fixture)
    p = planned["payload"]
    claims = {x["id"]: x for x in p["claims"]}
    ordered = order_rungs(p["rungs"], claims)
    require(ordered == p["order"], "Plan order differs from validated dependency order")
    indexed = {x["id"]: x for x in p["rungs"]}
    results = {}
    for rid in ordered:
        rung = indexed[rid]
        unmet = [dep for dep in rung.get("requires_established_claim", [])
                 if results[dep["rung_id"]]["evidence_kind"] != dep["evidence_kind"]]
        if unmet:
            raw = {"execution_status": "BLOCKED_PREMISE", "evidence_kind": "NOT_ESTABLISHED",
                   "details": {"unmet": unmet}, "counterexample": None,
                   "limitations": ["Scheduling after a result is different from relying on it as a premise."],
                   "product_verified": False}
        else:
            try:
                raw = evaluate(rung["method"], rung["parameters"], rung["max_cases"])
            except ModelError as exc:
                raw = {"execution_status": "MODEL_INVALID", "evidence_kind": "NOT_ESTABLISHED",
                       "details": {"error": str(exc)}, "counterexample": None,
                       "limitations": ["Invalid model is not evidence against the product."],
                       "product_verified": False}
        raw.update({"rung_id": rid, "claim_id": rung["claim_id"],
                    "model_scope": rung["model_scope"], "binding": "MODEL_ONLY",
                    "model_sha256": digest({"method": rung["method"], "parameters": rung["parameters"]}),
                    "requested_claim_status": "NOT_DISCHARGED",
                    "why_run": rung["reason"]})
        results[rid] = raw
    return envelope(planned, "EVIDENCE", task_id, inputs, {
        "claims": copy.deepcopy(p["claims"]), "results": list(results.values()),
        "open_obligations": copy.deepcopy(p["open_obligations"]),
        "non_claims": copy.deepcopy(p["non_claims"]), "questions": copy.deepcopy(p["questions"]),
        "runtime": {"python": platform.python_version(), "platform": platform.platform(),
                    "entrypoint": "verification_kernel.execute",
                    "process_argv": list(sys.argv)},
        "trusted_boundary": "Hand-authored input interpretation and Python reference adapters; not proof certificates or project C.",
    })


def briefing(doc):
    lines = [f"# {doc['kind']} engineering briefing", "",
             f"Project: `{doc['project_id']}` | Task: `{doc['task_id']}`", "",
             f"**Subject:** {doc['subject']['id']}",
             f"**Scope:** {doc['subject']['scope']}",
             "**Authority:** draft, independent review pending; no product verification or VO discharge.", ""]
    p = doc["payload"]
    if doc["kind"] == "ERS":
        lines += ["## What changed", f"Projected {len(p['claims'])} claims from the explicit source inventory.",
                  "The code-observation annotations were kept separate from normative statements.",
                  "", "## What needs attention", "Unconfirmed implementation annotations: " +
                  (", ".join(p["implementation_observation_gaps"]) or "none in this inventory"),
                  p["coverage_limit"]]
    elif doc["kind"] == "PLAN":
        lines += ["## What changed", f"Validated {len(p['rungs'])} hand-authored model rungs and their dependency graph.",
                  "Scheduling after failure does not establish a logical premise.",
                  "", "## What remains open", "Claims without a planned method: " +
                  (", ".join(p["unplanned_claim_ids"]) or "none in this inventory"),
                  "Model rungs do not establish product correspondence."]
    else:
        lines += ["## Outcomes"]
        for item in p["results"]:
            lines += [f"### {item['rung_id']}: {item['evidence_kind']}",
                      f"Execution: {item['execution_status']}. Scope: {item['model_scope']}.",
                      item["why_run"], "```json", json.dumps(item["details"], indent=2), "```",
                      *item["limitations"], ""]
        lines += ["A failed model or counterexample is a scoped finding, not an automatically diagnosed product defect."]
    lines += ["", "## Questions for the engineer", *(p.get("questions") or ["No new question from this stage."]),
              "", "## Non-claims", *p["non_claims"], "", "## Next action",
              "Independent review of this exact artifact. Preserve open obligations: " +
              (", ".join(p["open_obligations"]) or "none declared"), ""]
    return "\n".join(lines)


def _yaml(root, ref):
    import yaml
    return object_(yaml.safe_load(safe_path(root, ref).read_text(encoding="utf-8")), ref)


def input_for_task(root, task):
    """Single stage-input protocol for all six registered operations."""
    op = task.get("operation")
    require(op in OPERATIONS, "Not a VK-001 operation")
    require(task.get("trigger", {}).get("kind") == "VERIFICATION_INPUT", "Wrong verification trigger")
    ref = task["trigger"].get("reference")
    incoming = load(root, ref)
    if op == "DERIVE_ERS":
        validate_package(root, incoming)
        require(incoming["spine"] == task["spine"], "Cross-project task input")
        return incoming, {**incoming["source_sha256"], ref: file_hash(safe_path(root, ref))}
    require(incoming.get("schema") == SCHEMA, "Wrong stage receipt schema")
    require(incoming.get("mode") == "PROJECT" and incoming.get("spine") == task["spine"],
            "Cross-project or fixture receipt")
    document = read_pin(root, incoming.get("artifact"))
    expected = REVIEWS.get(op) or ("ERS" if op == "DESIGN_VERIFICATION_LADDER" else "PLAN")
    check_artifact(root, document, expected)
    require(document["project_id"] == incoming.get("project_id") and document["spine"] == task["spine"],
            "Receipt/artifact project mismatch")
    require(document["subject"] == incoming.get("subject"), "Receipt/artifact subject mismatch")
    if op in REVIEWS:
        require(incoming.get("kind") == "SUBMISSION" and incoming.get("gate_status") == "DRAFT_READY",
                "Reviewer needs a draft submission")
        require(incoming.get("task_id") == document["task_id"], "Submission author mismatch")
    else:
        require(incoming.get("kind") == "REVIEW" and incoming.get("operation") == REVIEW_FOR[expected],
                "Expected independent review of preceding stage")
        require(incoming.get("vo_discharged", []) == [] and incoming.get("product_verified", False) is False,
                "Stage review may not claim product acceptance or VO discharge")
        require(incoming.get("disposition") in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS"),
                "Preceding stage was not accepted")
        require(incoming.get("independent_of_authoring_invocation") is True
                and incoming.get("reviewed_author_task_id") == document["task_id"]
                and incoming.get("task_id") != document["task_id"], "Review independence/reference missing")
        require(isinstance(incoming.get("reviewer_invocation_id"), str) and incoming["reviewer_invocation_id"],
                "Review invocation identity missing")
        findings = array(incoming.get("findings"), "findings")
        require(not any(object_(f, "finding").get("severity") == "blocking" for f in findings),
                "Accepted review still contains a blocker")
        rid = ident(incoming.get("task_id"))
        reviewer_task = _yaml(root, "process/tasks/" + rid + ".yaml")
        require(reviewer_task.get("operation") == incoming["operation"]
                and reviewer_task.get("spine") == task["spine"], "Review task stage/project mismatch")
        submission = load(root, reviewer_task.get("trigger", {}).get("reference"))
        require(submission.get("artifact") == incoming["artifact"]
                and submission.get("task_id") == document["task_id"], "Review changed the submitted artifact")
    pins = dict(document["source_sha256"])
    pins[ref] = file_hash(safe_path(root, ref))
    pins[incoming["artifact"]["path"]] = incoming["artifact"]["sha256"]
    return document, pins


def validate_task(root, task):
    try:
        input_for_task(root, task)
    except VerificationError:
        raise
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise VerificationError("Invalid verification task input: " + str(exc)) from exc


def publish(root, task, doc):
    ident(task["id"])
    base_ref = "reviews/verification/" + task["id"]
    target = safe_path(root, base_ref, "reviews/verification", exists=False)
    artifact_ref = base_ref + "/artifact.json"
    brief_ref = base_ref + "/briefing.md"
    artifact_bytes = json.dumps(doc, indent=2, ensure_ascii=False, allow_nan=False).encode("utf-8") + b"\n"
    receipt = {"schema": SCHEMA, "kind": "SUBMISSION", "mode": "PROJECT",
               "operation": task["operation"], "task_id": task["id"],
               "project_id": doc["project_id"], "spine": doc["spine"], "subject": doc["subject"],
               "gate": REVIEW_FOR[doc["kind"]], "gate_status": "DRAFT_READY",
               "artifact": {"path": artifact_ref, "sha256": hashlib.sha256(artifact_bytes).hexdigest()},
               "briefing": brief_ref, "execution_status": "COMPLETED",
               "review_state": "PENDING", "vo_discharged": [],
               "changed_artifacts": [artifact_ref, brief_ref, base_ref + "/receipt.json"]}
    require(not target.exists(), "Output bundle exists; use a new task ID or inspect existing receipt")
    target.parent.mkdir(parents=True, exist_ok=True)
    lock = target.with_name(target.name + ".lock")
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise VerificationError("Output is locked; inspect interrupted/concurrent run before retrying") from exc
    staging = Path(tempfile.mkdtemp(prefix=".vk-", dir=target.parent))
    try:
        (staging / "artifact.json").write_bytes(artifact_bytes)
        (staging / "briefing.md").write_text(briefing(doc), encoding="utf-8")
        (staging / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        require(not target.exists(), "Output appeared during publish; refusing overwrite")
        os.rename(staging, target)
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    finally:
        lock.rmdir()
    return {"status": "DRAFT_WRITTEN", "artifact": artifact_ref,
            "receipt": base_ref + "/receipt.json", "briefing": brief_ref}


def run_task(root, task):
    require(task.get("operation") in AUTHORS, "Only author operations execute deterministically")
    incoming, pins = input_for_task(root, task)
    for ref in ("tools/verification_kernel.py", "tools/verification_models.py", "tools/task.py"):
        pins[ref] = file_hash(safe_path(root, ref))
    manifest = "process/tasks/" + ident(task["id"]) + ".yaml"
    pins[manifest] = file_hash(safe_path(root, manifest, "process/tasks"))
    for ref in ("process/operations.yaml", "process/loop_transitions.yaml", task["playbook"]):
        pins[ref] = file_hash(safe_path(root, ref))
    previous = "reviews/verification/" + task["id"] + "/receipt.json"
    if safe_path(root, previous, "reviews/verification", exists=False).exists():
        receipt = load(root, previous)
        doc = read_pin(root, receipt.get("artifact"))
        check_artifact(root, doc, AUTHORS[task["operation"]])
        require(receipt.get("kind") == "SUBMISSION" and receipt.get("task_id") == task["id"]
                and doc.get("task_id") == task["id"], "Existing bundle has wrong author")
        require(doc["source_sha256"] == pins, "Existing task result has different inputs; new task ID required")
        return {"status": "ALREADY_PRESENT", "receipt": previous, "briefing": receipt["briefing"]}
    functions = {"DERIVE_ERS": derive, "DESIGN_VERIFICATION_LADDER": plan,
                 "EXECUTE_VERIFICATION_LADDER": execute}
    document = functions[task["operation"]](root, incoming, task["id"], pins)
    check_pins(root, pins)  # Refuse stale inputs before publishing a result.
    return publish(root, task, document)


def demo(root, fixture_ref, out_ref):
    package = load(root, fixture_ref, "process/verification/fixtures")
    require(package.get("mode") == "FIXTURE", "Demo refuses project packages")
    target = safe_path(root, out_ref, "runs", exists=False)
    require(not target.exists(), "Demo output exists; choose a new local output")
    target.mkdir(parents=True)
    inputs = {**package["source_sha256"], fixture_ref: file_hash(safe_path(root, fixture_ref))}
    for source in ("tools/verification_kernel.py", "tools/verification_models.py"):
        inputs[source] = file_hash(safe_path(root, source))
    current = package
    for label, function in (("ers", derive), ("plan", plan), ("evidence", execute)):
        current = function(root, current, "FIXTURE-" + label, inputs, fixture=True)
        path = target / (label + ".json")
        path.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
        (target / (label + "-briefing.md")).write_text(briefing(current), encoding="utf-8")
        inputs = {**inputs, path.relative_to(root).as_posix(): file_hash(path)}
    return {"status": "FIXTURE_ONLY_NOT_REVIEWED", "output": out_ref,
            "results": current["payload"]["results"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    d = sub.add_parser("demo")
    d.add_argument("--fixture", required=True)
    d.add_argument("--out", required=True, help="New directory under runs/")
    c = sub.add_parser("check")
    c.add_argument("--artifact", required=True)
    args = parser.parse_args()
    try:
        if args.command == "demo":
            answer = demo(ROOT, args.fixture, args.out)
        else:
            artifact = load(ROOT, args.artifact)
            check_artifact(ROOT, artifact, fixture=artifact.get("mode") == "FIXTURE")
            answer = {"status": "INTEGRITY_CHECKED_NOT_ACCEPTED", "artifact": args.artifact}
        print(json.dumps(answer, indent=2))
        return 0
    except (VerificationError, OSError, ValueError, TypeError, KeyError) as exc:
        print("VERIFICATION_BLOCKED:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
