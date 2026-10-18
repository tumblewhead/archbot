# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 Stage-9 independent AP feasibility evaluation prepared

The focused Stage-8 R1 independent review was pushed at
`698c162e624df0faab640ef294a1bea63997981e`. Its
[report](reviews/diagnostics/CLN-001-TASK-008/REVIEW-AS-ADDENDUM-008-R1.md)
and [JSON receipt](reviews/diagnostics/CLN-001-TASK-008/REVIEW-AS-ADDENDUM-008-R1.json)
returned `READY_FOR_DELEGATED_AS_ADDENDUM_DISPOSITION`. Original
Stage-8 `REVISE_AS_ADDENDUM` evidence is preserved. R008-3 was
independently resolved for exact R1 bytes: reset acknowledgment
is optional, while consumer-visible order/old-new sequence
association and stale-output nonaliasing are required. Reviewer
reported 18/18 current-source matches and six finite test groups;
OS/connector separation and target feasibility were NOT verified.

The CLN-001-only sponsor delegate has **separately accepted** the
[AS-ADDENDUM-008-R1-DISPOSITION](reviews/diagnostics/CLN-001-TASK-009/AS-ADDENDUM-008-R1-DISPOSITION.yaml)
for this synthetic diagnostic. This activates additive R1
*observable interpretation* while preserving original D001 and
the activated AS-REV-002 source unchanged. Physical RI, RN, C-HIST,
publisher backpressure, retry/recovery and any specific reset
protocol remain unapproved. Exact `n` must be decodable by the
actual consumer from available accepted-event/reset information,
not omniscient trace rank; fault reports do not complete an
accepted output obligation; no material weakening or added
universal recovery guarantees are adopted.

**Next eligible task: Stage-9 independent AP feasibility evaluation**
of unselected A (raw 31-tail + recompute), B (squared 31-tail +
incremental total) and C (prospective upstream exact snapshot),
under accepted [evaluation scope](reviews/diagnostics/CLN-001-TASK-009/AP-EVALUATION-SCOPE-009.yaml)
and [task](reviews/diagnostics/CLN-001-TASK-009/TASK-AP-EVALUATION-009.md).
Read the [human pull-run-push handoff](reviews/diagnostics/CLN-001-TASK-009/STAGE9_HANDOFF.md);
run [source-pinned preparation](reviews/diagnostics/CLN-001-TASK-009/prepare_ap_evaluation009.sh),
start a fresh separate Codex evaluator and use
[restartable exact-evidence archive](reviews/diagnostics/CLN-001-TASK-009/archive_ap_evaluation009.sh).
The evaluation may produce independent finite numeric-model and
typed symbolic F evidence, candid unsupplied service/physical
index/debt and ownership matrix, and falsifiers, but **NO AP SELECTION**.
Its outputs will need a **distinct Stage-10 independent evaluation review**
before a separate possible AP commitment.

All realized H1–H6 remain UNKNOWN until eligible evidence establishes
otherwise, as do measured F values
(`RAM_peak`, `compute_effort`, `device_energy_consumption`).
T1 future-numeric equivalence and conditional T2
`2^372` complete-state capacity are not physical index or
sufficient RAM proofs. T002-2..8 remain OPEN, R4 full sustained
detection deferred. No AP selection, CON/DE/C, legacy Toy1
VO discharge, target/product qualification, formal cleanroom
or framework freeze is authorized.

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
