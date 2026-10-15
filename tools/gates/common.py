"""Reusable AP gate mechanics. Deterministic eligibility, never product approval."""
from __future__ import annotations

STAGES = ['AS', 'AP', 'CON', 'DE', 'IMPLEMENTATION', 'TARGET_VALIDATION']
ACCEPTABLE = {'SATISFIED', 'CONDITIONALLY_SATISFIED', 'DEFERRED'}
DEFERRAL_FIELDS = ['owner', 'method', 'due_stage', 'acceptance', 'assumptions', 'escalation']


def nonempty(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0 and all(nonempty(x) for x in value)
    return value is not None and value is not False


def inspect_state(policy, scopes, vo, ad):
    return {
        'policy': {'id': policy.get('id'), 'status': policy.get('status')},
        'scopes': {x['requirement']: {'id': x['scope'].get('id'),
                  'status': x['scope'].get('status')} for x in scopes},
        'vos': [{k: row.get(k) for k in ('id', 'requirement', 'state', 'due_stage')}
                for row in vo.get('obligations', [])],
        'debts': [{k: row.get(k) for k in ('id', 'state', 'due_stage')}
                  for row in ad.get('items', [])],
    }


def evaluate(assessment, policy, vo_ledger, ad_ledger, validators=(), *,
             project_id=None, spine=None, root=None):
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
    if project_id is not None:
        if not project_id or not spine or assessment.get('project_id') != project_id or assessment.get('spine') != spine:
            errors.append('Assessment project identity or spine mismatch')
    required = policy.get('protected_scope_decisions', [])
    implemented = [item['requirement'] for item in validators]
    if (not isinstance(required, list) or not all(isinstance(k, str) for k in required)
            or len(set(required)) != len(required) or
            set(required) != set(implemented) or len(implemented) != len(set(implemented))):
        errors.append('Missing, duplicate or unexpected protected domain validator')
    for item in validators:
        plugin = item['module']
        scope = item['scope']
        errs, notes = plugin.validate_scope(assessment, scope, root, simulated=simulated)
        errors.extend(errs)
        note.extend(notes)

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
        if status in ('SATISFIED', 'CONDITIONALLY_SATISFIED'):
            for domain in validators:
                if domain['requirement'] == req:
                    errors.extend(domain['module'].validate_requirement(item, domain['scope']))
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
        note.append('Comparative projection is not the final ' +
                    str(policy.get('original_f', 'declared F')) + ' Pareto ranking')
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
        'reminder': 'A successful policy check is not proof, final ' + str(policy.get('original_f', 'F')) + ' ranking, or an approved architectural selection.',
    }
