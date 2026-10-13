---
type: Contract Spine
id: AS-001-CON-SPINE-002
title: AP-002 contract relationship index v2
status: draft
version: 2
relations:
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-001-v2.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v2.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v2.md
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

Version 2 is the active draft set; v1 contracts and spine remain immutable history. DE links are responsibility placeholders only; algorithm/source internals are not designed here.
