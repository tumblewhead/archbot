# FR-003 historical source-integrity auditor: source candidate

**State:** Source authored, **NOT LOCALLY EXECUTED** and **NOT INDEPENDENTLY REVIEWED**.  
**Authorization:** `process/decisions/FR003-HISTORICAL-INTEGRITY-AUTHORIZATION-001.yaml`.  
**Scope:** Read-only historical source-byte audit; no acceptance state transitions or existing current-source checker changes.

## Implemented separation

- `tools/historical_audit.py` adds `inspect(root, receipt_ref, revision=None, check_current=False, review_ref=None)` and an explicit `inspect` command. The historical result is `HISTORICAL_MATCH`, `HISTORICAL_MISMATCH` or `UNRESOLVED`.
- Supported receipt forms are explicitly limited to `pc-framework-repair-test-evidence/v1` (`source_revision`, `source_sha256`, optional `source_git_blob_sha1`), `pc-framework-repair-review/v1` (`reviewed_source_revision`, `verified_source_sha256`, optional `verified_source_sha1`), and `pc-verification/v1` with an **explicit recorded** `source_revision` and `source_sha256`. A verification artifact without source revision remains `UNRESOLVED` even when its current files happen to match.
- A full 40-hex commit identity is mandatory, and `--revision` must agree with the receipt's own source revision. The auditor uses Git's local object store, lists exact tree paths, refuses symlink/non-regular historical modes and reads only regular blobs of at most 2 MB. No Git network fetch, shell interpolation or executable code loaded from the historic tree.
- Optional `--check-current` reports today's source correspondence **separately**. `present_applicability` remains `NOT_EVALUATED`, since a digest comparison is not a project authority decision.
- Optional `--review` reports a separately linked `pc-framework-repair-review/v1` disposition and scope, or an explicit unresolved overlay. It **never** changes the original `review_state=PENDING` of an authoring artifact.
- Failure to locate a historical revision/file, unsafe or unsupported input schema, missing pin and oversized object are `UNRESOLVED`, not proof the historical source was wrong. A retrieved byte mismatch is a `HISTORICAL_MISMATCH`.
- `tools/verification_kernel.py` and `tools/active_baseline.py` remain unmodified and retain their *present-state* semantics.

## Proposed local regression

`tests/test_historical_audit.py` contains 12 methods exercising a disposable local Git repository, a later committed source revision, mismatch with presently matching content, correct Git blob hashing, missing/unsafe revisions and paths, unsupported schema, review overlay, historical symlink, explicit source revision for verification artifacts, review receipt shape and the committed FR-002 authoring receipt.

The human should run the new unit suite first, then the unchanged VK-001 and active-baseline suites plus FR-001/FR-002 route regressions. Run the real FR-002 historical CLI example and confirm `HISTORICAL_MATCH`. Preserve failed-run diagnostics under ignored `runs/` and do not create success evidence if any check fails.

The source candidate is not a historical approval, semantic proof, independent review, product/target qualification, FR-004 authorization, cleanroom activation or VO discharge. The previously reviewed FR-002 implementation, the Toy 1 candidate projection and all accepted records remain unchanged.

**Next gate:** bounded human local test receipt, then an independently invoked FR-003 reviewer. FR-003 cannot qualify itself. Framework freeze is still false; VO-002 through VO-006 remain open.
