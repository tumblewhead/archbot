"""FR-002 R1 independent review route and historical source-pinning canary.

A successful structural test is not an engineering or independent verdict.
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

MANIFEST = "process/tasks/REVIEW_FR002_GATE_ADAPTER_R1-001.yaml"


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def historical_bytes(revision: str, path: str) -> bytes:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Historical revision must be a full SHA-1")
    if (not path or path.startswith("/") or ".." in Path(path).parts
            or ":" in path or "\\" in path):
        raise ValueError("Unsafe historical source path")
    result = subprocess.run(["git", "show", revision + ":" + path],
                            cwd=ROOT, capture_output=True, check=False)
    if result.returncode != 0:
        raise AssertionError("Pinned source unavailable: " + revision + ":" + path)
    return result.stdout


class FR002R1ReviewRoutingTests(unittest.TestCase):
    def manifest(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text(encoding="utf-8"))

    def test_registered_reviewer_operation_and_gate(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_GATE_ADAPTER_R1")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "FR002_GATE_ADAPTER_R1_INDEPENDENT_REVIEW")
        rendered = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, rendered)
        self.assertIn("REVIEW_GATE_ADAPTER_R1", rendered)

    def test_receipt_and_eight_source_identities_at_pinned_revision(self):
        m = self.manifest()
        v = m["context"]["review_inputs"]
        self.assertEqual(m["trigger"]["reference"], v["submission_path"])
        self.assertEqual(m["trigger"]["revision"], v["source_revision"])
        raw = historical_bytes(v["submission_commit"], v["submission_path"])
        self.assertEqual(git_blob_sha1(raw), v["submission_blob_sha1"])
        r = json.loads(raw.decode("utf-8"))
        self.assertEqual(r["schema"], v["expected_submission_schema"])
        self.assertEqual(r["task_id"], v["repair_id"])
        self.assertEqual(r["source_revision"], v["source_revision"])
        self.assertEqual(sorted(r["addressed_findings"]), sorted(v["addressed_findings"]))
        self.assertFalse(r["independently_reviewed"])
        for key in ("framework_frozen", "cleanroom_authorized", "product_verified"):
            self.assertFalse(r[key])
        self.assertEqual(r["vo_discharged"], [])
        self.assertEqual(len(r["checks"]), 10)
        self.assertTrue(all(c["exit_code"] == 0 for c in r["checks"]))
        for item in r["checks"]:
            self.assertRegex(item["log_sha256"], r"^[0-9a-f]{64}$")
            self.assertGreater(item["log_bytes"], 0)
        self.assertEqual(set(v["source_git_blob_sha1"]), set(r["source_sha256"]))
        self.assertEqual(set(v["source_git_blob_sha1"]), set(r["source_git_blob_sha1"]))
        for path, expected_blob in v["source_git_blob_sha1"].items():
            data = historical_bytes(v["source_revision"], path)
            self.assertEqual(git_blob_sha1(data), expected_blob)
            self.assertEqual(expected_blob, r["source_git_blob_sha1"][path])
            self.assertEqual(hashlib.sha256(data).hexdigest(), r["source_sha256"][path])

    def test_old_revise_is_preserved_and_no_scope_escalation(self):
        m = self.manifest()
        v = m["context"]["review_inputs"]
        old = json.loads((ROOT / v["previous_review"]).read_text(encoding="utf-8"))
        self.assertEqual(old["disposition"], "REVISE")
        self.assertEqual(v["previous_disposition"], "REVISE")
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        for name in ("rewrite_prior_REVISE_review", "discharge_VO", "accept_AD",
                     "implement_FR003", "freeze_generic_process", "authorize_cleanroom"):
            self.assertIn(name, m["outputs"]["prohibited"])

    def test_historical_git_rejects_unsafe_identity(self):
        with self.assertRaises(ValueError):
            historical_bytes("main", "tools/gates/binding.py")
        with self.assertRaises(ValueError):
            historical_bytes("0" * 40, "../tools/gates/binding.py")


if __name__ == "__main__":
    unittest.main()
