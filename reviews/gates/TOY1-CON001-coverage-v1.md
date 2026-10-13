# TOY1-CON001 requirement and VO coverage (draft)

| Inherited item | Contract coverage | DE responsibility | Verification owner / due stage | State |
|---|---|---|---|---|
| C-001 / VO-001 | CON-AP2-001 legal input domain | DE-AP2-INGRESS | Existing accepted VO-001 receipt; scoped to synthetic ADC domain | Discharged within that scope |
| C-002 / VO-002 | CON-AP2-001 handoff; CON-AP2-002 state/scratch; CON-AP2-003 full categorized caps | DE-AP2-STATE, UPDATE, TASK, IRQ, SHARED, MEM | implementation-agent / IMPLEMENTATION | Open; map, stack, IRQ and shared attribution evidence pending |
| C-003 / VO-003 | CON-AP2-002 integer-only arithmetic | DE-AP2-UPDATE | implementation-agent / IMPLEMENTATION | Open; build/toolchain inspection pending |
| R-001 / VO-004 | CON-AP2-001 one sample per ms; CON-AP2-003 execution assumptions | DE-AP2-TASK, IRQ, SHARED | verification-agent / TARGET_VALIDATION | Open; target WCET and platform scheduling evidence pending |
| R-002 / VO-005 | CON-AP2-001 output semantics; CON-AP2-002 recurrence/reset | DE-AP2-STATE, UPDATE, TASK | verification-agent / IMPLEMENTATION | Open; concrete correspondence/integration review pending |
| R-003 / VO-006 | CON-AP2-002 range invariant and widened arithmetic | DE-AP2-UPDATE, STATE | proof-reviewer / IMPLEMENTATION | Open; C type/promotion and invariant mapping review pending |
| AD-003 | CON-AP2-003 preserves provisional allocation/timing checkpoints | All listed DE owners | evaluation-agent / before final acceptance | Accepted debt remains open to its due stage |

No VO is discharged by these drafts. Interface assumptions needing target resolution include producer continuity guarantees, queue capacity, ISR vector/priority/nesting, scheduler response, synchronization primitive and fault observability.
