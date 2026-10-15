# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VK-001 authored, local qualification pending

The user approved a bounded end-to-end implementation of ERS derivation, rung
planning and model-evidence execution after VS-001/VS-002. The first slice is
implemented, but its new regression tests have **not been run by the assistant**.
Read [VK-001 operating guide](docs/VERIFICATION_SLICE_VK001.md).

The three author operations use a shared deterministic kernel. Their independent
reviews use the existing task/receipt mechanism and local Codex. Inputs, stages,
source fingerprints, project scope and result limitations use pc-verification/v1.
The initial planner validates explicit model/rung candidates; it does not discover
arbitrary physics. Model evidence cannot discharge a product VO. The interactive
human interface is not installed; structured briefings/questions are emitted now.

**Next local action:** run the full Python suite and structural checker, exercise
ring/queue/statistical fixture demos, then run
`process/tasks/TOY1-VERIFY-ERS001.yaml` and read its generated briefing. Commit the
ERS artifact/receipt/task outputs, not ignored raw runs. Independent ERS review
comes next; planning and execution each retain separate review gates.

## Current Toy 1 authority

- Active versions: `process/baselines/AS-001-v2-active.yaml`.
- Live VO index: `process/ledgers/vo_ledger-AS-001-v2-active.yaml`.
- Host-only independent C review:
  `reviews/gates/IMPLEMENT_DE-900da7a3ce8c-independent-review.json`.
- Implementation: `implementation/toy1/`, its Engineering Briefing and review request.
- No new product requirements, firmware changes or VO/AD dispositions in VK-001.
  VO-002 through VO-006 and AD-003/F-001 final evidence remain open as recorded.
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
instructions are history, not the current task. Existing source/authority artifacts
remain unchanged. The old task.py is likewise preserved as tools/task_legacy.py
while the new entry point adds one shared verification contract hook.

Roadmap: finish Toy 1, genericity review/freeze, cleanroom Toy 1 without the future
dialogue interface, add dialogue, replay Toy 1 with it, then Toy 2 and increased
novelty/scale. VK-001 is the first runnable slice, not completion of that campaign.
