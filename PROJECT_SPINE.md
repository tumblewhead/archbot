# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: ERS002 independently accepted; rung planning next

User commit `9737d44d6631` contains the revised ERS bundle at
[TOY1-VERIFY-ERS002](reviews/verification/TOY1-VERIFY-ERS002/receipt.json)
and its independent
[REVIEW_ERS-1a1accbb740a](reviews/gates/REVIEW_ERS-1a1accbb740a-receipt.json).
Disposition: **ACCEPT_WITH_CLARIFICATIONS**. The
[review report](reviews/gates/REVIEW_ERS-1a1accbb740a-report.md) resolves
F-ERS-001 and F-ERS-002 for ERS coverage, reports 21 requirements/21 claims,
and records matching artifact integrity and all 31 source pins. These are
reported independent-review results, not tests executed by this assistant.

The clarification preserves the distinction between conditional SRAM category
commitments, proposed DE accounting assignments, and actual target feasibility.
VO-002 through VO-006 remain OPEN. This accepts the ERS projection for the next
scoped activity, not product behavior, target qualification or VO discharge.
The original draft artifact's PENDING field remains historical authoring state;
its separate review receipt supplies the disposition. Do not edit accepted bytes.

**Next local action:** use `tools/next_task.py inspect/emit --receipt
reviews/gates/REVIEW_ERS-1a1accbb740a-receipt.json` to generate
`DESIGN_VERIFICATION_LADDER`, inspect/run that task, then read its generated
`reviews/verification/<task-id>/briefing.md`. Route that plan's submission
receipt through the existing `REVIEW_VERIFICATION_LADDER` operation. Do not
execute the ladder before favorable independent plan review.

The accepted ERS currently supplies one candidate rung, ARITHMETIC-MODEL-BOUND,
targeting only ERS-CON-ARITH-BOUNDS with a MODEL_ONLY binding. The deterministic
planner validates that candidate and records the remaining claims in
`unplanned_claim_ids`; it does not generate a complete target campaign. No missing
method may be silently represented as a passed or inapplicable claim. Whether
this bounded plan is adequate for its declared next activity is for independent
plan review. No new kernel, role, playbook or routing change is needed to launch.

## VK-001 implementation and limits

Read [VK-001 operating guide](docs/VERIFICATION_SLICE_VK001.md). Its three author
operations use a shared deterministic kernel and pc-verification/v1. Independent
reviews use local Codex. The initial planner validates explicit model/rung
candidates; it does not discover arbitrary physics. Model evidence cannot
discharge a product VO. The interactive human interface is not installed;
structured briefings/questions are emitted now. The ERS bundles record local
authoring, and their reviews record scoped checks. They do not establish that
all fixture demos or the complete regression suite passed; consult actual run
evidence before making those claims. This assistant has not run those tests.

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
Neither that repair nor its acceptance changes product requirements or firmware.

Roadmap: finish Toy 1, genericity review/freeze, cleanroom Toy 1 without the future
dialogue interface, add dialogue, replay Toy 1 with it, then Toy 2 and increased
novelty/scale. VK-001 is the first runnable slice, not completion of that campaign.
