# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-003 R1 accepted; project isolation architecture proposed

Follow [the machine-readable roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and the [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md).
FR-001 and FR-002 remain independently `ACCEPT_WITH_CLARIFICATIONS`
for their scoped implementations. FR-002's Toy 1 continuity projection
remains a candidate, and its ROOT-002 protected-validator clarification
remains. No project product acceptance follows.

The latest [focused FR-003 R1 independent review](reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_R1_001-receipt.json)
pushed in `ff9c723882b88dd9e5589c745768a1590e0cc9eb` returned
**ACCEPT** for `FR003_R1_FOCUSED_UNICODE_PATH_CORRECTION_ONLY`,
resolving `FR003-REVIEW-FINDING-001`. The reviewer independently
ran 91 test methods, reproduced escaped U+D800/U+DC00 returning bounded
`UNRESOLVED`, and confirmed a valid Unicode path still matches.
Producer logs were unavailable to this reviewer; source identities
and key tests were independently reproduced. The initial FR-003
`REVISE` and all historical receipts remain immutable.
FR-003 acceptance is scoped to the correction plus previously
examined evidence behavior, not new broad security assurance.

**New human architectural direction:** visibly distinguish permanent
framework machinery from project-owned state and disposable runtime.
[Directory ownership contract](process/layout/PC_PROJECT_BOUNDARY_001.yaml),
[layout design](docs/PROJECT_BOUNDARY_LAYOUT_001.md), and the
[bounded migration proposal](process/proposals/PC_PROJECT_ISOLATION_MIGRATION_001.yaml)
document `framework/` (reusable code/process/qualification),
`projects/<project_id>/` (self-contained knowledge, authority, code,
validators, reviews, tests), and project-local ignored `.work/`.
A project should be discoverable simply by dropping in its directory,
and removable as active state by deleting that directory without
altering shared framework source.

**Important:** this target structure is **NOT YET IMPLEMENTED**.
The present root still mixes Toy 1 with the framework across
`knowledge/`, `process/`, `reviews/`, `tools/` and `tests/`.
Do not delete those roots, rewrite accepted receipts, or claim
portable delete/drop works today. Git history retains previous project
content even when the worktree project is removed; FR-005 cleanroom
requires separate positive-allowlist packaging with no old Git history.

**Next eligible decision:** engineering authority approval or revision
of `PC-PROJECT-ISOLATION-MIGRATION-001` before any bulk path moves,
source routing migration or removal of old active roots. FR-004
reviewer-mode qualification remains separately pending; we should
qualify only the single mode actually promised. FR-005's working
fresh-agent unsolved-project bootstrap is the main integration
milestone, then FR-006 separate independent freeze review. No
cleanroom run, target qualification, final F-001, VO discharge or
framework freeze is authorized by this architecture proposal.

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
