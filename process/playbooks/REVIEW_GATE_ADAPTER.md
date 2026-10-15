# REVIEW_GATE_ADAPTER: independent FR-002 source and authority review

**Operation:** `REVIEW_GATE_ADAPTER`  
**Role:** `verification-agent`  
**Scope:** `FR002_GATE_ADAPTER_IMPLEMENTATION_REVIEW_ONLY`  
**Entry:** bounded FR-002 source candidate, a corrected fixture, human local regression receipt, and explicit engineering-authority scope.  
**Authority:** independent code and evidence review only, not approval of a Toy 1 architecture, product, F-001 outcome, cleanroom or a framework freeze.

## Identity, scope and reviewer execution

1. Start from the repository's current HEAD. Read `AGENTS.md`, `PROJECT_SPINE.md`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, role definition and this exact registered manifest/playbook.
2. Read `process/decisions/FR-002-GATE-ADAPTER-AUTHORIZATION-001.yaml`, the bounded FR-002 proposal/design, authoring report, and the FR-001 R1 `ACCEPT_WITH_CLARIFICATIONS` receipt. Check that accepted AS/AP/F/CON/DE, C-002 scope, product sources, active VO/AD ledgers and previous independent receipts have not been rewritten.
3. Verify the human receipt `reviews/qualification/FR002_GATE_ADAPTER-local-test-receipt.json` at **submission commit** `c0cc00658c9afdc3eea111905b131a272d87863c`, blob SHA-1 `531ba3bf4d713a45a2e669e26b2e888da4c3f0a9`, schema `pc-framework-repair-test-evidence/v1`, and source revision `3c2fd85cb0bde0c13b7639e24220143e26344536`. It reports nine checks, all exit zero, and a deliberately absent independent disposition. Their raw logs may exist only in ignored local `runs/fr002-gate-adapter-r1/`; do not claim raw log inspection when unavailable.
4. Verify each of the **seven** Git source blobs at the pinned source revision against the manifest and receipt SHA-256 values. The implementation first landed at `57f69f5b2d8d69de876aa72649e8aa5f783ef4e9` and the fixture fix at `3c2fd85cb0bde0c13b7639e24220143e26344536`. Do not compare historical source bytes against a mutable future working tree.
5. Establish a genuinely distinct reviewer invocation from the assistant author and human test producer. In `CURRENT_AGENT_DIRECT`, run `task.py inspect` then `render` and perform the review *in that invocation*. In `OUTER_SHELL_LAUNCH`, use `task.py run` from the outer host shell, then confirm real completed reviewer turns and outputs. Do not start nested Codex. Neither a prompt render nor a failed launcher can be promoted into a review.

## Adversarial review, beyond green tests

**G1: Common versus domain scope.** Confirm `tools/gates/common.py` has no implicit AS-001, C-002, 2048-byte SRAM, detector buckets or F-001 constants. Confirm `tools/gates/toy1_c002.py` preserves the original seven-category accounting, positive margin, scope and authority checks. Compare the old `tools/stage_gate.py` behavior at `fbb63f2b8120fbc7b6d610f02f1d61595ba6e934` with new explicit historical `stage_gate.evaluate` and `--legacy-toy1`. Check positive and every recorded negative gate canary, not just test count.

**G2: Fail-closed validator dispatch.** Examine `gates.binding.load_binding` and `gates.common.evaluate`. Try missing, duplicate, unknown, wrong-project validators; mismatched requirement ID; swapped approved C-002 scope; altered validator implementation pin; and protected-policy requirement changes. Check that `C-002` can never be silently waived when the reviewed Toy 1 policy requires it. Distinguish checks enforced by binding from checks enforced only if a caller voluntarily uses `load_binding`.

**G3: Authority laundering, high priority.** A Git blob hash establishes content identity, **not by itself engineering approval**. Attempt a synthetic copy of the project with policy `protected_scope_decisions` weakened or changed, and then *recompute* the blob ID in a new binding. Can an attacker or mistaken operator reach an eligible gate with the altered policy, forged baseline review, or forged 'active' VO ledger, even though all byte pins are internally consistent? Check whether the active reviewed source/policy identity and reviewer provenance are verified against independent authority or merely read from a self-asserted candidate manifest. This is a central FR-002 requirement: wrong authority cannot be accepted merely because content is pinned. If a counterexample passes, record exact scope and return `REVISE`, not a favorable verdict based on the limited existing canaries.

**G4: Fresh project and evidence boundaries.** Exercise `ROOT-002` or a second synthetic project with its own baseline, policy, VO/AD and F identifier. Distinguish a demonstration of *syntactic* project routing from genuine authorized source provenance. Test no forced Toy 1 numerical assumptions, C-002 validator, 2048-byte limit, or final F-001 label. Verify a wrong project/spine, cross-project VO ledger or baseline, unsupported stage, or missing required review results in a blocker.

**G5: CLI and backward compatibility.** Re-run or inspect explicit `--binding` and `--legacy-toy1` inspector paths. Confirm the generic CLI has no implicit Toy 1 file defaults; verify overrides do not combine unsafely with `--binding`. The historical programmatic `evaluate` is Toy 1-only and should never be misrepresented as the generic authority path. Inspect how non-simulation decisions are labeled and ensure eligibility is never phrased as approval, product evidence, proof of C correctness, VO discharge, or a final F-001 ranking.

**G6: Evidence, tests and history.** Independently run
`python -m unittest discover -s tests -p 'test_fr002_review_route.py' -v`,
`test_gate_adapter.py`, `test_stage_gate.py`,
`test_task.py`, and `test_fr001_r1_review_route.py`.
Record actual test counts and exit codes, plus any new adversarial case. Inspect the nine producer logs and match SHA-256/bytes if locally accessible; otherwise mark them `HUMAN_REPORTED_ONLY`. Preserve the initial FR-002 failed fixture run and corrected source/test commits separately. An unexpected structural failure or missing source pin is a blocker, not a success by association.

## Scoped disposition and outputs

Produce **only**:
- `reviews/qualification/REVIEW_FR002_GATE_ADAPTER_001-report.md`
- `reviews/qualification/REVIEW_FR002_GATE_ADAPTER_001-receipt.json`

Receipt schema `pc-framework-repair-review/v1`. Include task/operation/gate, `FR002_GATE_ADAPTER_IMPLEMENTATION_REVIEW_ONLY`, source and evidence revisions, verified source SHA-1/SHA-256, reviewer invocation and execution mode, independence, per-check `REVIEWER_REPRODUCED`/`REVIEWER_INSPECTED`/`PRODUCER_REPORTED_ONLY`/`NOT_PERFORMED`, G1–G6 classifications, findings with severity, `disposition` (`ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `UNRESOLVED`), bounded `next_eligible_action`, and exactly the two new changed paths.

Remain explicit: `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, `open_vos:[VO-002,VO-003,VO-004,VO-005,VO-006]`, no target configuration or final F-001 completion. A favorable scoped review may support proposing the *next* repair; it cannot retroactively grant authority to freeze, change accepted scope, accept AD or run a cleanroom.

If missing provenance, authority laundering, inconclusive checks, or another material defect is found, return `REVISE` or `UNRESOLVED` and preserve the source and receipts rather than silently changing the tested code.
