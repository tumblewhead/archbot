#!/usr/bin/env python3
"""Resolve version-scoped effective OKF links for a baseline candidate.

Historical concept edges are immutable. Only explicitly declared,
review-backed overrides may select newer dependencies for this baseline.
Planning and inspection do not activate the candidate or change authority.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]


class BaselineRelationError(ValueError):
    pass


def _relative(root: Path, ref: str, prefix: str) -> Path:
    if not isinstance(ref, str) or not ref or Path(ref).is_absolute():
        raise BaselineRelationError("Expected repository-relative path")
    p = (root / ref).resolve()
    if not p.is_relative_to((root / prefix).resolve()) or not p.is_file():
        raise BaselineRelationError("Invalid scoped file: " + ref)
    return p


def _yaml(path: Path) -> dict:
    item = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(item, dict):
        raise BaselineRelationError("YAML must contain a mapping")
    return item


def _concept(root: Path, ref: str) -> dict:
    content = _relative(root, ref, "knowledge").read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\n---\n" not in content:
        raise BaselineRelationError("Invalid OKF frontmatter: " + ref)
    doc = yaml.safe_load(content.split("\n---\n", 1)[0][4:])
    if not isinstance(doc, dict) or not isinstance(doc.get("relations"), list):
        raise BaselineRelationError("Missing typed concept relations: " + ref)
    return doc


def _knowledge_ref(repo_path: str) -> str:
    if not repo_path.startswith("knowledge/"):
        raise BaselineRelationError("Override targets must be knowledge concepts")
    return "/" + repo_path.removeprefix("knowledge/")


def resolve(root: Path, ref: str) -> dict:
    root = root.resolve()
    baseline = _yaml(_relative(root, ref, "process/baselines"))
    if (baseline.get("schema") != "pc-baseline-candidate/v1"
            or baseline.get("status") != "pending_independent_baseline_review"
            or baseline.get("review_required_before_activation") is not True):
        raise BaselineRelationError("Not an independently reviewable baseline candidate")
    source = baseline.get("candidate_active_as")
    target = baseline.get("candidate_active_verification_plan")
    _relative(root, source, "knowledge")
    _relative(root, target, "knowledge")
    rels = _concept(root, source)["relations"]
    overrides = baseline.get("effective_relation_overrides", [])
    if not isinstance(overrides, list) or not overrides:
        raise BaselineRelationError("No explicit effective relation override")
    effective = [dict(x) for x in rels if isinstance(x, dict)]
    changes = []
    seen = set()
    for entry in overrides:
        if not isinstance(entry, dict):
            raise BaselineRelationError("Malformed relation override")
        src, kind = entry.get("source"), entry.get("kind")
        before, after = entry.get("historical_target"), entry.get("active_target")
        authority = entry.get("selection_authority")
        if (src != source or kind != "specifies" or after != target
                or entry.get("scope") != "this_baseline_only_after_independent_acceptance"):
            raise BaselineRelationError("Override does not match selected AS/VP relationship")
        if (src, kind, before) in seen:
            raise BaselineRelationError("Duplicate effective relation override")
        seen.add((src, kind, before))
        before_ref = _knowledge_ref(before)
        after_ref = _knowledge_ref(after)
        _relative(root, before, "knowledge")
        _relative(root, after, "knowledge")
        if before_ref == after_ref:
            raise BaselineRelationError("Override must select a changed target")
        matches = [x for x in effective if x.get("kind") == kind and x.get("target") == before_ref]
        if len(matches) != 1:
            raise BaselineRelationError("Superseded edge not uniquely present in historical AS")
        review = json.loads(_relative(root, authority, "reviews").read_text(encoding="utf-8"))
        claims = {x.get("path") for x in review.get("candidate_artifacts", [])
                  if isinstance(x, dict)}
        if (review.get("gate") != "AS_REVIEW"
                or review.get("independent_of_authoring_invocation") is not True
                or review.get("disposition") not in ("ACCEPT", "ACCEPT_WITH_CLARIFICATIONS")
                or source not in claims or after not in claims):
            raise BaselineRelationError("Replacement edge lacks favorable independent source review")
        matches[0]["target"] = after_ref
        changes.append({"source": source, "kind": kind,
                        "historical_target": before, "active_target": after,
                        "selection_authority": authority})
    # Check this chosen source's currently applicable verification-plan edge.
    chosen = [x["target"] for x in effective if x.get("kind") == "specifies"
              and x.get("target") == _knowledge_ref(target)]
    if len(chosen) != 1:
        raise BaselineRelationError("Active AS does not specify exactly one selected VP")
    return {"baseline": ref, "status": "CANDIDATE_NOT_ACTIVE",
            "active_source": source, "effective_relations": effective,
            "overrides": changes}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect",))
    parser.add_argument("--baseline", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(resolve(ROOT, args.baseline), indent=2))
    except (OSError, yaml.YAMLError, json.JSONDecodeError,
            BaselineRelationError, TypeError, KeyError) as exc:
        print("BASELINE_RELATION_INVALID:", exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
