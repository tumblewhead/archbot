"""FR-001 independent review dispatch and evidence identity canary.

These structural checks do not independently accept any repair or product.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class FrameworkRepairReviewRouteTests(unittest.TestCase):
    MANIFEST = "process/tasks/REVIEW_FR001_PROJECT_CONTEXT-001.yaml"

    def task_manifest(self):
        return yaml.safe_load((ROOT / self.MANIFEST).read_text(encoding="utf-8"))

    def test_operation_role_gate_and_prompt(self):
        selected = task.validate(ROOT, self.MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_FRAMEWORK_REPAIR")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "FR001_PROJECT_CONTEXT_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn(self.MANIFEST, prompt)
        self.assertIn("REVIEW_FRAMEWORK_REPAIR", prompt)

    def test_submission_pin_and_source_fingerprints(self):
        m = self.task_manifest()
        inputs = m["context"]["review_inputs"]
        self.assertEqual(m["trigger"]["reference"], inputs["submission_path"])
        self.assertEqual(m["trigger"]["revision"], inputs["source_revision"])
        evidence_path = ROOT / inputs["submission_path"]
        self.assertEqual(git_blob_sha1(evidence_path.read_bytes()),
                         inputs["submission_blob_sha1"])
        self.assertNotEqual(git_blob_sha1(evidence_path.read_bytes() + b"!"),
                            inputs["submission_blob_sha1"])
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        self.assertEqual(evidence["schema"], inputs["expected_submission_schema"])
        self.assertEqual(evidence["task_id"], inputs["repair_id"])
        self.assertEqual(evidence["source_revision"], inputs["source_revision"])
        self.assertIs(evidence["independently_reviewed"], False)
        for key in ("framework_frozen", "cleanroom_authorized", "product_verified"):
            self.assertIs(evidence[key], False)
        self.assertEqual(evidence["vo_discharged"], [])
        self.assertEqual(len(evidence["checks"]), 6)
        self.assertEqual({c["name"] for c in evidence["checks"]},
                         {"telemetry", "task", "genericity_review",
                          "genericity_audit", "stage_gate", "task_inspect"})
        for check in evidence["checks"]:
            self.assertEqual(check["exit_code"], 0)
            self.assertRegex(check["log_sha256"], r"^[0-9a-f]{64}$")
            self.assertGreater(check["log_bytes"], 0)
        self.assertEqual(set(inputs["reviewed_source_blob_sha1"]),
                         set(evidence["source_sha256"]))
        for path, blob_id in inputs["reviewed_source_blob_sha1"].items():
            data = (ROOT / path).read_bytes()
            self.assertEqual(git_blob_sha1(data), blob_id)
            self.assertEqual(hashlib.sha256(data).hexdigest(),
                             evidence["source_sha256"][path])

    def test_scope_rejects_freeze_and_vo_discharge(self):
        m = self.task_manifest()
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        forbidden = m["outputs"]["prohibited"]
        for action in ("modify_submitted_evidence", "discharge_VO", "accept_AD",
                       "freeze_generic_process", "authorize_cleanroom",
                       "implement_unreviewed_additional_repair"):
            self.assertIn(action, forbidden)
        self.assertEqual(m["context"]["review_inputs"]["scope"],
                         "FR001_PROJECT_CONTEXT_IMPLEMENTATION_REVIEW_ONLY")


if __name__ == "__main__":
    unittest.main()
