"""FR-003 independent-review route and historical source-identity canary.

This checks registration and evidence provenance, not the audit's correctness.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task

MANIFEST = "process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY-001.yaml"


def git_bytes(revision, path):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Git source revision must be an exact commit SHA")
    if (not path or path.startswith("/") or ".." in Path(path).parts or
            "\\" in path or ":" in path):
        raise ValueError("Unsafe Git source path")
    result = subprocess.run(["git", "show", revision + ":" + path], cwd=ROOT,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise AssertionError("Historical source unavailable: " + path)
    return result.stdout


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii")
                        + b"\0" + raw).hexdigest()


class FR003ReviewRouteTests(unittest.TestCase):
    def read_manifest(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text(encoding="utf-8"))

    def test_registered_independent_review_and_prompt(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_HISTORICAL_INTEGRITY")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"],
                         "FR003_HISTORICAL_INTEGRITY_INDEPENDENT_REVIEW")
        rendered = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, rendered)
        self.assertIn("REVIEW_HISTORICAL_INTEGRITY", rendered)

    def test_submission_receipt_and_nine_historical_source_pins(self):
        doc = self.read_manifest()
        inp = doc["context"]["review_inputs"]
        self.assertEqual(doc["trigger"]["reference"], inp["submission_path"])
        self.assertEqual(doc["trigger"]["revision"], inp["source_revision"])
        receipt_bytes = git_bytes(inp["submission_commit"], inp["submission_path"])
        self.assertEqual(blob_sha(receipt_bytes), inp["submission_blob_sha1"])
        receipt = json.loads(receipt_bytes)
        self.assertEqual(receipt["schema"], inp["submitted_schema"])
        self.assertEqual(receipt["task_id"], inp["repair_id"])
        self.assertEqual(receipt["source_revision"], inp["source_revision"])
        self.assertEqual(receipt["authorization"], inp["authorization"])
        self.assertEqual(receipt["independently_reviewed"], False)
        self.assertEqual(receipt["vo_discharged"], [])
        self.assertEqual(len(receipt["checks"]), 14)
        self.assertTrue(all(check["exit_code"] == 0 for check in receipt["checks"]))
        for check in receipt["checks"]:
            self.assertGreater(check["log_bytes"], 0)
            self.assertRegex(check["log_sha256"], r"^[0-9a-f]{64}$")
        paths = inp["source_git_blob_sha1"]
        self.assertEqual(len(paths), 9)
        self.assertEqual(set(paths), set(receipt["source_git_blob_sha1"]))
        self.assertEqual(set(paths), set(receipt["source_sha256"]))
        for path, expected in paths.items():
            source_bytes = git_bytes(inp["source_revision"], path)
            self.assertEqual(blob_sha(source_bytes), expected)
            self.assertEqual(receipt["source_git_blob_sha1"][path], expected)
            self.assertEqual(hashlib.sha256(source_bytes).hexdigest(),
                             receipt["source_sha256"][path])

    def test_no_promotion_of_review_or_product_authority(self):
        doc = self.read_manifest()
        self.assertTrue(doc["gate"]["require_independent_review"])
        self.assertEqual(doc["gate"]["on_missing_evidence"], "UNRESOLVED")
        prohibited = doc["outputs"]["prohibited"]
        for item in ("rewrite_historical_evidence", "approve_own_gate",
                     "discharge_VO", "accept_AD", "implement_FR004",
                     "freeze_generic_process", "authorize_cleanroom"):
            self.assertIn(item, prohibited)
        self.assertIn("PC-COOPERATIVE-AUDIENCE-001.yaml",
                      doc["context"]["review_inputs"]["operating_assumption"])

    def test_historical_helper_refuses_moving_or_unsafe_ref(self):
        with self.assertRaises(ValueError):
            git_bytes("main", "tools/historical_audit.py")
        with self.assertRaises(ValueError):
            git_bytes("0" * 40, "../tools/historical_audit.py")


if __name__ == "__main__":
    unittest.main()
