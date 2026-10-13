---
type: Design Contract
id: CON-AP2-001-v3
title: Sample ingress and detector result contract
status: draft
version: 3
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-001-v2.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v3.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v3.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-001 v3: Sample ingress and result

## Boundary and data

For each 1 ms acquisition period, the producer supplies one logical record `(sequence, sample)`, in acquisition order. `sample` is unsigned and legal in `0..4095`. `sequence` is a 32-bit unsigned acquisition counter, incremented exactly once per acquisition modulo 2^32. Producer owns a record until handoff; detector owns its copy after acceptance. This synthetic ADC domain implies no physical ADC guarantee.

The detector publishes the exact integer sum of squares of the newest 32 contiguous accepted samples. Before 32 samples have been accepted since reset, missing prehistory contributes zero. Output range is `0..536,608,800` squared ADC counts and identifies the newest included sequence. Publish only after a complete update.

## Continuity and loss semantics (CON002-F01)

The producer/handoff interface provides the sequence metadata and a producer-owned, saturating unsigned 64-bit `loss_epoch`, initialized to zero for a session. The producer increments it once for every acquisition record lost before successful handoff. It is monotonic and is never acknowledged or cleared while the session is active. Increment is an indivisible read-modify-write with retry or equivalent serialization; concurrent losses may not overwrite one another. At saturation, it remains saturated. Any nonzero observation is a permanent continuity fault for that session, so further increments need not be distinguishable. The detector latches continuity fault and invalidates publication on observing nonzero. This removes the clear/acknowledgement race: the consumer never clears producer state. Reset to zero is permitted only after producer quiescence, handoff drain, and creation of a new session.

At session start, ingress reads zero `loss_epoch`, establishes the first delivered sequence as baseline, and sets expected sequence to its successor. For each record, ingress requires the next expected modulo-2^32 sequence and rechecks `loss_epoch` before accepting/publishing. Any mismatch, duplicate, nonzero epoch, or change from the session baseline is a continuity fault: reject the record, invalidate output, latch fault, and require explicit session reset before valid publication resumes. A change racing after the final check must be observed before any later record can be accepted; it cannot be cleared by acknowledgement.

The producer/handoff must enforce a maximum of **2^32-1 acquisition periods** between successfully delivered records, including startup and stalls. An independent receiver-side elapsed-time watchdog must invalidate the session before that bound is reached, even if the detector task is not scheduled; timeout is a fault and requires reset. This prevents a full 2^32-period gap from aliasing as a continuous modulo sequence. The watchdog timebase, scheduling independence, and strict timeout bound are integration obligations, not asserted physical guarantees. If they cannot be demonstrated, continuity remains unresolved and implementation approval is blocked. Ordinary wrap from `0xffffffff` to `0` is continuous within the bound.

An input outside `0..4095` is rejected before squaring, raises a bounded range fault, and does not mutate rolling state. Consumer reads only a complete prior or new result; partial publication is forbidden. Exact queue capacity, synchronization and physical reporting mechanisms remain DE/platform choices subject to these semantics.

## Timing, resources, verification

R-001 requires one sample per millisecond. Bound update, handoff response and independent timeout response; target WCET including interrupt interference must be at most 1 ms with documented margin (VO-004, TARGET_VALIDATION). Shared producer/consumer allocation is at most 128 bytes and counted once under C-002-SCOPE-001 (VO-002).

Verify ordering, loss-epoch monotonicity under concurrent loss, saturation, session reset preconditions, wrap, gap timeout while task is unscheduled, range rejection, startup and atomic publication by integration tests and target observation. Record queue capacity, overflow behavior, ISR priorities/nesting, scheduler response, watchdog timebase and fault observability. This draft discharges no VO.

## Responsible DEs

DE-AP2-INGRESS owns sequence/range validation, timeout response and continuity-fault reporting. DE-AP2-SHARED owns bounded handoff, producer loss epoch and result publication. DE-AP2-TASK consumes records and reports results/faults.
