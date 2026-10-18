# CLN-001 continuation: sponsor-delegated diagnostic requirements

**Status:** Stage-2 authoring handoff ready. Not yet executed.  
**Scope:** `experiment/toy1-pipe-cleaner-001` only.  
**Decision authority:** human experiment sponsor explicitly empowered this
assistant to make synthetic CLN-001 decisions. This does not make the
assistant the authoring agent, independent reviewer or a real hardware
stakeholder. The delegation is captured in
[DECISION-001.yaml](DECISION-001.yaml).

The human said: *"ill empower you, and yes limited to this diagnostic
project. We already know what we want to end up with, we are just
testing the system"*. Therefore the next step is controlled **new
diagnostic requirements**, not repeated interviews with the human
about known synthetic test targets.

## Decisions recorded

New `DECISION-001.yaml` resolves Q1-Q7 under the delegated synthetic
scope, preserving explicit non-approval of the current AS.
Specifically: exact latest-32 energy, startup zeros and no FPU are
adopted; R3 1 ms semantics are explicitly revised to per-accepted-sample
updates with nominal illustrative cadence but no invented execution
deadline; R4 full sustained-energy decision is distinguished from the
numeric primitive and tracked as deferred integration work; RAM
ownership and target assumptions are defined without pretending
target evidence exists; sample order and input validity are bounded.

**Experiment validity caveat:** this coordinating assistant has seen
the earlier Toy 1 program and cannot claim blind problem-setting.
The *fresh authoring agent* must see only the original BKP, its own
previous output and newly controlled synthetic decisions, never
older solved Toy 1 artifacts or evaluator oracle. Do not cite previous
Toy 1 decisions as the source of this new specification.

## Prepare the NEXT stage in the existing diagnostic workspace

Run from the Archbot **experiment branch checkout**, not from within
the temporary authoring workspace:

```bash
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"

# The original authoring workspace, not the separate review workspace.
workspace="$HOME/archbot-toy1-Q9RnZlCE/package/workspace"
dst="$workspace/projects/CLN-001/process/decisions"
mkdir -p "$dst"

test ! -e "$dst/DECISION-001.yaml"
test ! -e "$workspace/TASK-002.md"
test -s "$workspace/projects/CLN-001/out/AS-DRAFT-001.md"
test -s "$workspace/projects/CLN-001/out/QUESTIONS-001.md"

cp -- reviews/diagnostics/CLN-001-TASK-001/DECISION-001.yaml \
  "$dst/DECISION-001.yaml"
cp -- reviews/diagnostics/CLN-001-TASK-001/TASK-002.md \
  "$workspace/TASK-002.md"

# Capture the exact newly admitted inputs for Stage 2.
sha256sum "$dst/DECISION-001.yaml" "$workspace/TASK-002.md"
```

These two files are **new Stage-2 input material**. The original
Stage-1 `cleanroom_pipe_cleaner.py inspect` will now flag them as
unexpected because its original positive allowlist is frozen. This
is an expected stage transition, **not** a PASS under the old manifest.
Record Stage-2 source hashes and preserve Stage-1 receipts; do not
edit the original auditor manifest to pretend these inputs were there
at the beginning.

Use a **new authoring agent invocation** restricted to the workspace
(there is no benefit to inheriting the old Codex conversation). Do
not launch Codex from the original Archbot repo with old Toy 1
solutions accessible. New agent prompt:

> Read AGENTS.md and then TASK-002.md. TASK-001 has already completed
> and its stop gate was honored. This is a separately authorized
> diagnostic AS revision. Use the new sponsor-delegate DECISION-001,
> previous draft and three original BKP files. Produce only
> AS-REV-002.md, DECISION-TRACE-002.md, BRIEFING-002.md and stop.

Review the three outputs **before committing**. Copy them back to
`reviews/diagnostics/CLN-001-TASK-002/`, with SHA256SUMS and truthful
run notes. Only then should a distinct reviewer compare them to the
three BKP files and DECISION-001. No F/P/AP/CON/DE/C yet.

## Approval boundaries

- DECISION-001 is a recorded, explicit synthetic specification choice
  attributable to delegated CLN-001 authority, **not an approved AS**.
- The independent reviewer of AS-REV-002 must be separate from the
  AS author and this decision-maker; provenance limitations remain
  visible.
- Formal cleanroom/FR-005/FR-006 remains unauthorized and unqualified.
- Existing original Toy 1 accepted decisions, review receipts, VOs,
  ADs, source and implementation are not changed.
- This is a proof-of-process diagnostic. Success means a reasoned,
  traceable handoff, not matching a hidden previous solution byte-for-byte.
