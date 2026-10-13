---
type: Design Contract
id: CON-AP2-003
title: AP-002 execution, concurrency, and resource boundary
status: draft
version: 1
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
# CON-AP2-003 v1: Execution and resource accounting

## Execution model

The provisional AP-002 envelope assumes one periodic detector task, one sample-capture ISR, no nesting of that detector ISR, no recursive or callback execution into detector state, and no second detector instance. The ISR may capture and hand off a sample but does not update the rolling state. The task is the sole state writer. Any platform arrangement that cannot enforce these assumptions requires an AP-002 envelope/contract review before decomposition proceeds.

Interrupt priority/vector, scheduler policy, queue depth, atomic publication primitive, and concrete fault channel are not specified by current source evidence. They are unresolved integration inputs. DE-AP2-TASK and DE-AP2-IRQ must document and verify them before implementation approval. No claim is made that a hypothetical Cortex-M target supplies these facilities as assumed.

## C-002 allocation contract

Under approved C-002-SCOPE-001, unique detector-attributable peak SRAM is capped at 2048 bytes. Every byte belongs to one category exactly once; simultaneous peaks are summed, while exclusive reuse requires evidence of nonoverlapping lifetimes. Shared bytes use documented conservative attribution. No unbounded contributor is allowed.

| Category | Maximum bytes | Owner / evidence responsibility |
|---|---:|---|
| Persistent state | 72 | DE-AP2-STATE: object layout and static allocation |
| Temporary/scratch outside task stack | 64 | DE-AP2-UPDATE: lifetime and overlap reconciliation |
| Detector task stack | 384 | DE-AP2-TASK: call depth, ABI, compiler stack/map evidence |
| Detector-attributable interrupt context/stack | 128 | DE-AP2-IRQ: single non-nested ISR frame and stack evidence |
| Detector-attributable shared allocations | 128 | DE-AP2-SHARED: mailbox, synchronization and publication inventory |
| Detector-attributable dynamic allocations | 0 | All DEs: no heap and allocator call-graph scan |
| Other detector-attributable SRAM | 128 | DE-AP2-MEM: complete map/section inventory, including any DMA |
| **Allocated ceiling** | **904** | Sum of category maxima |
| **Reserved positive margin** | **1024** | Must remain unallocated |
| **Envelope total** | **1928 / 2048** | 120 bytes remain beyond reserved margin |

The 72-byte persistent-state estimate is distinct from F-001 state-SRAM ranking. Caps are contractual allocations, not measured physical use. If any category cap, no-heap rule, non-nesting rule, single-writer rule or positive reserve cannot be enforced, mark this contract unresolved and reopen the affected CON/DE/AP commitment. VO-002 remains open through implementation pending map, stack/interrupt and shared allocation evidence.

## Verification and debt

DE owners supply static allocation inventory, stack and interrupt analysis, shared-byte attribution, and evidence that all simultaneous live allocations fit the envelope. The verification-agent reviews the 1 ms bound with target-specific interrupt load and margin at TARGET_VALIDATION (VO-004). AD-003 remains accepted and due before final acceptance; this contract neither resolves it nor claims final F-001 ranking.
