#!/usr/bin/env python3
"""Explicit Archbot project discovery and unsolved-project bootstrap.

Works with checked-out Git submodules or ordinary project directories.
Does not read legacy Toy 1 roots, approve authority, or load project code.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
PROJECT_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
SCHEMA = "pc-project-bundle/v1"
ROOT_NAMES = ("knowledge", "process", "reviews", "implementation",
              "adapters", "tests")


class ProjectError(ValueError):
    pass


def validated_id(value: str) -> str:
    if not isinstance(value, str) or not PROJECT_ID.fullmatch(value):
        raise ProjectError("Invalid project ID")
    return value


def path_name(value: str) -> str:
    if (not isinstance(value, str) or not value or
            value.startswith("/") or "\\" in value or ":" in value or
            value != PurePosixPath(value).as_posix() or
            any(part in ("", ".", "..", ".git") for part in value.split("/"))):
        raise ProjectError("Unsafe project-relative path")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ProjectError("Unencodable project-relative path") from exc
    return value


def _within(directory: Path, path: str, *, kind: str) -> Path:
    """Require in-bundle path with no symlinked component."""
    target = directory / path_name(path)
    if not target.resolve().is_relative_to(directory):
        raise ProjectError("Project path escapes bundle")
    if target.resolve() != target:
        raise ProjectError("Project path is aliased or symlinked")
    if kind == "file" and not target.is_file():
        raise ProjectError("Missing project file: " + path)
    if kind == "dir" and not target.is_dir():
        raise ProjectError("Missing project directory: " + path)
    return target


def _projects_dir(root: Path) -> Path:
    base = root / "projects"
    if base.is_symlink():
        raise ProjectError("Project collection cannot be a symlink")
    if base.exists() and not base.is_dir():
        raise ProjectError("Project collection is not a directory")
    return base


def _gitlink(root: Path, project_id: str) -> bool:
    """Git index identification only. Never run Git in a candidate project."""
    try:
        p = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--stage", "--",
             "projects/" + project_id],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=5, check=False, text=True,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    line = p.stdout.strip() if p.returncode == 0 else ""
    return any(
        item.startswith("160000 ") and
        item.endswith("\tprojects/" + project_id)
        for item in line.splitlines()
    )


def inspect_project(root: Path, project_id: str) -> dict:
    root = Path(root).resolve()
    project_id = validated_id(project_id)
    directory = _projects_dir(root) / project_id
    if directory.is_symlink() or not directory.is_dir():
        raise ProjectError("Project is not installed: " + project_id)
    if directory.resolve() != directory:
        raise ProjectError("Project directory escapes root")
    manifest = _within(directory, "project.yaml", kind="file")
    if manifest.stat().st_size > 128_000:
        raise ProjectError("Project manifest exceeds size limit")
    try:
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    except (yaml.YAMLError, UnicodeError) as exc:
        raise ProjectError("Malformed project manifest") from exc
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise ProjectError("Unrecognized project manifest schema")
    if data.get("project_id") != project_id:
        raise ProjectError("Project ID does not match installed folder")
    if type(data.get("bundle_schema_version")) is not int or data["bundle_schema_version"] != 1:
        raise ProjectError("Unsupported project bundle version")
    if data.get("framework_contract_version") != SCHEMA:
        raise ProjectError("Incompatible framework contract")
    spine = data.get("project_spine")
    _within(directory, spine, kind="file")
    roots = data.get("roots")
    if not isinstance(roots, dict) or set(roots) != set(ROOT_NAMES):
        raise ProjectError("Project artifact roots must be explicit")
    for key in ROOT_NAMES:
        _within(directory, roots[key], kind="dir")
    baseline = data.get("active_baseline", None)
    if baseline is not None:
        _within(directory, baseline, kind="file")
    validators = data.get("declared_validators")
    if not isinstance(validators, list) or any(
            not isinstance(v, str) or not v or
            v != path_name(v) for v in validators):
        raise ProjectError("Invalid declared validator paths")
    for validator in validators:
        _within(directory, validator, kind="file")
    vcs = ("git-submodule" if _gitlink(root, project_id) else
           "nested-git" if (directory / ".git").is_file() or
           (directory / ".git").is_dir() else "directory")
    return {
        "schema": "pc-project-inspection/v1",
        "project_id": project_id,
        "path": "projects/" + project_id,
        "installation": vcs,
        "framework_contract_version": SCHEMA,
        "project_spine": spine,
        "active_baseline_reference": baseline,
        "declared_validator_count": len(validators),
        "authority_status": "NOT_EVALUATED",
        "product_verified": False,
        "note": "Discovery does not activate accepted authority or execute validators",
    }


def list_projects(root: Path) -> dict:
    root = Path(root).resolve()
    base = _projects_dir(root)
    installed, invalid = [], []
    if base.exists():
        for item in sorted(base.iterdir(), key=lambda p: p.name):
            if not item.is_dir() and not item.is_symlink():
                continue
            if item.name.startswith("."):
                continue
            try:
                installed.append(inspect_project(root, item.name))
            except ProjectError as exc:
                invalid.append({"path": "projects/" + item.name,
                                "reason": str(exc)})
    return {"schema": "pc-project-list/v1", "projects": installed,
            "invalid": invalid, "active_project": None}


def init_project(root: Path, project_id: str) -> dict:
    """Create unsolved contents only; Git repository creation is user's choice."""
    root = Path(root).resolve()
    project_id = validated_id(project_id)
    base = _projects_dir(root)
    directory = base / project_id
    if directory.exists() or directory.is_symlink():
        raise ProjectError("Refusing to overwrite installed project")
    base.mkdir(exist_ok=True)
    directory.mkdir()
    for name in ROOT_NAMES:
        (directory / name).mkdir()
        (directory / name / ".gitkeep").write_text("")
    (directory / ".gitignore").write_text(
        "/.work/\n__pycache__/\n*.py[cod]\n*.log\n"
    )
    (directory / "project.yaml").write_text(
        yaml.safe_dump({
            "schema": SCHEMA,
            "project_id": project_id,
            "bundle_schema_version": 1,
            "framework_contract_version": SCHEMA,
            "project_spine": "PROJECT_SPINE.md",
            "roots": {name: name for name in ROOT_NAMES},
            "active_baseline": None,
            "declared_validators": [],
        }, sort_keys=False),
        encoding="utf-8",
    )
    (directory / "PROJECT_SPINE.md").write_text(
        "# " + project_id + ": unsolved project spine\n\n"
        "Status: NEW / NO ACCEPTED ARCHITECTURE OR BASELINE.\n\n"
        "This project owns its requirements, decisions, evidence, and implementation.\n"
        "No other project's accepted material is inherited.\n",
        encoding="utf-8",
    )
    return inspect_project(root, project_id)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("operation", choices=("list", "inspect", "init"))
    p.add_argument("project_id", nargs="?")
    p.add_argument("--root", type=Path, default=ROOT)
    args = p.parse_args(argv)
    try:
        if args.operation == "list":
            if args.project_id is not None:
                raise ProjectError("Project ID is not accepted for list")
            result = list_projects(args.root)
            exit_code = 2 if result["invalid"] else 0
        elif args.operation == "inspect":
            if args.project_id is None:
                raise ProjectError("Project ID is required")
            result = inspect_project(args.root, args.project_id)
            exit_code = 0
        else:
            if args.project_id is None:
                raise ProjectError("Project ID is required")
            result = init_project(args.root, args.project_id)
            exit_code = 0
    except ProjectError as exc:
        result = {"schema": "pc-project-error/v1", "status": "UNRESOLVED",
                  "reason": str(exc)}
        exit_code = 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
