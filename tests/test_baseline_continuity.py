"""FR-002 transition tests. Synthetic records do not grant project authority."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from gates import continuity


class BaselineContinuityTests(unittest.TestCase):
    def case(self):
        accepted = {
            "schema": "pc-project-ap-continuity/v1",
            "status": "candidate_for_independent_review",
            "id": "NUM-001", "project_id": "ROOT-002",
            "spine": "/architecture/ROOT-002/spine.md", "stage": "AP",
            "active_baseline": {"path": "baselines/ROOT.yaml"},
            "required_validators": [{"requirement": "R-NUM", "id": "NUM"}],
        }
        candidate = {
            "project_id": accepted["project_id"], "spine": accepted["spine"],
            "stage": "AP", "active_baseline": accepted["active_baseline"],
            "required_validators": [],
        }
        return accepted, candidate

    def test_silent_removal_is_rejected(self):
        old, new = self.case()
        with self.assertRaisesRegex(ValueError, "continuity mismatch"):
            continuity.compare(old, new)

    def test_recorded_transition_can_authorize_synthetic_change(self):
        old, new = self.case()
        transition = {
            "schema": "pc-project-authority-transition/v1",
            "status": "accepted", "project_id": "ROOT-002",
            "previous_projection_id": old["id"],
            "previous_baseline": old["active_baseline"]["path"],
            "approved_by": "SIMULATED", "approval_evidence": "SIMULATED_REVIEW",
            "replacements": {"required_validators": []},
        }
        self.assertIs(continuity.compare(old, new, transition), new)
        transition["status"] = "proposed"
        with self.assertRaisesRegex(ValueError, "not approved"):
            continuity.compare(old, new, transition)

    def test_explicit_project_validator_registration(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        from gates import binding
        plugin = SimpleNamespace(
            VALIDATOR_ID="ROOT-NUM", PROJECT_ID="ROOT-002",
            REQUIREMENT="R-NUM",
            validate_scope=lambda *args, **kwargs: ([], []),
            validate_requirement=lambda *args: [],
        )
        with patch.dict(binding.REGISTRY, {}, clear=False):
            binding.register_validator(plugin)
            self.assertIs(binding.REGISTRY["ROOT-NUM"], plugin)
            with self.assertRaisesRegex(ValueError, "already registered"):
                binding.register_validator(SimpleNamespace(
                    VALIDATOR_ID="ROOT-NUM", PROJECT_ID="ROOT-002",
                    REQUIREMENT="R-NUM",
                    validate_scope=lambda *args: ([], []),
                    validate_requirement=lambda *args: [],
                ))

    def test_noncontract_change_is_rejected(self):
        old, new = self.case()
        record = {
            "schema": "pc-project-authority-transition/v1",
            "status": "accepted", "project_id": "ROOT-002",
            "previous_projection_id": old["id"],
            "previous_baseline": old["active_baseline"]["path"],
            "approved_by": "SIMULATED", "approval_evidence": "SIMULATED",
            "replacements": {"unrelated": 2},
        }
        with self.assertRaisesRegex(ValueError, "unsupported contract field"):
            continuity.compare(old, new, record)


if __name__ == "__main__":
    unittest.main()
