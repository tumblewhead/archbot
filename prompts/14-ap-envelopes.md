# AP-stage envelopes for Option B (preparation, not selection)

Read AGENTS.md, the root theory, the AS-001 spine, AS, F-001, AP-001/AP-002,
VP-001, VOs, PR-002, EP-002 and the APPROVED C-002-SCOPE-001 decision.
Read `docs/AE003_GATE.md` and the current AP selection policy.

Produce distinct conservative *proposal-level* SRAM allocation envelopes for
AP-001 and AP-002. Count the full detector-attributable boundary, not only the
algorithm buffer. Include state, scratch, stack, attributable interrupts,
shared allocations, bounded dynamic memory, other charged SRAM, and a positive
reserve. Specify which costs can overlap and why. Record all relevant
assumptions, including expected task/interrupt organization, and which
concrete CON/DE checks will enforce each budget. Mark uncertain costs plainly;
do not invent evidence, a compiler map, or target measurements. If a known
contributor cannot be bounded credibly, mark that candidate unresolved.

Distinguish each AP's charged-SRAM feasibility from the F-001 *state-SRAM*
ranking objective. Provide a bounded work model and note flash uncertainty.
Do not claim Pareto dominance without evidence.

Create an OKF artifact and spine links for the two candidate envelopes and a
review receipt. No architectural selection, AS/F modification, or VO discharge.
