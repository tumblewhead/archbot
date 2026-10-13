import sys
import unittest
from copy import deepcopy
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
                            set(self.views['mandatory_closure']), self.docs,
                            include_nonconcept=bool(config.get('include_nonconcept', False)))
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

    def test_optional_nonconcept_filtered_from_proof_scout(self):
        docs = dict(self.docs)
        meta, body = docs[self.spine]
        meta = deepcopy(meta)
        meta.setdefault('relations', []).append({
            'kind': 'supported_by',
            'target': '/architecture/AS-001/evidence/manifest.json',
        })
        docs[self.spine] = (meta, body)
        target = (pc.KB / 'architecture/AS-001/evidence/manifest.json').resolve()
        args = (self.spine, set(self.views['roles']['proof-scout']['follow']),
                4, set(self.views['mandatory_closure']), docs)
        default_view = {p for p, _, _ in pc.traverse(*args, include_nonconcept=False)}
        explicit_view = {p for p, _, _ in pc.traverse(*args, include_nonconcept=True)}
        self.assertNotIn(target, default_view)
        self.assertIn(target, explicit_view)

    def test_mandatory_nonconcept_not_silently_excluded(self):
        docs = dict(self.docs)
        meta, body = docs[self.spine]
        meta = deepcopy(meta)
        meta.setdefault('relations', []).append({
            'kind': 'assumes',
            'target': '/architecture/AS-001/evidence/manifest.json',
        })
        docs[self.spine] = (meta, body)
        with self.assertRaisesRegex(ValueError, 'Mandatory non-concept dependency excluded'):
            pc.traverse(self.spine, {'assumes'}, 1,
                        set(self.views['mandatory_closure']), docs,
                        include_nonconcept=False)

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
