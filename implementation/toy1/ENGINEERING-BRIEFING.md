# Toy 1 implementation briefing

Task: [IMPLEMENT_DE-900da7a3ce8c](../../process/tasks/IMPLEMENT_DE-900da7a3ce8c.yaml)
at repository revision `aad9208420dc3962ddc583999b9464e6a9e3a16b`.
This is a guarded prototype for the independently reviewed DE-v7 package;
it is not independently accepted firmware.

## What changed and why

`detector.c` implements the approved 32-slot rolling state with 16-bit
samples, a 32-bit accumulator, and an 8-bit oldest-slot index. Each call
evicts one value, computes both squares only after widening operands to
`uint32_t`, then performs one add/subtract transition and returns the
post-update value. The function's documented precondition is a legal sample
in `[0,4095]`; the contract leaves out-of-domain behavior unspecified, so
the prototype adds no rejection, clamping, or recovery semantics. Reset is
an explicit caller-quiesced lifecycle operation with no synchronization
mechanism selected.

The public call return supplies the operation result, so there is no second
published result field and no claim about an external concurrent reader.
There are no timing, ISR, watchdog, publisher continuity, floating-point,
or target-specific claims.

## Verification performed

Built and ran the deterministic reference-model test with:

```sh
cc -std=c99 -Wall -Wextra -Wconversion -Werror -pedantic -O2 \
  implementation/toy1/detector.c implementation/toy1/test_detector.c \
  -o /tmp/toy1_detector_test
/tmp/toy1_detector_test
```

GCC 16.2.1 on the host reported `sizeof(detector_t)=72 bytes` and all test
assertions passed. Tests compare every returned update with a shift-based
newest-32 model, including zero padding, reset, max-domain startup, removal
after a full max window, mixed legal inputs, and multiple ring wraps. This
host test does not establish target ABI, generated target instructions,
physical memory fit, stack/nesting use, cycle time, or publisher continuity.

## Resource attribution and open evidence

The persistent object is 72 host-ABI bytes in this build. It is attributable
to the STATE persistent category and the DE-v7 proposed STATE subceiling of
256 bytes, subject to target layout confirmation. The implementation makes
no dynamic allocations and declares no shared or interrupt state. The host
object size does not measure target padding, stack, call depth, interrupt
context, shared allocations, or other integration-attributable SRAM. The
full C-002 inventory and peak overlap analysis must therefore be completed
with the actual target/toolchain and integration topology.

VO-002 through VO-006 remain OPEN. VO-002 needs target/integration memory
and stack evidence; VO-003 needs target build/source evidence for the
no-floating-point constraint; VO-004 needs independent checking of the
sample-indexed exactly-once operation against accepted calls; VO-005 needs
independent correspondence review; VO-006 needs independent C range,
promotion, and overflow review. The external ordered-publisher assumption
remains unverified. No obligation is discharged here. AD-003 and F-001 are
unchanged; final F comparison remains due before final acceptance.

## Human contribution and next gate

Provide the intended target/compiler configuration and integration memory,
stack, and call-context details so VO-002/VO-003 evidence can be collected.
Next eligible action is independent implementation verification of the
source, tests, arithmetic correspondence, and evidence limits in the linked
review request. The task runner's Codex subprocess could not initialize in
this read-only app-server environment; its local structural check, active
baseline check, and 103 repository unit tests completed successfully before
this implementation was authored.
