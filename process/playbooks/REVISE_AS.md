# REVISE_AS: Controlled architectural statement correction

**Reusable operation:** REVISE_AS  
**Role:** architecture-agent  
**Trigger:** A protected, explicit engineering-authority decision authorizes
a scoped amendment to a previously reviewed architecture statement.

## Procedure

1. Resolve the versioned authority decision, its source request, independent
   audit, original AS, BKP sources, current verification plan and VO/AD ledgers.
   Confirm what the authority *actually approved*. Do not treat synthetic
   demonstration assumptions as human-approved requirements.
2. Separate interface and mathematical algorithm semantics from environment
   and integration assumptions. Explicitly classify each derived claim's
   provenance and authority. Do not assume hardware features are present.
3. Create an additive, versioned **draft** AS concept; preserve original
   sources and prior AS versions byte-for-byte. If correcting source provenance,
   add an annotation or versioned source concept rather than rewriting an
   original accepted or previously reviewed BKP concept in place.
4. Specify the exact changed C/R/PS clauses and immutable inherited
   constraints. Show impact on all affected proof assumptions, F objectives,
   AP selection, accepted debt, contracts and verification obligations.
5. Create versioned verification-plan and VO correction proposals where
   needed. An obsolete due-stage check may be **superseded as a proposal**,
   not silently deleted, discharged, or waived. Preserve the historical
   ledger and traceability until an independent accepted review and any
   required authority update establish the active replacement.
6. Clearly state external producer promises separately from detector
   guarantees; an external integration contract may require independent
   verification, but that is not a reason to implement a redundant
   internal watchdog or loss-detection protocol.
7. Produce a bounded coverage/impact matrix, next independent-review
   request and versioned authoring receipt. Record unverified assumptions
   and what would cause a return to authority for clarification.
8. Run appropriate structural checks and report which claims remain
   pending verification. Submit for independent AS review.

## Exit

- AS_REVISION_READY_FOR_INDEPENDENT_REVIEW if the new draft is complete,
  source-authorized and contains a controlled VO/AP/AD impact analysis.
- AS_REVISION_UNRESOLVED if a necessary interpretation, source or authority
  is missing. Record the smallest missing decision and stop.

No draft from this operation is automatically an accepted AS baseline.
Do not approve a contract, implement firmware, discharge a VO, amend
F, or overwrite an accepted architecture. This procedure is independent
of the sampled signal, MCU, solver, toy number and requirement identifiers.
