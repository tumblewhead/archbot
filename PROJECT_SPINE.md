# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: VC-001 source/compiler evidence collector authored, local runs next

The user explicitly authorized the proposed follow-on scope after the terminal
VK-001 bounded review: collect concrete Toy 1 VO-003/VO-006 source and compiler
correspondence evidence, followed by VO-002 charged-SRAM resource evidence.
This authorizes **evidence collection**, not product acceptance or VO discharge.

Read the [VC-001 source/compiler campaign](docs/TOY1_C_COMPILER_CORRESPONDENCE_VC001.md).
Installed additions:

- `implementation/toy1/correspondence_probe.c`: independent shift-queue host
  probe with 8192 legal accepted samples, reset/wrap, and a deliberately failing
  reference-only negative control that is not disabled by `NDEBUG`.
- `tools/toy1_c_evidence.py`: bounded host C99 compilation/execution and
  optional explicitly configured target object/assembly/disassembly collection;
  outputs hashed local logs plus a candidate evidence JSON. All generated
  results are **pending independent review**.
- `tests/test_toy1_c_evidence.py`: collector and resource-template tests.
- `process/verification/toy1-vo002-inventory-template-v1.yaml`: unmeasured
  accounting template with accepted 1792-byte category ceilings and 256-byte
  reserve under the 2048-byte cap. No target or integration measurements are
  invented.

**Next local action:** pull, run the new `test_toy1_c_evidence.py` regression,
then run the evidence collector with a unique `runs/` output and versioned
`reviews/verification/` summary as shown in the VC-001 guide. Review its
actual results and push the candidate summary. If a target compiler is not
available, collect bounded host evidence and keep target correspondence
unresolved; the optional target mode must not be guessed. Independent source,
toolchain and evidence review follows once actual output is available. VO-002
inventory follows with an explicitly selected target and integration context.

The completed [VK-001 terminal checkpoint](docs/VK001_TERMINAL_CHECKPOINT.md)
and [independent rung review](reviews/gates/REVIEW_VERIFICATION_RUNG-9de9286189ea-receipt.json)
remain authoritative for their MODEL_ONLY scopes. The 20 unplanned ERS claims,
VO-002..VO-006, AD-003 and final F-001 comparison remain open. No VK-001
source/evidence bytes, accepted AS/AP/F/CON/DE or firmware were modified.
The new collector is **outside** the terminal MODEL_ONLY operation set; it
creates no self-approved rung or automatically routable acceptance receipt.

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
