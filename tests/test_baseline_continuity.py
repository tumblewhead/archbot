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

    def test_root_002_uses_project_bound_loader(self):
        from tempfile import TemporaryDirectory
        import yaml
        from gates.binding import blob_id, load_binding

        with TemporaryDirectory() as directory:
            root = Path(directory)

            def file(path, document):
                dest = root / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(yaml.safe_dump(document), encoding="utf-8")
                entry = {"path": path, "git_blob_sha1": blob_id(dest.read_bytes())}
                if isinstance(document.get("id"), str):
                    entry["id"] = document["id"]
                return entry

            bp = "baselines/ROOT-002.yaml"
            rp = "reviews/ROOT-002.yaml"
            vp = "ledgers/ROOT-002.yaml"
            spine = "/architecture/ROOT-002/spine.md"
            shared = {
                "project_id": "ROOT-002", "spine": spine, "stage": "AP",
                "spine_source": file("knowledge" + spine, {"id": "ROOT-002"}),
                "active_baseline": file(bp, {
                    "schema": "pc-active-baseline/v1", "id": "ROOT-V1",
                    "status": "active", "source_candidate": "source/root.yaml",
                    "source_candidate_sha256": "synthetic-source",
                    "independent_baseline_review": rp,
                    "active_artifacts": {
                        "architecture_statement": "knowledge/architecture/ROOT-002/statement.md",
                        "vo_ledger": vp,
                    },
                }),
                "baseline_review": file(rp, {
                    "schema": "pc-baseline-review/v1",
                    "independent_of_baseline_authoring_invocation": True,
                    "disposition": "ACCEPT_WITH_CLARIFICATIONS",
                    "candidate": "source/root.yaml",
                    "candidate_sha256": "synthetic-source",
                }),
                "policy": file("policies/ROOT-AP.yaml", {
                    "id": "ROOT-AP", "status": "approved_for_trial",
                    "selection_kind": "PROVISIONAL_COMMITMENT",
                    "requirements": ["R-NUM"], "protected_scope_decisions": [],
                }),
                "vo_ledger": file(vp, {
                    "activation": {"active_baseline": bp, "reviewed_baseline": rp},
                    "obligations": [],
                }),
                "ad_ledger": file("ledgers/ROOT-AD.yaml", {"items": []}),
                "required_validators": [],
            }
            projection = {
                **shared, "schema": "pc-project-ap-continuity/v1",
                "id": "ROOT-PROJECTION-001",
                "status": "candidate_for_independent_review",
            }
            p = file("project/ROOT-projection.yaml", projection)
            candidate = {
                **shared, "schema": "pc-ap-gate-binding/v1",
                "status": "candidate_for_independent_review",
                "accepted_projection": p,
            }
            path = "gates/ROOT-binding.yaml"
            file(path, candidate)
            resolved, policy, _, _, validators = load_binding(root, path)
            self.assertEqual(resolved["project_id"], "ROOT-002")
            self.assertEqual(policy["id"], "ROOT-AP")
            self.assertEqual(validators, [])
            self.assertEqual(resolved["_projection_status"],
                             "candidate_for_independent_review")

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
