---
type: Design Contract
id: CON-AP2-003-v4
title: AP-002 execution, concurrency, and resource boundary
status: draft
version: 4
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-003-v3.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: specifies
    target: /architecture/AS-001/proposals/envelopes/AP-002-SRAM-ENVELOPE-001.md
---
# CON-AP2-003 v4: Execution and resource accounting

## Execution and synchronization obligations

The v3 single task writer, at most one non-nested capture ISR, no recursion/callback into state, and no second detector instance constraints remain. The handoff/loss/result commit protocol and independent receiver watchdog must satisfy CON-AP2-001-v4. Any concrete synchronization object, ISR path, timer state or output validity mechanism is subject to the unchanged C-002 attribution rules. Queue capacity, timer mechanism and primitive are not selected here.

## Shared allocation blocker (CON003-F03)

The detector-attributable shared allocation ceiling remains 128 bytes. The known inventory is: bounded handoff record storage; expected sequence and session/initialized control; producer-owned 64-bit loss epoch; published value, sequence, session and validity/status; synchronization/control needed to serialize producer loss reporting, handoff, consumer check/commit and readers; and receiver watchdog counter/timebase/control state. Each allocation must be counted once, with widths, alignment/padding, lifetime, overlap and ownership stated. The current evidence does not specify handoff capacity or the concrete representation and sizes of synchronization, session, publication and watchdog objects. Therefore no numeric shared allocation or fit is established. This contract is unresolved under the existing 128-byte cap; no cap increase or fit claim is made. Before DE refinement, the integration owner must provide a bounded numeric object inventory and nonoverlapping peak allocation plan at or below 128 bytes, or request controlled authority revision if that cannot be achieved.

The other approved limits remain unchanged: 72 persistent, 64 scratch, 384 task stack, 128 IRQ, 0 dynamic, 128 other detector-attributable bytes, 904 allocated ceiling, and 1024-byte reserve within 2048 bytes total. These are caps, not measured usage. VO-002 remains open for numeric shared fit, physical layout, padding, stacks and attribution; VO-003 through VO-006 remain open. AD-003 remains accepted and due before final acceptance. No authority or acceptance state changes.
