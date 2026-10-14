---
type: Design Element
id: DE-AP2-RESOURCE-v7
title: Conditional resource allocation and evidence composition
status: draft
version: 7
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-003-v6.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: addresses
    target: /architecture/AS-001/merit.md
---
# DE-AP2-RESOURCE-v7

**Purpose and boundary.** Own the implementation-stage accounting and
evidence package demonstrating that the combined design stays within the
approved C-002 charged-SRAM envelope and provides integer-only behavior.
This is an attribution/evidence responsibility, not a claim of physical
fit or target measurement.

**Conditional budget and conceptual attribution.** The v6 contract's
nonoverlapping charged-SRAM category ceilings remain binding: persistent
256 B; temporary/scratch 128 B; detector stack 512 B; attributable
interrupt context 256 B; shared allocations 256 B; dynamic allocations
128 B; other attributable SRAM 256 B. Allocated ceilings total 1,792 B,
with 256 B reserve under 2,048 B. The following are proposed DE-level
subceilings for implementation inventory and attribution. They are not
measured sizes or new total budgets; the column totals are exactly the v6
category ceilings. RESOURCE owns cross-element shared/dynamic/other
accounting and integration reconciliation.

| Element | Persistent | Scratch | Stack | IRQ context | Shared | Dynamic | Other |
|---|---:|---:|---:|---:|---:|---:|---:|
| INGRESS | 0 | 16 | 96 | 128 | 0 | 0 | 0 |
| STATE | 256 | 16 | 96 | 0 | 0 | 0 | 0 |
| UPDATE | 0 | 48 | 192 | 128 | 0 | 0 | 0 |
| RESULT | 0 | 16 | 64 | 0 | 0 | 0 | 0 |
| RESOURCE / integration reconciliation | 0 | 32 | 64 | 0 | 256 | 128 | 256 |
| **Column ceiling totals** | **256** | **128** | **512** | **256** | **256** | **128** | **256** |

These are ownership partitions for accounting, not claims that each
element's actual usage fits. At implementation, attribute every byte once
to its owner and category; account for overlapping lifetimes and relevant
nesting in the applicable stack/context subceilings. The complete measured
inventory must meet each subceiling and category ceiling. Any infeasible
subceiling requires design review before implementation acceptance; no
aggregate or category ceiling may be exceeded.

No separate concurrent-reader state or transport buffer is assumed.
Dynamic allocations are not forbidden; if used, their bounded simultaneous
peak must be inventoried within the existing category ceiling. The concrete
inventory must identify every live allocation, owner, lifetime, overlap,
shared attribution and category sum; show per-category ceilings and total
≤2,048 B. If a ceiling is infeasible in the selected integration, the
design is unresolved and requires reviewed budget change before
implementation acceptance.

**Other evidence.** Provide source/build evidence that the implementation
does not rely on floating-point hardware (VO-003). Coordinate evidence
collection for VO-002; do not represent estimates as measurements. VO-004
through VO-006 remain assigned to verification-agent in the active ledger.
The active F objective and accepted AD-003 remain unchanged; final F-001
comparison remains due before final acceptance.

**Verification hooks.** At implementation, produce a reproducible charged
memory inventory and category/lifetime reconciliation, stack and relevant
context/nesting analysis, shared and dynamic attribution, integer-only
source/build evidence, and target measurements when available. This
design-stage allocation alone discharges no obligation.
