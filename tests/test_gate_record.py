import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
class GateRecordTest(unittest.TestCase):
    def test_cli_has_help(self):
        out=subprocess.run([sys.executable,str(ROOT/'tools/gate_record.py'),'--help'],capture_output=True,text=True)
        self.assertEqual(out.returncode,0,out.stderr)
    def test_roles_are_declared(self):
        import yaml
        roles=yaml.safe_load((ROOT/'agents/registry.yaml').read_text())['roles']
        views=yaml.safe_load((ROOT/'process/views.yaml').read_text())['roles']
        for role in ('proof-reviewer','evaluation-agent'):
            self.assertIn(role,roles)
            self.assertIn(role,views)
            self.assertTrue((ROOT/roles[role]['file']).exists())
if __name__=='__main__': unittest.main()
