#!/usr/bin/env python3
"""Collect host-only Toy 1 object layout and preserve unknown charged SRAM.

No target ABI, linker map, stack maxima, nesting, FSRAM ranking, product
verification, or VO discharge is inferred from a host sizeof observation.
User runs this locally; the resulting versioned candidate needs review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = "process/verification/toy1-vo002-inventory-template-v1.yaml"
SOURCE = "implementation/toy1/resource_layout_probe.c"
HEADER = "implementation/toy1/detector.h"
IMPLEMENTATION = "implementation/toy1/detector.c"
CONTRACT = "knowledge/architecture/AS-001/contracts/CON-AP2-003-v6.md"
SCOPE = "process/decisions/C-002-scope.yaml"
MAX_OUTPUT = 32768


def hashed(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_output(value: str, parent: str) -> Path:
    p = Path(value)
    if not value or p.is_absolute() or ".." in p.parts:
        raise ValueError("Output must be a repository-relative path without parent traversal")
    q = (ROOT / p).resolve()
    base = (ROOT / parent).resolve()
    if not q.is_relative_to(base) or q == base:
        raise ValueError("Output must be inside " + parent)
    if q.exists():
        raise ValueError("Refusing to overwrite existing output: " + value)
    return q


def invocation(args: list[str], out: Path, tag: str) -> dict:
    entry: dict = {"label": tag, "argv": args, "cwd": ".", "exit_code": None,
                   "status": "NOT_EXECUTED"}
    try:
        proc = subprocess.run(args, cwd=ROOT, capture_output=True,
                              timeout=60, check=False)
        entry["exit_code"] = proc.returncode
        entry["status"] = "COMPLETED"
        output = {"stdout": proc.stdout, "stderr": proc.stderr}
    except FileNotFoundError as err:
        entry["status"] = "EXECUTABLE_NOT_FOUND"
        output = {"stdout": b"", "stderr": str(err).encode()}
    except subprocess.TimeoutExpired as err:
        entry["status"] = "TIMEOUT"
        output = {"stdout": err.stdout or b"", "stderr": err.stderr or b""}
    for stream, payload in output.items():
        rel = (out / (tag + "." + stream + ".txt")).relative_to(ROOT).as_posix()
        saved = payload[:MAX_OUTPUT]
        (ROOT / rel).write_bytes(saved)
        entry[stream] = {"path": rel, "sha256": hashlib.sha256(saved).hexdigest(),
                         "byte_count": len(payload), "truncated": len(payload) > MAX_OUTPUT}
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="New ignored directory below runs/")
    parser.add_argument("--summary", required=True, help="New JSON below reviews/verification/")
    parser.add_argument("--host-cc", default="cc", help="Executable or quoted host compiler command")
    opts = parser.parse_args()
    try:
        out = relative_output(opts.out, "runs")
        summary = relative_output(opts.summary, "reviews/verification")
        cc = shlex.split(opts.host_cc)
        if not cc:
            raise ValueError("Host compiler command must not be empty")
        template = yaml.safe_load((ROOT / TEMPLATE).read_text(encoding="utf-8"))
        ceilings = template["category_ceilings_bytes"]
        actual = template["actual_category_peaks_bytes"]
        if (sum(ceilings.values()) != 1792 or template["approved_limit_bytes"] != 2048
                or template["reserve_bytes"] != 256 or set(actual) != set(ceilings)
                or any(value is not None for value in actual.values())):
            raise ValueError("Unmeasured VO-002 template does not match accepted envelope")
        out.mkdir(parents=True)
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as err:
        print("RESOURCE_SETUP_INVALID:", err, file=sys.stderr)
        return 2

    source_pins = {
        file: hashed(ROOT / file)
        for file in [TEMPLATE, SOURCE, HEADER, IMPLEMENTATION, CONTRACT, SCOPE,
                     "tools/toy1_resource_evidence.py"]
    }
    binary = (out / "toy1-host-layout").relative_to(ROOT).as_posix()
    commands = [
        invocation(cc + ["--version"], out, "host-compiler-version"),
        invocation(cc + ["-std=c99", "-Wall", "-Wextra", "-Werror", "-pedantic",
                         "-I", "implementation/toy1", SOURCE, "-o", binary],
                   out, "compile-host-layout"),
    ]
    if commands[-1]["exit_code"] == 0:
        commands.append(invocation(["./" + binary], out, "execute-host-layout"))
    observation = None
    if commands[-1]["label"] == "execute-host-layout" and commands[-1]["exit_code"] == 0:
        try:
            printed = (out / "execute-host-layout.stdout.txt").read_text(encoding="utf-8")
            observation = json.loads(printed.strip())
            fields = ("sizeof_samples", "sizeof_oldest", "sizeof_sum_squares")
            if (observation.get("schema") != "pc-toy1-layout-observation/v1"
                    or observation.get("window") != 32
                    or any(not isinstance(observation.get(f), int) for f in fields)
                    or observation["sizeof_detector"] < sum(observation[f] for f in fields)):
                raise ValueError("Invalid host layout observation")
            observation["field_bytes"] = sum(observation[f] for f in fields)
            observation["object_overhead_bytes"] = (
                observation["sizeof_detector"] - observation["field_bytes"])
        except (UnicodeError, json.JSONDecodeError, ValueError, KeyError, TypeError) as err:
            commands.append({"label": "parse-host-layout", "status": "INVALID_OUTPUT",
                             "error": str(err), "exit_code": None})
            observation = None

    source_stable = all(hashed(ROOT / file) == h for file, h in source_pins.items())
    status = ("HOST_LAYOUT_RECORDED" if observation is not None and source_stable
              else "INCOMPLETE_OR_FAILED")
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=False)
    report = {
        "schema": "pc-toy1-resource-evidence/v1",
        "project_id": "AS-001",
        "spine": "/architecture/AS-001/spine.md",
        "source_revision": revision.stdout.strip() if revision.returncode == 0 else None,
        "source_sha256": source_pins,
        "source_stable_during_collection": source_stable,
        "observation_status": status,
        "host_layout_observation": observation,
        "host_evidence_scope": "C99 ABI object layout in the invoking host compiler, not target SRAM",
        "commands": commands,
        "raw_directory": out.relative_to(ROOT).as_posix(),
        "target_status": "NOT_REQUESTED",
        "target_measurements_available": False,
        "accepted_conditional_envelope_bytes": {
            "category_ceilings": ceilings,
            "allocated_category_ceiling": 1792,
            "reserve": 256,
            "approved_limit": 2048,
        },
        "measured_target_category_peaks_bytes": dict(actual),
        "unknown_or_unverified": [
            "Selected target CPU/ABI/toolchain, linker and actual integration are unspecified",
            "Detector stack depth and worst-case stack/context nesting",
            "Shared, dynamic and other attributable allocations and justified exclusions",
            "Peak simultaneous SRAM with nonoverlap and lifetime evidence",
            "Target sizeof, section symbols and memory map",
            "Independent target/integration qualification and final F-001 comparison",
        ],
        "interpretation_limit": (
            "An observed host object size is not a complete C-002 charged-SRAM"
            " inventory, nor proof of a target category ceiling or VO discharge."),
        "review_state": "PENDING_INDEPENDENT_REVIEW",
        "product_verified": False,
        "vo_discharged": [],
        "open_obligations": ["VO-002", "VO-003", "VO-004", "VO-005", "VO-006"],
    }
    (out / "manifest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    summary.parent.mkdir(parents=True, exist_ok=True)
    with summary.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": status,
                      "host_size": observation.get("sizeof_detector") if observation else None,
                      "target_status": "NOT_REQUESTED",
                      "summary": summary.relative_to(ROOT).as_posix(),
                      "vo_discharged": []}, indent=2))
    return 0 if status == "HOST_LAYOUT_RECORDED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
