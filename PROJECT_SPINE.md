# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 delegated diagnostic authority; AS revision next

**Human delegation:** the human experiment sponsor explicitly stated
"ill empower you, and yes limited to this diagnostic project. We
already know what we want to end up with, we are just testing the
system." This grants ChatGPT assistant **synthetic requirements
decision authority for CLN-001 only**, not independent reviewer
authority, formal cleanroom approval or real product acceptance.

The prior fresh author produced [AS-DRAFT-001](reviews/diagnostics/CLN-001-TASK-001/AS-DRAFT-001.md),
[QUESTIONS-001](reviews/diagnostics/CLN-001-TASK-001/QUESTIONS-001.md)
and [BRIEFING-001](reviews/diagnostics/CLN-001-TASK-001/BRIEFING-001.md)
at `57c49628dfca12e30315eb7b08f63c478379cc68`, stopping
at initial C/R/PS. A separately invoked reviewer returned
**READY_FOR_HUMAN_QUESTIONS** in
[REVIEW-001.json](reviews/diagnostics/CLN-001-TASK-001/REVIEW-001.json)
pushed at `e01f91177c20e14f3aea3a11d9025821156dd971`.
This is source-fidelity/question readiness, not AS acceptance.
External reviewer independence and physical runtime isolation
were not authenticated.

**NEW synthetic requirements decisions:**
[DECISION-001.yaml](reviews/diagnostics/CLN-001-TASK-001/DECISION-001.yaml)
records the user-delegated role and new Q1-Q7 decisions. R1 latest-32
exact sum, R2 startup zeros and R6 no hardware FPU dependency are
adopted for this synthetic exercise. R3's ambiguous 1 ms statement is
**explicitly revised** to one logical result per accepted ordered
sample; nominal 1 ms arrival is a model assumption, not an invented
hard WCET deadline. R4's whole-detector decision is distinguished
from the current numerical primitive and remains a tracked deferred
integration obligation. Other decisions define synthetic SRAM scope,
init/reset, error boundary and publisher assumptions. These are newly
authored decisions under user delegation, **not imported historical
Toy 1 approvals**. This coordinating assistant knows the earlier
Toy 1 program; blinding applies to fresh author, not sponsor delegate.

**Next eligible task:** [TASK-002](reviews/diagnostics/CLN-001-TASK-001/TASK-002.md),
with [stage-2 handoff](reviews/diagnostics/CLN-001-TASK-001/DELEGATED_DECISION_HANDOFF.md).
Human copies only the new DECISION-001 and TASK-002 into the existing
isolated authoring workspace. The authoring agent creates
`AS-REV-002.md`, `DECISION-TRACE-002.md`, `BRIEFING-002.md`
and **stops before proof/AP/CON/DE/implementation**. These files
are new Stage-2 package inputs, so the frozen initial Stage-1
allowlist is not a valid post-transition PASS oracle. Preserve its
manifest and record new file digests separately.

After Stage-2 output, a distinct independent reviewer checks
source-decision fidelity; only then can the delegated decision
maker dispose the revised AS. No automatic acceptance is asserted
now. Keep previous source AS and all independent review receipts
untouched.

**Still parked:** dual projects, submodule migration, framework
polish and unrelated registry review. **Still unqualified:** formal
FR-005 cleanroom, FR-006 freeze, product/target evidence, final F-001,
VO-002..VO-006, AD-003. `main` and the old Toy 1 accepted project
remain unchanged.

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
