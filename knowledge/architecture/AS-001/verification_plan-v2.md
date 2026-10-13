---
type: Verification Plan
id: VP-001-v2-candidate
title: AS-001 version 2 staged evidence plan candidate
status: draft
version: 2
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: derived_from
    target: /architecture/AS-001/verification_plan.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-004-v2.md
---
# VP-001-v2 candidate: stage-appropriate evidence

This is a proposed replacement plan for independent review. It does not
change the authoritative VO ledger or discharge any obligation.

| Requirement | First assessable | Final due | AP-stage evidence | Later evidence |
|---|---|---|---|---|
| C-001 | AS | AS | Declared synthetic unsigned 12-bit input domain | Verify interface range enforcement and retain synthetic scope |
| C-002 | AP | IMPLEMENTATION | Categorized charged-SRAM envelope, attribution, margin, assumptions | Static allocation, stack/interrupt, dynamic and shared-memory evidence |
| C-003 | AP | IMPLEMENTATION | Integer-only algorithm plan | Build and code evidence that does not rely on FPU |
| R-001 | AP | INTEGRATION_VALIDATION (only if a separately approved integration rate/deadline exists) | Show once-per-accepted-sample semantics and sample-indexed work; do not invent a timing number | Verify accepted-input handling; separately verify any approved throughput/overload/deadline requirement at its own boundary |
| R-002 | AP | IMPLEMENTATION | PR-002 abstract recurrence plus explicit accepted-sample order and zero-padding assumptions | C-to-model and integration evidence for exact newest-32 behavior |
| R-003 | AP | IMPLEMENTATION | Universal mathematical bound under legal input assumptions | Verify C expression types, input validation, update invariant and implementation behavior |

## R-001 and publisher boundary

The detector-side obligation is one update for each legal sample accepted at
its interface; there is no elapsed-time cadence in corrected R-001. The
publisher's uninterrupted ordered delivery promise is external and remains
unverified at the physical integration boundary. If an integration authority
later imposes throughput, overload, or real-time constraints, define a
separate requirement, evidence owner, acceptance criterion and due stage.
Do not turn this conditional future work into an implied current detector
deadline.

## Evidence status and gate rule

All outstanding VOs remain open unless an independent accepted receipt
updates the authoritative ledger. Mathematical proof, structural validation,
and implementation/target evidence remain distinct. Missing evidence due at
the current stage is `UNRESOLVED`; later evidence can be deferred only with an
owner and credible plan.

