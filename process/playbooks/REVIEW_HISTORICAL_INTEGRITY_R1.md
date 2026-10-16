# REVIEW_HISTORICAL_INTEGRITY_R1: focused independent FR-003 correction review

**Scope:** FR003_R1_FOCUSED_UNICODE_PATH_CORRECTION_ONLY.  
**Goal:** Close or reject original blocking `FR003-REVIEW-FINDING-001`, not open another prefreeze audit campaign.  
**Role:** verification-agent. **Disposition:** independent scoped review only.

## Entry and provenance

1. Read current `AGENTS.md`, `PROJECT_SPINE.md`, `process/roadmaps/PC_ROADMAP_CURRENT.yaml`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md`, this playbook and task.
2. Check the original FR-003 independent `REVISE` [report](../../reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-report.md) and receipt, the source authorization and exactly its original finding `FR003-REVIEW-FINDING-001`. Preserve those artifacts untouched.
3. From **evidence submission commit** `d35b51da1e7efefa4fe4bf1db7e2a4beb2d2d601`, inspect `reviews/qualification/FR003_HISTORICAL_INTEGRITY_R1-local-test-receipt.json` and verify Git blob `26f72860147b53ed31cc5a9b9a1139585f2387bd`. Confirm receipt `task_id` `FR003-HISTORICAL-INTEGRITY-R1-001`, exactly 7 producer checks with actual recorded exit codes, source revision `0c17ff1b749a675980d848477a92980ff7782c4c`, and addressed finding. Check all nine source SHA-1 and SHA-256 identities against the pinned source revision and receipt. Classify local producer-log claims appropriately if logs are unavailable.
4. A **separate reviewer invocation** is mandatory. If already inside a separately invoked Codex reviewer: `task.py inspect` then `render` and do the review within this invocation. Outside Codex, `task.py run` may launch the assigned reviewer. A rendered prompt alone is not review execution.

## Focused technical review

**F1.** Compare only the `tools/historical_audit.py` and `tests/test_historical_audit.py` changes from original source `66b75a2a3720bca32f13b430a26715da8477641f` to R1 source `0c17ff1b749a675980d848477a92980ff7782c4c`. Are they the minimal UTF-8 path validation and focused negative regression? Check no change to accepted authority, live ledgers or current-worktree verification modules.

**F2.** In an isolated disposable Git fixture, create valid source commit and a JSON receipt with `source_sha256` containing a key `"\\ud800"` (JSON escaped lone high surrogate). Repeat with `"\\udc00"`. Both must produce a bounded `UNRESOLVED` report with a path-encoding reason, never uncaught UnicodeEncodeError. Check a valid Unicode filename still works. If malformed input still escapes, return `REVISE` with exact reproducer.

**F3.** Verify the original FR-003 claims remain scoped: historical match at source revision despite later worktree difference, `HISTORICAL_MISMATCH` only when source-time digests differ, missing source Git objects as `UNRESOLVED`, optional current comparison and separate reviewer disposition with authoring PENDING unchanged. This is a limited regression review, not complete fresh qualification. Source-time hash correspondence is not semantic acceptance or current applicability.

**F4.** Independently run at least `test_fr003_r1_review_route.py`, `test_historical_audit.py`, `test_verification_kernel.py`, `test_active_baseline.py`, `test_fr003_review_route.py`, and one prior review-route test. Record exit codes and test counts; independently inspect the previous evidence audit on actual FR-003 source and original `REVISE` receipt. Producer's seven commands are evidence, but the reviewer should reproduce the critical correction.

## Output and limits

Only write:
- `reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_R1_001-report.md`
- `reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_R1_001-receipt.json`

Use schema `pc-framework-repair-review/v1`, correct task/operation/gate and disposition scope, verified source/evidence identities, distinct reviewer invocation and evidence classes, actual tests and targeted probes, explicit resolution status for `FR003-REVIEW-FINDING-001`, and disposition `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE` or `UNRESOLVED`. State what was not tested.

**Important:** A favorable outcome qualifies only the bounded FR-003 code correction, not any project or firmware. Keep historical initial `REVISE` unchanged. FR-004 work still needs its own authorization. `framework_frozen=false`, `cleanroom_authorized=false`, `product_verified=false`, `vo_discharged=[]`, open VOs 002–006, target `NOT_SELECTED`, F-001 `OUTSTANDING`. The next milestone should emphasize qualifying a single review mode and then a usable fresh-agent bootstrap, not extending this narrow fix into broad security polish.
