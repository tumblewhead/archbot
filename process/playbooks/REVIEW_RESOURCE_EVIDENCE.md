# REVIEW_RESOURCE_EVIDENCE: independently assess resource observations

**Operation:** `REVIEW_RESOURCE_EVIDENCE`
**Role:** `verification-agent`
**Entry:** versioned resource-evidence candidate, pinned source, reviewed
project authority, explicit task manifest.
**Authority:** scoped evidence review only. NOT VO discharge or target acceptance.

## Procedure

1. Read `AGENTS.md`, `PROJECT_SPINE.md`, this manifest and exact submitted
   resource record. Check the input source revision, Git blob identity, all
   source SHA-256 pins, project spine and the reviewed C-002 scope.
2. Inspect the *actual* `sizeof`/`offsetof` host layout observation and
   submitted commands. If raw logs are accessible locally, hash-check and
   inspect them. If not, say so and optionally reproduce with a new isolated
   `runs/` directory. Neither an author's PASS string nor structural
   integrity alone constitutes an independent measurement.
3. Compare field sizes and offsets against the real `detector_t` declaration
   and accepted CON/DE. An object-size result is host-compiler/ABI dependent;
   it is neither the target structure size nor total detector-attributable
   SRAM, and it is not the F-001 state-SRAM merit quantity.
4. Check the *seven* accepted conditional charged-SRAM category ceilings:
   persistent 256, temporary 128, stack 512, interrupt context 256, shared
   256, dynamic 128, and other 256 bytes, total 1792, with 256 reserve below
   the 2048-byte C-002 ceiling. These are binding allocation commitments,
   NOT measured usage or proved feasible target allocations.
5. Check that each actual **target** category peak is unknown (`null`) in
   this host-only record. No stack/context nesting, overlap/lifetime,
   dynamic/shared attribution, target ABI, linker map or final image is
   available from this observation. Do not interpret a missing value as zero.
6. Preserve the separate accepted DE element subceilings as *proposed*
   ownership partitions; if infeasible in a selected integration, request
   reviewed design/budget revision. Do not invent an ISR/task topology,
   require a heap prohibition, infer an absent shared allocation, or change
   accepted source requirements.
7. Review the explicit evidence/claim limitations and all VO/AD/F boundaries.
   If source pins, domain, data or statements disagree, return REVISE or
   UNRESOLVED. If sound, accept the HOST-ONLY observation with
   clarifications and leave VO-002 through VO-006 OPEN.

## Outputs

Write **only** new files:
- `reviews/gates/<task-id>-report.md`, source-backed review and concise
  engineering briefing.
- `reviews/gates/<task-id>-receipt.json`, schema
  `pc-resource-evidence-review/v1`, fields:
  `task_id`, `operation`, `project_id`, `spine`,
  `submitted_evidence`, `submitted_evidence_git_blob_sha1`,
  `submitted_source_revision`, `reviewer_invocation_id`,
  `independent_of_authoring_invocation`, `checks`, `findings`,
  `disposition` (ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE, UNRESOLVED),
  `disposition_scope`, `next_eligible_action`,
  `product_verified:false`, `vo_discharged:[]`,
  and the unchanged list of open VOs.

Report which checks were producer-reported, reviewer-inspected, and
reviewer-reproduced. Do not claim the registered Codex runner succeeded
unless a reviewer turn actually completed through it. A direct independent
review, if needed, must be separately identified as such and the launcher
defect must remain visible.

Never modify accepted requirements, source, implementation, VO/AD ledgers or
this submitted record to force an acceptance. The review receipt alone does
not authorize target qualification or any automatic next task.
