# CLN-001 Stage 4: F disposition and first Proof Engineer

**Stage-3 evidence:** pushed at
`bca9319576cbe23ef66b2bfdb84ffa130f5c6860`.
Distinct reviewer produced TWO scoped verdicts:
- PO: `READY_FOR_PROOF_ENGINEER`, with `proofs_accepted=false`.
- F: `READY_FOR_DELEGATED_F_DISPOSITION`, with `f_accepted=false`.

The reviewer checked the mathematical opportunities for obvious
counterexamples and F's objective-authority boundaries. Actual
reviewer output files and SHA256SUMS are pinned in
`reviews/diagnostics/CLN-001-TASK-003/`. Neither report
accepted a theorem or an F by itself.

## Sponsor-delegate diagnostic F decision

The human sponsor previously delegated synthetic engineering
decisions to the assistant for **CLN-001 only**. This assistant
issued the additive new
[F-DISPOSITION-003](F-DISPOSITION-003.yaml):
`ACCEPT_WITH_EXPLICIT_NEW_OBJECTIVE_AUTHORITY_AND_EVIDENCE_LIMITS`.

F's accepted diagnostic axes are now
`(RAM_peak, compute_effort, device_energy_consumption)`, subject
to original H1..H6 hard gates. The **RAM minimization preference**
inside the 2048-byte cap and the **device-energy preference** are
new *explicit* CLN-001 decisions. Device energy is not the ADC
sum-of-squares signal energy, nor was it already approved by the
old BKP. No numeric power/cycle target, hard 1 ms completion
deadline, budget change, AP ranking, or scalar weights are added.

All **realization values remain UNKNOWN** and no unknown coordinate
may be treated as favorable, zero or PASS. Comparison is a scoped
Pareto partial order when compatible evidence is available.
Energy can make potential candidates incomparable until adequately
modeled. Conditional symbolic evidence is not a target measurement.
Flash remains an inactive, unapproved interest. All T002-2 through
T002-8 verification obligations and deferred R4 detection remain
OPEN; F acceptance does not discharge them.

## Selected opportunity: PO-003-2

The independent reviewer prioritized PO-003-2 because it can
establish a representation-independent minimum retained-history
information bound. No proof is currently established.

A distinct Proof Engineer is authorized to attempt to prove or
refute the **future numeric output** equivalence:
`h~g iff padded 31-tails equal`, quantifying over every
nonempty continuation. Under a closed deterministic **no-replay**
model, it proposes a lower bound of `4096^31=2^372`
distinguishable states, or 372 bits of retained information.

The engineer must independently reason about startup, 1..31 zero
continuations, same-length histories, nonnegative square
injectivity, and external information/ownership exceptions.
The full indexed output is outside that numerical theorem.
A later separate proof reviewer must accept or reject the
result before we cite it as proven.

**PO-003-3 remains open** as a separate conditional
finite-state/unbounded-index issue. No new wrap rule, maximum epoch
length, external-index mechanism or AS amendment is silently
chosen. Resolve this interface question before a complete
implementation contract or irreversible architecture selection
that relies on an unbounded index.

## Run one source-pinned local preparation script

From your real Archbot Git checkout:

```bash
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
bash reviews/diagnostics/CLN-001-TASK-004/prepare_proof004.sh
```

The script **creates** `~/archbot-cln001-proof-engineer-004/`,
checks original BKP and versioned Git source blob identities,
and populates `AGENTS.md`, `TASK.md`, `inputs/`,
`inputs/SHA256SUMS`, and `out/`. It fails if the directory
already exists. It puts no old solved Toy 1 proof/code/F/AP into
the workspace.

New Codex terminal/session (never resume the scout or reviewer):

```bash
cd "$HOME/archbot-cln001-proof-engineer-004" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS. Independently prove
> or refute PO-003-2's exact numeric future-output equivalence
> and conditional state-information lower bound. Write only
> out/PROOF-ATTEMPT-004.md and out/PROOF-BRIEFING-004.md.
> Classify any claimed proof as PENDING INDEPENDENT REVIEW.
> Do not select an AP or implement C. Stop.

The directory is a context allowance, not an OS-level cleanroom.
Reviewers and engineers must not assert filesystem/connector
isolation was proved by `cd`.

## Preserve actual proof attempt and push

Only after the two expected files exist, from your actual
experiment-branch checkout:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
src="$HOME/archbot-cln001-proof-engineer-004/out"
dst="reviews/diagnostics/CLN-001-TASK-004"
test -z "$(git diff --cached --name-only)"
for f in PROOF-ATTEMPT-004.md PROOF-BRIEFING-004.md; do
  test -s "$src/$f"
  test ! -e "$dst/$f"
  cp -- "$src/$f" "$dst/$f"
done
(
  cd "$dst"
  sha256sum PROOF-ATTEMPT-004.md PROOF-BRIEFING-004.md > PROOF004_SHA256SUMS
  sha256sum -c PROOF004_SHA256SUMS
)
git add -- "$dst/PROOF-ATTEMPT-004.md" "$dst/PROOF-BRIEFING-004.md" "$dst/PROOF004_SHA256SUMS"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record CLN-001 independently scoped PO-003-2 proof attempt"
git push origin experiment/toy1-pipe-cleaner-001
)
```

If the Proof Engineer finds a counterexample or an unresolved gap,
preserve the actual result. Do not rewrite history to force a proof.
After push, coordinator prepares the distinct proof-review gate.
No old Toy 1 history, other project, hidden evaluator, F-001, AP,
contract or C implementation may be brought into this exercise.

**No formal cleanroom, F_f target realization, full detector,
actual SRAM/timing/energy qualification, or historical VO discharge
is claimed.**
