---
type: Design Contract
id: CON-AP2-001
title: Sample ingress and detector result contract
status: draft
version: 1
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-001 v1: Sample ingress and result

## Boundary and data

The sample producer supplies one unsigned integer sample for each 1 ms acquisition period, in acquisition order. The legal domain is `0..4095` inclusive. The timestamp/order and sample value form one logical input; the producer owns the value until publication and the detector owns its copied value after acceptance. No analog accuracy or physical ADC guarantee is implied by the synthetic ADC source.

The detector publishes the exact integer sum of squares of the newest 32 accepted samples. Before 32 samples have been accepted since reset, unavailable older samples are zero. The output is a value in `0..536,608,800`; units are squared ADC counts. A result is associated with the newest sample included and is published only after the state update is complete.

## Preconditions, behavior, and failure

- Producer provides each sample once, in order, with no loss or duplication. The integration must demonstrate this property for the chosen queue/mailbox and scheduling arrangement.
- An input outside `0..4095` is rejected before squaring, raises a bounded range fault, and does not mutate ring state or publish a new valid result.
- A detected sequence gap, duplicate, or handoff overrun raises a bounded continuity fault. The detector does not silently treat a gap as a sample or publish a result marked valid for a discontinuous window. Recovery requires the defined reset operation and a new zero-padded window.
- The consumer may read only a fully published result. A result is either the previous complete result or the new complete result; partial publication is forbidden.

Exact fault reporting mechanism, queue capacity, and physical sample-loss detection depend on the target integration and remain unresolved until specified and reviewed.

## Timing, resources, verification

R-001 requires accepting one sample each millisecond. The update path must have a bounded execution and handoff response; target WCET including interrupt interference must be at most 1 ms with documented margin (VO-004, due TARGET_VALIDATION; verification-agent). The AP-002 allocation ceilings govern all storage, including handoff and publication. The producer/consumer shared allocation is capped at 128 bytes and must be counted once under C-002-SCOPE-001 (VO-002, due IMPLEMENTATION; implementation-agent).

Verify ordering, no-loss behavior, range rejection, reset startup, and atomic result publication by integration tests and target observation. Record queue capacity, overflow behavior, ISR priorities/nesting, scheduler response and fault observability. Acceptance requires independent review; this draft discharges no VO.

## Responsible design elements

DE-AP2-INGRESS owns source adaptation, ordering and range checks. DE-AP2-SHARED owns bounded handoff and publication. DE-AP2-TASK consumes accepted samples and reports results/faults.
