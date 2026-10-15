# FR-002 accepted-baseline continuity replacement: authoring report

**Status:** Bounded source candidate authored, NOT LOCALLY TESTED and NOT INDEPENDENTLY REVIEWED.  
**Authorization:** `process/decisions/FR002_BASELINE_CONTINUITY_REPLACEMENT-AUTHORIZATION-001.yaml`.  
**Prior independent review:** FR-002 `REVISE`, preserved; the preceding hostile-forgery-oriented R1 branch remains historical and not accepted.

## Design embodied by this candidate

- `tools/gates/continuity.py`: generic comparison of an explicitly declared project baseline projection and a new candidate binding, requiring exact obligation continuity or a separately documented accepted transition.
- `tools/gates/binding.py`: no call to the engine-owned `trusted_root(project_id)`. Loads a pinned project-owned projection and separate source references, validates current baseline review and active ledger correspondence, invokes reviewed project validators through an explicit registration map, and checks independent transition receipts. No YAML-driven dynamic Python loading.
- `process/project_authority/AS-001-AP-continuity-candidate-v1.yaml`: a new **candidate projection**, derived from existing accepted Toy 1 sources and their unchanged Git blobs; this projection is NOT itself accepted.
- `process/gate_configs/AS-001-AP-continuity-candidate-v2.yaml`: new explicit binding pointing to the projection and the unchanged accepted authority inputs.
- `tests/test_gate_adapter.py`: re-expresses the cooperative assumption with Toy 1 validation, omitted C-002 controls, source mismatch rejection, and a projection-not-approved control.
- `tests/test_baseline_continuity.py`: synthetic second-project continuity, reviewed-transition *shape* and explicit validator registry canaries.

The original explicit `AS-001-AP-v1.yaml` remains available as history but is not a valid new-style `--binding` input until a project-owned projection is named. The `--legacy-toy1` path is unchanged. This source revision is not a review decision, and synthetic tests never grant product authority.

## Precisely bounded limitations

A currently **candidate** Toy 1 projection may be inspected and used for simulations; `evaluate_bound` refuses to call such a projection genuine real-world eligibility. Its activation needs a separate reviewed projection and human approval record before `accepted_for_trial` is honored. The actual accepted Toy 1 baseline, independent AS review, policy, C-002 scope, active VO/AD and AP authority are not modified.

A transition may change only enumerated baseline fields, must carry an explicit separate accepted decision and independent review receipt, and must match the previously selected projection. An eligible AP remains a provisional gate result, not approval, proof, final F-001 comparison, or VO discharge.

`binding.REGISTRY` retains the existing Toy 1 validator and an explicit `register_validator` hook for additional reviewed project modules. A future project's entrypoint must deliberately register its own validator; the generic YAML loader neither imports arbitrary candidate code nor possesses an engine-wide project authorization list.

## Next evidence and review

Human operator pulls the source commit, runs new and historic targeted regressions and both explicit stage-gate inspection commands, and pushes a new `FR002_BASELINE_CONTINUITY-local-test-receipt.json` only if they pass. The assistant must inspect remote evidence before authoring a new **independent cooperative-continuity review**. Do not invoke the previously paused adversarial FR-002 R1 review.

Unexecuted source candidate, no cleanroom, framework freeze, product qualification, AD change, target selection or discharged VO.
