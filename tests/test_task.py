"""Task manifests are reusable across architectures; they never grant approval."""
from pathlib import Path
import sys
import tempfile
import json
import hashlib
import unittest
from unittest.mock import patch

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

    def _make_approved_as_scope_task(self):
        (self.root / "agents/architecture-agent.md").write_text("# Architecture agent\n")
        (self.root / "process/playbooks/REVISE_AS.md").write_text("# Revise AS\n")
        view_path = self.root / "process/views.yaml"
        views = yaml.safe_load(view_path.read_text(encoding="utf-8"))
        views["roles"]["architecture-agent"] = {"follow": []}
        view_path.write_text(yaml.safe_dump(views), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        registry["operations"]["REVISE_AS"] = {
            "role": "architecture-agent",
            "playbook": "process/playbooks/REVISE_AS.md",
        }
        ops_path.write_text(yaml.safe_dump(registry), encoding="utf-8")
        for name, body in {
            "process/decisions/scope-request.md": "# Source request\n",
            "process/decisions/scope-approval.md": "# Explicit authority\n",
            "reviews/gates/scope-audit.json": '{"gate":"SCOPE_AUDIT"}\n',
        }.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
        decision_path = self.root / "process/decisions/scope-approval.yaml"
        authority = {
            "schema": "pc-as-authority/v1",
            "status": "approved",
            "decision": "APPROVE_SCOPED_AS_REVISION",
            "authorizes": "VERSIONED_AS_VP_VO_CORRECTION_FOR_INDEPENDENT_REVIEW",
            "approved_by": "user:engineering_authority",
            "source_request": "process/decisions/scope-request.md",
            "independent_scope_review": "reviews/gates/scope-audit.json",
            "authority_evidence": "process/decisions/scope-approval.md",
            "accepted_scope": {
                "fixed_1ms_requirement": "superseded_subject_to_versioned_AS_review",
                "publisher_responsibility": "uninterrupted_ordered_sample_delivery",
            },
        }
        decision_path.write_text(yaml.safe_dump(authority), encoding="utf-8")
        self.manifest.update(
            role="architecture-agent",
            operation="REVISE_AS",
            playbook="process/playbooks/REVISE_AS.md",
            trigger={"kind": "AS_SCOPE_CORRECTION_APPROVED",
                     "reference": "process/decisions/scope-approval.yaml"},
            context={"authority_inputs": {
                "accepted_scope": "process/decisions/scope-approval.yaml",
            }},
            gate={"kind": "AS_REVIEW", "on_missing_evidence": "UNRESOLVED",
                  "require_independent_review": True},
        )
        self.store()
        return decision_path

    def test_approved_scope_allows_versioned_as_revision(self):
        self._make_approved_as_scope_task()
        result = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(result["operation"], "REVISE_AS")
        self.manifest["spine"] = "/architecture/beta/spine.md"
        self.store()
        result = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(result["spine"], "/architecture/beta/spine.md")

    def test_unapproved_scope_blocks_as_revision(self):
        path = self._make_approved_as_scope_task()
        authority = yaml.safe_load(path.read_text(encoding="utf-8"))
        authority["status"] = "proposed"
        path.write_text(yaml.safe_dump(authority), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "missing explicit accepted scope"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_changed_publisher_boundary_blocks_as_revision(self):
        path = self._make_approved_as_scope_task()
        authority = yaml.safe_load(path.read_text(encoding="utf-8"))
        authority["accepted_scope"]["publisher_responsibility"] = "none"
        path.write_text(yaml.safe_dump(authority), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "approved producer boundary"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_scope_task_must_match_exact_authority_receipt(self):
        self._make_approved_as_scope_task()
        self.manifest["context"]["authority_inputs"]["accepted_scope"] = (
            "process/decisions/different.yaml"
        )
        self.store()
        with self.assertRaisesRegex(task.TaskError, "exact accepted scope"):
            task.validate(self.root, "process/tasks/task.yaml")

    def _make_as_review_task(self):
        self._make_approved_as_scope_task()
        reviewer = self.root / "agents/verification-agent.md"
        reviewer.write_text("# Independent reviewer\n", encoding="utf-8")
        reviews_playbook = self.root / "process/playbooks/REVIEW_AS.md"
        reviews_playbook.write_text("# Review AS\n", encoding="utf-8")
        views_path = self.root / "process/views.yaml"
        views = yaml.safe_load(views_path.read_text(encoding="utf-8"))
        views["roles"]["verification-agent"] = {"follow": []}
        views_path.write_text(yaml.safe_dump(views), encoding="utf-8")
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        registry["operations"]["REVIEW_AS"] = {
            "role": "verification-agent",
            "playbook": "process/playbooks/REVIEW_AS.md",
        }
        registry_path.write_text(yaml.safe_dump(registry), encoding="utf-8")
        candidate_ref = "knowledge/architecture/alpha/statement-v2.md"
        cand = self.root / candidate_ref
        cand.write_text(
            "---\ntype: Architecture Statement\nid: AS-ALPHA-v2\n"
            "status: draft\n---\n# Candidate\n", encoding="utf-8")
        receipt_ref = "reviews/gates/as-authoring.json"
        receipt = self.root / receipt_ref
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps({
            "schema": "pc-gate-receipt/v1", "gate": "AS_REVIEW",
            "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW",
            "changed_artifacts": [candidate_ref],
        }), encoding="utf-8")
        self.manifest.update(
            role="verification-agent", operation="REVIEW_AS",
            playbook="process/playbooks/REVIEW_AS.md",
            trigger={"kind": "AS_REVISION_SUBMITTED", "reference": candidate_ref},
            context={"artifact_inputs": {
                "primary_concept": candidate_ref,
                "submission_receipt": receipt_ref,
            }},
        )
        self.store()
        return receipt, cand

    def test_as_candidate_ready_requires_matching_authoring_receipt(self):
        receipt, candidate = self._make_as_review_task()
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"], "REVIEW_AS")
        body = json.loads(receipt.read_text(encoding="utf-8"))
        body["status"] = "AS_REVISION_UNRESOLVED"
        receipt.write_text(json.dumps(body), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "matching ready receipt"):
            task.validate(self.root, "process/tasks/task.yaml")
        body["status"] = "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW"
        receipt.write_text(json.dumps(body), encoding="utf-8")
        candidate.write_text(candidate.read_text().replace("status: draft", "status: approved"))
        with self.assertRaisesRegex(task.TaskError, "draft Architecture Statement"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_as_review_revision_requires_independent_blocker(self):
        self._make_approved_as_scope_task()
        self.manifest["trigger"] = {
            "kind": "AS_REVIEW_REVISION_REQUIRED",
            "reference": "reviews/gates/as-review.json",
        }
        receipt = self.root / "reviews/gates/as-review.json"
        receipt.write_text(json.dumps({
            "schema": "pc-as-review/v1", "gate": "AS_REVIEW",
            "disposition": "REVISE",
            "next_stage_recommendation": "AS_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "findings": [{"id": "AS-F1", "severity": "blocking"}],
        }))
        self.store()
        self.assertEqual(task.validate(self.root, "process/tasks/task.yaml")["operation"], "REVISE_AS")
        body = json.loads(receipt.read_text(encoding="utf-8"))
        body["independent_of_authoring_invocation"] = False
        receipt.write_text(json.dumps(body), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "independent blocking"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_as_review_allows_versioned_VP_only_resubmission(self):
        receipt, candidate = self._make_as_review_task()
        dependent = self.root / "knowledge/architecture/alpha/verification_plan-v3.md"
        dependent.write_text("# Corrected VP\n", encoding="utf-8")
        data = json.loads(receipt.read_text(encoding="utf-8"))
        data["review_subject"] = "knowledge/architecture/alpha/statement-v2.md"
        data["changed_artifacts"] = [
            "knowledge/architecture/alpha/verification_plan-v3.md",
        ]
        receipt.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"],
            "REVIEW_AS",
        )
        data["review_subject"] = "knowledge/architecture/alpha/other.md"
        receipt.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "matching ready receipt"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_as_correction_accepts_independent_gate_status(self):
        self._make_approved_as_scope_task()
        self.manifest["trigger"] = {
            "kind": "AS_REVIEW_REVISION_REQUIRED",
            "reference": "reviews/gates/as-review.json",
        }
        receipt = self.root / "reviews/gates/as-review.json"
        receipt.write_text(json.dumps({
            "schema": "pc-as-review/v1", "gate": "AS_REVIEW",
            "disposition": "REVISE", "gate_status": "AS_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "findings": [{"id": "ASR-001", "severity": "blocking"}],
        }))
        self.store()
        self.assertEqual(task.validate(
            self.root, "process/tasks/task.yaml")["operation"], "REVISE_AS")

    def _make_baseline_review(self):
        (self.root / "agents/verification-agent.md").write_text(
            "# Baseline reviewer\n", encoding="utf-8")
        (self.root / "process/playbooks/REVIEW_BASELINE.md").write_text(
            "# REVIEW_BASELINE\n", encoding="utf-8")
        views_file = self.root / "process/views.yaml"
        views = yaml.safe_load(views_file.read_text(encoding="utf-8"))
        views["roles"]["verification-agent"] = {"follow": []}
        views_file.write_text(yaml.safe_dump(views), encoding="utf-8")
        ops_file = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_file.read_text(encoding="utf-8"))
        ops["operations"]["REVIEW_BASELINE"] = {
            "role": "verification-agent",
            "playbook": "process/playbooks/REVIEW_BASELINE.md",
        }
        ops_file.write_text(yaml.safe_dump(ops), encoding="utf-8")
        files = {
            "process/decisions/scope.yaml": yaml.safe_dump({"status": "approved"}),
            "process/decisions/ap.yaml": yaml.safe_dump({
                "status": "approved", "decision": "PROVISIONALLY_SELECTED",
                "authorizes": "CON_FIRST_DECOMPOSITION_AFTER_BASELINE_RECONCILIATION",
                "authority_evidence": "process/decisions/ap.md",
                "authorized_vo_supersessions": [{
                    "id": "VO-X",
                    "from_due_stage": "TARGET_VALIDATION",
                    "to_due_stage": "IMPLEMENTATION",
                    "preserved_state": "open",
                }],
            }),
            "process/decisions/ap.md": "# Explicit authority\n",
            "knowledge/architecture/alpha/statement-v2.md": "# Sample-indexed AS\n",
            "knowledge/architecture/alpha/vp-v3.md": "# VP\n",
            "knowledge/architecture/alpha/vo-v2.md": "# VO\n",
            "process/ledgers/vo-original.yaml": yaml.safe_dump({
                "obligations": [{"id": "VO-X", "requirement": "R-X",
                                 "owner": "verification-agent",
                                 "state": "open", "due_stage": "TARGET_VALIDATION",
                                 "evidence_receipt": None}],
            }),
            "process/ledgers/vo-candidate.yaml": yaml.safe_dump({
                "status": "pending_independent_baseline_review",
                "base_ledger": "process/ledgers/vo-original.yaml",
                "obligations": [{"id": "VO-X", "requirement": "R-X",
                                 "owner": "verification-agent",
                                 "state": "open", "due_stage": "IMPLEMENTATION",
                                 "evidence_receipt": None}],
            }),
            "reviews/gates/as-review.json": json.dumps({
                "gate": "AS_REVIEW", "disposition": "ACCEPT_WITH_CLARIFICATIONS",
                "independent_of_authoring_invocation": True,
                "candidate_artifacts": [
                    {"path": "knowledge/architecture/alpha/statement-v2.md"},
                    {"path": "knowledge/architecture/alpha/vp-v3.md"},
                    {"path": "knowledge/architecture/alpha/vo-v2.md"},
                ],
            }),
        }
        for name, content in files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        baseline_path = self.root / "process/baselines/alpha-v2.yaml"
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(yaml.safe_dump({
            "schema": "pc-baseline-candidate/v1",
            "status": "pending_independent_baseline_review",
            "review_required_before_activation": True,
            "candidate_active_as": "knowledge/architecture/alpha/statement-v2.md",
            "candidate_active_verification_plan": "knowledge/architecture/alpha/vp-v3.md",
            "candidate_active_vo_004": "knowledge/architecture/alpha/vo-v2.md",
            "candidate_active_vo_ledger": "process/ledgers/vo-candidate.yaml",
            "independent_as_review": {"receipt": "reviews/gates/as-review.json"},
            "authority": {"provisional_ap": "process/decisions/ap.yaml",
                          "scope": "process/decisions/scope.yaml"},
        }), encoding="utf-8")
        self.manifest.update(
            role="verification-agent", operation="REVIEW_BASELINE",
            playbook="process/playbooks/REVIEW_BASELINE.md",
            trigger={"kind": "BASELINE_RECONCILIATION_REQUESTED",
                     "reference": "process/baselines/alpha-v2.yaml"},
            context={"authority_inputs": {
                "baseline_candidate": "process/baselines/alpha-v2.yaml",
            }},
            gate={"kind": "BASELINE_REVIEW", "on_missing_evidence": "UNRESOLVED",
                  "require_independent_review": True},
        )
        self.store()
        return baseline_path

    def test_independently_reviewed_baseline_keeps_VO_open(self):
        self._make_baseline_review()
        self.assertEqual(task.validate(
            self.root, "process/tasks/task.yaml")["operation"], "REVIEW_BASELINE")

    def test_baseline_cannot_silently_discharge_VO(self):
        self._make_baseline_review()
        path = self.root / "process/ledgers/vo-candidate.yaml"
        body = yaml.safe_load(path.read_text(encoding="utf-8"))
        body["obligations"][0]["state"] = "discharged"
        path.write_text(yaml.safe_dump(body), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "change VO authority or discharge"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_baseline_cannot_steal_unapproved_due_stage(self):
        self._make_baseline_review()
        path = self.root / "process/ledgers/vo-candidate.yaml"
        body = yaml.safe_load(path.read_text(encoding="utf-8"))
        body["obligations"][0]["due_stage"] = "AS"
        path.write_text(yaml.safe_dump(body), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "without explicit authority"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_baseline_review_uses_verified_relation_projection(self):
        self._make_baseline_review()
        source = self.root / "knowledge/architecture/alpha/statement-v2.md"
        source.write_text(
            "---\ntype: Architecture Statement\nid: AS-ALPHA-v2\n"
            "relations:\n  - kind: specifies\n"
            "    target: /architecture/alpha/vp-v2.md\n"
            "---\n# Existing reviewed AS\n", encoding="utf-8")
        (self.root / "knowledge/architecture/alpha/vp-v2.md").write_text(
            "# Historical verification plan\n", encoding="utf-8")
        baseline_path = self.root / "process/baselines/alpha-v2.yaml"
        baseline = yaml.safe_load(baseline_path.read_text(encoding="utf-8"))
        baseline["effective_relation_overrides"] = [{
            "source": "knowledge/architecture/alpha/statement-v2.md",
            "kind": "specifies",
            "historical_target": "knowledge/architecture/alpha/vp-v2.md",
            "active_target": "knowledge/architecture/alpha/vp-v3.md",
            "scope": "this_baseline_only_after_independent_acceptance",
            "selection_authority": "reviews/gates/as-review.json",
        }]
        baseline_path.write_text(yaml.safe_dump(baseline), encoding="utf-8")
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"],
            "REVIEW_BASELINE",
        )
        baseline["effective_relation_overrides"][0]["historical_target"] = (
            "knowledge/architecture/alpha/vo-v2.md"
        )
        baseline_path.write_text(yaml.safe_dump(baseline), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "Invalid effective baseline relations"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_unapproved_AP_cannot_start_baseline_review(self):
        self._make_baseline_review()
        path = self.root / "process/decisions/ap.yaml"
        body = yaml.safe_load(path.read_text(encoding="utf-8"))
        body["status"] = "proposed"
        path.write_text(yaml.safe_dump(body), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "accepted scope and AP authority"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_unresolved_contract_review_requires_exact_receipt_and_active_baseline(self):
        role = self.root / "agents/verification-agent.md"
        role.write_text("# Independent reviewer\n", encoding="utf-8")
        playbook = self.root / "process/playbooks/REVIEW_CON.md"
        playbook.write_text("# REVIEW_CON\n", encoding="utf-8")
        views = self.root / "process/views.yaml"
        view_data = yaml.safe_load(views.read_text(encoding="utf-8"))
        view_data["roles"]["verification-agent"] = {"follow": []}
        views.write_text(yaml.safe_dump(view_data), encoding="utf-8")
        registry = self.root / "process/operations.yaml"
        registry_data = yaml.safe_load(registry.read_text(encoding="utf-8"))
        registry_data["operations"]["REVIEW_CON"] = {
            "role": "verification-agent", "playbook": "process/playbooks/REVIEW_CON.md",
        }
        registry.write_text(yaml.safe_dump(registry_data), encoding="utf-8")
        spine = "knowledge/architecture/alpha/contracts/spine-v5.md"
        contract = "knowledge/architecture/alpha/contracts/CON-01-v5.md"
        receipt_ref = "reviews/gates/contract-authoring.json"
        for name, content in {
            spine: "---\ntype: Contract Spine\nid: CON-S5\n---\n",
            contract: "---\ntype: Design Contract\nid: CON-01-v5\n---\n",
            "process/tasks/CON-AUTHOR.yaml": yaml.safe_dump({
                "id": "CON-AUTHOR", "operation": "DEFINE_CON",
                "trigger": {"kind": "BASELINE_ACTIVATED",
                            "reference": "process/baselines/active.yaml"}}),
            "process/baselines/active.yaml": "status: active\n",
            receipt_ref: json.dumps({
                "schema": "pc-con-authoring-receipt/v1",
                "task_id": "CON-AUTHOR", "operation": "DEFINE_CON",
                "gate_status": "CONTRACTS_UNRESOLVED",
                "unresolved": ["Stack layout due at implementation"],
                "changed_artifacts": [spine, contract]}),
        }.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        self.manifest.update(
            role="verification-agent", operation="REVIEW_CON",
            playbook="process/playbooks/REVIEW_CON.md",
            trigger={"kind": "CONTRACT_UNRESOLVED_SUBMITTED",
                     "reference": spine},
            context={"artifact_inputs": {
                "primary_concept": spine,
                "related_concepts": [contract],
                "submission_receipt": receipt_ref,
            }},
        )
        self.store()
        with patch("active_baseline.verify", return_value={"status": "ACTIVE_BASELINE_VERIFIED"}):
            self.assertEqual(task.validate(self.root, "process/tasks/task.yaml")["operation"],
                             "REVIEW_CON")
        with patch("active_baseline.verify", side_effect=ValueError("invalid baseline")):
            with self.assertRaisesRegex(task.TaskError, "lacks verified baseline"):
                task.validate(self.root, "process/tasks/task.yaml")
        receipt = self.root / receipt_ref
        data = json.loads(receipt.read_text(encoding="utf-8"))
        data["changed_artifacts"] = [spine]
        receipt.write_text(json.dumps(data), encoding="utf-8")
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "not in submitted receipt"):
                task.validate(self.root, "process/tasks/task.yaml")

    def _make_accepted_contract_to_design_task(self):
        (self.root / "agents/design-agent.md").write_text("# Design\n", encoding="utf-8")
        (self.root / "process/playbooks/DECOMPOSE_DE.md").write_text("# DE\n", encoding="utf-8")
        views_path = self.root / "process/views.yaml"
        views = yaml.safe_load(views_path.read_text(encoding="utf-8"))
        views["roles"]["design-agent"] = {"follow": []}
        views_path.write_text(yaml.safe_dump(views), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["DECOMPOSE_DE"] = {
            "role": "design-agent", "playbook": "process/playbooks/DECOMPOSE_DE.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        contract_spine = "knowledge/architecture/alpha/contracts/spine-v6.md"
        contract = "knowledge/architecture/alpha/contracts/CON-001-v6.md"
        baseline = "process/baselines/alpha-active.yaml"
        for ref, content in {
            contract_spine: "---\ntype: Contract Spine\nid: CS-6\n---\n",
            contract: "---\ntype: Design Contract\nid: C-6\n---\n",
            baseline: "status: active\n",
        }.items():
            path = self.root / ref
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        prior = "process/tasks/REVIEW-CON.yaml"
        (self.root / prior).write_text(yaml.safe_dump({
            "id": "REVIEW-CON", "operation": "REVIEW_CON",
            "spine": "/architecture/alpha/spine.md",
            "trigger": {"kind": "CONTRACT_DRAFT_SUBMITTED",
                        "reference": contract_spine},
            "context": {"artifact_inputs": {
                "primary_concept": contract_spine,
                "related_concepts": [contract],
            }},
        }), encoding="utf-8")
        pins = {ref: hashlib.sha256((self.root / ref).read_bytes()).hexdigest()
                for ref in (contract_spine, contract, baseline)}
        receipt_ref = "reviews/gates/contract-accepted.json"
        receipt = self.root / receipt_ref
        receipt.parent.mkdir(parents=True, exist_ok=True)
        review = {
            "schema": "pc-contract-review/v1", "task_id": "REVIEW-CON",
            "gate": "CONTRACT_REVIEW", "disposition": "ACCEPT_WITH_CLARIFICATIONS",
            "next_stage_recommendation": "CON_ACCEPTABLE_FOR_DE_REFINEMENT",
            "independent_of_authoring_invocation": True,
            "reviewed_input_sha256": pins, "findings": [],
        }
        receipt.write_text(json.dumps(review), encoding="utf-8")
        self.manifest.update(
            role="design-agent", operation="DECOMPOSE_DE",
            playbook="process/playbooks/DECOMPOSE_DE.md",
            trigger={"kind": "CONTRACT_ACCEPTED_FOR_DE", "reference": receipt_ref},
            context={"review_inputs": {"independent_review": receipt_ref}},
            gate={"kind": "DE_REVIEW", "on_missing_evidence": "UNRESOLVED",
                  "require_independent_review": True},
        )
        self.store()
        return receipt, self.root / contract

    def test_accepted_contract_review_permits_design(self):
        self._make_accepted_contract_to_design_task()
        with patch("active_baseline.verify", return_value={"status": "ACTIVE_BASELINE_VERIFIED"}):
            result = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(result["operation"], "DECOMPOSE_DE")

    def test_design_rejects_stale_contract_hash(self):
        _, contract = self._make_accepted_contract_to_design_task()
        contract.write_text(contract.read_text() + "unauthorized change\n", encoding="utf-8")
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "contract bytes changed"):
                task.validate(self.root, "process/tasks/task.yaml")

    def test_design_rejects_unaccepted_contract_review(self):
        receipt, _ = self._make_accepted_contract_to_design_task()
        data = json.loads(receipt.read_text(encoding="utf-8"))
        data["disposition"] = "REVISE"
        receipt.write_text(json.dumps(data), encoding="utf-8")
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "favorable independent CON acceptance"):
                task.validate(self.root, "process/tasks/task.yaml")

    def test_design_rejects_cross_project_review(self):
        self._make_accepted_contract_to_design_task()
        self.manifest["spine"] = "/architecture/beta/spine.md"
        self.store()
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "different project spines"):
                task.validate(self.root, "process/tasks/task.yaml")

    def _make_de_review_task(self):
        (self.root / "agents/verification-agent.md").write_text(
            "# Reviewer\n", encoding="utf-8")
        (self.root / "process/playbooks/REVIEW_DE.md").write_text(
            "# Review DE\n", encoding="utf-8")
        view_path = self.root / "process/views.yaml"
        views = yaml.safe_load(view_path.read_text(encoding="utf-8"))
        views["roles"]["verification-agent"] = {"follow": []}
        view_path.write_text(yaml.safe_dump(views), encoding="utf-8")
        registry_path = self.root / "process/operations.yaml"
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        registry["operations"]["REVIEW_DE"] = {
            "role": "verification-agent", "playbook": "process/playbooks/REVIEW_DE.md",
        }
        registry_path.write_text(yaml.safe_dump(registry), encoding="utf-8")
        spine = "knowledge/architecture/alpha/design_elements/spine-v7.md"
        element = "knowledge/architecture/alpha/design_elements/DE-001-v7.md"
        receipt_ref = "reviews/gates/de-authoring.json"
        for path, content in {
            spine: "---\ntype: Design Element Spine\nid: DS-7\n---\n",
            element: "---\ntype: Design Element\nid: DE-7\n---\n",
            "process/tasks/DE-AUTHOR.yaml": yaml.safe_dump({
                "id": "DE-AUTHOR", "operation": "DECOMPOSE_DE",
                "spine": "/architecture/alpha/spine.md",
                "trigger": {"kind": "CONTRACT_ACCEPTED_FOR_DE",
                            "reference": "reviews/gates/accepted.json"},
            }),
            receipt_ref: json.dumps({
                "schema": "pc-de-authoring-receipt/v1",
                "task_id": "DE-AUTHOR", "operation": "DECOMPOSE_DE",
                "gate": "DE_REVIEW",
                "gate_status": "DE_READY_FOR_INDEPENDENT_REVIEW",
                "changed_artifacts": [spine, element],
            }),
        }.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        self.manifest.update(
            role="verification-agent", operation="REVIEW_DE",
            playbook="process/playbooks/REVIEW_DE.md",
            trigger={"kind": "DE_DRAFT_SUBMITTED", "reference": spine},
            context={"artifact_inputs": {
                "primary_concept": spine, "related_concepts": [element],
                "submission_receipt": receipt_ref,
            }},
            gate={"kind": "DE_REVIEW", "on_missing_evidence": "UNRESOLVED",
                  "require_independent_review": True},
        )
        self.store()
        return self.root / receipt_ref

    def test_de_review_requires_ready_receipt(self):
        receipt = self._make_de_review_task()
        self.assertEqual(
            task.validate(self.root, "process/tasks/task.yaml")["operation"],
            "REVIEW_DE",
        )
        obj = json.loads(receipt.read_text(encoding="utf-8"))
        obj["gate_status"] = "DE_UNRESOLVED"
        receipt.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "matching ready authoring receipt"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_de_review_rejects_malformed_frontmatter(self):
        self._make_de_review_task()
        path = self.root / "knowledge/architecture/alpha/design_elements/spine-v7.md"
        path.write_text("# No OKF header\n", encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "lacks OKF frontmatter"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_de_review_rejects_cross_project_author(self):
        self._make_de_review_task()
        self.manifest["spine"] = "/architecture/beta/spine.md"
        self.store()
        with self.assertRaisesRegex(task.TaskError, "not authorized for this project"):
            task.validate(self.root, "process/tasks/task.yaml")

    def _make_implementation_task(self):
        (self.root / "agents/implementation-agent.md").write_text(
            "# Implementation\n", encoding="utf-8")
        (self.root / "process/playbooks/IMPLEMENT_DE.md").write_text(
            "# Implement DE\n", encoding="utf-8")
        views_path = self.root / "process/views.yaml"
        views = yaml.safe_load(views_path.read_text(encoding="utf-8"))
        views["roles"]["implementation-agent"] = {"follow": []}
        views_path.write_text(yaml.safe_dump(views), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["IMPLEMENT_DE"] = {
            "role": "implementation-agent",
            "playbook": "process/playbooks/IMPLEMENT_DE.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        spine = "knowledge/architecture/alpha/design_elements/spine-v7.md"
        element = "knowledge/architecture/alpha/design_elements/DE-001-v7.md"
        active = "process/baselines/alpha-active.yaml"
        for ref, content in {
            spine: "---\ntype: Design Element Spine\nid: DS-7\n---\n",
            element: "---\ntype: Design Element\nid: DE-7\n---\n",
            active: "status: active\n",
        }.items():
            path = self.root / ref
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        source_task = "process/tasks/REVIEW-DE.yaml"
        (self.root / source_task).write_text(yaml.safe_dump({
            "id": "REVIEW-DE", "operation": "REVIEW_DE",
            "spine": "/architecture/alpha/spine.md",
            "trigger": {"kind": "DE_DRAFT_SUBMITTED", "reference": spine},
            "context": {"artifact_inputs": {
                "primary_concept": spine, "related_concepts": [element],
            }},
        }), encoding="utf-8")
        pins = {ref: hashlib.sha256((self.root / ref).read_bytes()).hexdigest()
                for ref in (spine, element, active)}
        receipt_ref = "reviews/gates/de-accepted.json"
        path = self.root / receipt_ref
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({
            "schema": "pc-de-review/v1", "task_id": "REVIEW-DE",
            "gate": "DE_REVIEW", "disposition": "ACCEPT_WITH_CLARIFICATIONS",
            "next_stage_recommendation": "DE_ACCEPTABLE_FOR_GUARDED_IMPLEMENTATION_TASK",
            "independent_of_authoring_invocation": True,
            "reviewed_input_sha256": pins, "findings": [],
        }), encoding="utf-8")
        self.manifest.update(
            role="implementation-agent", operation="IMPLEMENT_DE",
            playbook="process/playbooks/IMPLEMENT_DE.md",
            trigger={"kind": "DESIGN_ACCEPTED_FOR_IMPLEMENTATION",
                     "reference": receipt_ref},
            context={"review_inputs": {"independent_review": receipt_ref}},
            outputs={"allowed": ["implementation_source", "implementation_tests",
                                 "engineering_briefing"],
                     "prohibited": ["approve_own_gate", "discharge_VO"]},
            gate={"kind": "IMPLEMENTATION_REVIEW", "on_missing_evidence": "UNRESOLVED",
                  "require_independent_review": True},
        )
        self.store()
        return path, self.root / element

    def test_implementation_requires_accepted_de_and_hashes(self):
        receipt, element = self._make_implementation_task()
        with patch("active_baseline.verify", return_value={}):
            self.assertEqual(
                task.validate(self.root, "process/tasks/task.yaml")["operation"],
                "IMPLEMENT_DE",
            )
        element.write_text(element.read_text() + "changed\n", encoding="utf-8")
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "changed after independent review"):
                task.validate(self.root, "process/tasks/task.yaml")
        data = json.loads(receipt.read_text(encoding="utf-8"))
        data["disposition"] = "REVISE"
        receipt.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(task.TaskError, "lacks favorable independent DE acceptance"):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_implementation_cannot_inherit_source_prohibition(self):
        self._make_implementation_task()
        self.manifest["outputs"]["prohibited"].append("implement_firmware")
        self.store()
        with patch("active_baseline.verify", return_value={}):
            with self.assertRaisesRegex(task.TaskError, "explicitly permitted source output"):
                task.validate(self.root, "process/tasks/task.yaml")

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
