# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 Stage-11 IF11 NEW feasibility evidence prepared

Stage-9 numerical evaluation at `0783a3b95a384e4e24b89a68740555055b2383f6`
was independently reviewed at `e5d2cfde2c856cc84192b294ac8c42a8746ba5aa`.
The independent Stage-10 report
[REVIEW-AP-EVALUATION-010](reviews/diagnostics/CLN-001-TASK-010/REVIEW-AP-EVALUATION-010.md)
returned `READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`: Stage-9
models and finite counterexamples were reproduced, **not** any
full physical AP. The Stage-10 HIGH unknowns are
`R010-4` consumer rank/debt/reset, `R010-5` unapproved
RN/C-HIST providers/ownership, and `R010-6` complete RAM,
compute and device-energy feasibility. Model C explicitly assumes
a perfect correct-event snapshot, not an accepted provider.
All realized H1–H6 and measured F coordinates remain UNKNOWN.

The CLN-001-only delegate separately issued
[AP-EVIDENCE-DISPOSITION-010](reviews/diagnostics/CLN-001-TASK-011/AP-EVIDENCE-DISPOSITION-010.yaml):
accept reproduced **finite model evidence only**, retain A/B/C
unselected, and authorize an evidence-producing next investigation
instead of another review of unchanged UNKNOWNs.

**Next eligible task:** [IF11 feasibility evidence task](reviews/diagnostics/CLN-001-TASK-011/TASK-IF11.md)
focused on real consumer-visible rank/reset/output-debt *information*
at a named hypothetical boundary and explicit missing contracts.
It must produce an independently reproducible trace program,
contract alternatives, conditional counterexamples and an
evidence-acquisition ledger, NOT an accepted interface or
AP selection. Read [Stage11 handoff](reviews/diagnostics/CLN-001-TASK-011/STAGE11_HANDOFF.md),
run [source-pinned preparation](reviews/diagnostics/CLN-001-TASK-011/prepare_if11.sh),
fresh Codex, then [restartable archive](reviews/diagnostics/CLN-001-TASK-011/archive_if11.sh).
Distinct independent review follows new evidence. Separate
NUM11 C numerical prototype and SVC11 provider inquiry may
be authorized/worked as further evidence tracks.

A process weakness was identified: excellent reviews can reproduce
the same UNKNOWN without creating decision-relevant evidence.
See versioned [progress retrospective and orchestration pilot proposal](docs/CLN001_PROGRESS_GAP_AND_ORCHESTRATOR_PILOT_001.md).
**Sequencing recommendation:** fix evidence progression in this
diagnostic now; continue CLN-001 through a defensible AP, CON, DE,
C and scoped verification; in parallel develop a controlled
deterministic orchestrator via offline receipt replay then a
bounded live demonstration; only after a usable baseline/pilot
run a distinct noncontaminated Toy1 and compare iteration time.
The general process-progress rule, orchestrator automatic execution/
push and fresh Toy1 restart are **NOT** activated by this note.

Current authority remains activated AS-REV-002 plus accepted
AS-ADDENDUM-008-R1, adopted F (RAM_peak, compute_effort,
device_energy_consumption), D002, scoped T1/conditional T2.
RI/RN/C-HIST, nonloss publisher pause, fixed epoch, forced reset
and mandatory acknowledgment are not supplied/approved.
T002-2..8 OPEN; R4 whole detection DEFERRED;
PO-003-1/3 UNPROVEN. No AP selected, CON/DE/C, framework freeze,
formal cleanroom, target/product qualification or old Toy1
VO discharge.

**Parked ideas:** [Process Orchestrator and Human Attention Contract](docs/PROCESS_ORCHESTRATOR_HUMAN_ATTENTION_PROPOSAL.md)
and [Goblin Graph BKP spine builder](docs/GOBLIN_GRAPH_SPINE_BUILDER_REUSE_NOTE.md)
are design proposals, not authorized framework implementations.
`theory_of_operation.md` now includes ERS, verification ladder
and human-briefing orchestration concept; its adaptive pieces are
not installed. No diversion into these tasks until separately
authorized; protect the user's Toy-1 progress.

This is **pre-freeze diagnostic**, not FR-005/FR-006 formal
cleanroom or qualified target. T002-2..8 and R4 sustained-energy
detector remain OPEN; no implementation/CON/DE/C, legacy Toy 1
VO discharge, AP selection, submodule or framework freeze. Main
untouched.

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
