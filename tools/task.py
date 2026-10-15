#!/usr/bin/env python3
"""Shared task entry point; VK-001 extends, rather than rewrites, legacy gates."""
from __future__ import annotations

import argparse
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
