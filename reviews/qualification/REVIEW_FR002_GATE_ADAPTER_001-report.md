# Independent FR-002 gate adapter review

**Task:** `REVIEW_FR002_GATE_ADAPTER-001`  
**Scope:** `FR002_GATE_ADAPTER_IMPLEMENTATION_REVIEW_ONLY`  
**Disposition:** `REVISE`  
**Execution:** `CURRENT_AGENT_DIRECT`; task inspected and rendered, then reviewed in this existing invocation. No nested `task.py run` was used. This invocation is separate from the source author and human test producer.

## Identity and evidence

Checkout HEAD was `61bdc411e3cf88396e2489d1111c04ee3f5258a0`; the manifest's reviewed source revision is `3c2fd85cb0bde0c13b7639e24220143e26344536` (implementation first landed at `57f69f5b2d8d69de876aa72649e8aa5f783ef4e9`). The current checkout is later than the reviewed source. Historical Git objects were used for the seven source comparisons; all seven SHA-1 blob IDs and SHA-256 values match the manifest/producer receipt. The submitted evidence commit `c0cc00658c9afdc3eea111905b131a272d87863c`, receipt blob `531ba3bf4d713a45a2e669e26b2e888da4c3f0a9`, schema, and source revision match. All nine available producer logs match their declared byte counts and SHA-256 values. These verify the receipt's recorded executions, not their engineering conclusions.

The active baseline and VO/AD ledgers, accepted authority inputs, and historical independent-review receipts remain unchanged relative to the submitted source revision. The corrected local receipt remains distinct from the earlier failed fixture run.

## Checks and findings

| Area | Result | Evidence |
|---|---|---|
| G1 common/domain separation and legacy behavior | `REVIEWER_INSPECTED` | Common gate has no Toy 1 resource constants. Toy 1 validator retains seven categories, positive margin, and scope checks. Legacy Python API is explicitly Toy 1-only; CLI requires binding or explicit legacy mode. Regression suite passed. |
| G2 fail-closed validator dispatch | `REVIEWER_REPRODUCED` with defect | Existing missing/duplicate/unknown/wrong-project cases reject. However, policy authority is not anchored independently; see finding F1. Direct use of `common.evaluate` also relies on callers to supply the validator set; the bound CLI path calls `load_binding`. |
| G3 authority laundering | `REVIEWER_REPRODUCED`, FAIL | In an isolated synthetic copy, changed `protected_scope_decisions` to `[]`, recomputed the policy blob ID and binding, removed the validator declaration, and `load_binding` accepted the altered policy with zero validators. A hash proves byte identity only; this loader checks self-consistency, not that policy bytes or review provenance descend from independently established authority. |
| G4 fresh project/evidence boundary | `REVIEWER_REPRODUCED` with scope limit | ROOT-002 structural canary passes and rejects wrong spine, but its baseline, review, and policy are synthetic self-assertions. It demonstrates routing syntax, not authorized provenance. Same authority weakness as F1. |
| G5 CLI/backward compatibility and labels | `REVIEWER_INSPECTED` | Explicit binding/legacy modes and eligibility wording preserve the stated limits. Historical `evaluate` remains Toy 1-specific. |
| G6 evidence and history | `REVIEWER_REPRODUCED` | Five required suites: FR002 route 3, gate adapter 10, stage gate 13, task 44, FR001 R1 route 3; all exit 0 (73 tests). Nine producer log hashes/byte counts match. Prior failed fixture evidence is preserved. |

### F1 — self-repinned policy can remove a protected validator

**Severity:** blocking for this scoped review. `load_binding` trusts `protected_scope_decisions` from the policy path and a binding supplied with that policy's recomputed blob ID. It checks the validator list against that same candidate policy, but does not compare policy identity/content and review provenance to an independent accepted authority root. The counterexample passed `load_binding` with no C-002 validator. Consequently the gate can skip a domain check while every supplied hash remains internally consistent. The ROOT-002 fixture's forgeable baseline-review booleans show the same provenance limitation for synthetic bindings.

Repair must anchor the binding to an independently authorized policy and accepted review provenance (with a fail-closed identity check); merely adding another self-asserted hash or boolean is insufficient. Add adversarial tests that re-pin a weakened policy and forge baseline/review and active ledger evidence, and show each is rejected. Preserve the current implementation and receipts as history; submit a new versioned candidate and evidence for review.

## Structural results and scope limits

`python tools/task.py inspect` and `render` succeeded. The five test commands above all passed. The isolated policy-repin probe reproduced F1. Test success and matching hashes establish structure and provenance of submitted bytes only; they do not establish policy authority, mathematical proof, C/firmware correctness, product verification, or stakeholder approval.

The gate remains scoped to this implementation review. `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`; VO-002 through VO-006 remain open. No target configuration is selected, final F-001 comparison remains outstanding, and AD-003 is unchanged.

**Next eligible action:** repair authority-root/provenance validation and add the adversarial rejection cases, then submit a new FR-002 candidate and local evidence for independent review. No freeze, cleanroom, VO discharge, AD acceptance, or product qualification is authorized by this result.
