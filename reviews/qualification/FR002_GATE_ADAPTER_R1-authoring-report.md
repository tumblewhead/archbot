# FR-002 R1: engine-root policy and review provenance correction

**Origin:** `REVIEW_FR002_GATE_ADAPTER_001`, disposition **REVISE**, commit `eb5753a371632fbc093811b09a7c70bea458fc60`.
**Human authority:** Existing `FR-002-GATE-ADAPTER-AUTHORIZATION-001`; reviewer requested a bounded correction to project/source authority enforcement.
**Status:** Source candidate only. Neither local tests nor a new independent review have been executed.

## Repaired trust boundary

The old `gates.binding.load_binding()` checked whether a candidate's policy,
baseline and validator references were internally consistent. The reviewer
demonstrated that an attacker could change the policy to remove protected
validators, compute a new Git blob SHA-1 and pass this check.

The R1 code creates `tools/gates/authority_roots.py`, an *engine-owned*
registry for the already approved Toy 1 source authority. It pins accepted
policy, independent baseline and AS reviews, active baseline, AP
reconfirmation, active VO/AD ledgers, spine and C-002 scope/validator
implementation identities. Candidate bindings cannot change these roots
by changing their own hashes.

The loader now (1) rejects a project absent from the engine authority
registry; (2) compares candidate paths and blob IDs against the trusted
authority root *before* following candidate-provided policies; (3) reads
and checks the reviewed baseline, independent AS review and AP
reconfirmation provenance at source identities that the binding cannot
override; and (4) requires the approved C-002 protected requirement and
validator set, even when the candidate policy attempts to omit them.

New negative canaries exercise re-hashing an unprotected Toy 1 policy,
forging a baseline/review pair with matching internal hashes, re-pinning
a VO or AD ledger, and asserting a forged second-project review. These
must fail before evaluator eligibility is returned.

## Explicit synthetic-project limit

`ROOT-002` remains a *pure structural* canary. It calls
`gates.common.evaluate` with a synthetic in-memory model, thereby
demonstrating reusability of generic mechanics and its own checks.
The production authority-bound loader must **reject ROOT-002** because it
has no independently approved engine authority root. A future project
must be explicitly reviewed and registered; it cannot authorize itself.

This does not transform repository hashes into digital signatures or
protect against arbitrary replacement of trusted engine code. The
trust root is anchored in versioned, independently reviewable engine
source and preexisting accepted authority artifacts. Changes to that
root require a separate authorized revision and independent review.

## Preserved work and next checks

No accepted AS/AP/F/CON/DE, firmware, product scope, active VO/AD ledger,
prior reviewer receipt, or historical evidence was changed. The common
gate and Toy 1 memory-envelope validator remain in place.
`test_stage_gate.py` preserves the original Toy 1 negative cases.
Source/tests are not yet qualified.

**Next local run:** targeted `test_gate_adapter.py`,
`test_stage_gate.py`, `test_task.py`,
`test_fr002_review_route.py`, and the previous FR-001 canaries;
`tools/stage_gate.py inspect --binding
process/gate_configs/AS-001-AP-v1.yaml` and explicit
`--legacy-toy1` inspection. Capture command exits and hashes in a
*new* `FR002_GATE_ADAPTER_R1-local-test-receipt.json` only if checks pass.
A **different independent reviewer** must audit provenance and adversarial
re-pinning, not just count passing tests.

Authority limits: `framework_frozen=false`,
`cleanroom_authorized=false`, `product_verified=false`,
`vo_discharged=[]`, VO-002 through VO-006 remain open.
