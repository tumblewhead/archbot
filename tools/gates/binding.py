"""Project binding loader for generic AP checks, with pinned authority sources.

Binding data is a candidate review input, never a product authority.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
import yaml

from gates import toy1_c002

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
    spine = binding.get('spine')
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
