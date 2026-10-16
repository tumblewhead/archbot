# FR-003 historical integrity independent review

**Disposition:** `REVISE`  
**Scope:** `FR003_HISTORICAL_SOURCE_INTEGRITY_IMPLEMENTATION_ONLY`  
**Invocation:** `direct-review-20261015T-FR003-HISTORICAL-INTEGRITY-001` (`CURRENT_AGENT_DIRECT`)  
**Input checkout:** `563f0789907c09f1735ce37d43e4b09e7098eced`  
**Reviewed source:** `66b75a2a3720bca32f13b430a26715da8477641f`  
**Submitted test evidence:** commit `040400394e030c7898de66aa3bd1a3648f8e3555`, path `reviews/qualification/FR003_HISTORICAL_INTEGRITY-local-test-receipt.json`, blob `32c0bda1e7cde375da76fe0e09890e8655cd9033`.

## Independence and execution

This was a distinct current-agent invocation from both the source-authoring and local-test-producing activities. `python tools/task.py inspect --manifest process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY-001.yaml` and `python tools/task.py render --manifest process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY-001.yaml` both exited 0. I performed the review in this invocation; no nested `task.py run` was used. The task manifest, authorization, cooperative operating decision, design, playbook, predecessor FR-002 receipt, and AS-001 spine were inspected.

The submitted receipt has the required schema, task ID, and source revision. Its blob at the declared submission commit equals the pinned blob. All nine declared source paths match both their producer-declared SHA-1 Git blob identities and SHA-256 digests when read from the pinned source revision. The 14 ignored producer logs are available and every file matches its declared byte count and SHA-256 digest. These establish evidence identity and producer-log correspondence, not semantic correctness or acceptance.

## Findings

### F1 — malformed UTF-8 path escapes the bounded unresolved result (blocking)

I created a disposable Git repository with a valid exact commit and a valid `pc-framework-repair-test-evidence/v1` JSON receipt whose `source_sha256` mapping contains the key `"\\ud800"`. `historical_audit.inspect()` raised `UnicodeEncodeError: 'utf-8' codec can't encode character '\\ud800' ...` from `ref.encode("utf-8")` in `historical_blob()`. It did not return the required bounded `UNRESOLVED` result. JSON permits escaped lone surrogates, and `path_ref()` currently does not reject them. This directly violates the required behavior for malformed receipt fields and means the caller can receive an uncaught exception instead of a normal audit record.

**Required correction:** reject non-UTF-8-encodable path strings in `path_ref()` or catch the encoding failure and convert it to `AuditInputError`, then add a regression asserting `UNRESOLVED` with a reason for a JSON-escaped lone surrogate. Re-run the authorized FR-003 regression and submit a new source/evidence revision for review.

## H1–H6 review results

- **H1 — `REVIEWER_REPRODUCED`.** The synthetic old-commit/later-edit canary passes: historical bytes remain `HISTORICAL_MATCH` while current correspondence is `DIFFERENT`. I also ran the auditor against the FR-003 receipt at its exact source revision: `HISTORICAL_MATCH`, with current correspondence `DIFFERENT` because `AGENTS.md`, `PROJECT_SPINE.md`, and the roadmap have since changed. The result leaves `present_applicability` as `NOT_EVALUATED`. Historical digest mismatch is separately asserted to produce `HISTORICAL_MISMATCH` even when present bytes match.
- **H2 — `REVIEWER_REPRODUCED`, with blocking counterexample F1.** Existing tests cover missing/conflicting revision, unsupported schema, malformed/missing digest declarations, missing historical files, and unresolved linked reviews. My additional probe confirmed an empty optional Git blob-SHA1 map is accepted when SHA-256 pins match. The lone-surrogate key escapes as an exception, so malformed fields do not uniformly yield bounded `UNRESOLVED` output.
- **H3 — `REVIEWER_INSPECTED` and `REVIEWER_REPRODUCED`.** Exact 40-hex revisions are required; `HEAD`, `main`, zero/nonexistent commits and unsafe paths are rejected/unresolved in the canaries or targeted probe. Historical tree modes are limited to regular blobs, source bytes to 2,000,000, receipt bytes to 2,000,000, items to 128, and each Git subprocess has a 15-second timeout. Fixed argv with no shell, local Git object reads, no fetch, and no execution of historical objects were inspected. Existing canaries cover traversal, aliases, symlink objects, and moving refs. No hostile Git-forgery claim is made. `subprocess.run` captures command output in memory before path/result bounds are applied; the timeout and Git object checks bound normal cooperative use, but there is no independent total-output memory cap for `ls-tree`.
- **H4 — `REVIEWER_REPRODUCED`.** The synthetic overlay test keeps authoring `review_state=PENDING` while reporting the independent disposition separately; mismatched source/path overlays become `UNRESOLVED` without changing historical status. The FR-003 submitted test-evidence receipt itself has no `review_state`, so this input correctly reports `authoring_review_state: null`; its authoring report still states it is not independently reviewed. The real FR-002 CLI check reports a linked `ACCEPT_WITH_CLARIFICATIONS` overlay separately, `HISTORICAL_MATCH`, and `present_applicability: NOT_EVALUATED`. That prior disposition is not imported as an FR-003 decision.
- **H5 — `REVIEWER_INSPECTED` and `REVIEWER_REPRODUCED`.** The implementation explicitly supports only the three documented receipt schemas and requires the explicit source revision for `pc-verification/v1`. A synthetic path under `knowledge/other-project/` passes through the same generic audit path without AS-001/C-002 defaults. The unchanged current-file verifier and active-baseline verifier have no diff between the pinned source and this checkout.
- **H6 — `REVIEWER_REPRODUCED`.** Commands and actual results:

  | Check | Methods | Exit |
  |---|---:|---:|
  | `test_fr003_review_route.py` | 4 | 0 |
  | `test_historical_audit.py` | 12 | 0 |
  | `test_verification_kernel.py` | 13 | 0 |
  | `test_active_baseline.py` | 7 | 0 |
  | `test_fr001_r1_review_route.py` | 3 | 0 |
  | `test_fr002_continuity_review_route.py` | 4 | 0 |
  | `test_task.py` | 44 | 0 |
  | FR-002 historical CLI | `HISTORICAL_MATCH` | 0 |

  Total: 87 unit-test methods across the seven suites. The FR-003 historical CLI also returned `HISTORICAL_MATCH` (exit 0), current correspondence `DIFFERENT`, and `present_applicability: NOT_EVALUATED`. All 14 producer log size/digest declarations matched the available ignored files. The targeted malformed-surrogate probe failed as described in F1.

## Disposition and limits

`REVISE` is limited to the FR-003 historical-auditor implementation because F1 contradicts the required bounded failure semantics. The source-time match proves only byte correspondence. It does not establish source correctness, current applicability, product verification, target qualification, or VO discharge. The independent FR-003 review observation is separate from the source artifact's authoring state.

Framework freeze remains false; cleanroom remains unauthorized; product remains unverified; no VO is discharged; VO-002 through VO-006 remain open; target remains `NOT_SELECTED`; final F-001 comparison remains `OUTSTANDING`. No accepted product state, historical receipt, or existing FR-002 review was changed.

**Next eligible action:** correct F1 within the existing FR-003 source authorization, add its regression, obtain new local test evidence, and request a distinct review of the new revision. This `REVISE` disposition does not authorize FR-004, framework freeze, cleanroom, target selection, or product acceptance.
