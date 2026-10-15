# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: first ERS review requires inventory revision

User commit `830f91a98d4a` records the independent
[REVIEW_ERS-1d5aeec83447](reviews/gates/REVIEW_ERS-1d5aeec83447-receipt.json):
REVISE. F-ERS-001 identifies missing concrete C arithmetic/promotion/domain
facets; F-ERS-002 identifies missing conditional SRAM category, attribution and
implementation-evidence obligations. No product or firmware defect was declared.

[ERS revision 2](docs/ERS_REVISION_002.md) explains the versioned candidate repair.
`process/verification/toy1-input-v2.json` retains the original eight statements
and adds thirteen explicit CON/DE facets. Category ceilings and reserve remain
conditional commitments; DE subceilings remain accounting assignments; actual
C and target evidence remains open. The single model rung now targets only the
mathematical bound facet. No kernel, playbook, schema or firmware changes.

**Next local action:** run `process/tasks/TOY1-VERIFY-ERS002.yaml`, inspect its
briefing, then use `tools/next_task.py` on the newly generated
`reviews/verification/TOY1-VERIFY-ERS002/receipt.json` to launch independent
REVIEW_ERS. The previous bundle and review remain immutable. This new task has
not been run by the assistant. Planning still requires favorable ERS review.

## VK-001 implementation and limits

Read [VK-001 operating guide](docs/VERIFICATION_SLICE_VK001.md). Its three author
operations use a shared deterministic kernel and pc-verification/v1. Independent
reviews use local Codex. The initial planner validates explicit model/rung
candidates; it does not discover arbitrary physics. Model evidence cannot
discharge a product VO. The interactive human interface is not installed;
structured briefings/questions are emitted now. Generated ERS001 proves a local
authoring run occurred; no fixture-run evidence was included in that push.

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
review is retained under `reviews/gates/REVIEW_ERS-1d5aeec83447-*`.

Roadmap: finish Toy 1, genericity review/freeze, cleanroom Toy 1 without the future
dialogue interface, add dialogue, replay Toy 1 with it, then Toy 2 and increased
novelty/scale. VK-001 is the first runnable slice, not completion of that campaign.
