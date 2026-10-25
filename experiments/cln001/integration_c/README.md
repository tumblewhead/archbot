# CLN-001: bounded integration and fixed-width C feasibility witness

**Status:** EXPLORATORY_IMPLEMENTATION_EVIDENCE; NOT an accepted AP, CON, DE,
qualified firmware or discharge of any T002/VO. Work branch only.
The experiment branch's Stage-12 independent IF11 review remains pending.

The original 12-bit accepted input, latest-32 exact squared-energy PS and
invalid-rejection invariance are retained. This work independently instantiates:

- **A:** `uint16_t raw[31]`, recomputes the 32-term exact sum on valid input,
  evicts the oldest only after using it.
- **B:** `uint32_t square[31]`, `sum31`, oldest-first ring; computes
  `E=sum31+value^2`, next `sum31=E-oldest_square`.
- **S-bounded:** synchronous caller/consumer wrapper around either
  kernel. Returns an observation with sequence, one-based rank, energy
  on each valid input. Invalid input does not change state. Explicit
  reset zeroes numeric state. It is **not an implementation of the
  arbitrary-lifetime consumer contract**: `uint64_t` rank/sequence
  exhaustion is surfaced, not solved. It assumes an always-present
  caller with retained state, no independent publisher, exactly one
  synchronous completion per accepted event and no crashes/restarts.

The public wrapper contains `uint64_t` ordinal and sequence, which
**cannot** meet the accepted unrestricted-index relation by itself.
Treat `CLN_SYNC_EXHAUSTED` as a negative feasibility finding under
this finite representation, not authority to reject an otherwise-valid
sample or impose a mandatory reset. The full H3 outcome is UNKNOWN.

## Run

From repo root on a host with a C11 compiler:

```bash
bash experiments/cln001/integration_c/run.sh
```

For a separate sanitizer replay:

```bash
cd experiments/cln001/integration_c || exit 1
cc -std=c11 -O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer \
  -Wall -Wextra -Werror -pedantic -Iinclude \
  src/cln_numeric.c src/cln_sync_experiment.c tests/test_cln.c \
  -o /tmp/cln001_c_witness_san
ASAN_OPTIONS=detect_leaks=1 /tmp/cln001_c_witness_san
```

The run script builds in a temporary directory and removes it. No
outputs are automatically staged or committed.

## Tests and what they actually establish

Independent C reference oracle retains an ordered 32-entry history
distinct from A/B's 31-entry representation. It checks accepted values,
rejects (4096, 65536 and UINT32_MAX) without state transition or output
modification, validates B's ordered 31-term next sum, exercises resets
and source-width bounds, and tests a 32,768-sample uninterrupted stream
covering each 12-bit value eight times. A bounded synchronous integration
run checks exact consumer-facing output for both algorithms and explicit
model exhaustion rather than silent wrap.

`EXPERIMENT-RESULT-001.json` records the **actual local container**
compiler/build and sanitizer run and exact source SHA256. These are host
tests only, not a Cortex-M build or stack/WCET/energy evidence.
The bytes reported by `sizeof` are object-only, not attributable
peak-live RAM; output staging, live stack, integration ownership,
provider/rank history, potential pending debt and transport are absent.

## Critical missing pieces before a complete interface

1. Actual publisher/consumer identification and a lossless acceptance
   contract, including readiness and no silently lost valid arrivals.
2. Consumer rank and reset identity across arbitrary accepted sequences,
   without a fixed-width rollover, forced reset or new restriction.
3. Explicit accepted-but-unpublished debt retention/retry and reset
   fencing, including delayed and duplicate responses.
4. C's optional snapshot/provider service, its ownership and same-device
   costs. No such service is implemented by this C witness.
5. Real MCU compilation, object/stack/queue/live-memory inventory and
   full comparable compute/device-electrical-energy measurements.

The existing original AS, R1 clarification, Stage-12 IF11 reviewer
handoff, scoped T1/conditional T2, all H1-H6, F and T002-2..8 retain
their authority and prior UNKNOWN/OPEN states.

## Engineering significance

We now have **real C integer arithmetic evidence** for A and B,
plus a testable, deliberately bounded S integration surface. It
narrows numeric implementation uncertainty while exposing the
remaining index/backpressure/debt assumptions rather than hiding
them under a model-success or RAM claim. A subsequent distinct review
must verify these bytes, measurements and scope before promoting
any finding to an accepted evidence disposition.
