# REVIEW_FRAMEWORK_REPAIR_R1: independent FR-001 correction review

**Operation:** `REVIEW_FRAMEWORK_REPAIR_R1`  
**Role:** `verification-agent`  
**Scope:** `FR001_PROJECT_CONTEXT_R1_IMPLEMENTATION_REVIEW_ONLY`  
**Entry:** R1 source correction, fresh human-run test receipt and prior **REVISE** review.  
**Authority:** Evaluate whether this bounded context-selection repair satisfies its own claim. No framework freeze, cleanroom authorization, product acceptance, VO/AD mutation or authority over FR-002.

## Independence and immutable identity

1. Read `AGENTS.md`, `PROJECT_SPINE.md`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md`, and this exact task manifest. Read the FR-001 authorization and R1 author report. Read the prior `REVIEW_FR001_PROJECT_CONTEXT_001` **REVISE** report and receipt, not merely their summaries.
2. Confirm the new R1 receipt is at the pinned submission commit `8d06dc3dd87db0c244ed72dc5cc1a69702c573dd`, with Git blob SHA-1 `3b575f20b4b6616d27a5f65be312a96e7f57e822`. Verify its schema, R1 identity, seven actual command entries, zero reported exit codes, log SHA-256/size declarations, all three finding IDs and `independently_reviewed:false`.
3. Resolve **each of the five** manifest-pinned source blobs from `3dc5f6ec854971243877f5d7357c7ca034880539`. Compare their Git blob SHA-1 identities and the source SHA-256 values in the R1 evidence receipt. Note that the telemetry fix was initially committed at `e0ef748b70c29b6c802b325aab0afaa4d8b4ecd7`, and the source revision also includes a historical-pin regression repair. **Do not** validate original FR-001 pins against current worktree bytes. Never edit the original submission, prior REVISE receipt or accepted project documents.
4. Confirm this reviewer is a distinct invocation from the source author and human test producer. `CURRENT_AGENT_DIRECT`: inspect, render and actually review within the existing independently invoked Codex agent. `OUTER_SHELL_LAUNCH`: start via `tools/task.py run` from a host shell and verify actual completed reviewer turns and output. A rendered prompt alone is not an execution. Preserve earlier failed nested-runner records.

## Focused review questions and adversarial tests

**R1 symlink provenance:** Reproduce the prior Alpha spine symlink counterexample and the new negative control. Attempt a symlink in a parent directory, a symlink on an optional or mandatory relationship target, and an alias that resolves inside another project. Check whether a role can report Alpha while actually projecting Beta. The lexical/resolved comparison and their error paths must be examined, not assumed effective.

**R2 project boundary:** Independently test a typed edge into another project under (a) the same architecture collection, (b) a different collection such as `history/beta`, and (c) the explicitly shared `knowledge/bkp`. Confirm foreign project-owned nodes fail closed while valid shared-BKP evidence is still accessible through permitted, explicit typed links. Inspect whether the policy is *intentionally restrictive*, and identify any other shared collection which would require future authorization rather than accidentally becoming visible.

**R3 mandatory closure:** Reproduce the missing mandatory relationship target and a mandatory nonlocal/URL-valued target. Check at multiple traversal depths and on a descendant concept. Confirm an absent mandatory dependency cannot yield an `available:true` profile or a ZIP context payload that silently omits it. Optional missing edges need not become mandatory. Record whether this guarantee is enforced only at telemetry projection or also by the underlying `pc.traverse`; do not overstate its scope.

**Historical pins and regression:** Reproduce or independently inspect the new `tests/test_fr001_review_route.py` behavior: resolve prior evidence at original commit, compare original source hashes, and reject unsafe revision/path expressions. Do not rewrite the old manifest to point at R1. Inspect all seven original producer logs if they are available under ignored `runs/`; otherwise mark them *not inspected* and independently reproduce relevant tests. Run these exact checks: `python -m unittest discover -s tests -p 'test_fr001_r1_review_route.py' -v`, `test_telemetry.py`, `test_task.py`, `test_fr001_review_route.py`, and `test_stage_gate.py`. Record actual test counts and exit codes, not just "all green".

**Limited authority:** Validate source/test changes relative to `42b19e7b64e65e8df34eeabc7b0631e8051f6312`: only authorized telemetry/test/historical route repairs plus additively versioned reports/spine. Do not confuse an accepted FR-001 *role-projected context* guarantee with whole-repository isolation: `pc.catalog()`, broad `snapshot()`, shell access, task evidence links, historical source availability and the cleanroom input pack remain separate work.

## Independent disposition and outputs

Produce **only** two new, versioned files:

- `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-report.md`
- `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-receipt.json`

Use schema `pc-framework-repair-review/v1` and include task/operation/gate/project/spine, previous review ID and preserved `REVISE` disposition, reviewed source revision, submission commit/blob, verified per-file Git blob SHA-1 and SHA-256, reviewer invocation ID/mode and independence evidence, log provenance, actual tests, reproduced/inspected/not-performed checks, R1/R2/R3 and historical-pin classifications, findings with severity, `disposition` (`ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `UNRESOLVED`), `disposition_scope`, exact `changed_artifacts`, and a bounded `next_eligible_action`.

The receipt MUST retain `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, `open_vos:["VO-002","VO-003","VO-004","VO-005","VO-006"]`. Do not assert target selection, final F-001 comparison or accepted architectural debt changes.

On a source mismatch, uncontrolled leakage path, unexplained test failure, or missing reviewer independence, issue `REVISE` or `UNRESOLVED` rather than a fabricated acceptance. This task neither implements FR-002 nor authorizes the physical cleanroom.
