# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: R1 regression evidence pushed, independent correction review next

The original [FR-001 independent review](reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_001-report.md)
returned **REVISE** at `8e58c2607dbab9e64668f6f4728b543070387ad6`.
It documented three unresolved counterexamples: FR001-R1 symlink alias,
FR001-R2 alternate-collection traversal, and FR001-R3 missing mandatory
dependency. That historical verdict **remains unchanged**.

A targeted FR-001 R1 correction was authored at
`e0ef748b70c29b6c802b325aab0afaa4d8b4ecd7`, followed by the
historical review pin test correction at
`3dc5f6ec854971243877f5d7357c7ca034880539`.
The human's [R1 regression receipt](reviews/qualification/FR001_PROJECT_CONTEXT_R1-local-test-receipt.json)
was pushed as `8d06dc3dd87db0c244ed72dc5cc1a69702c573dd`. It records **seven successful local commands**
and source SHA-256 fingerprints, with raw logs held locally. These are
reported test outcomes, not independent implementation acceptance.

**Next assigned gate:** `REVIEW_FR001_PROJECT_CONTEXT_R1-001`,
operation `REVIEW_FRAMEWORK_REPAIR_R1`, role `verification-agent`,
[task manifest](process/tasks/REVIEW_FR001_PROJECT_CONTEXT_R1-001.yaml)
and [review playbook](process/playbooks/REVIEW_FRAMEWORK_REPAIR_R1.md).
The manifest pins the new R1 evidence, the source revision and all five
source/test blobs, without rebinding original FR-001 historical pins.

**Next local action:** pull `main`; run
`python -m unittest discover -s tests -p 'test_fr001_r1_review_route.py' -v`;
`python tools/task.py inspect --manifest process/tasks/REVIEW_FR001_PROJECT_CONTEXT_R1-001.yaml`;
then from an ordinary host shell invoke
`python tools/task.py run --manifest process/tasks/REVIEW_FR001_PROJECT_CONTEXT_R1-001.yaml`.
Inside a *separate existing* Codex reviewer invocation, `render` the task
and actually conduct the review without launching nested Codex.
Publish only the resulting
`reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-report.md`
and `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_R1_001-receipt.json`
after checking real outputs.

The earlier review failure and runner limitations are preserved. No
FR-002 implementation, framework freeze, cleanroom execution, target
selection, Toy 1 product acceptance, F-001 final conclusion or VO discharge
is authorized here.

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
