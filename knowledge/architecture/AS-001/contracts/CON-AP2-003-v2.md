---
type: Design Contract
id: CON-AP2-003-v2
title: AP-002 execution, concurrency, and resource boundary
status: draft
version: 2
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: specifies
    target: /architecture/AS-001/proposals/envelopes/AP-002-SRAM-ENVELOPE-001.md
---
# CON-AP2-003 v2: Execution and resource accounting

## Execution model

The provisional AP-002 envelope assumes one periodic detector task and at most one non-nested sample-capture ISR; the ISR hands off sample plus sequence metadata and a persistent, acknowledgeable overrun indication, but never updates rolling state. The task is sole state writer. There is no recursion/callback into state and no second detector instance. Queue capacity, vector/priority, scheduler policy, synchronization primitive and concrete fault channel remain target DE choices, but must enforce CON-AP2-001 continuity, atomic publication and the bounds below before implementation approval. An arrangement unable to enforce them leaves this contract unresolved.

## C-002 allocation contract

C-002-SCOPE-001 caps unique detector-attributable peak SRAM at 2048 bytes. Each byte belongs to one category once; simultaneous peaks are summed; exclusive reuse requires lifetime evidence; shared bytes use documented conservative attribution. No unbounded contributor is allowed.

| Category | Maximum bytes | Owner / evidence |
|---|---:|---|
| Persistent state | 72 | DE-AP2-STATE; exact field inventory in CON-AP2-002 v2, layout evidence pending |
| Temporary/scratch outside task stack | 64 | DE-AP2-UPDATE; reconcile lifetimes and stack placement |
| Detector task stack | 384 | DE-AP2-TASK; call depth, ABI, compiler/map evidence |
| Detector-attributable interrupt context/stack | 128 | DE-AP2-IRQ; one non-nested ISR frame and stack evidence |
| Detector-attributable shared allocations | 128 | DE-AP2-SHARED; includes handoff, the 32-bit expected-sequence value and its initialized flag, persistent overrun indication, publication value/sequence/status and synchronization; inventory each object once |
| Detector-attributable dynamic allocations | 0 | All DEs; no heap and allocator-call scan |
| Other detector-attributable SRAM | 128 | DE-AP2-MEM; full map/section inventory including DMA |
| **Allocated ceiling** | **904** | Sum of category maxima |
| **Reserved positive margin** | **1024** | Must remain unallocated |
| **Envelope total** | **1928 / 2048** | 120 bytes remain beyond reserve |

Caps are allocations, not measured use. If any cap, no-heap rule, non-nesting rule, single-writer rule or reserve cannot be enforced, this contract is unresolved and affected commitments reopen. VO-002 remains open pending map, stack/interrupt, shared and attribution evidence.

## Verification and debt

DE owners provide static allocation inventory, stack/interrupt analysis and shared-byte attribution. Verification-agent reviews target 1 ms WCET and margin under interrupt load (VO-004, TARGET_VALIDATION). AD-003 remains accepted and due before final acceptance. This contract does not resolve it or claim final F-001 ranking. VO-002 through VO-006 remain open; no authority or acceptance state changes.
