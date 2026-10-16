"""FR-003 R1 independent-review routing; structural checks are not a review."""
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

MANIFEST = "process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY_R1-001.yaml"


def git_bytes(rev, path):
    result = subprocess.run(["git", "show", rev + ":" + path], cwd=ROOT,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise AssertionError("Unavailable pinned source: " + path)
    return result.stdout


def blob_id(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() +
                        b"\0" + raw).hexdigest()


class FR003R1RouteTests(unittest.TestCase):
    def task(self):
        return yaml.safe_load((ROOT / MANIFEST).read_text())

    def test_operation_and_prompt(self):
        selected = task.validate(ROOT, MANIFEST)
        self.assertEqual(selected["operation"], "REVIEW_HISTORICAL_INTEGRITY_R1")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "FR003_R1_FOCUSED_INDEPENDENT_REVIEW")
        prompt = task.make_prompt(ROOT, selected)
        self.assertIn(MANIFEST, prompt)

    def test_source_and_test_evidence_revisions(self):
        m = self.task()
        context = m["context"]["review_inputs"]
        data = git_bytes(context["evidence_submission_commit"],
                         context["evidence_submission_path"])
        self.assertEqual(blob_id(data), context["evidence_submission_blob_sha1"])
        receipt = json.loads(data)
        self.assertEqual(receipt["task_id"], context["repair_id"])
        self.assertEqual(receipt["source_revision"],
                         context["reviewed_source_revision"])
        self.assertEqual(receipt["previous_review"], context["first_review"])
        self.assertEqual(receipt["addressed_findings"],
                         [context["addressed_finding"]])
        self.assertEqual(len(receipt["checks"]), 7)
        self.assertTrue(all(x["exit_code"] == 0 for x in receipt["checks"]))
        paths = context["source_git_blob_sha1"]
        self.assertEqual(len(paths), 9)
        self.assertEqual(set(paths), set(receipt["source_git_blob_sha1"]))
        self.assertEqual(set(paths), set(receipt["source_sha256"]))
        for path, expected in paths.items():
            raw = git_bytes(context["reviewed_source_revision"], path)
            self.assertEqual(blob_id(raw), expected)
            self.assertEqual(hashlib.sha256(raw).hexdigest(),
                             receipt["source_sha256"][path])

    def test_previous_revise_and_authority_limits(self):
        m = self.task()
        old = json.loads((ROOT /
            m["context"]["review_inputs"]["first_review"]).read_text())
        self.assertEqual(old["disposition"], "REVISE")
        self.assertTrue(m["gate"]["require_independent_review"])
        self.assertEqual(m["gate"]["on_missing_evidence"], "UNRESOLVED")
        for item in ("rewrite_original_REVISE_receipt", "discharge_VO",
                     "implement_FR004", "freeze_framework", "authorize_cleanroom"):
            self.assertIn(item, m["outputs"]["prohibited"])


if __name__ == "__main__":
    unittest.main()
