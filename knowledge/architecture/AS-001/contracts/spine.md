---
type: Contract Spine
id: AS-001-CON-SPINE-001
title: AP-002 contract relationship index
status: draft
relations:
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-001.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003.md
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

Draft contracts define sample/result behavior, exact rolling state/update, and execution/resource constraints. DE links are responsibility placeholders only; algorithm/source internals are not designed here.
