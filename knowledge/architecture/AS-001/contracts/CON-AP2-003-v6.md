---
type: Design Contract
id: CON-AP2-003-v6
title: Resource envelope and evidence obligations
status: draft
version: 6
relations:
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: constrained_by
    target: /architecture/AS-001/merit.md
  - kind: derived_from
    target: /architecture/AS-001/contracts/CON-AP2-003-v5.md
---
# CON-AP2-003 v6: Resource and verification plan

## C-002 charged-SRAM envelope

The binding C-002 cap is 2,048 unique detector-attributable SRAM bytes.
The following are **contract-stage category ceilings**, not measured usage
or claims about the target. They are nonoverlapping accounting buckets;
simultaneously live bytes are charged to exactly one bucket. Shared storage
is counted once under a documented conservative attribution. The ceilings
sum to 1,792 bytes, leaving a positive 256-byte unallocated reserve.

| Category | Ceiling (bytes) |
|---|---:|
| Persistent detector state | 256 |
| Temporary and scratch | 128 |
| Detector stack | 512 |
| Detector-attributable interrupt context | 256 |
| Detector-attributable shared allocations | 256 |
| Detector-attributable dynamic allocations | 128 |
| Other detector-attributable SRAM | 256 |
| **Allocated ceiling** | **1,792** |
| **Unallocated reserve** | **256** |
| **C-002 limit** | **2,048** |

These ceilings are enforceable only under these explicit conditions:

1. The implementation-stage inventory identifies every charged byte and
   category, proves the nonoverlap and lifetime claims, and checks each
   category against its ceiling and the aggregate cap.
2. Stack and interrupt-context ceilings cover worst-case detector activity
   and relevant nesting. No particular task, ISR, scheduler, or interrupt
   topology is assumed; if the selected integration cannot satisfy its
   applicable ceilings, the contract is unresolved and requires a reviewed
   budget revision before implementation acceptance.
3. Shared allocations use documented detector attribution and are charged
   once. Dynamic allocations, if any, have bounded peak simultaneously-live
   bytes within their category ceiling. The contract does not mandate a heap
   prohibition.
4. Unrelated system allocations are excluded only when their lack of
   detector attribution is documented. Any category ceiling found
   infeasible is not permission to exceed it or the approved C-002 cap.

The ceilings are a conditional budget commitment, not evidence of physical
feasibility. Concrete layout, stack/interrupt analysis, dynamic bounds,
shared attribution, and final use evidence remain due under VO-002 at
IMPLEMENTATION. This charged-SRAM envelope is distinct from any F state-SRAM
metric. The approved cap is not changed.

## Other requirements and evidence

C-003 prohibits reliance on floating-point hardware. Integer-only behavior
is binding; source/build evidence remains due under VO-003.

| Obligation | Contract evidence target | Owner / due |
|---|---|---|
| VO-002 / C-002 | Category ceilings and reserve above; concrete inventory and target verification later | implementation-agent / IMPLEMENTATION |
| VO-003 / C-003 | Integer-only plan; source/build evidence | implementation-agent / IMPLEMENTATION |
| VO-004 / R-001 | One bounded update per accepted published sample; no elapsed-time deadline | verification-agent / IMPLEMENTATION |
| VO-005 / R-002 | Accepted-sample order, zero-padded startup, exact latest-32 result | verification-agent / IMPLEMENTATION |
| VO-006 / R-003 | Mathematical bounds and C expression/domain correspondence | verification-agent / IMPLEMENTATION |

VO-002 through VO-006 remain OPEN. VO-001 remains discharged only within
its accepted synthetic-domain scope. AD-003 remains accepted; final F-001
comparison remains due before final acceptance. No target measurements,
resource fit, cycle or flash ranking is asserted.
