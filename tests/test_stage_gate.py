"""Policy checks are not engineering approvals or proof validators."""
import copy
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import stage_gate


class StageGateTests(unittest.TestCase):
    def setUp(self):
        self.policy = stage_gate.read_doc(ROOT/'process/policies/AP_SELECTION_v2.yaml')
        self.scope = stage_gate.read_doc(ROOT/'process/decisions/C-002-scope.yaml')
        self.vo = stage_gate.read_doc(ROOT/'process/ledgers/vo_ledger.yaml')
        self.ad = stage_gate.read_doc(ROOT/'process/ledgers/ad_ledger.yaml')
        self.scope.update(status='approved', chosen='detector_owned_state',
                          approved_by='SIMULATED STAKEHOLDER', approval_evidence='SIMULATED DECISION')
        # Simulate an accepted AS-stage receipt. This is NEVER written to repo.
        self.vo['obligations'][0]['state'] = 'discharged'
        self.vo['obligations'][0]['evidence_receipt'] = 'SIMULATED-AS-REVIEW'
        self.ad['items'][0]['state'] = 'resolved'
        self.ad['items'][1].update(state='accepted', accepted_by='SIMULATED STAKEHOLDER',
                                    accepted_decision='SIMULATED-TRADEOFF')
        self.assessment = {
            'schema':'pc-ap-assessment/v2', 'candidate':'AP-002', 'stage':'AP',
            'simulation_only': True,
            'policy_id':'AP-SELECT-002', 'scope_id':'C-002-SCOPE-001',
            'comparative_decision':{'mode':'authorized_tradeoff',
                                     'authority':'SIMULATED STAKEHOLDER',
                                     'rationale':'SIMULATED EXPLICIT COMPROMISE',
                                     'architectural_debt':'AD-002'},
            'requirements': {},
        }
        for req in self.policy['requirements']:
            binding = next(v for v in self.vo['obligations'] if v['requirement']==req)
            item = {'stage_status':'CONDITIONALLY_SATISFIED',
                    'evidence':['SIMULATED AP STAGE EVIDENCE'],
                    'assumptions':['SIMULATED DOMAIN'], 'vo':binding['id'],
                    'final_status':'OPEN',
                    'deferral':{'owner':binding['owner'], 'method':'SIMULATED VERIFICATION',
                                'due_stage':binding['due_stage'], 'acceptance':'SIMULATED PASS CONDITION',
                                'assumptions':['SIMULATED DOMAIN'],
                                'escalation':'SIMULATED REOPEN AP'}}
            if req == 'C-001':
                item.update(final_status='DISCHARGED')
                item.pop('deferral')
            if req == 'C-002':
                item['memory_envelope'] = {
                    'boundary': 'detector_owned_state', 'limit_bytes': 2048,
                    'aggregation': 'nonoverlapping_peak',
                    'nonoverlap_reasoning': 'SIMULATED nonoverlap statement',
                    'budget_enforcement': 'SIMULATED downstream CON budget',
                    'evidence_refs': ['SIMULATED architectural evidence'],
                    'unknown_unbounded_contributors': [],
                    'buckets': {k: {'max_bytes': (64 if k == 'persistent_state' else 0),
                                     'basis': 'SIMULATED known charge'}
                                for k in stage_gate.MEMORY_CATEGORIES},
                    'reserved_margin_bytes': 1984,
                }
            self.assessment['requirements'][req] = item

    def judge(self):
        return stage_gate.evaluate(self.assessment, self.policy, self.scope, self.vo, self.ad)

    def test_legitimate_future_verification_allows_provisional_review(self):
        res = self.judge()
        self.assertEqual(res['decision'], 'PASS_SIMULATION', res['errors'])
        self.assertIn('not proof', res['reminder'])

    def test_scope_authority_cannot_be_assumed(self):
        self.scope['status']='pending_authority'
        res=self.judge()
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')
        self.assertIn('C-002 scope requires independent explicit authority', res['errors'])

    def test_unjustified_deferral_is_rejected(self):
        item=self.assessment['requirements']['R-001']
        item['stage_status']='DEFERRED'
        item['ap_assessment_due']=False  # An agent cannot override the governing policy.
        item.pop('evidence')
        item['deferral'].pop('owner')
        res=self.judge()
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')
        self.assertTrue(any('AP-due' in x for x in res['errors']))
        self.assertTrue(any('lacks owner' in x for x in res['errors']))

    def test_known_violation_blocks(self):
        self.assessment['requirements']['C-002']['stage_status'] = 'VIOLATED'
        res=self.judge()
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')
        self.assertTrue(any('C-002: AP-stage evidence' in x for x in res['errors']))

    def test_unaccepted_debt_blocks_tradeoff(self):
        self.ad['items'][1]['state']='proposed'
        res=self.judge()
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')
        self.assertTrue(any('independently accepted Architectural Debt' in x for x in res['errors']))

    def test_cannot_claim_final_discharge_from_prose(self):
        self.assessment['requirements']['R-003']['final_status']='DISCHARGED'
        res=self.judge()
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')
        self.assertTrue(any('without accepted VO receipt' in x for x in res['errors']))

    def test_default_policy_scope_unapproved(self):
        original = stage_gate.read_doc(ROOT/'process/decisions/C-002-scope.yaml')
        original['status'] = 'pending_authority'  # negative test independent of project state
        original['chosen'] = None
        res = stage_gate.evaluate(self.assessment, self.policy, original, self.vo, self.ad)
        self.assertEqual(res['decision'], 'NO_DOWNSELECTION')


    def test_no_firmware_required_for_ap_resource_envelope(self):
        result = self.judge()
        self.assertEqual(result['decision'], 'PASS_SIMULATION', result['errors'])

    def test_unbounded_memory_category_blocks_ap(self):
        env = self.assessment['requirements']['C-002']['memory_envelope']
        env['unknown_unbounded_contributors'] = ['detector IRQ stack']
        self.assertTrue(any('unbounded' in e for e in self.judge()['errors']))

    def test_missing_margin_blocks_ap(self):
        self.assessment['requirements']['C-002']['memory_envelope']['reserved_margin_bytes'] = 0
        self.assertTrue(any('margin' in e for e in self.judge()['errors']))

    def test_budget_overflow_blocks_ap(self):
        env = self.assessment['requirements']['C-002']['memory_envelope']
        env['buckets']['detector_stack']['max_bytes'] = 2048
        self.assertTrue(any('exceeds' in e for e in self.judge()['errors']))

    def test_real_gate_requires_authority_evidence_file(self):
        self.assessment['simulation_only'] = False
        self.scope['chosen'] = 'detector_charged_sram'
        self.scope['approval_evidence'] = 'nonexistent/authority.txt'
        self.assessment['requirements']['C-002']['memory_envelope']['boundary'] = 'detector_charged_sram'
        outcome = self.judge()
        self.assertIn('C-002 approved scope missing authority evidence file', outcome['errors'])

    def test_missing_category_blocks_ap(self):
        env = self.assessment['requirements']['C-002']['memory_envelope']
        del env['buckets']['detector_attributable_shared_allocations']
        self.assertTrue(any('enumerate' in e for e in self.judge()['errors']))


if __name__=='__main__': unittest.main()
