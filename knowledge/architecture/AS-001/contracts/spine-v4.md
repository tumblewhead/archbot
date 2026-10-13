---
type: Contract Spine
id: AS-001-CON-SPINE-004
title: AP-002 contract relationship index v4
status: draft
version: 4
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/spine-v3.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-001-v4.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v4.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v4.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-INGRESS.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-STATE.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-UPDATE.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-TASK.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-IRQ.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-SHARED.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-MEM.md
---
# AS-001 contract spine v4

Version 4 is the active unresolved candidate for independent review. Versions 1 through 3 remain historical evidence. DE links continue to identify responsibility placeholders; DE refinement and implementation remain blocked pending accepted review and closure of the bounded shared-allocation blocker.
