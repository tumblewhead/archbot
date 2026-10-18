# CLN-001 Stage 7: independent review of proposed D003

Stage-6 AP source-quality review is archived (commit `45d85dad82aaf3b1a74b856138d4bc0ccd8e4b47`).
Its disposition is `READY_FOR_INDEPENDENT_AP_EVALUATION`, NOT AP selection
or hardware qualification. It recommends an explicit D003/index-and-lifecycle
authority clarification before full-interface AP eligibility.

The delegate has authored **D003-PROPOSAL-007.yaml** and
**D003-BRIEFING-007.md** as NON-EFFECTIVE proposals.
A new independent reviewer must check the exact accepted AS semantics
before the delegate may issue a disposition. In particular, request/response
rank RI is not approved merely because a mathematical ranking is possible.
Preserve all source limitations and AP-A/B/C as unselected.

## 1. Update real checkout and inspect

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD
bash -n reviews/diagnostics/CLN-001-TASK-007/prepare_d003_review007.sh
bash -n reviews/diagnostics/CLN-001-TASK-007/archive_d003_review007.sh
bash reviews/diagnostics/CLN-001-TASK-007/prepare_d003_review007.sh
```

If any command fails, STOP before launching reviewer. Do not delete existing
reviewer workspace or clean unrelated changes to make the script pass.

## 2. Start NEW distinct reviewer session

In a new terminal (not `codex resume` and not inside active Codex):

```bash
cd "$HOME/archbot-cln001-d003-review-007" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md, and inputs/SHA256SUMS. Independently assess
> the proposed D003-P1..P5 clauses against accepted D001, AS/D002, F,
> T1/T2 and Stage-6 REVIEW-AP-006. Determine whether implicit rank
> truly supplies the consumer index, or changes AS authority. Challenge
> acceptance, stalls, old result reset fencing, and unapproved RN/snapshot
> services. Preserve all UNKNOWN H gates and unselected APs. Write ONLY
> out/REVIEW-D003-007.md and out/REVIEW-D003-007.json. Stop.

Expected reviewer outputs are **not yet verified**.

## 3. Archive exact independent evidence

Only after both review files exist, from the real checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-007/archive_d003_review007.sh
git show --stat --oneline HEAD
```

The restartable archive script copies original bytes without overwrite,
validates JSON and SHA-256, stages only the expected MD/JSON/manifest,
commits if new evidence exists and pushes only the experiment branch.
Unrelated staged paths force a STOP. Whitespace warnings do not rewrite
the original review.

## Next gate

On successful push, assistant verifies actual review disposition and
source identities. If favorable, author a **separate** delegated D003
disposition with explicit AS impact assessment. If REVISE/UNRESOLVED,
prepare the smallest correction/investigation and another review.
Stage-appropriate independent AP feasibility evaluation follows only
after the necessary authority clarification. No AP selection,
CON/DE/C, legacy VO discharge or cleanroom/product qualification.
