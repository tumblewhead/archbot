# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: Stage-3 draft proofs and F received; combined review next

The diagnostic AS-REV-002 was **accepted and activated for the
synthetic CLN-001 energy-computation primitive only** by the human
sponsor's scoped delegation, after the separate reviewer receipt and
its conditional disposition were archived. The additive activation
record is
[AS-ACTIVATION-002](reviews/diagnostics/CLN-001-TASK-003/AS-ACTIVATION-002.yaml).
This is not whole-detector, real-hardware or formal cleanroom
qualification; legacy Toy 1 obligations remain unaffected.

The human created the two fresh source-only Stage-3 author
workspaces and pushed their **four original outputs plus a SHA-256
manifest** at
`1f7645135581ede5696596ab8abc1034e75a53cd`:
[PO-OPPORTUNITIES-003](reviews/diagnostics/CLN-001-TASK-003/PO-OPPORTUNITIES-003.md),
[PO-BRIEFING-003](reviews/diagnostics/CLN-001-TASK-003/PO-BRIEFING-003.md),
[F-DRAFT-003](reviews/diagnostics/CLN-001-TASK-003/F-DRAFT-003.md),
[F-TRACE-003](reviews/diagnostics/CLN-001-TASK-003/F-TRACE-003.md).

**All three proof opportunities are UNPROVEN.**
PO-003-1 proposes 29-bit exact energy/output bound plus conditional
30-bit addition-first intermediate bound.
PO-003-2 proposes `2^372` distinguishable futures / a 31-sample
tail minimality result under a deterministic **no replay** model,
separate from full-interface output index.
PO-003-3 proposes conditional impossibility of indefinitely growing
internally generated exact logical indices from a closed finite-state
machine. The latter may reveal an AS-to-interface lifetime/ownership
question, not an unconditional AS contradiction.

**The F draft is NOT accepted.** It proposes H1–H6 hard gates and
`F=(RAM_peak,compute_effort,energy)`, with UNKNOWN measured costs
and a Pareto partial ordering. The first two optimization interests
trace to RAM/compute conservation; the *active energy coordinate* is
a new proposed choice, not stakeholder-granted objective authority.
R4 whole-detector detection is still deferred with open T002-8.

**Next:** [REVIEW003_HANDOFF](reviews/diagnostics/CLN-001-TASK-003/REVIEW003_HANDOFF.md)
runs one
[prepare_review003.sh](reviews/diagnostics/CLN-001-TASK-003/prepare_review003.sh)
script from the experiment-branch checkout to CREATE
`~/archbot-cln001-review-003` with only the pinned accepted AS,
original BKP/D001 and Stage-3 authored outputs. A distinct new
reviewer session follows
[TASK-REVIEW-003](reviews/diagnostics/CLN-001-TASK-003/TASK-REVIEW-003.md)
and emits four files: separate PO and F JSON/Markdown verdicts.
A review is not proof or F acceptance. After archival, the
CLN-001-only sponsor delegate considers F and independent Proof
Engineer task authorization.

Stale author-side self-review vs actual independent REVIEW-001
remain preserved in historical documents. Neither fresh source
allowlists nor a different `cd` establish OS/connector isolation.
This is still a **pre-freeze diagnostic**, NOT formal FR-005/FR-006.
No product verification, historical VO discharge, selected AP,
CON/DE/C, submodule migration or framework freeze is implied.
`main` stays untouched.

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
