# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 conditional theorem accepted; Stage-5 interface applicability next

The human sponsor delegated CLN-001 **synthetic diagnostic** engineering
authority to the assistant, not real product or generalized process
authority. The scoped AS and F remain accepted:
[AS-ACTIVATION-002](reviews/diagnostics/CLN-001-TASK-003/AS-ACTIVATION-002.yaml)
and [F-DISPOSITION-003](reviews/diagnostics/CLN-001-TASK-004/F-DISPOSITION-003.yaml).
All RAM/compute/device-energy realization values are UNKNOWN.
No AP has been selected.

The first separate Proof Engineer's attempt and distinct mathematical
review were archived at
`2026cb251353285d8fe63671b9ce2b25c9fa9be6` and
`f255c662847378ac3df39b55c71e146a1f71cf7c`.
The independent review returned **ACCEPT_WITH_CLARIFICATIONS**.
[PROOF-DISPOSITION-004](reviews/diagnostics/CLN-001-TASK-004/PROOF-DISPOSITION-004.yaml)
records **T1 accepted**: exact future NUMERIC output equivalence
iff padded ordered 31-tails agree (all nonempty continuations).
**T2 accepted conditionally**: at fixed n>=32, a deterministic
complete retained-information no-replay machine needs at least
`2^372` distinguishable states (372 bits or 47 whole octets
of information capacity). This is not a 47-byte implementation
or an unconditional detector-local SRAM bound. The indexed
interface was not part of T1. PO-003-1 and PO-003-3 remain UNPROVEN.

**Next eligible project task:** [TASK-INTERFACE-005](reviews/diagnostics/CLN-001-TASK-005/TASK-INTERFACE-005.md).
The accepted AS permits upstream ownership of acquisition memory,
but neither the ability to reread prior samples nor a no-replay
contract is yet established. It calls for a logically exact
`(n,E_n)` pair, but does not assign a finite-implementation
index owner, epoch lifetime or overflow policy. Stage-5 analyst
must compare alternative information boundaries and index
interpretations, trace conditional T2 applicability, and create
a D002 **PROPOSED_NOT_APPROVED** decision with exact consequences,
without silently amending the AS or choosing AP.

The user pulls the branch and runs
[prepare_interface005.sh](reviews/diagnostics/CLN-001-TASK-005/prepare_interface005.sh)
from the real Archbot checkout to CREATE
`~/archbot-cln001-interface-005`, then launches a fresh
Codex analyst. Read
[STAGE5_HANDOFF](reviews/diagnostics/CLN-001-TASK-005/STAGE5_HANDOFF.md).
After its three outputs appear,
[archive_interface005.sh](reviews/diagnostics/CLN-001-TASK-005/archive_interface005.sh)
copies and pushes original evidence with safe restart behavior:
existing identical files and previously staged intended outputs
are recognized. The next independent review and delegated D002
disposition are separate gates.

R4 full sustained-energy detector and T002-2..8 remain OPEN.
This is **pre-freeze diagnostic**, not formal FR-005/FR-006
cleanroom, hardware qualification or original Toy 1 VO
discharge. Historical accepted Toy 1 solution remains excluded
from fresh-agent packages. Framework/submodule work parked;
`main` unchanged.

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
