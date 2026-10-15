# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-002 gate adapter candidate authored, local evidence next

The independent FR-001 R1 review
[report](reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-report.md)
and [receipt](reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-receipt.json)
remain `ACCEPT_WITH_CLARIFICATIONS` for telemetry role-projected context only.
Its earlier `REVISE` review remains immutable.

Engineering authority explicitly approved the bounded
[FR-002 gate adapter proposal](process/proposals/FR002_GATE_ADAPTER_001.yaml).
The [FR-002 authorization record](process/decisions/FR-002-GATE-ADAPTER-AUTHORIZATION-001.yaml)
controls implementation scope. The
[FR-002 authoring report](reviews/qualification/FR002_GATE_ADAPTER-authoring-report.md)
describes reusable AP mechanics, opt-in Toy 1 C-002 validation, a pinned
project gate-binding candidate, and new synthetic other-project tests.

**Status: source authored, local execution and independent review PENDING.**
The first FR-002 local `test_gate_adapter.py` run stopped with one failure
and one error. Source inspection identified a synthetic fixture bug:
`write_pinned()` omitted the policy document's `id` from the generated
pin, so `load_binding()` correctly rejected the artificial root-solver
policy before the intended assertions. A bounded test-only revision
preserves the identity key and adds a negative policy-ID control.
This revision has NOT yet been run locally, and no FR-002 test receipt was
created. Preserve the original failed log under `runs/fr002-gate-adapter/`.

The human's next action is to pull `main`, run the explicitly listed stage
gate, gate adapter, task and FR-001 regressions, inspect the explicit Toy 1
binding, and selectively push a versioned bounded test receipt. The assistant
will review pushed evidence and register a separate independent FR-002
implementation reviewer.

This change is NOT a freeze or cleanroom launch. The FR-002 code cannot
accept product evidence, discharge a VO, alter accepted C-002 scope, or
change the F-001 protected comparison. Keep earlier VC-001/VR-001 registered
launch failures preserved.

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
