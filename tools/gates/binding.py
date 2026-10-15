"""Project binding loader for generic AP checks, with pinned authority sources.

Binding data is a candidate review input, never a product authority.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
import yaml

from gates import toy1_c002
from gates.authority_roots import trusted_root

REGISTRY = {toy1_c002.VALIDATOR_ID: toy1_c002}
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


def load_binding(root: Path, ref: str):
    """Read only explicitly named pinned project evidence and validators."""
    root = root.resolve()
    binding = yaml.safe_load(safe_file(root, ref).read_text(encoding='utf-8'))
    if not isinstance(binding, dict) or binding.get('schema') != 'pc-ap-gate-binding/v1':
        raise ValueError('Unrecognized gate project binding')
    if binding.get('status') != 'candidate_for_independent_review':
        raise ValueError('Gate binding is not a declared review candidate')
    project = binding.get('project_id')
    # Trust is rooted in reviewed engine code, not a candidate binding.
    anchor = trusted_root(project)
    spine = binding.get('spine')
    if spine != anchor['spine'] or binding.get('stage') != anchor['stage']:
        raise ValueError('Project spine/stage differs from trusted authority root')
    for key, accepted in anchor['sources'].items():
        if key in ('approved_ap_authority', 'reviewed_as'):
            continue
        spec = binding.get(key)
        if (not isinstance(spec, dict) or
                spec.get('path') != accepted['path'] or
                spec.get('git_blob_sha1') != accepted['git_blob_sha1']):
            raise ValueError('Untrusted project authority source: ' + key)
    trusted_validator = anchor['accepted_validator']
    specs = binding.get('required_validators')
    if not isinstance(specs, list) or len(specs) != 1:
        raise ValueError('Untrusted protected domain validator set')
    declared_validator = specs[0]
    if (not isinstance(declared_validator, dict) or
            declared_validator.get('id') != trusted_validator['id'] or
            declared_validator.get('requirement') != trusted_validator['requirement'] or
            declared_validator.get('scope') != trusted_validator['scope'] or
            declared_validator.get('implementation') != trusted_validator['implementation']):
        raise ValueError('Untrusted protected domain validator authority')
    if (not isinstance(project, str) or not project or
            spine != '/architecture/' + project + '/spine.md' or
            binding.get('stage') != 'AP'):
        raise ValueError('Missing or mismatched project, spine or gate stage')
    expected_spine = 'knowledge' + spine
    if binding.get('spine_source', {}).get('path') != expected_spine:
        raise ValueError('Spine authority belongs to another project')
    pinned(root, binding['spine_source'], yaml_input=False)
    baseline = pinned(root, binding['active_baseline'])
    # These accepted provenance files are discovered only through the engine
    # trust root. Binding metadata cannot replace or re-pin them.
    authority = pinned(root, anchor['sources']['approved_ap_authority'])
    as_review = pinned(root, anchor['sources']['reviewed_as'])
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
    if (baseline.get('independent_as_review') != anchor['sources']['reviewed_as']['path'] or
            authority.get('schema') != 'pc-ap-authority/v1' or
            authority.get('status') != 'approved' or
            authority.get('decision') != 'PROVISIONALLY_SELECTED' or
            authority.get('architecture') != project + '-v2' or
            authority.get('basis', {}).get('independent_review') != anchor['sources']['reviewed_as']['path'] or
            authority.get('basis', {}).get('memory_scope') != trusted_validator['scope']['path'] or
            'C-002_2048_bytes_detector_attributable_sram' not in authority.get('protected_requirements', []) or
            as_review.get('schema') != 'pc-as-review/v1' or
            as_review.get('disposition') not in ('ACCEPT', 'ACCEPT_WITH_CLARIFICATIONS') or
            baseline.get('accepted_authority', {}).get('provisional_ap') != anchor['sources']['approved_ap_authority']['path'] or
            vo.get('activation', {}).get('authority') != anchor['sources']['approved_ap_authority']['path']):
        raise ValueError('Active baseline lacks independently anchored AP authority')
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
    if (policy.get('protected_scope_decisions') != anchor['protected_requirements'] or
            policy.get('approved_scope_refs', {}).get(trusted_validator['requirement']) !=
            'C-002-SCOPE-001'):
        raise ValueError('AP policy conflicts with protected trusted authority root')
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
        if (item['implementation']['path'] != 'tools/gates/toy1_c002.py' or
                scope.get('requirement') != item['requirement'] or
                scope.get('id') != policy.get('approved_scope_refs', {}).get(item['requirement']) or
                baseline.get('accepted_authority', {}).get('memory_scope') != item['scope']['path']):
            raise ValueError('Validator scope or accepted authority mismatch')
        active.append({'requirement': item['requirement'], 'scope': scope,
                       'id': key, 'module': plugin})
    return binding, policy, vo, ad, active


def evaluate_bound(root: Path, binding_path: str, assessment: dict):
    from gates.common import evaluate
    binding, policy, vo, ad, validators = load_binding(root, binding_path)
    if not isinstance(assessment, dict):
        raise ValueError('Assessment must be a mapping')
    return evaluate(assessment, policy, vo, ad, validators,
                    project_id=binding['project_id'], spine=binding['spine'],
                    root=root.resolve())
