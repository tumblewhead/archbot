# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-003 independent REVISE; focused correction next

Read [the machine-readable roadmap](process/roadmaps/PC_ROADMAP_CURRENT.yaml)
and [qualification campaign](docs/QUALIFICATION_CAMPAIGN.md).
FR-001 and FR-002 are independently accepted only with their stated
clarifications; Toy 1's continuity projection is still a candidate,
and VO-002..VO-006 and final F-001 remain outstanding.

The [FR-003 independent report](reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-report.md)
and [receipt](reviews/qualification/REVIEW_FR003_HISTORICAL_INTEGRITY_001-receipt.json)
were pushed in `f33cd51bddc3c415293899d0350b469e67403823`: **REVISE**, not acceptance.
Reviewed source: `66b75a2a3720bca32f13b430a26715da8477641f`;
human producer evidence: `040400394e030c7898de66aa3bd1a3648f8e3555`.
The reviewer independently reran 87 unit tests, confirmed all nine
source identities and fourteen local-log fingerprints, and observed
`HISTORICAL_MATCH` with later-worktree correspondence `DIFFERENT`
and `present_applicability=NOT_EVALUATED`.

**Only blocking defect:** `FR003-REVIEW-FINDING-001`. A JSON-escaped
lone surrogate (U+D800) in a source path passes `path_ref` then raises
uncaught `UnicodeEncodeError`, instead of bounded `UNRESOLVED`.
A narrow correction is authorized under existing FR-003 source scope:
reject non-UTF-8-encodable paths or catch encoding failure, add one
negative regression, then obtain fresh human tests and distinct review.
Do not rewrite the original `REVISE` receipt or call the code accepted.

**Strategic priority after this small correction:** accelerate toward
the actual proof-of-use. FR-004 should qualify the reviewer execution
mode the process promises, without demanding two modes for symmetry.
FR-005 should demonstrate an independently checked, positive-allowlist
fresh-agent bootstrap from unsolved inputs. FR-006 is a separate
integrated framework-freeze review. A practical end-to-end cleanroom
Toy 1 demonstration is the milestone, not an unlimited succession of
metadata/edge-case audits. This is prioritization guidance, **not**
authorization to skip existing stage gates or launch cleanroom early.

The cooperative-audience operating assumption applies. The source-time
auditor's digest result is not review approval or product correctness.
No FR-004 implementation, framework freeze, cleanroom, target selection,
accepted AD change, final F-001 decision or VO discharge is authorized.

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
