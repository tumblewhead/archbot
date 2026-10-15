"""Toy 1 C-002 domain validator. Not a universal stage-gate requirement.

Preserves the original charged-SRAM category/margin and scope checks.
"""
from pathlib import Path
from gates.common import nonempty

VALIDATOR_ID = "TOY1_C002_CHARGED_SRAM"
PROJECT_ID = "AS-001"
REQUIREMENT = "C-002"

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

def validate_scope(assessment, scope, root, *, simulated=False):
    errors = []
    note = []
    if assessment.get('scope_id') != scope.get('id'):
        errors.append('C-002 scope-decision identifier mismatch')
    choices = [option.get('id') for option in scope.get('options', [])]
    if not (scope.get('status') == 'approved' and scope.get('chosen') in choices
            and nonempty(scope.get('approved_by')) and nonempty(scope.get('approval_evidence'))):
        errors.append('C-002 scope requires independent explicit authority')
    else:
        note.append('C-002 has an identified approved accounting boundary')
        if not simulated:
            approval_path = root / str(scope.get('approval_evidence'))
            if not approval_path.is_file():
                errors.append('C-002 approved scope missing authority evidence file')

    return errors, note

def validate_requirement(item, scope):
    return check_memory_envelope(item, scope)
