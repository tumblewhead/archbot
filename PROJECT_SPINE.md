# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VR-001 host observation submitted; independent resource review next

User commit `96dcb745ae6f` contains the
[VR-001 host resource evidence](reviews/verification/TOY1-VO002-HOST-20261015T035845Z.json),
reporting an observed **72-byte host `detector_t`** object: 64 bytes for
`samples` at offset 0, one byte for `oldest` at offset 64, three bytes
of padding/overhead, and four bytes for `sum_squares` at offset 68.
It records successful host compilation and execution with matching
declared source pins and stable sources. The result is
`HOST_LAYOUT_RECORDED`; **not target SRAM, stack or product acceptance**.

The accepted C-002 charged-SRAM contract remains 2048 unique attributable
bytes: seven conditional category ceilings totaling 1792 and a 256-byte
reserve. All seven actual target category peaks remain `null`, the target
status is `NOT_REQUESTED`, and all VO-002..VO-006 remain OPEN.

**Next local action:** run
`process/tasks/REVIEW_RESOURCE_EVIDENCE-TOY1-VR001.yaml` using
`tools/task.py inspect` and `tools/task.py run`, after running
`test_toy1_resource_evidence.py`. The registered
`REVIEW_RESOURCE_EVIDENCE` playbook and task pin the submitted source
revision and evidence blob. A favorable host-only review can accept only
that observation; it cannot discharge VO-002 or establish physical fit.
The [VR-001 guide](docs/TOY1_RESOURCE_EVIDENCE_VR001.md) records the exact
handoff and target/integration omissions. Do not automatically route to a
target verification gate without an authorized target configuration.

The previous [VC-001 host compiler review](reviews/gates/REVIEW_COMPILER_EVIDENCE-TOY1-VC001-receipt.json)
reported `ACCEPT_WITH_CLARIFICATIONS` for a host-only finding, while
also recording a **registered Codex runner launch failure** before any reviewer
turn. The directly authored review is not proof that the runner succeeded.
Genericity audit must preserve and address this separate process defect.

The independently accepted [VK-001 model slice](docs/VK001_TERMINAL_CHECKPOINT.md)
also remains bounded. Twenty other ERS claims are unplanned. The active
AS/AP/F/CON/DE, detector implementation, VO/AD ledger and final F-001
comparison are unchanged. A complete target qualification or cleanroom
process freeze is not yet established.

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
