---
type: Contract Spine
id: AS-001-CON-SPINE-006
title: Minimal AP-002 contract relationship index v6
status: draft
version: 6
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/spine-v5.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v6.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v6.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-INGRESS-v6.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-STATE-v6.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-UPDATE-v6.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-RESULT-v6.md
  - kind: decomposes_into
    target: /architecture/AS-001/design_elements/DE-AP2-RESOURCE-v6.md
---
# AS-001 contract spine v6

Additive minimal CON revision for active AS-v2 and AP-002. It supersedes v5
as the current candidate while preserving all earlier contracts and DE
placeholders as history. No contract/DE is accepted; independent review is
required before DE refinement or implementation. Publisher continuity
remains external and unverified.
