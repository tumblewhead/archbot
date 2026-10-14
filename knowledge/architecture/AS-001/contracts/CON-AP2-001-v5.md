---
type: Design Contract
id: CON-AP2-001-v5
title: Accepted-sample interface and observable detector result
status: draft
version: 5
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v5.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v5.md
---
# CON-AP2-001 v5: Minimal sample and result boundary

## Contract

The producer publishes legal samples as unsigned integers in `[0,4095]` in
the intended acceptance order. The upstream publisher owns uninterrupted,
ordered delivery to the detector boundary. This is an external, unverified
assumption; this contract adds no detector-side sequence, loss, or watchdog
mechanism and makes no claim about physical ADC behavior.

For each legal sample accepted at the detector boundary, the detector
performs exactly one update. Its observable value is the exact sum of squares
of the latest 32 accepted samples, in acceptance order; before 32 samples,
missing history is zero. The value depends on sample order, not elapsed time.
There is no specified sampling rate, throughput, deadline, or overload
behavior. Invalid input is rejected before state mutation and must not be
silently treated as a legal sample. How rejection is reported is unresolved.

The detector result is an integer in `[0,536,608,800]`. Result representation,
publication mechanism, reader concurrency, and visibility during an update
are unspecified; no external atomicity guarantee is made. Reset starts with
zero history and zero result. Reset concurrency and lifecycle authority are
unspecified and must be settled before implementation.

## Preconditions, failure, and proof boundary

The mathematical contract assumes legal inputs reach the boundary exactly in
the publisher's intended uninterrupted order. Violation of that external
assumption is not detected or repaired by this contract. Input outside the
legal domain is rejected without changing rolling state; persistent fault
latching and recovery policy remain unresolved.

PR-002 supports the abstract integer recurrence, zero-padded initialization,
and once-per-input update under its stated ring assumptions. It does not
prove publisher continuity, C expression safety, concrete synchronization,
or firmware behavior.

## Interface and responsibility

`DE-AP2-INGRESS-v5` owns legal-domain acceptance and one-to-one accepted
sample delivery to the rolling update. `DE-AP2-STATE-v5` owns reset state and
window representation. `DE-AP2-UPDATE-v5` owns the per-accepted-sample
transition. `DE-AP2-RESULT-v5` owns result exposure; reader and atomicity
semantics require integration authority before they can be strengthened.

No ISR/task topology, queue, synchronization primitive, single-writer
platform assumption, or heap policy is selected here.
