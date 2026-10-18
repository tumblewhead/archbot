# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 synthetic AS activated; Proof Scout and FOM next

The original AS revision `AS-REV-002.md` was archived at
`50abb5f57d4e049825bb565d53f477fc303d08dd` from the
new diagnostic author; its exact bytes and separate D001 requirements
choices are pinned on `experiment/toy1-pipe-cleaner-001`.
The second distinct reviewer produced
[REVIEW-002.json](reviews/diagnostics/CLN-001-TASK-002/REVIEW-002.json)
and [REVIEW-002.md](reviews/diagnostics/CLN-001-TASK-002/REVIEW-002.md),
both pushed at `82ea7793b15c292e103fcd3d18ab1dc8504abf4f`.
The source Git blob identities match the reviewer outputs
recorded in the earlier conditional AS disposition. Reviewer verdict:
**READY_FOR_DELEGATED_AS_DISPOSITION** with no blocking technical
finding, F3 MINOR provenance clarification.

By the human's explicit CLN-001-only synthetic requirements
delegation, the assistant previously issued
[AS-DISPOSITION-002](reviews/diagnostics/CLN-001-TASK-002/AS-DISPOSITION-002.yaml):
`ACCEPT_WITH_NONBLOCKING_PROVENANCE_CLARIFICATION`.
The *exact reviewer archival condition is now met*, so the additive
[AS-ACTIVATION-002](reviews/diagnostics/CLN-001-TASK-003/AS-ACTIVATION-002.yaml)
records an **ACTIVE accepted diagnostic AS=(C,R,PS)** for the
**numeric latest-32 energy primitive only**. It does not approve
full sustained-energy detection, firmware, real hardware or
selected architecture, and it discharges no verification obligations.

The authoring workspace's stale `UNRESOLVED` self-review is separate
from the real first independent
`READY_FOR_HUMAN_QUESTIONS` review at
`e01f91177c20e14f3aea3a11d9025821156dd971`. This provenance
clarification is preserved in the additive decision rather than
rewriting the author's draft or either reviewer record. External
agent identity, physical filesystem isolation and connector
isolation were NOT authenticated.

**Next authorized diagnostic stage:** first fresh proof-opportunity
discovery and candidate Figure-of-Merit definition, using strictly
the newly accepted AS, original unsolved BKP, D001 and trace.
Read [STAGE3_HANDOFF](reviews/diagnostics/CLN-001-TASK-003/STAGE3_HANDOFF.md).
The human pulls this branch and runs the single
`prepare_stage3_workspaces.sh` script, which creates **both**
`~/archbot-cln001-proof-003` and
`~/archbot-cln001-fom-003` after source-pin checks. Run two
separate new Codex agents. Proof Scout produces **unproven**
candidate propositions; FOM analyst produces **draft** criteria,
not automatically approved F or an AP selection. No previous
Toy 1 solution, proof, F-001, AP, contracts, code, old decisions
or evaluator is supplied.

Still **pre-freeze diagnostic**, not formal FR-005/FR-006 cleanroom.
All T002 realization and detection obligations remain OPEN;
product target qualification, original Toy 1 VOs and AD-003
remain unaffected. Project-registry, submodules and multi-project
work remain parked. `main` remains untouched.

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
