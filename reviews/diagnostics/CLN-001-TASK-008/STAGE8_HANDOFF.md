# CLN-001 Stage 8: review additive AS index/lifecycle clarification

The independent Stage-7 review archived at `eb491accb86b12dad783d8ce02b4dff19b490079`
returned `READY_FOR_DELEGATED_D003_DISPOSITION`. The CLN-001-only
sponsor delegate issued [D003-DISPOSITION-007.yaml](D003-DISPOSITION-007.yaml):
a **guarded disposition to prepare and independently review an additive
AS clarification**, not a complete active interface/index mechanism.

The new [AS-ADDENDUM-008.md](AS-ADDENDUM-008.md) and
[BRIEFING-008.md](BRIEFING-008.md) are **PROPOSALS NOT ACTIVE**.
The independent review must test exact consumer index supply, output debt,
acceptance and reset ordering and whether any clause is a material AS
change. All A/B/C remain unselected; no CON/DE/C or product qualification.

## 1. Pull and prepare

From the **real** Git checkout, with no unrelated staged changes:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1

git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD

bash -n reviews/diagnostics/CLN-001-TASK-008/prepare_as_addendum_review008.sh
bash -n reviews/diagnostics/CLN-001-TASK-008/archive_as_addendum_review008.sh
bash reviews/diagnostics/CLN-001-TASK-008/prepare_as_addendum_review008.sh
```

If a command fails, STOP. Do not delete an existing reviewer directory
or overwrite/truncate historical evidence to make preparation pass.
Preparation checks pinned Git blobs and source SHA-256, and creates
`$HOME/archbot-cln001-as-addendum-review-008` with allowlisted inputs.
This is a context restriction, **not** independently proven OS isolation.

## 2. Fresh independent Codex reviewer

New terminal and new Codex invocation, NOT `codex resume`:

```bash
cd "$HOME/archbot-cln001-as-addendum-review-008" || exit 1
codex
```

Give Codex:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently review
> AS-ADDENDUM-008 A008-R1/R2/R3 against the supplied original BKP,
> D001, activated AS, D002, reviewed D003 and guarded disposition.
> Challenge exact consumer-decodable index, no-loss/acceptance
> obligations, consumer restart, reset debt and finite queues.
> Identify interpretation versus material changed requirement.
> Write ONLY out/REVIEW-AS-ADDENDUM-008.md and
> out/REVIEW-AS-ADDENDUM-008.json; STOP. Do not activate AS,
> approve RI/RN, assume services or select an AP.

Expected reports are not yet verified or accepted.

## 3. Archive original results, selectively

Only when both raw review outputs exist:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1

git status -sb
bash reviews/diagnostics/CLN-001-TASK-008/archive_as_addendum_review008.sh
git show --stat --oneline HEAD
```

The archive checks both files, preserves raw bytes and hashes, stages
only these two and their checksum manifest, commits if needed and pushes
only `experiment/toy1-pipe-cleaner-001`. No `git add -A`, no force-push.

## After the next push

Assistant verifies actual reviewer disposition and source identity.
Favorable -> **separate delegate AS-addendum activation decision**
or explicit amendment after assessing findings. REVISE/UNRESOLVED ->
bounded versioned correction/investigation; do not invent acceptance.

Subsequent separately authorized independent AP evidence/feasibility
evaluation is required before any reversible AP selection. Preserve
H1-H6 UNKNOWN, accepted three-axis F, T002-2..8 OPEN,
R4 full detector DEFERRED, conditional T1/T2, and all unapproved
index/snapshot/reset services.
