---
type: Resource Allocation Envelope
id: AP-001-SRAM-ENVELOPE-001
title: AP-001 detector-attributable SRAM envelope
status: draft
tags: [proposal, sram, envelope]
sources:
  - id: as
    resource: /architecture/AS-001/statement.md
    title: AS-001 requirements and C-002 limit
  - id: ap
    resource: /architecture/AS-001/proposals/AP-001.md
    title: Recompute candidate
  - id: scope
    resource: /architecture/AS-001/decisions/C-002-SCOPE-001.md
    title: Approved detector-attributable SRAM boundary
  - id: vp
    resource: /architecture/AS-001/verification_plan.md
    title: Staged verification plan
  - id: target
    resource: /bkp/target.md
    title: Hypothetical MCU resource assumption
  - id: adc
    resource: /bkp/adc.md
    title: Hypothetical ADC domain
relations:
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-001.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-002.md
---
# AP-001 proposal envelope (not a selection)

## Boundary and disposition

This is a proposed allocation ceiling under approved C-002-SCOPE-001: peak total detector-attributable SRAM, limit 2048 bytes. It is an allocation proposal, not measured consumption, a linker map, or a VO-002 discharge. **Conditional / unresolved pending contract authority and independent review:** the target's actual task, interrupt, stack, shared-memory and linker organization is unspecified. If the organization cannot be constrained to the caps below, this candidate remains unresolved. [^scope][^target]

## Categorized budget

| Charged category | Cap (bytes) | Basis and CON/DE enforcement |
|---|---:|---|
| Persistent algorithm state | 72 | 32 `uint16_t` samples (64 B), 32-bit accumulator (4 B), index/control allowance (4 B). CON-AP1-STATE fixes representation and ownership; DE-AP1-STATE checks `sizeof`, alignment, and static allocation. The 72 B is an estimate, not a compiler result. [^ap][^adc] |
| Temporary/scratch | 64 | Includes recompute accumulator if it is not already charged as persistent state, square/product temporaries, loop/index locals, and compiler spill allowance. CON-AP1-UPDATE caps explicit temporary objects; DE-AP1-UPDATE audits lifetimes and generated stack contribution. |
| Detector call/task stack | 384 | Proposed dedicated task stack cap, including detector call chain, locals, ABI/alignment and safety allowance; does not include separately dedicated interrupt stack. CON-AP1-TASK fixes task ownership and stack size; DE-AP1-STACK provides static call-depth analysis plus compiler stack-usage/map check. Unmeasured. |
| Detector-attributable interrupt context/stack | 128 | Dedicated, bounded interrupt stack/context cap for one detector sample-capture ISR; no nesting, no detector work in unrelated ISRs. CON-AP1-IRQ restricts ownership, priority/nesting and stack; DE-AP1-IRQ checks vector assignments, frame/stack bound and linker allocation. Unverified assumption. |
| Detector-attributable shared allocations | 128 | Cap for sample handoff/mailbox, synchronization state, and any shared buffer/control charged to detector. CON-AP1-SHARED names owner and maximum allocation; DE-AP1-SHARED inventories static objects and verifies no duplicate charge. |
| Bounded dynamic allocation | 0 | Proposed no-heap rule for detector and its callback/ISR path. CON-AP1-MEM forbids allocation after/before initialization; DE-AP1-MEM scans calls and link symbols for allocator use. If any allocator is required, this zero cap is invalid and candidate is unresolved until a bound is assigned. |
| Other detector-attributable SRAM | 128 | Cap for alignment/padding, DMA-visible staging or directly attributable control not listed elsewhere. CON-AP1-MEM requires inventory and ownership; DE-AP1-MEM accounts linker sections and padding. Whether DMA is needed is unknown; allowance is not evidence. |
| **Charged allocation ceiling** | **904** | Sum of category caps; simultaneous peak, with no category omitted. |
| **Positive reserved margin** | **1024** | Unallocated positive margin against the 2048 B ceiling. |
| **Total envelope** | **1928 / 2048** | Arithmetic only: 904 + 1024 = 1928 B, leaving 120 B unallocated beyond named reserve. |

### Overlap and concurrency model

The proposed organization is one periodic detector task, at most one sample-capture ISR at a time, no nested detector interrupt, and no concurrent detector instances. The task stack and dedicated interrupt stack are separate physical allocations, so both are charged independently even though execution is sequential; their maxima cannot coincide in time, but summing both is conservative. Persistent state, scratch, shared handoff memory, and any other allocated sections coexist and are summed. The 64 B scratch cap covers compiler temporaries/spills only when they are outside the 384 B task-stack cap; DE stack accounting must identify overlap and remove duplicate bytes from the category sum. IRQ-context frames physically on the dedicated IRQ stack are included only in the 128 B IRQ category, not task stack. No allocator pool is permitted. Unexpected nesting, recursion, DMA buffering, extra task instances, or shared-service growth violates this model until bounded and re-budgeted. [^scope]

The 1024 B reserve is a separately unallocated positive reserve; it is not a substitute for bounding any named allocation. Total maxima must satisfy `sum(non-overlapping charged maxima) + reserve <= 2048` at CON/DE review and implementation accounting. If overlap cannot be demonstrated, count both categories.

## F-001 state SRAM and work/flash

For F-001's **state-SRAM** dimension, the projected algorithm-owned persistent state is 72 B under the representation above. The 1928 B charged envelope is the distinct C-002 feasibility quantity; it must not be substituted for, or described as, the F-001 state-SRAM score. [^scope]

Work per update is bounded analytically by at most 32 sample-square operations and 32 accumulation additions plus bounded loop/index/control work, per AP-001. This bounds operation counts, not cycles or 1 ms WCET; timing remains subject to VO-004 target evidence. Flash bytes are unknown until a concrete implementation/toolchain build; no estimate or ranking is asserted. [^ap][^vp]

## Assumptions and open checks

- ADC input remains 0..4095 and zero-padded 32-sample history semantics hold. [^adc][^as]
- CON must adopt the proposed single task, dedicated stack, bounded non-nested ISR, no heap, and object ceilings; actual platform compatibility is not established.
- AP-001 still lacks candidate-specific accepted correctness/overflow evidence. This envelope does not discharge R-002 or R-003.
- No linker map, compiler stack report, binary, physical target, or measurements were inspected or created. VO-002 remains pending; other VOs remain governed by their existing records. [^vp]

[^as]: AS-001, `/architecture/AS-001/statement.md`.
[^ap]: AP-001, `/architecture/AS-001/proposals/AP-001.md`.
[^scope]: C-002-SCOPE-001, `/architecture/AS-001/decisions/C-002-SCOPE-001.md`.
[^vp]: VP-001, `/architecture/AS-001/verification_plan.md`.
[^target]: BKP-TARGET-001, `/bkp/target.md`.
[^adc]: BKP-ADC-001, `/bkp/adc.md`.
