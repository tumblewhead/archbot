# archbot project spine

## Status
Repository: `tumblewhead/archbot`, canonical nonvolatile project memory.
This is an **initial bootstrap**. The latest locally generated proof/evaluation artifacts and code must be imported from the developer's existing `progressive-concretization-codex/` checkout. Do not treat this bootstrap as the full working tree.

## Theory
Progressive Concretization:
BKP -> AS = (C,R,PS), with independent Proofs (P/T), Proof Opportunities (PO), and Figure of Merit (F) -> competing APs -> provisional selection -> Contracts (CON) -> Design Elements (DE) -> Firmware -> final acceptance.

Every transition preserves obligations and supporting evidence. Proofs are conditional on stated assumptions. Requirements become binding immediately but demand stage-appropriate evidence: first_assessable_at, verification_due_at. Verification Obligations (VO) travel with artifacts. Architectural Debt (AD) records uncertainty and fallback plans associated with early commitment. An architecture may be provisionally selected for CON-first decomposition without completed firmware; final acceptance discharges all due VOs.

## Knowledge and agents
Google OKF v0.2 Markdown concepts with project-defined typed relationships. Spines select role-specific graph projections without deleting source artifacts. `agents/` defines roles; `process/` defines policies and gates; `tools/` contains deterministic structural checks, telemetry, and stage-gate validation. The LLM proposes; independent reviews and checkers gate accepted status.

## Authority
C-002 Option B was explicitly approved by the engineering authority: limit of 2,048 bytes **detector-attributable SRAM**, including owned state, scratch, charged stack/interrupt, and allocated shared memory under documented ownership rules. This does not approve an AP or discharge VO-002.
Authority decision artifact from prior development: `process/decisions/C-002-scope.yaml` (import from the local working checkout).

## Latest known live experiment status before Git bootstrap
- Proof Scout PO-001 proposed 32-sample / 12-bit squared-sum bound.
- PE-001-v2 corrected an invalid add-before-subtract overflow counterexample and addressed C integer promotion. PR-002 accepted the *abstract mathematics* with clarifications. Firmware remains unverified.
- AE-001 / AE-002: no downselection. EP-001 / EP-002: stage-appropriate planning and candidate memory envelopes.
- AE-003: no downselection; outstanding VO-001 source-adequacy review. C-002 approved scope and candidate-level envelopes now available, not target-verified.
- The last reported local unit suite had 25 tests with one failure: `test_context_profile_excludes_raw_from_proof_scout`, which found two non-concept auxiliary references. Graph check itself had zero errors (31 concepts, 114 typed links).
- Fix prepared as `patches/pc-spine-context-regression.patch`. Apply to the imported local working tree *only if applicable* and rerun tests. Do not change a test expectation from zero to two.

## Immediate next steps
1. Import the actual latest developer checkout and run evidence into this new repository (see `docs/IMPORT_LOCAL_WORKTREE.md`).
2. Resolve the spine-filter regression and verify all tests pass.
3. Reconcile VO-001 with source-adequacy evidence scoped to the synthetic ADC model; do not mistake it for certified physical ADC metrology.
4. Reassess AE-003 under approved staged selection policy without assuming a winner. Carry any accepted AD/VO forward into CON.

## Source-of-truth rule
Chat summaries are navigation aids only. Once imported, the live versioned source, spines, authority decisions, and receipts supersede this bootstrap status. Update this file with concise status pointers after each substantive gate. Never duplicate large experimental evidence here.
