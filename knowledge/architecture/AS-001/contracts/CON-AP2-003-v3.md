---
type: Design Contract
id: CON-AP2-003-v3
title: AP-002 execution, concurrency, and resource boundary
status: draft
version: 3
relations:
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-003-v2.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: specifies
    target: /architecture/AS-001/proposals/envelopes/AP-002-SRAM-ENVELOPE-001.md
---
# CON-AP2-003 v3: Execution and resource accounting

## Execution model and shared inventory

The v2 model remains: one periodic detector task, at most one non-nested sample-capture ISR, ISR hands off but never updates rolling state, one task writer, no recursion/callback into state, and no second detector instance. Platform choices remain deferred only if they enforce the contract semantics.

Within the existing 128-byte detector-attributable shared-allocation cap, inventory once: bounded handoff storage; 32-bit expected sequence and initialized/session state; producer-owned 64-bit saturating loss epoch; publication value, sequence and status; synchronization objects; and watchdog state/timebase allocation if detector-attributable. No item may be omitted or double charged. Alignment/padding and atomic implementation costs must be included in VO-002 layout evidence. The approved 2048-byte total detector-attributable SRAM cap, category ceilings (72 persistent, 64 scratch, 384 task stack, 128 IRQ, 128 shared, 0 dynamic, 128 other), 904 allocated ceiling and 1024-byte reserve are unchanged from CON-AP2-003-v2. A fit for the new shared inventory is not yet demonstrated; if it does not fit, stop and request controlled revision rather than enlarge any cap.

The producer loss epoch increment and session reset must be serialized as required by CON-AP2-001-v3. Consumer observation is read-only and cannot clear or acknowledge the epoch. The receiver-side elapsed-time watchdog must operate independently of detector-task scheduling and fault before 2^32-1 acquisition periods without a successful handoff. Concrete timer range, continued operation during stalls, response time, ISR/task interaction, and resource attribution require target evidence; absence of that evidence leaves the continuity obligation unresolved.

VO-002 remains open pending map, layout, stack/interrupt, shared and attribution evidence. VO-003 through VO-006 remain open. AD-003 remains accepted and due before final acceptance. No authority or acceptance state changes.
