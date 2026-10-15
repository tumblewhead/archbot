"""Review-route and immutable subject canary; not an independent audit verdict."""
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
    header = b"blob " + str(len(data)).encode("ascii") + b"\\0"
    return hashlib.sha1(header + data).hexdigest()


class GenericityIndependentReviewRouteTests(unittest.TestCase):
    MANIFEST = "process/tasks/REVIEW_GENERICITY_PREFREEZE-001.yaml"

    def load_manifest(self):
        return yaml.safe_load((ROOT / self.MANIFEST).read_text(encoding="utf-8"))

    def test_review_is_registered_and_renderable(self):
        selected = task.validate(ROOT, self.MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_GENERICITY_AUDIT")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "GENERICITY_PREFREEZE_AUDIT_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn("REVIEW_GENERICITY_AUDIT", prompt)
        self.assertIn(self.MANIFEST, prompt)

    def test_submitted_candidate_pinned_and_safe(self):
        m = self.load_manifest()
        p = m["context"]["review_inputs"]
        self.assertEqual(m["trigger"]["reference"], p["candidate_receipt"])
        self.assertEqual(m["trigger"]["revision"], p["candidate_commit"])
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(p["expected_schema"], "pc-genericity-audit/v1")
        self.assertEqual(p["scope"], "FRAMEWORK_PREFREEZE_AUDIT_ONLY")
        for prefix in ("candidate_report", "candidate_receipt"):
            filename = p[prefix]
            self.assertTrue(filename.startswith("reviews/qualification/"))
            contents = (ROOT / filename).read_bytes()
            self.assertEqual(git_blob_sha1(contents), p[prefix + "_blob_sha1"])
            self.assertNotEqual(git_blob_sha1(contents + b"X"), p[prefix + "_blob_sha1"])
        candidate = json.loads((ROOT / p["candidate_receipt"]).read_text(encoding="utf-8"))
        self.assertEqual(candidate["schema"], p["expected_schema"])
        self.assertEqual(candidate["task_id"], "AUDIT_GENERICITY-PREFREEZE-001")
        self.assertEqual(candidate["report"], p["candidate_report"])
        self.assertEqual(candidate["source_revision"], p["source_snapshot"])
        self.assertEqual(candidate["disposition"], "AUDIT_CANDIDATE_ONLY")
        self.assertTrue(candidate["independent_review_required"])
        for key in ("freeze_authorized", "cleanroom_authorized", "product_verified"):
            self.assertIs(candidate[key], False)
        self.assertEqual(candidate["vo_discharged"], [])

    def test_review_is_never_a_freeze_or_product_gate(self):
        m = self.load_manifest()
        banned = m["outputs"]["prohibited"]
        for action in ("modify_candidate_audit", "discharge_VO", "freeze_generic_process",
                       "authorize_cleanroom", "modify_approved_AS_AP_F_CON_or_DE"):
            self.assertIn(action, banned)
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
