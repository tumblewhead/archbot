# AE-003: Stage-appropriate provisional architecture selection

## Authority

C-002 scope `C-002-SCOPE-001` is approved: Option B. This decision defines
**detector-attributable SRAM** with a 2048-byte hard ceiling, not only persistent
state. It is not approval of a candidate, memory budget, or tradeoff.

## Two separate decisions

**Provisional selection for CON-first decomposition:** stage-level architecture
obligations must have credible evidence. Remaining final checks travel forward as
Verification Obligations (VO). Accepted risk of a provisional commitment is
Architectural Debt (AD). A gate packet with structural PASS is only **eligible
for independent review**, not automatically selected.

**Final acceptance:** all requirements are satisfied by accepted concrete
implementation/target evidence, the outstanding VOs are discharged, and original
F-001's state-SRAM/cycles/flash comparison is applied using appropriate evidence.

## Mandatory AE-003 entry checks

1. C-002 authority record is approved and cross-referenced; no change to AS/F.
2. VO-001 (AS-due, 12-bit ADC-domain authority) has a reviewable accepted receipt.
   Do not mark it discharged because earlier narrative text said PASS.
3. Each candidate has an AP-stage assessment for all C/R, with assumptions and
   references. No ungrounded SATISFIED status.
4. C-002 assessment has a categorized **allocation envelope** covering state,
   scratch, stack, detector-attributable interrupts, shared memory, dynamic and
   other charged SRAM. Document the charging rule, simultaneous peak, overlap,
   evidence/model, budget enforcement, and positive reserved margin.
   Arithmetic: `sum(charged maxima) + reserved margin <= 2048`.
   If a category is zero, justify why. A known unbounded contributor is a blocker.
   A budget allocation is *not* verified physical consumption.
5. R-001 has a bounded workload/timing feasibility argument and final timing VO;
   **no completed firmware or hardware WCET is required at AP selection**.
6. R-002/R-003 may use accepted abstract proof, but carry source-to-C correctness
   and integer-promotion VOs through implementation.
7. F-001 remains unchanged. Compare *projected* state SRAM, cycles and flash
   separately, with uncertainty. Never equate detector-charged SRAM with the
   state-SRAM objective. If the candidates are incomparable, the independent
   authority must approve a documented provisional tradeoff and AD; the
   evaluator cannot accept it on behalf of the authority.
8. All outstanding VOs have owner, due stage, method, acceptance threshold,
   assumptions, and escalation. Relevant accepted AD has owner, fallback,
   consequence, due stage and approving decision.

## Decisions

- `ELIGIBLE_FOR_INDEPENDENT_REVIEW`: structurally complete, evidence still needs review.
- `NO_DOWNSELECTION`: current AP obligations unresolved, conflicts or permissions missing.
- `PROVISIONALLY_SELECTED`: separate explicit authority acceptance of a
  reviewable candidate, with VOs/AD and fallback attached.

Never convert a successful structural check into `PROVISIONALLY_SELECTED` automatically.

## Next steps

1. Install/reconcile v2 controls and the new authority decision using
   `tools/reconcile_option_b.py` (dry-run then apply).
2. Reconcile VO-001 through `prompts/13-vo-reconciliation.md`; require a genuine
   accepted receipt before changing the ledger.
3. Prepare candidate resource allocations with `prompts/14-ap-envelopes.md`.
4. Run the versioned AE-003 evaluation prompt, generate explicit comparison and
   assessments, validate with `tools/stage_gate.py evaluate` and independently
   review any provisional commitment.
