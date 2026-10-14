# REVIEW_BASELINE: Independent controlled activation-package review

**Reusable operation:** REVIEW_BASELINE
**Role:** verification-agent

## Scope

Review a proposed *active baseline* assembled from independently
reviewed stage candidates and explicit engineering-authority decisions.
A structural check does not grant activation authority. The reviewer
must be independent of the baseline package's authoring invocation.

## Inputs and method

1. Resolve task spine, baseline candidate, source and superseding authority,
   independent stage review receipts, current active/historical records,
   candidate VO/AD ledgers and proposal/F/proof dependencies.
2. Verify exact source identities and revisions or artifact hashes.
   Reject stale, missing or internally contradictory authority references.
3. Compare each protected requirement with its proposed active baseline.
   Identify changes to timing, source guarantees, resource accounting,
   arithmetic domain, F objectives and accepted proof assumptions.
4. Diff candidate ledgers against historical current ledgers, entry by entry.
   For every revised due stage or scope, require explicit source authority.
   Reject silently discharged or deleted obligations, changed acceptance
   evidence, or unauthorized new Architectural Debt.
5. Check that upstream/environment assumptions are assigned to their
   responsible interface, not incorrectly imposed as downstream detector
   or implementation obligations.
6. Check applicability of accepted provisional AP selection, conditions,
   fallback and F ranking uncertainty. Preserve all historical decisions.
   When a candidate declares `effective_relation_overrides`, verify its
   deterministic, independently review-backed projection. Distinguish
   *historical concept links* from relationships selected by the candidate
   baseline. Review the selected dependency and its provenance rather than
   requiring an unrelated immutable concept revision. Reject ambiguous
   overrides, mismatches with reviewed artifacts or any claim that a
   pending candidate already changes the active graph.
7. Identify the precise candidate active-AS and VO record that may be
   installed after review, and the smallest remaining approvals or open
   obligations before downstream contracts.
8. Produce a versioned independent review report and receipt. Include
   exact sources, findings, inspected checks and uninspected material.

## Outcomes

- ACCEPT or ACCEPT_WITH_CLARIFICATIONS:
  BASELINE_PACKAGE_ACCEPTABLE_FOR_CONTROLLED_ACTIVATION.
- REVISE: BASELINE_PACKAGE_REVISION_REQUIRED.
- UNRESOLVED: BASELINE_AUTHORITY_OR_EVIDENCE_REQUIRED.

A favorable review establishes admissibility of the proposed
baseline *package*, not physical product/firmware acceptance.
**Do not edit** the authoritative VO ledger or current AS index in
this review invocation. The controlled activation step must follow
the accepted receipt and must not discharge VOs or rewrite history.
