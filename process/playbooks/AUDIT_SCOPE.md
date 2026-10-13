# AUDIT_SCOPE: Trace derived obligations to architectural authority

**Reusable operation:** AUDIT_SCOPE
**Role:** verification-agent
**Purpose:** Investigate suspected scope inflation or unjustified strengthening of a downstream contract, proof obligation, design or verification gate.

## Required inputs

Resolve the task's spine and triggering receipt. Inspect the exact AS = (C,R,PS), accepted stakeholder decisions, applicable proof assumptions, stage policy, current candidate artifacts and associated VO/AD ledgers. Review only the relevant dependency graph. Source provenance and status must be explicit.

## Audit method

1. Enumerate each contested guarantee and split compound requirements into individual testable claims.
2. For every claim, classify its authority:
   - REQUIRED_BY_AS: explicit binding constraint or requirement.
   - NECESSARY_DERIVATION: logically required by AS or an accepted theorem, with the derivation shown.
   - ENVIRONMENT_PRECONDITION: required of an external producer/consumer, with an enforceable, independently verifiable integration contract.
   - OPTIONAL_ROBUSTNESS: attractive engineering behavior that is not part of the accepted AS.
   - UNSUPPORTED_SCOPE_EXPANSION: a claimed binding behavior without source authority.
   - UNKNOWN: provenance cannot yet be resolved.
3. Identify the minimum externally observable behavior necessary to satisfy the original AS. Do not silently weaken an obligation or assume a physical guarantee.
4. Compare this minimal behavior with the current design, including extra mechanisms, resource commitments, concurrency assumptions and verification burdens. Construct concrete counterexamples where relevant.
5. Determine whether a missing quantitative bound is genuinely due at the current stage or is implementation evidence that must be carried as an explicit future VO. Never equate a hypothetical resource budget with proof of target fit.
6. Present safe options: preserve the stronger interface with explicit authority, restore a minimal scope **through controlled versioned contracts**, or obtain a necessary external guarantee. If options require changing AS/F, call for separate human authority.
7. Record the affected dependency/impact set. Keep unaffected accepted proofs, architecture, obligations and independent findings intact. No implicit rollback.
8. Produce an independent audit and bounded receipt, including source versions, finding-by-finding classifications, authority references, unresolved questions and recommended next operation.

## Outcomes

- SCOPE_BASELINE_VALID: Claims trace to existing authority; resolve remaining evidence.
- SCOPE_REDUCTION_CANDIDATE: Unsupported or optional guarantees are candidates for controlled versioned simplification, followed by independent review.
- AUTHORITY_CLARIFICATION_REQUIRED: An explicit AS or risk interpretation must be decided by engineering authority.
- INSUFFICIENT_EVIDENCE: Unable to distinguish scope without further sources.

The audit may recommend a revision, but cannot unilaterally approve contracts, change AS/F/AP, remove a binding VO, accept AD, or implement firmware. Repeated review failures should trigger an audit of the obligations themselves rather than reflexively adding mechanisms.
