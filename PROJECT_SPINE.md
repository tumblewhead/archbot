# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-002 continuity local evidence received; independent review next

Read the [machine-readable roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md) for complete
milestones and authority boundaries.

The user explicitly authorized the bounded cooperative
[FR-002 baseline-continuity replacement](process/decisions/FR002_BASELINE_CONTINUITY_REPLACEMENT-AUTHORIZATION-001.yaml).
Source was authored at `c23a31b93574cd71eb6f7cc6b65e1ee470b5a482`
and supplemented by a real second-project loader canary at
`44063ef971bcfd13e96c29eb5371e8fcc14e333a`.
The human's [local regression receipt](reviews/qualification/FR002_BASELINE_CONTINUITY-local-test-receipt.json)
was submitted in `44da84c263b54c8b5fcda3d9ea80bfd4109aa6ea`:
12 checks with zero exit codes and ten Git source identities that match the
tested source commit. Raw test logs are local; no independent review yet.

**Next authorized task:** independent `REVIEW_FR002_BASELINE_CONTINUITY-001`
with operation `REVIEW_BASELINE_CONTINUITY` and
[manifest](process/tasks/REVIEW_FR002_BASELINE_CONTINUITY-001.yaml)/
[playbook](process/playbooks/REVIEW_BASELINE_CONTINUITY.md).
The reviewer must test project-owned baseline continuity, prevention of
accidental C-002 omission, a truly usable reviewed transition path, Toy 1
negative controls, explicit simulation-vs-approval boundary, and a
second-project binding with no engine-owned project registry.

**Next human action:** pull, run the new route canary, inspect the manifest,
then launch a genuinely separate `verification-agent` review, or render
and perform the task inside an already separately invoked reviewer.
Commit/push only the new scoped report and receipt. The assistant then
inspects the actual verdict before suggesting FR-003 or a correction.

The original FR-002 independent `REVISE` review and older R1 source and
test receipt remain historical and unchanged. The hostile-forgery review
task `REVIEW_FR002_GATE_ADAPTER_R1-001` remains **paused**. The new
Toy 1 continuity projection remains `candidate_for_independent_review`
and cannot confer real product gate eligibility. FR-001 R1 remains accepted
with clarifications for role-context projection only.

The cooperative-audience assumption governs: preserve requirements and
reviewed authority transitions against accidental mistakes; do not
expand this review into hostile repository forgery or cryptographic
signing. FR-002 is **not independently accepted**. No freeze, cleanroom,
target qualification, AD change, final F-001, VO discharge or FR-003
implementation is authorized.

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
