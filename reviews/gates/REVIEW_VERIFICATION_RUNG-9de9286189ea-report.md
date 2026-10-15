# Independent verification rung review — REVIEW_VERIFICATION_RUNG-9de9286189ea

## Scope and integrity

Reviewed submission `reviews/verification/EXECUTE_VERIFICATION_LADDER-956fdb75fa6b/receipt.json` for author task `EXECUTE_VERIFICATION_LADDER-956fdb75fa6b` at checkout revision `60132e257bdd93fcf2a4cfe34828e482b20b7fbd`. The submission points to `reviews/verification/EXECUTE_VERIFICATION_LADDER-956fdb75fa6b/artifact.json`; its SHA-256 is `f78257b516195f1883131a9bf8758ebba73df0a4dbdc1f8b6fa9b85404183621`, matching the receipt. The embedded content digest matches, and all 37 declared source pins match this checkout.

The accepted predecessor is `reviews/gates/REVIEW_VERIFICATION_LADDER-954fe316bda6-receipt.json`, disposition `ACCEPT_WITH_CLARIFICATIONS`. It authorizes only `ARITHMETIC-MODEL-BOUND`, using `window_integer_bound/v1` with `window=32`, `max_sample=4095`, and `bits=32`, binding `MODEL_ONLY` and maximum conclusion `MODEL_EVIDENCE`. The execution artifact reports that same rung, claim, parameters, binding, and model scope.

## Rung review

The reported integer arithmetic is consistent with the declared formula:

- `4095² = 16,769,025`.
- `32 × 4095² = 536,608,800` for the final 32-sample sum.
- `33 × 4095² = 553,377,825` for the add-before-subtract intermediate under the stated valid-sum invariant.
- The unsigned 32-bit capacity is `2³² − 1 = 4,294,967,295`; both the final sum and intermediate are below it.

The deterministic check `python3 tools/verification_kernel.py check --artifact reviews/verification/EXECUTE_VERIFICATION_LADDER-956fdb75fa6b/artifact.json` returned `INTEGRITY_CHECKED_NOT_ACCEPTED`. That establishes structural and reference integrity as implemented by the kernel, not theorem acceptance. The adapter is a Python reference calculation. Its result is conditional on legal unsigned inputs and a valid sum-of-squares state. It does not establish those premises for project C, C integer promotions or expression evaluation, domain enforcement, generated code, target memory, publisher continuity, or product behavior.

The execution correctly records `product_verified: false`, `requested_claim_status: NOT_DISCHARGED`, no counterexample, and no discharged VOs. VO-002 through VO-006 remain open. The other 20 ERS claims remain unplanned/open under the accepted plan. No result here is evidence that any implementation or hardware test ran.

## Finding

**F-RUNG-CLAR-001 (clarification):** Treat this result only as conditional mathematical model evidence for the declared bound and premise. Retain all concrete C, target, integration, publisher, and product correspondence obligations as unresolved. Preserve VO-002 through VO-006 and the 20 unplanned claims as open; this review discharges none.

## Disposition

**ACCEPT_WITH_CLARIFICATIONS.** Accept the exact bounded model result within its `MODEL_ONLY` scope. The arithmetic and artifact integrity checks are reproducible, while mathematical acceptance of the premise and any implementation correspondence remain outside this result. This rung review is terminal for the present VK-001 slice. Any further verification activity requires a separately authorized scope; do not infer product acceptance or update VO/AD state from this receipt.
