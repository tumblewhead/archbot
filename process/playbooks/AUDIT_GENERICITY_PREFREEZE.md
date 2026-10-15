# AUDIT_GENERICITY: prefreeze framework qualification audit

**Role:** architecture-agent
**Operation:** AUDIT_GENERICITY
**Entry:** explicitly assigned, versioned manifest pointing to the final
scoped Toy 1 host-resource independent review.
**Stage:** investigation and report only. This does NOT freeze the framework,
accept Toy 1 product, authorize a cleanroom replay or close VOs.

## Purpose

Evaluate whether Progressive Concretization can be frozen as a reusable,
project-isolated process before its first fresh Toy 1 replay. The cleanroom
will test whether a new agent can recover architecture from authorized
problem inputs without carrying forward Toy 1 solution files, chat history
or prior decisions. Audit both missing generalization and source leakage.

## Required sources

Read `AGENTS.md`, `PROJECT_SPINE.md`,
`docs/QUALIFICATION_CAMPAIGN.md`,
`docs/VK001_TERMINAL_CHECKPOINT.md`,
`docs/REVIEW_EXECUTION_MODES.md`,
`process/pull_run_push_contract.v1.json`,
all independent reviews directly pertinent to the VK-001/VC-001/VR-001
chain, and only the relevant engine/role/playbook/test sources.
Do not assume historical "not started" lines supersede current
reviewed receipts.

## Audit checklist

**Q1: Execution and independent review orchestration.**
- Independently identify registered `task.py run` and `task.py render`
  behavior. Preserve the VC-001 and VR-001 failures: zero reviewer turns
  after nested Codex launch failed, read-only app-server reported.
- Classify outer-shell Codex launch vs direct current-agent execution.
  A direct reviewed receipt does not retroactively make a failed
  registered runner successful. Record whether either mode has *actual
  tested evidence* of working for cleanroom.
- Confirm that role registry points to existing role/view/playbook files.
  Test and document a missing-role negative control if useful.

**Q2: Cross-project isolation.**
- Identify any hardcoded AS-001, C-002, target/ADC or Toy 1 paths in
  shared telemetry, task runners, stage gates and generic prompts.
- Propose minimum generic engine/domain-policy split and a cross-project
  canary for Toy 2. Mark untested isolation as BLOCKED or UNRESOLVED,
  not PASS.

**Q3: Authority and evidence integrity.**
- Check review independence, exact subject/source pins, scope maturity,
  model-vs-compiled-C-vs-target distinctions, and VO/AD update rules.
- Check historical-verification pin behavior after a source update.
  Current-worktree pin validation cannot replace a versioned archive
  auditor. Preserve immutable accepted evidence.
- Check stale inherited ERS questions and PENDING author artifacts
  displayed alongside later favorable reviews. No status mutation
  may edit historical artifacts.

**Q4: Cleanroom contamination and reproducibility.**
- Define allowed cleanroom input pack (authorized BKP/problem and
  engineering authority constraints, approved generic process code,
  selected independent acceptance rubric) separately from forbidden
  prior Toy 1 solution, private run output, reviewer receipts,
  complete old `PROJECT_SPINE.md`, and prior agent/chat reasoning.
- Explicitly record where the correct process currently requires old
  `knowledge/architecture/AS-001` files and why simply cloning
  current `main` would violate cleanroom isolation.
- Audit whether a fresh project can be initialized without hidden
  tool assumptions. No cleanroom run is permitted by this audit alone.

**Q5: Qualification gates and remaining Toy 1 scope.**
- Record completed abstract/provisional/contract/DE/host milestones
  from reviewed receipts, not the stale historical matrix alone.
- Record VO-002 through VO-006 open, target unset, F-001 final comparison
  outstanding, with a documented host-only limit.
- Distinguish user permission for host-focused development from final
  target acceptance. State whether host-qualified-only Toy 1 can be
  closed as an explicit scoped milestone; do NOT do that automatically.

**Q6: Human friction and readiness.**
- Identify at least the observed two runner failures and missing role
  canary as process friction. Do not fabricate human-minutes metrics.
- Rank blockers by cleanroom contamination risk and reusability impact.
  Recommend smallest repair plan and order of checks.

## Deliverables (versioned, additive)

- `reviews/qualification/GENERICITY_PREFREEZE_001-report.md`: a
  source-backed concise matrix with each Q1..Q6 assessed
  `PASS`, `BLOCKED` or `UNRESOLVED`, evidence paths, actual
  reproduced tests, proposed minimal repairs, explicit non-claims, and
  separation of the framework from Toy 1 requirements.
- `reviews/qualification/GENERICITY_PREFREEZE_001-receipt.json`:
  schema `pc-genericity-audit/v1`, task ID, project/spine, exact
  invocation, source revision, applicable inspected source hashes,
  classifications, outstanding blockers, `freeze_authorized:false`,
  `cleanroom_authorized:false`, `product_verified:false`,
  `vo_discharged:[]`.
- Independent review of this audit must happen in a **separate**
  later task. Successful creation of these files is not acceptance.

## Safeguards

No AS/AP/F/CON/DE edits, firmwares, target guess, VO/AD mutation,
review rewrites, invented product guarantees, or cleanroom leakage.
No unnecessary large-run artifact reading. Do not use a blanket
"all green" summary to conceal an unknown target or failed review
launcher. If a requested fact cannot be established from source, mark
UNRESOLVED with a precise required experiment or authority input.
