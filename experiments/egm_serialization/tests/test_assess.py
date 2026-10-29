"""Local, offline unit tests for EGM-P0 structural checker only."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import assess  # noqa: E402


def reference():
    return {
        "schema": assess.REF_SCHEMA, "project_id": "ROOT-002",
        "allowed_source_ids": ["contract-source", "de-source", "proof-source"],
        "required_facts": [
            {"id": "CON-1", "kind": "CONTRACT", "authority": "ACCEPTED",
             "source_ids": ["contract-source"]},
            {"id": "PR-1", "kind": "PROOF", "authority": "ACCEPTED",
             "source_ids": ["proof-source"],
             "proof_conditions": ["assume-ordered"]},
            {"id": "DE-1", "kind": "MODULE", "authority": "PROPOSED",
             "source_ids": ["de-source"]},
        ],
        "required_relations": [
            {"from": "DE-1", "type": "IMPLEMENTS", "to": "CON-1"},
            {"from": "CON-1", "type": "PROVEN_BY", "to": "PR-1"},
        ],
    }


def goldfish():
    r = reference()
    return {
        "schema": assess.GOLDFISH_SCHEMA, "project_id": r["project_id"],
        "traversed_source_ids": list(r["allowed_source_ids"]),
        "facts": [dict(f) for f in r["required_facts"]],
        "relations": [dict(edge) for edge in r["required_relations"]],
        "unknowns": [],
    }


class AssessTests(unittest.TestCase):
    def test_matching_is_structural_not_semantic_acceptance(self):
        x = assess.compare(reference(), goldfish())
        self.assertTrue(x["structural_match"])
        self.assertFalse(x["authority_accepted"])
        self.assertEqual(x["semantic_review"], "NOT_PERFORMED")
        self.assertEqual(x["findings"], [])

    def test_missing_edge_detected(self):
        g = goldfish()
        g["relations"].pop()
        result = assess.compare(reference(), g)
        self.assertFalse(result["structural_match"])
        self.assertIn("MISSING_RELATION", [f["kind"] for f in result["findings"]])

    def test_missing_proof_condition_detected(self):
        g = goldfish()
        g["facts"][1]["proof_conditions"] = []
        result = assess.compare(reference(), g)
        self.assertIn("MISSING_PROOF_SCOPE", [f["kind"] for f in result["findings"]])

    def test_misclassified_authority_detected(self):
        g = goldfish()
        g["facts"][0]["authority"] = "PROPOSED"
        result = assess.compare(reference(), g)
        self.assertIn("MISCLASSIFIED_FACT", [f["kind"] for f in result["findings"]])

    def test_unexpected_fact_detected(self):
        g = goldfish()
        g["facts"].append({"id": "FAKE-PROVIDER", "kind": "MODULE",
                           "authority": "ACCEPTED", "source_ids": ["de-source"]})
        result = assess.compare(reference(), g)
        self.assertIn("UNEXPECTED_ASSERTION", [f["kind"] for f in result["findings"]])

    def test_unknown_is_visible_not_passed(self):
        g = goldfish()
        g["facts"] = g["facts"][:-1]
        g["relations"] = [x for x in g["relations"] if x["from"] != "DE-1"]
        g["unknowns"] = [{"id": "DE-1", "reason": "No module definition in projection",
                          "source_ids": ["de-source"]}]
        result = assess.compare(reference(), g)
        self.assertFalse(result["structural_match"])
        self.assertIn("DE-1", result["declared_unknowns"])

    def test_unallowlisted_source_fails_closed(self):
        g = goldfish()
        g["facts"][0]["source_ids"] = ["not-allowed"]
        with self.assertRaises(assess.Invalid):
            assess.compare(reference(), g)

    def test_duplicate_fact_fails_closed(self):
        g = goldfish()
        g["facts"].append(dict(g["facts"][0]))
        with self.assertRaises(assess.Invalid):
            assess.compare(reference(), g)

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "dup.json"
            source.write_text('{"schema":"x","schema":"y"}', encoding="utf-8")
            with self.assertRaises(assess.Invalid):
                assess.load(source, "x")

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            r = Path(directory) / "reference.json"
            g = Path(directory) / "goldfish.json"
            r.write_text(json.dumps(reference()), encoding="utf-8")
            g.write_text(json.dumps(goldfish()), encoding="utf-8")
            self.assertEqual(assess.main(["--reference", str(r),
                                          "--reconstruction", str(g)]), 0)
            bad = goldfish()
            bad["relations"].pop()
            g.write_text(json.dumps(bad), encoding="utf-8")
            self.assertEqual(assess.main(["--reference", str(r),
                                          "--reconstruction", str(g)]), 1)
            g.write_text("not json", encoding="utf-8")
            self.assertEqual(assess.main(["--reference", str(r),
                                          "--reconstruction", str(g)]), 2)


if __name__ == "__main__":
    unittest.main()
