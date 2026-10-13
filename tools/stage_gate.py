#!/usr/bin/env python3
"""Deterministic completeness checks for staged architecture decisions.

Does NOT establish physical validity, mathematical proof, or engineering approval.
Use immutable independent review receipts to establish those properties.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULTS = {
    'policy': 'process/policies/AP_SELECTION_v2.yaml',
    'scope': 'process/decisions/C-002-scope.yaml',
    'vo': 'process/ledgers/vo_ledger.yaml',
    'ad': 'process/ledgers/ad_ledger.yaml',
}
STAGES = ['AS', 'AP', 'CON', 'DE', 'IMPLEMENTATION', 'TARGET_VALIDATION']
ACCEPTABLE = {'SATISFIED', 'CONDITIONALLY_SATISFIED', 'DEFERRED'}
DEFERRAL_FIELDS = ['owner', 'method', 'due_stage', 'acceptance', 'assumptions', 'escalation']
MEMORY_CATEGORIES = [
    'persistent_state', 'temporary_or_scratch', 'detector_stack',
    'detector_attributable_interrupt_context', 'detector_attributable_shared_allocations',
    'detector_attributable_dynamic_allocations', 'other_detector_attributable',
]


def check_memory_envelope(item, scope):
    """Validate the AP-stage resource *allocation*, never physical utilization."""
    errs = []
    env = item.get('memory_envelope')
    if not isinstance(env, dict):
        return ['C-002: credible AP-stage memory_envelope is missing']
    if env.get('boundary') != scope.get('chosen'):
        errs.append('C-002: envelope accounting boundary differs from approved scope')
    limit = scope.get('accounting', {}).get('limit_bytes', 2048)
    if env.get('limit_bytes') != limit:
        errs.append('C-002: envelope limit differs from authorized 2048 bytes')
    if env.get('aggregation') != 'nonoverlapping_peak':
        errs.append('C-002: specify nonoverlapping_peak accounting')
    for key in ('nonoverlap_reasoning', 'budget_enforcement', 'evidence_refs'):
        if not nonempty(env.get(key)):
            errs.append(f'C-002: envelope lacks {key}')
    if env.get('unknown_unbounded_contributors'):
        errs.append('C-002: unbounded charged contributors remain')
    buckets = env.get('buckets')
    if not isinstance(buckets, dict):
        return errs + ['C-002: envelope has no categorized budget']
    if set(buckets) != set(MEMORY_CATEGORIES):
        errs.append('C-002: envelope must enumerate every approved charged category')
    total = 0
    for name in MEMORY_CATEGORIES:
        bucket = buckets.get(name)
        if not isinstance(bucket, dict):
            continue
        count = bucket.get('max_bytes')
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            errs.append(f'C-002: {name} maximum must be a nonnegative integer')
        else:
            total += count
        if not nonempty(bucket.get('basis')):
            errs.append(f'C-002: {name} missing budget basis, including zero-attribution rationale')
    margin = env.get('reserved_margin_bytes')
    if isinstance(margin, bool) or not isinstance(margin, int) or margin <= 0:
        errs.append('C-002: strictly positive reserved margin required')
    elif total + margin > limit:
        errs.append(f'C-002: charged budget {total} + margin {margin} exceeds {limit}')
    return errs



def read_doc(path):
    data = yaml.safe_load(Path(path).read_text(encoding='utf-8'))
    if not isinstance(data, dict):
        raise ValueError(f'Expected YAML mapping: {path}')
    return data


def nonempty(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0 and all(nonempty(x) for x in value)
    return value is not None and value is not False


def inspect_state(policy, scope, vo, ad):
    return {
        'policy': {'id': policy.get('id'), 'status': policy.get('status')},
        'scope': {'id': scope.get('id'), 'status': scope.get('status'), 'chosen': scope.get('chosen')},
        'vos': [{k: x.get(k) for k in ('id', 'requirement', 'state', 'due_stage')}
                for x in vo.get('obligations', [])],
        'debts': [{k: x.get(k) for k in ('id', 'state', 'due_stage')}
                  for x in ad.get('items', [])],
    }


def evaluate(assessment, policy, scope, vo_ledger, ad_ledger):
    """Check eligibility of a PROVISIONAL_COMMITMENT, not final acceptance.

    This procedure is intentionally strict about evidence receipts and permissions.
    It cannot determine whether cited evidence is actually true.
    """
    errors = []
    note = []
    simulated = assessment.get('simulation_only') is True
    if policy.get('status') != 'approved_for_trial' or policy.get('selection_kind') != 'PROVISIONAL_COMMITMENT':
        errors.append('AP-stage policy not authorized for trial')
    if assessment.get('policy_id') != policy.get('id'):
        errors.append('Assessment policy identifier mismatch')
    if assessment.get('stage') != 'AP' or assessment.get('schema') != 'pc-ap-assessment/v2':
        errors.append('Invalid gate stage or assessment schema')
    if not nonempty(assessment.get('candidate')):
        errors.append('Candidate not identified')
    if assessment.get('scope_id') != scope.get('id'):
        errors.append('C-002 scope-decision identifier mismatch')
    choices = [option.get('id') for option in scope.get('options', [])]
    if not (scope.get('status') == 'approved' and scope.get('chosen') in choices
            and nonempty(scope.get('approved_by')) and nonempty(scope.get('approval_evidence'))):
        errors.append('C-002 scope requires independent explicit authority')
    else:
        note.append('C-002 has an identified approved accounting boundary')
        if not simulated:
            approval_path = ROOT / str(scope.get('approval_evidence'))
            if not approval_path.is_file():
                errors.append('C-002 approved scope missing authority evidence file')

    ledger = {entry['requirement']: entry for entry in vo_ledger.get('obligations', [])
              if isinstance(entry, dict) and entry.get('requirement')}
    debts = {entry['id']: entry for entry in ad_ledger.get('items', [])
             if isinstance(entry, dict) and entry.get('id')}
    reqs = assessment.get('requirements', {})
    if not isinstance(reqs, dict):
        errors.append('Requirements assessment must be a mapping')
        reqs = {}
    expected = policy.get('requirements', [])
    if set(reqs) != set(expected):
        errors.append(f'Requirements mismatch: missing={sorted(set(expected)-set(reqs))}, extra={sorted(set(reqs)-set(expected))}')

    for req in expected:
        item = reqs.get(req)
        if not isinstance(item, dict):
            errors.append(f'{req}: missing assessment')
            continue
        status = item.get('stage_status')
        if status not in ACCEPTABLE:
            errors.append(f'{req}: AP-stage evidence is {status!r} (not admissible)')
            continue
        if not nonempty(item.get('evidence')) and status != 'DEFERRED':
            errors.append(f'{req}: missing AP-stage evidence references')
        if req == 'C-002' and status in ('SATISFIED', 'CONDITIONALLY_SATISFIED'):
            errors.extend(check_memory_envelope(item, scope))
        if status == 'CONDITIONALLY_SATISFIED' and not nonempty(item.get('assumptions')):
            errors.append(f'{req}: conditional evidence missing assumptions')
        if status == 'DEFERRED' and req in policy.get('ap_due_requirements', expected):
            errors.append(f'{req}: cannot defer an AP-due assessment')
        binding = ledger.get(req)
        if binding is None:
            errors.append(f'{req}: missing authoritative VO ledger entry')
            continue
        if item.get('vo') != binding.get('id'):
            errors.append(f'{req}: does not carry expected {binding.get("id")}')
        final_status = item.get('final_status', 'OPEN')
        if final_status == 'DISCHARGED':
            if binding.get('state') != 'discharged' or not nonempty(binding.get('evidence_receipt')):
                errors.append(f'{req}: cannot claim final discharge without accepted VO receipt')
        elif final_status == 'OPEN':
            if binding.get('state') == 'discharged':
                errors.append(f'{req}: final_status contradicts discharged ledger')
            plan = item.get('deferral')
            if not isinstance(plan, dict):
                errors.append(f'{req}: open VO requires complete forward plan')
                continue
            for field in DEFERRAL_FIELDS:
                if not nonempty(plan.get(field)):
                    errors.append(f'{req}: deferral lacks {field}')
            due = plan.get('due_stage')
            if due not in STAGES:
                errors.append(f'{req}: unknown due stage {due}')
            elif STAGES.index(due) <= STAGES.index('AP'):
                errors.append(f'{req}: binding VO was due at or before AP; cannot defer it')
            if due != binding.get('due_stage'):
                errors.append(f'{req}: deferral due stage differs from authoritative ledger')
        else:
            errors.append(f'{req}: invalid final status {final_status}')

    comparative = assessment.get('comparative_decision', {})
    if not isinstance(comparative, dict):
        comparative = {}
    mode = comparative.get('mode')
    if mode == 'supported_projection':
        if not nonempty(comparative.get('evidence')):
            errors.append('Projection ranking requires actual cited comparative evidence')
        note.append('Comparative projection is not the final F-001 Pareto ranking')
    elif mode == 'authorized_tradeoff':
        if not nonempty(comparative.get('authority')) or not nonempty(comparative.get('rationale')):
            errors.append('Provisional tradeoff requires explicit authority and rationale')
        debt_id = comparative.get('architectural_debt')
        debt = debts.get(debt_id)
        if not debt or debt.get('state') != 'accepted' or not all(nonempty(debt.get(k)) for k in ('accepted_by','accepted_decision','owner','due_stage','fallback')):
            errors.append('Unknown F tradeoff requires independently accepted Architectural Debt')
        else:
            note.append(f'Accepted risk linked: {debt_id}')
    else:
        errors.append('Cannot commit an AP without projected comparison or authorized tradeoff')

    for debt in ad_ledger.get('items', []):
        if debt.get('state') == 'blocking' and debt.get('due_stage') in ('AS', 'AP'):
            errors.append(f'Architectural blocker remains open: {debt.get("id")}')

    return {
        'gate': 'AP_PROVISIONAL_SELECTION',
        'candidate': assessment.get('candidate'),
        'decision': 'PASS_SIMULATION' if simulated and not errors else ('ELIGIBLE_FOR_INDEPENDENT_REVIEW' if not errors else 'NO_DOWNSELECTION'),
        'errors': list(dict.fromkeys(errors)),
        'notes': note,
        'simulation_only': simulated,
        'reminder': 'A successful policy check is not proof, final F-001 ranking, or an approved architectural selection.',
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inspect','evaluate'))
    parser.add_argument('--assessment')
    for k, v in DEFAULTS.items():
        parser.add_argument(f'--{k}', default=v)
    args = parser.parse_args(argv)
    try:
        inputs = {k: read_doc(ROOT / getattr(args, k)) for k in DEFAULTS}
        if args.command == 'inspect':
            print(json.dumps(inspect_state(inputs['policy'], inputs['scope'], inputs['vo'], inputs['ad']), indent=2))
            return 0
        if not args.assessment:
            parser.error('evaluate requires --assessment')
        result = evaluate(read_doc(ROOT / args.assessment), inputs['policy'], inputs['scope'], inputs['vo'], inputs['ad'])
        print(json.dumps(result, indent=2))
        return 0 if result['decision'] in ('ELIGIBLE_FOR_INDEPENDENT_REVIEW', 'PASS_SIMULATION') else 2
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
