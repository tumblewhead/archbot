# CLN-001 Stage 10: independent AP evaluation evidence review handoff

The Stage-9 independent AP feasibility evaluation was archived in
`tumblewhead/archbot`, branch `experiment/toy1-pipe-cleaner-001`,
at `0783a3b95a384e4e24b89a68740555055b2383f6`.

Its **reported** finite model totals were 299,296 accepted events,
24,192 rejected attempts, 11,386 resets and 897,888 A/B/C
energy-to-oracle comparisons with zero mismatches. Candidate C's
numeric success presumes a hypothetical exact snapshot provider,
not an authorized or verified physical C-HIST service.

The model also reported 21 witness groups, eight reset/publication
interleavings, a wrong-snapshot read at 31 of 32 cuts, and a
preliminary cursor witness that did not discriminate a faulty
implementation until it was corrected. The actual code, seeds,
test counts and provenance are embedded in
`AP-EVALUATION-009.json`. Reviewer must check/reproduce the evidence
rather than assuming these assertions qualify H1–H6.

The Stage-10 [task](TASK-REVIEW-AP-EVALUATION-010.md) requires a
**separate independent source/evidence quality review**, not AP
selection or an implementation gate. A/B/C remain UNSELECTED;
all realized H1–H6 and measured F values are UNKNOWN. The
accepted AS is the original activated AS-REV-002 plus the scoped,
separately reviewed and delegated-accepted R1 addendum. T002-2..8
OPEN, R4 detection DEFERRED, RI/RN/C-HIST unapproved.

## 1. Pull experiment branch and prepare reviewer

In the **actual** Archbot Git checkout, not a Codex evaluator directory:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1

git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD

bash -n reviews/diagnostics/CLN-001-TASK-010/prepare_ap_evaluation_review010.sh
bash -n reviews/diagnostics/CLN-001-TASK-010/archive_ap_evaluation_review010.sh
bash reviews/diagnostics/CLN-001-TASK-010/prepare_ap_evaluation_review010.sh
```

The preparation script checks named Git blobs, original BKP SHA-256,
Stage-8 R1 review and Stage-9 evaluation evidence manifests, and
creates `$HOME/archbot-cln001-ap-eval-review-010` with only the
source-allowlisted material. STOP on failure. Do not delete a
previous workspace, reset Git, stash unrelated work or force push.
A workspace allowlist is not an OS/connector isolation proof.

## 2. Independent reviewer in a NEW Codex session

In another terminal, not `codex resume`:

```bash
cd "$HOME/archbot-cln001-ap-eval-review-010" || exit 1
codex
```

Give Codex:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently review
> all three original Stage-9 AP evaluation outputs against the
> supplied activated synthetic AS, scoped F, D002 and conditional
> T1/T2. Inspect and reproduce the embedded numerical programs in
> inputs/AP-EVALUATION-009.json if safe and feasible, checking actual
> counts, seeds, oracle, A/B expiry/cursor and the expressly
> hypothetical C service. Audit all counterexamples, reset/result
> debt, exact consumer index, resource ownership and compatible F
> comparisons. Distinguish model evidence from realized H gate PASS.
> Output ONLY out/REVIEW-AP-EVALUATION-010.md and
> out/REVIEW-AP-EVALUATION-010.json. Do not select AP or approve
> services, AS changes, contracts, hardware or implementation. STOP.

Expected outputs are **not yet verified**.

## 3. Preserve original review evidence and push

After both review artifacts exist, return to real checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-010/archive_ap_evaluation_review010.sh
git show --stat --oneline HEAD
```

The restartable archive validates JSON disposition/no-selection flags,
original MD/JSON identities and SHA-256, selectively stages ONLY
those two files plus the manifest, commits when needed, and pushes
only the experiment branch. Fail closed on unrelated staged files.

## Gate after Stage-10 push

On `READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`, delegate may
separately decide a bounded next evidence task or whether sufficient
grounds exist to *consider* a reversible provisional AP commitment,
without pretending open H gates passed. Review does not select.
On `REVISE_AP_EVALUATION`, preserve original receipts and repair
only identified source/evidence defects with independent review.
On `UNRESOLVED`, ask only for minimum missing evidence/authority.

No automatically accepted AP, CON/DE/C, target/product qualification,
formal cleanroom or historical Toy 1 VO discharge follows.
