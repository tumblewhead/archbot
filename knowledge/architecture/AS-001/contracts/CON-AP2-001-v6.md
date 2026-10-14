---
type: Design Contract
id: CON-AP2-001-v6
title: Accepted-sample interface and observable detector result
status: draft
version: 6
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-001-v5.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v6.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v6.md
---
# CON-AP2-001 v6: Sample, reset, and result boundary

## Input and update contract

The detector boundary accepts only legal samples represented as unsigned
integers in `[0,4095]`. An accepted sample is delivered exactly once to the
rolling update. The upstream publisher owns uninterrupted, ordered delivery
in the intended acceptance order. This is an external, unverified assumption;
the detector contract adds no loss detection, sequence tracking, or watchdog.

For every accepted sample, the detector performs exactly one update. At
completion of that operation, its associated result is the exact sum of
squares of the latest 32 accepted samples in acceptance order. Before 32
samples, missing history is zero. The result is in `[0,536,608,800]` and is
represented as an unsigned integer capable of that full range (at least 29
value bits). The completion result is the abstract handoff: a caller
completing an accepted-sample operation can obtain that operation's coherent
post-update value. This contract makes no guarantee for a separate concurrent
reader. Any such reader semantics require separately authorized integration
requirements; no atomic primitive, publication mechanism, or platform
topology is selected here.

## Initialization and reset ordering

Initialization establishes zero history and zero result before the first
sample can be accepted. Reset is permitted only while acceptance is quiesced
and no accepted-sample operation is in progress. Acceptance remains quiesced
through reset completion; after completion, the next accepted sample starts
from zero history and zero result. Thus every accepted sample is ordered
either before reset completion or after it, and reset cannot overlap an
accepted update. This is an interface lifecycle precondition, not a required
ISR/task arrangement or synchronization primitive.

## Preconditions and proof boundary

There is no specified sampling rate, throughput, deadline, or overload
behavior. Values outside `[0,4095]` are outside this contract's input domain;
the contract imposes no rejection, reporting, or recovery behavior for them.
Range checks needed to protect legal-input arithmetic remain an
implementation obligation under VO-006.

PR-002 supports the abstract integer recurrence, zero-padded initialization,
and once-per-input update under its stated ring assumptions. It does not
prove publisher continuity, C expression safety, concrete synchronization,
the reset lifecycle's physical enforcement, or firmware behavior.

## Responsibility

Ingress preserves the legal-domain precondition and one-to-one delivery of
accepted samples. State/reset implements the stated initialization and
quiescent lifecycle. Update implements the recurrence. The completed
accepted-sample operation returns its associated post-update result. No
external concurrent-reader guarantee is implied.
