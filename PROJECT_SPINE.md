# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VC-001 host C evidence submitted; independent compiler review next

The user pushed `b3205bca0c74` with
[TOY1-VO003006-20261015T031625Z](reviews/verification/TOY1-VO003006-20261015T031625Z.json)
(`pc-toy1-c-evidence/v1`). The candidate records `HOST_PROBE_PASSED`,
successful host C99 `-O0`, `-O2`, and `-O2 -DNDEBUG` compilations
and executions of `detector.c` with the 8192-case shifted-queue
correspondence probe. The deliberately wrong `NDEBUG` reference
exited 1 as expected. All submitted source pins match the reviewed
implementation; no target compiler was requested (`NOT_REQUESTED`).
These are **user-local reported executions awaiting independent review**.
Raw stdout/stderr and binaries are held under ignored `runs/`; the
committed summary contains their hashes, not the full data.

The independently reviewed terminal [VK-001](docs/VK001_TERMINAL_CHECKPOINT.md)
MODEL_ONLY rung remains historical. The user explicitly authorized
subsequent VO-003/VO-006 source/compiler evidence collection, followed by
VO-002 resource evidence. The new
[VC-001 guide](docs/TOY1_C_COMPILER_CORRESPONDENCE_VC001.md)
describes the scope and source/build evidence boundary.

**Next local action:** pull and run the registered
`process/tasks/REVIEW_COMPILER_EVIDENCE-TOY1-VC001.yaml` using
`tools/task.py inspect` then `tools/task.py run`, after the new
`test_toy1_c_evidence.py` regression. The playbook is
`process/playbooks/REVIEW_COMPILER_EVIDENCE.md`. The review task
is pinned to the user's source revision and submitted evidence blob.
Record an independent Markdown report and JSON receipt under
`reviews/gates/`. Distinguish reviewed host behavior from any
unexecuted target or linked-build claim. Stop for review before
extending evidence collection.

VO-002, VO-003, VO-004, VO-005 and VO-006 remain OPEN. The 20 unplanned
ERS claims remain visible. Host C tests do not prove target/compiler
instruction behavior, actual SRAM/stack/nesting or publisher
continuity. The [VO-002 unmeasured inventory template](process/verification/toy1-vo002-inventory-template-v1.yaml)
is only a preparation for a separately grounded target/integration
campaign; no hardware values are invented. Existing accepted C/AS/CON/DE,
VO/AD states and final F-001 comparison are unchanged.

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
