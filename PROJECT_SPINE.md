# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 Stage-12 independent review of NEW IF11 evidence prepared

The IF11 evidence producer's five outputs, archived at
[1baf0d1](https://github.com/tumblewhead/archbot/commit/1baf0d1fc03c67fc181341e8f53dac9011581c52),
include [executable trace model](reviews/diagnostics/CLN-001-TASK-011/IF11_TRACE_MODEL.py),
[feasibility dossier](reviews/diagnostics/CLN-001-TASK-011/IF11_FEASIBILITY.md),
[structured author receipt](reviews/diagnostics/CLN-001-TASK-011/IF11_RECEIPT.json)
and [human briefing](reviews/diagnostics/CLN-001-TASK-011/IF11_BRIEFING.md).
The author reports 14,327 successful finite-model cases, a
one-error deliberately mutated 256-bit rank wrap and 16 input hashes.
These are author claims pending distinct independent reproduction.

**New engineering information:** two conditional consumer
refinements, S (ordered success/reject and retained rank context)
and X (explicit sequence/ordinal frames from hypothetical provider),
expose different lifetime/storage/provider dependencies. IF11's
`2^m` distinguishable unpaid-result transcripts at a fixed final
numeric state/rank give a potential conditional `>=m` retained-bit
bound when all accepted results remain owed during arbitrarily long
stalls, with no outside information, storage/replay or flow control.
This is a *new unreviewed conditional claim*, not accepted theorem
or whole-AS impossibility. Real publisher/consumer/ordinal service,
C-history service, full interface and target resources remain UNKNOWN.

**Next eligible task:** [Stage-12 independent IF11 review task](reviews/diagnostics/CLN-001-TASK-012/TASK-REVIEW-IF11-012.md).
Use [source-pinned preparation](reviews/diagnostics/CLN-001-TASK-012/prepare_if11_review012.sh),
a fresh independent Codex reviewer, then [exact-byte archive](reviews/diagnostics/CLN-001-TASK-012/archive_if11_review012.sh).
Read [Stage-12 handoff](reviews/diagnostics/CLN-001-TASK-012/STAGE12_HANDOFF.md).
Review MUST independently replay source and challenge the exact
conditional claims. This is review of NEW evidence, **not another
assessment of identical prior UNKNOWNs**. A favorable disposition
allows a separate CLN-001 delegate decision and concrete implementation
or provider/consumer evidence task, not immediate AP acceptance.

The [progress/orchestration retrospective](docs/CLN001_PROGRESS_GAP_AND_ORCHESTRATOR_PILOT_001.md)
remains a proposal: finish current CLN-001 end-to-end as baseline,
pilot deterministic orchestrator separately (offline receipt replay,
then bounded live execution), and conduct a separately isolated fresh
Toy1 replay to measure iteration speed/human minutes. No autonomous
orchestrator, generic progress policy or new cleanroom has been activated.

Current authority: original activated AS-REV-002 plus accepted
AS-ADDENDUM-008-R1, D002, three-axis F, scoped T1/conditional T2.
All A/B/C unselected; all fully realized H1–H6 and measured F
remain UNKNOWN. T002-2..8 OPEN, R4 sustained detector deferred,
PO-003-1/3 UNPROVEN. No CON/DE/C, external service approval,
formal cleanroom, target/product qualification or old Toy1 VO discharge.

## Parallel evidence prototype and roadmap improvement (not active Stage-12 authority)

**EGM Goldfish research input captured:** A
[byte-preserved user research note](docs/research/EGM_ELEPHANT_GOLDFISH_USER_NOTE_20261028.yaml)
(`archbot_research_note/v1.0`, Elephant–Goldfish Model) proposes
testing architecture **serialization/deserialization** rather than
treating every fresh review as an adequate handoff. The Elephant
explores, the accepted spine/OKF/CON/proof/ERS graph serializes,
and a truly fresh Goldfish reconstructs requirements, ownership
and dependencies without conversational context. A private,
independently source-grounded evaluator reference checks whether
implementation-critical facts and proof conditions survive the
boundary; a structural match cannot itself prove semantic accuracy
or authority. See the
[bounded EGM design](docs/EGM_GOLDFISH_SERIALIZATION_001.md),
[typed EGM roadmap](process/roadmaps/EGM_GOLDFISH_001.yaml)
and [offline structural checker/tests](experiments/egm_serialization/README.md).
The user reported **10/10 EGM-P0 unit tests passed**, including
three distinct structural-checker CLI exits, preserved as
[P0 local test observation](experiments/egm_serialization/P0_USER_TEST_REPORT_001.json).
This is user-reported local test evidence, **not independent review,
source/semantic qualification or a fresh-agent experiment**.
A first [P1 source-pinned Goldfish package](experiments/egm_serialization/p1/README.md)
has been authored on this work branch, with a compact
[spine](experiments/egm_serialization/p1/SPINE.md), independent
[reconstruction task](experiments/egm_serialization/p1/TASK_GOLDFISH.md),
positive-allowlist [preparer](experiments/egm_serialization/p1/prepare_p1.sh)
and evaluator-only [reference](experiments/egm_serialization/p1/REFERENCE.json).
The reference is a **provisional author draft** requiring independent
source-grounded validation. The P1 worker has NOT been launched; no
runtime isolation, semantic comparison or generic gate approval
is claimed. The next EGM-specific action is a
[focused independent P0 checker and P1 answer-key review](experiments/egm_serialization/p0_review/README.md),
with source-pinned preparer, independent reviewer, and restartable
original-output archive. The EGM pilot's current target is source
recoverability, not implementation correctness or a changed
protected Stage-12 IF11 gate.
The proposed EGM-INV-1/2/3 and mandatory fresh-Goldfish gates are
not active policy. Source-pinned Goldfish reconstruction is a
potential pre-code check of whether an independent implementer can
produce the previously proposed **S0 linkable skeleton**; implementation
still requires its own authority. The CLN-001 Stage-12 IF11 review
remains the next formal gate.

**New implementation-method direction, captured in the roadmap:** begin
every authorized implementation at an **S0 linkable skeleton**
containing the planned modules, exact public signatures, port and
integration boundaries, and build/link configuration, *before* filling
in application logic. Save an initial linker map, symbol/cross-reference
inventory, section placement (`.text`, `.rodata`, `.data`, `.bss`),
memory-region ownership and explicit stack/peak-memory unknowns.
Then populate a single reviewed contract/DE at a time, relinking
and measuring size/dependency deltas. A linked stub is a structural
milestone, **not** evidence of functional compliance. Where
instructions and constants are SRAM-resident, include them in
the SRAM budget. See the user-directed
[implementation skeleton-first protocol](docs/IMPLEMENTATION_SKELETON_FIRST_001.md),
its [proposed IMPLEMENT_DE playbook amendment](process/playbooks/IMPLEMENT_DE.md),
and the [CLN001 typed roadmap](process/roadmaps/CLN001_PROGRESS_AND_HARNESS_001.yaml).
The generic process amendment is on the work branch pending review.
Existing A/B and FLOW-002 prototypes were **not** created in
skeleton-first order and must not be represented otherwise.

**FLOW-002 newly executed host evidence:** An additional
[finite publisher/consumer C flow witness](experiments/cln001/integration_c/README.md)
uses a one-sample offered input slot and one accepted-but-unreceived
result, orders commit/receipt, defers reset through debt settlement,
and keeps pre-reset offered (not accepted) samples for admission after
the reset marker. GCC 14.2 optimized and ASan/UBSan runs each returned
zero with 55,775 accepted events per A/B model. Exact checked source
bytes and initial oracle off-by-one correction are in
[FLOW-RESULT-002.json](experiments/cln001/integration_c/FLOW-RESULT-002.json).
**This is bounded conditional evidence, not a working physical ADC
publisher:** a second offer returns BUSY; upstream lossless staging
and retry are unsupported. The consumer's rank state is hypothetical
and retained, the 64-bit rank exhausts, publication/receipt is assumed
atomic and actual reset/restart/pending-output recovery is not tested.
All fully realized H1–H6 remain UNKNOWN; independent evidence review
is pending, and the original Stage-12 IF11 review is not replaced.

A separately branched exploratory C experiment and bounded S
synchronous interface witness are authored at
[experiments/cln001/integration_c](experiments/cln001/integration_c/README.md)
with an [author-executed host test receipt](experiments/cln001/integration_c/EXPERIMENT-RESULT-001.json).
The source bytes passed optimized GCC and sanitizer host runs in the
assistant's container; no local Cortex-M/target test or independent
review has occurred. A's 31 raw samples and B's 31 squares plus
sum are implemented as fixed-width C numeric kernels with independent
32-slot oracle tests. The S caller is explicitly bounded: its
`uint64_t` ordinal/sequence eventually exhaust, it has no
real asynchronous publisher or owed-result queue, and **cannot be
claimed full-AS compliant**. Full H1-H6 remain UNKNOWN and A/B/C
unselected. The experiment does not start protected CON/DE/C.

The previously identified **review-without-evidence-progress defect**
is now referenced by the actual central
[roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml), its
[typed companion](process/roadmaps/CLN001_PROGRESS_AND_HARNESS_001.yaml),
and original [retrospective](docs/CLN001_PROGRESS_GAP_AND_ORCHESTRATOR_PILOT_001.md).
A separate human design request `ARCHBOT-HARNESS-ARCHITECTURE-001`
is reflected in a
[bounded offline open-source harness architecture proposal](docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md),
including D01-D05 design drafts: artifact-first, nonlinear entry,
deterministic authorized mutation, provenance, durable worker replay,
composable spines and human intervention. It is **not**
a deployed orchestrator, changed process authority or a new
cleanroom Toy1 run.

The original experiment branch and its next Stage-12 independent
IF11 evidence review remain untouched and necessary. The parallel
prototype and harness design require separate review before any
adoption or merge.

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
