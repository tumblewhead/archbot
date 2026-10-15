"""FR-002 synthetic two-project gate canaries; no product/target acceptance."""
from __future__ import annotations
import copy
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import stage_gate
from gates import common
from gates.authority_roots import trusted_root
from gates.binding import blob_id, evaluate_bound, load_binding

TOY1 = "process/gate_configs/AS-001-AP-v1.yaml"


def write_pinned(root, path, obj):
    dest = root / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(yaml.safe_dump(obj, sort_keys=False), encoding='utf-8')
    # Preserve the document's declared identity in the pinned binding.
    # The production loader requires this additional identity agreement:
    # a matching blob alone does not substitute for a reviewed policy ID.
    pin = {'path': path, 'git_blob_sha1': blob_id(dest.read_bytes())}
    if isinstance(obj, dict) and isinstance(obj.get('id'), str):
        pin['id'] = obj['id']
    return pin


class GenericGateAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.toy1 = yaml.safe_load((ROOT / TOY1).read_text(encoding='utf-8'))
        for key in ('spine_source', 'active_baseline', 'baseline_review',
                    'policy', 'vo_ledger', 'ad_ledger'):
            path = self.toy1[key]['path']
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, dest)
        for item in self.toy1['required_validators']:
            for key in ('scope', 'implementation'):
                path = item[key]['path']
                dest = self.root / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, dest)
        # Test source snapshots must include the independent anchor provenance,
        # not merely the candidate binding's self-declared files.
        for spec in trusted_root('AS-001')['sources'].values():
            dest = self.root / spec['path']
            if not dest.is_file():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / spec['path'], dest)
        self.write_binding(self.toy1)

    def write_binding(self, doc):
        path = self.root / TOY1
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding='utf-8')

    def test_real_toy1_binding_has_exact_active_scope(self):
        binding, policy, vo, ad, validators = load_binding(self.root, TOY1)
        self.assertEqual(binding['project_id'], 'AS-001')
        self.assertEqual(policy['protected_scope_decisions'], ['C-002'])
        self.assertEqual([x['requirement'] for x in validators], ['C-002'])
        self.assertEqual(validators[0]['scope']['accounting']['limit_bytes'], 2048)
        self.assertEqual(vo['status'], 'active')
        self.assertTrue(ad['items'])

    def test_missing_wrong_or_duplicate_validator_fails_closed(self):
        for bad in ([], [{'id': 'UNKNOWN', 'requirement': 'C-002'}],
                    self.toy1['required_validators'] * 2):
            with self.subTest(case=bad):
                data = copy.deepcopy(self.toy1)
                data['required_validators'] = bad
                self.write_binding(data)
                with self.assertRaises(ValueError):
                    load_binding(self.root, TOY1)

    def test_changed_policy_pin_and_wrong_project_rejected(self):
        data = copy.deepcopy(self.toy1)
        data['policy']['git_blob_sha1'] = '0' * 40
        self.write_binding(data)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
            load_binding(self.root, TOY1)
        data = copy.deepcopy(self.toy1)
        data['project_id'] = 'ROOT-002'
        data['spine'] = '/architecture/ROOT-002/spine.md'
        self.write_binding(data)
        with self.assertRaises(ValueError):
            load_binding(self.root, TOY1)

    def test_stale_or_wrong_independent_baseline_review_rejected(self):
        doc = copy.deepcopy(self.toy1)
        path = self.root / doc['baseline_review']['path']
        review = yaml.safe_load(path.read_text())
        review['independent_of_baseline_authoring_invocation'] = False
        doc['baseline_review'] = write_pinned(
            self.root, doc['baseline_review']['path'], review)
        self.write_binding(doc)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
            load_binding(self.root, TOY1)

    def test_cross_project_vo_ledger_cannot_be_substituted(self):
        doc = copy.deepcopy(self.toy1)
        vp = doc['vo_ledger']['path']
        ledger = yaml.safe_load((self.root / vp).read_text())
        ledger['activation']['active_baseline'] = 'process/baselines/OTHER.yaml'
        doc['vo_ledger'] = write_pinned(self.root, vp, ledger)
        self.write_binding(doc)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
            load_binding(self.root, TOY1)

    def test_no_unqualified_default_cli(self):
        with self.assertRaises(SystemExit) as raised:
            stage_gate.main(['inspect'])
        self.assertEqual(raised.exception.code, 2)

    def make_root_solver(self):
        project = 'ROOT-002'
        bp = 'process/baselines/ROOT-002.yaml'
        vr = 'reviews/ROOT-002-baseline-review.yaml'
        vol = 'process/ledgers/ROOT-002.yaml'
        spine = 'knowledge/architecture/ROOT-002/spine.md'
        manifest = {
            'schema': 'pc-ap-gate-binding/v1',
            'status': 'candidate_for_independent_review',
            'project_id': project,
            'spine': '/architecture/ROOT-002/spine.md',
            'stage': 'AP',
        }
        manifest['spine_source'] = write_pinned(
            self.root, spine, {'type': 'Architecture Spine', 'id': project})
        manifest['policy'] = write_pinned(
            self.root, 'process/policies/ROOT-AP.yaml', {
                'id': 'ROOT-AP', 'status': 'approved_for_trial',
                'selection_kind': 'PROVISIONAL_COMMITMENT',
                'original_f': 'F-ROOT', 'requirements': ['R-NUM'],
                'ap_due_requirements': ['R-NUM'], 'protected_scope_decisions': [],
            })
        manifest['active_baseline'] = write_pinned(
            self.root, bp, {
                'schema': 'pc-active-baseline/v1', 'id': 'ROOT-002-V1',
                'status': 'active',
                'source_candidate': 'process/baselines/ROOT-002-candidate.yaml',
                'source_candidate_sha256': 'example-reviewed-source-identity',
                'independent_baseline_review': vr,
                'active_artifacts': {
                    'architecture_statement':
                    'knowledge/architecture/ROOT-002/statement.md',
                    'vo_ledger': vol,
                },
            })
        manifest['active_baseline']['id'] = 'ROOT-002-V1'
        manifest['baseline_review'] = write_pinned(
            self.root, vr, {
                'schema': 'pc-baseline-review/v1',
                'independent_of_baseline_authoring_invocation': True,
                'disposition': 'ACCEPT_WITH_CLARIFICATIONS',
                'candidate': 'process/baselines/ROOT-002-candidate.yaml',
                'candidate_sha256': 'example-reviewed-source-identity',
            })
        manifest['vo_ledger'] = write_pinned(
            self.root, vol, {
                'activation': {'active_baseline': bp, 'reviewed_baseline': vr},
                'obligations': [{
                    'id': 'VO-NUM', 'requirement': 'R-NUM',
                    'state': 'open', 'due_stage': 'IMPLEMENTATION',
                    'owner': 'verification-agent',
                }],
            })
        manifest['ad_ledger'] = write_pinned(
            self.root, 'process/ledgers/ROOT-AD.yaml', {
                'items': [{
                    'id': 'AD-ROOT', 'state': 'accepted',
                    'accepted_by': 'TEST AUTHORITY', 'accepted_decision': 'REVIEW',
                    'owner': 'verification-agent', 'due_stage': 'IMPLEMENTATION',
                    'fallback': 'Reconsider root solver',
                }],
            })
        manifest['required_validators'] = []
        path = 'process/gate_configs/ROOT-002-AP.yaml'
        write_pinned(self.root, path, manifest)
        return path

    def test_root_solver_structural_gate_has_no_toy1_c002_or_f001(self):
        path = self.make_root_solver()
        # ROOT-002 is synthetic, and its locally fabricated approval cannot
        # enter the production authority-bound loader.
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)
        bound = yaml.safe_load((self.root / path).read_text())
        policy = yaml.safe_load((self.root / bound['policy']['path']).read_text())
        vo = yaml.safe_load((self.root / bound['vo_ledger']['path']).read_text())
        ad = yaml.safe_load((self.root / bound['ad_ledger']['path']).read_text())
        self.assertEqual(bound['project_id'], 'ROOT-002')
        assessment = {
            'schema': 'pc-ap-assessment/v2', 'candidate': 'AP-NUM', 'stage': 'AP',
            'project_id': 'ROOT-002', 'spine': '/architecture/ROOT-002/spine.md',
            'simulation_only': True, 'policy_id': 'ROOT-AP',
            'requirements': {'R-NUM': {
                'stage_status': 'CONDITIONALLY_SATISFIED',
                'evidence': ['SYNTHETIC NUMERICAL EVIDENCE'],
                'assumptions': ['bounded derivative'], 'vo': 'VO-NUM',
                'final_status': 'OPEN',
                'deferral': {
                    'owner': 'verification-agent', 'method': 'synthetic test',
                    'due_stage': 'IMPLEMENTATION',
                    'acceptance': 'independent evidence',
                    'assumptions': ['bounded derivative'],
                    'escalation': 'reopen AP',
                },
            }},
            'comparative_decision': {
                'mode': 'authorized_tradeoff',
                'authority': 'SIMULATED STAKEHOLDER', 'rationale': 'synthetic',
                'architectural_debt': 'AD-ROOT',
            },
        }
        result = common.evaluate(
            assessment, policy, vo, ad,
            project_id=bound['project_id'], spine=bound['spine'])
        self.assertEqual(result['decision'], 'PASS_SIMULATION', result['errors'])
        self.assertNotIn('C-002', str(result))
        self.assertNotIn('F-001', str(result))
        assessment['spine'] = '/architecture/AS-001/spine.md'
        rejected = common.evaluate(
            assessment, policy, vo, ad,
            project_id=bound['project_id'], spine=bound['spine'])
        self.assertEqual(rejected['decision'], 'NO_DOWNSELECTION')
        self.assertIn('Assessment project identity or spine mismatch', rejected['errors'])

    def test_root_solver_fixture_preserves_policy_identity(self):
        path = self.make_root_solver()
        manifest = yaml.safe_load((self.root / path).read_text())
        self.assertEqual(manifest['policy']['id'], 'ROOT-AP')
        self.assertEqual(manifest['active_baseline']['id'], 'ROOT-002-V1')
        self.assertEqual(
            manifest['policy']['id'],
            yaml.safe_load((self.root / manifest['policy']['path']).read_text())['id'])
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)
        manifest['policy']['id'] = 'WRONG-POLICY'
        write_pinned(self.root, path, manifest)
        self.assertNotEqual(
            manifest['policy']['id'],
            yaml.safe_load((self.root / manifest['policy']['path']).read_text())['id'])
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)

    def test_root_solver_cannot_remove_protected_validator_by_policy_change(self):
        path = self.make_root_solver()
        manifest = yaml.safe_load((self.root / path).read_text())
        policy_path = manifest['policy']['path']
        policy = yaml.safe_load((self.root / policy_path).read_text())
        policy['protected_scope_decisions'] = ['R-NUM']
        manifest['policy'] = write_pinned(self.root, policy_path, policy)
        write_pinned(self.root, path, manifest)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)
        # Generic *mechanics* still block missing required checks in the
        # synthetic project, but such evidence conveys no approval.
        mechanics = common.evaluate(
            {'schema': 'pc-ap-assessment/v2',
             'stage': 'AP', 'candidate': 'ROOT-AP',
             'policy_id': 'ROOT-AP', 'simulation_only': True,
             'project_id': 'ROOT-002',
             'spine': '/architecture/ROOT-002/spine.md',
             'requirements': {},
             'comparative_decision': {'mode': 'supported_projection',
                                      'evidence': ['synthetic']}},
            policy,
            yaml.safe_load((self.root / manifest['vo_ledger']['path']).read_text()),
            yaml.safe_load((self.root / manifest['ad_ledger']['path']).read_text()),
            project_id='ROOT-002', spine='/architecture/ROOT-002/spine.md')
        self.assertEqual(mechanics['decision'], 'NO_DOWNSELECTION')
        self.assertIn('Missing, duplicate or unexpected protected domain validator',
                      mechanics['errors'])

    def test_rehashed_weakened_toy1_policy_cannot_remove_c002(self):
        doc = copy.deepcopy(self.toy1)
        path = doc['policy']['path']
        policy = yaml.safe_load((self.root / path).read_text())
        policy['protected_scope_decisions'] = []
        doc['policy'] = write_pinned(self.root, path, policy)
        doc['required_validators'] = []
        self.write_binding(doc)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
            load_binding(self.root, TOY1)

    def test_forged_active_baseline_and_review_pins_are_rejected(self):
        doc = copy.deepcopy(self.toy1)
        basepath = doc['active_baseline']['path']
        baseline = yaml.safe_load((self.root / basepath).read_text())
        baseline['source_candidate_sha256'] = 'fake-but-self-consistent'
        doc['active_baseline'] = write_pinned(self.root, basepath, baseline)
        doc['active_baseline']['id'] = baseline['id']
        reviewpath = doc['baseline_review']['path']
        review = yaml.safe_load((self.root / reviewpath).read_text())
        review['candidate_sha256'] = 'fake-but-self-consistent'
        doc['baseline_review'] = write_pinned(self.root, reviewpath, review)
        self.write_binding(doc)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
            load_binding(self.root, TOY1)

    def test_rehashed_ledger_and_validator_cannot_replace_authority(self):
        for field in ('vo_ledger', 'ad_ledger'):
            with self.subTest(field=field):
                doc = copy.deepcopy(self.toy1)
                path = doc[field]['path']
                original = (ROOT / path).read_bytes()
                (self.root / path).write_bytes(original)
                value = yaml.safe_load(original)
                value['unreviewed_extra'] = 'invented'
                doc[field] = write_pinned(self.root, path, value)
                self.write_binding(doc)
                with self.assertRaisesRegex(ValueError, 'Untrusted project authority source'):
                    load_binding(self.root, TOY1)
                (self.root / path).write_bytes(original)

    def test_untrusted_second_project_cannot_promote_forged_review(self):
        path = self.make_root_solver()
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)
        # A fabricated candidate may look self-consistent but still has
        # no reviewed authority root in this engine.
        binding = yaml.safe_load((self.root / path).read_text())
        fake_review = self.root / binding['baseline_review']['path']
        forged = yaml.safe_load(fake_review.read_text())
        forged['disposition'] = 'ACCEPT'
        binding['baseline_review'] = write_pinned(
            self.root, binding['baseline_review']['path'], forged)
        write_pinned(self.root, path, binding)
        with self.assertRaisesRegex(ValueError, 'Untrusted project authority root'):
            load_binding(self.root, path)

    def test_generic_code_has_no_toy1_constants(self):
        code = (ROOT / 'tools/gates/common.py').read_text()
        for token in ('C-002', 'AS-001', '2048', 'F-001',
                      'detector_attributable_shared_allocations'):
            self.assertNotIn(token, code)


if __name__ == '__main__':
    unittest.main()
