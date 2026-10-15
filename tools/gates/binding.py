"""Cooperative project-owned AP baseline binding and continuity checks.

A project projection is a separate input; hashes identify source bytes, not approval.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
import yaml

from gates import toy1_c002
from gates import continuity

REGISTRY = {toy1_c002.VALIDATOR_ID: toy1_c002}


def register_validator(plugin):
    """Register an explicitly supplied reviewed project validator.

    The program entrypoint selects the module; YAML does not import code.
    This is a cooperative extension hook, not an executable-plugin sandbox.
    """
    key = getattr(plugin, 'VALIDATOR_ID', None)
    if (not isinstance(key, str) or not key or
            not isinstance(getattr(plugin, 'PROJECT_ID', None), str) or
            not isinstance(getattr(plugin, 'REQUIREMENT', None), str) or
            not callable(getattr(plugin, 'validate_scope', None)) or
            not callable(getattr(plugin, 'validate_requirement', None))):
        raise ValueError('Invalid registered domain validator')
    if key in REGISTRY and REGISTRY[key] is not plugin:
        raise ValueError('Validator identity already registered')
    REGISTRY[key] = plugin


SHA1_RE = re.compile(r"^[0-9a-f]{40}$")


def safe_file(root: Path, ref: str) -> Path:
    root = root.resolve()
    if not isinstance(ref, str) or not ref or ref.startswith('/') or '\\' in ref:
        raise ValueError('Unsafe project input path')
    parts = Path(ref).parts
    if any(x in ('..', '.') for x in parts):
        raise ValueError('Project input escapes repository')
    path = root.joinpath(*parts)
    if path.resolve() != path or not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Missing or aliased project input: ' + ref)
    return path


def blob_id(raw: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def pinned(root: Path, spec: dict, *, yaml_input=True):
    if not isinstance(spec, dict) or not SHA1_RE.fullmatch(str(spec.get('git_blob_sha1', ''))):
        raise ValueError('Missing pinned Git blob identity')
    path = safe_file(root, spec.get('path'))
    data = path.read_bytes()
    if blob_id(data) != spec['git_blob_sha1']:
        raise ValueError('Stale project authority or source pin: ' + spec['path'])
    if not yaml_input:
        return data
    obj = yaml.safe_load(data.decode('utf-8'))
    if not isinstance(obj, dict):
        raise ValueError('Pinned YAML document must be a mapping')
    return obj




def _transition(root, binding, projection):
    ref = binding.get('transition')
    if ref is None:
        return None
    record = pinned(root, ref)
    review_spec = record.get('review')
    if not isinstance(review_spec, dict):
        raise ValueError('Authority transition missing review')
    review = pinned(root, review_spec)
    if (review.get('schema') != 'pc-project-transition-review/v1' or
            review.get('independent_of_transition_authoring_invocation') is not True or
            review.get('disposition') not in ('ACCEPT', 'ACCEPT_WITH_CLARIFICATIONS') or
            review.get('transition') != ref['path'] or
            review.get('previous_projection_id') != projection.get('id') or
            record.get('review_path') != review_spec['path']):
        raise ValueError('Authority transition lacks matching independent review')
    return record

def load_binding(root: Path, ref: str):
    """Read only explicitly named pinned project evidence and validators."""
    root = root.resolve()
    binding = yaml.safe_load(safe_file(root, ref).read_text(encoding='utf-8'))
    if not isinstance(binding, dict) or binding.get('schema') != 'pc-ap-gate-binding/v1':
        raise ValueError('Unrecognized gate project binding')
    if binding.get('status') != 'candidate_for_independent_review':
        raise ValueError('Gate binding is not a declared review candidate')
    if not isinstance(binding.get('accepted_projection'), dict):
        raise ValueError('Explicit accepted project projection required')
    projection = pinned(root, binding['accepted_projection'])
    transition = _transition(root, binding, projection)
    continuity.compare(projection, binding, transition)
    # Real (non-simulation) eligibility requires a separately reviewed and
    # human-approved project projection. Candidate projections remain usable
    # for inspection and simulation, never as accepted authority.
    if projection['status'] == 'accepted_for_trial':
        review_spec = projection.get('activation_review')
        decision_spec = projection.get('activation_decision')
        if not isinstance(review_spec, dict) or not isinstance(decision_spec, dict):
            raise ValueError('Accepted projection lacks review and approval')
        accepted_review = pinned(root, review_spec)
        approved = pinned(root, decision_spec)
        if (accepted_review.get('schema') != 'pc-project-projection-review/v1' or
                accepted_review.get('independent_of_projection_authoring_invocation') is not True or
                accepted_review.get('disposition') not in ('ACCEPT', 'ACCEPT_WITH_CLARIFICATIONS') or
                accepted_review.get('projection_id') != projection['id'] or
                accepted_review.get('project_id') != projection['project_id'] or
                approved.get('schema') != 'pc-project-projection-approval/v1' or
                approved.get('decision') != 'APPROVE_FOR_TRIAL' or
                approved.get('project_id') != projection['project_id'] or
                approved.get('projection_id') != projection['id'] or
                approved.get('review_path') != review_spec['path'] or
                not approved.get('approved_by')):
            raise ValueError('Accepted projection lacks matching independent authority')
    project = binding['project_id']
    spine = binding['spine']
    if (not isinstance(project, str) or not project or
            spine != '/architecture/' + project + '/spine.md' or
            binding.get('stage') != 'AP'):
        raise ValueError('Missing or mismatched project, spine or gate stage')
    expected_spine = 'knowledge' + spine
    if binding.get('spine_source', {}).get('path') != expected_spine:
        raise ValueError('Spine authority belongs to another project')
    pinned(root, binding['spine_source'], yaml_input=False)
    baseline = pinned(root, binding['active_baseline'])
    review = pinned(root, binding['baseline_review'])
    policy = pinned(root, binding['policy'])
    vo = pinned(root, binding['vo_ledger'])
    ad = pinned(root, binding['ad_ledger'])
    if baseline.get('schema') != 'pc-active-baseline/v1' or baseline.get('status') != 'active':
        raise ValueError('Project baseline is not active')
    if (baseline.get('independent_baseline_review') != binding['baseline_review']['path'] or
            review.get('schema') != 'pc-baseline-review/v1' or
            review.get('independent_of_baseline_authoring_invocation') is not True or
            review.get('disposition') not in ('ACCEPT', 'ACCEPT_WITH_CLARIFICATIONS') or
            review.get('candidate') != baseline.get('source_candidate') or
            review.get('candidate_sha256') != baseline.get('source_candidate_sha256') or
            vo.get('activation', {}).get('reviewed_baseline') != binding['baseline_review']['path']):
        raise ValueError('Baseline lacks matching independent review authority')
    if 'reviewed_as' in binding:
        reviewed = pinned(root, binding['reviewed_as'])
        if (baseline.get('independent_as_review') != binding['reviewed_as']['path'] or
                reviewed.get('disposition') not in ('ACCEPT', 'ACCEPT_WITH_CLARIFICATIONS')):
            raise ValueError('Baseline lacks matching AS review authority')
    if 'approved_ap_authority' in binding:
        authority = pinned(root, binding['approved_ap_authority'])
        if (authority.get('schema') != 'pc-ap-authority/v1' or
                authority.get('status') != 'approved' or
                authority.get('basis', {}).get('independent_review') !=
                binding.get('reviewed_as', {}).get('path') or
                baseline.get('accepted_authority', {}).get('provisional_ap') !=
                binding['approved_ap_authority']['path'] or
                vo.get('activation', {}).get('authority') != binding['approved_ap_authority']['path']):
            raise ValueError('Baseline lacks matching AP authority')
    if baseline.get('id') != binding['active_baseline'].get('id'):
        raise ValueError('Baseline id differs from pinned context')
    artifacts = baseline.get('active_artifacts', {})
    if (not str(artifacts.get('architecture_statement', '')).startswith(
            'knowledge/architecture/' + project + '/') or
            artifacts.get('vo_ledger') != binding['vo_ledger']['path']):
        raise ValueError('Baseline project or active VO ledger mismatch')
    if vo.get('activation', {}).get('active_baseline') != binding['active_baseline']['path']:
        raise ValueError('VO ledger does not belong to active baseline')
    if policy.get('id') != binding['policy'].get('id'):
        raise ValueError('Policy identity mismatch')
    if (policy.get('status') != 'approved_for_trial' or
            policy.get('selection_kind') != 'PROVISIONAL_COMMITMENT' or
            not isinstance(policy.get('requirements'), list) or
            not policy['requirements']):
        raise ValueError('Project AP policy is not eligible for trial')
    if (not isinstance(vo.get('obligations'), list) or
            not isinstance(ad.get('items'), list)):
        raise ValueError('Malformed authoritative project ledgers')
    specs = binding.get('required_validators')
    required = policy.get('protected_scope_decisions')
    if (not isinstance(required, list) or not isinstance(specs, list) or
            len(set(required)) != len(required) or
            len(specs) != len(required) or
            set(x.get('requirement') for x in specs if isinstance(x, dict)) != set(required)):
        raise ValueError('Missing or mismatched protected domain validators')
    active = []
    for item in specs:
        key = item.get('id')
        plugin = REGISTRY.get(key)
        if (plugin is None or plugin.PROJECT_ID != project or
                plugin.REQUIREMENT != item.get('requirement')):
            raise ValueError('Unknown or wrong-project domain validator')
        scope = pinned(root, item.get('scope'))
        pinned(root, item.get('implementation'), yaml_input=False)
        approved_scope_path = baseline.get('accepted_authority', {}).get('memory_scope')
        if (scope.get('requirement') != item['requirement'] or
                scope.get('id') != policy.get('approved_scope_refs', {}).get(item['requirement']) or
                (approved_scope_path is not None and
                 item['requirement'] in projection.get('protected_requirements', []) and
                 approved_scope_path != item['scope']['path'])):
            raise ValueError('Validator scope or accepted authority mismatch')
        active.append({'requirement': item['requirement'], 'scope': scope,
                       'id': key, 'module': plugin})
    binding['_projection_status'] = projection['status']
    return binding, policy, vo, ad, active


def evaluate_bound(root: Path, binding_path: str, assessment: dict):
    from gates.common import evaluate
    binding, policy, vo, ad, validators = load_binding(root, binding_path)
    if not isinstance(assessment, dict):
        raise ValueError('Assessment must be a mapping')
    result = evaluate(assessment, policy, vo, ad, validators,
                      project_id=binding['project_id'], spine=binding['spine'],
                      root=root.resolve())
    if binding['_projection_status'] != 'accepted_for_trial' and assessment.get('simulation_only') is not True:
        result['errors'].append('Project continuity projection is not independently accepted')
        result['decision'] = 'NO_DOWNSELECTION'
    return result
