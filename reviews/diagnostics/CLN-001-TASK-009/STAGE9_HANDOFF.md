# CLN-001 Stage 9: independently evaluate three unselected AP candidates

## Accepted authority for this stage

R1 focused review pushed as commit
`698c162e624df0faab640ef294a1bea63997981e`, with disposition
`READY_FOR_DELEGATED_AS_ADDENDUM_DISPOSITION`. The CLN-001-only sponsor
delegate issued [AS-ADDENDUM-008-R1-DISPOSITION](AS-ADDENDUM-008-R1-DISPOSITION.yaml),
which **accepts only** the additive interface interpretation for this
synthetic diagnostic. The original activated AS remains unchanged.

The distinction now binding is that exactly indexed energy must reach
the actual consumer, not merely be reconstructible by an external trace
observer; reset requires correct observable old/new association but no
specific acknowledgment event. Accepted-event debt cannot be canceled
by a fault report or reset. No RI, RN or C-HIST implementation or
service is approved. Candidate A/B/C remain UNSELECTED.

[Stage-9 evaluation scope](AP-EVALUATION-SCOPE-009.yaml) and
[TASK-AP-EVALUATION-009](TASK-AP-EVALUATION-009.md)
authorize bounded independent model, dependency and symbolic F
feasibility work. Evaluation is **not** AP selection, firmware source
production or target qualification.

## Step 1: pull current branch and prepare new evaluator

Run in actual Archbot checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD
bash -n reviews/diagnostics/CLN-001-TASK-009/prepare_ap_evaluation009.sh
bash -n reviews/diagnostics/CLN-001-TASK-009/archive_ap_evaluation009.sh
bash reviews/diagnostics/CLN-001-TASK-009/prepare_ap_evaluation009.sh
```

STOP if `git pull --ff-only`, Bash syntax, source-blob checks or BKP
SHA-256 checks fail. Do not reset/stash/force-push unrelated work or
delete an already created evaluator directory just to retry.

This creates `$HOME/archbot-cln001-ap-eval-009`, checks pinned inputs
and provides a positive-allowlist workspace, not OS-level cleanroom
proof. Do not run an old Codex resume session.

## Step 2: fresh independent evaluator

Start a NEW terminal:

```bash
cd "$HOME/archbot-cln001-ap-eval-009" || exit 1
codex
```

Give Codex this prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently evaluate
> the three UNSELECTED AP candidates A/B/C under the accepted synthetic
> original AS, R1 additive AS disposition, D002, accepted F and
> conditional T1/T2. Perform source-grounded numeric model checks if
> useful. Separate conditional numeric feasibility from consumer-index
> and reset/output-debt feasibility, full RAM ownership, typed compute
> and device-energy unknowns. Record service dependencies, falsifiers,
> actual test evidence and economical next evaluations; no selected AP,
> no invented service, no target qualification or implementation.
> Write ONLY the three evaluation outputs named in TASK.md and STOP.

Expected output names (not yet verified):
`out/AP-EVALUATION-009.md`,
`out/AP-EVALUATION-009.json`,
`out/AP-EVALUATION-BRIEFING-009.md`.

## Step 3: selectively archive and push actual evaluator evidence

After all three raw outputs exist, use the original checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-009/archive_ap_evaluation009.sh
git show --stat --oneline HEAD
```

The archive is restartable, retains byte-for-byte original evaluator
outputs and SHA-256 hashes, validates JSON no-selection/qualification
flags, refuses unrelated staged changes, commits only the required
three reports and manifest and pushes the experiment branch.

## Next gate

After the push, assistant reads the full evaluation, verifies source
identities and checks, prepares a **distinct independent evaluation
review** (Stage 10), and only after review may propose an
explicitly authorized *reversible provisional* AP commitment or
further evidence task. No AP selection is automatic.

Keep H1-H6 realized compliance UNKNOWN unless appropriately qualified
evidence proves otherwise. Unknown F measured axes are not zero, PASS
or favorable ties. T002-2..8 remain OPEN, R4 detection deferred.
No CON/DE/C, old Toy1 solution import, formal cleanroom or product VO
discharge is authorized by Stage 9.
