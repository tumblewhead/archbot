# AP-stage SRAM envelope preparation receipt

## Claims and supporting artifacts

- [AP-001 envelope](../knowledge/architecture/AS-001/proposals/envelopes/AP-001-SRAM-ENVELOPE-001.md) proposes a 1,928 B charged envelope against the 2,048 B C-002 limit, including 904 B categorized caps and a separate positive 1,024 B reserve.
- [AP-002 envelope](../knowledge/architecture/AS-001/proposals/envelopes/AP-002-SRAM-ENVELOPE-001.md) proposes the same whole-subsystem ceiling and reserve, with candidate-specific state and scratch assumptions.
- Both distinguish the projected 72 B F-001 state-SRAM value from charged C-002 allocation feasibility; both give bounded operation models and leave cycle/WCET and flash unresolved.
- Both depend on a proposed single detector task, distinct bounded task and interrupt stacks, one non-nested sample ISR, no heap, and capped shared/other allocations. Platform compatibility and enforcement are not verified. Thus both envelopes remain conditional/unresolved pending independent review and CON adoption; neither establishes C-002 feasibility or selects an AP.

## Inspected evidence

Read AGENTS.md, `agents/architecture-agent.md`, architecture-agent context view, root theory, AS-001 spine/statement, F-001, AP-001/AP-002, VP-001 and VO-001 through VO-006, PR-002, EP-002 and its receipt, approved C-002-SCOPE-001, `docs/AE003_GATE.md`, AP_SELECTION_v2, the memory-envelope template and prompt 14. The approved Option B boundary and 2048 B ceiling informed category coverage. Existing conceptual buffer representations informed the algorithm-state estimates.

## Uninspected evidence

No raw data, target, firmware, concrete task/ISR configuration, allocator call graph, declarations, compiler output, linker map, stack analysis, SRAM use, timing or flash measurements were available or inspected. No external measurement or compiler evidence was created. Structural validation is not semantic review.

## Unresolved obligations

VO-002 remains pending: the proposed task/interrupt and allocation caps require contract authority, later CON/DE enforcement, implementation accounting and independent acceptance. VO-001's separate accepted receipt requirement from AE-003 is not addressed or discharged here. AP-001 candidate-specific correctness/overflow evidence remains absent; AP-002 concrete correspondence to PR-002 remains open. VO-003 through VO-006 remain governed by their existing records. C-002 envelopes do not modify AS/F, discharge any VO, or establish F-001 ranking. Flash and cycles remain unknown.

## Suggested next gate

Independent review the two envelope models and assumptions. Then establish CON ownership and caps for each category, with DE allocation/stack/map checks and explicit concurrency/overlap accounting. Keep AE-003 disposition separate; do not infer a selection from these proposals or from `pc.py check`.
