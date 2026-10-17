# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: first fresh Toy 1 AS submitted; independent diagnostic review next

The human created an external pre-freeze diagnostic workspace from
the original three synthetic Toy 1 BKP inputs and ran a fresh Codex
architecture agent. The produced artifacts were submitted on branch
`experiment/toy1-pipe-cleaner-001` at
`57c49628dfca12e30315eb7b08f63c478379cc68`:

- [AS-DRAFT-001](reviews/diagnostics/CLN-001-TASK-001/AS-DRAFT-001.md)
- [QUESTIONS-001](reviews/diagnostics/CLN-001-TASK-001/QUESTIONS-001.md)
- [BRIEFING-001](reviews/diagnostics/CLN-001-TASK-001/BRIEFING-001.md)
- [source/run notes](reviews/diagnostics/CLN-001-TASK-001/RUN-NOTES.md) and
  [SHA256SUMS](reviews/diagnostics/CLN-001-TASK-001/SHA256SUMS)

The authoring result stops at AS=(C,R,PS), records requirement
candidates and synthetic assumptions separately, raises specific
stakeholder-authority and timing questions, and does not claim
proof, selection, CON, DE or implementation. This is a useful
**first-stage authoring result**, NOT independent acceptance.

**Next handoff:** read
[REVIEW_HANDOFF](reviews/diagnostics/CLN-001-TASK-001/REVIEW_HANDOFF.md).
Human creates a *separate* reviewer workspace by positive allowlist:
three BKP files, three newly authored artifacts and generic
verification guidance only. Run a distinct Codex reviewer; it emits
`REVIEW-001.md` and `REVIEW-001.json`, then stop. Copy only those
reviewer artifacts back to the experiment branch. A favorable
source-fidelity review opens **human requirements disposition**;
it does not automatically approve AS or permit downstream stages.

**Important remaining limitation:** The author's run notes record
filesystem/runtime isolation **NOT INDEPENDENTLY VERIFIED**.
Earlier `cleanroom_pipe_cleaner.py inspect` reported the initial
allowlisted package intact; that does not establish the agent could
not access host paths, connections or prior memory. This remains a
**pre-freeze diagnostic, not FR-005 qualification or a formal
cleanroom result**.

**Work intentionally parked:** multi-project experiments,
project-registry independent review, Toy 1 submodule migration,
and the legacy task/gate root refactoring. The registry's local
producer tests were pushed in `a6bb262e609dfeb609616e895a3925358d2dffd3`,
but no independent registry acceptance was declared. Preserve
original Toy 1 accepted records and all historical review receipts.

**Formal milestones unchanged:** FR-004 reviewer-mode qualification,
FR-005 positive-allowlist isolation, FR-006 integrated freeze,
and a separately authorized real cleanroom replay. Toy 1 final
F-001 is outstanding, no target selected, AD-003 unresolved,
VO-002..VO-006 open. No VO/AD authority was altered here.

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
