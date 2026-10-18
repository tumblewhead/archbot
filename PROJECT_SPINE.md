# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 independent Stage-6 AP review prepared

The user-sponsored, **CLN-001-only** synthetic diagnostic has an
accepted scoped AS/F, D001 and D002, and mathematical T1 plus
conditional T2. The latter's `2^372` state requirement applies
only to a deterministic complete retained-information no-replay
boundary with unrestricted futures, **not** automatically to
detector SRAM. Full event-index implementation and theorem
applicability to actual resources remain unresolved.

The fresh Proposal Agent authored three **unselected**
alternatives, pushed at
`65ba5bf74347b28464e0ac610eea160bc131971f`:
[AP-CANDIDATES-006](reviews/diagnostics/CLN-001-TASK-006/AP-CANDIDATES-006.md),
[AP-COMPARISON-006](reviews/diagnostics/CLN-001-TASK-006/AP-COMPARISON-006.md)
and [AP-BRIEFING-006](reviews/diagnostics/CLN-001-TASK-006/AP-BRIEFING-006.md)
with output hashes. AP A retains local raw-tail samples and
recomputes; AP B retains local squares plus an incremental sum;
AP C requires prospective publisher-owned history readback.
A/B's RI event-rank index interpretation and C's RN external
numeral service are **not** yet accepted physical-interface
contracts. All H1..H6 candidate gates and realized RAM,
compute, device-energy costs are UNKNOWN. No AP selected.

**Next eligible task: independent source and candidate-quality
review of AP-006-A/B/C**, not a winning AP decision:
[TASK-REVIEW-AP-006](reviews/diagnostics/CLN-001-TASK-006/TASK-REVIEW-AP-006.md)
and [AP_REVIEW_HANDOFF](reviews/diagnostics/CLN-001-TASK-006/AP_REVIEW_HANDOFF.md).
Human pulls the experiment branch and executes
[prepare_ap_review006.sh](reviews/diagnostics/CLN-001-TASK-006/prepare_ap_review006.sh),
which CREATEs `~/archbot-cln001-ap-review-006` with
source-pinned BKP/AS/D001/D002/F/proof and only the three new
AP drafts. A fresh, separate Codex reviewer writes
`REVIEW-AP-006.md` and `REVIEW-AP-006.json`. Human runs
restartable
[archive_ap_review006.sh](reviews/diagnostics/CLN-001-TASK-006/archive_ap_review006.sh)
from its real Git checkout to preserve and selectively push
raw reviewer output. Then source-specific AP evaluation or
revision may be authorized, separately from selection.

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
