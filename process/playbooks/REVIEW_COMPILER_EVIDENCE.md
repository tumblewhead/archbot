# REVIEW_COMPILER_EVIDENCE: independent executable evidence review

**Reusable operation:** REVIEW_COMPILER_EVIDENCE
**Role:** verification-agent
**Entry:** a pinned, versioned compiler/test-evidence candidate and an explicit project-scoped review task.
**Status:** independent evidence judgment only. NOT an automated product-verification or VO discharge gate.

## Procedure

1. Read `AGENTS.md`, the project spine, the task manifest, and the exact
   evidence summary identified by its trigger. Verify project/spine/subject,
   declared source revision, file hashes and referenced prior implementation
   review. Do not use unrelated project evidence or infer provenance from a filename.
2. Inspect each concrete command recorded in the evidence summary, including
   flags, exit status, compiler identity, actual tested C sources, assertions,
   positive cases and deliberate negative control. Verify that a nonzero
   negative-control exit represents a detected mismatch rather than missing
   executable, signal termination or another unrelated failure.
3. If raw logs/binaries under ignored `runs/` are available, verify their
   hashes and inspect important output. They may be absent from another clone.
   Distinguish report integrity, independently reproduced execution and
   unexamined locally retained data. Optionally rerun in a *new* local
   `runs/` path; do not overwrite the submitting run.
4. Independently reason about the C expression/ABI semantics for each relevant
   compiled environment. Review multiplication promotions, add/subtract
   intermediate bounds, wrap, legal inputs, initialization/reset and source
   correspondence to active AS/CON/DE and accepted abstract proof.
5. Distinguish evidence for source-level integer arithmetic from an actual
   target linked-image dependency and instruction audit. Host compilation and
   even a target object/assembly are not proof of no reliance on floating-point
   hardware throughout an unexamined final application. Do not mark VO-003
   discharged on that basis.
6. Identify what is established about VO-006 on the examined host and what
   remains for legal-domain ingress responsibility and actual target/compiler
   correspondence. Preserve the external publisher contract: no new sample
   timing, loss watchdog, out-of-domain behavior, ISR layout or concurrent-reader
   obligation is authorized.
7. Treat charged-SRAM evidence under VO-002 separately: a host object size or
   assembly listing is not a category/lifetime, stack/nesting or integration
   inventory. Refer to the accepted seven categories and their conditional
   budget ceilings, not to guessed measurements.
8. Compare the author's positive result with independent observations and
   adverse cases. Mark missing evidence as UNRESOLVED. A successful test run is
   not an accepted theorem. Any correction must be a versioned new artifact.

## Outputs and authority

Produce a bounded `reviews/gates/` Markdown report and JSON review receipt,
using `pc-compiler-evidence-review/v1`, with:
- review task ID, operation, project ID and spine;
- submitted evidence path and its exact SHA-256, reviewed source revision,
  reviewer execution identity and independently verified hashes;
- each actual command independently rerun or inspected, distinguishing
  `PRODUCER_REPORTED` from `REVIEWER_REPRODUCED` evidence;
- `disposition`: ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE or UNRESOLVED,
  **of the evidence report within its stated scope only**;
- grounded findings, unresolved target/integration requirements, any follow-up
  evidence request, and concise Engineering Briefing;
- `product_verified: false`, `vo_discharged: []` and carried open VOs.

Do not modify accepted ERS, AS, CON, DE, firmware or the active VO ledger.
Do not claim independence unless running a genuinely separate invocation.
No review receipt from this operation automatically routes to broader
verification execution or product acceptance. Missing target compiler/ABI
means target-qualification evidence is missing, not that the host evidence
is automatically false.

This playbook is reusable across projects with different C sources, targets,
bounds and memory limits. Domain-specific numbers come from the task's
accepted authority, not from this playbook.
