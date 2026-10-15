# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: host VR-001 review received; prefreeze genericity audit next

User push `d0eb059d2d6d` contains the
[VR-001 independent resource review](reviews/gates/REVIEW_RESOURCE_EVIDENCE-TOY1-VR001-receipt.json).
The disposition is `ACCEPT_WITH_CLARIFICATIONS` **only for the
reported 72-byte host C99 ABI layout**: samples 64 B, oldest 1 B,
sum_squares 4 B and padding/overhead 3 B. The reviewer inspected the
source, reported layout output and hashes, but did not independently
recompile the layout probe. Its source commit and hashes were pinned;
the differing review checkout HEAD is recorded transparently.

**Unresolved process defect:** both
[VC-001 compiler review](reviews/gates/REVIEW_COMPILER_EVIDENCE-TOY1-VC001-receipt.json)
and VR-001 record failures of `python tools/task.py run` before any
registered Codex reviewer turn. Separately authored direct review reports
are not evidence of a successful nested runner. See
[review execution modes](docs/REVIEW_EXECUTION_MODES.md) for distinct
outer-shell launch vs current-agent direct execution; neither route is
yet qualified for cleanroom reproducibility by this documentation alone.
Do not conceal the original failures or relax sandbox controls.

The next assigned work is a **bounded prefreeze genericity audit**:
`process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml`, operation
`AUDIT_GENERICITY`, role `architecture-agent`, playbook
`process/playbooks/AUDIT_GENERICITY_PREFREEZE.md`. The audit is
authorized for *investigation only*, anchored to the latest review,
and must produce `reviews/qualification/GENERICITY_PREFREEZE_001-report.md`
and `reviews/qualification/GENERICITY_PREFREEZE_001-receipt.json`.
It cannot accept Toy 1, freeze the framework or launch a cleanroom.
Those outputs need a distinct independent review later.

**Next local action:** pull, run
`python -m unittest discover -s tests -p 'test_genericity_audit_route.py' -v`,
then `python tools/task.py inspect --manifest
process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml`. If already inside a
Codex agent invocation, use `python tools/task.py render --manifest ...`
and carry out that assigned audit within the **current** invocation.
Do not recursively invoke `task.py run`. From an outer host shell,
`run` remains the registered launcher if it actually works. Stage the
audit report and receipt selectively after inspecting their contents.

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
