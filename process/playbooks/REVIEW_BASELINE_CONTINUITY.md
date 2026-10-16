# REVIEW_BASELINE_CONTINUITY: independent FR-002 cooperative model review

**Operation:** `REVIEW_BASELINE_CONTINUITY`  
**Role:** `verification-agent`  
**Scope:** `FR002_COOPERATIVE_BASELINE_CONTINUITY_IMPLEMENTATION_ONLY`  
**Entry:** reviewed scope, bounded source replacement and ten pinned files, human-reported successful local tests.  
**Authority:** assess this FR-002 implementation only. No project or framework approval, cleanroom launch, target acceptance, VO discharge or FR-003 implementation.

## Entry and independence

1. Start at current HEAD. Read `AGENTS.md`, `PROJECT_SPINE.md`, `process/roadmaps/PC_ROADMAP_CURRENT.yaml`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md` and this manifest/playbook.
2. Read the accepted cooperative-audience operating decision, bounded source authorization and proposal/design, the FR-002 authoring report, the original FR-002 independent **REVISE** review and its preserved source/evidence. The old adversarial R1 review task is paused and must not be treated as a newly approved review.
3. Resolve the human receipt **at submission commit** `44da84c263b54c8b5fcda3d9ea80bfd4109aa6ea`, blob `bf0c598e75bc098998df9552c94bd19d99858da8`, and exact `FR002-BASELINE-CONTINUITY-REPLACEMENT-001` source revision `44063ef971bcfd13e96c29eb5371e8fcc14e333a`. Verify ten Git blob SHA-1 identities and ten SHA-256 values at the original revision. Check all 12 reported command results/exit statuses and log digest/size declarations; if logs are unavailable, classify them `PRODUCER_REPORTED_ONLY`, never claim direct inspection.
4. Establish a **distinct reviewer invocation**, separate from both the assistant implementation author and human test producer. From an already running independent reviewer agent, `task.py inspect`, `render`, and perform the review in that same invocation. From a host shell, `task.py run` and verify actual successful reviewer turns. A rendered prompt or failed nested launcher is not review evidence.

## Required engineering review questions

**C1: Project-owned acceptance boundary.** Inspect `tools/gates/continuity.py` and `tools/gates/binding.py`. Verify the accepted projection is separately identified and cannot be replaced by a candidate without a visible status/authority transition. Distinguish `candidate_for_independent_review` (simulation/inspection) from `accepted_for_trial` (requires separate independent projection review and human approval). Trace actual active Toy 1 baseline, VO/AD, AP and C-002 scope. **Check the non-simulation eligibility path**, not just inspect output.

**C2: Never silently drop obligations.** In a temporary fixture, remove C-002 from the candidate policy/validator while leaving the selected project projection unchanged. Check both `continuity.compare` and the bound CLI/evaluator behavior. Try a stale scope, cross-project VO ledger, missing required validator and a mismatched baseline/review path. Failures should identify the missing or changed accepted obligation. Compare Toy 1's seven charged SRAM categories, 2048-byte ceiling, margin and original negative controls with the historical tests.

**C3: Legitimate changes must be possible.** Use a *synthetic* project to test an explicit, versioned accepted transition and its independent review. Verify exact prior projection ID and baseline, authority record, changed fields, reviewed transition identity and that an unreviewed transition is not sufficient. Check whether the full loader truly permits a reviewed transition changing a protected requirement, rather than only a direct unit call to `continuity.compare`. If only the latter passes, record this limitation and consider `REVISE` or `ACCEPT_WITH_CLARIFICATIONS` according to impact. Do not relax real Toy 1 requirements.

**C4: Truly generic engine.** Confirm no hardcoded `AS-001` authority root in the production loader or common gate. A synthetic ROOT-002 project must load through the same project-owned binding mechanism. If it uses an intentionally unprotected requirement, state that scope and do not treat it as evidence of a new reviewed product. Verify the explicit validator-registration API for future reviewed domain modules is usable and not silently influenced by candidate YAML. No hostile code-execution security testing is required.

**C5: Continuity and historical evidence.** Confirm the original source candidate/reviewer `REVISE`, the R1 trust-registry candidate and its local receipt, and the old Toy 1 binding remain unchanged. Inspect whether the new `AS-001-AP-continuity-candidate-v1.yaml` accurately projects accepted records; candidate status must not imply independently accepted project authority. A content hash proves reproducible bytes, not approval. Do not require cryptographic tamper resistance or treat cooperative users as malicious.

**C6: Reproduction.** Run or independently inspect actual tests:
`test_fr002_continuity_review_route.py`, `test_baseline_continuity.py`, `test_gate_adapter.py`, `test_stage_gate.py`, `test_task.py`, `test_telemetry.py` and a prior FR-002 review-route canary. Capture actual test counts, exit codes, and what each test really proved. Also inspect the new explicit v2 binding and `--legacy-toy1` CLI modes. Reviewers may add temporary adversarial fixtures for **accidental omissions**, without modifying accepted project artifacts.

## Review outcomes

Produce **only**:
- `reviews/qualification/REVIEW_FR002_BASELINE_CONTINUITY_001-report.md`
- `reviews/qualification/REVIEW_FR002_BASELINE_CONTINUITY_001-receipt.json`

Use `pc-framework-repair-review/v1`; record task/operation/gate/scope, reviewed source revision, submission commit/blob, ten verified source Git identities and SHA-256 digests, reviewer mode/independence, producer-log provenance, C1–C6 evidence classes (`REVIEWER_REPRODUCED`, `REVIEWER_INSPECTED`, `PRODUCER_REPORTED_ONLY`, `NOT_PERFORMED`), findings and severity, exact executed checks, `disposition` of `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE` or `UNRESOLVED`, bounded next eligible action, and only the two new changed paths.

Preserve prior `REVISE` without rewriting it. Maintain `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, open VOs `VO-002`–`VO-006`, target `NOT_SELECTED`, and final F-001 `OUTSTANDING`. An independently scoped code verdict is **not** permission to edit accepted products, activate candidate projections or start FR-003.
