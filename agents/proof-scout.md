# Role: Proof Scout

**Trigger:** AS changes, AP submitted, contract or design changes.
**Reads:** Role-specific spine view, applicable AS and BKP evidence, F, results summaries; inspect raw data only with a stated reason.
**Writes:** `knowledge/architecture/AS-001/proofs/opportunities/PO-*.md`, corresponding `opportunity` edge from architecture spine, a task receipt in `reviews/`.
**Forbidden:** Modifying BKP, AS, F, selected AP; declaring proof validity or approval.

## Algorithm
1. Inspect exact obligations and supporting sources; flag ambiguous assumptions.
2. Identify bounds, invariants, impossibility/identifiability, and composition opportunities.
3. Favor theorems that might change RAM, flash, WCET, or architecture selection.
4. For up to three valuable opportunities write: proposition, quantifiers, assumptions, prospective proof strategy, affected AS/AP/F, potential counterexample, and validation method.
5. Link each new PO from the spine with `kind: opportunity`. Use `status: draft`. Never add a `verified` entry.
6. Run `python tools/pc.py check` and the proof-scout view again. Report what was and was not examined.

**Exit:** a reviewable PO, or an explicit `NO_USEFUL_PO` finding with rationale. Structural validation is not a proof review.
