# VK-001 terminal checkpoint and follow-on boundaries

**Date:** 2026-10-14 (US Pacific) / 2026-10-15 (Git timestamps).
**Status:** Completed bounded ERS → PLAN → MODEL EVIDENCE → independent review slice. Not product acceptance or a generic verifier qualification.
**Execution commit:** `df1c35e08bb438956a0950641defb2dd1c0a0786`.
**Terminal review:** [REVIEW_VERIFICATION_RUNG-9de9286189ea](../reviews/gates/REVIEW_VERIFICATION_RUNG-9de9286189ea-receipt.json), `ACCEPT_WITH_CLARIFICATIONS`.

## Grounded outcome

- Initial eight-obligation ERS inventory was rejected for underrepresenting accepted CON/DE C-expression and conditional charged-SRAM obligations. This was an inventory completeness failure, not a new product defect.
- Versioned ERS002 mapped 21 declared source obligations to 21 claims. Its independent reviewer accepted it with a clarification about conditional budget commitments versus actual physical fit.
- The independent plan reviewer accepted **one** candidate mathematical rung only, `ARITHMETIC-MODEL-BOUND`, targeting `ERS-CON-ARITH-BOUNDS`. The other 20 ERS claims remain unplanned, not failed or inapplicable.
- The execution recorded `CONDITIONAL_INTEGER_BOUND` and `COMPLETED` in `MODEL_ONLY` scope: `4095^2 = 16,769,025`, `32*4095^2 = 536,608,800`, `33*4095^2 = 553,377,825`, all below `2^32-1`. Independent review recomputed these numbers, reported artifact integrity and 37 source pins matched its checkout, and returned `ACCEPT_WITH_CLARIFICATIONS`.
- Product verification stayed false, `requested_claim_status=NOT_DISCHARGED`, and **VO-002 through VO-006 remain OPEN**. AD-003 and final F-001 comparison remain unchanged.
- The initially generated executor manifest referenced `experimental-investigator`, a registered role whose role file had not been installed. `tools/task.py inspect` returned status 2; the user's Bash `set -e` then exited. Commits `e8f81a3` and `60132e2` installed the missing role and a registry-completeness regression check. The subsequently pushed execution/review establishes that this execution path proceeded. Do not infer the entire Python regression suite or all three generic fixtures ran without logs.

## A meaningful success, not a generalization

The routed project run demonstrated immutable authoring artifacts and independent reviews across three stage kinds. It also caught a source-coverage omission and a missing role-file integration bug. It did **not** automate ERS discovery, create a complete Toy 1 verification ladder, validate arbitrary symbolic expressions, formally prove C correspondence, or measure target SRAM, stack or publisher behavior. Avoid promoting this first vertical slice into cleanroom or reusable-system acceptance.

## Next engineering scope proposed, not yet activated

The terminal review explicitly requires separately authorized scope before further verification. Recommended priorities:

1. **Concrete implementation correspondence:** design source/build checks for actual C widths, multiplication promotions, integer-only instructions/ABI and legal-domain boundary under VO-003/006. Preserve the distinction between accepted abstract PR-002 mathematics, host source review and target compiler evidence.
2. **Resource/integration evidence:** gather a target/integration configuration and charged-SRAM inventory with the existing seven conditional ceilings, lifetimes, ownership, overlap, stack/context nesting, shared/dynamic accounting and 256-byte reserve under VO-002. No target/toolchain or topology is authorized merely because it would ease a test.
3. **Behavioral correspondence:** test/reset/ordering/result across the accepted caller/publisher boundary for VO-004/005, with external publisher continuity remaining its own responsibility. Do not invent 1-ms deadlines, watchdogs, concurrent-reader guarantees or an out-of-domain policy.
4. **Finish Toy 1 with honest qualification:** review the actual evidence, keep uncovered requirements visibly open, complete the authorized F-001 comparison and then audit/freeze genericity before the first cleanroom replay.

These are candidate follow-on activities. The current VK-001 terminal receipt is **not** an automatically routable approval for them.

## UI and provenance lessons needing a bounded framework correction

1. **Stale inherited language:** The execution briefing's inherited `questions` and `non_claims` still say that F-ERS-001/002 need independent re-review, even though ERS002 had already been independently accepted. The authored execution bundle remains immutable, but the eventual UI must render accepted review overlays, superseded questions and current applicability instead of displaying old language as live blockers. A signed historical artifact should remain historically faithful, never silently rewritten.
2. **Source retention versus current-worktree pin checking:** `tools/verification_kernel.py` checks historical artifact `source_sha256` entries against files at the **current** worktree paths. After future modifications of `verification_kernel.py`, `task.py` or other pinned sources, old artifacts can fail a current-worktree integrity check even though their original Git content is still available. Before generic qualification, add an **offline read-only archive verifier** that resolves each source from the recorded version/content identity and distinguishes historical integrity from present applicability. Do not weaken freshness checks when creating *new* evidence.
3. **UI verdict layer:** Authoring artifacts correctly keep `review_state=PENDING`; subsequent independent review receipts carry acceptance. Project dashboards must join by exact artifact hash and show **current reviewed disposition separately from original authoring state**, never overwrite accepted evidence bytes.
4. **Role-registry canary:** Keep the added check that every registered task role file, view, and playbook exists, and test actual emitted manifests for the intended operation.

Treat these as framework defects/qualification tasks, not Toy 1 product requirements. In particular, do not change the pinned execution kernel just to tidy the already-accepted historical briefing. Any future corrected output must have a new task ID and be reviewed under its own evidence identity.

## Interaction/archive and user work split

All verified receipts stay in the project spine's linked history. No live conversational UI or automated project acceptance was installed. Human runs tests, compiler and target experiments locally; the assistant authors patches and reviews pushed evidence. Preserve this division and request material scope authorization at the next stage.
