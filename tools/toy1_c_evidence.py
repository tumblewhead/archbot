#!/usr/bin/env python3
"""Collect bounded Toy 1 host-C and optional target-object evidence.

This collector is project-specific. It does NOT accept a product, discharge
VOs, prove compiled-code correspondence, or infer an actual target ABI from a
host build. User executes it locally; results require independent review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    "implementation/toy1/detector.h",
    "implementation/toy1/detector.c",
    "implementation/toy1/correspondence_probe.c",
    "implementation/toy1/test_detector.c",
    "tools/toy1_c_evidence.py",
]
BASELINE_REVIEW = "reviews/gates/IMPLEMENT_DE-900da7a3ce8c-independent-review.json"
STRICT_FLAGS = ["-std=c99", "-Wall", "-Wextra", "-Wconversion", "-Werror", "-pedantic"]
MAX_LOG = 1_000_000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_under(name: str, folder: str, *, must_not_exist: bool = True) -> Path:
    path = Path(name)
    if not name or path.is_absolute() or ".." in path.parts:
        raise ValueError("Expected repository-relative path without '..'")
    real = (ROOT / path).resolve()
    allowed = (ROOT / folder).resolve()
    if real == allowed or not real.is_relative_to(allowed):
        raise ValueError("Output must be below " + folder)
    if must_not_exist and real.exists():
        raise ValueError("Output already exists; use a new identifier: " + name)
    return real


def run(command: list[str], label: str, out: Path, *, timeout: int = 90) -> dict:
    """Run a concrete local compiler command; no shell, no inherited approval."""
    result = {"label": label, "argv": command, "cwd": ".", "timeout_s": timeout}
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=timeout,
                              check=False)
        result["returncode"] = proc.returncode
        result["status"] = "COMPLETED"
        stdout, stderr = proc.stdout, proc.stderr
    except FileNotFoundError as exc:
        result["returncode"] = None
        result["status"] = "COMPILER_NOT_FOUND"
        stdout, stderr = b"", str(exc).encode()
    except subprocess.TimeoutExpired as exc:
        result["returncode"] = None
        result["status"] = "TIMEOUT"
        stdout, stderr = exc.stdout or b"", exc.stderr or b""
    for stream, raw in (("stdout", stdout), ("stderr", stderr)):
        # Capture bounded stdout/stderr; an overlong log is an explicit
        # evidence limitation, never silently counted as complete.
        name = label + "." + stream + ".txt"
        truncated = len(raw) > MAX_LOG
        stored = raw[:MAX_LOG]
        (out / name).write_bytes(stored)
        result[stream] = {"path": (out / name).relative_to(ROOT).as_posix(),
                          "sha256": hashlib.sha256(stored).hexdigest(),
                          "bytes_total": len(raw), "truncated": truncated}
    return result


def passed(result: dict, *, expect_failure: bool = False) -> bool:
    if result["status"] != "COMPLETED":
        return False
    code = result["returncode"]
    if expect_failure:
        return isinstance(code, int) and code > 0
    return code == 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True,
                        help="New repository-relative raw directory below runs/")
    parser.add_argument("--summary", help="New tracked JSON under reviews/verification/")
    parser.add_argument("--host-cc", default="cc",
                        help="Host compiler executable (default cc)")
    parser.add_argument("--host-extra", default="",
                        help="Additional host compiler flags, shell-style quoted")
    parser.add_argument("--target-cc", default=None,
                        help="Explicit OPTIONAL target compiler, never guessed")
    parser.add_argument("--target-extra", default="",
                        help="Target compiler flags, e.g. CPU/ABI options")
    parser.add_argument("--target-objdump", default=None,
                        help="Optional target disassembler, output for human review")
    args = parser.parse_args(argv)

    try:
        out = path_under(args.out, "runs")
        summary = path_under(args.summary, "reviews/verification") if args.summary else None
        host_cc = shlex.split(args.host_cc)
        target_cc = shlex.split(args.target_cc) if args.target_cc else None
        host_extra = shlex.split(args.host_extra)
        target_extra = shlex.split(args.target_extra)
        objdump = shlex.split(args.target_objdump) if args.target_objdump else None
        if not host_cc or (args.target_cc and not target_cc) or (args.target_objdump and not target_cc):
            raise ValueError("Compiler or disassembler executable is missing")
        out.mkdir(parents=True, exist_ok=False)
    except (ValueError, OSError) as exc:
        print("EVIDENCE_SETUP_INVALID:", exc, file=sys.stderr)
        return 2

    commands = []
    source_pins = {ref: sha256(ROOT / ref) for ref in SOURCES}
    reviewed = json.loads((ROOT / BASELINE_REVIEW).read_text(encoding="utf-8"))
    previous_pins = reviewed.get("reviewed_source_sha256", {})
    source_matches_review = all(source_pins.get(ref) == expected
                                for ref, expected in previous_pins.items())
    commands.append(run(host_cc + ["--version"], "host-version", out))
    commands.append(run(host_cc + ["-dumpmachine"], "host-machine", out))
    host_ok = passed(commands[-1]) and passed(commands[-2])

    # The explicit checks in correspondence_probe.c survive NDEBUG.
    matrix = [("O0", ["-O0"], False),
              ("O2", ["-O2"], False),
              ("O2-NDEBUG", ["-O2", "-DNDEBUG"], False),
              ("negative-NDEBUG", ["-O2", "-DNDEBUG", "-DTOY1_KNOWN_BAD_CONTROL"], True)]
    for name, variant, negative in matrix:
        executable = (out / ("toy1-" + name)).relative_to(ROOT).as_posix()
        flags = STRICT_FLAGS + host_extra + variant
        compile_cmd = host_cc + flags + [
            "implementation/toy1/detector.c",
            "implementation/toy1/correspondence_probe.c",
            "-o", executable,
        ]
        compiled = run(compile_cmd, "compile-" + name, out)
        commands.append(compiled)
        if not passed(compiled):
            host_ok = False
            continue
        observed = run(["./" + executable], "execute-" + name, out)
        commands.append(observed)
        if not passed(observed, expect_failure=negative):
            host_ok = False
        if negative and passed(observed, expect_failure=True):
            result_text = (out / ("execute-" + name + ".stderr.txt")).read_text(
                encoding="utf-8", errors="replace")
            if "MISMATCH case=" not in result_text:
                host_ok = False

    target_status = "NOT_REQUESTED"
    if target_cc:
        target_commands = [
            ("target-version", target_cc + ["--version"]),
            ("target-machine", target_cc + ["-dumpmachine"]),
            ("target-object", target_cc + STRICT_FLAGS + target_extra + ["-O2", "-c",
                "implementation/toy1/detector.c", "-o",
                (out / "detector-target.o").relative_to(ROOT).as_posix()]),
            ("target-assembly", target_cc + STRICT_FLAGS + target_extra + ["-O2", "-S",
                "implementation/toy1/detector.c", "-o",
                (out / "detector-target.s").relative_to(ROOT).as_posix()]),
        ]
        target_ok = True
        for label, command in target_commands:
            result = run(command, label, out)
            commands.append(result)
            if not passed(result):
                target_ok = False
        target_status = ("OBJECT_AND_ASSEMBLY_GENERATED_NOT_LINKED_OR_APPROVED"
                         if target_ok else "TARGET_COMPILATION_INCOMPLETE")
        if target_ok and objdump:
            commands.append(run(objdump + ["-d",
                (out / "detector-target.o").relative_to(ROOT).as_posix()],
                "target-disassembly", out))
            if not passed(commands[-1]):
                target_status = "TARGET_DISASSEMBLY_FAILED"
    try:
        revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                  capture_output=True, text=True, check=False)
        git_revision = revision.stdout.strip() if revision.returncode == 0 else None
    except OSError:
        git_revision = None

    # Detect a concurrent source edit during collection; never silently bind
    # measurements from different source revisions to the first hash set.
    sources_unchanged = all(sha256(ROOT / ref) == expected
                            for ref, expected in source_pins.items())
    if not sources_unchanged:
        host_ok = False
        if target_cc:
            target_status = "SOURCE_CHANGED_DURING_COLLECTION"

    outputs = {}
    for name in ("detector-target.o", "detector-target.s"):
        artifact = out / name
        if artifact.is_file():
            outputs[name] = {"path": artifact.relative_to(ROOT).as_posix(),
                             "sha256": sha256(artifact), "bytes": artifact.stat().st_size}
    body = {
        "schema": "pc-toy1-c-evidence/v1",
        "project_id": "AS-001",
        "spine": "/architecture/AS-001/spine.md",
        "stage": "C_SOURCE_AND_COMPILER_CORRESPONDENCE_EVIDENCE",
        "source_revision": git_revision,
        "subject": "implementation/toy1/detector.c and detector.h",
        "source_sha256": source_pins,
        "prior_independent_review": BASELINE_REVIEW,
        "sources_match_prior_review": source_matches_review,
        "sources_unchanged_during_collection": sources_unchanged,
        "host_status": ("HOST_PROBE_PASSED" if host_ok else "HOST_PROBE_INCOMPLETE_OR_FAILED"),
        "target_status": target_status,
        "commands": commands,
        "target_outputs": outputs,
        "scope": {
            "host": "Compiled C source tested against an independent shifting queue on the invoking host only.",
            "target": "If requested: target object/assembly compilation evidence only; no link, run, ABI/instruction certification.",
            "domain": "Only legal unsigned 12-bit accepted samples; no required out-of-domain behavior.",
            "execution": "Host is sequential; does not prove external publisher or reset-quiescence enforcement.",
        },
        "review_state": "PENDING_INDEPENDENT_REVIEW",
        "product_verified": False,
        "vo_discharged": [],
        "open_obligations": ["VO-002", "VO-003", "VO-004", "VO-005", "VO-006"],
        "review_questions": [
            "Does actual C promotion, width and expression order preserve CON-AP2-002-v6 on this compiler?",
            "Does source/build/object and any linked binary avoid reliance on floating-point hardware?",
            "Which approved integration layer guarantees legal input and quiescent reset?",
            "If target compilation was requested, what additional target ABI, linking, disassembly and integration evidence is needed?",
        ],
        "notes": [
            "No source scanner or host executable proves absence of target floating-point hardware reliance.",
            "No runtime out-of-range behavior, timing, ISR or watchdog obligation was added.",
            "Host object sizeof, if printed, is NOT a full charged-SRAM or target-stack inventory.",
            "The negative control mutates only the reference oracle and must fail with a MISMATCH.",
            "Actual commands, raw output hashes and artifact hashes refer to local runs/ files.",
            "The identity of an executed tool is not independently authenticated by its string version output.",
        ],
    }
    manifest_path = out / "manifest.json"
    manifest_path.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
    if summary:
        summary.parent.mkdir(parents=True, exist_ok=True)
        with summary.open("x", encoding="utf-8") as stream:
            json.dump(body, stream, indent=2)
            stream.write("\n")
    print(json.dumps({"status": body["host_status"], "target": target_status,
                      "raw_manifest": manifest_path.relative_to(ROOT).as_posix(),
                      "summary": summary.relative_to(ROOT).as_posix() if summary else None,
                      "source_matches_review": source_matches_review,
                      "vo_discharged": []}, indent=2))
    return 0 if host_ok and target_status not in (
        "TARGET_COMPILATION_INCOMPLETE", "TARGET_DISASSEMBLY_FAILED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
