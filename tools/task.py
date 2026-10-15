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
