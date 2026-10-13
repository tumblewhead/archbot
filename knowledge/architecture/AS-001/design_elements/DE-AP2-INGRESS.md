---
type: Design Element
id: DE-AP2-INGRESS
title: Sample ingress and validation responsibility
status: draft
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v3.md
---
# DE-AP2-INGRESS placeholder

**Owner:** implementation-agent (assignment pending).

Own adaptation of source samples, legal-domain validation, sequence/order preservation, read-only observation of producer loss epoch, fail-closed response to the independent gap watchdog, and bounded reporting of range or continuity faults. The producer owns loss epoch increments; ingress never acknowledges or clears it. Must not choose a physical ADC behavior absent target evidence. Interfaces and fault semantics are governed by CON-AP2-001-v3. No implementation is specified.
