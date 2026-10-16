# REVIEW_HISTORICAL_INTEGRITY: independent FR-003 source-time auditor review

**Operation:** `REVIEW_HISTORICAL_INTEGRITY`  
**Role:** `verification-agent`  
**Scope:** `FR003_HISTORICAL_SOURCE_INTEGRITY_IMPLEMENTATION_ONLY`  
**Entry:** FR-003 authorized read-only source candidate, human local regression evidence and immutable Git identities.  
**Authority:** Independent implementation review only. Neither acceptance of a product nor framework freeze, historical receipt promotion, VO discharge, cleanroom or FR-004 work.

## Entry: exact source and independent execution

1. From current HEAD read `AGENTS.md`, `PROJECT_SPINE.md`, `process/roadmaps/PC_ROADMAP_CURRENT.yaml`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md`, this task manifest and playbook. Use selective retrieval; do not load the repository's large historical evidence in bulk.
2. Verify the explicit FR-003 authorization, original proposal/design, authoring report and the predecessor FR-002 `ACCEPT_WITH_CLARIFICATIONS` receipt. FR-002 did not authorize this review or any FR-004 work. Do not change accepted AS/AP/F/CON/DE, target, VO/AD, firmware, original authoring artifacts or historical review receipts.
3. Resolve human receipt `reviews/qualification/FR003_HISTORICAL_INTEGRITY-local-test-receipt.json` **at submission commit** `040400394e030c7898de66aa3bd1a3648f8e3555`; require Git blob `32c0bda1e7cde375da76fe0e09890e8655cd9033`, schema `pc-framework-repair-test-evidence/v1`, task `FR003-HISTORICAL-INTEGRITY-001`, and tested source `66b75a2a3720bca32f13b430a26715da8477641f`. Validate 14 actual recorded command exits (zero) with log digests and sizes.
4. Resolve all **nine** source paths at the pinned tested revision, matching both Git blob SHA-1 against this task and the producer receipt and SHA-256 against producer receipt. Do not compare original source pin against current mutable worktree bytes. Current source `tools/verification_kernel.py` and `tools/active_baseline.py` must remain unchanged.
5. Use a genuinely distinct reviewer invocation from the assistant source author and local test producer. `CURRENT_AGENT_DIRECT`: `task.py inspect`, `render`, then independently perform the review within that existing agent invocation. `OUTER_SHELL_LAUNCH`: `task.py run` from a host shell and confirm actual completed reviewer turns. No nested Codex. `render` alone is never a review.

## Required reviews and reproductions

**H1. Historical identity versus fresh worktree.** Independently reproduce a temporary Git repo with a source file at an old commit, a receipt pinning its SHA-256 and optional Git blob SHA-1, and a later commit changing the file. FR-003 must return `HISTORICAL_MATCH` for the source-time bytes and optionally `DIFFERENT` for present correspondence. Check that current-file verification still detects stale inputs. A historical digest mismatch must return `HISTORICAL_MISMATCH`, not `UNRESOLVED` merely because current files differ. Report exact fixture and actual status.

**H2. Missing/incomplete evidence semantics.** Check missing source_revision, unsupported schema, missing file at an otherwise available commit, nonexistent commit, out-of-range blob, malformed digest, and incomplete optional SHA-1 declarations. Such cases must return `UNRESOLVED` with reasons. Inspect mixed multi-item states: a mismatch and an unresolved item must not be described as fully matched. Critically evaluate whether missing or malformed receipt fields produce a normal bounded `UNRESOLVED` report or escape as an uncaught exception.

**H3. Path/commit safety under cooperative assumptions.** Require exact 40-hex commit IDs. Test `HEAD`, `main`, path traversal, absolute paths, aliases/symlinks at original revision, Git special path notation, and attempts to access history outside requested repository. Verify Git subprocess uses fixed argv, no shell interpretation, no Git network fetching, no execution of source objects and bounded file sizes. Do not expand into hostile cryptographic forgery. Document any genuine memory/size/time limitation of the present implementation.

**H4. Evidence status and review independence.** Preserve original source-time `review_state=PENDING` and report an explicitly linked independent review disposition separately. Check receipt-to-review source revision and submission path agreement; `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE` are review observations, not silently imposed artifact state. An unresolved overlay must not turn a historical `HISTORICAL_MATCH` into acceptance. `present_applicability` must remain `NOT_EVALUATED` unless separately justified; current hash correspondence alone does not prove active applicability.

**H5. Schema and genericity boundaries.** Check only the documented receipt forms are accepted: FR framework authoring source, FR framework independent review, and `pc-verification/v1` with an explicit original source revision. Unknown fields/source mappings must not be guessed. Ensure a second project uses the same audit path, without implicit AS-001/C-002 defaults. The original current-file `verification_kernel.check_pins` and `active_baseline.verify` stay intact.

**H6. Evidence, actual runs and scope.** Independently run or inspect exact commands:
`python -m unittest discover -s tests -p 'test_fr003_review_route.py' -v`;
`test_historical_audit.py`, `test_verification_kernel.py`, `test_active_baseline.py`, `test_fr001_r1_review_route.py`, `test_fr002_continuity_review_route.py`, `test_task.py`; 
`python tools/historical_audit.py inspect --receipt reviews/qualification/FR002_BASELINE_CONTINUITY-local-test-receipt.json --revision 44063ef971bcfd13e96c29eb5371e8fcc14e333a --check-current --review reviews/qualification/REVIEW_FR002_BASELINE_CONTINUITY_001-receipt.json`.
Record exact test counts, actual exits and observed report statuses, not just "green". Verify producer logs in ignored `runs/fr003-historical-integrity/` against their 14 SHA-256/size declarations if available; otherwise mark them `PRODUCER_REPORTED_ONLY` and reproduce key checks. Check prior review and product inputs remain unchanged. A report of `HISTORICAL_MATCH` is **only byte correspondence**, never proof of source correctness, target verification or a VO discharge.

## Reviewer output

Produce **only** new, versioned artifacts:
- `reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-report.md`
- `reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-receipt.json`

Receipt schema: `pc-framework-repair-review/v1`. Include task, operation, gate, disposition scope, distinct invocation ID/mode and independence basis; actual source and evidence revisions/blobs; nine verified source SHA-1 and SHA-256 values; source-time versus current versus reviewer-overlay behavior; classifications H1–H6 as `REVIEWER_REPRODUCED`, `REVIEWER_INSPECTED`, `PRODUCER_REPORTED_ONLY` or `NOT_PERFORMED`; concrete counterexamples; test counts/exits and producer log provenance; findings with severity; and one independent disposition: `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `UNRESOLVED`. The next eligible action is limited by the actual disposition. A blocking exception, incorrect status, or missing evidence must not be reclassified as passing.

Always retain `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, `open_vos:[VO-002,VO-003,VO-004,VO-005,VO-006]`. Toy 1 target remains `NOT_SELECTED`; F-001 final comparison `OUTSTANDING`. No accepted product state or historical receipts may be modified. A favorable FR-003 code review still does not authorize FR-004 implementation or framework freeze.
