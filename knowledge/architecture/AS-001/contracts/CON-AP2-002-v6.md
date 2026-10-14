---
type: Design Contract
id: CON-AP2-002-v6
title: Exact rolling window and integer arithmetic obligations
status: draft
version: 6
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: assumes
    target: /architecture/AS-001/proofs/PE-001-v2.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-002-v5.md
---
# CON-AP2-002 v6: Rolling state and update

The abstract state represents the latest 32 accepted legal samples, with
zeroes for absent startup history, and an accumulator equal to their exact
square sum. Initialization and reset establish all-zero state. For each
accepted sample `x`, exactly one transition evicts the oldest value, includes
`x`, and restores the oldest-slot convention for the next transition. The
result associated with completion of the transition is the exact newest-32
sum.

For each legal sample, `x^2 <= 16,769,025`, the resulting sum is at most
`32*4095^2 = 536,608,800`, and an add-before-subtract transient from a valid
state is at most `33*4095^2 = 553,377,825`. These are mathematical bounds;
the implementation must use expression types and evaluation order that
prevent intermediate C overflow. Operand widening must occur before
multiplication unless concrete integer promotion rules prove the product
safe. Legal-domain enforcement needed to protect squaring is an
implementation obligation under VO-006; this contract does not define
behavior for out-of-domain inputs.

The abstract contract requires consistent initialization, oldest-slot
selection, one replacement, and one index advance per accepted sample,
including modulo-32 wrap. Reset obeys the quiescent lifecycle in
CON-AP2-001-v6. Concrete layout, C types, update ordering, and any mechanism
used to enforce lifecycle conditions remain implementation obligations; no
specific ring representation or concurrency mechanism is mandated.

PR-002 accepts the mathematical recurrence and bounds under its stated
assumptions. C correspondence, expression promotions, generated code,
concurrency, and firmware correctness remain unproved.
