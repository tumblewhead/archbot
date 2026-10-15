"""FR-002 cooperative baseline continuity and Toy 1 compatibility tests.

Synthetic projects are simulations, not actual engineering approvals.
"""
from __future__ import annotations
import copy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import stage_gate
from gates import binding, common
from gates.binding import blob_id, evaluate_bound, load_binding

TOY1 = "process/gate_configs/AS-001-AP-continuity-candidate-v2.yaml"


def write_pinned(root, name, value):
    target = root / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
    spec = {"path": name, "git_blob_sha1": blob_id(target.read_bytes())}
    if isinstance(value, dict) and isinstance(value.get("id"), str):
        spec["id"] = value["id"]
    return spec


class GateAdapterTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.toy1 = yaml.safe_load((ROOT / TOY1).read_text())
        self.projection = yaml.safe_load(
            (ROOT / self.toy1["accepted_projection"]["path"]).read_text())
        refs = [self.toy1["accepted_projection"]]
        for key in ("spine_source", "active_baseline", "baseline_review",
                    "policy", "vo_ledger", "ad_ledger", "reviewed_as",
                    "approved_ap_authority"):
            refs.append(self.toy1[key])
        for item in self.toy1["required_validators"]:
            refs.extend((item["scope"], item["implementation"]))
        for item in refs:
            target = self.root / item["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / item["path"], target)
        previous = self.root / "process/gate_configs/AS-001-AP-v1.yaml"
        previous.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "process/gate_configs/AS-001-AP-v1.yaml", previous)
        self.write_binding(self.toy1)

    def write_binding(self, obj):
        p = self.root / TOY1
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(yaml.safe_dump(obj, sort_keys=False), encoding="utf-8")

    def test_toy1_binding_preserves_c002(self):
        obj, policy, vo, ad, validators = load_binding(self.root, TOY1)
        self.assertEqual(obj["project_id"], "AS-001")
        self.assertEqual(obj["_projection_status"], "candidate_for_independent_review")
        self.assertEqual(policy["protected_scope_decisions"], ["C-002"])
        self.assertEqual([v["requirement"] for v in validators], ["C-002"])
        self.assertEqual(validators[0]["scope"]["accounting"]["limit_bytes"], 2048)
        self.assertEqual(vo["status"], "active")
        self.assertTrue(ad["items"])

    def test_accepted_baseline_never_silently_loses_validator(self):
        for candidate in ([], self.toy1["required_validators"] * 2,
                          [{"id": "UNKNOWN", "requirement": "C-002"}]):
            with self.subTest(candidate=candidate):
                obj = copy.deepcopy(self.toy1)
                obj["required_validators"] = candidate
                self.write_binding(obj)
                with self.assertRaisesRegex(ValueError, "continuity mismatch"):
                    load_binding(self.root, TOY1)

    def test_policy_repin_without_reviewed_transition_fails(self):
        obj = copy.deepcopy(self.toy1)
        old = obj["policy"]["path"]
        policy = yaml.safe_load((self.root / old).read_text())
        policy["protected_scope_decisions"] = []
        obj["policy"] = write_pinned(self.root, old, policy)
        obj["required_validators"] = []
        self.write_binding(obj)
        with self.assertRaisesRegex(ValueError, "continuity mismatch"):
            load_binding(self.root, TOY1)

    def test_baseline_review_and_ledger_substitution_fail(self):
        for key in ("active_baseline", "baseline_review", "vo_ledger",
                    "ad_ledger", "reviewed_as", "approved_ap_authority"):
            with self.subTest(key=key):
                obj = copy.deepcopy(self.toy1)
                obj[key] = {"path": "different.yaml", "git_blob_sha1": "0" * 40}
                self.write_binding(obj)
                with self.assertRaisesRegex(ValueError, "continuity mismatch"):
                    load_binding(self.root, TOY1)

    def test_scope_and_validator_implementation_cannot_be_lost(self):
        for key in ("scope", "implementation"):
            with self.subTest(key=key):
                obj = copy.deepcopy(self.toy1)
                obj["required_validators"][0][key]["git_blob_sha1"] = "0" * 40
                self.write_binding(obj)
                with self.assertRaisesRegex(ValueError, "continuity mismatch"):
                    load_binding(self.root, TOY1)

    def test_explicit_projection_and_project_identity_required(self):
        obj = copy.deepcopy(self.toy1)
        obj.pop("accepted_projection")
        self.write_binding(obj)
        with self.assertRaisesRegex(ValueError, "projection required"):
            load_binding(self.root, TOY1)
        obj = copy.deepcopy(self.toy1)
        obj["project_id"] = "ROOT-002"
        obj["spine"] = "/architecture/ROOT-002/spine.md"
        self.write_binding(obj)
        with self.assertRaisesRegex(ValueError, "continuity identity"):
            load_binding(self.root, TOY1)

    def test_candidate_status_cannot_grant_real_eligibility(self):
        obj, policy, vo, ad, active = load_binding(self.root, TOY1)
        self.assertEqual(obj["_projection_status"], "candidate_for_independent_review")
        # The candidate continuity projection must not produce genuine
        # eligibility even with an otherwise permitted assessment.
        with patch.object(common, "evaluate", return_value={
            "decision": "ELIGIBLE_FOR_INDEPENDENT_REVIEW", "errors": [], "notes": []}):
            result = evaluate_bound(self.root, TOY1, {"simulation_only": False})
        self.assertEqual(result["decision"], "NO_DOWNSELECTION")
        self.assertIn("Project continuity projection is not independently accepted",
                      result["errors"])

    def test_fake_accepted_projection_needs_review_and_approval(self):
        projection = copy.deepcopy(self.projection)
        projection["status"] = "accepted_for_trial"
        ref = write_pinned(self.root, self.toy1["accepted_projection"]["path"], projection)
        obj = copy.deepcopy(self.toy1)
        obj["accepted_projection"] = ref
        self.write_binding(obj)
        with self.assertRaisesRegex(ValueError, "lacks review and approval"):
            load_binding(self.root, TOY1)

    def test_legacy_and_explicit_modes(self):
        with self.assertRaises(SystemExit) as raised:
            stage_gate.main(["inspect"])
        self.assertEqual(raised.exception.code, 2)
        self.assertEqual(stage_gate.main(["inspect", "--binding", TOY1]), 0)
        self.assertEqual(stage_gate.main(["inspect", "--legacy-toy1"]), 0)

    def test_previous_binding_is_historical_not_a_default(self):
        with self.assertRaisesRegex(ValueError, "projection required"):
            load_binding(self.root, "process/gate_configs/AS-001-AP-v1.yaml")

    def test_common_gate_has_no_toy1_domain_numbers(self):
        source = (ROOT / "tools/gates/common.py").read_text()
        for token in ("AS-001", "C-002", "F-001", "2048"):
            self.assertNotIn(token, source)
        code = (ROOT / "tools/gates/binding.py").read_text()
        self.assertNotIn("trusted_root", code)
        self.assertNotIn("AS-001", code)


if __name__ == "__main__":
    unittest.main()
