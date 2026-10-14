---
type: Design Element
id: DE-AP2-STATE-v6
title: Rolling state and reset responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-002-v6.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
---
# DE-AP2-STATE-v6 placeholder

**Owner:** implementation-agent (assignment pending). Own a representation
that corresponds to the abstract 32-sample window, zero-padded initialization,
and exact accumulator invariant. Reset requires acceptance quiescence and no
sample operation in progress; acceptance stays quiesced through reset
completion. Concrete enforcement and layout remain implementation/evidence
obligations. No synchronization primitive or topology is selected.
