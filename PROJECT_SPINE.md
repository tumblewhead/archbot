# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-002 local checks pushed, independent review next

The human's [FR-002 regression receipt](reviews/qualification/FR002_GATE_ADAPTER-local-test-receipt.json)
was pushed in `c0cc00658c9afdc3eea111905b131a272d87863c`. It records nine local checks with exit code zero,
including the corrected synthetic gate adapter fixture, Toy 1 stage-gate
negative tests and bound/legacy inspection. Source revision
`3c2fd85cb0bde0c13b7639e24220143e26344536` contains the original
FR-002 implementation at `57f69f5b2d8d69de876aa72649e8aa5f783ef4e9`
and a fixture-only correction. Producer logs remain local. These are
**reported local tests**, not independent acceptance.

**Next authorized task:** independent `REVIEW_FR002_GATE_ADAPTER-001`,
operation `REVIEW_GATE_ADAPTER`, role `verification-agent`;
[manifest](process/tasks/REVIEW_FR002_GATE_ADAPTER-001.yaml) and
[playbook](process/playbooks/REVIEW_GATE_ADAPTER.md).
The manifest pins the new evidence and seven source/test Git blobs.
The reviewer must challenge validator omission, synthetic project
isolation, and especially **authority laundering**: self-consistent
hashes alone do not make a re-pinned policy or review approval.

**Next local action:** pull `main`; run
`python -m unittest discover -s tests -p 'test_fr002_review_route.py' -v`
and inspect the manifest with `python tools/task.py inspect --manifest
process/tasks/REVIEW_FR002_GATE_ADAPTER-001.yaml`. From an outer host
shell use `python tools/task.py run --manifest
process/tasks/REVIEW_FR002_GATE_ADAPTER-001.yaml`. From a distinct
already-running Codex reviewer, `render` the manifest and actually
execute the review in that existing invocation instead of nesting Codex.
Only after review results exist, inspect, selectively stage and push the
new `REVIEW_FR002_GATE_ADAPTER_001` report and receipt.

FR-001 R1 remains independently `ACCEPT_WITH_CLARIFICATIONS` for
role-projected context only. The previous FR-002 fixture failure remains
historical and the corrected receipt does not erase it. No framework
freeze, cleanroom, product verification, target configuration, final F-001
resolution, VO discharge or AD change follows from these checks.

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
