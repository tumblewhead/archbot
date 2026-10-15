# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-001 local tests pushed, independent review next

The human's [FR-001 local regression receipt](reviews/qualification/FR001_PROJECT_CONTEXT-local-test-receipt.json)
was pushed at `4ad7d1cb3121791c6258b90fbe93895a0a689164`. It records **six successful local check exit codes**
and hashes for locally retained logs (not included in this Git commit).
The candidate source remains at `42b19e7b64e65e8df34eeabc7b0631e8051f6312`.
These are **reported local tests**, not independent framework qualification.

**Next assigned task:** independent reviewer `REVIEW_FR001_PROJECT_CONTEXT-001`,
operation `REVIEW_FRAMEWORK_REPAIR`, role `verification-agent`,
[manifest](process/tasks/REVIEW_FR001_PROJECT_CONTEXT-001.yaml),
[playbook](process/playbooks/REVIEW_FRAMEWORK_REPAIR.md).
The task pins the test-evidence receipt by Git blob identity and all four
source/test files by their reviewed blob hashes. The reviewer must verify
the source SHA-256 values, inspect actual local logs if accessible or
independently reproduce checks, investigate cross-project negative controls,
and assess any manual telemetry/export incompatibility.

**Next local action:** pull `main`, run `python -m unittest discover -s tests -p
'test_fr001_review_route.py' -v`, inspect the review manifest, then start a
separate independent reviewer. From an ordinary **outer host shell**, use
`python tools/task.py run --manifest process/tasks/REVIEW_FR001_PROJECT_CONTEXT-001.yaml`.
If already inside a genuinely separate Codex reviewer invocation, use
`python tools/task.py render --manifest process/tasks/REVIEW_FR001_PROJECT_CONTEXT-001.yaml`
and perform the rendered review in that invocation. Do not claim
a successful runner or reviewer turn merely because a prompt rendered.
Check newly created `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_001-report.md`
and `reviews/qualification/REVIEW_FR001_PROJECT_CONTEXT_001-receipt.json`,
stage only those two outputs, then push.

The [human authorization record](process/decisions/FR-001-PROJECT-CONTEXT-AUTHORIZATION-001.yaml)
covers only the FR-001 source candidate. The earlier
[genericity independent review](reviews/qualification/REVIEW_GENERICITY_PREFREEZE_001-report.md)
accepted the audit only with clarifications. The
[cleanroom isolation proposal](docs/CLN_BOUNDARY_PREFREEZE_001.md)
remains unimplemented. No FR-002 source repair, framework freeze,
cleanroom, Toy 1 product acceptance, target selection, F-001 conclusion or
VO discharge has been authorized by these reviews.

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
