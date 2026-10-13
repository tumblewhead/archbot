---
type: Resource Allocation Envelope
id: AP-002-SRAM-ENVELOPE-001
title: AP-002 detector-attributable SRAM envelope
status: draft
tags: [proposal, sram, envelope]
sources:
  - id: as
    resource: /architecture/AS-001/statement.md
    title: AS-001 requirements and C-002 limit
  - id: ap
    resource: /architecture/AS-001/proposals/AP-002.md
    title: Incremental candidate
  - id: scope
    resource: /architecture/AS-001/decisions/C-002-SCOPE-001.md
    title: Approved detector-attributable SRAM boundary
  - id: vp
    resource: /architecture/AS-001/verification_plan.md
    title: Staged verification plan
  - id: proof_review
    resource: /architecture/AS-001/proofs/PR-002.md
    title: Accepted abstract rolling-sum proof review
  - id: target
    resource: /bkp/target.md
    title: Hypothetical MCU resource assumption
  - id: adc
    resource: /bkp/adc.md
    title: Hypothetical ADC domain
relations:
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-002.md
---
# AP-002 proposal envelope (not a selection)

## Boundary and disposition

This is a proposed allocation ceiling under approved C-002-SCOPE-001: peak total detector-attributable SRAM, limit 2048 bytes. It is an allocation proposal, not measured consumption, a linker map, or a VO-002 discharge. **Conditional / unresolved pending contract authority and independent review:** actual task, interrupt, stack, shared-memory and linker organization is unspecified. If it cannot be constrained to the caps below, this candidate remains unresolved. [^scope][^target]

## Categorized budget

| Charged category | Cap (bytes) | Basis and CON/DE enforcement |
|---|---:|---|
| Persistent algorithm state | 72 | 32 `uint16_t` ring entries (64 B), 32-bit rolling sum (4 B), index/control allowance (4 B). CON-AP2-STATE fixes ring representation and ownership; DE-AP2-STATE checks size, alignment, initialization and static allocation. Estimate only. [^ap][^adc] |
| Temporary/scratch | 64 | Square operands/results, eviction/new-value temporaries, and spill/local allowance outside stack cap. CON-AP2-UPDATE limits explicit objects and lifetimes; DE-AP2-UPDATE audits data widths and compiler temporaries; duplicate stack-resident bytes must not be counted twice. PR-002 supplies mathematical bounds, not storage measurements. [^proof_review] |
| Detector call/task stack | 384 | Dedicated task stack cap including detector call chain, locals, ABI/alignment and safety allowance, excluding separately dedicated interrupt stack. CON-AP2-TASK fixes execution ownership and cap; DE-AP2-STACK supplies static call-depth analysis and compiler stack-usage/map check. Unmeasured. |
| Detector-attributable interrupt context/stack | 128 | Dedicated bounded context/stack cap for a single sample-capture ISR, no nesting and no detector work in unrelated ISRs. CON-AP2-IRQ specifies vector/priority/nesting/ownership; DE-AP2-IRQ checks actual frame and allocated stack. Unverified assumption. |
| Detector-attributable shared allocations | 128 | Cap for sample mailbox/handoff, synchronization/control, and other shared objects charged to detector. CON-AP2-SHARED names ownership and cap; DE-AP2-SHARED inventories objects and avoids duplicate charge. |
| Bounded dynamic allocation | 0 | No heap use in detector, update path or ISR. CON-AP2-MEM prohibits allocation; DE-AP2-MEM checks allocator references and allocation call graph. Any required pool makes this envelope unresolved until bounded. |
| Other detector-attributable SRAM | 128 | Cap for padding/alignment, optional DMA staging or other directly attributable sections not already counted. CON-AP2-MEM requires full inventory; DE-AP2-MEM checks map sections. DMA/platform need is unknown; budget cap is not evidence. |
| **Charged allocation ceiling** | **904** | Sum of category caps; simultaneous peak, no omitted category. |
| **Positive reserved margin** | **1024** | Separately unallocated positive margin. |
| **Total envelope** | **1928 / 2048** | 904 + 1024 = 1928 B, leaving 120 B beyond reserve. |

### Overlap and concurrency model

Assume one periodic detector task and at most one non-nested sample-capture ISR, no concurrent detector instances, and distinct task and IRQ stack allocations. Both stacks are included independently, conservatively, even though execution is sequential. State, handoff/shared memory and other static allocations coexist with scratch and are summed. Scratch is disjoint from the task stack only for objects not placed in stack; DE accounting must reconcile compiler stack reports and avoid counting any byte twice. IRQ frames are charged to the IRQ-stack category only. Heap is forbidden. Nested interrupts, recursive/callback execution, multiple instances, DMA staging beyond its cap, or shared-service growth invalidates the assumptions until re-budgeted. [^scope]

The reserve cannot offset an unbounded contributor. At each later gate, require `sum(non-overlapping charged maxima) + reserve <= 2048`; count both terms if overlap is uncertain.

## F-001 state SRAM and work/flash

F-001 **state SRAM** is projected at 72 B for the ring, rolling accumulator and index/control allowance, conditional on concrete representation. The 1928 B C-002 charged envelope is a different feasibility metric and is not the F-001 state-SRAM ranking value. [^scope]

The update has fixed bounded algorithmic work: one outgoing and one incoming square, one subtraction and one addition to the accumulator, one ring replacement, one index advance/wrap operation, and bounded control. The abstract proof establishes mathematical recurrence and bounds under its assumptions, not target cycles. VO-004 must establish deadline/WCET on target; no cycle claim is made. Flash bytes are unknown without a concrete compiler/build and are not ranked. [^ap][^proof_review][^vp]

## Assumptions and open checks

- Inputs are 0..4095; initialization, oldest-slot convention and one-step index advancement match PR-002's abstract model. [^adc][^proof_review]
- CON must enforce the proposed task/IRQ organization, no heap and caps; platform compatibility is not established.
- PR-002 does not discharge concrete source-to-C expression-width, synchronization, reset or resource obligations. VO-005/VO-006 and VO-002 remain open. [^vp][^proof_review]
- No firmware, linker map, compiler output, stack report, target measurement or flash measurement was inspected or created. [^target]

[^as]: AS-001, `/architecture/AS-001/statement.md`.
[^ap]: AP-002, `/architecture/AS-001/proposals/AP-002.md`.
[^scope]: C-002-SCOPE-001, `/architecture/AS-001/decisions/C-002-SCOPE-001.md`.
[^vp]: VP-001, `/architecture/AS-001/verification_plan.md`.
[^proof_review]: PR-002, `/architecture/AS-001/proofs/PR-002.md`.
[^target]: BKP-TARGET-001, `/bkp/target.md`.
[^adc]: BKP-ADC-001, `/bkp/adc.md`.
