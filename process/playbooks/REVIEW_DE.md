# REVIEW_DE: Independent design-element and contract-conformance review

**Reusable operation:** REVIEW_DE  
**Role:** verification-agent

Review a submitted versioned DE spine, all related DEs, the accepted CON review, current active AS/VO ledger, approved AP/F, accepted proof scope and any architectural debt. Do not rely on an agent's completion message as acceptance.

For each DE verify: (1) it implements a specific accepted CON responsibility without changing observable semantics; (2) all accepted C/R and relevant VO responsibilities are covered; (3) interfaces, ownership, reset and state transitions compose without ambiguity; (4) the conditional resource envelope remains plausible and attributable, without falsely claiming measured fit; (5) external publisher/integration assumptions remain external; (6) mathematical invariants are preserved with explicit later C correspondence obligations; (7) no new unsupported rate, watchdog, concurrency, ISR or fault-handling requirement was invented.

Record any contradictions with precise source references, counterexamples, severity and smallest corrective action. Separate present design blockers from implementation-stage evidence. Produce an independent `pc-de-review/v1` receipt with `gate: DE_REVIEW`, `disposition: ACCEPT | ACCEPT_WITH_CLARIFICATIONS | REVISE | UNRESOLVED`, and exact reviewed source paths/hashes. Favorable review may authorize an implementation *task* through a later guarded transition; it does not approve firmware, discharge a VO, or assert target measurements.
