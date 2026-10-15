# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: bounded plan accepted; model-evidence execution next

User commit `cd431e0f7603` contains the plan bundle at
[DESIGN_VERIFICATION_LADDER-dedd836166b5](reviews/verification/DESIGN_VERIFICATION_LADDER-dedd836166b5/receipt.json)
and its independent
[REVIEW_VERIFICATION_LADDER-954fe316bda6](reviews/gates/REVIEW_VERIFICATION_LADDER-954fe316bda6-receipt.json).
Disposition: **ACCEPT_WITH_CLARIFICATIONS**. The
[plan review report](reviews/gates/REVIEW_VERIFICATION_LADDER-954fe316bda6-report.md)
records matching artifact integrity and 34 source pins, and independently
recomputes the conditional arithmetic bounds. These are reported reviewer
checks, not tests or experiments executed by this assistant.

The accepted plan contains only `ARITHMETIC-MODEL-BOUND`, targeting
`ERS-CON-ARITH-BOUNDS` using `window_integer_bound/v1` with window=32,
max_sample=4095 and bits=32. Its binding is MODEL_ONLY and maximum conclusion
is MODEL_EVIDENCE. F-PLAN-CLAR-001 explicitly keeps the other 20 ERS claims
unplanned/open. VO-002 through VO-006 remain OPEN. The plan is not a complete
verification campaign or evidence of C, target, integration or publisher behavior.

**Next local action:** use `tools/next_task.py inspect/emit --receipt
reviews/gates/REVIEW_VERIFICATION_LADDER-954fe316bda6-receipt.json` to generate
`EXECUTE_VERIFICATION_LADDER`; inspect/run the deterministic task and read its
`reviews/verification/<task-id>/briefing.md`. Route the execution submission
receipt through the existing `REVIEW_VERIFICATION_RUNG` operation for independent
review. Preserve unplanned claims, model scope and all open VOs. Stop at that
review for the next decision; it is terminal in the present VK-001 slice.
No new operation, kernel, model, schema, playbook or routing change is needed.

The generated PLAN artifact's PENDING field and inherited subject text are
historical authoring content; the separate review receipt supplies its acceptance
for this bounded activity. Do not edit accepted bytes to change their status.
No execution-evidence bundle was included in this push. Running the third stage
and reviewing its output remains outstanding.

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
