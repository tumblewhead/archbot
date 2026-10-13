---
type: Design Element
id: DE-AP2-TASK
title: Detector task and scheduling responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-003.md
---
# DE-AP2-TASK placeholder

**Owner:** implementation-agent (assignment pending).

Own the sole detector task, consumption order, result publication, and reset/fault coordination. Adopt the 384-byte task-stack cap and 1 ms service requirement. Provide scheduler, call-depth, compiler stack/map and target timing evidence. Platform scheduling and queue details remain unresolved. No task implementation is specified.
