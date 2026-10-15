# VR-001: Toy 1 charged-SRAM resource evidence, without invented targets

**Stage:** host-object-layout observation and target/integration evidence gap map.
**Status:** collector authored for local qualification; no target measurements.
**Authority:** AS-001-v2 active; C-002-SCOPE-001; CON-AP2-003-v6;
DE-AP2-RESOURCE-v7; VO-002 remains OPEN at IMPLEMENTATION.

## Reviewed prerequisite and workflow caveat

The user pushed VC-001 independent compiler review in
`38e90e6dde80aa98ec8d2b6590721caaf7139071`.
Receipt: `reviews/gates/REVIEW_COMPILER_EVIDENCE-TOY1-VC001-receipt.json`.
Disposition: `ACCEPT_WITH_CLARIFICATIONS` **for host source/compiler evidence only**.
The reviewer independently compiled and executed the 8192-case host probe
at strict C99 `-O2`, checked submitted raw hashes and inspected the deliberate
negative-control mismatch. This supports the bounded host observation.

**Workflow defect still open:** `python tools/task.py run` for VC-001
failed before any Codex reviewer turn and reported no formal gate decision.
The independent agent directly authored the submitted report/receipt. Thus
the scoped report is useful, but the registered launcher did not complete
and **must not be marked successful**. Preserve this distinction for
genericity audit. Do not infer a second review run from a disposition field.

No linked target build, instruction audit, target stack calculation, or
physical publisher/integration review was present.

## Resource quantities, distinguished by evidence type

The accepted contract constrains 2048 **unique** detector-attributable
SRAM bytes, with seven nonoverlapping category ceilings totaling 1792
bytes and 256 bytes unallocated reserve:

| Category | Accepted conditional ceiling |
|---|---:|
| Persistent state | 256 |
| Temporary/scratch | 128 |
| Detector stack | 512 |
| Attributable interrupt context | 256 |
| Attributable shared allocations | 256 |
| Attributable dynamic allocations | 128 |
| Other attributable SRAM | 256 |

These figures are contract-stage budget commitments, **not measured usage**.
The DE partitions assign conceptual per-element ownership, not physical
measurements. Each byte must eventually be attributed exactly once under
a documented overlap/lifetime model, including applicable stack and
interrupt nesting and justified shared/dynamic allocations. Do not silently
charge zero for categories lacking measurements.

The reviewed detector header contains:

- `uint16_t samples[32]`: 64 object bytes on an implementation with 16-bit
  `uint16_t`, as guaranteed by the chosen exact-width type.
- `uint8_t oldest`: one object byte for the exact-width type.
- `uint32_t sum_squares`: four object bytes for the exact-width type.

These total 69 bytes of **fields**, before implementation-specific struct
padding/alignment. Prior host review reported `sizeof(detector_t)=72`
for its examined host compiler. This is not a verified target object size,
total SRAM attribution, stack maximum or F-001 ranking.

## New reproducible host-only observation

- `implementation/toy1/resource_layout_probe.c` compiles the real
  `detector.h`, and prints C99 `sizeof` and `offsetof` observations in JSON.
- `tools/toy1_resource_evidence.py` compiles and executes the host-only
  probe, preserving compiler invocation, reported output, checksums,
  accepted category budgets, null target peaks, and source hashes.
- `tests/test_toy1_resource_evidence.py` checks the result's evidence
  boundaries and confirms that output traversal is rejected.
- `process/verification/toy1-vo002-inventory-template-v1.yaml` remains
  unmeasured and unchanged.

**The host observation cannot close VO-002.** A C object size is only a
narrow component of the charged-SRAM inventory. A target build and
integration information are necessary for physical acceptance.

## Local commands

Use a unique case ID because this collector never overwrites previous
evidence. If `set -e` was previously active in an interactive shell,
disable it for diagnostics.

```bash
set +e
git pull --ff-only origin main
python -m unittest discover -s tests -p 'test_toy1_resource_evidence.py' -v

case_id="TOY1-VO002-HOST-$(date -u +%Y%m%dT%H%M%SZ)"
python tools/toy1_resource_evidence.py \
  --out "runs/$case_id" \
  --summary "reviews/verification/$case_id.json"

rc=$?
printf 'Resource evidence exit code: %s\n' "$rc"
```

Inspect the actual JSON, build outputs under `runs/$case_id`, and
the code's stated limits. When the collector exits 0 and outputs are
present, selectively stage `reviews/verification/$case_id.json`,
run `git diff --cached --check` and inspect the diff, then commit and
push. Keep raw binaries, logs, `runs/`, credentials and environment
files local. If execution fails, do not publish a favorable result.

The JSON retains `review_state=PENDING_INDEPENDENT_REVIEW`,
`target_status=NOT_REQUESTED`, and every target-category peak as
`null`. The current evidence status is a **HOST_LAYOUT_RECORDED**
observation, not a final resource fit assessment.

## Subsequent decision boundary

After the host layout run, compare the reported structure with source and
existing implementation review and decide what additional evidence is
actually available. At that point, either:

- gather a **declared** target CPU/ABI/compiler, link/memory map, stack and
  integration nesting information and complete the existing VO-002
  inventory, with an independent reviewer checking every charged category;
- or record an explicit **host-qualified-only** implementation result and
  list target/integration obligations as OPEN, rather than inventing target
  data. A formal final-product acceptance or completed VO discharge is
  not warranted by the host-only path.

Before the first cleanroom replay, also audit the generic process:
project-specific assumptions in telemetry and stage gates, the failure
to launch VC-001 reviewer through the registered runner, role-file
coverage, integrity of historical pins across changed source versions,
and current-status overlays versus immutable authoring artifacts.
Do not promote current Toy 1 solution artifacts into the cleanroom input.
