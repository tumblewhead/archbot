# REVIEW_AS: Independent architecture statement and obligation review

**Reusable operation:** REVIEW_AS
**Role:** verification-agent
**Trigger:** A versioned architecture statement candidate is submitted for independent review.

## Input and authority

1. Resolve the task's declared architecture spine and current versioned AS candidate.
   Inspect the exact authoring receipt, the supporting source authority record,
   prior AS/BKP, current and proposed verification plans, due VO ledger, accepted
   AD/architectural decisions, proof assumptions, and candidate impact report.
2. Confirm authorship and independence. A candidate's status, clean structural
   check, or successful agent invocation is not independent acceptance.
3. Read only the required source and mandatory dependency closure. Preserve
   untouched historical versions.

## Review questions

1. **Authority and provenance:** Is every newly binding C/R/PS clause supported
   by explicit authority or a demonstrated necessary derivation? Keep synthetic
   fixtures, unverified external facts, and optional robustness separate.
2. **Sufficiency and minimality:** Does the revised AS state exactly the
   approved problem without implying stronger timing, source-integrity,
   security, concurrency, or target guarantees? Identify missing required
   semantics as well as invented ones.
3. **Interface separation:** Are upstream promises, detector obligations,
   integration checks and unknown hardware capability assigned to appropriate
   owners and verification boundaries?
4. **Proof impact:** Do existing mathematical proofs remain true under the
   revised input domain and order? If assumptions change, identify precisely
   which claim needs review; no blanket proof revocation.
5. **VO/VP continuity:** Map every inherited or revised obligation to an
   unambiguous owner, verification method and due stage. A conditional
   integration requirement must not leave a binding detector VO with no due
   stage. Historical VOs may be proposed as superseded, not silently removed
   or discharged.
6. **Decision impact:** Verify whether a prior selected AP, F evaluation, or
   accepted architectural debt protects an altered requirement. Record an
   explicit need for superseding authority instead of reinterpreting an old
   approval in place.
7. **Stage readiness:** Decide whether the revised AS and verification
   plan form a coherent draft baseline suitable for controlled authority
   disposition and later contract work. Do not demand finished firmware
   evidence at AS review.

## Receipt and limits

Produce an additive, independent, versioned report with exact source paths
and revision/hash provenance, findings by severity and claim, numerical checks
where applicable, continuing VOs/AD, and one of:
- ACCEPT / AS_CANDIDATE_ACCEPTABLE_FOR_CONTROLLED_BASELINE
- ACCEPT_WITH_CLARIFICATIONS / AS_CANDIDATE_ACCEPTABLE_WITH_EXPLICIT_CONDITIONS
- REVISE / AS_REVISION_REQUIRED
- UNRESOLVED / AUTHORITY_OR_EVIDENCE_REQUIRED

Use a review receipt with schema `pc-as-review/v1`, gate `AS_REVIEW`,
independent-of-authoring-invocation and explicit disposition.
Record uninspected material and actual tests/checks, not guessed results.

A favorable review **does not** change protected authority, silently
activate an AS, rewrite historical AP approval, discharge a VO, approve
CON/DE, or implement firmware. Explicitly identify the authorized next
decision or review step. Genericity: use only the task manifest, authority
documents and architecture spine to determine domain-specific obligations.
