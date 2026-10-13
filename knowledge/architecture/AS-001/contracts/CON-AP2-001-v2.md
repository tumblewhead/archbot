---
type: Design Contract
id: CON-AP2-001-v2
title: Sample ingress and detector result contract
status: draft
version: 2
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: addresses
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v2.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-003-v2.md
  - kind: constrained_by
    target: /bkp/adc.md
---
# CON-AP2-001 v2: Sample ingress and result

## Boundary and data

For each 1 ms acquisition period, the producer supplies one logical record `(sequence, sample)`, in acquisition order. `sample` is unsigned and legal in `0..4095`. `sequence` is a 32-bit unsigned acquisition counter, incremented exactly once per acquisition using modulo-2^32 arithmetic. The producer owns each record until handoff; the detector owns its copied value after acceptance. This synthetic ADC domain implies no physical ADC guarantee.

The detector publishes the exact integer sum of squares of the newest 32 contiguous accepted samples. Before 32 samples have been accepted since reset, missing prehistory contributes zero. The output range is `0..536,608,800` squared ADC counts and identifies the sequence of the newest included sample. Publish only after a complete update.

## Enforceable continuity semantics (resolves CON001-F01)

The producer/handoff boundary MUST provide both sequence metadata and an overrun indication that remains observable until acknowledged. On the first record after reset, ingress establishes the baseline and sets expected sequence to its successor. For each later delivered record, ingress compares `sequence` with the expected successor modulo 2^32, then advances expected sequence after acceptance. A mismatch, duplicate, or asserted overrun is a continuity fault; do not accept that record into a valid window, mark the result invalid, latch the fault, and require reset/reinitialization before valid publication resumes. The overrun indication covers any lost record, including loss before enqueue; it is cleared only after detector acknowledgement. The integration must show that the counter is incremented for every acquisition and that overrun cannot be lost or cleared prematurely. Sequence wrap from 0xffffffff to 0 is continuous. The source/handoff contract must prevent an unobservable gap of exactly 2^32 acquisitions between delivered records; if that cannot be enforced, this interface is unresolved and must be revised before implementation approval.

An input outside `0..4095` is rejected before squaring, raises a bounded range fault, and does not mutate rolling state. The consumer reads only a fully published result, either prior complete or new complete; partial publication is forbidden. Exact queue capacity, synchronization and physical reporting mechanisms remain DE/platform choices, subject to these semantics.

## Timing, resources, verification

R-001 requires one sample per millisecond. Bound update and handoff response; target WCET including interrupt interference must be at most 1 ms with documented margin (VO-004, TARGET_VALIDATION, verification-agent). The AP-002 ceilings apply to all storage. Producer/consumer shared allocation is at most 128 bytes and counted once under C-002-SCOPE-001 (VO-002, IMPLEMENTATION, implementation-agent).

Verify ordering, loss/duplicate detection, overrun persistence/acknowledgement, range rejection, reset startup and atomic publication by integration tests and target observation. Record queue capacity, overflow behavior, ISR priorities/nesting, scheduler response and fault observability. This draft discharges no VO.

## Responsible DEs

DE-AP2-INGRESS owns counter comparison, range validation and fault requests. DE-AP2-SHARED owns bounded handoff, persistent overrun indication and publication. DE-AP2-TASK consumes records and reports results/faults.
