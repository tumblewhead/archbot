# REVIEW_GENERICITY_AUDIT: independently challenge prefreeze audit candidate

**Operation:** `REVIEW_GENERICITY_AUDIT`  
**Role:** `verification-agent`  
**Entry:** versioned candidate audit report and receipt, pinned by the task manifest to an exact Git commit and Git blob identities.  
**Authority:** review of the audit's *analysis quality and traceability only*. Acceptance does **not** freeze the framework, qualify Toy 1, repair a blocker or authorize a cleanroom.

## First: establish independent execution and input identity

1. Read `AGENTS.md`, `PROJECT_SPINE.md`, the assigned manifest, `docs/REVIEW_EXECUTION_MODES.md`, `process/pull_run_push_contract.v1.json`, and `agents/verification-agent.md`.
2. Read **both** `reviews/qualification/GENERICITY_PREFREEZE_001-report.md` and `reviews/qualification/GENERICITY_PREFREEZE_001-receipt.json`. Compare the candidate receipt with the author task `AUDIT_GENERICITY-PREFREEZE-001`.
3. Verify the submitted files' **exact Git blob SHA-1 identities**, pinned in `context.review_inputs`, against their bytes and against the source commit `404bef8120dc24782b1c71baffea528ca268b754`. The source snapshot in the author receipt (`c0b6a5e...`) predates the audit candidate's authoring commit; they serve different purposes. Confirm candidate bytes are unchanged since submission. Check source paths/hashes cited by the candidate using the appropriate commit; avoid treating a current-worktree mismatch as evidence that an old accepted artifact was forged.
4. Identify the **actual** current independent reviewer invocation (not a claim derived from `render`). `OUTER_SHELL_LAUNCH` must record actual completed Codex reviewer turns, exit code, output files and telemetry. `CURRENT_AGENT_DIRECT` must be a fresh invocation distinct from the connected-GitHub authoring event, report the actual operations performed and never claim `task.py run` succeeded. Preserve earlier VC-001/VR-001 failed launches unchanged.

## Independently review the six claims

- **Q1 execution modes:** Inspect `tools/task.py`, `tools/task_legacy.py`, `tools/telemetry.py`, `process/operations.yaml`, `process/views.yaml`, `agents/registry.yaml`, role files and relevant tests. Establish whether the missing `experimental-investigator` entry in `agents/registry.yaml` is an actual active-path defect or simply a vestigial metadata difference; avoid assuming every registry must be authoritative. Separate historical launcher failure from evidence about the available host launch mode. Do not require both modes to pass unless the intended frozen process actually supports both.
- **Q2 generality:** Independently inspect the explicit AS-001 paths in telemetry, stage gates and `tools/pc.py`; determine which are generic core coupling versus intentionally Toy 1-specific fixtures. Look for existing project override/configuration paths before declaring a blocker. Preserve legitimate negative stage-gate semantics.
- **Q3 evidence integrity:** Read VK-001 terminal review and VC-001/VR-001 receipts, inspect the version-sensitive behavior of `verification_kernel.check_pins`, and confirm whether current-worktree checking serves *freshness* only or is being used as *historical validity*. Check the retained author briefing versus later independent review. Do not convert host correspondence to target qualification.
- **Q4 cleanroom:** Independently enumerate what a fresh clone/prompt/context projection exposes; distinguish a conceptual disclosure risk from a demonstrated ability to read forbidden sources in a real isolated workspace. Challenge the allowlist: can a fresh project bootstrap without prior solution artifacts, and can the independent acceptance rubric be hidden from the agent? Clarify what can be verified and what remains untested.
- **Q5 Toy 1 scope:** Cross-check the active baseline, VO/AD ledgers, reviewed CON-v6/DE-v7, F-001 state, VK-001 terminal checkpoint, VC-001 and VR-001. Distinguish accepted abstract/model/host evidence from target/integration/publisher claims. Do not invent the target or assert that a host-only milestone is already authorized.
- **Q6 process friction:** Reconcile the two runner failures and prior missing-role incident against measured evidence. No guessed human minutes, token cost, runtime or actual context reads.

## Reviewer must challenge the plan, not just its formatting

For each Q1..Q6, issue `CONFIRMED`, `QUALIFIED`, `DISPUTED`, or `UNRESOLVED` with exact file/section evidence and any independently reproduced check. Explicitly challenge:

- Whether the proposed repair ordering genuinely minimizes rework and unreviewed policy changes.
- Whether cleanroom isolation should be defined first but not physically tested until after generic engine separation.
- Whether project-local roles and test fixtures have incorrectly been described as shared-engine defects.
- Whether an independent review can meaningfully approve an audit report **without** qualifying any execution path.

Use `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, or `UNRESOLVED` only for the **audit candidate within its declared scope**. A favorable disposition is permission to *propose* a bounded repair task under appropriate separate authority, not to make framework changes in this review.

## Executable checks

Run `python -m unittest discover -s tests -p 'test_genericity_review_route.py' -v` and `python tools/task.py inspect --manifest process/tasks/REVIEW_GENERICITY_PREFREEZE-001.yaml`. Independently run other targeted structural/negative controls if useful; record exact commands, exit status, and evidence class. Do **not** run target compilation or a cleanroom replay. Source inspection is not the same as reproducing a programmatic test.

## Immutable outputs

Author **only** these two versioned files, no placeholder output:

- `reviews/qualification/REVIEW_GENERICITY_PREFREEZE_001-report.md`
- `reviews/qualification/REVIEW_GENERICITY_PREFREEZE_001-receipt.json`

Receipt schema `pc-genericity-audit-review/v1`, with at least:

- `task_id`, `operation`, `project_id`, `spine`, `reviewed_candidate_commit`, `reviewed_candidate_report`, `reviewed_candidate_receipt`, their actual Git blob identities and `reviewer_invocation_id`.
- `reviewer_execution_mode` (`OUTER_SHELL_LAUNCH` or `CURRENT_AGENT_DIRECT`), `independent_of_authoring_invocation`, source/subject checks, explicit `reviewer_inspected`, `reviewer_reproduced`, `producer_reported_only`, `not_performed`, and any launcher failure evidence.
- `classifications` for Q1..Q6, findings with severity, `disposition`, `disposition_scope`, `next_eligible_action`, `changed_artifacts`.
- Strictly: `freeze_authorized:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, `open_vos:[VO-002,VO-003,VO-004,VO-005,VO-006]`, `framework_frozen:false`.

If the reviewer is not actually independent, cannot verify submitted identities, or fails to execute, report the blocker and do **not** fabricate a favorable review receipt. Do not overwrite the audit candidate, accepted historical evidence, implementation, active AS/AP/F/CON/DE, VO/AD ledgers or framework engine. Do not automatically issue a repair manifest or claim a freeze.
