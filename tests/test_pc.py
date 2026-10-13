import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import pc


class ProgressiveConcretizationTests(unittest.TestCase):
    def setUp(self):
        self.docs = pc.catalog()
        self.spine = (pc.KB / 'architecture/AS-001/spine.md').resolve()
        self.views = pc.load_yaml(pc.REPO / 'process/views.yaml')

    def _view(self, role):
        config = self.views['roles'][role]
        nodes = pc.traverse(self.spine, set(config['follow']), config['max_depth'],
                            set(self.views['mandatory_closure']), self.docs)
        return {path.relative_to(pc.KB).as_posix() for path, _, _ in nodes}

    def test_full_structural_check(self):
        self.assertEqual(pc.check(), 0)

    def test_proof_scout_gets_results_not_raw(self):
        nodes = self._view('proof-scout')
        self.assertIn('architecture/AS-001/evidence/results.md', nodes)
        self.assertNotIn('architecture/AS-001/evidence/raw/samples.csv', nodes)
        self.assertIn('bkp/adc.md', nodes)

    def test_investigator_sees_raw_but_not_forced_to_read_it(self):
        nodes = self._view('experimental-investigator')
        self.assertIn('architecture/AS-001/evidence/raw/samples.csv', nodes)

    def test_boundary_for_accumulator_width(self):
        bound = 32 * (2**12 - 1)**2
        self.assertEqual(bound, 536608800)
        self.assertLessEqual(bound, 2**32 - 1)
        # This numerical assertion is NOT a complete rolling-update proof.

    def test_invalid_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            pc.resolve_target(self.spine, '/../../etc/passwd')


if __name__ == '__main__':
    unittest.main()
