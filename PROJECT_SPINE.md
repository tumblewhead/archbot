# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: first CLN-001 conditional theorem independently reviewed

The CLN-001 synthetic energy primitive AS is accepted under
[AS-ACTIVATION-002](reviews/diagnostics/CLN-001-TASK-003/AS-ACTIVATION-002.yaml),
and its diagnostic three-axis F under
[F-DISPOSITION-003](reviews/diagnostics/CLN-001-TASK-004/F-DISPOSITION-003.yaml).
No target measurements or AP have been accepted.

The first separate Proof Engineer authored
[PROOF-ATTEMPT-004](reviews/diagnostics/CLN-001-TASK-004/PROOF-ATTEMPT-004.md)
at `2026cb251353285d8fe63671b9ce2b25c9fa9be6`.
The user then ran the independent proof reviewer, archived its
original REVIEW-PROOF-004.md/json and manifest at
`f255c662847378ac3df39b55c71e146a1f71cf7c`.
Reviewer verdict: **ACCEPT_WITH_CLARIFICATIONS**, no blocking
mathematical defect. Its report independently reconstructs
the crucial 31-zero-continuation recovery and state-distinguishability
proofs, with separately recorded finite checks.

The CLN-001 sponsor delegate records the scoped result in
[PROOF-DISPOSITION-004](reviews/diagnostics/CLN-001-TASK-004/PROOF-DISPOSITION-004.yaml):
**T1 ACCEPTED** for future **numeric** outputs under all
nonempty continuations iff padded 31-sample tails agree.
**T2 ACCEPTED CONDITIONALLY**: `2^372` distinguishable complete
retained states (at least 372 bits or 47 octets of information
capacity) at a fixed epoch length n>=32, assuming a complete
deterministic **no external replay/readback** information boundary
and unrestricted future continuations. This is **not**
a detector SRAM lower bound without ownership closure, nor
a sufficient 47-byte implementation, target fit or proof of
the full indexed output interface.

PO-003-1 and PO-003-3 remain **UNPROVEN**.
The finite-state unbounded-index issue in PO-003-3, external
publisher-history/replay ownership and permitted epoch length
must be analyzed before using T2 to qualify an architectural
candidate. No index wrap policy, AS amendment or AP is silently
adopted. All T002-2..8 and deferred R4 whole-detector detection
obligations remain OPEN.

**Next work is scoped applicability/interface clarification**:
decide what information is retained locally versus accessible
upstream, whether indices are externally supplied, and whether
epochs can be unbounded. The next AP author must not import
the old Toy 1 solution or treat conditional theorem applicability
as resolved. Current user goal includes learning the Git
workflow; no new Codex agent task has been launched yet.

This remains a **pre-freeze diagnostic**, not formal cleanroom
FR-005/FR-006. Real hardware, target memory/timing/power and
full detector remain unqualified. No old Toy 1 VO or architectural
debt is discharged, and dual-project/migration work stays parked.
`main` remains unchanged.

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
