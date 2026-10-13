---
type: Contract Spine
id: AS-001-CON-SPINE-003
title: AP-002 contract relationship index v3
status: draft
version: 3
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/spine-v2.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-001-v3.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v3.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v3.md
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
# AS-001 contract spine

Version 3 is the active draft set for independent review; v1 and v2 contracts and spines remain immutable history. DE links remain responsibility placeholders; implementation internals are not designed here.
