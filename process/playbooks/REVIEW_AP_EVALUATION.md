# REVIEW_AP_EVALUATION: Independent architectural evaluation review

**Applicable to:** any versioned AP evaluation, regardless of domain or AS identifier.

**Role:** `verification-agent`. This reviewer must not be the author of the evaluation under review.

## Inputs

Obtain the task's triggering evaluation/review artifact and the current architecture spine.
Retrieve the AS, F, applicable selection and scope policy, candidate assessments,
accepted proof/source receipts, VO/AD ledgers, and prior evaluations only where needed.
Confirm their Git revisions or hashes and the exact scope of accepted evidence.

## Review method

1. Check that the evaluation's source versions, cited inputs, and accepted receipts
   correspond to the relevant claims. A changed spine link alone is not necessarily
   a change to an accepted mathematical assumption; inspect claim-level dependencies.
2. Check **every AP-due requirement** independently against the current stage policy.
   Distinguish `SATISFIED`, `CONDITIONALLY_SATISFIED`, `DEFERRED`,
   `UNRESOLVED`, and `VIOLATED`. A pending or future VO does not waive a
   requirement due now.
3. Check abstract proof scope versus source-level implementation and hardware
   verification. Do not promote a conditional theorem into target validation.
4. Check numeric arithmetic and resource-envelope accounting. State whether a
   budget represents a proposal, a proven bound, or a measurement.
5. Check the F comparison. Distinguish state SRAM from subsystem-wide memory,
   operation complexity from actual cycles, and projected flash from compiled flash.
   Do not invent a Pareto winner.
6. Run the project's applicable deterministic checks; record precisely what
   they verify and what they do not.
7. Determine whether the evaluation is **faithful to the evidence** and whether
   a candidate is **eligible for authority consideration**. Those are separate
   questions. Never select an AP or accept Architectural Debt on behalf of
   engineering authority.
8. Identify the smallest missing evidence or required protected decision, and
   ensure VOs and proposed AD are traceable without silently closing them.

## Output

Create a new versioned independent-review receipt (Markdown or JSON) referencing
the exact evaluation artifact. Include reviewer identity, source revision, examined
claims, dispositions with evidence links, test results, unresolved obligations,
independence limitations, and the next eligible gate.

Disposition for the **evaluation**: `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`,
`REVISE`, or `REJECT`.

Separate recommendation for architecture: `NO_DOWNSELECTION`,
`ELIGIBLE_FOR_AUTHORITY_DECISION`, or `FURTHER_EVIDENCE_REQUIRED`.

A positive review establishes neither final AP selection nor final firmware
acceptance. Preserve existing evaluations and prior review receipts unchanged.
