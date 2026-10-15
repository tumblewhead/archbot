"""Prefreeze route canary. Does not execute Codex or approve a cleanroom."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import task


class PrefreezeAuditRoutingTests(unittest.TestCase):
    def test_prefreeze_audit_registered_and_renderable(self):
        path = "process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml"
        selected = task.validate(ROOT, path)
        self.assertEqual(selected["operation"], "AUDIT_GENERICITY")
        self.assertEqual(selected["role"], "architecture-agent")
        self.assertEqual(selected["gate"], "GENERICITY_PREFREEZE_AUDIT_REVIEW")
        self.assertIn("AUDIT_GENERICITY", task.make_prompt(ROOT, selected))
        self.assertIn(path, task.make_prompt(ROOT, selected))

    def test_no_freeze_or_product_approval_in_audit_manifest(self):
        manifest = yaml.safe_load(
            (ROOT / "process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml").read_text()
        )
        forbidden = manifest["outputs"]["prohibited"]
        self.assertIn("freeze_generic_process", forbidden)
        self.assertIn("authorize_cleanroom", forbidden)
        self.assertIn("discharge_VO", forbidden)
        self.assertTrue(manifest["gate"]["require_independent_review"])
        receipt = json.loads((ROOT / manifest["trigger"]["reference"]).read_text())
        self.assertEqual(receipt["disposition"], "ACCEPT_WITH_CLARIFICATIONS")
        self.assertEqual(receipt["vo_discharged"], [])

    def test_collaboration_contract_distinguishes_current_agent(self):
        protocol = json.loads(
            (ROOT / "process/pull_run_push_contract.v1.json").read_text()
        )
        self.assertEqual(protocol["schema"], "pc-pull-run-push-collaboration/v1")
        direct = protocol["execution_modes"]["current_agent_direct"]
        self.assertIn("render", direct["render"])
        self.assertIn("Do not recursively call task.py run", direct["execute"])
        self.assertIn("DIRECT_IN_CURRENT_INVOCATION", direct["evidence"])


if __name__ == "__main__":
    unittest.main()
