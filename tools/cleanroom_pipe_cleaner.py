#!/usr/bin/env python3
"""Prepare or inspect a Toy 1 *diagnostic* fresh-agent package.

This is not a qualified cleanroom or a Codex launcher. Copy only fixed
reviewed-by-inspection input files; never package old solutions or .git.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "pc-toy1-pipe-cleaner/v1"

# Source Git blob IDs bind this prototype to inspected, versioned inputs.
# Do not append files by globbing the legacy Toy 1 repository.
SOURCES = {
    "knowledge/bkp/problem-origin.md":
        ("workspace/projects/CLN-001/knowledge/bkp/problem-origin.md",
         "d5ae64168585475e0307d34c1eab8713ad56615d"),
    "knowledge/bkp/adc.md":
        ("workspace/projects/CLN-001/knowledge/bkp/adc.md",
         "91321092a99e24c2dee325877a8ea6196e5d1f6e"),
    "knowledge/bkp/target.md":
        ("workspace/projects/CLN-001/knowledge/bkp/target.md",
         "052f765d0c72f5d805e9fd49bdb19197ee6aa170"),
    "agents/architecture-agent.md":
        ("workspace/framework/agents/architecture-agent.md",
         "a3690968df441cd1f23c02836cfaef5a92df97bc"),
    "agents/verification-agent.md":
        ("workspace/framework/agents/verification-agent.md",
         "b29c1bff90cefcc7e9bf34a65bcfa9a77bd6c8cb"),
    "process/playbooks/REVIEW_AS.md":
        ("workspace/framework/playbooks/REVIEW_AS.md",
         "66c0cc31f2934fdb2a4a407c30a242db390fd73c"),
    "framework/core/project_registry.py":
        ("workspace/framework/core/project_registry.py",
         "4ade03cf69cfedc86f97ee582faf364b646b60c2"),
}

AGENT_INSTRUCTIONS = """# Fresh Archbot project: diagnostic pipe-cleaner

Read TASK-001.md first. This workspace is a standalone unsolved engineering
project. Only its own problem inputs and its small generic framework slice
are authoritative inputs. Do not import another project's architecture,
algorithm, proofs, reviewer outputs, code, or baseline.

The process is progressive: first create a DRAFT Architecture Statement
(C, R, PS), source and uncertainty index, and questions for engineering
authority. Do not jump directly to implementation. Identify stakeholder
requirements versus hypothetical assumptions. Do not declare an agent
draft approved, or discharge a verification obligation.

For independent review use a separate reviewer invocation. Ask the human
to resolve missing authority rather than inventing an approval.

This is a pre-freeze DIAGNOSTIC, not a certified cleanroom qualification.
Any capability you cannot perform must be recorded as UNRESOLVED.
"""

FIRST_TASK = """# TASK-001: initial Toy 1 Architecture Statement from unsolved BKP

Role: architecture-agent
Inputs:
- projects/CLN-001/knowledge/bkp/problem-origin.md
- projects/CLN-001/knowledge/bkp/adc.md
- projects/CLN-001/knowledge/bkp/target.md
- framework/agents/architecture-agent.md

Start by inspecting projects/CLN-001/PROJECT_SPINE.md. Generate the
first project-owned architecture candidate from the listed BKP only.

Permitted new outputs, under projects/CLN-001/out/:
- AS-DRAFT-001.md: C/R/PS, traceability and explicit assumptions
- QUESTIONS-001.md: missing authority and ambiguities for the human
- BRIEFING-001.md: completion status, unresolved requirements and next gate

Do not use any prior solution, selected AP, existing PR/CON/DE, implementation
or previous review. Do not create final accepted authority. The old problem
statement may mix invented demonstration assumptions with stakeholder
requirements. Preserve that distinction and ask rather than guessing.

STOP after the first Architecture Statement draft and questions.
A separate reviewer and human approval are required before progression.
"""

PROJECT_SPINE = """# CLN-001: unsolved project

Status: NEW; NO APPROVED AS, P, AP, CON, DE, implementation or VO discharge.

## Readable inputs
- knowledge/bkp/problem-origin.md
- knowledge/bkp/adc.md
- knowledge/bkp/target.md

## Current operation
- TASK-001.md (at workspace root)
- architecture-agent draft is pending

## Accepted authority
None. Missing questions require engineering authority.
"""

PROJECT_MANIFEST = """schema: pc-project-bundle/v1
project_id: CLN-001
bundle_schema_version: 1
framework_contract_version: pc-project-bundle/v1
project_spine: PROJECT_SPINE.md
roots:
  knowledge: knowledge
  process: process
  reviews: reviews
  implementation: implementation
  adapters: adapters
  tests: tests
active_baseline: null
declared_validators: []
"""

GENERATED = {
    "workspace/AGENTS.md": AGENT_INSTRUCTIONS,
    "workspace/TASK-001.md": FIRST_TASK,
    "workspace/projects/CLN-001/PROJECT_SPINE.md": PROJECT_SPINE,
    "workspace/projects/CLN-001/project.yaml": PROJECT_MANIFEST,
}


class PackageError(ValueError):
    pass


def git_blob_id(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") +
                        b"\0" + raw).hexdigest()


def _inside(root: Path, candidate: Path) -> bool:
    return candidate == root or candidate.is_relative_to(root)


def _read_source(root: Path, rel: str, git_pin: str) -> bytes:
    source = root / rel
    if source.resolve() != source or not source.is_file():
        raise PackageError("Missing or aliased allowlisted source: " + rel)
    raw = source.read_bytes()
    if git_blob_id(raw) != git_pin:
        raise PackageError("Allowlisted source changed; inspect before updating: " + rel)
    return raw


def prepare(source_root: Path, output: Path) -> dict:
    source_root = source_root.resolve()
    output = output.absolute()
    if output.exists() or output.is_symlink():
        raise PackageError("Destination already exists")
    if output.parent.resolve() != output.parent:
        raise PackageError("Destination parent is aliased")
    if _inside(source_root, output.resolve()):
        raise PackageError("Destination must be outside source repository")
    # Complete preflight before writing anything.
    originals = {rel: _read_source(source_root, rel, pin)
                 for rel, (_, pin) in SOURCES.items()}
    output.mkdir(parents=True, mode=0o700)
    agent = output / "workspace"
    auditor = output / "auditor_only"
    agent.mkdir()
    auditor.mkdir()
    for directory in ("knowledge", "process", "reviews", "implementation",
                      "adapters", "tests", "out"):
        (agent / "projects" / "CLN-001" / directory).mkdir(
            parents=True, exist_ok=True
        )
    inputs = []
    for origin, (dest, pin) in SOURCES.items():
        raw = originals[origin]
        path = output / dest
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        inputs.append({
            "path": dest.removeprefix("workspace/"),
            "classification": "original_unsolved_BKP" if origin.startswith("knowledge/") else
                              "generic_framework",
            "source_path": origin,
            "source_git_blob_sha1": pin,
            "sha256": hashlib.sha256(raw).hexdigest(),
        })
    for dest, text in GENERATED.items():
        path = output / dest
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        inputs.append({
            "path": dest.removeprefix("workspace/"),
            "classification": "fresh_generated_scaffold",
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        })
    manifest = {
        "schema": SCHEMA,
        "mode": "PRE_FREEZE_DIAGNOSTIC_NOT_CLEANROOM_QUALIFICATION",
        "workspace": "workspace",
        "allowlisted_files": sorted(inputs, key=lambda d: d["path"]),
        "auditor_only": True,
        "reviewed_for_cleanroom": False,
        "framework_frozen": False,
        "contains_prior_Toy1_solution": False,
        "project_id": "CLN-001",
        "limits": [
            "A directory package does not isolate host mounts, connectors or agent context.",
            "Use a fresh agent with access restricted to workspace before claiming even diagnostic isolation.",
            "Do not expose auditor_only, source checkout, parent Git or evaluation oracle to the agent.",
            "Input BKP contains synthetic timing statements whose authority has not been accepted."
        ],
    }
    (auditor / "manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def inspect_package(path: Path) -> dict:
    path = path.resolve()
    audit_path = path / "auditor_only" / "manifest.json"
    if not audit_path.is_file():
        raise PackageError("Missing auditor manifest")
    doc = json.loads(audit_path.read_text(encoding="utf-8"))
    if doc.get("schema") != SCHEMA:
        raise PackageError("Unsupported diagnostic manifest")
    workspace = path / "workspace"
    allowed = {f["path"]: f["sha256"] for f in doc["allowlisted_files"]}
    unexpected = []
    invalid = []
    seen = set()
    if not workspace.is_dir() or workspace.is_symlink():
        raise PackageError("Workspace missing or symlinked")
    for item in workspace.rglob("*"):
        if item.is_symlink():
            invalid.append(item.relative_to(workspace).as_posix())
            continue
        if item.is_dir():
            continue
        rel = item.relative_to(workspace).as_posix()
        if rel.startswith("projects/CLN-001/out/"):
            continue  # Agent outputs can be created after preparation.
        seen.add(rel)
        if rel not in allowed:
            unexpected.append(rel)
        elif hashlib.sha256(item.read_bytes()).hexdigest() != allowed[rel]:
            invalid.append(rel)
    missing = sorted(set(allowed) - seen)
    valid = not unexpected and not invalid and not missing
    return {
        "schema": "pc-pipe-cleaner-preflight/v1",
        "status": "PASS" if valid else "FAIL",
        "allowed_count": len(allowed),
        "unexpected": sorted(unexpected),
        "modified_or_aliased": sorted(invalid),
        "missing": missing,
        "cleanroom_qualified": False,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "inspect"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        result = (prepare(args.source_root, args.output)
                  if args.action == "prepare" else inspect_package(args.output))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "UNRESOLVED", "reason": str(exc)}))
        return 2
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if result.get("status") != "FAIL" else 2


if __name__ == "__main__":
    sys.exit(main())
