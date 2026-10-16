"""Pre-freeze Toy 1 pipe-cleaner package: isolation canaries only.

Successful tests do not prove an agent's runtime has no external access.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import cleanroom_pipe_cleaner as pc


class Toy1PipeCleanerTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.dest = self.tmp / "prepared"

    def prepare(self):
        result = pc.prepare(ROOT, self.dest)
        self.assertEqual(result["schema"], pc.SCHEMA)
        return result

    def test_source_time_allowlist_and_empty_unsolved_start(self):
        manifest = self.prepare()
        self.assertEqual(len(manifest["allowlisted_files"]),
                         len(pc.SOURCES) + len(pc.GENERATED))
        paths = {x["path"] for x in manifest["allowlisted_files"]}
        self.assertIn("projects/CLN-001/knowledge/bkp/problem-origin.md", paths)
        self.assertNotIn("knowledge/architecture/AS-001/spine.md", paths)
        self.assertFalse((self.dest / "workspace" / ".git").exists())
        self.assertFalse((self.dest / "workspace" / "implementation").exists())
        self.assertFalse((self.dest / "workspace" / "projects" /
                          "CLN-001" / "implementation" / "detector.c").exists())
        self.assertTrue((self.dest / "workspace" / "projects" /
                         "CLN-001" / "out").is_dir())
        self.assertEqual(pc.inspect_package(self.dest)["status"], "PASS")

    def test_only_exact_pinned_bkp_sources_are_copied(self):
        self.prepare()
        for source, (dest, blob) in pc.SOURCES.items():
            original = (ROOT / source).read_bytes()
            package = (self.dest / dest).read_bytes()
            self.assertEqual(original, package)
            self.assertEqual(pc.git_blob_id(package), blob)
        manifest = json.loads((self.dest / "auditor_only" /
                               "manifest.json").read_text())
        self.assertEqual(manifest["reviewed_for_cleanroom"], False)

    def test_unexpected_input_and_modified_seed_fail_preflight(self):
        self.prepare()
        extra = self.dest / "workspace" / "leaked-prior-solution.md"
        extra.write_text("unapproved content")
        self.assertEqual(pc.inspect_package(self.dest)["status"], "FAIL")
        self.assertIn("leaked-prior-solution.md",
                      pc.inspect_package(self.dest)["unexpected"])
        extra.unlink()
        seed = self.dest / "workspace" / "projects" / "CLN-001" / "project.yaml"
        seed.write_text(seed.read_text() + "# unauthorized alteration\n")
        self.assertIn("projects/CLN-001/project.yaml",
                      pc.inspect_package(self.dest)["modified_or_aliased"])

    def test_output_is_allowed_but_symlink_output_is_not(self):
        self.prepare()
        out = self.dest / "workspace" / "projects" / "CLN-001" / "out"
        (out / "AS-DRAFT-001.md").write_text("a candidate, not approved")
        self.assertEqual(pc.inspect_package(self.dest)["status"], "PASS")
        target = self.tmp / "outside"
        target.write_text("secret")
        (out / "alias.md").symlink_to(target)
        report = pc.inspect_package(self.dest)
        self.assertEqual(report["status"], "FAIL")
        self.assertIn("projects/CLN-001/out/alias.md",
                      report["modified_or_aliased"])

    def test_cannot_prepare_inside_source_checkout(self):
        inside = ROOT / "runs" / "should-never-create-pipe-cleaner"
        with self.assertRaisesRegex(pc.PackageError, "outside source"):
            pc.prepare(ROOT, inside)
        self.assertFalse(inside.exists())

    def test_never_replace_a_prior_package(self):
        self.prepare()
        with self.assertRaisesRegex(pc.PackageError, "already exists"):
            pc.prepare(ROOT, self.dest)

    def test_fresh_agent_task_stops_before_downstream_answer(self):
        self.prepare()
        task = (self.dest / "workspace" / "TASK-001.md").read_text()
        self.assertIn("STOP after the first Architecture Statement draft", task)
        self.assertIn("QUESTIONS-001.md", task)
        self.assertNotIn("PR-002", task)
        self.assertNotIn("ring buffer", task.lower())
        self.assertIn("NO APPROVED AS", (self.dest / "workspace" /
                        "projects/CLN-001/PROJECT_SPINE.md").read_text())

    def test_cli_prepare_then_inspect(self):
        cli = ROOT / "tools" / "cleanroom_pipe_cleaner.py"
        prep = subprocess.run([
            sys.executable, str(cli), "prepare", "--output", str(self.dest)
        ], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(prep.returncode, 0, prep.stderr)
        self.assertEqual(json.loads(prep.stdout)["reviewed_for_cleanroom"], False)
        audit = subprocess.run([
            sys.executable, str(cli), "inspect", "--output", str(self.dest)
        ], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(audit.returncode, 0, audit.stderr)
        self.assertEqual(json.loads(audit.stdout)["status"], "PASS")

    def test_project_registry_can_inspect_diagnostic_project(self):
        self.prepare()
        program = self.dest / "workspace" / "framework" / "core" / "project_registry.py"
        out = subprocess.run(
            [sys.executable, str(program), "inspect", "CLN-001", "--root",
             str(self.dest / "workspace")], capture_output=True, text=True
        )
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        report = json.loads(out.stdout)
        self.assertEqual(report["project_id"], "CLN-001")
        self.assertIsNone(report["active_baseline_reference"])
        self.assertEqual(report["declared_validator_count"], 0)


if __name__ == "__main__":
    unittest.main()
