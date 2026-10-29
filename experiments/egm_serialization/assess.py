#!/usr/bin/env python3
"""EGM-P0 deterministic STRUCTURAL reconstruction comparison, offline/stdlib.

Never send the --reference file to the Goldfish. The expected reference
is evaluator-only, source-grounded data, NOT automated engineering authority.
Exit 0 = structural match; 1 = discrepancy; 2 = invalid input.
No filesystem writes. This is not semantic review or cleanroom qualification.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:/-]{0,191}$")
KINDS = {"REQUIREMENT", "ASSUMPTION", "PROOF", "CONTRACT", "MODULE",
         "INTERFACE", "IMPLEMENTATION", "RESOURCE", "VERIFICATION"}
AUTHORITY = {"PROPOSED", "ACCEPTED", "UNRESOLVED", "REVIEWED_ONLY"}
RELATIONS = {"DEPENDS_ON", "REFINES", "IMPLEMENTS", "PROVEN_BY",
             "TESTED_BY", "OWNS", "PROVIDES", "CONSTRAINS"}
REF_SCHEMA = "pc-egm-evaluator-reference/v0"
GOLDFISH_SCHEMA = "pc-egm-goldfish-reconstruction/v0"


class Invalid(ValueError):
    pass


def duplicates(items):
    result = {}
    for k, v in items:
        if k in result:
            raise Invalid("Duplicate JSON property: " + k)
        result[k] = v
    return result


def load(path, expected_schema):
    try:
        raw = Path(path).read_text(encoding="utf-8")
        obj = json.loads(raw, object_pairs_hook=duplicates,
                         parse_constant=lambda x: (_ for _ in ()).throw(Invalid(x)))
    except (OSError, UnicodeError, ValueError) as e:
        raise Invalid("Cannot read/parse JSON: " + str(e)) from e
    if not isinstance(obj, dict) or obj.get("schema") != expected_schema:
        raise Invalid("Wrong schema for " + str(path))
    return obj


def identifier(x, label):
    if not isinstance(x, str) or not ID.fullmatch(x):
        raise Invalid("Invalid " + label + ": " + repr(x))
    return x


def string_ids(x, label):
    if not isinstance(x, list):
        raise Invalid(label + " must be an array")
    seen = set()
    for v in x:
        identifier(v, label)
        if v in seen:
            raise Invalid("Duplicate " + label + ": " + v)
        seen.add(v)
    return seen


def facts(values, label, allowed_sources):
    if not isinstance(values, list):
        raise Invalid(label + " must be an array")
    out = {}
    for f in values:
        if not isinstance(f, dict):
            raise Invalid(label + " fact must be an object")
        fid = identifier(f.get("id"), "fact ID")
        if fid in out:
            raise Invalid("Duplicate fact ID: " + fid)
        kind = f.get("kind")
        authority = f.get("authority")
        if kind not in KINDS or authority not in AUTHORITY:
            raise Invalid("Invalid kind/authority for " + fid)
        sources = string_ids(f.get("source_ids"), fid + " source_ids")
        if not sources or not sources <= allowed_sources:
            raise Invalid("Fact has missing/unallowlisted source: " + fid)
        conditions = string_ids(f.get("proof_conditions", []),
                                fid + " proof_conditions")
        out[fid] = {"kind": kind, "authority": authority,
                    "source_ids": sources, "proof_conditions": conditions}
    return out


def relations(values, label, fact_ids):
    if not isinstance(values, list):
        raise Invalid(label + " must be an array")
    output = set()
    for x in values:
        if not isinstance(x, dict):
            raise Invalid("Relation must be an object")
        src = identifier(x.get("from"), "relation from")
        dst = identifier(x.get("to"), "relation to")
        typ = x.get("type")
        if typ not in RELATIONS or src not in fact_ids or dst not in fact_ids:
            raise Invalid("Invalid or dangling relation: " + repr(x))
        edge = (src, typ, dst)
        if edge in output:
            raise Invalid("Duplicate relation: " + repr(edge))
        output.add(edge)
    return output


def unknowns(values, fact_ids, source_ids):
    if not isinstance(values, list):
        raise Invalid("unknowns must be an array")
    out = {}
    for x in values:
        if not isinstance(x, dict):
            raise Invalid("Unknown entry must be an object")
        fid = identifier(x.get("id"), "unknown fact ID")
        reason = x.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise Invalid("Unknown requires reason: " + fid)
        if fid in out or fid in fact_ids:
            raise Invalid("Unknown collides/duplicates: " + fid)
        refs = string_ids(x.get("source_ids", []), "unknown sources")
        if not refs <= source_ids:
            raise Invalid("Unknown cites unallowlisted source")
        out[fid] = reason
    return out


def compare(reference, output):
    if reference.get("project_id") != output.get("project_id"):
        raise Invalid("Project identity differs")
    identifier(reference.get("project_id"), "project ID")
    sources = string_ids(reference.get("allowed_source_ids"),
                         "allowed_source_ids")
    if not sources:
        raise Invalid("Reference has no allowed sources")
    claimed_sources = string_ids(output.get("traversed_source_ids", []),
                                 "traversed_source_ids")
    if not claimed_sources <= sources:
        raise Invalid("Goldfish claims sources outside input allowlist")
    required = facts(reference.get("required_facts"), "required_facts", sources)
    observed = facts(output.get("facts"), "facts", sources)
    expected_edges = relations(reference.get("required_relations"),
                               "required_relations", required)
    actual_edges = relations(output.get("relations"), "relations", observed)
    declared_unknowns = unknowns(output.get("unknowns", []), set(observed), sources)
    findings = []
    def report(kind, subject, detail):
        findings.append({"kind": kind, "subject": subject, "detail": detail})
    for fid, expected in sorted(required.items()):
        current = observed.get(fid)
        if current is None:
            report("MISSING_FACT", fid, "Declared UNKNOWN" if fid in declared_unknowns else "Not reconstructed")
            continue
        for field in ("kind", "authority"):
            if expected[field] != current[field]:
                report("MISCLASSIFIED_FACT", fid, field)
        for ref in sorted(expected["source_ids"] - current["source_ids"]):
            report("MISSING_PROVENANCE", fid, ref)
        for proof in sorted(expected["proof_conditions"] - current["proof_conditions"]):
            report("MISSING_PROOF_SCOPE", fid, proof)
        for extra in sorted(current["proof_conditions"] - expected["proof_conditions"]):
            report("UNSUPPORTED_PROOF_SCOPE", fid, extra)
    for fid in sorted(set(observed) - set(required)):
        report("UNEXPECTED_ASSERTION", fid, "Needs separate semantic source review")
    for edge in sorted(expected_edges - actual_edges):
        report("MISSING_RELATION", "/".join(edge), "Required typed dependency")
    for edge in sorted(actual_edges - expected_edges):
        report("UNEXPECTED_RELATION", "/".join(edge), "Not in reference; review separately")
    result = {
        "schema": "pc-egm-structural-assessment/v0",
        "project_id": reference["project_id"],
        "structural_match": not findings,
        "semantic_review": "NOT_PERFORMED",
        "authority_accepted": False,
        "runtime_isolation_verified": False,
        "required_fact_count": len(required),
        "reconstructed_fact_count": len(observed),
        "required_relation_count": len(expected_edges),
        "reconstructed_relation_count": len(actual_edges),
        "traversed_source_count": len(claimed_sources),
        "declared_unknowns": sorted(declared_unknowns),
        "findings": findings,
    }
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reference", required=True, help="Evaluator ONLY, never worker input")
    ap.add_argument("--reconstruction", required=True, help="Goldfish output")
    args = ap.parse_args(argv)
    try:
        ref = load(args.reference, REF_SCHEMA)
        gold = load(args.reconstruction, GOLDFISH_SCHEMA)
        result = compare(ref, gold)
    except Invalid as e:
        print(json.dumps({"error": str(e), "structural_match": False,
                          "authority_accepted": False}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["structural_match"] else 1


if __name__ == "__main__":
    sys.exit(main())
