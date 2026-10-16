# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-003 local tests submitted; independent review next

Read [the complete program roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md). FR-001 and
FR-002 remain independently `ACCEPT_WITH_CLARIFICATIONS` only within
their recorded scopes. FR-002's ROOT-002 protected-validator clarification
and unactivated Toy 1 candidate projection remain outstanding; accepted
product sources, VO/AD ledgers, and historical receipts remain unchanged.

The bounded FR-003 [authorization](process/decisions/FR003-HISTORICAL-INTEGRITY-AUTHORIZATION-001.yaml)
covers the read-only historical auditor, not source-time approval or
framework acceptance. FR-003 source revision
`66b75a2a3720bca32f13b430a26715da8477641f`
adds `tools/historical_audit.py` and 12 synthetic/real history canaries.
The human [local regression receipt](reviews/qualification/FR003_HISTORICAL_INTEGRITY-local-test-receipt.json)
was pushed at `040400394e030c7898de66aa3bd1a3648f8e3555`.
It **reports 14 successful checks**, with nine exact Git blob SHA-1
identities verified against the tested source revision. Log digest/size
declarations were inspected; raw logs are local. **FR-003 has not yet
passed independent review.**

**Next authorized task:** a distinct `verification-agent` review,
`REVIEW_FR003_HISTORICAL_INTEGRITY-001`, using
[manifest](process/tasks/REVIEW_FR003_HISTORICAL_INTEGRITY-001.yaml) and
[playbook](process/playbooks/REVIEW_HISTORICAL_INTEGRITY.md).
Review source-time versus current-file identity, historical-missing
`UNRESOLVED` behavior, exact revision/regular-file limits, and separate
review disposition without rewriting authoring `review_state`.

**Next local step:** pull latest `main`; run the new
`tests/test_fr003_review_route.py` canary and `tools/task.py inspect`;
then conduct the review in a genuinely separate invocation. From an
outer host shell use the registered `task.py run` launcher; within an
already independent Codex invocation use `task.py render` and actually
perform that review there. If completed, selectively publish only the
new report and receipt. The assistant must inspect the resulting verdict
before changing any milestone status.

Maintain cooperative-audience scope. Neither historical SHA matches,
current-file correspondence, nor an independent code-review disposition
can independently accept a project, close VOs, select a target or authorize
FR-004. The original current-state `verification_kernel.check_pins` and
`active_baseline.verify` remain unchanged. No framework freeze,
cleanroom, AD change, final F-001 decision or VO discharge is authorized.

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
