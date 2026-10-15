# archbot project spine

Repository: `tumblewhead/archbot`. Read `AGENTS.md`, then the current checkpoint
and linked constituent artifacts. This spine is an index, not the execution log.

## Current checkpoint: FR-002 authority-root R1 correction authored

The original independent
[FR-002 review](reviews/qualification/REVIEW_FR002_GATE_ADAPTER_001-report.md)
and [receipt](reviews/qualification/REVIEW_FR002_GATE_ADAPTER_001-receipt.json)
were pushed at `eb5753a371632fbc093811b09a7c70bea458fc60`, with disposition **REVISE**.
The reviewer reproduced `FR002-AUTH-001`: weakening
`protected_scope_decisions`, recomputing the policy blob hash, and dropping
the validator was accepted by the old binding loader. It also identified
`FR002-AUTH-002`: the ROOT-002 baseline/review inputs were self-asserted
synthetic sources, not independently established authority. Prior review,
producer test receipts, and failure artifacts remain immutable.

The authorized FR-002 R1 candidate adds an **engine-owned authority root**
in `tools/gates/authority_roots.py` with the reviewed Toy 1 baseline,
independent reviews, AP reconfirmation authority, policy, active VO/AD
ledgers, C-002 scope and validator source identities. The corrected
`tools/gates/binding.py` rejects missing/untrusted projects or binding
pins inconsistent with this trusted source registry. The modified
`tests/test_gate_adapter.py` retains ROOT-002 as a *synthetic
mechanics-only* canary, not an authorized production gate, and adds
re-pinned policy/baseline/review/ledger attack tests.

**Status: authored but NOT locally executed and NOT independently
reviewed.** The human should pull and run the FR-002 R1 regression suite,
inspect actual failures/successes, and push a new evidence receipt.
A separate independent reviewer must then examine the engine-root
provenance and the re-pinning attacks. Registering a new trusted project
requires separately authorized changes to the engine root and independent
review. Git blob hashes are content identities, not signatures; an
untrusted party replacing engine code remains outside this bounded claim.

No generic engine freeze, cleanroom, target evidence, product acceptance,
final F-001 decision, VO discharge, AD modification or FR-003
implementation is authorized here. FR-001 R1 remains independently
`ACCEPT_WITH_CLARIFICATIONS` for telemetry projection only.

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
