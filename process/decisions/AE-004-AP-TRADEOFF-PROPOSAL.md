# Proposed authority decision — incomplete F-001 comparison

**ID:** AE-004-AP-TRADEOFF-PROPOSAL  
**Status:** PROPOSED / UNAPPROVED  
**Authority:** Engineering authority

## Decision requested

Consider authorizing a **provisional AP-002 commitment** while AP-002's AP-stage obligations are conditionally satisfied but the F-001 comparison remains incomplete. This is a request for authority action, not a selection or approval. AP-002 is not selected unless a separate accepted authority decision records that outcome.

## Basis and limits

AP-002 has conditionally satisfied AP-stage R-002/R-003 on the accepted abstract scope of PR-002 and has a proposed categorized C-002 envelope under the approved 2,048-byte detector-attributable SRAM ceiling. VO-001 is discharged only for the declared synthetic ADC domain. The envelope is not measured memory use. F-001 state SRAM (conditional 72-byte estimate) differs from total charged SRAM. Neither candidate has measured target WCET/cycles or flash bytes, so no Pareto winner is established and operation counts do not establish the 1 ms deadline.

## Risk record proposed

- **Architectural risk:** A provisional commitment may favor AP-002 even if later target cycle, flash, memory, or implementation evidence shows AP-001 or another design is preferable or AP-002 infeasible. Unknown cycle and flash dimensions prevent a supported F-001 ranking.
- **Proposed AD:** AD-003, incomplete F-001 comparison for provisional AP-002 commitment. This proposal does not create an accepted AD or modify the AD ledger.
- **Proposed owner:** evaluation-agent, accountable for reopening the comparison when comparable evidence arrives; engineering authority owns the risk acceptance decision.
- **Proposed deadline:** 2026-11-13 (30 calendar days after the AE-004 evaluation date), or before CON approval, whichever comes first.
- **Fallback:** If evidence is not available by the deadline, or AP-002 violates an AS requirement / fails the 2,048-byte charged-SRAM ceiling, reopen AP selection and suspend further AP-002-specific commitment; compare feasible candidates under unchanged F-001 when evidence permits.

## Authority response required

Accept or reject the proposed provisional commitment and risk explicitly. If accepted, issue a separately versioned authority decision identifying AP-002, the accepted AD-003 details, and carried VOs. Until that record exists, the decision remains unapproved, AP status remains unselected, and CON/DE are not approved.
