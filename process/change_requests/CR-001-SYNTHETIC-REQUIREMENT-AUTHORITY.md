# CR-001: Synthetic requirement promoted into architectural authority

**Status:** OPEN / proposed correction, awaiting controlled scope decision  
**Detected:** 2026-10-13  
**Affected architecture:** AS-001 sliding-window squared-sum detector  
**Origin:** Human engineering challenge: the algorithm should not depend on sample rate, and additional hardware/security requirements appear to have been invented.

## Verified origin of 1 ms

- `knowledge/bkp/problem-origin.md`, ID `BKP-NEED-001`, explicitly labels its content **"Stakeholder need (invented for the demonstration)"** and specifies "updated every 1 ms".
- `knowledge/bkp/adc.md`, ID `BKP-ADC-001`, also specifies a synthetic 1 ms sample arrival assumption.
- `knowledge/architecture/AS-001/statement.md`, `R-001`, promotes that scenario into "Accept one sample per millisecond".
- `knowledge/architecture/AS-001/verification_plan.md`, `VO-004`, AP-stage budgets and downstream CON drafts require 1 ms timing evidence.
- These three source files were imported together in commit `aa2bbb5ec2e708f851bfccb9cbc1f4610bdfb899` (2026-10-13). No separate human approval for the 1 ms algorithmic rate has been identified in the inspected repository.
- The user now explicitly challenges this requirement and states the detector should work at any sample rate. This is a **requirements-change signal**, not approval to silently rewrite already reviewed artifacts.

**Finding:** A scenario assumption was labelled `Stakeholder Decision` and treated as binding even though the document itself calls it invented. Provenance is not equivalent to engineering authority.

## Mathematical clarification

For a fixed sample-count window `N`:

```text
S[k] = sum(j=0..N-1) x[k-j]^2
S[k+1] = S[k] - x[k-N+1]^2 + x[k+1]^2
P_mean_square[k] = S[k]/N
```

The recurrence is defined on **sample index**, not wall-clock time. The
algorithm is applicable at arbitrary input sampling rates and even
irregular sample timestamps, provided the specification defines "newest
N samples" by sample order. A fixed count spans a different real-time
duration at each rate, which is relevant only if an application-level
time window, spectral response or detection latency is separately required.

`S` is a squared-sample sum, sometimes used as a power/energy proxy.
A physical power in watts requires additional calibration, units and
physical assumptions. No alarm threshold or decision policy has been
approved in AS-001.

## Proposed minimal corrected requirement

A replacement **candidate** for R-001:

> The detector shall accept a legal input sample when invoked and
> update its output once for each accepted sample. Its numerical
> result and update rules shall not depend on the interval between
> sample invocations. Interface throughput and timing limits belong
> to separately approved target-integration requirements.

R-002's 32-sample window and R-003's overflow guarantees are maintained
as the current toy fixture until the scope audit determines otherwise.
Do not imply that "any sample rate" means an implementation has infinite
processing throughput.

## Secondary specification-origin audit

The AS does **not** expressly require detection of every missing
upstream acquisition, a loss epoch, counter wrap recovery, atomic
publication to external concurrent readers, an ISR topology, or an
independent watchdog. These appear in CON v1–v4 and review history.

For each, determine whether it is:
- necessary to implement R-002 under a *stated* input-stream model,
- an optional integration guarantee,
- a provisional robustness feature,
- a new stakeholder requirement needing separate approval, or
- an unjustified requirement expansion.

Do not presume the strongest protocol is necessary merely because
earlier independent reviews asked for missing guarantees within that
protocol. Review whether the underlying obligation is legitimate first.

## Preserve legitimate authority and scope

- C-002's detector-attributable 2 KiB accounting **was separately approved**
  by engineering authority as C-002 Option B. Do not delete it because its
  initial numeric bound was synthetic.
- AP-002's provisional CON-first selection and accepted AD-003 remain
  historical authority, but must be assessed for impact from a changed AS.
- VO-001's accepted review is specifically scoped to the synthetic
  12-bit ADC model. Do not silently expand its authority.
- PR-002's mathematical rolling recurrence/bounds can remain valid under
  sample-indexed inputs and the same N/legal-value assumptions; check its
  exact proof dependencies instead of invalidating it indiscriminately.
- VO-004's target 1 ms deadline will require controlled revision or
  retirement if R-001 changes. A due-stage VO cannot simply disappear.
- All CON v1–v4, reviews and receipts must remain immutable historical
  evidence. New contracts must be based on a formally accepted corrected AS.

## Process defect to correct

At source ingestion, record **both** provenance and authority class,
for example `human_approved_requirement`, `derived_obligation`,
`synthetic_fixture`, `proposed_assumption`, or `verified_external_fact`.
An upstream item labelled invented, synthetic or demonstrative must
not silently become a binding stakeholder requirement.

A transition from `synthetic_fixture` or `proposed_assumption` to
binding AS requires an explicit, source-referenced human decision.
Reviewers must check the **necessity and source** of a downstream
guarantee, not merely its internal consistency. Gate/receipt success
cannot upgrade authority.

## Requested controlled resolution

1. Run a new independent scope audit of both 1 ms and continuity
   specification provenance, including the human's current objection.
2. Prepare a versioned corrected AS candidate and an impact graph:
   R-001 / VO-004 / VP / CON / DE placeholders / F and proposal
   assessments / accepted proofs.
3. Explicitly decide the intended detector semantics, then seek the
   human's approval of the changed AS or any new robustness guarantees.
4. Resume review on the **smallest affected set**, using the accepted
   AS as the new authority. Do not continue elaborating the security-
   grade input-loss protocol merely because it exists in prior drafts.

Until the correction is authorized, do not imply that a revised R-001,
retired VO-004, or reduced continuity contract is already accepted.
