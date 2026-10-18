# CLN-001 Stage 5: information boundary and index applicability

**Status:** fresh analyst handoff authored; no Stage-5 agent run claimed.
**Branch:** `experiment/toy1-pipe-cleaner-001`.
**Prior result:** [PROOF-DISPOSITION-004](../CLN-001-TASK-004/PROOF-DISPOSITION-004.yaml)
after independent `ACCEPT_WITH_CLARIFICATIONS` review at
`f255c662847378ac3df39b55c71e146a1f71cf7c`.

The accepted theorem T1 concerns FUTURE NUMERIC outputs; conditional
T2 counts COMPLETE output-affecting retained information under a
no-replay model, not detector-local bytes. The AS separately
requires logical event/output association `(n,E_n)`, but
doesn't yet select an index owner, maximum epoch length or
physical interface. We must not silently settle these choices.

## Purpose

Run a single fresh diagnostic interface-applicability analyst,
**before** AP selection. Its task compares:
- detector-owned retained state vs upstream replay/readback vs shared
  information service, and where T2 applies in each;
- external logical association vs bounded finite detector index vs
  impossible unbounded closed-machine interpretation;
- resource/energy/compute consequences at the accepted F axes,
  with every unmeasured realization value UNKNOWN;
- a D002 *PROPOSAL* for delegated CLN-001 review/disposition,
  not an adopted requirements or architectural change.

## Run from the Archbot repository checkout

```bash
# Move to the already existing experiment branch (not a new branch).
git switch experiment/toy1-pipe-cleaner-001

# Fetch + integrate ONLY if fast-forward; never make a surprise merge.
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

# This script CREATES a fresh positive-allowlist workspace.
bash reviews/diagnostics/CLN-001-TASK-005/prepare_interface005.sh
```

The script checks Git object hashes of each authorized source and
SHA-256 hashes of the three original unsolved BKP inputs before
copying. It **creates** rather than assumes
`$HOME/archbot-cln001-interface-005/`; stops clearly if it exists.

A positive allowlist and `cd` are context controls, **not**
independently verified OS/connector isolation. Thus the run stays
pre-freeze diagnostic, not formally qualified cleanroom.

## New Codex invocation

```bash
cd "$HOME/archbot-cln001-interface-005" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS.
> Analyze the accepted T1/T2 applicability to detector versus
> upstream retained information, and the exact logical-index
> interface semantics. Compare options and create only
> INTERFACE-OPTIONS-005.md, DECISION-PROPOSAL-005.yaml and
> BRIEFING-005.md in out/. The proposed decision remains
> PROPOSED_NOT_APPROVED. Do not select AP, modify AS/F,
> invent a wrap/epoch limit or implement C. Stop.

Expected source files:
- `out/INTERFACE-OPTIONS-005.md`
- `out/DECISION-PROPOSAL-005.yaml`
- `out/BRIEFING-005.md`

## Inspect, archive and push, safely restartable

After those three files exist, go back to your real Archbot Git
checkout, then:

```bash
# Stage/commit/push only the three output files and checksum manifest.
# Safe to repeat if an earlier attempt already copied/staged them.
bash reviews/diagnostics/CLN-001-TASK-005/archive_interface005.sh
```

This fixes **two process lessons** from Stage 4:
1. Repeated execution accepts already-copied files if their bytes
   match the originals, then resumes rather than silently failing
   because the staging area is nonempty.
2. Git's `diff --cached --check` whitespace findings are printed,
   but immutable source evidence is kept byte-identical and checked
   with SHA-256. We do not alter reviewer/author text just to fix style.

Git walkthrough: `git add` stages those exact files; `git commit`
creates a local immutable snapshot from the staged index; `git push`
publishes the resulting branch commit to GitHub. Unrelated
untracked FR-002 files stay untouched. The archive script refuses
unrelated **staged** files and a modified copy of an original.

## After push

The coordinator fetches the new branch head, verifies the actual
source and source hashes, and prepares a **distinct** independent
review of the applicability matrix and D002 proposal. Only the
delegated engineering decision-maker may adopt a subsequent
D002, with a bounded scope and any AS/contract impacts explicit.
No subsequent AP/CON/DE/C or qualification follows automatically.

**Still not accepted:** a lifetime or wrap rule, a concrete index
mechanism, no-replay as a device requirement, any AP, implementation
RAM/timing/energy/power, full detector R4, formal cleanroom, or
historical Toy 1 VO discharge.
