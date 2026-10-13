---
type: Architecture Statement
id: AS-001-v2
title: Exact sliding-window squared-sum detector, sample-indexed scope
status: draft
version: 2
tags: [as, firmware, sample-indexed]
derived_from:
  - /architecture/AS-001/statement.md
  - /bkp/problem-origin.md
  - /bkp/adc.md
  - /bkp/target.md
  - /bkp/problem-origin-scope-correction-v2.md
relations:
  - kind: derived_from
    target: /architecture/AS-001/statement.md
  - kind: constrained_by
    target: /bkp/adc.md
  - kind: motivated_by
    target: /bkp/problem-origin-scope-correction-v2.md
  - kind: proven_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: specifies
    target: /architecture/AS-001/verification_plan-v2.md
  - kind: candidate
    target: /architecture/AS-001/verification/VO-004-v2.md
---
# AS = (C, R, PS), version 2 candidate

**Disposition:** Draft for independent AS review under
`AS-001-SCOPE-CORRECTION-001`. It is not an accepted baseline. The
original `statement.md` remains immutable history until review and any
required authority update.

## Constraints

- **C-001 (inherited):** Each legal detector input is an unsigned 12-bit
  integer in `[0, 4095]`. This is the synthetic domain, not a claim about a
  physical ADC.
- **C-002 (inherited):** Detector-attributable SRAM is limited to 2,048
  unique bytes under approved accounting scope `C-002-SCOPE-001`.
- **C-003 (inherited):** No reliance on floating-point hardware.

## Requirements

- **R-001 (corrected candidate):** For each legal sample accepted at the
  detector interface, update exactly once. Numerical rolling behavior is
  determined by accepted-sample order and is independent of elapsed time
  between invocations. No throughput guarantee is implied. Any throughput,
  overload, or real-time deadline requirement requires separate approved
  integration authority.
- **R-002 (clarified candidate):** Compute the exact sum of squares of the
  newest 32 samples accepted by the detector, in acceptance order. Until 32
  samples have been accepted, absent earlier history is zero-padded.
- **R-003 (inherited):** No arithmetic overflow for any legal accepted-input
  sequence.

## Problem Statement

Implement a small deterministic signal-energy detector over the declared
synthetic sample domain. The detector consumes the publisher's ordered
published samples. The upstream publisher is responsible for uninterrupted
ordered delivery at this interface. This is an external interface promise,
not verified physical transport evidence. The detector has no AS-mandated
responsibility for acquisition-loss detection, gap reconstruction, sequence
tracking, or watchdog behavior.

## Inherited mathematical basis and boundaries

PR-002 remains applicable to the abstract integer/ring recurrence, legal
12-bit domain, initialization, and once-per-input update assumptions. It
does not establish publisher integrity, concrete C correctness, target
timing, or firmware correctness. C-002, C-003, and F-001 are unchanged.

## Explicit exclusions and unresolved items

- No fixed 1 ms cadence or infinite input throughput is specified.
- Physical acquisition history and loss-free transport are outside this
  detector AS; publisher-integrity verification belongs at an approved
  integration boundary.
- Concurrent external-reader publication semantics are unspecified here.
  Any such interface must be separately defined before atomicity guarantees
  are claimed.
- Whether the existing AP-002 selection conditions and accepted AD-003
  remain applicable under corrected R-001 requires impact review and, if
  needed, a superseding authority decision. This candidate changes neither.

## Candidate clause changes

| Clause | Candidate treatment |
|---|---|
| R-001 | Replace fixed one-sample-per-millisecond with exactly one update per legal accepted sample, independent of elapsed time; throughput/deadline deferred to separately approved integration requirement. |
| R-002 | Clarify newest 32 as samples accepted at detector interface, in acceptance order, preserving zero-padded startup. |
| C-001..C-003, R-003 | Inherit unchanged. |
| Problem boundary | State publisher's ordered uninterrupted delivery responsibility; do not imply physical transport verification. |

