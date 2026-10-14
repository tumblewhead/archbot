# AP-002-AS-V2-RECONFIRMATION-001: Engineering-authority disposition

**Status:** APPROVED, provisional AP-002 selection under corrected AS-v2  
**Date (America/Los_Angeles):** 2026-10-13 (no clock time asserted)  
**Authority:** User, speaking as engineering authority  
**Scope:** Superseding *applicability* decision; earlier approved AP and AS records are immutable history.

## Explicit engineering approval

After presentation of `process/decisions/AP-002-AS-V2-APPLICABILITY-REQUEST-v1.md`
with Option A (provisionally reaffirm AP-002 for CON-first against the
sample-indexed AS, maintaining outstanding debt and verification duties),
the engineering authority replied:

> Approve Option A (the only option lol)

This approves **Option A as specified in the exact request**. The quote
is transcribed from this conversation and is not described as a
cryptographically authenticated export.

## Current protected scope

- **Selected architecture:** AP-002, incremental exact 32-sample
  squared sum using a rolling accumulator and 32-entry ring.
- **AS basis:** independently reviewed `statement-v2.md`, with
  `verification_plan-v3.md` and `VO-004-v2.md`;
  review `TOY1-AS002-independent-review-v3.json` records
  `ACCEPT_WITH_CLARIFICATIONS` with no AS-drafting blocker.
- **R-001:** For each accepted legal input from the upstream publisher,
  one update; numerical behavior depends on ordered sample index rather
  than elapsed time. The historical 1 ms timing requirement is
  superseded **for this revised baseline**.
- **Publisher boundary:** uninterrupted ordered samples are the
  publisher's **external interface responsibility**, not an
  established physical hardware fact or a detector-side loss detector.
- **Unchanged:** 12-bit synthetic range C-001; 2048-byte
  detector-attributable SRAM limit and approved attribution C-002;
  no-FPU C-003; zero-padded newest-32 exact result R-002; no-overflow
  R-003; three F-001 objectives; PR-002's conditional abstract theorem.
- **Continued debt:** AD-003 remains accepted, owned by the evaluation
  agent, due for actual F ranking and risk disposition before final
  acceptance. No Pareto winner or measured cycle/flash result is claimed.
- **VO-004:** Engineering authority authorizes controlled, *versioned*
  supersession of the old 1 ms TARGET_VALIDATION timing obligation
  with detector-side exactly-once accepted-sample processing due at
  IMPLEMENTATION. VO-004 remains **OPEN** until independently accepted
  implementation evidence. VO-002, VO-003, VO-005 and VO-006 remain OPEN;
  VO-001's synthetic-domain acceptance is unchanged.
- **Historical records:** Original AS, AP-002 selection, VP/VO
  documents, CON v1-v4, and existing review receipts remain untouched.
  Old timing-related selection/debt statements are not authority to
  reintroduce the removed deadline into any new contract.

## Controlled activation and limits

This record supersedes the *protected R-001 applicability premise*
of `AP-002-PROVISIONAL-SELECTION-001`, but never grants final
architecture acceptance.

The independently reviewed AS-v2/VP-v3/VO-004-v2 package may become
the active baseline **after** the controlled active-baseline and VO-ledger
reconciliation is recorded and independently checked. That
reconciliation is the next process task; it shall not mark VO-004
discharged or change the protected F/C-002 scope.

Only then may a fresh, minimal CON-first authoring task proceed.
The new CON contracts must not inherit old loss epochs, watchdogs,
sequence counters, 1 ms deadlines, or assumed external concurrent-reader
requirements without new approved integration authority.

No implementation, DE approval, target claim, measured resource fit,
new accepted AD, or automatic VO discharge follows from this decision.

## Source chain

- `process/decisions/AP-002-AS-V2-APPLICABILITY-REQUEST-v1.md`
- `process/decisions/AS-001-SCOPE-CORRECTION-001.yaml`
- `reviews/gates/TOY1-AS002-independent-review-v3.json`
- `knowledge/architecture/AS-001/statement-v2.md`
- `knowledge/architecture/AS-001/verification_plan-v3.md`
- `knowledge/architecture/AS-001/verification/VO-004-v2.md`
- `process/decisions/AP-002-PROVISIONAL-SELECTION-001.yaml`
- `process/ledgers/ad_ledger.yaml`, `process/ledgers/vo_ledger.yaml`
