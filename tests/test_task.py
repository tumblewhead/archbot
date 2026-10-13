"""Task manifests are reusable across architectures; they never grant approval."""
from pathlib import Path
import sys
import tempfile
import json
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task


class TaskManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for p, content in {
            "agents/evaluation-agent.md": "# Evaluator\n",
            "process/views.yaml": yaml.safe_dump({"roles": {"evaluation-agent": {"follow": []}}}),
            "process/operations.yaml": yaml.safe_dump({"operations": {
                "EVALUATE_AP": {
                    "role": "evaluation-agent",
                    "playbook": "process/playbooks/EVALUATE_AP.md",
                },
            }}),
            "process/playbooks/EVALUATE_AP.md": "# Reusable playbook\n",
            "prompts/generic-task.md": "Do not approve architecture.\n",
            "knowledge/architecture/alpha/spine.md": "# Alpha\n",
            "knowledge/architecture/beta/spine.md": "# Beta\n",
            "reviews/gates/accepted.json": "{}\n",
        }.items():
            dest = self.root / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        self.manifest = {
            "schema": "pc-task/v1",
            "id": "TASK-001", "role": "evaluation-agent",
            "operation": "EVALUATE_AP",
            "spine": "/architecture/alpha/spine.md",
            "trigger": {
                "kind": "VERIFICATION_RECEIPT_ACCEPTED",
                "reference": "reviews/gates/accepted.json",
            },
            "playbook": "process/playbooks/EVALUATE_AP.md",
            "outputs": {"allowed": ["versioned_evaluation"],
                        "prohibited": ["approve_architecture"]},
            "gate": {"kind": "AP_PROVISIONAL_SELECTION",
                     "on_missing_evidence": "UNRESOLVED",
                     "require_independent_review": True},
        }
        self.store()

    def store(self):
        dest = self.root / "process/tasks/task.yaml"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(yaml.safe_dump(self.manifest), encoding="utf-8")

    def test_first_architecture(self):
        selected = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(selected["spine"], "/architecture/alpha/spine.md")
        self.assertIn("process/tasks/task.yaml", task.make_prompt(self.root, selected))

    def test_second_architecture_same_role_and_playbook(self):
        self.manifest["spine"] = "/architecture/beta/spine.md"
        self.store()
        selected = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(selected["spine"], "/architecture/beta/spine.md")
        self.assertEqual(selected["playbook"], "process/playbooks/EVALUATE_AP.md")

    def test_spine_escape_rejected(self):
        self.manifest["spine"] = "/../../etc/passwd"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_playbook_rejected(self):
        self.manifest["playbook"] = "process/playbooks/MISSING.md"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_operation_must_be_registered(self):
        self.manifest["operation"] = "IMPLEMENT_DE"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_role_and_playbook_pairing_must_match_registry(self):
        self.manifest["playbook"] = "process/playbooks/OTHER.md"
        (self.root / "process/playbooks/OTHER.md").write_text("# Other\n")
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def _make_contract_task(self):
        files = {
            "agents/contract-agent.md": "# Contract\n",
            "process/playbooks/DEFINE_CON.md": "# Define contracts\n",
            "process/decisions/approved.yaml": yaml.safe_dump({
                "status": "approved", "decision": "PROVISIONALLY_SELECTED",
                "selected_candidate": "AP-002", "authorizes": "CON_FIRST_DECOMPOSITION",
                "approved_by": "user:test_authority",
                "authority_evidence": "process/decisions/approval.md",
                "accepted_architectural_debt": ["AD-X"],
                "carried_verification_obligations": ["VO-X"],
            }),
            "process/decisions/approval.md": "# Human approval\n",
            "process/ledgers/ad_ledger.yaml": yaml.safe_dump({"items": [{
                "id": "AD-X", "state": "accepted",
                "accepted_decision": "process/decisions/approved.yaml",
            }]}),
            "process/ledgers/vo_ledger.yaml": yaml.safe_dump({"obligations": [{
                "id": "VO-X", "state": "open",
            }]}),
        }
        for name, content in files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        registry = yaml.safe_load((self.root / "process/operations.yaml").read_text())
        registry["operations"]["DEFINE_CON"] = {
            "role": "contract-agent",
            "playbook": "process/playbooks/DEFINE_CON.md",
        }
        (self.root / "process/operations.yaml").write_text(yaml.safe_dump(registry))
        views = yaml.safe_load((self.root / "process/views.yaml").read_text())
        views["roles"]["contract-agent"] = {"follow": []}
        (self.root / "process/views.yaml").write_text(yaml.safe_dump(views))
        self.manifest.update(role="contract-agent", operation="DEFINE_CON",
                             playbook="process/playbooks/DEFINE_CON.md",
                             trigger={"kind": "AP_PROVISIONALLY_SELECTED",
                                      "reference": "process/decisions/approved.yaml"},
                             context={"authority_inputs": {
                                 "accepted_selection": "process/decisions/approved.yaml",
                                 "ad_ledger": "process/ledgers/ad_ledger.yaml",
                                 "vo_ledger": "process/ledgers/vo_ledger.yaml",
                             }})
        self.store()

    def test_protected_selection_requires_accepted_debt(self):
        self._make_contract_task()
        result = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(result["operation"], "DEFINE_CON")
        ledger_path = self.root / "process/ledgers/ad_ledger.yaml"
        ledger = yaml.safe_load(ledger_path.read_text())
        ledger["items"][0]["state"] = "proposed"
        ledger_path.write_text(yaml.safe_dump(ledger))
        with self.assertRaisesRegex(task.TaskError, "unaccepted architectural debt"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_protected_selection_requires_explicit_authority(self):
        self._make_contract_task()
        decision_path = self.root / "process/decisions/approved.yaml"
        decision = yaml.safe_load(decision_path.read_text())
        decision["status"] = "pending"
        decision_path.write_text(yaml.safe_dump(decision))
        with self.assertRaisesRegex(task.TaskError, "missing accepted authority"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_protected_selection_preserves_open_vos(self):
        self._make_contract_task()
        ledger_path = self.root / "process/ledgers/vo_ledger.yaml"
        ledger = yaml.safe_load(ledger_path.read_text())
        ledger["obligations"][0]["state"] = "discharged"
        ledger_path.write_text(yaml.safe_dump(ledger))
        with self.assertRaisesRegex(task.TaskError, "carry an open verification obligation"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_generic_contract_review_operation_retargets_two_spines(self):
        # Role and playbook are unchanged between toy architectures.
        role_path = self.root / "agents/verification-agent.md"
        role_path.write_text("# Independent reviewer\n")
        playbook_path = self.root / "process/playbooks/REVIEW_CON.md"
        playbook_path.write_text("# Reusable contract review\n")
        views_path = self.root / "process/views.yaml"
        views = yaml.safe_load(views_path.read_text())
        views["roles"]["verification-agent"] = {"follow": []}
        views_path.write_text(yaml.safe_dump(views))
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text())
        registry["operations"]["REVIEW_CON"] = {
            "role": "verification-agent",
            "playbook": "process/playbooks/REVIEW_CON.md",
        }
        registry_path.write_text(yaml.safe_dump(registry))
        for name in ("alpha", "beta"):
            self.manifest.update(
                role="verification-agent",
                operation="REVIEW_CON",
                playbook="process/playbooks/REVIEW_CON.md",
                spine=f"/architecture/{name}/spine.md",
            )
            self.store()
            result = task.validate(self.root, "process/tasks/task.yaml")
            self.assertEqual(result["operation"], "REVIEW_CON")
            self.assertEqual(result["spine"], f"/architecture/{name}/spine.md")

    def _make_contract_correction_task(self):
        self._make_contract_task()
        review_path = self.root / "reviews/gates/con-review.json"
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_path.write_text(json.dumps({
            "gate": "CONTRACT_REVIEW", "disposition": "REVISE",
            "next_stage_recommendation": "CON_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "findings": [{"id": "F-01", "severity": "blocking"}],
        }))
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text())
        registry["operations"]["REVISE_CON"] = {
            "role": "contract-agent",
            "playbook": "process/playbooks/REVISE_CON.md",
        }
        registry_path.write_text(yaml.safe_dump(registry))
        (self.root / "process/playbooks/REVISE_CON.md").write_text("# Revise contracts\n")
        self.manifest.update(
            role="contract-agent", operation="REVISE_CON",
            playbook="process/playbooks/REVISE_CON.md",
            trigger={"kind": "CONTRACT_REVIEW_REVISION_REQUIRED",
                     "reference": "reviews/gates/con-review.json"},
        )
        self.store()
        return review_path

    def test_contract_revision_requires_independent_blocking_review(self):
        review_path = self._make_contract_correction_task()
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"],
            "REVISE_CON"
        )
        review = json.loads(review_path.read_text())
        review["disposition"] = "ACCEPT"
        review_path.write_text(json.dumps(review))
        with self.assertRaisesRegex(task.TaskError, "blocking REVISE"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_contract_revision_cannot_be_triggered_by_self_review(self):
        review_path = self._make_contract_correction_task()
        review = json.loads(review_path.read_text())
        review["independent_of_authoring_invocation"] = False
        review_path.write_text(json.dumps(review))
        with self.assertRaisesRegex(task.TaskError, "blocking REVISE"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_contract_revision_without_blocking_findings_is_rejected(self):
        review_path = self._make_contract_correction_task()
        review = json.loads(review_path.read_text())
        review["findings"][0]["severity"] = "nonblocking"
        review_path.write_text(json.dumps(review))
        with self.assertRaisesRegex(task.TaskError, "blocking REVISE"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_evidence_plan_must_have_real_artifacts(self):
        self._make_contract_task()
        report = self.root / "reviews/gates/evidence-plan.json"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps({
            "schema": "pc-evidence-plan/v1",
            "status": "EVIDENCE_PLAN_READY_FOR_REVISION",
            "plan_artifacts": ["reviews/gates/missing-plan.md"],
        }))
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text())
        registry["operations"]["REVISE_CON"] = {
            "role": "contract-agent",
            "playbook": "process/playbooks/REVISE_CON.md",
        }
        registry_path.write_text(yaml.safe_dump(registry))
        (self.root / "process/playbooks/REVISE_CON.md").write_text("# Revise\n")
        self.manifest.update(
            operation="REVISE_CON",
            playbook="process/playbooks/REVISE_CON.md",
            trigger={"kind": "EVIDENCE_PLAN_READY",
                     "reference": "reviews/gates/evidence-plan.json"},
        )
        self.store()
        with self.assertRaisesRegex(task.TaskError, "Required task input is missing"):
            task.validate(self.root, "process/tasks/task.yaml")
        (self.root / "reviews/gates/missing-plan.md").write_text("# Bounded plan\n")
        self.assertEqual(task.validate(self.root, "process/tasks/task.yaml")["operation"], "REVISE_CON")

    def test_unresolved_stage_needs_real_blocker(self):
        self._make_contract_task()
        receipt = self.root / "reviews/gates/blocker.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps({
            "schema": "pc-gate-receipt/v1", "status": "CONTRACTS_UNRESOLVED",
            "unresolved": [],
        }))
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text())
        registry["operations"]["PLAN_EVIDENCE"] = {
            "role": "contract-agent",
            "playbook": "process/playbooks/PLAN_EVIDENCE.md",
        }
        registry_path.write_text(yaml.safe_dump(registry))
        (self.root / "process/playbooks/PLAN_EVIDENCE.md").write_text("# Plan\n")
        self.manifest.update(
            operation="PLAN_EVIDENCE",
            playbook="process/playbooks/PLAN_EVIDENCE.md",
            trigger={"kind": "STAGE_EVIDENCE_REQUIRED",
                     "reference": "reviews/gates/blocker.json"},
        )
        self.store()
        with self.assertRaisesRegex(task.TaskError, "nonempty unresolved"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_scope_audit_requires_unresolved_evidence_receipt(self):
        self._make_contract_task()
        ops = self.root / "process/operations.yaml"
        registry = yaml.safe_load(ops.read_text(encoding="utf-8"))
        registry["operations"]["AUDIT_SCOPE"] = {
            "role": "contract-agent",
            "playbook": "process/playbooks/AUDIT_SCOPE.md",
        }
        ops.write_text(yaml.safe_dump(registry), encoding="utf-8")
        (self.root / "process/playbooks/AUDIT_SCOPE.md").write_text(
            "# Scope audit\n", encoding="utf-8")
        receipt = self.root / "reviews/gates/scope-evidence.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        evidence = {
            "schema": "pc-gate-receipt/v1",
            "gate": "EVIDENCE_PLANNING",
            "status": "EVIDENCE_STILL_UNRESOLVED",
            "unresolved": ["Missing resource evidence"],
        }
        receipt.write_text(json.dumps(evidence), encoding="utf-8")
        self.manifest.update(
            operation="AUDIT_SCOPE",
            playbook="process/playbooks/AUDIT_SCOPE.md",
            trigger={"kind": "STAGE_EVIDENCE_UNRESOLVED",
                     "reference": "reviews/gates/scope-evidence.json"},
        )
        self.store()
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"],
            "AUDIT_SCOPE",
        )
        evidence["status"] = "EVIDENCE_PLAN_READY_FOR_REVISION"
        receipt.write_text(json.dumps(evidence), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "unresolved evidence-plan"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_evidence_must_not_pass(self):
        self.manifest["gate"]["on_missing_evidence"] = "PASS"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_role_policy_rejected(self):
        self.manifest["role"] = "unknown"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")


if __name__ == "__main__":
    unittest.main()
