# DECOMPOSE_DE: Contract-first design-element refinement

**Reusable operation:** DECOMPOSE_DE  
**Role:** design-agent  
**Entry:** Independent CON review has ACCEPT or ACCEPT_WITH_CLARIFICATIONS and explicitly permits DE refinement.

## Procedure

1. Resolve the triggering review, its authoring task and exact reviewed contract artifacts. Check their identities and hashes, then resolve the active AS/VP/VO baseline and accepted AP/F/proof/debt. Use the current baseline's effective relationships, not historical edges as authority.
2. Begin with **CON-defined interfaces and observable behavior**. Partition responsibilities into DEs with explicit inputs/outputs, ownership, state, reset/init lifecycle, composition order, invariants, and interface assumptions. Minimize coupling and avoid introducing new contracts merely for convenient implementation.
3. Explain the design to the human: what each DE does, why its boundary exists, what alternatives were considered, what assumptions would invalidate it, and how it preserves the accepted architecture. This explanation is a versioned design rationale; no interactive UI is presumed implemented.
4. Record a traceability matrix from every accepted CON and relevant AS C/R to DE(s) and the still-open verification obligations. Any unverified external producer assumption remains external. No DE may silently claim its physical enforcement.
5. Carry forward accepted resource ceilings as conditional allocations. Propose per-DE state/stack/scratch attribution and a checkable composition plan, without presenting compiler layout or target timing as measured. Preserve the approved total cap and F objectives; if an allocation cannot plausibly fit, report the smallest concrete blocker.
6. Specify implementable, language-independent DE contracts and correspondence tests. Describe safe integer widths and initialization/order requirements where applicable. Do not mandate unsupported hardware, concurrency, error handling, rate or watchdog behavior.
7. Produce **additive, versioned** DE concepts and one DE spine, plus a compact design-rationale/coverage report, independent review request and authoring receipt. Keep existing CON, AP, AS, proof and VO ledgers unchanged.
8. If blocked by a genuinely missing interface fact, report the exact question, source and affected gate. Do not invent a specification or escalate a future implementation measurement into a DE-stage blocker.

## Exit and authority

Use a receipt with `schema: pc-de-authoring-receipt/v1`, `operation: DECOMPOSE_DE`, `gate: DE_REVIEW`, and either `DE_READY_FOR_INDEPENDENT_REVIEW` or `DE_UNRESOLVED`. List changed artifacts and exact source references. Structural checks are not independent approval.

**Forbidden:** firmware implementation, approving DE, discharging VO, accepting new debt, changing AS/AP/F/CON, or asserting target measurements. Implementation begins only after an independent DE review and its guarded downstream authorization.
