"""Regression checks for Toy 1 C evidence collection.

These tests deliberately invoke the host compiler on the user's machine.
They do not qualify a target or independently accept a product obligation.
"""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]
COLLECTOR = ROOT / "tools/toy1_c_evidence.py"


class Toy1CompilerEvidenceTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("cc"), "No host C compiler installed")
    def test_positive_controls_and_negative_control(self):
        rel = "runs/test-toy1-evidence-" + uuid.uuid4().hex[:12]
        target = ROOT / rel
        self.addCleanup(lambda: shutil.rmtree(target, ignore_errors=True))
        result = subprocess.run(
            [sys.executable, str(COLLECTOR), "--out", rel],
            cwd=ROOT, capture_output=True, text=True, check=False, timeout=120)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        data = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(data["host_status"], "HOST_PROBE_PASSED")
        self.assertEqual(data["target_status"], "NOT_REQUESTED")
        self.assertFalse(data["product_verified"])
        self.assertEqual(data["vo_discharged"], [])
        commands = {item["label"]: item for item in data["commands"]}
        for variant in ("O0", "O2", "O2-NDEBUG"):
            self.assertEqual(commands["compile-" + variant]["returncode"], 0)
            self.assertEqual(commands["execute-" + variant]["returncode"], 0)
            self.assertIn("HOST_PROBE_OK checks=8192",
                          (target / ("execute-" + variant + ".stdout.txt")).read_text())
        self.assertEqual(commands["compile-negative-NDEBUG"]["returncode"], 0)
        self.assertGreater(commands["execute-negative-NDEBUG"]["returncode"], 0)
        self.assertIn("MISMATCH case=",
                      (target / "execute-negative-NDEBUG.stderr.txt").read_text())

    def test_rejects_output_outside_runs(self):
        result = subprocess.run(
            [sys.executable, str(COLLECTOR), "--out", "../bad-evidence-directory"],
            cwd=ROOT, capture_output=True, text=True, check=False, timeout=10)
        self.assertEqual(result.returncode, 2)
        self.assertIn("EVIDENCE_SETUP_INVALID", result.stderr)

    def test_resource_template_is_unmeasured(self):
        import yaml
        template = yaml.safe_load(
            (ROOT / "process/verification/toy1-vo002-inventory-template-v1.yaml").read_text())
        ceilings = template["category_ceilings_bytes"]
        self.assertEqual(sum(ceilings.values()), 1792)
        self.assertEqual(template["reserve_bytes"], 256)
        self.assertEqual(template["approved_limit_bytes"], 2048)
        self.assertEqual(template["measurement_state"], "NO_TARGET_MEASUREMENTS")
        self.assertFalse(template["product_verified"])
        self.assertTrue(all(x is None for x in template["actual_category_peaks_bytes"].values()))


    def test_independent_compiler_review_task_is_routable_and_pinned(self):
        # This uses the real task registry, role, playbook and pushed evidence.
        sys.path.insert(0, str(ROOT / "tools"))
        import task
        manifest = "process/tasks/REVIEW_COMPILER_EVIDENCE-TOY1-VC001.yaml"
        selected = task.validate(ROOT, manifest)
        self.assertEqual(selected["operation"], "REVIEW_COMPILER_EVIDENCE")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "COMPILER_EVIDENCE_REVIEW")


if __name__ == "__main__":
    unittest.main()
