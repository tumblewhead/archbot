---
type: Design Contract
id: CON-AP2-002-v2
title: AP-002 rolling state and exact update contract
status: draft
version: 2
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: assumes
    target: /architecture/AS-001/proofs/PE-001-v2.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-002 v2: Rolling state and update

## Representation, ownership and complete persistent inventory (resolves CON001-F02)

DE-AP2-STATE exclusively owns one statically allocated 32-entry `uint16` ring, one 32-bit unsigned rolling sum, one 8-bit index in `0..31` naming the oldest slot, one 8-bit accepted-count in `0..32`, and one 8-bit packed control field. No heap, second instance or concurrent writer is permitted. The packed control field has named bits for `initialized`, `result_valid`, and `continuity_fault_latched`; remaining bits are reserved and must be zero. No other persistent state is permitted within this contract.

| Persistent field | Width | Bytes charged | Owner / lifetime |
|---|---:|---:|---|
| 32 ring entries (`uint16`) | 16 bits each | 64 | DE-AP2-STATE; static for instance lifetime |
| Rolling sum (`uint32`) | 32 bits | 4 | DE-AP2-STATE; static for instance lifetime |
| Oldest-slot index | 8 bits | 1 | DE-AP2-STATE; static |
| Accepted-sample count | 8 bits | 1 | DE-AP2-STATE; static |
| Packed control flags | 8 bits | 1 | DE-AP2-STATE; static |
| **Total persistent state** |  | **71** | Within approved 72-byte cap; 1 byte remains unallocated |

These are charged byte widths, not a claim about target object layout: implementation must verify `uint16`/`uint32` exact widths, alignment and padding and keep total persistent allocation <=72 bytes. No persistent publication copy, sequence counter, fault counter or hidden initialization field is included. Publication/result storage (including the 32-bit value, associated 32-bit sequence, valid/fault status and any synchronization object) belongs to DE-AP2-SHARED and is charged within the existing 128-byte shared-allocation cap in CON-AP2-003. It must not be charged again as persistent state. Temporary objects and stack-resident objects remain charged to their respective existing categories, without double counting.

At every completed update, ring order represents newest contiguous accepted samples with zero-filled prehistory, index names oldest slot, accepted count saturates at 32, and sum equals the squares sum of ring values. Thus `0 <= sum <= 536,608,800`.

## Reset and transition

Reset zeroes ring and sum, sets index/count to zero, sets initialized, and clears result-valid and continuity-fault-latched only as part of explicit recovery. For each legal, continuity-validated record, remove oldest square, add incoming square with operands widened before multiplication (or equivalent reviewed promotion guarantee), replace slot, advance index exactly once modulo 32 and update count. State transition is atomic with respect to readers and other mutations. Invalid input or continuity fault does not mutate the ring/sum and prevents valid publication until reset/reinitialization.

`uint32` or reviewed equivalent must hold each square, accumulator and intermediate. PR-002 bounds a one-update add-before-subtract transient from valid state by 553,377,825; corrupted state and multiple unbounded additions are outside its theorem and must be detected or excluded.

## Failure, timing, resources and obligations

No floating-point operation or FPU reliance (C-003, VO-003, IMPLEMENTATION). Update is bounded and must meet 1 ms under ingress/task contract; target evidence remains due VO-004. Persistent cap is 72 B (71 B inventoried); scratch outside task stack <=64 B. Full envelope remains 904 B allocation ceilings + 1024 B reserve = 1928 B within 2048 B, pending evidence (VO-002).

PR-002 assumptions remain binding. VO-005 requires independent concrete correspondence review of representation, reset, indexing, synchronization and publication. VO-006 requires inspection of declarations, promotions, widening, range validation and invariant mapping. Tests/reviews listed here are evidence plans, not completed evidence. Neither theorem acceptance nor this draft discharges any VO.
