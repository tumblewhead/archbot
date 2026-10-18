# CLN-001 Stage 5: independent interface proposal review handoff

**State:** original Stage-5 interface options and D002 PROPOSAL (not
an approved D002) were pushed at
`c977e487bd0bce0f726e122ce44a96945f0e2461`.
The proposed policy preserves the accepted abstract AS while
requiring future AP candidates to disclose their *complete*
information/ownership/readback and logical-index refinement.

The source documents remain unchanged:
- `INTERFACE-OPTIONS-005.md`, blob `b64ece52ada5963f5196800b81ddb816904602e0`
- `DECISION-PROPOSAL-005.yaml`, blob `3846119f191ee4776e1242100d003d91a32da7b2`
- `BRIEFING-005.md`, blob `9dec948faa94ab6982e87801816b3b0ce49b982b`
- `STAGE5_OUTPUT_SHA256SUMS`, blob `ad9751445d4fb37ddd828f930a6736316fb5b9c7`

The pending independent review must check:
- T2 is a **complete-state** no-replay bound, not detector-owned SRAM.
- A/B/C history ownership and I/II/III index interpretations do
  not silently alter accepted AS, add assumed external services,
  or declare PO-003-3 mathematically accepted.
- A bounded epoch changes unrestricted future quantifiers and
  needs explicit new authority if it limits valid operation.
- All nine option combinations are conditional with
  RAM, compute and electrical device energy UNKNOWN; no winner,
  feasibility or resource-fit claim is proven.
- T002-2..8, including R4 sustained detection, remain OPEN.

## Step 1: update your existing Archbot checkout

From the **actual Archbot Git repository**, not from a Codex workspace:

```bash
# Branch is a pointer to history. Select the current experiment.
git switch experiment/toy1-pipe-cleaner-001

# Update without creating a surprise merge.
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

# Inspect ahead/behind state and any untracked files.
git status -sb

# Create the review directory and verify the exact BKP/decision/author bytes.
bash reviews/diagnostics/CLN-001-TASK-005/prepare_interface_review005.sh
```

The script **creates**, rather than presumes the existence of,
`$HOME/archbot-cln001-interface-review-005/` containing
`AGENTS.md`, `TASK.md`, `inputs/`, `out/`.
It refuses to overwrite an existing reviewer workspace.

The positive allowlist restricts *supplied task context*. It does
not independently establish OS, container, Git-history or
connector isolation. Formal cleanroom remains false.

## Step 2: start a NEW reviewer invocation

```bash
cd "$HOME/archbot-cln001-interface-review-005" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Review the
> history-ownership/index alternatives and unapproved D002 proposal
> against the original synthetic BKP, D001, activated AS, accepted F,
> and mathematical T1/T2 scope. Independently test counterexamples
> and authority boundaries. Write ONLY
> out/REVIEW-INTERFACE-005.md and out/REVIEW-INTERFACE-005.json,
> choose READY_FOR_DELEGATED_D002_DISPOSITION, REVISE_PROPOSAL
> or UNRESOLVED, then stop. Do not approve D002 or select an AP.

Verify the reviewer actually produced **both** files before moving
back to your Archbot Git checkout.

## Step 3: preserve and push the review, restartably

From your Archbot Git checkout (same experiment branch):

```bash
bash reviews/diagnostics/CLN-001-TASK-005/archive_interface_review005.sh
```

This is deliberately **restartable** after a partial copy or stage:
- If an original file was already copied, `cmp` verifies identical
  bytes instead of refusing to continue.
- If the intended files were already staged, `git add` updates only
  those three intended paths. Unrelated staged files cause a clear
  STOP, not a silent `test` exit.
- `sha256sum -c` verifies the review original-byte manifest.
- `git diff --cached --check` may report Markdown trailing-space
  warnings, but the evidence's bytes are preserved.
- `git commit` records the staged snapshot locally and
  `git push origin experiment/toy1-pipe-cleaner-001` publishes
  the branch to GitHub. A rerun after a completed commit/push does
  not create another commit.

Do not stage unrelated untracked FR-002 files; don't modify old
independent reviews, D001, AS or F.

## After push

The coordinator fetches exact remote REVIEW-INTERFACE-005 source
files and disposition. Only then can the human's CLN-001 delegated
engineering decision-maker adopt, revise or defer D002 in a **new**
versioned authority record. An independent review's READY means
*ready for disposition*, not acceptance.

No AP, CON, DE, C, real target fit, formal cleanroom, device-energy
threshold or original Toy 1 VO discharge is authorized by this
handoff.
