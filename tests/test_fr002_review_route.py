"""FR-002 independent-review routing and original source-pinning canary.

Structural registration checks, NOT an independent gate verdict.
"""
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

MANIFEST = "process/tasks/REVIEW_FR002_GATE_ADAPTER-001.yaml"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def historical_bytes(revision: str, path: str) -> bytes:
    result = subprocess.run(["git", "show", revision + ":" + path],
                            cwd=ROOT, capture_output=True, check=False)
    if result.returncode:
        raise AssertionError("Missing pinned historical evidence: " + path)
    return result.stdout


class FR002IndependentReviewRouteTests(unittest.TestCase):
    def manifest(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text(encoding="utf-8"))

    def test_registered_operation_and_independent_gate(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_GATE_ADAPTER")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "FR002_GATE_ADAPTER_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, prompt)
        self.assertIn("REVIEW_GATE_ADAPTER", prompt)

    def test_historical_evidence_and_seven_source_fingerprints(self):
        v = self.manifest()["context"]["review_inputs"]
        receipt_bytes = historical_bytes(
            v["submitted_evidence_commit"], v["submitted_evidence_path"])
        self.assertEqual(git_blob_sha1(receipt_bytes),
                         v["submitted_evidence_blob_sha1"])
        obj = json.loads(receipt_bytes.decode("utf-8"))
        self.assertEqual(obj["schema"], v["submitted_evidence_schema"])
        self.assertEqual(obj["task_id"], v["repair_id"])
        self.assertEqual(obj["source_revision"], v["source_revision"])
        self.assertFalse(obj["independently_reviewed"])
        self.assertEqual(len(obj["checks"]), 9)
        self.assertTrue(all(x["exit_code"] == 0 for x in obj["checks"]))
        for x in obj["checks"]:
            self.assertGreater(x["log_bytes"], 0)
            self.assertRegex(x["log_sha256"], r"^[0-9a-f]{64}$")
        self.assertEqual(set(v["source_git_blob_sha1"]), set(obj["source_sha256"]))
        for path, blob in v["source_git_blob_sha1"].items():
            source = historical_bytes(v["source_revision"], path)
            self.assertEqual(git_blob_sha1(source), blob)
            self.assertEqual(hashlib.sha256(source).hexdigest(),
                             obj["source_sha256"][path])

    def test_no_approval_or_product_discharge_in_manifest(self):
        m = self.manifest()
        self.assertEqual(m["trigger"]["reference"],
                         m["context"]["review_inputs"]["submitted_evidence_path"])
        self.assertEqual(m["trigger"]["revision"],
                         m["context"]["review_inputs"]["source_revision"])
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        for x in ("approve_own_gate", "discharge_VO", "accept_AD", "implement_FR003",
                  "freeze_generic_process", "authorize_cleanroom"):
            self.assertIn(x, m["outputs"]["prohibited"])


if __name__ == "__main__":
    unittest.main()
