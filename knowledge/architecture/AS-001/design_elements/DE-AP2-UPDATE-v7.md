---
type: Design Element
id: DE-AP2-UPDATE-v7
title: Sample-indexed rolling update
status: draft
version: 7
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-002-v6.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
---
# DE-AP2-UPDATE-v7

**Purpose and boundary.** Coordinate the single state transition for each
accepted sample. Separating sequencing from storage makes the exactly-once
update and its correspondence to the abstract recurrence independently
reviewable.

**Operation.** Given a legal sample `x`, obtain the oldest value `old` from
`DE-AP2-STATE-v7`; compute the exact squares; replace `old` with `x`, advance
the oldest index modulo 32, and update the accumulator by including `x²`
and removing `old²`. Return the resulting accumulator as the completion
value. This is a mathematical operation order, not source code or a
prescription for add-before-subtract. The transition occurs once per
accepted sample, including during startup with zero-filled absent history.

**Numeric obligations.** `x² ≤ 16,769,025`, the resulting accumulator is
at most `536,608,800`, and an add-before-subtract intermediate from a valid
state is at most `553,377,825`. Each selected implementation expression
must use safe widths and conversions, including widening before
multiplication unless promotion rules establish safety. Legal-domain
protection is an implementation obligation under VO-006; out-of-domain
behavior is unspecified. No floating-point operation is permitted by
C-003.

**Pre/postconditions and composition.** Preconditions: a legal accepted
sample, initialized or reset state, and no reset in progress. Postconditions:
exactly one replacement and index advance; state represents the newest 32
accepted samples; accumulator equals their exact sum of squares; returned
completion value is that accumulator. Uses STATE and hands the value to
RESULT. It imposes no deadline, throughput, concurrency primitive, or
execution topology.

**Verification hooks.** Compare each abstract transition with PR-002 and a
bounded reference model, exercise startup and modulo-32 wrap, and inspect
the eventual language implementation for promotions and overflow under
VO-006. The abstract proof does not establish C correspondence.
