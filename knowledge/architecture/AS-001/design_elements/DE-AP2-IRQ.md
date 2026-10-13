---
type: Design Element
id: DE-AP2-IRQ
title: Sample capture interrupt responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-003.md
---
# DE-AP2-IRQ placeholder

**Owner:** implementation-agent (assignment pending).

Own bounded sample capture and handoff in one non-nested detector ISR; it must not mutate rolling state or block. Adopt the 128-byte interrupt-context/stack cap. Identify vector, priority, nesting, frame and capture-loss observability, then provide target evidence. These platform facts remain unresolved. No ISR implementation is specified.
