---
type: Design Contract
id: CON-AP2-002
title: AP-002 rolling state and exact update contract
status: draft
version: 1
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
# CON-AP2-002 v1: Rolling state and update

## Representation, ownership, invariant

DE-AP2-STATE exclusively owns a 32-entry ring of unsigned 16-bit sample values, a 32-bit unsigned rolling sum, an index in `0..31` naming the oldest slot, and initialization/control state. The AP-002 estimate is 72 bytes total for persistent state; this is an allocation cap, not measured object layout. State is statically allocated, single-instance, and single-writer. No heap allocation is permitted.

At every completed update, the ring in age order represents the newest 32 accepted samples (zero-filled history before startup completes), the index identifies the oldest slot, and the accumulator equals the sum of squares of all ring values. Therefore `0 <= sum <= 32 * 4095^2 = 536,608,800`.

## Reset and transition

Reset initializes every ring slot and the accumulator to zero, sets the oldest index to zero, clears valid-result and continuity-fault state, and starts the zero-padded history. For each legal accepted sample `x`, read `old` from the oldest slot, compute the exact squares, replace that slot with `x`, update the accumulator by removing `old^2` and adding `x^2`, then advance the index exactly once modulo 32. The completed transition is atomic with respect to readers and other mutations. No concurrent writer is permitted.

The C implementation must widen operands before multiplication (or establish an equivalent reviewed promotion guarantee); assignment to a wider result after a narrow multiplication is insufficient. `uint32_t` or a reviewed equivalent must hold each square, accumulator and intermediate. The mathematical one-update add-before-subtract transient is at most `33 * 4095^2 = 553,377,825`; state corruption and multiple unbounded additions are outside PR-002's theorem and must be detected or excluded by the implementation contract.

## Failure, timing, and resources

An invalid input does not change state. If an invariant check, sequence continuity check, or arithmetic range check fails, mark the result invalid, latch a bounded fault, and require reset/reinitialization before resuming valid publication. No floating-point operation or FPU reliance is allowed (C-003, VO-003, due IMPLEMENTATION; implementation-agent).

The update performs bounded constant work and must meet the 1 ms system deadline under the ingress/task contract; target evidence remains due under VO-004. Persistent state is capped at 72 B and update scratch outside stack at 64 B. Stack-resident temporaries are included in the task stack cap and must not be double-counted. The complete C-002 envelope is 904 B allocated ceilings plus 1024 B reserve, within 2048 B; these are commitments pending implementation evidence (VO-002, due IMPLEMENTATION).

## Proof and verification obligations

PR-002 accepts the abstract recurrence only under its legal input, zero initialization, oldest-slot, replacement and one-step index assumptions. VO-005 (R-002, verification-agent, IMPLEMENTATION) requires independent concrete correspondence review for representation, reset, indexing, synchronization and published results. VO-006 (R-003, proof-reviewer, IMPLEMENTATION) requires inspection of declarations, integer promotions, widening, range validation and invariant mapping. Required evidence: boundary/property tests over legal sequences, first 31 updates, all-zero/all-4095 windows and wraparound; static type/range review; independent review. Neither theorem acceptance nor these proposed tests imply C correctness.
