# Independent contract review: TOY1-CON002

- Input revision: `e14b2d100eeb8de4fd630e7b58f7bc14ad556a66`
- Trigger revision: `edffca69e8e7dc6c10623558f768da72f3246d0c`
- Submission revision recorded by author: `c99dbc56fc0baadca03b6489b7a60f0cc2f8a74d`
- Disposition: **REVISE**
- Next-stage recommendation: **CON_REVISION_REQUIRED**

This review is independent of the contract-authoring invocation. The active v2 drafts close the original field-accounting gap, but the continuity semantics still admit loss of an overrun indication during acknowledgement. The stated exclusion of an unobservable 2^32-acquisition gap also remains a requirement without a specified enforceable bound or mechanism.

## Findings

### CON002-F01 — Blocking: continuity faults can be cleared across a new overrun

**Evidence:** CON-AP2-001-v2 requires an overrun indication to persist until detector acknowledgement, but does not define the atomicity or generation semantics of acknowledgement. CON-AP2-003-v2 leaves the synchronization primitive and concrete handoff to later DE work. The contract also says the producer/handoff must prevent an unobservable gap of exactly 2^32 acquisitions, without stating a maximum handoff latency/outstanding gap or another enforceable means to make that guarantee true.

**Counterexample:** Detector observes the overrun flag and begins acknowledgement. Before the acknowledgement clears the flag, another sample is lost and the producer sets the same flag. A non-atomic clear then erases the new event. The detector can resume with a discontinuous window while believing continuity is intact. Separately, if 2^32 acquisitions elapse between observed records, the modulo counter matches the expected sequence, and there is no required check that can distinguish this gap absent a bounded-gap guarantee.

**Required resolution:** Specify an acknowledgement protocol that cannot erase an overrun occurring after the detector's observation (for example, atomic consume/exchange or a generation protocol), and state which producer/handoff owner enforces it. Give a checkable maximum outstanding gap/latency or equivalent mechanism that rules out a full counter-period gap. Preserve reset-required invalidation after any detected fault.

### CON002-F02 — Resolved: persistent-state accounting

The v2 inventory sums to `64 + 4 + 1 + 1 + 1 = 71` bytes, within the 72-byte persistent-state cap, leaving 1 byte. The 32 ring entries are each 16 bits and the rolling sum is 32 bits. Publication value, sequence and status, expected-sequence tracking and synchronization are assigned to the separate shared allocation in CON-AP2-003-v2 and are not charged a second time as persistent state in CON-AP2-002-v2. The 128-byte shared cap is a budget, not target layout evidence; that remains VO-002 implementation evidence. No F02 blocker remains at this contract gate.

## Coverage and authority

- CON001-F01: **not closed**; see CON002-F01.
- CON001-F02: **closed at contract level**; concrete layout and attribution evidence remains under VO-002.
- VO-001: discharged within synthetic ADC domain only, per ledger and accepted receipt.
- VO-002 through VO-006: remain open; no obligation discharged by this review.
- AD-003: remains accepted, due before final acceptance; unchanged.
- Approved AP-002 provisional selection, AS, F and C-002 scope: unchanged.
- DE approval and firmware approval: none inferred.

## Checks and limits

- `python tools/task.py inspect --manifest process/tasks/TOY1-CON002-REVIEW.yaml` — PASS; manifest role, playbook, spine and gate resolved.
- `python tools/pc.py check --fast` — PASS; 48 concepts, 188 typed links, zero warnings/errors. Structural check only; raw hashes skipped by the checker.
- Persistent field byte arithmetic independently recalculated as above.

Not inspected: firmware/source implementation, concrete MCU/RTOS queue and synchronization configuration, compiler output/linker map, stack/interrupt measurements, target timing, and raw data. No target or host integration tests were run as part of this review.

## Next eligible action

Contract Agent should prepare additive v3 contracts resolving CON002-F01 while preserving v1 and v2 history. Then request another independent `REVIEW_CON`. Do not begin DE refinement or firmware implementation until an accepted contract review receipt exists.
