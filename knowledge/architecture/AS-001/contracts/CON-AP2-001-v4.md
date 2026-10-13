---
type: Design Contract
id: CON-AP2-001-v4
title: Sample ingress and detector result contract
status: draft
version: 4
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-001-v3.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v4.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v4.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-001 v4: Sample ingress and result

## Boundary and data

For each 1 ms acquisition period, the producer supplies one logical record `(session, sequence, sample)` in acquisition order. `sample` is unsigned in `0..4095`; `sequence` is a 32-bit unsigned acquisition counter incremented once per acquisition modulo 2^32. Producer owns a record until successful handoff; ingress owns its copy after acceptance. The session identifier is an interface token, not a claim about physical ADC behavior. The detector publishes the exact integer sum of squares for the newest 32 contiguous accepted samples, zero-padding startup, and identifies the newest sequence and session. Publish only a complete update.

## Loss observation and publication linearization (CON003-F01)

The producer owns a saturating unsigned 64-bit `loss_epoch`, initialized to zero for each session. Every loss before successful handoff increments it once; increments are indivisible and serialized. It is never cleared while a session is active. Saturation is permanent continuity failure. The consumer never acknowledges or clears it.

The producer's loss decision/epoch increment, successful record handoff, consumer epoch observation, and result commit are ordered by one mutually exclusive handoff/publication protocol. A producer may not hand off a later record while an earlier loss is unreported. Consumer obtains a coherent epoch snapshot and holds the protocol exclusion continuously from its final epoch/sequence/session checks through the atomic result commit. Thus a loss ordered before commit is observed and the record is rejected; a loss ordered after commit immediately invalidates the result before any subsequent consumer commit. No valid result may remain externally observable after a loss event has linearized. The externally visible validity flag and result are changed atomically with respect to readers; a reader sees either the complete prior result/status or complete new result/status.

This exclusion and atomic visibility are semantic preconditions, not a selection of mutex/critical-section/atomic implementation. The integration must prove they cover producer loss reporting and handoff, consumer checks and commit, and output readers. If the producer can discover/report a loss only after publishing a later handoff, or the output reader can observe a partial/stale-valid result, continuity remains unresolved.

For the first record, ingress establishes the session and expected successor. Each subsequent record must match the active session and expected modulo-2^32 sequence. A mismatch, duplicate, nonzero/change in loss epoch, or watchdog expiry rejects the record, invalidates output, latches continuity fault, and prevents rolling updates until session reset. Ordinary wrap is continuous only if the independent elapsed-time condition below holds.

Session transition order is: atomically invalidate output; quiesce producer and stop new handoffs; drain/discard all old-session records; stop old watchdog; initialize rolling state and session-local epoch/sequence state; arm the new watchdog; then activate the new session and permit handoff. No old-session record or result may be accepted or published after activation. Failure to establish this order leaves output invalid and the session inactive.

## Independent watchdog (CON003-F02)

The watchdog is receiver-side and must continue while the detector task is unscheduled. Each successful handoff is the sole event that restarts its elapsed-time bound; queue enqueue attempts, task wakeups, and timer callbacks do not restart it. The receiver starts the watchdog before accepting the first session record. If the next successful handoff does not occur, timeout invalidates output and latches fault without waiting for detector-task execution.

Let `P=1 ms` and `B=(2^32-1)P`. The target integration must select and evidence a conservative timer conversion and a positive margin `M` such that the latest possible invalidation, including conversion error, interrupt latency, and response latency, is strictly earlier than `B-M`, with `M>0`. Timer rounding must never postpone expiration; use a conservative lower bound on elapsed real time or an equivalent proven bound. The timer must span the required interval without wrap ambiguity or be extended with a separately bounded mechanism. Timeout response is the atomic invalidation of externally visible validity; its maximum response is part of the bound and must be enforced independently of detector-task scheduling. These are checkable integration obligations, not assumed MCU capabilities. Until timer range, conversion error, margin, response and ownership are evidenced for the target, the continuity contract remains unresolved.

Out-of-range samples are rejected before squaring and do not mutate rolling state. The 1 ms update deadline, range-fault reporting, publication and reset semantics remain subject to VO-004/VO-005. This contract discharges no VO.

## Responsible DEs

DE-AP2-INGRESS owns session/sequence validation, fault latching and timeout semantics. DE-AP2-SHARED owns the ordered handoff/loss/publication protocol and atomic validity visibility. DE-AP2-IRQ owns watchdog event delivery and its scheduling independence. Platform synchronization and timer implementations remain deferred pending evidence against these semantics.
