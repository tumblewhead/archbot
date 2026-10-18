# CLN-001 Stage 3: Proof Scout and Figure-of-Merit scoping

**Status:** package preparation ready, no local stage-3 execution claimed.
**Branch:** `experiment/toy1-pipe-cleaner-001`.
**Scoped AS activation:** `AS-ACTIVATION-002.yaml`, triggered
by user push `82ea7793b15c292e103fcd3d18ab1dc8504abf4f` of both
exact REVIEW-002 sources. Original AS revision and D001 source
identities remain unchanged.
**Continuing limits:** synthetic diagnostic only, no qualified
cleanroom, no validated implementation or real hardware.

## What is authorized

Two **draft discovery** exercises after acceptance of AS-REV-002:
- Proof Scout proposes 1–3 **unproven** proposition candidates and
  explicit counterexample searches/assumptions. It is not a Proof
  Engineer, independent proof reviewer or architecture selector.
- FOM Analyst proposes a new vector/partial ordering that distinguishes
  hard constraints from comparative objectives, unknown target
  costs and future evidence. It is not an accepted F, old Toy 1 F-001,
  or selection of an architectural proposal.

The two tasks have no need to read one another's output. They can be
completed in distinct fresh Codex invocations. Their exact source
allowlists are identical, so their independent discoveries can be
compared later rather than cross-contaminating the workspaces.

## One local preparation command

**From your real Archbot Git checkout** on the experiment branch:

```bash
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
bash reviews/diagnostics/CLN-001-TASK-003/prepare_stage3_workspaces.sh
```

The shell script **creates the directories** and verifies the source
hashes before populating either input package. It will fail rather
than overwrite an existing directory. Do not assume a workspace
exists before this command succeeds.

It constructs:
- `$HOME/archbot-cln001-proof-003/` with `AGENTS.md`, `TASK.md`,
  `inputs/`, `inputs/SHA256SUMS`, `out/`.
- `$HOME/archbot-cln001-fom-003/` with the same structure and
  its distinct task.

Inputs include **only** original unsolved BKP, D001, accepted
AS-REV-002, decision trace, and activation record. Both tasks were
newly authored on this experiment branch. The script also checks
the actual archived REVIEW-002 and task Git identities at preparation
time, without putting reviewer files into the two author packages.

Never include old solved Toy 1 F/AP, code, proof, legacy decisions,
old repo spine or evaluation oracle. A different directory alone
is **not an OS/container sandbox**; formal cleanroom remains false
unless that external isolation is separately demonstrated.

## New Codex sessions, separately

Proof Scout terminal:

```bash
cd "$HOME/archbot-cln001-proof-003" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. From the supplied
> accepted synthetic AS and decision evidence only, propose 1–3
> mathematically precise **unproven proof opportunities** with
> assumptions, potential counterexamples and value. Write only
> out/PO-OPPORTUNITIES-003.md and out/PO-BRIEFING-003.md. Stop.

FOM analyst terminal, a DIFFERENT new Codex invocation:

```bash
cd "$HOME/archbot-cln001-fom-003" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Derive a new
> candidate F from accepted synthetic AS, original BKP and D001.
> Keep hard constraints distinct from optimization axes, treat
> unknown target values as UNKNOWN, and do not select an AP.
> Write only out/F-DRAFT-003.md and out/F-TRACE-003.md. Stop.

Do not resume old reviewer or author sessions.

## Outputs and selective archival

After both sessions finish, from the actual experiment-branch checkout:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
dst="reviews/diagnostics/CLN-001-TASK-003"
proof="$HOME/archbot-cln001-proof-003/out"
fom="$HOME/archbot-cln001-fom-003/out"

test -z "$(git diff --cached --name-only)"
for spec in \
  "$proof/PO-OPPORTUNITIES-003.md" \
  "$proof/PO-BRIEFING-003.md" \
  "$fom/F-DRAFT-003.md" \
  "$fom/F-TRACE-003.md"; do
  test -s "$spec"
  name="${spec##*/}"
  test ! -e "$dst/$name"
  cp -- "$spec" "$dst/$name"
done
(
cd "$dst"
sha256sum PO-OPPORTUNITIES-003.md PO-BRIEFING-003.md \
  F-DRAFT-003.md F-TRACE-003.md > OUTPUT_SHA256SUMS
sha256sum -c OUTPUT_SHA256SUMS
)
git add -- \
  "$dst/PO-OPPORTUNITIES-003.md" \
  "$dst/PO-BRIEFING-003.md" \
  "$dst/F-DRAFT-003.md" \
  "$dst/F-TRACE-003.md" \
  "$dst/OUTPUT_SHA256SUMS"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record fresh CLN-001 proof opportunities and FOM proposals"
git push origin experiment/toy1-pipe-cleaner-001
)
```

If only one role completes, do **not** fabricate the other's
outputs. Save the completed role separately with its own source
manifest, or upload the files to the coordinator for a selective
archival decision. No user edit of source outputs merely to pass
a checkpoint.

## Next delegated gate

After source results are Git-pinned, inspect both, resolve any
scope/provenance problems, and arrange appropriate independent
review of claims. The delegated CLN-001 decision maker may accept
a proposed F only with explicit source-linked rationale and open
measurement obligations. A proposed theorem cannot be promoted to
a proven theorem by a favorable informal review. No AP, CON, DE,
C implementation or historical VO discharge is authorized by
this Stage-3 handoff.
