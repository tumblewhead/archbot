---
type: Verification Plan
id: VP-001-v3-candidate
title: AS-001 version 2 staged evidence plan candidate, corrected R-001 due stage
status: draft
version: 3
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: derived_from
    target: /architecture/AS-001/verification_plan-v2.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-004-v2.md
---
# VP-001-v3 candidate: unambiguous detector-side R-001 evidence

This additive candidate corrects finding ASR-001 from the independent AS
review. It does not change the authoritative VO ledger, discharge any
obligation, or replace earlier plan versions.

| Requirement | First assessable | Final due | AP-stage evidence | Later evidence |
|---|---|---|---|---|
| C-001 | AS | AS | Declared synthetic unsigned 12-bit input domain | Verify interface range enforcement and retain synthetic scope |
| C-002 | AP | IMPLEMENTATION | Categorized charged-SRAM envelope, attribution, margin, assumptions | Static allocation, stack/interrupt, dynamic and shared-memory evidence |
| C-003 | AP | IMPLEMENTATION | Integer-only algorithm plan | Build and code evidence that does not rely on FPU |
| R-001 | AP | IMPLEMENTATION | Show exactly one sample-indexed update per legal accepted sample and a bounded per-call work argument; impose no numerical call-rate requirement | Inspect implementation input dispatch and update behavior for one-to-one accepted-sample processing. Any separately approved integration throughput, overload, or deadline requirement has its own owner, criterion, VO and due stage |
| R-002 | AP | IMPLEMENTATION | PR-002 abstract recurrence plus explicit accepted-sample order and zero-padding assumptions | C-to-model and integration evidence for exact newest-32 behavior |
| R-003 | AP | IMPLEMENTATION | Universal mathematical bound under legal input assumptions | Verify C expression types, input validation, update invariant and implementation behavior |

## R-001 and publisher boundary

The binding detector-side obligation is one update for each legal sample
accepted at its interface; there is no elapsed-time cadence in corrected
R-001. VO-004-v2 assigns implementation evidence for this obligation to
`IMPLEMENTATION`, and this plan now does the same. This assignment does not
prove physical publisher continuity or unlimited throughput.

The publisher's uninterrupted ordered delivery promise remains an
unverified external interface assumption. If an integration authority later
approves throughput, overload, or real-time constraints, define a separate
requirement and VO with its own owner, acceptance criterion, evidence, and
due stage. That future obligation does not alter the current R-001 due stage.

## Evidence status and gate rule

All outstanding VOs remain open unless an independent accepted receipt
updates the authoritative ledger. Mathematical proof, structural validation,
and implementation/target evidence remain distinct. Missing evidence due at
the current stage is `UNRESOLVED`; later evidence can be deferred only with an
owner and credible plan.
