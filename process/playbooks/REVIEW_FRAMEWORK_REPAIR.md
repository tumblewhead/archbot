# REVIEW_FRAMEWORK_REPAIR: independently assess FR-001 project context isolation

**Operation:** `REVIEW_FRAMEWORK_REPAIR`  
**Role:** `verification-agent`  
**Entry:** a human-authorized, versioned source candidate plus a separately pushed local test-evidence receipt.  
**Scope:** `FR001_PROJECT_CONTEXT_IMPLEMENTATION_REVIEW_ONLY`. This gate is not framework freeze, cleanroom containment qualification, Toy 1 final acceptance, or any VO discharge.

## Preconditions and source identity

1. Read `AGENTS.md`, `PROJECT_SPINE.md`, this task manifest, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md`, `process/pull_run_push_contract.v1.json`, and the accepted genericity audit review. Inspect the human authorization decision before judging the patch.
2. Verify the submitted local test receipt at `reviews/qualification/FR001_PROJECT_CONTEXT-local-test-receipt.json`: schema, task identity, six named command results, actual statuses, recorded log sizes/hashes, flags indicating *no* prior independent review, and `source_revision=42b19e7b64e65e8df34eeabc7b0631e8051f6312`.
3. Verify its Git blob SHA-1 `0f5b09af1b9efa549bdfaebcef8fd17cc8d99d3e` at submission commit `4ad7d1cb3121791c6258b90fbe93895a0a689164`. Independently hash all four reviewed source files and compare both their receipt SHA-256 and manifest-pinned Git blob SHA-1 against the source commit. The newer reviewer task and changed project spine are **not** the previous source snapshot.
4. Establish reviewer independence from the source author and human test submitter. From an **outer host shell**, `python tools/task.py run --manifest process/tasks/REVIEW_FR001_PROJECT_CONTEXT-001.yaml` launches Codex and must report a real reviewer turn, actual artifacts and exit. If already inside a **distinct current Codex invocation**, use `task.py inspect`, then `task.py render`, and independently perform the task there. Do not start nested Codex reflexively. Record exact mode and what ran; `render` alone is not review execution. Preserve any failed launch reports without changing them into successful runs.

## Required adversarial checks

**T1. Correct propagation:** Independently inspect `task.main`: validate manifest, forward *exactly that* spine to telemetry; reject unsafe/missing task spines. Test at least two distinct declared spines; verify no AS-001 hardcoded fallback in shared telemetry context selection or review export. A dispatcher pass is not evidence of agent workspace isolation.

**T2. Fail closed:** Inspect `require_spine`, `context_nodes`, `initial_state`, `context_profile` and `selected_context`. Confirm unsafe, nonexistent, symlink escape and missing project cases are not silently redirected. Check that rejection occurs **before** spawning Codex or generating misleading successful run state. Examine whether a failure in any optional/mandatory traversal fails closed versus producing partial context, and whether a role may traverse another project through alternate paths/collections.

**T3. Isolation semantics:** Reproduce or inspect alpha/beta positive and negative controls; inspect both context estimate and ZIP export, confirming project-appropriate hashes and paths. **Differentiate** unintended role-selected cross-project input from whole-repository operations such as `pc.catalog()`, `snapshot()`, unrestricted shell/search permissions and cross-project evidence references. These remain independent cleanroom-safety obligations unless actually constrained by FR-001.

**T4. Evidence integrity and regressions:** Compare local `runs/fr001-project-context/` test logs with each recorded SHA-256/byte count if present. They may be missing in a fresh checkout; if absent, explicitly record not inspected and independently rerun relevant tests to cover the same properties. Verify receipt self-consistency and source pinning. Run
`python -m unittest discover -s tests -p 'test_fr001_review_route.py' -v`,
`python -m unittest discover -s tests -p 'test_telemetry.py' -v`,
`python -m unittest discover -s tests -p 'test_task.py' -v`,
and
`python -m unittest discover -s tests -p 'test_stage_gate.py' -v`.
Additional negative controls are encouraged only if scoped to this review. Preserve their exact commands, outcomes and whether the reviewer actually reproduced them.

**T5. Authorized boundary and backwards compatibility:** Check that manual telemetry `start`, batch `run`, `finish`, and `export` behave coherently with new required `--spine` and that legacy run packets lacking a spine cannot silently export Toy 1 context. Identify any unsupported/manual bypass or behavior change transparently. Confirm no accepted AS/AP/F/CON/DE, firmware, C-002 gate logic, VO/AD ledger, historical review or final F-001 outcome was modified. Treat `pc.py check` and C-002 separation as **FR-002 or later**, not grounds to enlarge this patch without authorization.

**T6. Adequacy of claim:** The narrow claim is **role-projected context reporting and export require a declared spine and reject sibling-project traversal**. Do **not** claim process-wide project isolation, physical cleanroom containment, model inability to remember past Toy 1, or complete support for arbitrary project layouts. If the advertised property is only partially protected, return `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, or `UNRESOLVED` with a specific counterexample.

## Independent review artifacts (new files only)

- `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_001-report.md`
- `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_001-receipt.json`

Receipt schema: `pc-framework-repair-review/v1`. Record task/operation, reviewed source revision, submission path, **verified** Git blob and source SHA-256 identities, reviewer invocation ID and mode, independent-of-authoring flag, explicit checks with evidence class (`REVIEWER_REPRODUCED`, `REVIEWER_INSPECTED`, `PRODUCER_REPORTED_ONLY`, `NOT_PERFORMED`), separate classifications T1–T6, findings with severity, `disposition` (`ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `UNRESOLVED`), scoped rationale, `changed_artifacts`, and specific next eligible action.

The immutable authority fields must remain:
`framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`,
`vo_discharged:[]`, `open_vos:["VO-002","VO-003","VO-004","VO-005","VO-006"]`.
No direct reviewer authorizes future FR-002 implementation, selects a target, accepts architectural debt or silently marks FR-001 fully qualified outside its narrow scope.

If required identities disagree, source files changed, tests fail unexpectedly or independence is not demonstrable, STOP or return `REVISE`/`UNRESOLVED`. Do not rewrite the evidence receipt to make it pass.
