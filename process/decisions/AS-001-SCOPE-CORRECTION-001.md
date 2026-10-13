# AS-001-SCOPE-CORRECTION-001: Engineering-authority decision

**Status:** APPROVED for controlled revision and independent review  
**Date (America/Los_Angeles):** 2026-10-13 (no clock time asserted)  
**Authority:** User, speaking as engineering authority

## Explicit approval

Following `process/decisions/AS-001-SCOPE-CORRECTION-REQUEST-v1.md` and
the independent scope audit, the engineering authority replied:

> yes, newest 32 samples, it is the responsibility of the upstream sample publisher to give uninterrupted samples

This statement **approves** removal of the invented fixed 1 ms
*algorithmic* cadence, using the newest 32 samples from the upstream
publisher in publication order, with zero-padded startup. The detector
updates once for each legal received sample; numerical behavior is
independent of elapsed time between invocations.

**Uninterrupted delivery is the publisher's interface responsibility.**
For this toy's algorithmic boundary, the producer promises the intended
published sequence without missing, duplicated, or reordered sample
records. No assertion is made that a physical ADC, queue, ISR or target
has already demonstrated that promise. A publisher-integrity claim must
be separately checked at its own integration/verification boundary.

The detector **is not required to detect or reconstruct upstream loss**.
No loss epoch, sequence counter, 2^32-wrap mitigation or task-independent
watchdog is mandated by AS. None of these mechanisms can become required
merely because a prior CON draft included them. Concurrent external
reader semantics must be grounded in an approved interface, not invented.

The quotation is transcribed from the conversation, not a
cryptographically authenticated chat export.

## Bounded approval and untouched constraints

- R-001 is authorized to become sample-indexed, replacing the original
  1 ms cadence in the *new versioned AS*. No infinite throughput is claimed.
- R-002 remains exact newest-32 sum-of-squares over published samples,
  zero-padded during startup; R-003's legal-input overflow bound remains.
- C-001 stays unsigned 12-bit synthetic, C-003 stays no FPU; C-002
  stays the separately approved **2 KiB detector-attributable** SRAM
  scope with peak unique-byte attribution.
- F-001, PR-002's conditional abstract result and VO-001's accepted
  synthetic-domain scope are unchanged.
- The existing AP-002 provisional CON-first decision and AD-003 remain
  valid **historical** records; their applicability to a corrected
  R-001 must be reviewed before an accepted downstream continuation.
  This decision supersedes the old R-001 timing premise, not all
  other AP-002 conditions.
- VO-004 remains OPEN until a versioned, independently reviewed scope
  disposition replaces its 1 ms timing duty. Other due VOs remain open.
- Source BKP, AS v1, VP v1, prior CON v1-v4 and review receipts remain
  immutable history. Do not overwrite them.

## Authorized next operation

Use the generic Architecture Agent with a reusable, guarded
`REVISE_AS` playbook to draft a versioned corrected BKP/AS, verification
plan and VO-004 disposition, plus an AP-selection/AD impact matrix.
Then obtain an independent AS review before a fresh contract baseline.

**This authority decision is not itself an acceptance of newly drafted
AS text, a contract review PASS, source-delivery hardware evidence, a
VO discharge, or authorization to implement firmware.**
