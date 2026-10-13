"""Task manifests are reusable across architectures; they never grant approval."""
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task


class TaskManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for p, content in {
            "agents/evaluation-agent.md": "# Evaluator\n",
            "process/views.yaml": yaml.safe_dump({"roles": {"evaluation-agent": {"follow": []}}}),
            "process/playbooks/EVALUATE_AP.md": "# Reusable playbook\n",
            "prompts/generic-task.md": "Do not approve architecture.\n",
            "knowledge/architecture/alpha/spine.md": "# Alpha\n",
            "knowledge/architecture/beta/spine.md": "# Beta\n",
            "reviews/gates/accepted.json": "{}\n",
        }.items():
            dest = self.root / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        self.manifest = {
            "schema": "pc-task/v1",
            "id": "TASK-001", "role": "evaluation-agent",
            "operation": "EVALUATE_AP",
            "spine": "/architecture/alpha/spine.md",
            "trigger": {
                "kind": "VERIFICATION_RECEIPT_ACCEPTED",
                "reference": "reviews/gates/accepted.json",
            },
            "playbook": "process/playbooks/EVALUATE_AP.md",
            "outputs": {"allowed": ["versioned_evaluation"],
                        "prohibited": ["approve_architecture"]},
            "gate": {"kind": "AP_PROVISIONAL_SELECTION",
                     "on_missing_evidence": "UNRESOLVED",
                     "require_independent_review": True},
        }
        self.store()

    def store(self):
        dest = self.root / "process/tasks/task.yaml"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(yaml.safe_dump(self.manifest), encoding="utf-8")

    def test_first_architecture(self):
        selected = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(selected["spine"], "/architecture/alpha/spine.md")
        self.assertIn("process/tasks/task.yaml", task.make_prompt(self.root, selected))

    def test_second_architecture_same_role_and_playbook(self):
        self.manifest["spine"] = "/architecture/beta/spine.md"
        self.store()
        selected = task.validate(self.root, "process/tasks/task.yaml")
        self.assertEqual(selected["spine"], "/architecture/beta/spine.md")
        self.assertEqual(selected["playbook"], "process/playbooks/EVALUATE_AP.md")

    def test_spine_escape_rejected(self):
        self.manifest["spine"] = "/../../etc/passwd"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_playbook_rejected(self):
        self.manifest["playbook"] = "process/playbooks/MISSING.md"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_evidence_must_not_pass(self):
        self.manifest["gate"]["on_missing_evidence"] = "PASS"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")

    def test_missing_role_policy_rejected(self):
        self.manifest["role"] = "unknown"
        self.store()
        with self.assertRaises(task.TaskError):
            task.validate(self.root, "process/tasks/task.yaml")


if __name__ == "__main__":
    unittest.main()
