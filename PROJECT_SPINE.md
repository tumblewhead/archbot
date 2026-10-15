# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VK-001 bounded path complete; next scope not yet authorized

User push `df1c35e08bb4` contains execution
[EXECUTE_VERIFICATION_LADDER-956fdb75fa6b](reviews/verification/EXECUTE_VERIFICATION_LADDER-956fdb75fa6b/receipt.json)
and independent
[REVIEW_VERIFICATION_RUNG-9de9286189ea](reviews/gates/REVIEW_VERIFICATION_RUNG-9de9286189ea-receipt.json).
Independent disposition: **ACCEPT_WITH_CLARIFICATIONS**. The one approved rung
`ARITHMETIC-MODEL-BOUND` completed, reporting the conditional model results:
`4095²=16,769,025`, `32×4095²=536,608,800`,
`33×4095²=553,377,825`, all fitting modeled unsigned 32-bit arithmetic.
The reviewer independently checked those values, references and 37 source pins
at its checkout. This result is **MODEL_ONLY**, not C/target/product acceptance.

The earlier ERS002 and bounded plan passed independent review. The other 20
ERS claims remain unplanned and **VO-002 through VO-006 remain OPEN**.
No product obligations, design scope, firmware, or authority states changed.
The terminal rung reviewer explicitly requires a separately authorized scope
before further verification execution.

Read [VK-001 terminal checkpoint](docs/VK001_TERMINAL_CHECKPOINT.md) for the
worked gate sequence, a precise next Toy 1 qualification proposal, and UI/archive
defects found during audit. The generated historical briefing carries a stale
reference to earlier ERS re-review. Show subsequent acceptance through linked
review receipts rather than rewriting historical bytes. Current-worktree pin
checking is not a substitute for historical version-aware archive verification.

**Next proposed development after scoped authorization:** finish Toy 1's
actual source/build arithmetic and resource/integration correspondence rather
than repeating the model bound; gather VO-002/003 evidence, then VO-004..006 and
F-001, as the authorized target permits. The documented cleanroom/dialogue/Toy 2
roadmap remains unchanged. The new UI/data-contract concerns are framework
qualification work, not new detector requirements.

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
