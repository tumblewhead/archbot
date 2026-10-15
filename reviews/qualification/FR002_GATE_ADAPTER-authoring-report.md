# FR-002: generic stage gate with Toy 1 opt-in validator

**Status:** Authored source candidate, NOT LOCALLY TESTED and NOT INDEPENDENTLY REVIEWED.  
**Authority:** `process/decisions/FR-002-GATE-ADAPTER-AUTHORIZATION-001.yaml`.  
**Predecessor:** FR-001 R1 `ACCEPT_WITH_CLARIFICATIONS`, recorded in `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-receipt.json`.

## Separation implemented

- `tools/gates/common.py`: the shared AP provisional eligibility mechanics, requirement evidence maturity, due-stage checks, VO carry-forward, accepted AD tradeoff and policy-specific F note. No Toy 1 SRAM categories, C-002, AS-001 or F-001 defaults.
- `tools/gates/toy1_c002.py`: extracted C-002 scope authority and seven-category charged-SRAM envelope validation. Preserves the original check and message semantics.
- `tools/gates/binding.py`: explicit project binding with Git blob SHA-1 pins for the spine, active baseline, independently reviewed baseline receipt, stage policy, active VO/AD ledgers, validator implementation and scope. Rejects unregistered/wrong-project validators, missing required C-002 scope, altered policy or authority, and cross-project baseline/VO ledger links.
- `tools/stage_gate.py`: public Python `evaluate(...)` retains its explicit historical Toy 1 compatibility behavior. The CLI now requires either `--binding` for a project-scoped gate or `--legacy-toy1` to select historical defaults *explicitly*. No implicit C-002 defaults on the new generic path.
- `process/gate_configs/AS-001-AP-v1.yaml`: **candidate, not an accepted product policy**, binding the current reviewed Toy 1 authority bytes without altering them.
- `tests/test_gate_adapter.py`: new source/authority negative controls and a completely separate synthetic root-solver AP simulation. Original `tests/test_stage_gate.py` is unchanged, so its 13 existing Toy 1 positive and negative tests continue to act as regression requirements.

## Limitations and concrete next evidence

A fake project's simulation is *structural* evidence only. The generic gate does not prove mathematics, product feasibility, source correctness, acceptance of any AP, or VO discharge. The binding registry is an explicit code allowlist, not permission to load arbitrary Python validators. A distinct project requiring a different domain-specific check must have a reviewed validator and a new binding; absence of a protected validator blocks rather than waives its checks.

No claim is made about standalone `tools/pc.py check` genericity or repository-wide cleanroom isolation; those remain separately scoped. The approved Toy 1 policy, active baseline, VO/AD ledgers, proof/contract/design/firmware, and all historical receipts remain untouched. The explicit `--legacy-toy1` CLI path is only for historical diagnostic/assessment compatibility. New generic project operations must use a pinned `--binding`.

**Human-run tests:** `python -m unittest discover -s tests -p 'test_stage_gate.py' -v`, `test_gate_adapter.py`, `test_task.py`, `test_fr001_r1_review_route.py`; additionally run `python tools/stage_gate.py inspect --binding process/gate_configs/AS-001-AP-v1.yaml` and the explicit legacy inspector. Capture failures and source hashes; do not claim PASS until executed. The result is a versioned candidate requiring a distinct independent review.

`framework_frozen=false`, `cleanroom_authorized=false`, `product_verified=false`, `vo_discharged=[]`; VO-002 through VO-006 remain open.
