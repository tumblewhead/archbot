---
type: Design Contract
id: CON-AP2-002-v4
title: AP-002 rolling state and exact update contract
status: draft
version: 4
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-002-v3.md
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
# CON-AP2-002 v4: Rolling state and update

This version carries forward the representation, ownership, reset, arithmetic, timing, resource and proof obligations of v3. Its persistent inventory remains 71 bytes (`64 + 4 + 1 + 1 + 1`) within the approved 72-byte cap; physical layout remains open under VO-002. A record mutates rolling state only after v4 ingress has validated session, sequence, loss epoch and watchdog status under the ordered protocol. A continuity fault invalidates publication and prevents further updates until the v4 session transition completes. PR-002 assumptions and VO-005/VO-006 remain binding. No VO is discharged.
