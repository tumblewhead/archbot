# REVIEW_IMPLEMENTATION: Independent implementation and evidence review

**Reusable operation:** REVIEW_IMPLEMENTATION
**Role:** verification-agent
**Entry:** A versioned implementation authoring receipt, source, tests and a bounded review request exist under a guarded, independently accepted DE task.

## Review

1. Resolve the exact authoring task, source receipt, project spine, accepted DE/CON reviews, active AS/VP/VO ledger, applicable proof, resource boundary and debt. Check exact file identities and hashes. Do not infer independent acceptance from a successful agent run.
2. Inspect the actual source and tests. Check that interfaces, state, reset, order, result semantics and arithmetic implement the accepted DE and CON, including the language's integer promotions, legal-domain bounds and worst-case intermediate expressions. Identify uncovered canaries and credible counterexamples.
3. Review the author's Engineering Briefing for accurate explanations, newly learned information, uncertainties, outstanding human questions and a traceable evidence path. Compare the author's claims with receipts and actual tool outputs; flag contradictions.
4. Independently evaluate reproducible test and build evidence when available. Distinguish commands run in the author's environment from those run by the reviewer, and distinguish host tests from target/integration measurements. Record toolchain, build flags and whether assertions are enabled. Avoid inventing measured facts.
5. For each open VO, classify available evidence, missing evidence, applicable due stage and next permitted action. In particular, a host `sizeof` or passing reference model is not a complete SRAM/stack or target proof. Preserve the external publisher's unverified interface responsibility.
6. Record whether implementation behavior is acceptable for the *examined environment*, whether target evidence is still needed, and whether additional independent tests or source revisions are necessary. If evidence is missing, make a bounded plan instead of demanding a new architectural requirement.
7. Produce an independent report and `pc-implementation-review/v1` receipt with exact reviewed source hashes, findings, scope, `disposition` (ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE or UNRESOLVED), and stage-specific next recommendation. Do not automatically discharge VOs, accept architectural debt, or approve a target product.

## Guardrails

The reviewer must not edit accepted AS/AP/F/CON/DE, change protected requirements, invent sample rates or hardware topology, or treat an unverified external assumption as a detector obligation. If the code needs correction, use a versioned implementation revision, not an unreviewed silent edit.

The independent review is a scoped evidence judgment, **not** an authorization to claim final firmware or physical target acceptance.
