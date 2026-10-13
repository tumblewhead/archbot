# AP-002-PROVISIONAL-SELECTION-001: Engineering authority decision

**Status:** APPROVED, provisional CON-first commitment only  
**Date (America/Los_Angeles):** 2026-10-13 (no clock time asserted)  
**Authority:** User, speaking as engineering authority

## Explicit approval

After the assistant asked whether to approve provisional AP-002 selection
and AD-003 under the revised v2 request, the engineering authority replied:

> Approved for CON-first

This record interprets that statement in the context of the immediately
preceding question and the revised request:
`process/decisions/AP-002-PROVISIONAL-AUTHORITY-REQUEST-v2.md`.

The statement **approves provisional AP-002 selection for CON-first work
and accepts the specified AD-003 risk**, but does not assert that AP-002 is
Pareto-optimal or that firmware and target claims have passed.

The authority quotation is transcribed from the conversation, not presented
as a cryptographically authenticated chat export.

## Conditions and scope

- AS-001 and F-001 remain unchanged.
- C-002 Option B's 2048-byte detector-attributable SRAM limit remains binding.
- PR-002 is accepted only for the abstract recurrence and bound under its
  stated assumptions, not the C implementation.
- VO-001 is discharged only for the synthetic ADC model.
- VO-002 through VO-006 remain open and shall be assigned through contracts,
  design, implementation, and validation.
- AD-003 records risk from the incomplete F-001 cycle and flash comparison.
  It is due for resolution before **final** acceptance, not before CON
  definition. CON-stage review must check evidence plans and enforceable
  budgets, not demand a finished firmware build.
- If later evidence falsifies a feasibility assumption, review affected
  commitments and return to AP selection if necessary.

## Source and review chain

- `knowledge/architecture/AS-001/evaluations/AE-004.md`
- `reviews/AE-004-review-v3.json`:
  `ACCEPT_WITH_CLARIFICATIONS`; `ELIGIBLE_FOR_AUTHORITY_DECISION`
- `process/policies/AP_SELECTION_v2.yaml`
- `process/decisions/C-002-scope.yaml`
- `process/ledgers/vo_ledger.yaml`
- `process/ledgers/ad_ledger.yaml`

This is a controlled *authority* decision. The postdecision AP-002 v4
stage-gate packet still requires deterministic checks and may be reviewed
independently. Neither the document nor a passing structural check serves
as final engineering verification.
