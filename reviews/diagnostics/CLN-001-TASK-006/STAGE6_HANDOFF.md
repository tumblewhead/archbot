# CLN-001 Stage 6: D002 accepted and first competing AP drafts

**Status:** D002 engineering disposition authored under explicit
CLN-001-only sponsor delegation; AP author task prepared, not
executed. No architecture selected. Still pre-freeze diagnostic.

## Scope of the D002 decision

The Stage-5 analyst authored a NONBINDING
`CLN-001-D002-PROPOSAL-005`, archived at
`c977e487bd0bce0f726e122ce44a96945f0e2461`.
A distinct independent reviewer returned
`READY_FOR_DELEGATED_D002_DISPOSITION` at
`6361abe11795c6e80d1c518eff6a5259f28b2c07`
with no blocking finding. R1 MINOR clarified that the source's
sample-order illustrations depend on an **exactly 31-entry
padded tail**. Reading the ellipses as a full 32-entry window
would falsify the claimed next-output equality. Preserve the
original analysis and reviewer unmodified.

The CLN-001 sponsor delegate explicitly adopts ONLY the
**six-clause disclosure and refinement process policy** in
[D002-INTERFACE-DISPOSITION.yaml](D002-INTERFACE-DISPOSITION.yaml).
This does NOT select detector-local A, publisher-readback B,
shared C, index I/II/III, an existing external protocol, an
epoch cap, counter width/wrap, new AS restriction or an AP winner.
It requires any proposed AP to account for consulted and retained
information, ownership, reset/error behavior, exact index
refinement, conditional T2 applicability, full H1-H6 and F
cost evidence. The abstract accepted AS, D001, F and proof
remain immutable. All T002-2..8 and R4 stay open.

## Next task: competing AP authoring, not AP selection

From your **real Archbot Git checkout**:

```bash
# Change the branch pointer/checkout to our experiment branch.
git switch experiment/toy1-pipe-cleaner-001

# Incorporate remote commits ONLY if this is a fast-forward.
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

# Show local branch tracking, staged/unstaged/untracked changes.
git status -sb

# This script CREATES the next workspace after pinned-identity checks.
bash reviews/diagnostics/CLN-001-TASK-006/prepare_ap006.sh
```

The script creates `~/archbot-cln001-ap-006` with
`AGENTS.md`, `TASK.md`, `inputs/SHA256SUMS`,
the source-only `inputs/` package and an empty `out/`.
It refuses to overwrite a workspace. Do not assume this
directory exists until script success.

The supplied source-only inputs are:
original three unsolved BKP, synthetic D001, activated AS and
trace, accepted F and its P1-P6 candidate definitions, accepted
conditional mathematical T1/T2 scope, and D002 policy.
The author sees **no previous solved Toy 1 AP, CON, DE, C,
previous implementation, hidden rubric or Git tree**. A working
directory/source allowlist still is NOT OS-level cleanroom
isolation.

In a **new Codex terminal/session, never `codex resume`**:

```bash
cd "$HOME/archbot-cln001-ap-006" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Invent at
> least two structurally different architecture proposal
> candidates satisfying the scoped synthetic numeric-energy
> problem and D002 disclosure rules, with explicit index
> and history ownership/refinement assumptions. Compare their
> symbolic hard gates and accepted Pareto F axes without
> ranking UNKNOWNs or choosing a winner. Write only
> out/AP-CANDIDATES-006.md, out/AP-COMPARISON-006.md and
> out/AP-BRIEFING-006.md; stop. Do not implement C.

Use the proposal role; no code, concrete contract acceptance,
selected AP or false target measurements. If some candidates
depend on an unapproved external source/index service, classify
them CONDITIONAL rather than treating the service as real.

## After Codex, return to the Archbot Git checkout

```bash
# Safe to repeat after partial copy/staging. Copies exact raw outputs.
bash reviews/diagnostics/CLN-001-TASK-006/archive_ap006.sh

# An instructive read-only peek: the new commit and its parent.
git log --oneline --decorate -4
```

The restartable archive script compares existing destination
files byte-for-byte (`cmp`), creates/verifies SHA-256 manifest,
allows ONLY intended files in the Git index, and commits/pushes
them. It reports nonblocking Git whitespace-style warnings but
does not edit original evidence. Unrelated FR-002 untracked
files remain untouched.

## Gate after AP authoring

A distinct independent AP reviewer must check the actual
proposal files and cost/authority semantics before any candidate
can become eligible for selection. A separate CLN-001 delegate
decision may then authorize **reversible AP selection** only
if no applicable hard constraint is contradicted and remaining
unknowns, external dependencies, and due-stage evidence are
recorded. No proposal or conditional theorem can alone confer
fit, target performance, entire detector R4 or VO discharge.

No formal FR-005/FR-006 cleanroom, hardware compliance, old Toy 1
migration/solution import, AP selection, CON/DE/C acceptance
or implementation is claimed here.
