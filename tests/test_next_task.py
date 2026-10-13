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



if __name__ == "__main__":
    unittest.main()
