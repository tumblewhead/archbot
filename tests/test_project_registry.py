"""Portable Archbot project root regression canaries.

These are synthetic fixtures, not accepted project or cleanroom evidence.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework" / "core"))
import project_registry as pr


class ProjectRegistryTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_empty_registry_has_no_implicit_project(self):
        found = pr.list_projects(self.root)
        self.assertEqual(found["projects"], [])
        self.assertEqual(found["active_project"], None)
        self.assertEqual(found["invalid"], [])
        with self.assertRaises(pr.ProjectError):
            pr.inspect_project(self.root, "AS-001")

    def test_init_emits_only_unsolved_project_scaffold(self):
        project = pr.init_project(self.root, "AS-001")
        self.assertEqual(project["project_id"], "AS-001")
        self.assertEqual(project["installation"], "directory")
        self.assertIsNone(project["active_baseline_reference"])
        p = self.root / "projects" / "AS-001"
        data = yaml.safe_load((p / "project.yaml").read_text())
        self.assertIsNone(data["active_baseline"])
        self.assertEqual(data["declared_validators"], [])
        self.assertIn("NO ACCEPTED ARCHITECTURE", (p / "PROJECT_SPINE.md").read_text())
        self.assertFalse((p / "implementation" / "detector.c").exists())
        self.assertEqual(len(pr.list_projects(self.root)["projects"]), 1)

    def test_drop_in_two_projects_remove_one_no_global_registration(self):
        pr.init_project(self.root, "AS-001")
        pr.init_project(self.root, "ROOT-002")
        a = self.root / "projects" / "AS-001"
        b = self.root / "projects" / "ROOT-002"
        (a / "knowledge" / "private_source.txt").write_text("A only")
        self.assertEqual([p["project_id"] for p in pr.list_projects(self.root)["projects"]],
                         ["AS-001", "ROOT-002"])
        self.assertEqual(pr.inspect_project(self.root, "ROOT-002")["project_id"],
                         "ROOT-002")
        shutil.rmtree(a)
        found = pr.list_projects(self.root)
        self.assertEqual([p["project_id"] for p in found["projects"]], ["ROOT-002"])
        self.assertFalse((b / "knowledge" / "private_source.txt").exists())

    def test_portable_folder_discovery_after_copy(self):
        pr.init_project(self.root, "ROOT-002")
        source = self.root / "projects" / "ROOT-002"
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        target = Path(tmp.name)
        (target / "projects").mkdir()
        shutil.copytree(source, target / "projects" / "ROOT-002")
        result = pr.list_projects(target)
        self.assertEqual(len(result["projects"]), 1)
        self.assertEqual(result["projects"][0]["installation"], "directory")

    def test_refuses_traversal_alias_and_invalid_id(self):
        for bad in ("../foo", "AS/001", ".git", "AS:001", ""):
            with self.subTest(bad=bad), self.assertRaises(pr.ProjectError):
                pr.init_project(self.root, bad)
        pr.init_project(self.root, "ROOT-002")
        filename = self.root / "projects" / "ROOT-002" / "project.yaml"
        data = yaml.safe_load(filename.read_text())
        data["active_baseline"] = "../AS-001/process/authority.yaml"
        filename.write_text(yaml.safe_dump(data))
        with self.assertRaises(pr.ProjectError):
            pr.inspect_project(self.root, "ROOT-002")

    def test_project_ids_and_schema_must_match(self):
        pr.init_project(self.root, "ROOT-002")
        f = self.root / "projects" / "ROOT-002" / "project.yaml"
        obj = yaml.safe_load(f.read_text())
        obj["project_id"] = "AS-001"
        f.write_text(yaml.safe_dump(obj))
        found = pr.list_projects(self.root)
        self.assertEqual(len(found["invalid"]), 1)
        self.assertEqual(found["projects"], [])
        with self.assertRaises(pr.ProjectError):
            pr.inspect_project(self.root, "ROOT-002")

    def test_symlinked_project_and_symlinked_spine_rejected(self):
        pr.init_project(self.root, "ROOT-002")
        p = self.root / "projects" / "ROOT-002"
        external = self.root / "outside.md"
        external.write_text("external")
        (p / "PROJECT_SPINE.md").unlink()
        (p / "PROJECT_SPINE.md").symlink_to(external)
        with self.assertRaises(pr.ProjectError):
            pr.inspect_project(self.root, "ROOT-002")
        (p / "PROJECT_SPINE.md").unlink()
        (p / "PROJECT_SPINE.md").write_text("repaired")
        (self.root / "projects" / "alias").symlink_to(p, target_is_directory=True)
        found = pr.list_projects(self.root)
        self.assertEqual(len(found["projects"]), 1)
        self.assertEqual(len(found["invalid"]), 1)

    def test_validators_declared_not_auto_imported(self):
        pr.init_project(self.root, "ROOT-002")
        p = self.root / "projects" / "ROOT-002"
        marker = self.root / "should-not-exist"
        adapter = p / "adapters" / "validator.py"
        adapter.write_text("from pathlib import Path\nPath(%r).write_text('oops')\n"
                           % str(marker))
        manifest = p / "project.yaml"
        doc = yaml.safe_load(manifest.read_text())
        doc["declared_validators"] = ["adapters/validator.py"]
        manifest.write_text(yaml.safe_dump(doc))
        inspection = pr.inspect_project(self.root, "ROOT-002")
        self.assertEqual(inspection["declared_validator_count"], 1)
        self.assertFalse(marker.exists())

    def test_missing_submodule_worktree_not_selected(self):
        root = self.root
        (root / "projects").mkdir()
        (root / "projects" / "README.md").write_text("Project installations")
        found = pr.list_projects(root)
        self.assertEqual(found["projects"], [])

    def test_gitlink_installed_project_detected(self):
        # Synthetic staged Gitlink tests index classification, not remote cloning.
        pr.init_project(self.root, "ROOT-002")
        def git(*args):
            return subprocess.run(["git", "-C", str(self.root), *args],
                                  check=True, capture_output=True, text=True)
        git("init", "-q")
        git("update-index", "--add", "--cacheinfo",
            "160000," + "1" * 40 + ",projects/ROOT-002")
        p = pr.inspect_project(self.root, "ROOT-002")
        self.assertEqual(p["installation"], "git-submodule")

    def test_cli_list_inspect_init(self):
        program = ROOT / "framework" / "core" / "project_registry.py"
        def cli(*args):
            return subprocess.run([sys.executable, str(program), *args,
                                   "--root", str(self.root)],
                                  capture_output=True, text=True)
        out = cli("list")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(json.loads(out.stdout)["projects"], [])
        new = cli("init", "ROOT-002")
        self.assertEqual(new.returncode, 0, new.stderr)
        self.assertEqual(json.loads(new.stdout)["project_id"], "ROOT-002")
        inspect = cli("inspect", "ROOT-002")
        self.assertEqual(inspect.returncode, 0, inspect.stderr)
        missing = cli("inspect", "AS-001")
        self.assertEqual(missing.returncode, 2)
        self.assertEqual(json.loads(missing.stdout)["status"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
