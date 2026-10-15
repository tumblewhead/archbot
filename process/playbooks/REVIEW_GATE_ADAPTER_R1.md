# REVIEW_GATE_ADAPTER_R1: independently challenge FR-002 authority roots

**Operation:** `REVIEW_GATE_ADAPTER_R1`  
**Role:** `verification-agent`  
**Scope:** `FR002_GATE_ADAPTER_R1_IMPLEMENTATION_REVIEW_ONLY`  
**Status:** Awaiting distinct independent review execution. This playbook is not a favorable verdict.

## Entry: provenance and independence

1. Read `AGENTS.md`, `PROJECT_SPINE.md`, `process/pull_run_push_contract.v1.json`, `docs/REVIEW_EXECUTION_MODES.md`, `agents/verification-agent.md`, this manifest, and the bounded FR-002 authorization.
2. Read the **original** `REVIEW_FR002_GATE_ADAPTER_001-report.md` and `-receipt.json`, including its **REVISE** verdict and reproduced `FR002-AUTH-001` policy-repin bypass plus `FR002-AUTH-002` forged review warning. Read `FR002_GATE_ADAPTER_R1-authoring-report.md`. Do not rewrite the original review, failed fixture logs or test receipt.
3. Verify the **R1** human receipt at submission commit `d7649b4a9df40a717b3c4fe1c0cb6b73328c8132`, with Git blob SHA-1 `785376703e6bb0775dfd808013b484458ff69bb6`. It must report `FR-002-GATE-ADAPTER-R1`, tested source `4c1810ecf520a7c2741c4a517532d05f1ee595fd`, exactly ten checks with actual exit codes, log hash/byte declarations, all eight `source_git_blob_sha1` values and SHA-256 fields, and `independently_reviewed:false`.
4. Read all eight source/test files from the **pinned source revision**, not a future working tree. Independently check their Git blob SHA-1 and SHA-256 against both the review manifest and producer receipt. Confirm prior accepted inputs and VO/AD ledgers remain unchanged; scope authorization never meant authority to rewrite them.
5. Establish a reviewer invocation genuinely separate from the source author and producer. In an existing separately invoked Codex, call `python tools/task.py inspect --manifest process/tasks/REVIEW_FR002_GATE_ADAPTER_R1-001.yaml` then `render`, and perform review **inside that invocation**. From an ordinary host shell, use `task.py run`, recording whether an actual Codex reviewer turn completed. Do not launch nested Codex reflexively or equate `render` with review execution.

## Adversarial review

**A1: Exact authority-root identity.** Check that `tools/gates/authority_roots.py` is part of the pinned reviewed engine source, not selected or rewritten by a candidate binding. Confirm approved Toy 1 policy, independent baseline review, independent AS review, active baseline, reviewed AP reconfirmation, active VO and AD ledgers, declared spine, C-002 scope and validator implementation identities. Check all linked reviewed source identities are meaningful, not just well-formed hashes.

**A2: Reproduce the original policy-laundering attack.** In a temporary project copy, mutate `protected_scope_decisions: []`, recompute the policy Git blob hash, omit the C-002 validator and rewrite the candidate binding. Verify that **the bound `load_binding/evaluate_bound` path now rejects it before eligibility**. Distinguish a genuinely executed negative probe from a test that merely asserts an error of any kind. Try retaining the validator while substituting a different approved scope and rehashing it. Inspect direct calls to `common.evaluate` and `stage_gate.evaluate`: clarify which are intentionally *not* authority-bound and whether any production route bypasses the binder.

**A3: Forge coherent baselines/reviews/ledgers.** Mutate a baseline and baseline review together so both re-pinned bytes and candidate names match; forge the approval boolean or review disposition. Mutate and re-pin VO or AD ledgers. Change the project ID/spine and substitute a project-owned policy from a second project. Verify the production loader rejects every path. Examine the new `authority_roots` fixed implementation identity and whether the loader verifies the *actual loaded Python module* against that pin (as opposed to only a matching file at a declarative path). If the effective code or trust registry can be changed while the candidate still passes, classify the real threat boundary.

**A4: Independent review provenance and bootstrapping.** A trust registry inside the same Git checkout is only meaningful if the reviewer or runtime has an independently established **trusted engine revision**. Ask: who authorizes updates to the registry, and what stops an untrusted actor from editing both registry and policy simultaneously? The stated model excludes arbitrary engine replacement; test whether the advertised protection depends on that exclusion. ROOT-002 may pass only the synthetic common-mechanics canary; it must **not** become independently authorized by fabricated review metadata. Any claim of cleanroom, cryptographic provenance or universally generic accepted-project support is out of scope.

**A5: Behavioral regressions.** Confirm the 2048-byte C-002 SRAM envelope, seven approved charged categories, positive margin, scope authority and missing required validator still block correctly. Reproduce the original Toy 1 negative gate tests and the new re-pin attacks. Run:
`python -m unittest discover -s tests -p 'test_fr002_r1_review_route.py' -v`,
`python -m unittest discover -s tests -p 'test_gate_adapter.py' -v`,
`python -m unittest discover -s tests -p 'test_stage_gate.py' -v`,
`python -m unittest discover -s tests -p 'test_task.py' -v`,
`python -m unittest discover -s tests -p 'test_fr002_review_route.py' -v`.
Record real exit codes and counts. Optional regression expansion should be labeled, not invented.

**A6: Evidence and authority limits.** If `runs/fr002-gate-adapter-authority-r1/` contains all ten local logs, verify their bytes and SHA-256 hashes against the human receipt. Otherwise label them `PRODUCER_REPORTED_ONLY` and independently reproduce the relevant tests. Reconfirm `FR002-AUTH-001` and `FR002-AUTH-002` are addressed only within the binding's trusted-engine threat model. A passing test suite does not prove AP approval, final F-001 ranking, C/firmware correctness, target SRAM fit, cleanroom isolation or VO discharge.

## Independent outputs and disposition

Write **only**:
- `reviews/qualification/REVIEW_FR002_GATE_ADAPTER_R1_001-report.md`
- `reviews/qualification/REVIEW_FR002_GATE_ADAPTER_R1_001-receipt.json`

Use `pc-framework-repair-review/v1`. Include task ID, operation, reviewer invocation/mode and actual independence evidence; original `REVISE` identity; source and evidence commits/blobs and independently verified SHA-1/SHA-256; A1–A6 evidence classes (`REVIEWER_REPRODUCED`, `REVIEWER_INSPECTED`, `PRODUCER_REPORTED_ONLY`, `NOT_PERFORMED`); material findings and **disposition** from `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `UNRESOLVED`; precisely scoped rationale and next eligible action. Preserve the previous rejection as historical truth.

Always retain `framework_frozen:false`, `cleanroom_authorized:false`, `product_verified:false`, `vo_discharged:[]`, open VOs `VO-002` through `VO-006`, and no target configuration or final F-001 completion. The review can accept the bounded implementation but **cannot authorize FR-003 source work or framework freeze**. On a verified bypass or unverifiable authority, return `REVISE`/`UNRESOLVED` with reproduction rather than greenwashing the result.
