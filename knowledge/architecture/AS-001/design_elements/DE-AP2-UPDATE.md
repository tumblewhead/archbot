---
type: Design Element
id: DE-AP2-UPDATE
title: Rolling update responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-002.md
---
# DE-AP2-UPDATE placeholder

**Owner:** implementation-agent (assignment pending).

Own the AP-002 transition while preserving CON-AP2-002 semantics. Adopt 64 bytes maximum scratch outside task stack and reconcile compiler spills/locals with DE-AP2-TASK. Verify widening before multiplication, bounded arithmetic, and exact index order. No algorithm code is specified.
