# CLN-001 Stage 6: independent review of three fresh AP drafts

**State:** authorized independent *candidate-quality* review prepared;
no new AP review has yet run. This is a synthetic, pre-freeze diagnostic.
**Working branch:** `experiment/toy1-pipe-cleaner-001`.

## Source evidence

The new Proposal Agent delivered three unselected alternatives:
- **AP-006-A:** local ordered raw 31-sample tail, recomputes full
  32-sample energy from each valid new sample;
- **AP-006-B:** local ordered squared 31-tail and redundant sum,
  proposes an incremental exact energy invariant;
- **AP-006-C:** detector reads a prospective upstream-owned,
  consistent snapshot of accepted history, then recomputes.

All three remain `AP_CANDIDATE_NOT_SELECTED`. Author output was
pushed at `65ba5bf74347b28464e0ac610eea160bc131971f`:
- `AP-CANDIDATES-006.md`, Git blob
  `6a87f5a8f44c736bf32b19338843b4e3c84f47fd`
- `AP-COMPARISON-006.md`, Git blob
  `4ab222da90473b868f5e4432603e05f0b5b88fe2`
- `AP-BRIEFING-006.md`, Git blob
  `a9ea9ac483f9e868cc7ad841e368896782724e04`
- `AP006_OUTPUT_SHA256SUMS`, Git blob
  `d0944075e8164d5f2068614d6b6e8d9af5b34479`

The reviewer must assess the exact accepted synthetic AS/D001,
three-axis F, conditional T1/T2 and D002 disclosure policy.
T002-2..8 and deferred R4 remain OPEN. None of the H1..H6
gate constraints or realized F coordinates is verified for any AP.

**Important interface uncertainty:** A/B suggest RI event-response
association where `n` is mathematical event rank, but whether
this actually **supplies** an index under AS remains pending.
C suggests RN external arbitrary-precision ordinal support,
which has not been authorized or demonstrated. No finite
epoch, overflow/wrap rule, external protocol or service is
presumed available.

## Create independent reviewer workspace

From the real Archbot checkout, not a Codex author directory:

```bash
# Select experiment history: this does not create a new branch.
git switch experiment/toy1-pipe-cleaner-001

# Fetch and update only if the remote is a linear descendant.
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

# Inspect the current working tree and Git index.
git status -sb

# This script CREATES the review workspace and verifies source identities.
bash reviews/diagnostics/CLN-001-TASK-006/prepare_ap_review006.sh
```

After successful preparation:
`$HOME/archbot-cln001-ap-review-006` contains `AGENTS.md`,
`TASK.md`, `inputs/SHA256SUMS`, `inputs/`, and `out/`.
It does not import solved Toy 1 AP/CON/DE/C or original
Git history. The source allowlist is a context boundary,
not OS-level cleanroom isolation.

## Run distinct Codex reviewer

In a **new terminal/session**, not `codex resume`:

```bash
cd "$HOME/archbot-cln001-ap-review-006" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently
> review AP-006-A/B/C against the accepted synthetic problem,
> H1–H6, the exact logical index interface, D002 and the
> conditional theorem. Challenge B's rolling invariant,
> C's unapproved snapshot/ordinal dependencies and all three
> candidates' symbolic F comparisons. Write ONLY
> out/REVIEW-AP-006.md and out/REVIEW-AP-006.json and stop.
> Do not select an AP or assert target feasibility.

Reviewer dispositions:
- `READY_FOR_INDEPENDENT_AP_EVALUATION`
- `REVISE_AP_DRAFTS`
- `UNRESOLVED`

All are review-of-draft dispositions; no acceptance of AP or
realization follows.

## Preserve and push original reviewer evidence

After **both** output files exist, return to the real Git checkout:

```bash
bash reviews/diagnostics/CLN-001-TASK-006/archive_ap_review006.sh

# Learn Git: show only the latest commit and paths it changed.
git show --stat --oneline HEAD
```

The archive script is restartable. It:
- verifies an existing copied file byte-for-byte with `cmp`;
- creates/validates SHA256SUMS without rewriting the original;
- stages ONLY expected files and refuses unrelated staged paths;
- reports nonblocking whitespace warnings without modifying
  immutable evidence;
- commits if new staged content exists and pushes only
  `experiment/toy1-pipe-cleaner-001`.

Untracked unrelated FR-002 receipts stay untouched.

## Next gate

After the actual remote reviewer evidence is verified, prepare
a **separately authorized AP evidence/feasibility evaluation**
or a focused revision/authority question from the review's
findings. AP source fidelity and AP-due feasibility are different
decisions. Only after stage-appropriate evidence and independent
evaluation could the CLN-001 delegate consider a **reversible
provisional** AP commitment, retaining all open VOs and any
separately accepted Architectural Debt.

The previously parked Goblin Graph-derived spine-builder concept
and Process Orchestrator proposal are unaffected. No implementation,
target qualification, entire sustained-energy detector, formal
cleanroom or old Toy 1 VO discharge is authorized.
