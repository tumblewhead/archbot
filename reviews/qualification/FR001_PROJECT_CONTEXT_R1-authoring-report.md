# FR-001-PROJECT-CONTEXT R1: bounded source correction

**Parent repair:** FR-001-PROJECT-CONTEXT, human-authorized by `process/decisions/FR-001-PROJECT-CONTEXT-AUTHORIZATION-001.yaml`.  
**Trigger:** Independent `REVIEW_FR001_PROJECT_CONTEXT_001` at commit `8e58c2607dbab9e64668f6f4728b543070387ad6`, disposition **REVISE**.  
**Status:** Remote-source candidate. Local test evidence and new independent review are **pending**. No previous accepted or reviewed artifact is overwritten.

## Counterexamples addressed

| Finding | R1 correction | New local regression |
|---|---|---|
| FR001-R1: symlink alias | The declared spine's lexical path must equal its resolved path; selected relationships also reject symlinked paths and path aliases. This prevents a declared Alpha spine from recording Alpha while selecting Beta. | `test_fr001_r1_symlink_spine_does_not_substitute_project`; `test_fr001_r1_symlink_dependency_does_not_alias_project` |
| FR001-R2: alternate collection | Project-owned nodes must remain under the declared project root across the knowledge tree. The only permitted shared collection is `knowledge/bkp`, reachable through explicit typed relations. Unrelated project collections fail closed. This is an intentionally restrictive FR-001 contract, not a universal future shared-data policy. | `test_fr001_r2_other_collection_cannot_supply_project_evidence`; `test_fr001_explicit_shared_bkp_keeps_mandatory_closure` |
| FR001-R3: missing mandatory edge | After role traversal, validate traversed concepts' relevant edges; a missing or nonlocal mandatory target is an error, not an available partial projection. Optional absent targets keep their original semantics. Do not edit the shared `pc.traverse` implementation in this scoped repair. | `test_fr001_r3_missing_mandatory_edge_is_not_silently_omitted` |

## Limits and review priorities

This path policy allows a declared project under `knowledge/<collection>/<project>/...` to reference only that project and explicitly linked BKP files. Cross-project collaboration or another shared collection requires a new reviewed context-sharing policy; no implicit trust based on matching directory names. The rule prevents selection through adjacent collections but does **not** prove a shared BKP item itself contains no private or prior-solution content. Cleanroom packaging and provenance remain separate qualification tasks.

The role view remains an eligibility estimate, not measured Codex reads. The `pc.catalog()` and `snapshot()` operations, shell/search access to an unfiltered checkout, and cross-project reviewer/evidence identity checks are outside the FR-001 selection claim. `tools/task.py`, stage-gate policy, active AS/AP/F/CON/DE, firmware and VO/AD ledgers are unchanged by R1.

**Reviewer should challenge:** aliasing via a parent directory, a relationship symlink, a URL-valued required edge, missing mandatory targets at traversal depth, and existing explicit Toy 1 BKP closure. Source and tests have not been executed by the connected-GitHub author.

## Local execution and follow-up

Run `test_telemetry.py`, `test_task.py`, `test_genericity_review_route.py`, `test_genericity_audit_route.py`, `test_fr001_review_route.py`, and `test_stage_gate.py`. Run `tools/task.py inspect` on the FR-001 independent-review task. Preserve nonzero results and submit a **new** bounded evidence receipt `reviews/qualification/FR001_PROJECT_CONTEXT_R1-local-test-receipt.json` only after successful execution. Pin this R1 source commit and the revised telemetry/test source hashes. Later route a *new* independent reviewer task; do not retroactively turn `REVIEW_FR001_PROJECT_CONTEXT_001` into an acceptance.

Authority remains: `framework_frozen=false`, `cleanroom_authorized=false`, `product_verified=false`, `vo_discharged=[]`; VO-002 through VO-006 stay open. No FR-002 source work is authorized by this correction.
