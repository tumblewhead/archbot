"""VK-001 probes. Product gates are exercised separately from fixture execution."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import verification_kernel as vk
import verification_models as models
import task
import next_task


class KernelTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for relative in ["process/verification/fixtures", "knowledge/verification-fixtures"]:
            shutil.copytree(ROOT / relative, self.root / relative)
        self.package = vk.load(self.root, "process/verification/fixtures/ring.json")
        self.inputs = dict(self.package["source_sha256"])

    def stages(self, package=None):
        p = package or self.package
        ers = vk.derive(self.root, p, "FIXTURE-ERS", self.inputs, fixture=True)
        plan = vk.plan(self.root, ers, "FIXTURE-PLAN", self.inputs, fixture=True)
        evidence = vk.execute(self.root, plan, "FIXTURE-EVIDENCE", self.inputs, fixture=True)
        return ers, plan, evidence

    def test_ring_slice_preserves_reset_and_detects_mutants(self):
        ers, _, evidence = self.stages()
        self.assertIn("F-RESET", ers["payload"]["implementation_observation_gaps"])
        self.assertEqual(len(ers["payload"]["claims"]), 2)
        rows = evidence["payload"]["results"]
        self.assertEqual(rows[0]["details"]["cases"], 4096)
        self.assertEqual(rows[0]["details"]["mismatches"], 0)
        self.assertTrue(all(x["details"]["mismatches"] > 0 for x in rows[1:]))
        self.assertTrue(all(x["requested_claim_status"] == "NOT_DISCHARGED" for x in rows))
        self.assertFalse(evidence["product_verified"])

    def test_bidirectional_coverage_and_normative_preservation(self):
        self.package["claims"].pop(0)
        with self.assertRaisesRegex(vk.VerificationError, "missing from ERS"):
            self.stages()
        self.package = vk.load(self.root, "process/verification/fixtures/ring.json")
        self.package["claims"][0]["statement"] = "Reset is optional"
        with self.assertRaisesRegex(vk.VerificationError, "Normative claim changed"):
            self.stages()

    def test_queue_units_boundary_and_witness(self):
        self.package = vk.load(self.root, "process/verification/fixtures/queue.json")
        _, _, evidence = self.stages()
        rows = evidence["payload"]["results"]
        self.assertEqual(rows[0]["details"]["bound_bytes"], "232")
        self.assertEqual(rows[1]["details"]["bound_bytes"], "296")
        self.assertIsNone(rows[1]["counterexample"])
        self.assertEqual(rows[2]["counterexample"]["required_bytes"], "260")
        self.package["rungs"][0]["parameters"]["latency"]["unit"] = "bytes"
        _, _, evidence = self.stages()
        self.assertEqual(evidence["payload"]["results"][0]["execution_status"], "MODEL_INVALID")

    def test_statistical_units_not_rows(self):
        self.package = vk.load(self.root, "process/verification/fixtures/statistics.json")
        _, _, evidence = self.stages()
        details = evidence["payload"]["results"][0]["details"]
        self.assertEqual(details["unique_units"], 10)
        self.assertEqual(details["duplicate_rows_not_counted"], 90)
        self.assertAlmostEqual(details["upper_failure_probability_float"], 1-0.05**0.1)
        self.package["rungs"][0]["parameters"]["protocol"]["selection"] = "adversarially_selected"
        _, _, evidence = self.stages()
        self.assertEqual(evidence["payload"]["results"][0]["evidence_kind"], "INCONCLUSIVE_SAMPLING_PROTOCOL")

    def test_cycle_and_unknown_dependency_rejected(self):
        self.package["rungs"][0]["scheduled_after_result"] = [self.package["rungs"][1]["id"]]
        with self.assertRaisesRegex(vk.VerificationError, "cycle"):
            self.stages()
        self.package["rungs"][0]["scheduled_after_result"] = ["ABSENT"]
        with self.assertRaisesRegex(vk.VerificationError, "Missing"):
            self.stages()

    def test_diagnostics_can_follow_failure_but_premise_cannot(self):
        bad = self.package["rungs"][1]
        good = self.package["rungs"][0]
        bad["scheduled_after_result"] = []
        good["scheduled_after_result"] = [bad["id"]]
        _, _, evidence = self.stages()
        rows = {x["rung_id"]: x for x in evidence["payload"]["results"]}
        self.assertEqual(rows[good["id"]]["execution_status"], "COMPLETED")
        good["requires_established_claim"] = [{"rung_id": bad["id"], "evidence_kind": "FINITE_MODEL_CHECK",
            "model_sha256": vk.digest({"method":bad["method"], "parameters":bad["parameters"]})}]
        _, _, evidence = self.stages()
        rows = {x["rung_id"]: x for x in evidence["payload"]["results"]}
        self.assertEqual(rows[good["id"]]["execution_status"], "BLOCKED_PREMISE")
        good["requires_established_claim"][0]["model_sha256"] = "0"*64
        with self.assertRaisesRegex(vk.VerificationError, "fingerprint mismatch"):
            self.stages()

    def test_unsupported_and_budget_are_not_success(self):
        self.package["rungs"][0]["method"] = "unavailable_smt/v1"
        self.package["rungs"][1]["max_cases"] = 1
        _, _, evidence = self.stages()
        rows = evidence["payload"]["results"]
        self.assertEqual(rows[0]["execution_status"], "UNSUPPORTED")
        self.assertEqual(rows[1]["execution_status"], "BUDGET_LIMIT")
        self.assertFalse(evidence["product_verified"])

    def test_integrity_is_not_product_acceptance(self):
        ers, _, _ = self.stages()
        ers["product_verified"] = True
        ers["content_sha256"] = vk.digest({k:v for k,v in ers.items() if k!='content_sha256'})
        with self.assertRaisesRegex(vk.VerificationError, "unauthorized acceptance"):
            vk.check_artifact(self.root, ers, fixture=True)

    def test_path_escape_stale_source_and_fixture_boundary(self):
        with self.assertRaises(vk.VerificationError):
            vk.safe_path(self.root, "../secret")
        with self.assertRaisesRegex(vk.VerificationError, "Fixture/project"):
            vk.validate_package(self.root, self.package)
        (self.root / "process/verification/fixtures/claims.md").write_text("changed")
        with self.assertRaisesRegex(vk.VerificationError, "Stale source"):
            self.stages()


class RegisteredWorkflowTests(unittest.TestCase):
    """Uses the actual registry/planner/task entry point; synthetic authority only in tempdir.

    The baseline verifier is mocked here to isolate the new protocol. A separate
    real Toy 1 validation below checks the existing baseline verifier without mocks.
    No synthesized review receipt leaves the temporary test workspace.
    """
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for path in ["process/operations.yaml", "process/loop_transitions.yaml", "process/views.yaml",
                     "tools/task.py", "tools/verification_kernel.py", "tools/verification_models.py",
                     "process/playbooks/VERIFICATION_AUTHOR.md", "process/playbooks/VERIFICATION_REVIEW.md"]:
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/path, dest)
        for role in ("evidence-planning-agent", "experimental-investigator", "verification-agent"):
            dest=self.root/f"agents/{role}.md"; dest.parent.mkdir(exist_ok=True)
            dest.write_text("# Test role\n")
        for rel in ["process/verification/fixtures", "knowledge/verification-fixtures"]:
            shutil.copytree(ROOT/rel, self.root/rel)
        self.package = vk.load(self.root, "process/verification/fixtures/queue.json")
        self.package["mode"]="PROJECT"
        base="process/baselines/fixture-active.yaml"; review="reviews/gates/fixture-implementation.json"
        src="implementation/fixture/source.c"
        self.put(base, "status: active\n")
        self.put(src, "/* Synthetic test source only. */\n")
        review_data={"schema":"pc-implementation-review/v1", "gate":"IMPLEMENTATION_REVIEW",
            "disposition":"ACCEPT", "independent_of_authoring_invocation":True,
            "reviewed_source_sha256":{src:vk.file_hash(self.root/src)}}
        self.put(review, json.dumps(review_data))
        self.package.update(active_baseline=base,implementation_review=review)
        for ref in [base,review,src]: self.package["source_sha256"][ref]=vk.file_hash(self.root/ref)
        self.package_ref="process/verification/test-package.json"
        self.put(self.package_ref,json.dumps(self.package))
        self.manifest={"schema":"pc-task/v1","id":"TEST-ERS","role":"evidence-planning-agent",
            "operation":"DERIVE_ERS","spine":self.package["spine"],
            "playbook":"process/playbooks/VERIFICATION_AUTHOR.md",
            "trigger":{"kind":"VERIFICATION_INPUT","reference":self.package_ref},
            "outputs":{"allowed":["new_versioned_stage_artifact"],"prohibited":["discharge_VO"]},
            "gate":{"kind":"REVIEW_ERS","on_missing_evidence":"UNRESOLVED","require_independent_review":True}}
        self.put("process/tasks/TEST-ERS.yaml",yaml.safe_dump(self.manifest))

    def put(self,path,content):
        dest=self.root/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content)

    def review_and_advance(self,submission_ref):
        decision=next_task.decision(self.root,submission_ref)
        self.put(decision["path"],yaml.safe_dump(decision["manifest"]))
        task.validate(self.root,decision["path"])
        submission=vk.load(self.root,submission_ref)
        review={key:submission[key] for key in ("schema","mode","project_id","spine","subject","artifact")}
        review.update(kind="REVIEW",task_id=decision["manifest"]["id"],operation=decision["manifest"]["operation"],
            reviewed_author_task_id=submission["task_id"],reviewer_invocation_id="synthetic-test-only",
            independent_of_authoring_invocation=True,disposition="ACCEPT_WITH_CLARIFICATIONS",findings=[])
        review_ref="reviews/gates/"+review["task_id"]+".json"
        self.put(review_ref,json.dumps(review))
        nxt=next_task.decision(self.root,review_ref)
        self.put(nxt["path"],yaml.safe_dump(nxt["manifest"]))
        task.validate(self.root,nxt["path"])
        return nxt["manifest"],review_ref

    def test_registered_three_stage_path_and_stale_review(self):
        with patch("active_baseline.verify",return_value={}):
            self.assertEqual(task.validate(self.root,"process/tasks/TEST-ERS.yaml")["executor"],"verification-kernel/v1")
            ers=vk.run_task(self.root,self.manifest)
            self.assertEqual(vk.run_task(self.root,self.manifest)["status"],"ALREADY_PRESENT")
            planner, review_ref=self.review_and_advance(ers["receipt"])
            planned=vk.run_task(self.root,planner)
            executor, _=self.review_and_advance(planned["receipt"])
            executed=vk.run_task(self.root,executor)
            evidence=vk.load(self.root,executed["artifact"])
            self.assertEqual(evidence["kind"],"EVIDENCE")
            self.assertFalse(evidence["product_verified"])
            review=vk.load(self.root,review_ref);review["artifact"]["sha256"]="0"*64
            self.put(review_ref,json.dumps(review))
            with self.assertRaises(vk.VerificationError):vk.run_task(self.root,planner)

    def test_missing_review_never_unlocks_next_stage(self):
        with patch("active_baseline.verify",return_value={}):
            authored=vk.run_task(self.root,self.manifest)
            bad=copy.deepcopy(self.manifest)
            bad.update(operation="DESIGN_VERIFICATION_LADDER",id="BYPASS")
            bad["trigger"]["reference"]=authored["receipt"]
            with self.assertRaisesRegex(vk.VerificationError,"independent review"):
                vk.run_task(self.root,bad)

    def test_actual_toy1_entry_uses_real_authority(self):
        result=task.validate(ROOT,"process/tasks/TOY1-VERIFY-ERS001.yaml")
        self.assertEqual(result["operation"],"DERIVE_ERS")
        self.assertEqual(result["executor"],"verification-kernel/v1")


class RegisteredRoleCompletenessTests(unittest.TestCase):
    """A routed task must not pass planning with an unresolvable role."""

    def test_registry_roles_views_and_playbooks_exist_in_real_checkout(self):
        registry = yaml.safe_load((ROOT / "process/operations.yaml").read_text(encoding="utf-8"))
        views = yaml.safe_load((ROOT / "process/views.yaml").read_text(encoding="utf-8"))
        for name, operation in registry["operations"].items():
            with self.subTest(operation=name):
                role = operation["role"]
                self.assertTrue((ROOT / "agents" / (role + ".md")).is_file(),
                                f"{name}: missing agents/{role}.md")
                self.assertIn(role, views["roles"], f"{name}: missing context view")
                self.assertTrue((ROOT / operation["playbook"]).is_file(),
                                f"{name}: missing registered playbook")


if __name__ == "__main__":
    unittest.main()
