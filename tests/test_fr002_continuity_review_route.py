"""FR-002 cooperative-continuity review routing and historical evidence canary.

Structural route checks never substitute for an independent engineering review.
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

MANIFEST = "process/tasks/REVIEW_FR002_BASELINE_CONTINUITY-001.yaml"


def historical_bytes(revision, path):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Unsafe historical revision")
    if (not path or path.startswith("/") or ".." in Path(path).parts
            or "\\" in path or ":" in path):
        raise ValueError("Unsafe historical file path")
    result = subprocess.run(["git", "show", revision + ":" + path],
                            cwd=ROOT, capture_output=True)
    if result.returncode:
        raise AssertionError("Missing historical evidence: " + path)
    return result.stdout


def blob_sha1(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii")
                        + b"\0" + data).hexdigest()


class BaselineContinuityReviewRouteTests(unittest.TestCase):
    def read_manifest(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text(encoding="utf-8"))

    def test_registered_independent_operation(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_BASELINE_CONTINUITY")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"],
                         "FR002_COOPERATIVE_CONTINUITY_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, prompt)
        self.assertIn("REVIEW_BASELINE_CONTINUITY", prompt)

    def test_pinned_receipt_and_ten_source_identities(self):
        m = self.read_manifest()
        v = m["context"]["review_inputs"]
        self.assertEqual(m["trigger"]["reference"], v["submission_path"])
        self.assertEqual(m["trigger"]["revision"], v["source_revision"])
        raw = historical_bytes(v["submission_commit"], v["submission_path"])
        self.assertEqual(blob_sha1(raw), v["submission_blob_sha1"])
        r = json.loads(raw.decode("utf-8"))
        self.assertEqual(r["schema"], v["expected_submission_schema"])
        self.assertEqual(r["task_id"], v["repair_id"])
        self.assertEqual(r["source_revision"], v["source_revision"])
        self.assertFalse(r["independently_reviewed"])
        self.assertEqual(len(r["checks"]), 12)
        self.assertTrue(all(x["exit_code"] == 0 for x in r["checks"]))
        self.assertTrue(all(x["log_bytes"] > 0 and
                            re.fullmatch(r"[a-f0-9]{64}", x["log_sha256"])
                            for x in r["checks"]))
        self.assertEqual(set(r["source_sha256"]), set(v["source_git_blob_sha1"]))
        self.assertEqual(set(r["source_git_blob_sha1"]),
                         set(v["source_git_blob_sha1"]))
        for path, expected in v["source_git_blob_sha1"].items():
            contents = historical_bytes(v["source_revision"], path)
            self.assertEqual(blob_sha1(contents), expected)
            self.assertEqual(r["source_git_blob_sha1"][path], expected)
            self.assertEqual(hashlib.sha256(contents).hexdigest(),
                             r["source_sha256"][path])

    def test_review_boundary_and_prior_revise_preserved(self):
        m = self.read_manifest()
        v = m["context"]["review_inputs"]
        prior = json.loads((ROOT / v["prior_independent_review"]).read_text())
        self.assertEqual(prior["disposition"], "REVISE")
        self.assertEqual(v["prior_disposition"], "REVISE")
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        self.assertIn("REVIEW_FR002_GATE_ADAPTER_R1-001.yaml",
                      v["retired_review_task"])
        for name in ("rewrite_old_REVISE_or_R1_receipts", "discharge_VO",
                     "accept_AD", "implement_FR003", "freeze_generic_framework",
                     "authorize_cleanroom"):
            self.assertIn(name, m["outputs"]["prohibited"])

    def test_reject_unsafe_revision_path(self):
        with self.assertRaises(ValueError):
            historical_bytes("main", "tools/gates/continuity.py")
        with self.assertRaises(ValueError):
            historical_bytes("0" * 40, "../tools/gates/continuity.py")


if __name__ == "__main__":
    unittest.main()
