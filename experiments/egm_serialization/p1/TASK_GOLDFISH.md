# EGM-P1 proposed fresh-agent reconstruction task

**Role:** Goldfish, a fresh agent with no Elephant conversation, no
knowledge of previous implementations, no evaluator-only reference.

**Status:** EXPERIMENT PROPOSAL. The EGM-P0 code has author unit-test
evidence but awaits distinct review before this P1 task can be
treated as an authorized general process gate.

Read `AGENTS.md`, `SPINE.md` and `inputs/SHA256SUMS`, then traverse
only the three explicitly referenced `inputs/` sources.

These are **proposed process architecture documents**, not approved
engineering contracts or implemented services. Preserve proposal
versus acceptance. Do not infer activation from names or from a
successful test. If a necessary fact is absent, report UNKNOWN.

## Reconstruction

Independently reconstruct the model of the proposed offline Archbot
harness, its authority boundaries, EGM reconstruction test and
linkable skeleton rule. A spine is a *traversal root*, not a complete
specification. You must follow required source links.

The vocabulary of candidate fact IDs is defined in `SPINE.md`.
Its purpose is to make independent reconstructions structurally
comparable; **the fact types, authority states, proof assumptions
and typed dependency relations are NOT provided in advance**.
Derive them from the referenced content.

Output ONLY `out/GOLDFISH_RECONSTRUCTION.json` with schema
`pc-egm-goldfish-reconstruction/v0`, `project_id` matching
the spine, `traversed_source_ids` for what you actually read,
`facts` entries each containing `id`, `kind`, `authority`,
`source_ids`, optional `proof_conditions`, `relations` entries
(`from`, `type`, `to`), and `unknowns` with
`id`, `reason`, `source_ids` if applicable.

Allowed fact kinds: `REQUIREMENT ASSUMPTION PROOF CONTRACT MODULE
INTERFACE IMPLEMENTATION RESOURCE VERIFICATION`.
Allowed authority values: `PROPOSED ACCEPTED UNRESOLVED REVIEWED_ONLY`.
Allowed relation types: `DEPENDS_ON REFINES IMPLEMENTS PROVEN_BY
TESTED_BY OWNS PROVIDES CONSTRAINS`.

Also output ONLY `out/GOLDFISH_BRIEFING.md`, documenting which
sources you traversed, any ambiguous owners/dependencies, missing
proof scope, requested clarifications, and whether you needed
information absent from the projection. Be explicit when a guessed
edge cannot be established.

Do not inspect the evaluator's `REFERENCE.json`, the containing
repository, `../auditor_only`, other workspaces, Git, chats,
connected apps, or networks. Access-control isolation is NOT proven
by a new directory. STOP after producing the two outputs.
