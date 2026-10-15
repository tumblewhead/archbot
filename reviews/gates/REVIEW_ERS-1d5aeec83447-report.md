# Independent ERS review — REVIEW_ERS-1d5aeec83447

## Scope and integrity

Reviewed submission `reviews/verification/TOY1-VERIFY-ERS001/receipt.json` for author task `TOY1-VERIFY-ERS001`, against checkout `ef72332966a78cc3c51f78494d379aae462ec344`. The artifact SHA-256 matches the submission receipt: `9377f70a55bb02c0e9cd60ceff91573e3c8c8c2bca2248dbc00cbe0d8d46c359`.

The candidate preserves the synthetic unsigned 12-bit domain, exact newest-32 sum, zero padded startup, accepted-sample ordering, reset lifecycle, full result range, lack of timing/concurrency guarantees, and the distinction between model evidence and C/target evidence. It names the active open obligations and does not claim any VO discharge. Its implementation observation caveat is appropriate.

## Findings

### F-ERS-001 — Arithmetic implementation obligations are underrepresented

**Severity:** blocking for ERS completeness.

The R-003 claim restates the AS requirement “No arithmetic overflow,” while CON-AP2-002-v6 and DE-AP2-UPDATE-v7 impose more specific obligations: bound the add-before-subtract intermediate from a valid state; ensure C expression types and evaluation order prevent intermediate overflow; widen before multiplication unless concrete promotion rules establish safety; and protect the legal-input domain under VO-006. The candidate rung's formula gives `(window+1)*max_sample^2 <= 2^bits-1`, but its stated subject is a mathematical model, and its parameters do not establish any C expression or domain correspondence. The ERS should represent these distinct obligation facets and their evidence boundary, not leave them implicit in a single generic R-003 claim.

**Source:** `knowledge/architecture/AS-001/contracts/CON-AP2-002-v6.md` (“Rolling state and update”); `knowledge/architecture/AS-001/design_elements/DE-AP2-UPDATE-v7.md` (“Numeric obligations”); `knowledge/architecture/AS-001/verification/VO-006.md`.

**Required resolution:** Add explicit claim/requirement coverage for the concrete integer-expression, multiplication-promotion, and legal-domain obligations (or demonstrate their explicit mapping to R-003/VO-006), with implementation due stage and no claim that the model rung closes them.

### F-ERS-002 — Conditional SRAM budget obligations are not projected

**Severity:** blocking for ERS completeness.

The candidate includes the 2,048-byte cap, but omits the CON-AP2-003-v6 / DE-AP2-RESOURCE-v7 binding evidence obligations that qualify it: the seven nonoverlapping categories and ceilings, 1,792-byte allocated ceiling plus 256-byte reserve, per-byte attribution and lifetime/nonoverlap inventory, peak dynamic allocation bounds, stack/interrupt nesting coverage, shared attribution, and handling of an infeasible category ceiling. C-002's one-sentence cap does not carry these contract-stage and implementation-stage details. The candidate also labels C-002 due only at IMPLEMENTATION, obscuring that the contract has already made a conditional budget commitment while physical feasibility and final inventory remain due.

**Source:** `knowledge/architecture/AS-001/contracts/CON-AP2-003-v6.md`; `knowledge/architecture/AS-001/design_elements/DE-AP2-RESOURCE-v7.md`; active ledger `process/ledgers/vo_ledger-AS-001-v2-active.yaml` (VO-002).

**Required resolution:** Project the conditional category-budget and attribution requirements, distinguish the existing contract-stage budget from implementation evidence, and retain VO-002 as open until concrete inventory and target verification are reviewed.

## Disposition

**REVISE.** The submission is a useful candidate inventory, but the uncovered accepted CON/DE obligations prevent accepting it as a complete ERS projection. No VO is discharged. No source artifact or authority record was modified by this review.

After the author updates the ERS and submits a new receipt, the next eligible action is an independent `REVIEW_ERS` against that exact submission. Structural integrity and hash checks do not establish mathematical or implementation correctness.
