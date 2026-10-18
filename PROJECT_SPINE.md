# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 Stage-10 independent AP evaluation review prepared

Stage-9 independent evaluation results were archived at
[commit 0783a3b](https://github.com/tumblewhead/archbot/commit/0783a3b95a384e4e24b89a68740555055b2383f6):
[evaluation](reviews/diagnostics/CLN-001-TASK-009/AP-EVALUATION-009.md),
[structured receipt](reviews/diagnostics/CLN-001-TASK-009/AP-EVALUATION-009.json),
[human briefing](reviews/diagnostics/CLN-001-TASK-009/AP-EVALUATION-BRIEFING-009.md)
and checksum manifest. Its independently authored finite models
**reported** 299,296 accepted transitions, 24,192 invalid attempts,
11,386 explicit resets, 897,888 A/B/C oracle energy comparisons
with zero correct-model mismatches. This is Stage-9 *author*
evidence, not independent verification of those counts. C's model
explicitly assumes a truthful immutable exact-event snapshot service,
and neither C-HIST nor RN exists as accepted external capability.

Stage 9 reported 21 witness groups: 20 refuting defective shortcuts
and one permitting permutation of a correct current term set.
An unprotected snapshot read was wrong at 31 of 32 tested
interleavings for its chosen trace. The evaluator disclosed a
preliminary wrong-age witness that failed to discriminate a fault;
it corrected that witness and reported only the completed rerun.
These findings warrant exact **independent replay and scope review**.

The **accepted synthetic AS** is activated AS-REV-002 plus separately
reviewed and [delegated-accepted additive R1](reviews/diagnostics/CLN-001-TASK-009/AS-ADDENDUM-008-R1-DISPOSITION.yaml).
The additive clarification requires exact `n` decodable by the
actual consumer, one owed output per accepted valid event and
consumer-visible reset ordering/nonaliasing, but no mandatory
acknowledgment. It does not approve RI, RN, C-HIST, queue/retry
guarantees, finite epochs, backpressure, target hardware or an AP.
Accepted T1 is future numeric equivalence only; conditional T2
complete-state capacity does not imply physical-index feasibility
or a sufficient 47-byte detector allocation.

**Next eligible task:** a **distinct independent Stage-10 evidence
quality review**, not AP downselection. Read
[Stage-10 handoff](reviews/diagnostics/CLN-001-TASK-010/STAGE10_HANDOFF.md)
and [review task](reviews/diagnostics/CLN-001-TASK-010/TASK-REVIEW-AP-EVALUATION-010.md).
The human runs
[source-pinned preparation](reviews/diagnostics/CLN-001-TASK-010/prepare_ap_evaluation_review010.sh),
starts NEW independent Codex (not resume), and
[restartably archives raw MD/JSON review](reviews/diagnostics/CLN-001-TASK-010/archive_ap_evaluation_review010.sh).
The review must check the source receipt, reproduce or bound
numeric program claims, inspect counterexamples, gate status and
compatibility of F/resource comparisons, and report residual
dependencies without choosing an architecture.

Only following actual favorable reviewed evidence may the
CLN-001-only delegate make a **separate AP evidence disposition**;
the gate does NOT require immediate provisional AP commitment.
All realized H1–H6 and measured `RAM_peak`,
`compute_effort`, `device_energy_consumption` remain UNKNOWN.
A/B/C remain UNSELECTED; T002-2..8 all OPEN, R4 full detector
DEFERRED, PO-003-1/3 UNPROVEN. No CON/DE/C, historical Toy1 VO
discharge, target/product qualification or formal cleanroom.

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
