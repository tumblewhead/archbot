# AS-001 corrected-scope candidate (not approved)

**Status:** proposal for engineering-authority decision only. This document does not amend `knowledge/architecture/AS-001/statement.md`.

## Candidate R-001

> For each legal input sample accepted by the detector interface, update the detector once. The rolling result is defined by accepted sample order and shall not depend on the elapsed time between sample invocations. Throughput, overload behavior, and any real-time deadline are specified by separately approved integration requirements.

## Semantics to confirm

- R-002 remains the exact sum of squares of the most recent 32 **accepted input samples**, in acceptance order; before 32 accepted samples, missing history is zero.
- C-001 remains the synthetic unsigned range 0..4095 pending any separate domain decision. R-003 remains the no-overflow requirement under that domain.
- This does not imply unlimited throughput or prescribe what happens when a producer cannot deliver every physical acquisition. If the intended meaning is “last 32 physical acquisitions,” authority must specify how acquisition loss is represented and what guarantee is required at the source boundary.
- No alarm threshold, time-duration window, loss-detection guarantee, external-reader concurrency model, watchdog, or timing bound is introduced by this candidate.
- C-002's separately approved 2048-byte detector-attributable SRAM accounting and C-003 remain unchanged.

## Required controlled follow-up if approved

Version the AS and verification plan; replace/re-scope VO-004 without deleting its history; assess AP-002 and AD-003 conditions; then issue a versioned contract correction and independently review it. Keep all current contract versions, proof receipts, VO/AD records, and selection history intact. No transition occurs by virtue of this candidate.
