# IMPLEMENT_DE: Implement an independently reviewed design

**Reusable operation:** IMPLEMENT_DE
**Role:** implementation-agent
**Entry:** Independent DE review has `ACCEPT` or `ACCEPT_WITH_CLARIFICATIONS` and explicitly recommends a guarded implementation task.

## Procedure

1. Resolve the exact accepted DE review receipt, reviewed source hashes, original DE authoring task and project spine. Verify the active AS/VP/VO baseline, accepted CON review, selected AP, F, C/R requirements, proof assumptions and accepted architectural debt. Refuse stale or mismatched inputs.
2. Explain the implementation approach and its traceability to DE interfaces **before** creating source. A DE is a responsibility, not necessarily a source file or thread. Favor the smallest sufficient implementation and explicitly identify any unavoidable target/integration assumptions.
3. Implement the approved DE/CON behavior using the requested language and target/toolchain context where provided. Do not invent a sample period, ISR topology, watchdog, continuity monitor, concurrent result reader, or out-of-domain behavior. For unspecified integration details, choose only nonbinding local implementation decisions and label them as such.
4. Produce runnable source and deterministic tests for startup/zero-padding, ring wrap, legal-domain extrema, exact arithmetic, result handoff, reset lifecycle and sample-order correspondence. Add negative/edge canaries appropriate to the **approved** domain. For C, justify intermediate widths and integer promotions and compare against a clear reference model.
5. Measure or bound each applicable verification obligation with honest provenance. C-002's charged SRAM includes all attributable categories and peak overlap, not just persistent state. Compiler/linker/stack/cycle claims require actual reproducible tool output; if unavailable, leave the corresponding VO open and provide precise local commands for the human to execute.
6. Produce a compact, human-readable **Engineering Briefing**: what was implemented, why, what was learned, what is still uncertain, and what needs human input. Link the briefing to the project task, evidence and next gate. Do not claim that this prototype implements the future conversational UI.
7. Produce a versioned implementation evidence manifest and independent verification request. Record exact commands and results actually executed, hashes for changed artifacts, toolchain/target, unresolved VOs, and all assumptions. Preserve the accepted DE, CON, AS, AP, proof and ledgers.
8. If a binding requirement cannot be implemented, report the smallest blocker and return to the affected gate. Do not silently relax C-002 or expand the AS.

## Exit

- `IMPLEMENTATION_READY_FOR_INDEPENDENT_REVIEW`: source, tests, evidence manifest, briefing and review request are present. The implementation is **not** independently accepted, and no VO is discharged by authoring.
- `IMPLEMENTATION_UNRESOLVED`: precise blockers, missing evidence and affected stage are recorded.

Use an additive receipt with `schema: pc-implementation-authoring-receipt/v1`, `operation: IMPLEMENT_DE`, `gate: IMPLEMENTATION_REVIEW`, and exact source provenance.

**Forbidden:** self-approval, rewriting accepted requirements/CON/DE, invented hardware evidence, unapproved architectural changes, or automatic VO discharge.
