---
type: Design Contract
id: CON-AP2-003-v5
title: Resource envelope and evidence obligations
status: draft
version: 5
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: constrained_by
    target: /architecture/AS-001/merit.md
  - kind: specifies
    target: /architecture/AS-001/contracts/CON-AP2-002-v5.md
---
# CON-AP2-003 v5: Resource and verification plan

## Resource boundary

The binding limit is at most 2,048 unique bytes of detector-attributable
SRAM under C-002-SCOPE-001. Accounting must cover persistent state,
temporary/scratch, detector stack, attributable interrupt context, shared
and dynamic allocations, and other attributable SRAM; count simultaneous
live storage, charge shared bytes no more than once, and justify any shared
storage by nonoverlapping lifetimes. Unrelated system memory is excluded only
when its lack of detector attribution is identified. This is a cap, not a
measurement or proof of feasibility.

This task does not establish numeric per-category allocations, target
topology, concurrency, stack sizes, shared-object sizes, or actual usage.
They remain unresolved for VO-002. The AP-002 proposal envelope is not treated
here as accepted measured evidence. Before implementation, the assigned owner
must provide a bounded, nonoverlapping peak inventory within 2,048 bytes,
with positive margin and evidence appropriate to the target. Dynamic-memory
policy is unspecified by this contract pending approved allocation and
integration requirements.

C-003 prohibits reliance on floating-point hardware. Integer-only behavior
is binding; actual source/build evidence is due under VO-003.

## Evidence and unresolved obligations

| Obligation | Contract evidence target | Owner / due |
|---|---|---|
| VO-002 / C-002 | Categorized charged-SRAM budget now; concrete layout, stack, interrupt, shared and dynamic attribution later | implementation-agent / IMPLEMENTATION |
| VO-003 / C-003 | Integer-only plan now; source/build evidence | implementation-agent / IMPLEMENTATION |
| VO-004 / R-001 | One bounded update for each accepted legal sample; no elapsed-time deadline | verification-agent / IMPLEMENTATION |
| VO-005 / R-002 | Accepted-sample order, zero-padded startup and exact latest-32 result | verification-agent / IMPLEMENTATION |
| VO-006 / R-003 | Mathematical bounds and C expression/range correspondence | verification-agent / IMPLEMENTATION |

All five obligations remain OPEN. No contract-level draft discharges them.
VO-001 remains discharged only within its accepted synthetic-domain scope.
AD-003 remains accepted; compare final evidence under unchanged F-001 before
final acceptance. No measured cycle or flash ranking is asserted.

Verification should use independent contract review, arithmetic/source
review, boundary and transition tests, static/resource accounting, and target
observations when implementation exists. Thresholds follow the binding
requirements above; target evidence is not available at this gate. Failure
or missing binding evidence is unresolved and requires correction or the
authorized AP/CON review path.
