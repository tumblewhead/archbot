"""Route and immutable R1 evidence canary; not an independent review verdict."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task

MANIFEST = "process/tasks/REVIEW_FR001_PROJECT_CONTEXT_R1-001.yaml"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def historical_bytes(revision: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", revision + ":" + path],
        cwd=ROOT, capture_output=True, check=False,
    )
    if result.returncode != 0:
        raise AssertionError("Pinned Git input missing: " + path)
    return result.stdout


class FR001R1ReviewRoutingTests(unittest.TestCase):
    def manifest(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text(encoding="utf-8"))

    def test_registered_independent_reviewer_and_gate(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_FRAMEWORK_REPAIR_R1")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "FR001_R1_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, prompt)
        self.assertIn("REVIEW_FRAMEWORK_REPAIR_R1", prompt)

    def test_pinned_r1_receipt_and_source_identities(self):
        m = self.manifest()
        v = m["context"]["review_inputs"]
        self.assertEqual(m["trigger"]["reference"], v["submission_path"])
        self.assertEqual(m["trigger"]["revision"], v["source_revision"])
        receipt_bytes = historical_bytes(v["submission_commit"], v["submission_path"])
        self.assertEqual(git_blob_sha1(receipt_bytes), v["submission_blob_sha1"])
        obj = json.loads(receipt_bytes.decode("utf-8"))
        self.assertEqual(obj["schema"], v["expected_submission_schema"])
        self.assertEqual(obj["task_id"], v["repair_id"])
        self.assertEqual(obj["source_revision"], v["source_revision"])
        self.assertEqual(obj["r1_implementation_revision"], v["implementation_revision"])
        self.assertEqual(sorted(obj["addressed_findings"]), sorted(v["addressed_findings"]))
        self.assertFalse(obj["independently_reviewed"])
        self.assertEqual(len(obj["checks"]), 7)
        self.assertTrue(all(x["exit_code"] == 0 for x in obj["checks"]))
        for x in obj["checks"]:
            self.assertRegex(x["log_sha256"], r"^[0-9a-f]{64}$")
            self.assertGreater(x["log_bytes"], 0)
        self.assertEqual(set(v["reviewed_source_blob_sha1"]), set(obj["source_sha256"]))
        for path, blob in v["reviewed_source_blob_sha1"].items():
            data = historical_bytes(v["source_revision"], path)
            self.assertEqual(git_blob_sha1(data), blob)
            self.assertEqual(hashlib.sha256(data).hexdigest(), obj["source_sha256"][path])

    def test_prior_revise_receipt_and_no_freeze(self):
        m = self.manifest()
        v = m["context"]["review_inputs"]
        old = json.loads((ROOT / v["previous_review"]).read_text(encoding="utf-8"))
        self.assertEqual(old["disposition"], "REVISE")
        self.assertEqual(v["previous_disposition"], "REVISE")
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        for prohibited in ("rewrite_prior_REVISE_review", "discharge_VO", "accept_AD",
                           "implement_FR002", "freeze_generic_process", "authorize_cleanroom"):
            self.assertIn(prohibited, m["outputs"]["prohibited"])


if __name__ == "__main__":
    unittest.main()
