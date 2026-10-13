# Independent contract review: TOY1-CON003

**Disposition: REVISE**  
**Next-stage recommendation: CON_REVISION_REQUIRED**  
**Reviewed checkout:** `bf5e5982d8f7cd6bab5518ebf497e23117f24ee8`

This review covers the v3 contract draft submitted from `d995e15fe45349553c22aee36cc53f4f23000cd7`. The submitted contracts are present at the reviewed checkout. No AP, AS, F, VO, AD, DE-approval, or implementation state is changed by this review.

## Findings

### CON003-F01 — Blocking: loss can race the last check and publication

**Contract:** CON-AP2-001-v3; related ownership in CON-AP2-003-v3.

The producer-owned saturating epoch removes the prior clear/acknowledge race if its update is truly serialized. The contract requires an indivisible read-modify-write or equivalent serialization, so concurrent producer losses cannot overwrite each other. Saturation is safe for the stated purpose because any nonzero value permanently faults the session. Reset after producer quiescence and handoff drain is directionally sound.

However, consumer reads are not specified as coherent/atomic observations, nor is there a commit/publication ordering that closes the interval after the final epoch read. Minimal counterexample: ingress reads `loss_epoch == 0`; a record is handed off; the producer loses a later acquisition and increments the epoch; ingress commits or publishes the earlier record based on its stale final read. That record can be visible as valid after continuity has already failed. The clause requiring a racing change to be observed before a *later* record is accepted does not prevent this already-in-flight record from being committed or published as valid.

**Required correction:** define a linearization/serialization guarantee across the final loss observation and record acceptance/publication, or define an equivalent producer-consumer handshake that guarantees any loss racing an in-flight record invalidates that record and the published result before it is externally observable as valid. Specify coherent epoch reads on the target interface and session-reset ordering so stale records or observations from the prior session cannot be accepted. Do not assume a particular MCU atomic instruction or lock primitive.

### CON003-F02 — Watchdog rule is directionally useful; enforceability remains unresolved

**Contract:** CON-AP2-001-v3 and CON-AP2-003-v3.

Requiring a watchdog independent of detector-task scheduling addresses the failure mode identified in CON002-F01. The stated maximum gap of `2^32-1` acquisition periods is strict enough in principle to rule out a gap of `2^32` periods, which would alias under the modulo sequence counter. The contract correctly states that target timebase, scheduling independence, and timeout evidence are not established and that continuity remains unresolved if they cannot be demonstrated.

The interface rule still lacks a fully checkable timing definition: it does not define the watchdog start/restart event, how elapsed time maps to acquisition periods under clock tolerance or stalled acquisition, or the bound from deadline detection to invalidating the published result. “Before that bound is reached” should be tied to a named successful-handoff event and an explicit maximum elapsed-time/period conversion with margin. The receiving mechanism must remain able to invalidate output while the detector task is unscheduled.

**Required correction/evidence:** state those timing semantics as an integration guarantee, with DE-AP2-INGRESS and DE-AP2-IRQ ownership and a target acceptance method. Keep implementation approval blocked unless target/integration evidence demonstrates the strict bound and independent fault response. No physical timer, clock, scheduler, or ADC capability is inferred here.

### CON003-F03 — New shared allocations are inventoried but not yet bounded

**Contract:** CON-AP2-003-v3.

The v3 draft names the 64-bit loss epoch and watchdog state/timebase, along with the handoff, expected-sequence/session state, publication, and synchronization. It assigns them once to the existing 128-byte shared ceiling and prohibits increasing that ceiling. This is the right accounting scope and does not silently alter the approved 2,048-byte envelope.

The draft does not give a bounded shared-memory allocation for the watchdog state/timebase or synchronization and handoff objects, so the named inventory cannot yet be arithmetically shown to fit 128 bytes. The draft itself acknowledges this. Treat fit as **unresolved under VO-002**, not as a demonstrated pass. Before DE refinement, preserve a concrete bounded allocation/ownership plan within the existing shared cap; physical layout, padding, and attribution evidence remain due under VO-002.

### CON003-F04 — CON002-F02 remains closed at contract level

**Contract:** CON-AP2-002-v3 and CON-AP2-003-v3.

The persistent field inventory is carried forward as `64 + 4 + 1 + 1 + 1 = 71` bytes, within the 72-byte persistent-state cap. Publication, expected sequence, synchronization, loss epoch, and watchdog-related state are assigned to the shared category rather than silently added to persistent state or counted twice. Thus the original CON002-F02 contract-level accounting defect remains closed. This is not physical-layout verification; VO-002 remains open for concrete layout, padding, stacks/interrupts, attribution, and map evidence.

## Coverage and continuing obligations

- **AP-002 / AS-001 / F-001:** unchanged; AP-002 remains provisionally selected under the accepted authority decision. No final F ranking is claimed.
- **PR-002:** abstract integer rolling-sum result remains conditional on its stated assumptions; it does not establish ingress concurrency or target behavior.
- **VO-001:** discharged only within the accepted synthetic ADC domain.
- **VO-002:** open; includes the new shared allocation and all physical memory attribution/layout evidence.
- **VO-003:** open; concrete integer implementation evidence remains due.
- **VO-004:** open; 1 ms timing and watchdog target response remain due.
- **VO-005:** open; end-to-end continuity, publication and exact-window integration remain due.
- **VO-006:** open; concrete range/arithmetic invariant evidence remains due.
- **AD-003:** accepted and unchanged; due before final acceptance.

No DE refinement or firmware implementation is authorized by this review. After a versioned correction and fresh independent review, DE refinement may be reconsidered only if the contract gate is favorable and its conditions are carried forward.

## Checks and limits

- `python tools/task.py inspect --manifest process/tasks/TOY1-CON003-REVIEW.yaml` — PASS; manifest, role, playbook, spine, and gate resolve.
- `python tools/pc.py check --fast` — PASS; 52 concepts, 217 typed links, zero warnings/errors. Structural check only; no proof or engineering acceptance.
- `git diff --check` — PASS.
- Independently recalculated persistent inventory: `64 + 4 + 1 + 1 + 1 = 71` bytes, within 72 bytes.
- Not inspected/available: firmware implementation, concrete MCU/RTOS synchronization and timer configuration, compiler output/linker map, target WCET/stack/interrupt evidence, raw data.

## Reviewed inputs

Exact SHA-256 values are recorded in `TOY1-CON003-independent-review-v3.json`. The input revision is the reviewed checkout HEAD above; the manifest's trigger revision identifies the submitted contract-draft source revision.
