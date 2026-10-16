# FR-003 R1 focused historical-integrity review

**Disposition:** `ACCEPT`  
**Scope:** `FR003_R1_FOCUSED_UNICODE_PATH_CORRECTION_ONLY`  
**Invocation:** `direct-review-20261016T-FR003-HISTORICAL-INTEGRITY-R1-001` (`CURRENT_AGENT_DIRECT`)  
**Input checkout:** `70fe90aeaae2c59044a10238c767c9eaae3a7303`  
**Reviewed source:** `0c17ff1b749a675980d848477a92980ff7782c4c`  
**Submitted evidence:** commit `d35b51da1e7efefa4fe4bf1db7e2a4beb2d2d601`, path `reviews/qualification/FR003_HISTORICAL_INTEGRITY_R1-local-test-receipt.json`, blob `26f72860147b53ed31cc5a9b9a1139585f2387bd`.

## Independence, routing, and provenance

This review was performed in a distinct current-agent invocation from the source correction and human-produced local test evidence. `python tools/task.py inspect --manifest process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY_R1-001.yaml` and `python tools/task.py render --manifest process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY_R1-001.yaml` both exited 0. The required route canary `test_fr003_r1_review_route.py` passed (3 tests). I performed the review in this invocation; no nested `task.py run` was used.

The R1 evidence receipt is the declared schema and task, identifies source revision `0c17ff1b749a675980d848477a92980ff7782c4c`, addresses `FR003-REVIEW-FINDING-001`, and records seven checks with exit code zero. Its blob at the declared submission commit matches the manifest pin. All nine declared source Git blob SHA-1 identities match the pinned source revision; all nine source SHA-256 values in the receipt also match bytes read from that revision. These checks establish provenance and identity, not correctness by themselves. Producer logs were not available in this checkout, so the seven producer commands are classified as submitted evidence; the critical correction and focused checks below were independently reproduced.

## Focused findings

### F1 — JSON-escaped lone surrogate path

**Resolved.** The narrow source change in `tools/historical_audit.py` checks UTF-8 encodability in `path_ref()` and converts `UnicodeEncodeError` to `AuditInputError`. The regression covers both lone high and low surrogates after JSON serialization. In an isolated temporary Git repository with an exact valid commit, I independently passed receipts containing U+D800 and U+DC00 keys to `inspect()`. Both returned `UNRESOLVED` with reason `Repository path is not UTF-8 encodable`; neither raised an uncaught exception. A valid repository path containing `é` returned `HISTORICAL_MATCH` / item `MATCH`.

The implementation diff from the originally reviewed source `66b75a2a3720bca32f13b430a26715da8477641f` to R1 is limited to UTF-8 validation in `tools/historical_audit.py` and the focused regression in `tests/test_historical_audit.py`. The current-worktree verifier and active-baseline verifier have no changes in that diff. No authority, accepted product artifacts, or live ledgers were changed.

### F2 — Existing FR-003 semantics and boundary

The independently rerun `test_historical_audit.py` confirms source-time correspondence remains separate from later worktree differences, digest disagreement is `HISTORICAL_MISMATCH`, absent or incomplete historical evidence is `UNRESOLVED`, and review disposition overlays do not rewrite authoring state. The FR-003 historical CLI at the exact R1 source revision returned `HISTORICAL_MATCH`; with `--check-current`, current correspondence is reported separately and present applicability remains `NOT_EVALUATED`. This establishes source-byte correspondence only, not semantic acceptance or current applicability.

## Reproduced checks

All commands exited zero:

| Check | Tests | Exit |
|---|---:|---:|
| `test_fr003_r1_review_route.py` | 3 | 0 |
| `test_historical_audit.py` | 13 | 0 |
| `test_verification_kernel.py` | 13 | 0 |
| `test_active_baseline.py` | 7 | 0 |
| `test_fr003_review_route.py` | 4 | 0 |
| `test_fr001_r1_review_route.py` | 3 | 0 |
| `test_fr002_continuity_review_route.py` | 4 | 0 |
| `test_task.py` | 44 | 0 |

Total: 91 test methods. The targeted disposable-Git probes for both surrogate forms and one valid Unicode filename also produced the expected outcomes. The historical audit CLI against the R1 receipt and pinned source revision exited 0 with `HISTORICAL_MATCH`; the additional `--check-current` run kept current correspondence and applicability separate.

## Disposition and limits

`ACCEPT` resolves the single bounded blocker `FR003-REVIEW-FINDING-001` and qualifies only the FR-003 R1 Unicode-path correction. This is not a fresh broad qualification of all historical-auditor properties. Producer logs were not independently checked because they were unavailable; producer claims beyond the reproduced checks remain classified as submitted evidence. No broad security review, firmware qualification, or product acceptance was performed.

Framework freeze remains false; cleanroom remains unauthorized; product remains unverified; no VO is discharged; VO-002 through VO-006 remain open; target remains `NOT_SELECTED`; final F-001 comparison remains `OUTSTANDING`. The original FR-003 `REVISE` report and receipt remain unchanged. FR-004 work still requires its own authorization.

**Next eligible action:** qualify the necessary reviewer execution mode under its own authorized FR-004 task, then prioritize the FR-005 fresh-agent cleanroom package and bootstrap. This review authorizes none of those actions by itself.
