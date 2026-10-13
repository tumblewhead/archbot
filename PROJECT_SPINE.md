# archbot project spine

## Status
Repository: `tumblewhead/archbot`, canonical nonvolatile project memory.
The locally developed Codex prototype and versioned architecture/evaluation evidence were imported in commit `aa2bbb5ec2e7`. Inspect live artifact revisions rather than relying on earlier bootstrap notes. The spine-filter fix is being applied as a follow-up commit; its regression tests still require confirmation on the developer's workstation.

## Theory
Progressive Concretization:
BKP -> AS = (C,R,PS), with independent Proofs (P/T), Proof Opportunities (PO), and Figure of Merit (F) -> competing APs -> provisional selection -> Contracts (CON) -> Design Elements (DE) -> Firmware -> final acceptance.

Every transition preserves obligations and supporting evidence. Proofs are conditional on stated assumptions. Requirements become binding immediately but demand stage-appropriate evidence: first_assessable_at, verification_due_at. Verification Obligations (VO) travel with artifacts. Architectural Debt (AD) records uncertainty and fallback plans associated with early commitment. An architecture may be provisionally selected for CON-first decomposition without completed firmware; final acceptance discharges all due VOs.

## Knowledge and agents
Google OKF v0.2 Markdown concepts with project-defined typed relationships. Spines select role-specific graph projections without deleting source artifacts. `agents/` defines roles; `process/` defines policies and gates; `tools/` contains deterministic structural checks, telemetry, and stage-gate validation. The LLM proposes; independent reviews and checkers gate accepted status.

## Authority
C-002 Option B was explicitly approved by the engineering authority: limit of 2,048 bytes **detector-attributable SRAM**, including owned state, scratch, charged stack/interrupt, and allocated shared memory under documented ownership rules. This does not approve an AP or discharge VO-002.
Approved authority record: `process/decisions/C-002-scope.yaml` (present in this repository).

## Historical experiment status through the imported working tree
- Proof Scout PO-001 proposed 32-sample / 12-bit squared-sum bound.
- PE-001-v2 corrected an invalid add-before-subtract overflow counterexample and addressed C integer promotion. PR-002 accepted the *abstract mathematics* with clarifications. Firmware remains unverified.
- AE-001 / AE-002: no downselection. EP-001 / EP-002: stage-appropriate planning and candidate memory envelopes.
- AE-003: no downselection; outstanding VO-001 source-adequacy review. C-002 approved scope and candidate-level envelopes now available, not target-verified.
- The last reported local unit suite had 25 tests with one failure: `test_context_profile_excludes_raw_from_proof_scout`, which found two non-concept auxiliary references. Graph check itself had zero errors (31 concepts, 114 typed links).
- Fix prepared as `patches/pc-spine-context-regression.patch`. Apply to the imported local working tree *only if applicable* and rerun tests. Do not change a test expectation from zero to two.

## Immediate next steps
1. Pull this commit and run the full unit suite plus `python tools/pc.py check --fast`. Confirm the Proof Scout context contains no non-concept artifacts.
2. Independently assess VO-001 using `prompts/16-vo001-authority-review.md`, scoped strictly to the synthetic ADC model. Do not mistake it for certified physical ADC metrology.
3. Reassess AP-stage eligibility and F-001 once due obligations have accepted receipts. Preserve AE-003's `NO_DOWNSELECTION` as history; carry accepted AD/VO forward if an AP is provisionally selected.

## Source-of-truth rule
Chat summaries are navigation aids only. Once imported, the live versioned source, spines, authority decisions, and receipts supersede this bootstrap status. Update this file with concise status pointers after each substantive gate. Never duplicate large experimental evidence here.
