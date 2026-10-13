---
type: Design Contract
id: CON-AP2-002-v3
title: AP-002 rolling state and exact update contract
status: draft
version: 3
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-002-v2.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: assumes
    target: /architecture/AS-001/proofs/PE-001-v2.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-002 v3: Rolling state and update

This version carries forward the representation, ownership, reset, arithmetic, timing, resource, and proof obligations of CON-AP2-002-v2 unchanged. In particular, its persistent inventory is 64 + 4 + 1 + 1 + 1 = 71 bytes within the approved 72-byte cap; publication, sequence metadata, synchronization, and the v3 loss epoch belong to the shared 128-byte cap in CON-AP2-003-v3 and are charged once. Layout evidence remains due under VO-002. No VO is discharged.

The only continuity interaction is that a record may mutate rolling state only after CON-AP2-001-v3 continuity checks succeed. A continuity fault invalidates publication and prevents further rolling updates until explicit session reset. PR-002 assumptions and VO-005/VO-006 remain binding.
