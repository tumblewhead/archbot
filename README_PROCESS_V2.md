# Progressive Concretization v2: Process repair

This update is an incremental overlay for the pilot repository, **not** a replacement
for the user's live Codex checkout. It does not rewrite AE-001, AE-002, EP-001,
EP-002, PR-002 or the original AS and F. The EP-002 review ZIP motivated it.

## Changes

- Explicit provisional AP commitment and separate final acceptance gate.
- Tracked Architectural Debt separate from Verification Obligations.
- Stage-specific admissibility policy that preserves original F-001 final dimensions.
- C-002 interpretation is **pending an authority decision**. No fabricated approval.
- Declarative workflow and first-class Evidence Planning Agent with bounded spine view.
- Deterministic gate-completeness validator and simulated positive/negative cases.
- Updated root theory_of_operation.md and Codex guidance.

## Apply and verify (after backing up/committing local work)

    git apply --check pc-process-v2.patch
    git apply pc-process-v2.patch
    python tools/attach_process_spine.py
    python tools/pc.py check --fast
    python -m unittest discover -s tests -v
    python tools/stage_gate.py inspect
    python tools/stage_gate.py evaluate --assessment process/examples/ap-assessment-template.yaml

The final evaluate currently returns NO_DOWNSELECTION (exit 2) by design,
because C-002 scope is not yet authorized and the example is not an evaluated AP.

## Next step

First obtain an explicit C-002 accounting decision. Also reconcile the prior
AS-due VO-001 acceptance with an independently reviewable receipt using
`prompts/13-vo-reconciliation.md`; it is deliberately left `open` in the
conservative ledger until accepted evidence is attached. Review
`process/decisions/C-002-scope.yaml` and `prompts/11-scope-authority.md`.
After authorization, run `prompts/12-ae003-provisional.md`. A `NO_DOWNSELECTION`
result until the required approval/evidence exists is correct behavior.

The tool checks record completeness and status discipline, not mathematical or
hardware truth. Every architecture decision still needs independent review.

The patch deliberately does not overwrite the local `AGENTS.md` or AS spine.
Your existing `AGENTS.md` rule about optional theory reading is preserved; the
updated role files and policy control the new decisions. Run the spine-attachment
script once after applying (it is idempotent).
