# EVIDENCE engineering briefing

Project: `AS-001` | Task: `EXECUTE_VERIFICATION_LADDER-956fdb75fa6b`

**Subject:** TOY1-C-SOURCE-REVIEWED
**Scope:** Candidate ERS revision 2: explicit CON/DE arithmetic and SRAM facets. Independent review pending; no new target, publisher or product acceptance.
**Authority:** draft, independent review pending; no product verification or VO discharge.

## Outcomes
### ARITHMETIC-MODEL-BOUND: CONDITIONAL_INTEGER_BOUND
Execution: COMPLETED. Scope: Conditional mathematical sum and add-first bound only; no concrete C-expression, promotion, legal-domain-enforcement or target-memory correspondence..
Target the mathematical facet explicitly. Concrete expression, multiplication and domain claims require separate evidence not supplied by this adapter.
```json
{
  "max_square": 16769025,
  "max_final": 536608800,
  "add_first_max": 553377825,
  "capacity": 4294967295,
  "final_fits": true,
  "add_first_fits": true,
  "premise": "valid sum-of-squares state; legal unsigned inputs"
}
```
Mathematical integer bound only; no compiler correspondence or memory evidence.

A failed model or counterexample is a scoped finding, not an automatically diagnosed product defect.

## Questions for the engineer
Independent reviewer: does the expanded inventory explicitly cover both review findings, including C evaluation/promotion/domain facets and every conditional SRAM accounting obligation, without adding product behavior?
Target/compiler and integration evidence remain unspecified. Keep the corresponding claims open; missing measurements do not block review of this ERS projection itself.

## Non-claims
New projection IDs expose already accepted CON/DE obligations; they do not add product requirements. F-ERS-001 and F-ERS-002 remain review findings until independently re-reviewed.
No 1-ms cadence, throughput guarantee, loss watchdog, ISR topology, heap prohibition, mandatory out-of-domain response or concurrent-reader behavior is introduced.
Publisher continuity is external project context, not a blanket premise conditioning unrelated SRAM, initialization or arithmetic obligations. No physical publisher evidence is asserted.
The seven SRAM category ceilings and 256-byte reserve are conditional contract commitments. DE subceilings are proposed accounting assignments subject to review, not measured capacities.
Initialization does not assume already-initialized state. Reset retains its accepted quiescent lifecycle precondition.
The MODEL_ONLY bound checks only a mathematical facet. Concrete C widths, promotions, legal-domain correspondence and target/integration evidence remain open; no VO is discharged.
Implementation observation gaps identify unconfirmed annotations, not failed requirements. The expanded inventory still needs independent semantic coverage review against accepted source artifacts.
AD-003/F-001 final comparison remains due before final acceptance. Active AS/AP/F/CON/DE, ledgers, firmware and the prior ERS bundle are unchanged.

## Next action
Independent review of this exact artifact. Preserve open obligations: VO-002, VO-003, VO-004, VO-005, VO-006
