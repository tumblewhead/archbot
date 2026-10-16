# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-003 R1 producer evidence verified; focused review next

Read the [durable roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md).
FR-001 and FR-002 retain scoped `ACCEPT_WITH_CLARIFICATIONS`, with
FR-002's ROOT-002 protected-validator coverage clarification preserved.
Toy 1's candidate continuity projection is not active.

FR-003 initially returned **REVISE** in
[its independent review](reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-receipt.json)
for finding `FR003-REVIEW-FINDING-001`: a JSON-escaped lone
surrogate source path escaped as `UnicodeEncodeError` rather than
bounded `UNRESOLVED`. This initial review and old producer receipt
remain untouched.

A narrow fix in `tools/historical_audit.py` and regression for high/low
lone surrogate values were committed at
`0c17ff1b749a675980d848477a92980ff7782c4c`.
The user's [new R1 local receipt](reviews/qualification/FR003_HISTORICAL_INTEGRITY_R1-local-test-receipt.json)
was pushed in `d35b51da1e7efefa4fe4bf1db7e2a4beb2d2d601`
and reports **seven exit-zero commands**, with nine source pins
matching the tested source commit. This is producer evidence, not
independent acceptance.

**Next eligible task:** distinct `verification-agent`
`REVIEW_FR003_HISTORICAL_INTEGRITY_R1-001` using
[manifest](process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY_R1-001.yaml)
and [focused playbook](process/playbooks/REVIEW_HISTORICAL_INTEGRITY_R1.md).
Human pulls, runs `test_fr003_r1_review_route.py`, inspects the task,
then executes a separate reviewer invocation and selectively publishes
the report/receipt. If reviewer reports `REVISE`, preserve it.
The assistant inspects the actual verdict before changing milestone
status or proposing FR-004.

**Direction after FR-003 acceptance:** minimize FR-004 to the necessary
reviewer mode, prioritize FR-005 fresh unsolved-project/bootstrap
demonstration, then FR-006 integrated freeze and an independently
authorized cleanroom Toy 1. No unlimited polish cycle.

FR-003 remains **not independently accepted**. No FR-004 implementation,
framework freeze, cleanroom, target acceptance, final F-001, AD change or
VO discharge is authorized. Cooperative-audience assumption applies.

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
