# REVIEW_FR001_PROJECT_CONTEXT-001: independent framework repair review

**Disposition: REVISE** for the narrow claim that declared-spine role context rejects sibling-project traversal. The source correctly propagates a spine and rejects ordinary unsafe or missing spine paths, but a symlink alias can make the selected project differ from the recorded project, and a relationship into another knowledge collection bypasses the sibling check.

## Identity and execution

- Checkout/input revision: `1d37651fd3cb44bf025f6f0be772c0c61f5f463f`.
- Reviewed source revision: `42b19e7b64e65e8df34eeabc7b0631e8051f6312`.
- Submission commit: `4ad7d1cb3121791c6258b90fbe93895a0a689164`.
- The submitted receipt blob is `0f5b09af1b9efa549bdfaebcef8fd17cc8d99d3e`, matching the manifest and the receipt at the pinned submission commit. Its six named check records have exit code 0, `independently_reviewed=false`, and the required authority limits.
- All four reviewed source blobs and source SHA-256 values match the manifest and submission receipt at the pinned source revision. The six local producer logs are present, and each recorded byte count and SHA-256 matches.
- Execution mode: `CURRENT_AGENT_DIRECT`, invocation `direct-review-20261015T064800Z-codex-current-agent`. This is the currently assigned invocation, separate from the source authoring and human local-test submission events. `task.py inspect` and `task.py render` succeeded; this review was then performed directly here. No nested `task.py run` was attempted.

## Checks and findings

| Check | Result | Evidence and limits |
|---|---|---|
| **T1 — spine propagation** | PASS | Inspected `task.main`: validated `selected["spine"]` is passed unchanged as telemetry `--spine`. `test_task_run_passes_exact_manifest_spine_to_telemetry` and two-project alpha/beta tests passed. No AS-001 fallback is present in shared context selection/export. This establishes dispatch and projection behavior, not agent workspace isolation. |
| **T2 — fail closed** | PARTIAL | `require_spine` resolves paths under `knowledge/`, rejects escape/non-Markdown/missing files, and `initial_state` validates context before creating run state; tests confirm missing/unsafe and ordinary cross-project declarations leave no run directory. However, a symlink at the declared alpha spine pointing to beta is resolved and accepted: the profile reports alpha while selected paths are beta. Also, `pc.traverse` silently skips a relationship whose target is absent, including a mandatory-closure edge, so partial context can be reported available. |
| **T3 — isolation semantics** | PARTIAL | The required telemetry tests passed and exercise both alpha/beta projections and ZIP context paths/hashes. A reviewer-reproduced temporary fixture confirmed the symlink mismatch. The cross-project rejection checks only paths under the spine's first collection (for example, `knowledge/architecture/`); a relation into a project under a different collection is not classified as cross-project by that check. This is an inspected code-path bypass, not a claim that an existing production spine currently uses it. Whole-repository `pc.catalog()`/`snapshot()`, shell/search access, and cross-project evidence references remain separate cleanroom obligations. |
| **T4 — integrity and regressions** | PASS | Receipt pins and all six producer logs verified. Reproduced: `python -m unittest discover -s tests -p 'test_fr001_review_route.py' -v` (3 tests); `... -p 'test_telemetry.py' -v` (8); `... -p 'test_task.py' -v` (44); `... -p 'test_stage_gate.py' -v` (13). All exited 0. Tests are deterministic structural/regression evidence, not approval or engineering proof. |
| **T5 — boundary and compatibility** | PASS WITH LIMITS | `start` and batch `run` require `--spine`; `finish` uses recorded run state. Export of a legacy run with no spine fails context export rather than falling back to Toy 1; `--no-context` remains an explicit way to omit context. Existing explicit Toy 1 tests pass. `pc.catalog()` and `snapshot()` still operate repo-wide and unrestricted shell/search/evidence references are not constrained here. Diff from source revision contains no accepted AS/AP/F/CON/DE, firmware, C-002, VO/AD ledger, historical-review, or F-001 outcome edits. |
| **T6 — claim adequacy** | REVISE | The authorized claim is not fully protected: the recorded-spine/selected-project mismatch is directly reproduced, and the collection-local sibling test can be bypassed through an alternate collection. Narrowing the claim to ordinary non-symlink projects in one collection would materially weaken the authorized sibling-project claim. |

### Findings

1. **High — declared spine can disagree with selected project.** `require_spine` resolves symlinks before deriving project identity, while state retains the caller's original spine string. A temporary alpha-to-beta spine symlink yielded `available=true`, `spine=/architecture/alpha/spine.md`, and beta spine/result in selected context. Reject symlinked spine paths or otherwise bind the declared identity to the resolved project before profile, run-state creation, and export.
2. **High — project boundary is collection-local.** `context_nodes` rejects another project only when a traversed path remains under the source collection. A relationship to a project under another collection is not rejected by this condition. Define project identity and reject traversal outside that project across all knowledge collections; add a negative control.
3. **Medium — missing mandatory target can yield partial context.** `pc.traverse` queues only existing files and does not fail on an absent target, including a mandatory edge. Decide whether context eligibility requires complete mandatory closure; if so, fail closed and test a missing mandatory target. This is distinct from FR-002 C-002 policy.

## Scoped rationale and next action

Core dispatch and normal alpha/beta role projection are sound, and no authority boundary was crossed. The two boundary counterexamples affect the central FR-001 claim, so this review does not accept the repair as implemented. Return the findings to the authorized FR-001 source-authoring workflow for a versioned correction, updated source/test evidence and manifest pins, followed by a new independent review. Do not infer permission here for FR-002, framework freeze, cleanroom work, product acceptance, target selection, or VO/AD changes.

`changed_artifacts` for this review are only the report and receipt named below. `framework_frozen=false`, `cleanroom_authorized=false`, `product_verified=false`, `vo_discharged=[]`; VO-002 through VO-006 remain open.
