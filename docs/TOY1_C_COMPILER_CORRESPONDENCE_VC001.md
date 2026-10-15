# VC-001: Toy 1 C-source/compiler correspondence evidence campaign

**Status:** Authorized scope for evidence collection after terminal VK-001 review.
**Project:** `AS-001`; **no product acceptance**. This campaign is outside the
MODEL_ONLY VK-001 adapters and is not an automatic extension of their acceptance.
It creates reviewable evidence candidates, not a VO discharge.

## Source authority and exact questions

Read the active `process/baselines/AS-001-v2-active.yaml`, the active VO
ledger, `CON-AP2-001-v6`, `CON-AP2-002-v6`, `CON-AP2-003-v6`,
`DE-AP2-UPDATE-v7`, and the existing implementation review
`reviews/gates/IMPLEMENT_DE-900da7a3ce8c-independent-review.json`.
The accepted abstract PR-002 recurrence and prior MODEL_ONLY rung establish
conditional mathematical bounds, **not** properties of compiler-generated
machine code. The current independent host implementation review was favorable
only for the examined host C99 environment.

| Concern | Source-level inspection | Executed evidence | Still requires |
|---|---|---|---|
| VO-006: multiplication | Both operands widened before multiplication, or concrete promotions shown safe | Host `-O0`, `-O2`, `-DNDEBUG` comparisons using actual detector C | Language/target ABI and C expression review |
| VO-006: transient sum | Valid-state invariant plus bound `33*4095²=553377825` | Reference queue exercises legal state transitions, rollover and reset | C expression types, evaluation order and target generated code |
| VO-006: legal domain | Header declares the legal `[0,4095]` precondition; out-of-domain response is not specified | All probe inputs remain legal | Evidence that caller/ingress maintains the precondition in selected integration |
| VO-003: no floating-point hardware | Detector source contains integer-only operations; probe's `stdio` does **not** become product source | Optional target object/assembly generated using supplied compiler | Actual target compiler, ABI, disassembly, final link/runtime dependencies and review |
| VO-002: charged SRAM | Existing budget is 1792 bytes of category ceilings + 256 reserve under 2048 cap | No allocation/stack measurement in this campaign | Separate inventory with target/integration facts |

For C integer arithmetic, type semantics are part of the evidence: the casts
are helpful, but the reviewer must determine the concrete integer-promotion
rules and intermediate types for the chosen compiler/ABI. On the host, explicit
comparisons in `correspondence_probe.c` do not depend on `assert`. A
deliberately wrong *reference-only* build must fail, even with `NDEBUG`.

## What is installed

- `implementation/toy1/correspondence_probe.c`: independently shifting
  queue; 8192 sequential legal samples; periodic quiescent reset; zero/startup,
  max, zero and deterministic varied data. Its negative-control macro alters
  the reference only. The probe never becomes production firmware.
- `tools/toy1_c_evidence.py`: executes host C99 compile-and-run variants and
  the negative control; optionally compiles a target object and emits assembly
  and disassembly. No arbitrary shell execution, C parser, solver, target
  runtime or VO authority.
- `tests/test_toy1_c_evidence.py`: local regression for positive/negative
  checks and resource-template semantics.
- `process/verification/toy1-vo002-inventory-template-v1.yaml`: **unmeasured**
  template for the next resource phase. The seven contract ceilings are
  copied from accepted CON, while every actual category peak remains null.

## Run: host source/compiler evidence first

From the repository root, choose a unique case identifier. The collector's
raw logs/binaries stay under ignored `runs/`; its concise versioned
evidence summary can be committed for independent review.

```bash
git pull --ff-only origin main

python -m unittest discover -s tests -p 'test_toy1_c_evidence.py' -v

case_id="TOY1-VO003006-$(date -u +%Y%m%dT%H%M%SZ)"
python tools/toy1_c_evidence.py \
  --out "runs/$case_id" \
  --summary "reviews/verification/$case_id.json"

python -m json.tool "reviews/verification/$case_id.json" | less
```

Do not use `set -e` while initially diagnosing failures if you want the
shell to remain open. A failed compiler/test or missing target compiler
returns nonzero with an evidence manifest; inspect the stderr log path in
`runs/$case_id/`. Do not call failed evidence a verification PASS.

Expected *categories of results*, not prereported measurements:

1. `HOST_PROBE_PASSED` only if three positive host builds/tests and a
   deliberately failing NDEBUG reference mutant behave as specified.
2. `sources_match_prior_review` checks only the original source files
   pinned by the earlier host review; new probe/collector identities are
   recorded separately.
3. `target_status=NOT_REQUESTED` unless the user provides an explicit
   target toolchain.
4. Product-verified stays false, all `vo_discharged` lists are empty, and
   VO-002..VO-006 remain open in the candidate evidence summary.

The collector stores recorded commands, tool-version output, local log
paths/hashes, source file SHA-256 and (when applicable) object/assembly hashes.
A committed summary does not itself contain ignored raw logs; an independent
reviewer must rerun, access those artifacts, or state the corresponding
reproducibility limitation.

## Optional target object/assembly evidence

**Only if an intended compiler and flags are known**, run a separate case:

```bash
# Replace placeholders with the toolchain/CPU/ABI that is actually authorized.
# This is an illustration, not a selected Toy 1 target.
python tools/toy1_c_evidence.py \
  --out "runs/TOY1-target-UNIQUE-ID" \
  --summary "reviews/verification/TOY1-target-UNIQUE-ID.json" \
  --target-cc "ACTUAL_TARGET_COMPILER" \
  --target-extra="ACTUAL_COMPILER_CPU_AND_ABI_FLAGS"
```

If a compatible disassembler exists, add `--target-objdump` with its exact
name. The raw `detector-target.o`, `detector-target.s` and optional
disassembly stay under `runs/`. A successful target object compile does not
mean firmware was linked, executed, found free of FPU instructions in every
dependency, or assigned a measured stack footprint.

## Next independent evidence review

Review the **actual candidate JSON**, raw/reproduced logs where available,
source and compiler settings, and the existing AS/CON/DE obligations. The
acceptance question is narrower than product acceptance:

- Were host variants compiled and run with the claimed flags and checks active?
- Was the negative control actually detected, including under `NDEBUG`?
- Do expression promotions and integer widths safely implement the accepted
  bounds on the examined compiler/ABI, and which correspondence remains open?
- Does the build evidence address `C-003` beyond source text?
- Is the legal-domain guarantee explicitly assigned but still unverified at
  its physical integration boundary?
- What exact target and integration evidence is still required?

This first collector is **not** wired into an auto-accepting VK-001 gate.
Create a separately versioned independent review for the new evidence scope;
do not masquerade as a MODEL_ONLY VK-001 artifact, or use the earlier
`REVIEW_VERIFICATION_RUNG` receipt to close VO-003/006.

## Following phase: VO-002

Use the unmeasured inventory template and `CON-AP2-003-v6` with the actual
target/toolchain and integration configuration. The binding conditional
ceilings (bytes) are: persistent 256, scratch 128, stack 512, attributable
interrupt context 256, shared 256, dynamic 128, other 256. Sum 1792; reserve
256; approved cap 2048. The DE partitions remain proposed accounting
assignments. To make the inventory reviewable, supply:
- exact source/linked build identity, linker map or symbol evidence and
  actual attributed persistent memory;
- stack maxima with a stated analysis method and relevant overlap/nesting;
- explicitly bounded dynamic and shared allocations if applicable, with
  lifetimes, owner and non-double-counting attribution;
- justified exclusions for unrelated memory, and treatment of infeasible
  category or element ceilings through reviewed design change;
- current unresolved items where a target or integration fact is absent.

No ISR/RTOS topology, heap prohibition, measured bytes, or target compiler
is invented by the template. A host `sizeof(detector_t)` alone cannot
discharge VO-002. Stop and report an evidence gap rather than invent a zero.

## UI compatibility

The summary distinguishes the *actual host result*, optional target-object
status, unverified source/build assumptions, and independent review pending.
It is a candidate event tied to the project spine. The future UI must not
turn `HOST_PROBE_PASSED` into `PRODUCT_VERIFIED`; historical reviewed results
remain immutable while current applicability is projected separately.


## Recorded host run and independent-review handoff (2026-10-15 UTC)

The user pushed `reviews/verification/TOY1-VO003006-20261015T031625Z.json`
in commit `b3205bca0c741eccc8ce0ab14ca25a210071ec06`.
It **reports** `HOST_PROBE_PASSED` with successful C99 `-O0`,
`-O2`, `-O2 -DNDEBUG` builds/executions, and a deliberate
reference-only `-DTOY1_KNOWN_BAD_CONTROL -DNDEBUG` run exiting 1
with a mismatch. `sources_match_prior_review` and
`sources_unchanged_during_collection` are true. Its
`target_status` is `NOT_REQUESTED`; no target objects or measurements
are included. Each normal probe represents 8192 legal calls according
to the corresponding source code; the summary retains hashes and byte
counts of raw local outputs, not their full text.

An explicit independent review task is now registered:

`process/tasks/REVIEW_COMPILER_EVIDENCE-TOY1-VC001.yaml`

The reusable procedure is
`process/playbooks/REVIEW_COMPILER_EVIDENCE.md`.
The task manifest binds the reviewed summary's Git blob identity,
source revision and accepted implementation-review references. The
controller checks source pins and review state before launch. The
independent reviewer should verify the negative control's actual
failure cause and either inspect available local raw logs or rerun
the prescribed host cases in a new `runs/` directory. Merely viewing
log hashes without raw data is not an independent execution.

Run locally after pulling:

```bash
python -m unittest discover -s tests -p 'test_toy1_c_evidence.py' -v
python tools/task.py inspect --manifest process/tasks/REVIEW_COMPILER_EVIDENCE-TOY1-VC001.yaml
python tools/task.py run --manifest process/tasks/REVIEW_COMPILER_EVIDENCE-TOY1-VC001.yaml
```

This independent review uses the registered `REVIEW_COMPILER_EVIDENCE`
operation. It is **not** the terminal VK-001 MODEL_ONLY reviewer and
must not reuse its verdict or discharge VOs. The reviewer should
author a versioned Markdown report and
`pc-compiler-evidence-review/v1` JSON receipt under `reviews/gates/`,
then submit them for inspection.

No target compiler or integrated firmware behavior is supplied by this
host run. If the real target and integration configuration remain
unspecified, the appropriate result is a favorable **host-only**
review (if warranted) with an unresolved target claim, not an invented
target pass.
