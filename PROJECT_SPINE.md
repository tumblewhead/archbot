# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-003 auditor source candidate; local evidence next

Follow the [program roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md).
The prior FR-002 [independent cooperative baseline-continuity review](reviews/qualification/REVIEW_FR002_BASELINE_CONTINUITY_001-receipt.json)
remains **ACCEPT_WITH_CLARIFICATIONS** within its scoped implementation
claim. The minor ROOT-002 protected-validator coverage clarification is
still open. The Toy 1 project continuity projection is still a candidate
and has **not** been activated; all historical FR-002 `REVISE` and R1
receipts remain unchanged.

Engineering authority explicitly approved the bounded
[FR-003 historical-integrity proposal](process/proposals/FR003_HISTORICAL_INTEGRITY_001.yaml)
with reply "yes proceed", recorded in the
[FR-003 authorization](process/decisions/FR003-HISTORICAL-INTEGRITY-AUTHORIZATION-001.yaml).
The [authoring report](reviews/qualification/FR003_HISTORICAL_INTEGRITY-authoring-report.md)
describes new read-only `tools/historical_audit.py`, its explicitly
supported receipt shapes, and 12 synthetic/real history regression
methods in `tests/test_historical_audit.py`. Existing
`tools/verification_kernel.py` current-file checking and
`tools/active_baseline.py` present applicability remain untouched.

**Status: SOURCE CANDIDATE AUTHORED, NOT LOCALLY TESTED, NOT
INDEPENDENTLY REVIEWED.** The human's next step is to pull, run
`test_historical_audit.py`, `test_verification_kernel.py`,
`test_active_baseline.py` and FR-001/FR-002 review-route regressions,
plus a real FR-002 historical-audit CLI check. Stop and return failing
diagnostics if any command fails. If all pass, publish a **new bounded**
`reviews/qualification/FR003_HISTORICAL_INTEGRITY-local-test-receipt.json`
with exact source identities and output fingerprints. The assistant
must inspect pushed evidence before preparing the new independent
FR-003 reviewer task.

The auditor reports (H) historical source-time byte identity,
(A) optional current-worktree byte correspondence, and
(R) a separately linked reviewer disposition. It **does not**
declare general current applicability, alter the original authoring
`review_state`, infer a favorable review, or change accepted project
authority. Missing source-time revision or Git blob means
`UNRESOLVED`, not a historical failure. No network fetch, source
execution, acceptance or target work is authorized.

No FR-004/FR-005/FR-006 implementation, generic framework freeze,
cleanroom, final F-001 decision, product verification or VO discharge
is authorized. Cooperative-audience assumptions remain active.
FR-001's scoped acceptance remains unchanged.

The accepted C-002 charged-SRAM envelope is seven conditional category
ceilings totaling 1792 bytes plus 256 reserve under 2048. All seven
actual target category peaks remain UNKNOWN (`null`), no target
configuration was selected, and VO-002..VO-006 remain OPEN.
Twenty other ERS claims remain unplanned; AD-003 and the final F-001
comparison remain outstanding. No AS/AP/F/CON/DE, implementation source,
VO/AD ledger, or accepted review artifact has been rewritten.
Before cleanroom, distinguish host-qualified-only disposition from
complete target qualification and audit Toy 1 solution leakage.

## VK-001 implementation and limits

Read [VK-001 operating guide](docs/VERIFICATION_SLICE_VK001.md). Its three author
operations use a shared deterministic kernel and pc-verification/v1. Independent
reviews use local Codex. The initial planner validates explicit model/rung
candidates; it does not discover arbitrary physics. Model evidence cannot
discharge a product VO. The interactive human interface is not installed;
structured briefings/questions are emitted now. The ERS and plan bundles record
local authoring, and their reviews record scoped checks. They do not establish
that all fixture demos or the complete regression suite passed; consult actual
run evidence before making those claims. This assistant has not run those tests.

## Current Toy 1 authority

- Active versions: `process/baselines/AS-001-v2-active.yaml`.
- Live VO index: `process/ledgers/vo_ledger-AS-001-v2-active.yaml`.
- Host-only independent C review:
  `reviews/gates/IMPLEMENT_DE-900da7a3ce8c-independent-review.json`.
- Implementation: `implementation/toy1/`, its Engineering Briefing and review request.
- VO-002 through VO-006 and AD-003/F-001 final evidence remain open as recorded.
- Sample-indexed newest-32 behavior, legal 12-bit domain, publisher-owned continuity,
  no invented 1-ms deadline/watchdog, and the approved C-002 scope are preserved.

## Theory and design records

- [Theory of Operation](theory_of_operation.md)
- [Theory of Verification](docs/THEORY_OF_VERIFICATION.md)
- [Verification Framework Requirements](docs/VERIFICATION_FRAMEWORK_REQUIREMENTS.md)
- [VS-001 adversarial study](docs/VERIFICATION_DESIGN_STUDY_VS001.md)
- [VS-002 human-interface study](docs/VERIFICATION_UI_STUDY_VS002.md)
- [Project interaction/archive proposal](docs/PROJECT_INTERACTION_ARCHIVE_PROPOSAL.md)
- [Qualification campaign](docs/QUALIFICATION_CAMPAIGN.md)

## Historical checkpoints

The previous long spine is preserved **byte-for-byte** in
[pre-VK-001 history](docs/history/PROJECT_SPINE_pre_VK001.md). Its older next-step
instructions are history, not the current task. The old task.py is preserved as
tools/task_legacy.py while the new entry point adds one shared verification hook.
ERS001 remains at `reviews/verification/TOY1-VERIFY-ERS001/`; its independent
REVISE review is retained under `reviews/gates/REVIEW_ERS-1d5aeec83447-*`.
[ERS revision 2](docs/ERS_REVISION_002.md) records the inventory repair:
`process/verification/toy1-input-v2.json` retains the original eight statements
and adds thirteen projections of existing arithmetic and resource obligations.
The accepted [ERS002 submission](reviews/verification/TOY1-VERIFY-ERS002/receipt.json)
and [independent ERS review](reviews/gates/REVIEW_ERS-1a1accbb740a-receipt.json)
record resolution of F-ERS-001/002 and 21 requirement/claim mappings. Conditional
SRAM ceilings and proposed DE partitions are commitments/accounting assignments,
not measured capacities. Neither that acceptance nor plan acceptance changes
product requirements, firmware or VO/AD state.

Roadmap: finish Toy 1, genericity review/freeze, cleanroom Toy 1 without the future
dialogue interface, add dialogue, replay Toy 1 with it, then Toy 2 and increased
novelty/scale. VK-001 is the first runnable slice, not completion of that campaign.
