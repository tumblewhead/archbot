# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: CLN-001 AS disposition issued; review archival pending

Stage-2 `AS-REV-002.md`, `DECISION-TRACE-002.md`, and
`BRIEFING-002.md` were archived on
`experiment/toy1-pipe-cleaner-001` at
`50abb5f57d4e049825bb565d53f477fc303d08dd`
with source blob identities and original SHA-256 manifest verified.

The user separately invoked the second diagnostic AS reviewer. Its
original two outputs were uploaded to the coordinator; actual verdict
**READY_FOR_DELEGATED_AS_DISPOSITION**, with no blocking technical
defects, and one **MINOR** finding on an earlier local self-review
provenance mismatch. The exact uploaded original REVIEW-002.md/json
hashes appear in
[REVIEW002_ARCHIVE_HANDOFF](reviews/diagnostics/CLN-001-TASK-002/REVIEW002_ARCHIVE_HANDOFF.md).
Those raw reviewer outputs **have not yet been committed in Git**.
Reviewer identity, full write/read history and host/connector isolation
are not independently authenticated.

The human experiment sponsor delegated *CLN-001 synthetic diagnostic
engineering decisions only* to this assistant via
[DECISION-001](reviews/diagnostics/CLN-001-TASK-001/DECISION-001.yaml).
The assistant inspected the uploaded reviewer evidence and issued
[AS-DISPOSITION-002](reviews/diagnostics/CLN-001-TASK-002/AS-DISPOSITION-002.yaml):
**ACCEPT_WITH_NONBLOCKING_PROVENANCE_CLARIFICATION** for only the
CLN-001 AS=(C,R,PS) numeric energy computation specification.
Its baseline **activation is conditional on original REVIEW-002.md
and REVIEW-002.json being Git-archived and matching the exact original
SHA-256/Git blob identities**. A user push plus remote verification
is the next action, not another review.

R3's nominal 1 ms arrival model is not a hard WCET deadline.
R4 whole-detector detection and threshold/duration criteria remain a
tracked uncompleted integration requirement. All T002 functional,
resource, timing and target-evidence obligations remain OPEN.
The stale `UNRESOLVED` self-review observed in the author's prior
workspace is distinct from the real first
`READY_FOR_HUMAN_QUESTIONS` review committed at
`e01f91177c20e14f3aea3a11d9025821156dd971`;
this distinction is recorded without editing author-era artifacts.

**Upon exact remote REVIEW-002 archive**, activate this diagnostic
baseline and proceed directly to fresh project proof-opportunity
discovery and symbolic Figure-of-Merit definition, not older solved
Toy 1 proofs, candidate AP or F-001. No selected AP, measured
implementation, complete detector, target/product verification,
legacy VO discharge, or formal cleanroom qualification is implied.
Keep project migration and multi-project work parked. Main untouched.

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
