"""FR-003 historical audit: synthetic Git histories, no product approval."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import historical_audit as ha


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True,
        text=True, check=True,
    ).stdout.strip()


class HistoricalAuditTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        git(self.root, "init", "-q")
        self.file_ref = "knowledge/other-project/root.txt"
        path = self.root / self.file_ref
        path.parent.mkdir(parents=True)
        path.write_bytes(b"version-one\n")
        self.initial = b"version-one\n"
        self.initial_sha = hashlib.sha256(self.initial).hexdigest()
        self.initial_blob = ha.git_blob_sha1(self.initial)
        self.revision = self.commit("Initial reviewed source")
        self.receipt_ref = "reviews/authoring.json"
        self.receipt = {
            "schema": "pc-framework-repair-test-evidence/v1",
            "source_revision": self.revision,
            "review_state": "PENDING",
            "source_sha256": {self.file_ref: self.initial_sha},
            "source_git_blob_sha1": {self.file_ref: self.initial_blob},
        }
        self.write_receipt()

    def commit(self, message):
        git(self.root, "add", "-A")
        git(self.root, "-c", "user.name=Fixture",
            "-c", "user.email=fixture@example.invalid",
            "commit", "-q", "-m", message)
        return git(self.root, "rev-parse", "HEAD")

    def write_receipt(self):
        path = self.root / self.receipt_ref
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.receipt, indent=2) + "\n")
        return path

    def test_source_time_remains_match_after_later_commit(self):
        (self.root / self.file_ref).write_bytes(b"version-two\n")
        self.commit("Later source revision")
        report = ha.inspect(self.root, self.receipt_ref, check_current=True)
        self.assertEqual(report["historical_status"], "HISTORICAL_MATCH")
        self.assertEqual(report["current_correspondence"]["status"], "DIFFERENT")
        self.assertEqual(report["present_applicability"], "NOT_EVALUATED")
        self.assertEqual(report["authoring_review_state"], "PENDING")
        self.assertFalse(report["product_verified"])

    def test_historical_mismatch_independent_of_current_match(self):
        newer = b"changed\n"
        self.receipt["source_sha256"][self.file_ref] = hashlib.sha256(newer).hexdigest()
        self.receipt.pop("source_git_blob_sha1")
        self.write_receipt()
        (self.root / self.file_ref).write_bytes(newer)
        report = ha.inspect(self.root, self.receipt_ref, check_current=True)
        self.assertEqual(report["historical_status"], "HISTORICAL_MISMATCH")
        self.assertEqual(report["current_correspondence"]["status"], "ALL_MATCH")

    def test_git_blob_hash_is_not_raw_sha1(self):
        self.receipt["source_git_blob_sha1"][self.file_ref] = hashlib.sha1(
            self.initial).hexdigest()
        self.write_receipt()
        result = ha.inspect(self.root, self.receipt_ref)
        self.assertEqual(result["historical_status"], "HISTORICAL_MISMATCH")
        self.assertEqual(result["items"][0]["historical_sha256"], self.initial_sha)
        self.assertNotEqual(result["items"][0]["historical_git_blob_sha1"],
                            self.receipt["source_git_blob_sha1"][self.file_ref])

    def test_missing_or_conflicting_revision_is_unresolved(self):
        for revision in ("HEAD", "main", "0" * 40):
            with self.subTest(revision=revision):
                result = ha.inspect(self.root, self.receipt_ref, revision=revision)
                self.assertEqual(result["historical_status"], "UNRESOLVED")
        self.receipt.pop("source_revision")
        self.write_receipt()
        result = ha.inspect(self.root, self.receipt_ref)
        self.assertEqual(result["historical_status"], "UNRESOLVED")
        self.assertIn("source-time", result["reason"])

    def test_missing_historical_file_is_unresolved(self):
        self.receipt["source_sha256"] = {"knowledge/other-project/missing.txt": "0" * 64}
        self.receipt.pop("source_git_blob_sha1")
        self.write_receipt()
        report = ha.inspect(self.root, self.receipt_ref)
        self.assertEqual(report["historical_status"], "UNRESOLVED")
        self.assertEqual(report["items"][0]["status"], "UNRESOLVED")

    def test_unsafe_paths_and_aliases_are_rejected(self):
        for bad in ("../root.txt", "/etc/passwd", "a/../b", "x:HEAD", "a//b",
                    ".git/config", "a\\b", "a/./b"):
            with self.subTest(path=bad):
                self.receipt["source_sha256"] = {bad: self.initial_sha}
                self.receipt.pop("source_git_blob_sha1", None)
                self.write_receipt()
                report = ha.inspect(self.root, self.receipt_ref)
                self.assertEqual(report["historical_status"], "UNRESOLVED")
        self.assertEqual(ha.inspect(self.root, "../bad.json")["historical_status"],
                         "UNRESOLVED")

    def test_unsupported_schema_and_missing_digest_unresolved(self):
        self.receipt["schema"] = "unknown-unreviewed-shape"
        self.write_receipt()
        self.assertEqual(ha.inspect(self.root, self.receipt_ref)["historical_status"],
                         "UNRESOLVED")
        self.receipt["schema"] = "pc-framework-repair-test-evidence/v1"
        self.receipt.pop("source_sha256")
        self.write_receipt()
        self.assertEqual(ha.inspect(self.root, self.receipt_ref)["historical_status"],
                         "UNRESOLVED")

    def test_review_overlay_never_rewrites_authoring_pending(self):
        review_ref = "reviews/independent.json"
        review = {
            "schema": "pc-framework-repair-review/v1",
            "submitted_evidence_path": self.receipt_ref,
            "reviewed_source_revision": self.revision,
            "disposition": "ACCEPT_WITH_CLARIFICATIONS",
            "disposition_scope": "SYNTHETIC_ONLY",
            "independent_of_authoring_invocation": True,
        }
        dest = self.root / review_ref
        dest.write_text(json.dumps(review))
        report = ha.inspect(self.root, self.receipt_ref, review_ref=review_ref)
        self.assertEqual(report["historical_status"], "HISTORICAL_MATCH")
        self.assertEqual(report["authoring_review_state"], "PENDING")
        self.assertEqual(report["review_overlay"]["disposition"],
                         "ACCEPT_WITH_CLARIFICATIONS")
        review["reviewed_source_revision"] = "0" * 40
        dest.write_text(json.dumps(review))
        bad = ha.inspect(self.root, self.receipt_ref, review_ref=review_ref)
        self.assertEqual(bad["historical_status"], "HISTORICAL_MATCH")
        self.assertEqual(bad["review_overlay"]["status"], "UNRESOLVED")

    def test_symlink_historical_blob_is_unresolved(self):
        link = self.root / "knowledge/other-project/link.txt"
        link.symlink_to("root.txt")
        revised = self.commit("Add symbolic-link source")
        self.receipt["source_revision"] = revised
        self.receipt["source_sha256"] = {
            "knowledge/other-project/link.txt": hashlib.sha256(
                b"root.txt").hexdigest()
        }
        self.receipt.pop("source_git_blob_sha1", None)
        self.write_receipt()
        audit = ha.inspect(self.root, self.receipt_ref)
        self.assertEqual(audit["historical_status"], "UNRESOLVED")
        self.assertIn("regular file", audit["items"][0]["reason"])

    def test_verification_receipt_needs_explicit_source_revision(self):
        self.receipt["schema"] = "pc-verification/v1"
        self.receipt.pop("source_revision")
        self.receipt.pop("source_git_blob_sha1")
        self.write_receipt()
        self.assertEqual(ha.inspect(self.root, self.receipt_ref)["historical_status"],
                         "UNRESOLVED")
        self.receipt["source_revision"] = self.revision
        self.write_receipt()
        self.assertEqual(ha.inspect(self.root, self.receipt_ref)["historical_status"],
                         "HISTORICAL_MATCH")

    def test_review_receipt_shape_is_supported(self):
        self.receipt = {
            "schema": "pc-framework-repair-review/v1",
            "reviewed_source_revision": self.revision,
            "verified_source_sha256": {self.file_ref: self.initial_sha},
            "verified_source_sha1": {self.file_ref: self.initial_blob},
        }
        self.write_receipt()
        report = ha.inspect(self.root, self.receipt_ref)
        self.assertEqual(report["historical_status"], "HISTORICAL_MATCH")

    def test_real_fr002_source_receipt(self):
        # Regression against canonical, committed FR-002 evidence, if history
        # is locally available. No network fetching or test-time mutations.
        ref = "reviews/qualification/FR002_BASELINE_CONTINUITY-local-test-receipt.json"
        result = ha.inspect(ROOT, ref)
        self.assertEqual(result["historical_status"], "HISTORICAL_MATCH",
                         result.get("reason"))
        self.assertEqual(len(result["items"]), 10)


if __name__ == "__main__":
    unittest.main()
