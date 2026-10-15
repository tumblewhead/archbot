#!/usr/bin/env python3
"""Shared task entry point; VK-001 extends, rather than rewrites, legacy gates."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml
import task_legacy as legacy

ROOT = Path(__file__).resolve().parents[1]
TaskError = legacy.TaskError
ID_PATTERN = legacy.ID_PATTERN
OP_PATTERN = legacy.OP_PATTERN
_file = legacy._file
make_prompt = legacy.make_prompt


def validate_compiler_evidence_review(root: Path, data: dict) -> None:
    """Review-input integrity, not an authority or compiler correctness verdict."""
    trig = data.get("trigger", {})
    context = data.get("context", {})
    inputs = context.get("review_inputs", {}) if isinstance(context, dict) else {}
    if (trig.get("kind") != "EXECUTABLE_EVIDENCE_SUBMITTED"
            or not isinstance(inputs, dict)
            or inputs.get("evidence_summary") != trig.get("reference")):
        raise TaskError("Compiler review requires a matching submitted evidence path")
    evidence_path = _file(root, trig["reference"], "reviews/verification")
    raw = evidence_path.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    if blob != inputs.get("evidence_blob_sha1"):
        raise TaskError("Submitted compiler evidence identity changed")
    try:
        record = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise TaskError("Submitted compiler evidence is invalid JSON") from exc
    if (not isinstance(record, dict)
            or record.get("schema") != inputs.get("expected_schema")
            or record.get("spine") != data.get("spine")
            or record.get("source_revision") != inputs.get("source_revision")
            or trig.get("revision") != inputs.get("source_revision")
            or record.get("prior_independent_review") != inputs.get("prior_review")
            or record.get("review_state") != "PENDING_INDEPENDENT_REVIEW"
            or record.get("product_verified") is not False
            or record.get("vo_discharged") != []):
        raise TaskError("Compiler review source, scope or evidence state disagrees")
    pins = record.get("source_sha256")
    if not isinstance(pins, dict) or not pins:
        raise TaskError("Compiler evidence has no source pins")
    for source, expected in pins.items():
        if (not isinstance(source, str) or not isinstance(expected, str)
                or len(expected) != 64):
            raise TaskError("Malformed compiler evidence pin")
        if hashlib.sha256(_file(root, source).read_bytes()).hexdigest() != expected:
            raise TaskError("Compiler evidence source changed: " + source)
    original = json.loads(_file(root, inputs["prior_review"], "reviews/gates").read_text(encoding="utf-8"))
    if (original.get("schema") != "pc-implementation-review/v1"
            or original.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
            or original.get("independent_of_authoring_invocation") is not True
            or not all(pins.get(ref) == sha
                       for ref, sha in original.get("reviewed_source_sha256", {}).items())):
        raise TaskError("Compiler review is not bound to accepted implementation sources")
    if ("discharge_VO" not in data.get("outputs", {}).get("prohibited", [])
            or not data.get("gate", {}).get("require_independent_review")):
        raise TaskError("Compiler review cannot alter verification authority")



def validate_resource_evidence_review(root: Path, data: dict) -> None:
    """Check submitted resource evidence identity and boundaries, not physical fit."""
    trigger = data.get("trigger", {})
    context = data.get("context", {})
    inputs = context.get("review_inputs", {}) if isinstance(context, dict) else {}
    if (not isinstance(trigger, dict) or not isinstance(inputs, dict)
            or trigger.get("kind") != "RESOURCE_EVIDENCE_SUBMITTED"
            or trigger.get("reference") != inputs.get("evidence_summary")):
        raise TaskError("Resource review requires matching evidence input")
    ref = trigger["reference"]
    raw = _file(root, ref, "reviews/verification").read_bytes()
    identity = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    if identity != inputs.get("evidence_blob_sha1"):
        raise TaskError("Submitted resource evidence identity changed")
    try:
        record = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise TaskError("Submitted resource evidence is invalid JSON") from exc
    if (not isinstance(record, dict)
            or record.get("schema") != inputs.get("expected_schema")
            or record.get("project_id") != inputs.get("project_id")
            or record.get("spine") != data.get("spine")
            or record.get("source_revision") != inputs.get("source_revision")
            or trigger.get("revision") != inputs.get("source_revision")
            or record.get("source_stable_during_collection") is not True
            or record.get("observation_status") != "HOST_LAYOUT_RECORDED"
            or record.get("review_state") != "PENDING_INDEPENDENT_REVIEW"
            or record.get("target_status") != "NOT_REQUESTED"
            or record.get("target_measurements_available") is not False
            or record.get("product_verified") is not False
            or record.get("vo_discharged") != []):
        raise TaskError("Resource evidence context or maturity does not match review")
    pins = record.get("source_sha256")
    if not isinstance(pins, dict) or not pins:
        raise TaskError("Resource evidence has no pinned inputs")
    for ref, expected in pins.items():
        if (not isinstance(ref, str) or not isinstance(expected, str)
                or len(expected) != 64
                or hashlib.sha256(_file(root, ref).read_bytes()).hexdigest() != expected):
            raise TaskError("Resource evidence source pin mismatch: " + str(ref))
    for key in ("accepted_scope", "resource_contract", "resource_template"):
        if inputs.get(key) not in pins:
            raise TaskError("Review omits pinned " + key)
    template = yaml.safe_load(_file(root, inputs["resource_template"]).read_text(encoding="utf-8"))
    ceilings = template.get("category_ceilings_bytes") if isinstance(template, dict) else None
    peaks = record.get("measured_target_category_peaks_bytes")
    if (not isinstance(ceilings, dict) or len(ceilings) != 7
            or not isinstance(peaks, dict) or set(peaks) != set(ceilings)
            or any(value is not None for value in peaks.values())
            or any(value is not None for value in template.get("actual_category_peaks_bytes", {}).values())):
        raise TaskError("Host-only review requires all target category peaks unknown")
    envelope = record.get("accepted_conditional_envelope_bytes", {})
    if (envelope.get("category_ceilings") != ceilings
            or envelope.get("allocated_category_ceiling") != template.get("allocated_category_ceiling_bytes")
            or envelope.get("reserve") != template.get("reserve_bytes")
            or envelope.get("approved_limit") != template.get("approved_limit_bytes")
            or sum(ceilings.values()) + template.get("reserve_bytes", -1)
                != template.get("approved_limit_bytes")):
        raise TaskError("Resource evidence does not match accepted conditional envelope")
    layout = record.get("host_layout_observation", {})
    if (not isinstance(layout, dict)
            or layout.get("schema") != "pc-toy1-layout-observation/v1"
            or any(type(layout.get(x)) is not int or layout[x] < 0
                   for x in ("sizeof_detector", "sizeof_samples", "sizeof_oldest",
                             "sizeof_sum_squares", "field_bytes", "object_overhead_bytes"))
            or layout["field_bytes"] != sum(layout[x] for x in (
                   "sizeof_samples", "sizeof_oldest", "sizeof_sum_squares"))
            or layout["sizeof_detector"] != layout["field_bytes"] +
                   layout["object_overhead_bytes"]):
        raise TaskError("Host layout totals inconsistent")
    if ("discharge_VO" not in data.get("outputs", {}).get("prohibited", [])
            or not data.get("gate", {}).get("require_independent_review")):
        raise TaskError("Resource review task must preserve independent authority")



def validate(root: Path, manifest: str) -> dict:
    result = legacy.validate(root, manifest)
    data = yaml.safe_load(_file(root, manifest, "process/tasks").read_text(encoding="utf-8"))
    registry = yaml.safe_load(_file(root, "process/operations.yaml").read_text(encoding="utf-8"))
    spec = registry["operations"][result["operation"]]
    # A single protocol hook covers all VK-001 stages and their reviews.
    from verification_kernel import AUTHORS, OPERATIONS, VerificationError, validate_task
    if result["operation"] in OPERATIONS:
        if spec.get("contract") != "pc-verification/v1":
            raise TaskError("Verification operation requires the shared contract")
        expected_executor = "verification-kernel/v1" if result["operation"] in AUTHORS else "codex"
        if spec.get("executor", "codex") != expected_executor:
            raise TaskError("Verification executor conflicts with operation contract")
        try:
            validate_task(root, data)
        except VerificationError as exc:
            raise TaskError(str(exc)) from exc
        result["executor"] = spec.get("executor", "codex")
    elif spec.get("contract") == "pc-verification/v1":
        raise TaskError("Unknown verification operation")
    if result["operation"] == "REVIEW_COMPILER_EVIDENCE":
        validate_compiler_evidence_review(root, data)
    elif result["operation"] == "REVIEW_RESOURCE_EVIDENCE":
        validate_resource_evidence_review(root, data)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect", "render", "run"))
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args(argv)
    try:
        selected = validate(ROOT, args.manifest)
        if args.command == "inspect":
            print(json.dumps(selected, indent=2))
            return 0
        if args.command == "run" and selected.get("executor") == "verification-kernel/v1":
            from verification_kernel import run_task
            data = yaml.safe_load(_file(ROOT, args.manifest, "process/tasks").read_text(encoding="utf-8"))
            # IDs must identify their persistent task file for reproducible input pinning.
            if Path(args.manifest).as_posix() != "process/tasks/" + data["id"] + ".yaml":
                raise TaskError("Verification manifest filename must match task ID")
            print(json.dumps(run_task(ROOT, data), indent=2))
            return 0
        prompt = make_prompt(ROOT, selected)
        if args.command == "render":
            sys.stdout.write(prompt)
            return 0
        outdir = ROOT / "runs" / "task-prompts"
        outdir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", prefix=selected["id"] + "-",
                                         suffix=".md", dir=outdir, delete=False) as handle:
            handle.write(prompt)
            task_prompt = Path(handle.name)
        print(f"TASK={selected['id']} MANIFEST={selected['manifest']} ROLE={selected['role']}", flush=True)
        return subprocess.run([sys.executable, str(ROOT / "tools/telemetry.py"), "run",
                               "--role", selected["role"], "--prompt", str(task_prompt),
                               "--label", selected["id"]], cwd=ROOT, check=False).returncode
    except (TaskError, OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        print("TASK_INVALID:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
