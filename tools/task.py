#!/usr/bin/env python3
"""Validate, preview, or execute a reusable Progressive Concretization task.

A task references a role, playbook and architecture spine. It does not approve
architecture, discharge obligations, or validate mathematics.
"""
from __future__ import annotations

import argparse
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
