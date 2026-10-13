# TOY1-CON002 requirement, VO and debt coverage (draft)

| Inherited item | Contract coverage | DE responsibility | Verification owner / due stage | State |
|---|---|---|---|---|
| C-001 / VO-001 | CON-AP2-001-v2 legal domain and reset | DE-AP2-INGRESS | Accepted receipt, synthetic ADC scope only | Discharged within that scope |
| C-002 / VO-002 | CON-AP2-001-v2 handoff/overrun; CON-AP2-002-v2 71-byte field inventory and scratch; CON-AP2-003-v2 full categorized envelope | INGRESS, STATE, UPDATE, TASK, IRQ, SHARED, MEM | implementation-agent / IMPLEMENTATION | Open; map, layout, stack, IRQ and shared attribution pending |
| C-003 / VO-003 | CON-AP2-002-v2 widened integer-only arithmetic | DE-AP2-UPDATE | implementation-agent / IMPLEMENTATION | Open; build/toolchain inspection pending |
| R-001 / VO-004 | CON-AP2-001-v2 1 ms ingress; CON-AP2-003-v2 execution assumptions | DE-AP2-TASK, IRQ, SHARED | verification-agent / TARGET_VALIDATION | Open; target WCET and scheduling evidence pending |
| R-002 / VO-005 | CON-AP2-001-v2 contiguous-window output; CON-AP2-002-v2 recurrence/reset; shared publication | DE-AP2-STATE, UPDATE, TASK, SHARED | verification-agent / IMPLEMENTATION | Open; concrete correspondence/integration review pending |
| R-003 / VO-006 | CON-AP2-002-v2 range invariant and widened arithmetic | DE-AP2-UPDATE, STATE | proof-reviewer / IMPLEMENTATION | Open; C type/promotion and invariant mapping review pending |
| AD-003 | CON-AP2-003-v2 preserves allocation and timing checkpoints | All listed DE owners | evaluation-agent / before final acceptance | Accepted; remains open to due stage |

## Finding closure map

| Finding | Correction | Evidence | Status |
|---|---|---|---|
| CON001-F01 | Sequence counter on every acquisition plus persistent acknowledgeable overrun indication; mismatch/overrun invalidates output and requires reset. Modulo wrap semantics and unobservable 2^32-gap limit are explicit. | CON-AP2-001-v2 §§ Boundary, Enforceable continuity; CON-AP2-003-v2 execution model | Addressed in draft; independent review required |
| CON001-F02 | Explicit field inventory charges 64+4+1+1+1=71 bytes to persistent state, leaving 1 byte of the approved 72-byte cap. Publication data/metadata and synchronization are explicitly charged to shared 128-byte cap, once. | CON-AP2-002-v2 inventory; CON-AP2-003-v2 categorized envelope | Addressed in draft; concrete layout evidence remains VO-002 |

No VO is discharged. AP, AS, F, C-002 authority and AD-003 are unchanged. Platform queue/IRQ/scheduler details remain deferred subject to enforceability of these semantics.
