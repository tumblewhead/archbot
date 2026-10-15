"""Local host-only layout collection checks; never assert target-SRAM acceptance."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]
COLLECTOR = ROOT / "tools/toy1_resource_evidence.py"


class Toy1ResourceEvidenceTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("cc"), "Host compiler not available")
    def test_host_observation_is_not_target_qualification(self):
        case = "test-vr001-" + uuid.uuid4().hex[:12]
        raw = ROOT / "runs" / case
        report = ROOT / "reviews" / "verification" / (case + ".json")
        self.addCleanup(lambda: shutil.rmtree(raw, ignore_errors=True))
        self.addCleanup(lambda: report.unlink(missing_ok=True))
        result = subprocess.run([sys.executable, str(COLLECTOR), "--out",
                                 "runs/" + case, "--summary",
                                 "reviews/verification/" + case + ".json"],
                                cwd=ROOT, capture_output=True, text=True,
                                timeout=90, check=False)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        record = json.loads(report.read_text())
        self.assertEqual(record["observation_status"], "HOST_LAYOUT_RECORDED")
        layout = record["host_layout_observation"]
        self.assertEqual(layout["window"], 32)
        self.assertEqual(layout["sizeof_samples"], 64)
        self.assertGreaterEqual(layout["sizeof_detector"], 69)
        self.assertEqual(layout["field_bytes"], 69)
        self.assertEqual(record["target_status"], "NOT_REQUESTED")
        self.assertFalse(record["target_measurements_available"])
        self.assertEqual(record["vo_discharged"], [])
        self.assertFalse(record["product_verified"])
        self.assertTrue(all(v is None for v in
                            record["measured_target_category_peaks_bytes"].values()))
        self.assertEqual(sum(record["accepted_conditional_envelope_bytes"][
            "category_ceilings"].values()), 1792)

    def test_rejects_output_path_traversal(self):
        result = subprocess.run(
            [sys.executable, str(COLLECTOR), "--out", "../escape",
             "--summary", "reviews/verification/test-escape.json"],
            cwd=ROOT, capture_output=True, text=True, timeout=10, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("RESOURCE_SETUP_INVALID", result.stderr)


    def test_independent_resource_review_task_is_pinned_and_routable(self):
        import yaml
        sys.path.insert(0, str(ROOT / "tools"))
        import task
        ref = "process/tasks/REVIEW_RESOURCE_EVIDENCE-TOY1-VR001.yaml"
        selected = task.validate(ROOT, ref)
        self.assertEqual(selected["operation"], "REVIEW_RESOURCE_EVIDENCE")
        self.assertEqual(selected["role"], "verification-agent")
        self.assertEqual(selected["gate"], "RESOURCE_EVIDENCE_REVIEW")
        task_data = yaml.safe_load((ROOT / ref).read_text(encoding="utf-8"))
        task_data["context"]["review_inputs"]["evidence_blob_sha1"] = "0" * 40
        with self.assertRaisesRegex(task.TaskError, "identity changed"):
            task.validate_resource_evidence_review(ROOT, task_data)


if __name__ == "__main__":
    unittest.main()
