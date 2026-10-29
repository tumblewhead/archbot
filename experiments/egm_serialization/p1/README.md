# EGM-P1: proposed fresh Goldfish reconstruction pilot

**Status: PREPARED, NOT EXECUTED OR GATE-ACTIVATED.**
Current test evidence: [user-reported 10/10 P0 unit
tests](../P0_USER_TEST_REPORT_001.json). Independent comparator
review is still due. P1 is an *exploratory* continuation, not
an accepted generic cleanroom or implementation qualification gate.

## Actual materials and control

The worker sees only `SPINE.md`, `TASK.md`, `AGENTS.md`, and
three source files from the actual repository:

- `HARNESS`: `docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md`
- `SKELETON`: `docs/IMPLEMENTATION_SKELETON_FIRST_001.md`
- `EGM`: `docs/EGM_GOLDFISH_SERIALIZATION_001.md`

These are all **proposed** process architecture sources. A Goldfish
must not infer that their components or invariants are activated
merely because they are named. The tiny `SPINE.md` gives candidate
concept identifiers for deterministic structural comparison, but
does **not** give the expected kinds, authority classifications
or typed dependency edges.

`REFERENCE.json` is an **author-drafted provisional evaluator-only
reference**, not an independently reviewed canonical truth.
It requires separate source-grounded semantic verification. The
Goldfish must not receive the reference or the comparison program.
The evaluator can identify suspicious reconstructions using it;
structural `MATCH` is neither semantic correctness nor authority.

## 1. Inspect branch and prepare

From your normal Archbot repository checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git fetch origin
git switch work/cln001-integration-c-kernel-harness
git pull --ff-only origin work/cln001-integration-c-kernel-harness

bash -n experiments/egm_serialization/p1/prepare_p1.sh
bash -n experiments/egm_serialization/p1/evaluate_p1.sh
bash experiments/egm_serialization/p1/prepare_p1.sh
```

Preparation refuses an existing workspace, verifies five exact
source blobs, and creates `$HOME/archbot-egm-p1-001` without
copying `REFERENCE.json`, Git metadata, prior Toy1 answer
or the comparator.

**Isolation warning:** a new directory, an `AGENTS.md` instruction,
or a positive source manifest alone does NOT prevent Codex/terminal
tools from reading the original checkout, evaluator reference or
other host files. This diagnostic can assess an *honored
source-policy* invocation; it cannot be labeled a verified
cleanroom. For an isolation claim, use a separately configured,
tested restricted filesystem/network/connector runtime. Record
actual mounts/tool permissions rather than asserting them.

## 2. Fresh reconstruction invocation (after scoped P0 review/authorization)

Launch a NEW agent invocation, not `codex resume`, with only the
prepared worker workspace visible. If your local runtime cannot
restrict filesystem and connected-data access, record that limitation
and do **not** describe the result as an isolated cleanroom.

```bash
cd "$HOME/archbot-egm-p1-001" || exit 1
codex
```

Prompt:

> Read AGENTS.md, SPINE.md, TASK.md and inputs/SHA256SUMS.
> Traverse only the permitted linked source files. Independently
> reconstruct the proposed harness architecture, S0 linkable-skeleton
> rule and Goldfish serialization obligations into the exact two
> outputs named in TASK.md. Preserve proposed authority status;
> report absent or ambiguous dependencies as UNKNOWN. Do not
> inspect Git, other directories, conversation history, any
> evaluator-only reference or connected apps. Stop after writing
> the outputs.

Expected output files:
`out/GOLDFISH_RECONSTRUCTION.json` and
`out/GOLDFISH_BRIEFING.md`.

## 3. Evaluate outside the Goldfish process

From the original repo checkout, **after** the independent
worker outputs exist:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
bash experiments/egm_serialization/p1/evaluate_p1.sh
rc=$?
printf 'EGM structural comparison exit: %s\n' "$rc"
```

The evaluator's `REFERENCE.json` stays in the original repo.
Its outputs are written to
`$HOME/archbot-egm-p1-audit-001`, **not** the worker
workspace. The audit script refuses an existing audit directory,
records source hashes and no-authority limits, and returns 0 for
structural match, 1 for discrepancy, 2 for malformed/out-of-scope
reconstruction. An output mismatch is useful research data, not
a failed project build.

A distinct semantic reviewer must inspect whether the evaluator-only
reference is itself faithful to the source, whether facts and
typed relations are semantically equivalent, and whether the Goldfish
was genuinely isolated from the reference. Do not silently fix
Goldfish's output to match the reference. If missing facts are real,
revise the versioned source graph under proper authority and rerun
from a newly prepared fresh process.

## 4. Interpretation and next step

The first experiment specifically tests:

1. Can a fresh process find all required sources from a compact spine?
2. Can it distinguish proposed from accepted authority?
3. Can it reconstruct module dependencies and proof/verification limits?
4. Does it identify absent facts instead of inventing implementation?
5. How many source traversals, questions and human minutes are needed?

Only after the source projection and evaluator reference have been
independently checked should a future P2 Goldfish attempt a linkable
S0 skeleton. The current CLN-001 Stage-12 IF11 review is an
independent engineering gate and remains unchanged.
