# AP-002 applicability under corrected AS: authority request v1

**Status:** PROPOSED, NOT APPROVED
**Decision authority:** Human engineering authority
**Architecture:** AS-001, versioned sample-indexed candidate AS-001-v2
**Requested action:** Reaffirm AP-002 for provisional CON-first decomposition under the corrected AS, conditioned on controlled baseline and VO alignment.

## Inputs and independent disposition

- Human-approved corrected scope: `process/decisions/AS-001-SCOPE-CORRECTION-001.yaml`
- Reviewed candidate: `knowledge/architecture/AS-001/statement-v2.md`
- Revised verification plan: `knowledge/architecture/AS-001/verification_plan-v3.md`
- Proposed R-001 VO: `knowledge/architecture/AS-001/verification/VO-004-v2.md`
- Independent review: `reviews/gates/TOY1-AS002-independent-review-v3.json`, `ACCEPT_WITH_CLARIFICATIONS`, `AS_CANDIDATE_ACCEPTABLE_WITH_EXPLICIT_CONDITIONS`
- Historical approved selection: `process/decisions/AP-002-PROVISIONAL-SELECTION-001.yaml`
- Historical accepted debt: `AD-003` in `process/ledgers/ad_ledger.yaml`
- Original F: `knowledge/architecture/AS-001/merit.md`
- Abstract mathematics: `knowledge/architecture/AS-001/proofs/PR-002.md`

## Finding and rationale

The historical AP-002 selection explicitly protects one sample every millisecond.
The approved corrected R-001 requires one update per accepted published sample
independent of the elapsed interval. The old timing condition therefore cannot
remain a binding premise of a newly effective AP selection.

The AP-002 proposal itself is a sample-indexed 32-slot ring plus rolling
squared sum. Its recurrence and accepted abstract mathematical argument do
not depend on 1-ms sample spacing. Removing that deadline does **not**
establish new target cycle, flash, or memory measurements and does **not**
prove an unrestricted input arrival rate.

No new AP comparison or Pareto winner is claimed. AP-001's prior missing
candidate-specific mathematical evidence remains historical; F-001's three
dimensions are unchanged.

## Exact engineering-authority disposition requested

**Option A (recommended): REAFFIRM AP-002 provisionally.**

1. Carry forward the **provisional**, reversible selection of AP-002 for
   CON-first refinement against independently reviewed AS-001-v2,
   once its controlled baseline/VO alignment records are complete.
2. Supersede **only** the old protected 1-ms R-001 cadence with:
   *one integer rolling update for each legal accepted sample, indexed by
   publication/acceptance order, independent of elapsed time*.
3. Retain R-002 newest-32 exact squared-sum, zero-padded startup; R-003
   no-overflow; C-001 12-bit synthetic range; C-003 no-FPU; and the
   separately approved C-002 2048-byte detector-attributable SRAM scope.
4. Preserve the external upstream publisher's responsibility for
   uninterrupted ordered delivery as an **interface assumption**, without
   imposing detector-side sequence tracking, loss epoch, acquisition
   watchdog, reconstruction, or unstated concurrent-reader behavior.
5. Keep F-001 unchanged. Preserve accepted AD-003's core risk, owner,
   final-comparison requirement, fallback, and deadline before final
   acceptance. The old R-001/timing references in historical debt and
   selection records are superseded **only in application to the corrected
   AS**; do not rewrite those historical files.
6. Authorize a versioned controlled **VO-004 rescoping** from the old
   TARGET_VALIDATION 1-ms deadline to the detector-side once-per-accepted-
   sample requirement, with implementation-stage verification as in
   VP-001-v3 and VO-004-v2. VO-004 stays OPEN, not discharged.
7. Keep VO-002, VO-003, VO-005, VO-006 open and VO-001 discharged only
   within its accepted synthetic-domain scope.
8. After controlled records and the required independent gate are updated,
   allow *new minimal contracts*, not resurrection of old CON v4
   publication/loss/watchdog obligations. No implementation or DE
   approval is granted by this provisional selection.

**Option B: REOPEN AP selection.** Require a fresh AP comparison under the
corrected AS before any new CON baseline. This may be appropriate if the
engineering authority no longer supports AP-002 as the provisional approach.

**Option C: REQUEST REVISION.** Identify the missing condition to change.

## What approval does not imply

- This request does not itself activate AS-001-v2, update VO ledger status,
  accept DEs/CONs, or verify firmware.
- A reviewer or agent cannot silently infer engineering authority from
  `ACCEPT_WITH_CLARIFICATIONS`.
- Publisher delivery and target timing are not claimed physically verified.
- Original AS, VP, VO, AP selection and AD receipts remain immutable history.
- Any materially new requirements need their own source and authorization.

## Proposed next sequence upon explicit Option A approval

1. Create a superseding versioned AP-002 applicability decision, referencing
   the reviewed AS and this request.
2. Create a reviewed controlled AS/VP/VO-004 active-baseline index and
   reconcile the VO ledger to the accepted replacement. VO-004 remains open.
3. Record AD-003 applicability to the corrected AS without modifying the
   original accepted debt record; preserve incomplete F ranking.
4. Generate a fresh CON-first authoring task on the corrected active AS,
   then independent CON review. Keep previous CON versions as historical
   evidence.
5. Continue toward DE, working C, and independently reviewed implementation
   evidence, discharging VOs only at their evidence gates.

**Approval requested:** "Approve Option A: provisionally reaffirm AP-002
under sample-indexed AS-001-v2, retaining AD-003, F-001, C-002 and
all open implementation VOs as stated."
