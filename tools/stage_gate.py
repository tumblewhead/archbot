#!/usr/bin/env python3
"""Explicit project-bound AP gate, plus opt-in historical Toy 1 compatibility.

No implicit Toy 1 policy/ledger defaults in the generic CLI. Deterministic
eligibility is not an accepted review or a verification-obligation discharge.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import yaml

from gates import common, toy1_c002
from gates.binding import evaluate_bound, load_binding

ROOT = Path(__file__).resolve().parents[1]
# Historic Python callers explicitly import stage_gate.evaluate. Preserve their
# Toy 1 behavior; generic/new project callers MUST use evaluate_bound.
MEMORY_CATEGORIES = toy1_c002.MEMORY_CATEGORIES
check_memory_envelope = toy1_c002.check_memory_envelope
STAGES = common.STAGES
ACCEPTABLE = common.ACCEPTABLE
DEFERRAL_FIELDS = common.DEFERRAL_FIELDS
nonempty = common.nonempty


def read_doc(path):
    data = yaml.safe_load(Path(path).read_text(encoding='utf-8'))
    if not isinstance(data, dict):
        raise ValueError(f'Expected YAML mapping: {path}')
    return data


def inspect_state(policy, scope, vo, ad):
    # Explicit Toy 1 historical inspection entry only.
    return {
        'policy': {'id': policy.get('id'), 'status': policy.get('status')},
        'scope': {'id': scope.get('id'), 'status': scope.get('status'),
                  'chosen': scope.get('chosen')},
        'vos': [{k: x.get(k) for k in ('id', 'requirement', 'state', 'due_stage')}
                for x in vo.get('obligations', [])],
        'debts': [{k: x.get(k) for k in ('id', 'state', 'due_stage')}
                  for x in ad.get('items', [])],
    }


def evaluate(assessment, policy, scope, vo_ledger, ad_ledger):
    """Legacy Toy 1 Python API (explicit by caller), not a generic gate."""
    return common.evaluate(assessment, policy, vo_ledger, ad_ledger,
                           [{'id': toy1_c002.VALIDATOR_ID,
                             'requirement': toy1_c002.REQUIREMENT,
                             'scope': scope, 'module': toy1_c002}],
                           root=ROOT)


LEGACY_TOY1_DEFAULTS = {
    'policy': 'process/policies/AP_SELECTION_v2.yaml',
    'scope': 'process/decisions/C-002-scope.yaml',
    'vo': 'process/ledgers/vo_ledger.yaml',
    'ad': 'process/ledgers/ad_ledger.yaml',
}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inspect', 'evaluate'))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--binding', help='Explicit pinned project gate binding')
    mode.add_argument('--legacy-toy1', action='store_true',
                      help='Explicit historical Toy 1 compatibility mode')
    parser.add_argument('--assessment')
    for name in LEGACY_TOY1_DEFAULTS:
        parser.add_argument('--' + name)
    args = parser.parse_args(argv)
    try:
        if args.binding:
            if any(getattr(args, k) is not None for k in LEGACY_TOY1_DEFAULTS):
                raise ValueError('Project binding cannot use legacy Toy 1 file overrides')
            binding, policy, vo, ad, validators = load_binding(ROOT, args.binding)
            if args.command == 'inspect':
                print(json.dumps({
                    'project_id': binding['project_id'], 'spine': binding['spine'],
                    'active_baseline': binding['active_baseline']['path'],
                    **common.inspect_state(policy, validators, vo, ad),
                }, indent=2))
                return 0
            if not args.assessment:
                raise ValueError('evaluate requires --assessment')
            result = evaluate_bound(ROOT, args.binding, read_doc(ROOT / args.assessment))
        else:
            values = {k: read_doc(ROOT / (getattr(args, k) or v))
                      for k, v in LEGACY_TOY1_DEFAULTS.items()}
            if args.command == 'inspect':
                print(json.dumps(inspect_state(values['policy'], values['scope'],
                                               values['vo'], values['ad']), indent=2))
                return 0
            if not args.assessment:
                raise ValueError('evaluate requires --assessment')
            result = evaluate(read_doc(ROOT / args.assessment),
                              values['policy'], values['scope'],
                              values['vo'], values['ad'])
        print(json.dumps(result, indent=2))
        return 0 if result['decision'] in ('ELIGIBLE_FOR_INDEPENDENT_REVIEW',
                                            'PASS_SIMULATION') else 2
    except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
