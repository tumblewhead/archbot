# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VC-001 host review recorded; VR-001 resource probe ready

User commit `38e90e6dde80` submitted
[VC-001 independent compiler review](reviews/gates/REVIEW_COMPILER_EVIDENCE-TOY1-VC001-receipt.json)
with `ACCEPT_WITH_CLARIFICATIONS` **for host source/compiler evidence only**.
The reviewer checked the user-submitted raw hashes and negative-control
mismatch, independently reproduced a strict C99 `-O2` 8192-case host
correspondence run, and found source-level C arithmetic consistent
with the accepted legal-domain and valid-state assumptions.

**Important unresolved workflow defect:** the same review report records
that the registered `tools/task.py run` failed before any Codex reviewer turn.
The independent direct review report/receipt exists, but a formally successful
registered reviewer run does **not**. Do not claim the task runner passed or
erase the failure. The genericity audit must address this separately.

The user previously authorized follow-on source/compiler evidence and then
VO-002 resource evidence. [VR-001 operating guide](docs/TOY1_RESOURCE_EVIDENCE_VR001.md)
provides a host-only memory-layout probe, collector and regression test:
`implementation/toy1/resource_layout_probe.c`,
`tools/toy1_resource_evidence.py`, and
`tests/test_toy1_resource_evidence.py`.

**Next local action:** pull, run the regression, then the VR-001 collector
to record a host C99 `sizeof(detector_t)`/field-offset observation with a
versioned candidate JSON under `reviews/verification/`. Stage that
candidate selectively and push it. The accepted 7 charged-SRAM category
ceilings (1792 bytes total) and 256-byte reserve remain budget
commitments, **not measured target use**. The collector leaves all 7
measured target category peaks null and `target_status=NOT_REQUESTED`.
No target compiler/ABI, linker, task/ISR nesting or shared allocations
may be invented. A host object size does not close VO-002.

The earlier independently accepted [VK-001 MODEL_ONLY slice](docs/VK001_TERMINAL_CHECKPOINT.md)
remains unchanged. VO-002..VO-006 are OPEN, the 20 unplanned ERS claims
remain visible, and AD-003/final F-001 comparison are outstanding.
No AS/AP/F/CON/DE, selected firmware, accepted receipts or VOs were
modified. Once host resource evidence is available, choose actual
target/integration evidence or an explicit host-only qualification
limit, then genericity audit/freeze before a cleanroom Toy 1 replay.

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
