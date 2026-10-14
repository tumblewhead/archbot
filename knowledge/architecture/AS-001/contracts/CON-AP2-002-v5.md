---
type: Design Contract
id: CON-AP2-002-v5
title: Exact rolling window and integer arithmetic obligations
status: draft
version: 5
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: assumes
    target: /architecture/AS-001/proofs/PE-001-v2.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v5.md
---
# CON-AP2-002 v5: Rolling state and update

The abstract state represents the latest 32 accepted legal samples, with
zeroes for absent startup history, and an accumulator equal to their exact
square sum. Initial state is all zero. For each accepted sample `x`, exactly
one transition evicts the oldest value, includes `x`, and restores the
oldest-slot convention for the next transition. The result after the
transition is the exact newest-32 sum. An invalid sample does not mutate this
state.

For each legal sample, `x^2 <= 16,769,025` and the resulting sum is at most
`32*4095^2 = 536,608,800`. The abstract proof also bounds an add-before-
subtract transient from a valid state by `33*4095^2 = 553,377,825`. These are
mathematical bounds; the implementation must use expression types and
evaluation order that prevent intermediate C overflow. In particular,
operand widening must occur before multiplication unless concrete integer
promotion rules prove the product safe. Range validation precedes squaring.

The abstract contract requires consistent initialization, oldest-slot
selection, one replacement, and one index advance per accepted sample,
including modulo-32 wrap. Concrete layout, exact C types, update ordering,
interrupt/task ownership, synchronization, and reset coordination remain
implementation obligations. No particular ring representation or
concurrency mechanism is mandated by this contract.

Theorem boundary: PR-002 accepts the mathematical recurrence and bounds under
its stated assumptions. C correspondence, actual expression promotions,
generated code, concurrency, and firmware correctness remain unproved.
