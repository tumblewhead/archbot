# VK-001: Deterministic verification authoring

Registered operations: DERIVE_ERS, DESIGN_VERIFICATION_LADDER,
EXECUTE_VERIFICATION_LADDER. All share `pc-verification/v1`.

Read `docs/VERIFICATION_SLICE_VK001.md` for limits and record contracts.
Run through `python tools/task.py run --manifest ...`; the task entry point
uses the deterministic Python kernel, not a nested Codex invocation.

ERS derivation projects the explicit obligation inventory and compares
separate implementation annotations. It does not automatically parse or
prove complete semantic coverage of English AS/CON/DE documents.

Planning validates hand-authored model rungs, sparse hyperedges and distinct
scheduling/premise dependencies. It does not discover arbitrary physics.
Execution runs allowlisted bounded reference adapters only. It does not
compile or execute project C, establish model-to-product correspondence,
run a trusted SMT solver, or discharge VOs.

Each stage writes a new immutable bundle under reviews/verification/<task>/
with artifact.json, briefing.md, and receipt.json. The briefing's status,
subject and scope come from the structured artifact. Review is pending.
Successful process exit does not imply that every rung supported a claim.

Do not edit output artifacts to force a gate, change accepted requirements,
or call this prototype a generic proof checker. After ERS and plan authoring,
independent review of the exact artifact is required before project advance.
The fixture-only demo intentionally bypasses these reviews and is barred from
project gates; it cannot create authority or accepted evidence.
