"""Receipt-driven contract loops must be portable and fail closed."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import next_task


class LoopTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self._put("process/loop_transitions.yaml", yaml.safe_dump({"transitions": [
            {"id": "repair", "receipt_schema": "pc-contract-review/v1",
             "requires": {"gate": "CONTRACT_REVIEW", "disposition": "REVISE",
                          "next_stage_recommendation": "CON_REVISION_REQUIRED",
                          "independent_of_authoring_invocation": True},
             "require_blocking_finding": True,
             "operation": "REVISE_CON", "target": "receipt",
             "trigger_kind": "CONTRACT_REVIEW_REVISION_REQUIRED",
             "gate": "CONTRACT_REVIEW"},
            {"id": "review", "receipt_schema": "pc-gate-receipt/v1",
             "requires": {"gate": "CONTRACT_REVIEW",
                          "status": "CONTRACTS_READY_FOR_INDEPENDENT_REVIEW"},
             "operation": "REVIEW_CON", "target": "changed_contract_spine",
             "trigger_kind": "CONTRACT_DRAFT_SUBMITTED", "gate": "CONTRACT_REVIEW"},
        ]}))
        self._put("process/operations.yaml", yaml.safe_dump({"operations": {
            "REVISE_CON": {"role": "contract-agent",
                           "playbook": "process/playbooks/REVISE_CON.md"},
            "REVIEW_CON": {"role": "verification-agent",
                           "playbook": "process/playbooks/REVIEW_CON.md"},
        }}))
        self._put("process/playbooks/REVISE_CON.md", "# Contract correction\n")
        self._put("process/playbooks/REVIEW_CON.md", "# Independent review\n")
        self._put("process/tasks/EXAMPLE-REVIEW.yaml", yaml.safe_dump({
            "id": "EXAMPLE-REVIEW",
            "spine": "/architecture/alpha/spine.md",
            "context": {"purpose": "first architecture"},
        }))
        self.review = {
            "schema": "pc-contract-review/v1", "task_id": "EXAMPLE-REVIEW",
            "gate": "CONTRACT_REVIEW", "disposition": "REVISE",
            "next_stage_recommendation": "CON_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "input_revision": "abc123",
            "findings": [{"id": "F1", "severity": "blocking"}],
        }
        self._put("reviews/gates/review.json", json.dumps(self.review))

    def _put(self, name, contents):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")
        return path

    def test_revision_planned_from_independent_receipt(self):
        out = next_task.decision(self.root, "reviews/gates/review.json")
        self.assertEqual(out["status"], "NEW")
        self.assertEqual(out["manifest"]["operation"], "REVISE_CON")
        self.assertEqual(out["manifest"]["context"]["review_inputs"]["finding_ids"], ["F1"])
        self.assertEqual(out["manifest"]["spine"], "/architecture/alpha/spine.md")

    def test_contract_revision_carries_unsupported_requirement_findings(self):
        self.review["findings"].append({
            "id": "F2", "severity": "unsupported_requirement",
        })
        self.review["findings"].append({
            "id": "F3", "severity": "clarification_nonblocking",
        })
        self._put("reviews/gates/review.json", json.dumps(self.review))
        out = next_task.decision(self.root, "reviews/gates/review.json")
        self.assertEqual(
            out["manifest"]["context"]["review_inputs"]["finding_ids"],
            ["F1", "F2"],
        )

    def test_repeated_receipt_returns_existing_plan(self):
        out = next_task.decision(self.root, "reviews/gates/review.json")
        self._put(out["path"], yaml.safe_dump(out["manifest"]))
        again = next_task.decision(self.root, "reviews/gates/review.json")
        self.assertEqual(again["status"], "ALREADY_PLANNED")
        self.assertEqual(again["path"], out["path"])

    def test_nonindependent_review_cannot_trigger_revision(self):
        self.review["independent_of_authoring_invocation"] = False
        self._put("reviews/gates/review.json", json.dumps(self.review))
        with self.assertRaises(next_task.LoopError):
            next_task.decision(self.root, "reviews/gates/review.json")

    def test_accepted_review_does_not_generate_correction(self):
        self.review["disposition"] = "ACCEPT"
        self._put("reviews/gates/review.json", json.dumps(self.review))
        with self.assertRaises(next_task.LoopError):
            next_task.decision(self.root, "reviews/gates/review.json")

    def test_no_blocking_finding_does_not_generate_correction(self):
        self.review["findings"][0]["severity"] = "informational"
        self._put("reviews/gates/review.json", json.dumps(self.review))
        with self.assertRaises(next_task.LoopError):
            next_task.decision(self.root, "reviews/gates/review.json")

    def test_new_submission_generates_independent_review(self):
        self._put("process/tasks/EXAMPLE-AUTHOR.yaml", yaml.safe_dump({
            "id": "EXAMPLE-AUTHOR",
            "spine": "/architecture/alpha/spine.md",
            "context": {"submission": "first architecture"},
        }))
        spine = "knowledge/architecture/alpha/contracts/spine-v3.md"
        contract = "knowledge/architecture/alpha/contracts/CON-01-v3.md"
        self._put(spine, "---\ntype: Contract Spine\nid: A-CON-SPINE\n---\n# Spine\n")
        self._put(contract, "---\ntype: Design Contract\nid: A-CON-01\n---\n# Contract\n")
        self._put("reviews/gates/submission.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "EXAMPLE-AUTHOR",
            "gate": "CONTRACT_REVIEW",
            "status": "CONTRACTS_READY_FOR_INDEPENDENT_REVIEW",
            "changed_artifacts": [spine, contract],
        }))
        out = next_task.decision(self.root, "reviews/gates/submission.json")
        self.assertEqual(out["manifest"]["operation"], "REVIEW_CON")
        self.assertEqual(out["manifest"]["trigger"]["reference"], spine)
        self.assertEqual(out["manifest"]["context"]["authority_inputs"]["current_contracts"], [contract])

    def test_unresolved_contracts_route_to_independent_scope_triage(self):
        rules_path = self.root / "process/loop_transitions.yaml"
        rules = yaml.safe_load(rules_path.read_text(encoding="utf-8"))
        rules["transitions"].append({
            "id": "contract_unresolved_scope_review",
            "receipt_schema": "pc-con-authoring-receipt/v1",
            "requires": {"operation": "DEFINE_CON", "gate_status": "CONTRACTS_UNRESOLVED"},
            "require_unresolved": True, "operation": "REVIEW_CON",
            "target": "changed_concept", "concept_type": "Contract Spine",
            "related_concept_type": "Design Contract",
            "trigger_kind": "CONTRACT_UNRESOLVED_SUBMITTED", "gate": "CONTRACT_REVIEW",
        })
        rules_path.write_text(yaml.safe_dump(rules), encoding="utf-8")
        self._put("process/tasks/CON-AUTHOR.yaml", yaml.safe_dump({
            "id": "CON-AUTHOR", "spine": "/architecture/alpha/spine.md",
        }))
        spine = "knowledge/architecture/alpha/contracts/spine-v5.md"
        contract = "knowledge/architecture/alpha/contracts/CON-001-v5.md"
        self._put(spine,
                  "---\ntype: Contract Spine\nid: CONTRACT-SPINE-v5\n---\n")
        self._put(contract,
                  "---\ntype: Design Contract\nid: CONTRACT-001-v5\n---\n")
        payload = {
            "schema": "pc-con-authoring-receipt/v1", "task_id": "CON-AUTHOR",
            "operation": "DEFINE_CON", "gate_status": "CONTRACTS_UNRESOLVED",
            "unresolved": ["Target-specific stack measurements remain open at implementation"],
            "changed_artifacts": [spine, contract],
        }
        receipt = "reviews/gates/contract-unresolved.json"
        self._put(receipt, json.dumps(payload))
        result = next_task.decision(self.root, receipt)
        self.assertEqual(result["manifest"]["operation"], "REVIEW_CON")
        self.assertEqual(result["manifest"]["trigger"]["kind"], "CONTRACT_UNRESOLVED_SUBMITTED")
        self.assertEqual(result["manifest"]["trigger"]["reference"], spine)
        self.assertEqual(result["manifest"]["context"]["artifact_inputs"]["related_concepts"],
                         [contract])
        self._put(result["path"], yaml.safe_dump(result["manifest"]))
        self.assertEqual(next_task.decision(self.root, receipt)["status"], "ALREADY_PLANNED")
        payload["unresolved"] = []
        self._put(receipt, json.dumps(payload))
        with self.assertRaises(next_task.LoopError):
            next_task.decision(self.root, receipt)

    def test_revised_contract_authoring_receipt_routes_independent_review(self):
        rules_path = self.root / "process/loop_transitions.yaml"
        rules = yaml.safe_load(rules_path.read_text(encoding="utf-8"))
        rules["transitions"].append({
            "id": "contract_revised_authoring_review",
            "receipt_schema": "pc-con-authoring-receipt/v1",
            "requires": {"operation": "REVISE_CON",
                         "gate_status": "CONTRACTS_READY_FOR_INDEPENDENT_REVIEW"},
            "operation": "REVIEW_CON",
            "target": "changed_concept", "concept_type": "Contract Spine",
            "related_concept_type": "Design Contract",
            "trigger_kind": "CONTRACT_DRAFT_SUBMITTED",
            "gate": "CONTRACT_REVIEW",
        })
        rules_path.write_text(yaml.safe_dump(rules), encoding="utf-8")
        self._put("process/tasks/CON-REV.yaml", yaml.safe_dump({
            "id": "CON-REV", "spine": "/architecture/beta/spine.md",
        }))
        spine = "knowledge/architecture/beta/contracts/spine-v6.md"
        contract = "knowledge/architecture/beta/contracts/CON-001-v6.md"
        self._put(spine, "---\\ntype: Contract Spine\\nid: CON-S6\\n---\\n")
        self._put(contract, "---\\ntype: Design Contract\\nid: CON-001-v6\\n---\\n")
        receipt = "reviews/gates/v6-ready.json"
        self._put(receipt, json.dumps({
            "schema": "pc-con-authoring-receipt/v1", "task_id": "CON-REV",
            "operation": "REVISE_CON",
            "gate_status": "CONTRACTS_READY_FOR_INDEPENDENT_REVIEW",
            "changed_artifacts": [spine, contract],
        }))
        out = next_task.decision(self.root, receipt)
        self.assertEqual(out["manifest"]["operation"], "REVIEW_CON")
        self.assertEqual(out["manifest"]["spine"], "/architecture/beta/spine.md")
        self.assertEqual(out["manifest"]["trigger"]["reference"], spine)
        self.assertEqual(out["manifest"]["context"]["artifact_inputs"]["related_concepts"], [contract])
        self._put(out["path"], yaml.safe_dump(out["manifest"]))
        self.assertEqual(next_task.decision(self.root, receipt)["status"], "ALREADY_PLANNED")

    def test_second_architecture_uses_same_operations(self):
        self._put("process/tasks/SECOND-REVIEW.yaml", yaml.safe_dump({
            "id": "SECOND-REVIEW",
            "spine": "/architecture/newton-raphson/spine.md",
            "context": {"purpose": "second architecture"},
        }))
        other = dict(self.review, task_id="SECOND-REVIEW")
        self._put("reviews/gates/second.json", json.dumps(other))
        out = next_task.decision(self.root, "reviews/gates/second.json")
        self.assertEqual(out["manifest"]["spine"], "/architecture/newton-raphson/spine.md")
        self.assertEqual(out["manifest"]["playbook"], "process/playbooks/REVISE_CON.md")


    def test_policy_can_review_a_different_artifact_type(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text())
        policy["transitions"].append({
            "id": "proof_package_review",
            "receipt_schema": "pc-stage-submission/v1",
            "requires": {"gate": "PROOF_REVIEW", "status": "READY_FOR_INDEPENDENT_REVIEW"},
            "operation": "REVIEW_PROOF",
            "target": "changed_concept",
            "concept_type": "Proof Package",
            "related_concept_type": "Proof Claim",
            "trigger_kind": "PROOF_SUBMITTED",
            "gate": "PROOF_REVIEW",
        })
        policy_path.write_text(yaml.safe_dump(policy))
        operations_path = self.root / "process/operations.yaml"
        operations = yaml.safe_load(operations_path.read_text())
        operations["operations"]["REVIEW_PROOF"] = {
            "role": "proof-reviewer",
            "playbook": "process/playbooks/REVIEW_PROOF.md",
        }
        operations_path.write_text(yaml.safe_dump(operations))
        self._put("process/playbooks/REVIEW_PROOF.md", "# Reusable proof review\n")
        self._put("process/tasks/PROOF-SUB.yaml", yaml.safe_dump({
            "id": "PROOF-SUB", "spine": "/architecture/newton-raphson/spine.md",
        }))
        packet = "knowledge/architecture/newton-raphson/proofs/packet.md"
        claim = "knowledge/architecture/newton-raphson/proofs/claim.md"
        self._put(packet, "---\ntype: Proof Package\nid: P-X\n---\n# Package\n")
        self._put(claim, "---\ntype: Proof Claim\nid: T-X\n---\n# Claim\n")
        self._put("reviews/gates/proof-sub.json", json.dumps({
            "schema": "pc-stage-submission/v1", "task_id": "PROOF-SUB",
            "gate": "PROOF_REVIEW", "status": "READY_FOR_INDEPENDENT_REVIEW",
            "changed_artifacts": [packet, claim],
        }))
        out = next_task.decision(self.root, "reviews/gates/proof-sub.json")
        self.assertEqual(out["manifest"]["operation"], "REVIEW_PROOF")
        self.assertEqual(out["manifest"]["trigger"]["reference"], packet)
        self.assertEqual(out["manifest"]["spine"], "/architecture/newton-raphson/spine.md")

    def test_generated_manifest_context_does_not_grow_recursively(self):
        self._put("process/tasks/EXAMPLE-REVIEW.yaml", yaml.safe_dump({
            "id": "EXAMPLE-REVIEW", "spine": "/architecture/alpha/spine.md",
            "context": {"prior_task_context": {"prior_task_context": {
                "prior_task_context": {"huge": "historical context"}
            }}},
        }))
        out = next_task.decision(self.root, "reviews/gates/review.json")
        context = out["manifest"]["context"]["review_inputs"]
        self.assertEqual(context["source_task_manifest"], "process/tasks/EXAMPLE-REVIEW.yaml")
        self.assertNotIn("prior_task_context", context)
        self.assertNotIn("huge", yaml.safe_dump(out["manifest"]))



    def _register_evidence_operation(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        policy["transitions"].extend([
            {
                "id": "resolve_stage_evidence",
                "receipt_schema": "pc-gate-receipt/v1",
                "requires": {"gate": "CONTRACT_REVIEW",
                             "status": "CONTRACTS_UNRESOLVED"},
                "require_unresolved": True,
                "operation": "PLAN_EVIDENCE",
                "target": "receipt",
                "trigger_kind": "STAGE_EVIDENCE_REQUIRED",
                "gate": "EVIDENCE_PLANNING",
            },
            {
                "id": "apply_stage_evidence",
                "receipt_schema": "pc-evidence-plan/v1",
                "requires": {"gate": "EVIDENCE_PLANNING",
                             "status": "EVIDENCE_PLAN_READY_FOR_REVISION"},
                "operation": "REVISE_CON", "target": "receipt",
                "trigger_kind": "EVIDENCE_PLAN_READY", "gate": "CONTRACT_REVIEW",
            },
        ])
        policy_path.write_text(yaml.safe_dump(policy), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["PLAN_EVIDENCE"] = {
            "role": "evidence-planning-agent",
            "playbook": "process/playbooks/PLAN_EVIDENCE.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        self._put("process/playbooks/PLAN_EVIDENCE.md", "# Evidence plan\n")
        self._put("process/tasks/EXAMPLE-AUTHOR.yaml", yaml.safe_dump({
            "id": "EXAMPLE-AUTHOR", "spine": "/architecture/alpha/spine.md",
        }))

    def test_unresolved_submission_routes_to_evidence_not_review(self):
        self._register_evidence_operation()
        self._put("reviews/gates/unresolved.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "EXAMPLE-AUTHOR",
            "gate": "CONTRACT_REVIEW", "status": "CONTRACTS_UNRESOLVED",
            "unresolved": ["Bound shared allocation before DE refinement"],
        }))
        out = next_task.decision(self.root, "reviews/gates/unresolved.json")
        self.assertEqual(out["manifest"]["operation"], "PLAN_EVIDENCE")
        self.assertEqual(out["manifest"]["gate"]["kind"], "EVIDENCE_PLANNING")
        self.assertEqual(
            out["manifest"]["context"]["evidence_inputs"]["unresolved"],
            ["Bound shared allocation before DE refinement"],
        )

    def test_empty_unresolved_submission_fails_closed(self):
        self._register_evidence_operation()
        self._put("reviews/gates/unresolved.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "EXAMPLE-AUTHOR",
            "gate": "CONTRACT_REVIEW", "status": "CONTRACTS_UNRESOLVED",
            "unresolved": [],
        }))
        with self.assertRaises(next_task.LoopError):
            next_task.decision(self.root, "reviews/gates/unresolved.json")

    def test_actionable_evidence_plan_routes_back_to_revision(self):
        self._register_evidence_operation()
        self._put("process/tasks/EVIDENCE-TASK.yaml", yaml.safe_dump({
            "id": "EVIDENCE-TASK", "spine": "/architecture/alpha/spine.md",
        }))
        self._put("reviews/gates/plan.json", json.dumps({
            "schema": "pc-evidence-plan/v1",
            "task_id": "EVIDENCE-TASK",
            "gate": "EVIDENCE_PLANNING",
            "status": "EVIDENCE_PLAN_READY_FOR_REVISION",
            "plan_artifacts": ["reviews/gates/bounded-plan.md"],
        }))
        out = next_task.decision(self.root, "reviews/gates/plan.json")
        self.assertEqual(out["manifest"]["operation"], "REVISE_CON")
        self.assertEqual(out["manifest"]["trigger"]["kind"], "EVIDENCE_PLAN_READY")
        self.assertEqual(
            out["manifest"]["context"]["evidence_inputs"]["plan_artifacts"],
            ["reviews/gates/bounded-plan.md"],
        )



    def test_as_review_uses_generic_typed_submission_router(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        policy["transitions"].append({
            "id": "as_review",
            "receipt_schema": "pc-gate-receipt/v1",
            "requires": {"gate": "AS_REVIEW",
                         "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW"},
            "operation": "REVIEW_AS", "target": "changed_concept",
            "concept_type": "Architecture Statement",
            "related_concept_type": None,
            "trigger_kind": "AS_REVISION_SUBMITTED", "gate": "AS_REVIEW",
        })
        policy_path.write_text(yaml.safe_dump(policy), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["REVIEW_AS"] = {
            "role": "verification-agent",
            "playbook": "process/playbooks/REVIEW_AS.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        self._put("process/playbooks/REVIEW_AS.md", "# Generic AS review\n")
        self._put("process/tasks/AS-AUTHOR.yaml", yaml.safe_dump({
            "id": "AS-AUTHOR", "spine": "/architecture/beta/spine.md",
        }))
        candidate = "knowledge/architecture/beta/statement-v2.md"
        self._put(candidate,
                  "---\ntype: Architecture Statement\nid: AS-BETA-v2\n"
                  "status: draft\n---\n# AS Beta\n")
        self._put("reviews/gates/as-submission.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "AS-AUTHOR",
            "gate": "AS_REVIEW",
            "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW",
            "changed_artifacts": [candidate],
        }))
        result = next_task.decision(self.root, "reviews/gates/as-submission.json")
        self.assertEqual(result["manifest"]["operation"], "REVIEW_AS")
        self.assertEqual(result["manifest"]["spine"], "/architecture/beta/spine.md")
        self.assertEqual(result["manifest"]["trigger"]["reference"], candidate)
        self.assertEqual(result["manifest"]["context"]["artifact_inputs"]["primary_concept"], candidate)

    def test_as_revise_can_loop_again_without_new_prompt(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        policy["transitions"].append({
            "id": "as_revision",
            "receipt_schema": "pc-as-review/v1",
            "requires": {"gate": "AS_REVIEW", "disposition": "REVISE",
                         "next_stage_recommendation": "AS_REVISION_REQUIRED",
                         "independent_of_authoring_invocation": True},
            "require_blocking_finding": True,
            "operation": "REVISE_AS", "target": "receipt",
            "trigger_kind": "AS_REVIEW_REVISION_REQUIRED", "gate": "AS_REVIEW",
        })
        policy_path.write_text(yaml.safe_dump(policy), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["REVISE_AS"] = {
            "role": "architecture-agent",
            "playbook": "process/playbooks/REVISE_AS.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        self._put("process/playbooks/REVISE_AS.md", "# Generic AS revision\n")
        self._put("process/tasks/AS-REVIEW.yaml", yaml.safe_dump({
            "id": "AS-REVIEW", "spine": "/architecture/beta/spine.md",
        }))
        self._put("reviews/gates/as-review.json", json.dumps({
            "schema": "pc-as-review/v1", "task_id": "AS-REVIEW",
            "gate": "AS_REVIEW", "disposition": "REVISE",
            "next_stage_recommendation": "AS_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "findings": [{"id": "AS-F1", "severity": "blocking"}],
        }))
        result = next_task.decision(self.root, "reviews/gates/as-review.json")
        self.assertEqual(result["manifest"]["operation"], "REVISE_AS")
        self.assertEqual(result["manifest"]["context"]["review_inputs"]["finding_ids"], ["AS-F1"])
        self._put(result["path"], yaml.safe_dump(result["manifest"]))
        again = next_task.decision(self.root, "reviews/gates/as-review.json")
        self.assertEqual(again["status"], "ALREADY_PLANNED")



    def test_actual_as_review_gate_status_routes_revision(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        policy["transitions"].append({
            "id": "as_revision_review_result",
            "receipt_schema": "pc-as-review/v1",
            "requires": {
                "gate": "AS_REVIEW", "disposition": "REVISE",
                "gate_status": "AS_REVISION_REQUIRED",
                "independent_of_authoring_invocation": True,
            },
            "require_blocking_finding": True,
            "operation": "REVISE_AS", "target": "receipt",
            "trigger_kind": "AS_REVIEW_REVISION_REQUIRED",
            "gate": "AS_REVIEW",
        })
        policy_path.write_text(yaml.safe_dump(policy), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["REVISE_AS"] = {
            "role": "architecture-agent",
            "playbook": "process/playbooks/REVISE_AS.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        self._put("process/playbooks/REVISE_AS.md", "# Correct AS\n")
        self._put("process/tasks/AS-REVIEW.yaml", yaml.safe_dump({
            "id": "AS-REVIEW", "spine": "/architecture/alpha/spine.md",
        }))
        self._put("reviews/gates/as-result.json", json.dumps({
            "schema": "pc-as-review/v1", "task_id": "AS-REVIEW",
            "gate": "AS_REVIEW", "disposition": "REVISE",
            "gate_status": "AS_REVISION_REQUIRED",
            "independent_of_authoring_invocation": True,
            "findings": [
                {"id": "ASR-001", "severity": "blocking"},
                {"id": "ASR-002", "severity": "blocking_for_downstream_authorization"},
            ],
        }))
        out = next_task.decision(self.root, "reviews/gates/as-result.json")
        self.assertEqual(out["manifest"]["operation"], "REVISE_AS")
        self.assertEqual(out["manifest"]["context"]["review_inputs"]["finding_ids"], ["ASR-001"])

    def test_dependent_only_as_resubmission_uses_original_review_subject(self):
        policy_path = self.root / "process/loop_transitions.yaml"
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        policy["transitions"].append({
            "id": "as_re_review", "receipt_schema": "pc-gate-receipt/v1",
            "requires": {"gate": "AS_REVIEW",
                         "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW"},
            "operation": "REVIEW_AS", "target": "changed_concept",
            "concept_type": "Architecture Statement",
            "related_concept_type": None,
            "trigger_kind": "AS_REVISION_SUBMITTED", "gate": "AS_REVIEW",
        })
        policy_path.write_text(yaml.safe_dump(policy), encoding="utf-8")
        ops_path = self.root / "process/operations.yaml"
        ops = yaml.safe_load(ops_path.read_text(encoding="utf-8"))
        ops["operations"]["REVIEW_AS"] = {
            "role": "verification-agent",
            "playbook": "process/playbooks/REVIEW_AS.md",
        }
        ops_path.write_text(yaml.safe_dump(ops), encoding="utf-8")
        self._put("process/playbooks/REVIEW_AS.md", "# Review AS\n")
        self._put("process/tasks/VP-CORRECTION.yaml", yaml.safe_dump({
            "id": "VP-CORRECTION", "spine": "/architecture/beta/spine.md",
        }))
        unchanged = "knowledge/architecture/beta/statement-v2.md"
        updated = "knowledge/architecture/beta/verification_plan-v3.md"
        self._put(unchanged, "---\ntype: Architecture Statement\nid: AS-BETA-v2\nstatus: draft\n---\n")
        self._put(updated, "---\ntype: Verification Plan\nid: VP-BETA-v3\nstatus: draft\n---\n")
        self._put("reviews/gates/vp-resubmission.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "VP-CORRECTION",
            "gate": "AS_REVIEW", "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW",
            "review_subject": unchanged,
            "changed_artifacts": [updated],
        }))
        out = next_task.decision(self.root, "reviews/gates/vp-resubmission.json")
        self.assertEqual(out["manifest"]["operation"], "REVIEW_AS")
        self.assertEqual(out["manifest"]["trigger"]["reference"], unchanged)
        # Re-running the same submission must be idempotent.
        self._put(out["path"], yaml.safe_dump(out["manifest"]))
        same = next_task.decision(self.root, "reviews/gates/vp-resubmission.json")
        self.assertEqual(same["status"], "ALREADY_PLANNED")
        # A later VP-only correction reuses the AS review subject but must
        # receive a fresh independent review task for its distinct receipt.
        updated_again = "knowledge/architecture/beta/verification_plan-v4.md"
        self._put(updated_again, "---\ntype: Verification Plan\nid: VP-BETA-v4\nstatus: draft\n---\n")
        self._put("reviews/gates/vp-resubmission-v4.json", json.dumps({
            "schema": "pc-gate-receipt/v1", "task_id": "VP-CORRECTION",
            "gate": "AS_REVIEW",
            "status": "AS_REVISION_READY_FOR_INDEPENDENT_REVIEW",
            "review_subject": unchanged,
            "changed_artifacts": [updated_again],
        }))
        fresh = next_task.decision(self.root, "reviews/gates/vp-resubmission-v4.json")
        self.assertEqual(fresh["status"], "NEW")
        self.assertNotEqual(fresh["path"], out["path"])



if __name__ == "__main__":
    unittest.main()
