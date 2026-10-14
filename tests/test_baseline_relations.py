"""Baseline-scoped effective relations must preserve history and source authority."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import baseline_relations


class BaselineRelationsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = "knowledge/architecture/beta/statement-v2.md"
        self.old = "knowledge/architecture/beta/verification_plan-v2.md"
        self.new = "knowledge/architecture/beta/verification_plan-v3.md"
        self.review_ref = "reviews/gates/as-review.json"
        self.baseline_ref = "process/baselines/beta-v2.yaml"
        self._put(self.source,
                  "---\ntype: Architecture Statement\nid: AS-BETA-v2\n"
                  "relations:\n  - kind: specifies\n"
                  "    target: /architecture/beta/verification_plan-v2.md\n"
                  "---\n# Immutable historical AS\n")
        self._put(self.old, "# Old VP\n")
        self._put(self.new, "# Reviewed VP\n")
        self._put(self.review_ref, json.dumps({
            "gate": "AS_REVIEW",
            "independent_of_authoring_invocation": True,
            "disposition": "ACCEPT_WITH_CLARIFICATIONS",
            "candidate_artifacts": [{"path": self.source}, {"path": self.new}],
        }))
        self.baseline = {
            "schema": "pc-baseline-candidate/v1",
            "status": "pending_independent_baseline_review",
            "review_required_before_activation": True,
            "candidate_active_as": self.source,
            "candidate_active_verification_plan": self.new,
            "effective_relation_overrides": [{
                "source": self.source,
                "kind": "specifies",
                "historical_target": self.old,
                "active_target": self.new,
                "scope": "this_baseline_only_after_independent_acceptance",
                "selection_authority": self.review_ref,
            }],
        }
        self._save()

    def _put(self, ref, data):
        path = self.root / ref
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data, encoding="utf-8")
        return path

    def _save(self):
        self._put(self.baseline_ref, yaml.safe_dump(self.baseline))

    def test_reviewed_edge_selected_without_mutating_original(self):
        original = (self.root / self.source).read_text()
        result = baseline_relations.resolve(self.root, self.baseline_ref)
        self.assertEqual(result["status"], "CANDIDATE_NOT_ACTIVE")
        self.assertIn("/architecture/beta/verification_plan-v3.md",
                      [r["target"] for r in result["effective_relations"]])
        self.assertEqual((self.root / self.source).read_text(), original)

    def test_reject_missing_historical_edge(self):
        self.baseline["effective_relation_overrides"][0]["historical_target"] = self.new
        self._save()
        with self.assertRaises(baseline_relations.BaselineRelationError):
            baseline_relations.resolve(self.root, self.baseline_ref)

    def test_reject_unreviewed_replacement(self):
        review = json.loads((self.root / self.review_ref).read_text())
        review["candidate_artifacts"] = [{"path": self.source}]
        self._put(self.review_ref, json.dumps(review))
        with self.assertRaisesRegex(baseline_relations.BaselineRelationError, "favorable independent"):
            baseline_relations.resolve(self.root, self.baseline_ref)

    def test_reject_unaccepted_projection(self):
        self.baseline["status"] = "approved"
        self._save()
        with self.assertRaisesRegex(baseline_relations.BaselineRelationError, "Not an independently"):
            baseline_relations.resolve(self.root, self.baseline_ref)

    def test_reject_unrelated_source_or_target(self):
        self.baseline["effective_relation_overrides"][0]["active_target"] = self.old
        self._save()
        with self.assertRaisesRegex(baseline_relations.BaselineRelationError, "does not match selected"):
            baseline_relations.resolve(self.root, self.baseline_ref)

    def test_reject_nonindependent_source_review(self):
        review = json.loads((self.root / self.review_ref).read_text())
        review["independent_of_authoring_invocation"] = False
        self._put(self.review_ref, json.dumps(review))
        with self.assertRaisesRegex(baseline_relations.BaselineRelationError, "favorable independent"):
            baseline_relations.resolve(self.root, self.baseline_ref)


if __name__ == "__main__":
    unittest.main()
