"""Regression checks for activation review pins and open VO preservation."""
import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import active_baseline

ACTIVE = "process/baselines/AS-001-v2-active.yaml"


class ActiveBaselineTests(unittest.TestCase):
    def test_reviewed_baseline_resolves_and_preserves_open_VOs(self):
        checked = active_baseline.verify(ROOT, ACTIVE)
        self.assertEqual(checked["status"], "ACTIVE_BASELINE_VERIFIED")
        self.assertEqual(checked["selected_ap"], "AP-002")
        self.assertEqual(
            checked["open_vos"],
            ["VO-002", "VO-003", "VO-004", "VO-005", "VO-006"]
        )
        self.assertTrue(any(x["active_target"].endswith("verification_plan-v3.md")
                            for x in checked["effective_relations"]))

    def test_generic_contract_task_uses_activated_baseline(self):
        import task
        result = task.validate(ROOT, "process/tasks/TOY1-CON005-MINIMAL.yaml")
        self.assertEqual(result["operation"], "DEFINE_CON")
        self.assertEqual(result["trigger"], "BASELINE_ACTIVATED")

    def test_contract_task_does_not_ignore_failed_baseline_guard(self):
        import task
        with patch.object(active_baseline, "verify",
                          side_effect=active_baseline.ActiveBaselineError("stale review")):
            with self.assertRaisesRegex(task.TaskError, "invalid active baseline"):
                task.validate(ROOT, "process/tasks/TOY1-CON005-MINIMAL.yaml")

    def test_nonaccepting_review_blocks_active_baseline(self):
        original = active_baseline._review
        def changed(root, path):
            result = copy.deepcopy(original(root, path))
            if path.endswith("TOY1-BASELINE002-independent-review.json"):
                result["disposition"] = "REVISE"
            return result
        with patch.object(active_baseline, "_review", side_effect=changed):
            with self.assertRaisesRegex(active_baseline.ActiveBaselineError, "favorable"):
                active_baseline.verify(ROOT, ACTIVE)

    def test_changed_candidate_hash_blocks_baseline(self):
        original = active_baseline._hash
        def changed(root, path, directory):
            if path == "process/baselines/AS-001-v2-candidate-r2.yaml":
                return "0" * 64
            return original(root, path, directory)
        with patch.object(active_baseline, "_hash", side_effect=changed):
            with self.assertRaisesRegex(active_baseline.ActiveBaselineError, "reviewed bytes"):
                active_baseline.verify(ROOT, ACTIVE)

    def test_changed_vo_state_blocks_baseline(self):
        original = active_baseline._yaml
        def changed(root, path, directory):
            doc = copy.deepcopy(original(root, path, directory))
            if path == "process/ledgers/vo_ledger-AS-001-v2-active.yaml":
                for row in doc["obligations"]:
                    if row["id"] == "VO-004":
                        row["state"] = "discharged"
            return doc
        with patch.object(active_baseline, "_yaml", side_effect=changed):
            with self.assertRaisesRegex(active_baseline.ActiveBaselineError, "differ from reviewed proposal"):
                active_baseline.verify(ROOT, ACTIVE)

    def test_unapproved_ap_blocks_baseline(self):
        original = active_baseline._yaml
        def changed(root, path, directory):
            doc = copy.deepcopy(original(root, path, directory))
            if path == "process/decisions/AP-002-AS-V2-RECONFIRMATION-001.yaml":
                doc["status"] = "proposed"
            return doc
        with patch.object(active_baseline, "_yaml", side_effect=changed):
            with self.assertRaisesRegex(active_baseline.ActiveBaselineError, "accepted provisional AP"):
                active_baseline.verify(ROOT, ACTIVE)


if __name__ == "__main__":
    unittest.main()
