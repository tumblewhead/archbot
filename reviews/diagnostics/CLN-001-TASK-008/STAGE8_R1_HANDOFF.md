# CLN-001 Stage 8-R1 handoff: focused correction review

Current independently archived Stage-8 review:
`REVIEW-AS-ADDENDUM-008.md/json`, committed at
`0d7f83b4e6b9d912562de93ea268eb1575f41f88`.
Disposition: `REVISE_AS_ADDENDUM`, one blocking finding
`R008-3`: original S28 accidentally mandates reset acknowledgment.

The original proposal/review/receipts remain untouched. New candidate
`AS-ADDENDUM-008-R1.md` changes ONLY the heading and S28 sentence.
It makes **consumer-visible reset ordering and old/new association**
mandatory while **acknowledgment remains optional**; no mechanism is
approved. A deterministic delta check is included in the preparer.
This is NOT an accepted or effective AS addendum.

## Prepare

From real local Archbot repository checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD
bash -n reviews/diagnostics/CLN-001-TASK-008/prepare_as_addendum_review008_r1.sh
bash -n reviews/diagnostics/CLN-001-TASK-008/archive_as_addendum_review008_r1.sh
bash reviews/diagnostics/CLN-001-TASK-008/prepare_as_addendum_review008_r1.sh
```

Stop on any nonzero command. Preparation verifies pinned source blobs,
original review hashes, synthetic BKP SHA-256, and precise source delta.
Creates `$HOME/archbot-cln001-as-addendum-review-008-r1`. A new
directory/positive source allowlist is not proof of OS/connector isolation.

## Independent reviewer, new terminal and Codex invocation

```bash
cd "$HOME/archbot-cln001-as-addendum-review-008-r1" || exit 1
codex
```

Instruction:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently check
> the original versus AS-ADDENDUM-008-R1 exact diff; review R008-3
> resolution and preservation of D001/accepted AS, D002, D003,
> consumer-decodable index, accepted result debt and reset fencing.
> Do not approve any specific acknowledgment, RI/RN/C-HIST, or AP.
> Write ONLY out/REVIEW-AS-ADDENDUM-008-R1.md and
> out/REVIEW-AS-ADDENDUM-008-R1.json. Stop.

## Preserve/commit/push original reviewer evidence

After both raw outputs exist, from the real repo checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-008/archive_as_addendum_review008_r1.sh
git show --stat --oneline HEAD
```

Archive script checks original output consistency, JSON and SHA-256,
stages ONLY the MD/JSON/manifest, commits if needed and pushes only
the experiment branch. Stop on unrelated staging, byte mismatch or
missing evidence. Do not force push.

## Subsequent eligibility

When review is pushed, assistant verifies remote SHA, actual reviewer
disposition and evidence; favorable -> separate explicit CLN-001
delegate AS-addendum activation/impact decision. REVISE/UNRESOLVED ->
focused remediation/investigation. Only after appropriate accepted
interface clarification may separately authorized AP evidence/feasibility
evaluation proceed.

A/B/C unselected; all realized H1-H6 UNKNOWN, F measured axes UNKNOWN,
T002-2..8 OPEN, R4 full detection DEFERRED. No CON/DE/C, qualified
target, formal cleanroom or old Toy1 VO discharge.
