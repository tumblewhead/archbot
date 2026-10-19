# CLN-001 Stage 12: independent audit of IF11's new evidence

The five raw IF11 files were pushed at
`1baf0d1fc03c67fc181341e8f53dac9011581c52`.
The author reported 14,327 successful finite-model checks, one
intentionally failing in-memory 256-bit wrap mutation, S synchronous
rank-association and X exact-frame candidate decoders, and a
conditional `2^m` outstanding-result information family.
**None of these is an accepted physical interface or theorem.**

The next action is a **distinct independent review of this NEW
evidence**, not another review of unchanged UNKNOWN. The
[review task](TASK-REVIEW-IF11-012.md) requires exact model replay,
assumption/theorem-scope audit and narrow counterexample challenges.
All A/B/C remain UNSELECTED, full H1–H6/F unknown.

## 1. Pull and prepare

Run in your real Archbot repository checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD

bash -n reviews/diagnostics/CLN-001-TASK-012/prepare_if11_review012.sh
bash -n reviews/diagnostics/CLN-001-TASK-012/archive_if11_review012.sh
bash reviews/diagnostics/CLN-001-TASK-012/prepare_if11_review012.sh
```

STOP on nonzero exit; do not delete existing workspace, force-push
or reset unrelated work. Source preparer checks exact Git blobs,
the IF11 SHA-256 manifest and the original synthetic BKP identities.
It creates `$HOME/archbot-cln001-if11-review-012`.

## 2. NEW independent Codex reviewer

In a new terminal, not `codex resume`:

```bash
cd "$HOME/archbot-cln001-if11-review-012" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Inspect the IF11
> trace-model source before execution; independently reproduce the
> 14,327-case output and the controlled mutant if safe/reconstructible.
> Challenge S and X actual consumer information, the 2^m unpaid-result
> information bound with its explicit hypotheses, reset/acceptance/
> retry state, unavailable C provider, F ownership and every open
> realization obligation. Distinguish positive finite evidence from
> complete AP/target feasibility. Write ONLY
> out/REVIEW-IF11-012.md and out/REVIEW-IF11-012.json. STOP.
> Do not choose an AP, authorize RI/RN/C-HIST or change AS.

The outputs are not verified until the review actually runs.

## 3. Exact selective archive / push

Once both output files exist, from the real checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-012/archive_if11_review012.sh
git show --stat --oneline HEAD
```

The restartable archive validates JSON disposition and no-selection
flags, preserves original reviewer bytes and SHA-256, stages ONLY its
two reports and checksum, commits if new and pushes this branch.

## Next engineering progression

After the actual review, the CLN-001 delegate may separately
accept narrow IF11 evidence and authorize the next concrete
interface/owner feasibility proof or chosen-width C A/B numeric
prototype. A favorable review is not automatic selection.
Keep [process improvement lessons](../../../docs/CLN001_PROGRESS_GAP_AND_ORCHESTRATOR_PILOT_001.md)
for a later orchestrated replay. Do not repeat endless
source reviews without new decision-relevant experiments.
T002-2..8 OPEN, R4 deferred, no formal cleanroom/product VO discharge.
