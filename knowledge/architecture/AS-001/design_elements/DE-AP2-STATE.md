---
type: Design Element
id: DE-AP2-STATE
title: Ring and accumulator state responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-002.md
---
# DE-AP2-STATE placeholder

**Owner:** implementation-agent (assignment pending).

Own the single statically allocated ring, accumulator, oldest index, reset state and invariant. Adopt the 72-byte persistent-state cap; verify object layout, initialization and single-writer ownership. No source representation beyond the contract is designed here.
