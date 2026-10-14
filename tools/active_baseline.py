#!/usr/bin/env python3
"""Verify a controlled active baseline, its reviewed inputs, and open VO state.

This is a read-only acceptance guard. It does not activate a candidate,
discharge a verification obligation, or assert firmware correctness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import yaml

from baseline_relations import BaselineRelationError, resolve as resolve_candidate

ROOT = Path(__file__).resolve().parents[1]


class ActiveBaselineError(ValueError):
    pass


def _file(root: Path, name: str, directory: str) -> Path:
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ActiveBaselineError("Expected repository-relative path")
    base = (root / directory).resolve()
    path = (root / name).resolve()
    if not path.is_relative_to(base) or not path.is_file():
        raise ActiveBaselineError("Missing or out-of-scope artifact: " + name)
    return path


def _yaml(root: Path, name: str, directory: str) -> dict:
    item = yaml.safe_load(_file(root, name, directory).read_text(encoding="utf-8"))
    if not isinstance(item, dict):
        raise ActiveBaselineError("Expected YAML mapping: " + name)
    return item


def _hash(root: Path, name: str, directory: str) -> str:
    return hashlib.sha256(_file(root, name, directory).read_bytes()).hexdigest()


def _review(root: Path, name: str) -> dict:
    data = json.loads(_file(root, name, "reviews").read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ActiveBaselineError("Review receipt is not a JSON object")
    return data


def verify(root: Path, ref: str) -> dict:
    root = root.resolve()
    active = _yaml(root, ref, "process/baselines")
    if active.get("schema") != "pc-active-baseline/v1" or active.get("status") != "active":
        raise ActiveBaselineError("Expected an explicitly active baseline")
    candidate_ref = active.get("source_candidate")
    candidate = _yaml(root, candidate_ref, "process/baselines")
    if candidate.get("schema") != "pc-baseline-candidate/v1":
        raise ActiveBaselineError("Active baseline does not reference a candidate")
    review = _review(root, active.get("independent_baseline_review"))
    if (review.get("schema") != "pc-baseline-review/v1"
            or review.get("gate") != "BASELINE_REVIEW"
            or review.get("independent_of_baseline_authoring_invocation") is not True
            or review.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
            or review.get("gate_status") != "BASELINE_PACKAGE_ACCEPTABLE_FOR_CONTROLLED_ACTIVATION"
            or review.get("candidate") != candidate_ref):
        raise ActiveBaselineError("No favorable independent review for source candidate")
    reviewed_hash = review.get("candidate_sha256")
    actual_hash = _hash(root, candidate_ref, "process/baselines")
    if (reviewed_hash != actual_hash
            or active.get("source_candidate_sha256") != actual_hash):
        raise ActiveBaselineError("Source candidate differs from independently reviewed bytes")
    artifacts = active.get("active_artifacts")
    if not isinstance(artifacts, dict):
        raise ActiveBaselineError("Missing active artifacts")
    matches = {
        "architecture_statement": "candidate_active_as",
        "verification_plan": "candidate_active_verification_plan",
        "vo_004": "candidate_active_vo_004",
        "vo_ledger_source_candidate": "candidate_active_vo_ledger",
    }
    for active_key, candidate_key in matches.items():
        if artifacts.get(active_key) != candidate.get(candidate_key):
            raise ActiveBaselineError("Activated artifact differs from reviewed candidate: " + active_key)
    reviewed = {item.get("path"): item.get("sha256")
                for item in review.get("reviewed_artifacts", []) if isinstance(item, dict)}
    required_refs = [
        candidate_ref,
        artifacts["vo_ledger_source_candidate"],
        artifacts["architecture_statement"],
        artifacts["verification_plan"],
        artifacts["vo_004"],
    ]
    for name in required_refs:
        directory = "knowledge" if name.startswith("knowledge/") else "process"
        if reviewed.get(name) != _hash(root, name, directory):
            # The candidate SHA is recorded in its own review field.
            if name != candidate_ref:
                raise ActiveBaselineError("Reviewed input changed: " + name)
    if artifacts.get("vo_ledger_source_sha256") != reviewed.get(artifacts["vo_ledger_source_candidate"]):
        raise ActiveBaselineError("Active ledger source pin differs from review")
    if active.get("independent_as_review") != candidate.get("independent_as_review", {}).get("receipt"):
        raise ActiveBaselineError("Active AS review differs from reviewed candidate")
    approved = active.get("accepted_authority")
    if not isinstance(approved, dict):
        raise ActiveBaselineError("Active baseline lacks authority index")
    for active_name, candidate_name in (
        ("scope", "scope"), ("provisional_ap", "provisional_ap"),
        ("memory_scope", "protected_memory_scope")
    ):
        if approved.get(active_name) != candidate.get("authority", {}).get(candidate_name):
            raise ActiveBaselineError("Active authority differs from candidate")
    ap = _yaml(root, approved["provisional_ap"], "process/decisions")
    if (ap.get("status") != "approved"
            or ap.get("decision") != "PROVISIONALLY_SELECTED"
            or ap.get("selected_candidate") != active.get("selected_ap")
            or ap.get("authorizes") != "CON_FIRST_DECOMPOSITION_AFTER_BASELINE_RECONCILIATION"):
        raise ActiveBaselineError("No accepted provisional AP authority")
    scope = _yaml(root, approved["scope"], "process/decisions")
    if scope.get("status") != "approved":
        raise ActiveBaselineError("No approved source scope")
    if (active.get("accepted_architectural_debt") != candidate.get("accepted_architectural_debt")
            or active.get("open_verification_obligations") != candidate.get("open_verification_obligations")):
        raise ActiveBaselineError("Active debt or open VOs differ from candidate")
    old = _yaml(root, "process/ledgers/vo_ledger.yaml", "process/ledgers")
    proposed = _yaml(root, artifacts["vo_ledger_source_candidate"], "process/ledgers")
    activated = _yaml(root, artifacts["vo_ledger"], "process/ledgers")
    if (activated.get("status") != "active"
            or activated.get("source_candidate") != artifacts["vo_ledger_source_candidate"]
            or activated.get("base_ledger") != "process/ledgers/vo_ledger.yaml"
            or activated.get("activation", {}).get("reviewed_baseline")
            != active["independent_baseline_review"]
            or activated.get("activation", {}).get("active_baseline") != ref):
        raise ActiveBaselineError("VO ledger is not an exact traceable activation")
    if activated.get("obligations") != proposed.get("obligations"):
        raise ActiveBaselineError("Active VO rows differ from reviewed proposal")
    before = {item["id"]: item for item in old.get("obligations", [])}
    now = {item["id"]: item for item in activated.get("obligations", [])}
    if len(before) != len(old.get("obligations", [])) or len(now) != len(activated.get("obligations", [])) or set(before) != set(now):
        raise ActiveBaselineError("VO IDs lost or duplicated")
    for key, row in before.items():
        entry = now[key]
        if (entry.get("state") != row.get("state")
                or entry.get("evidence_receipt") != row.get("evidence_receipt")
                or entry.get("requirement") != row.get("requirement")
                or entry.get("owner") != row.get("owner")):
            raise ActiveBaselineError("VO state or authority improperly changed: " + key)
        if entry.get("due_stage") != row.get("due_stage"):
            valid = any(
                v.get("id") == key and v.get("from_due_stage") == row.get("due_stage")
                and v.get("to_due_stage") == entry.get("due_stage")
                and v.get("preserved_state") == entry.get("state")
                for v in ap.get("authorized_vo_supersessions", [])
            )
            if not valid:
                raise ActiveBaselineError("Unapproved VO due-stage change: " + key)
    if active.get("effective_relations_from_reviewed_candidate") is not True:
        raise ActiveBaselineError("Active relation selection not explicitly linked to reviewed candidate")
    try:
        relation = resolve_candidate(root, candidate_ref)
    except BaselineRelationError as exc:
        raise ActiveBaselineError("Invalid reviewed effective relations: " + str(exc)) from exc
    return {
        "status": "ACTIVE_BASELINE_VERIFIED",
        "baseline": ref,
        "review": active["independent_baseline_review"],
        "architecture": artifacts["architecture_statement"],
        "verification_plan": artifacts["verification_plan"],
        "vo_ledger": artifacts["vo_ledger"],
        "selected_ap": active["selected_ap"],
        "open_vos": active["open_verification_obligations"],
        "effective_relations": relation["overrides"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inspect"])
    parser.add_argument("--baseline", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(ROOT, args.baseline), indent=2))
    except (ActiveBaselineError, OSError, ValueError, TypeError, KeyError,
            yaml.YAMLError, json.JSONDecodeError) as exc:
        print("ACTIVE_BASELINE_INVALID:", exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
