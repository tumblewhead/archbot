# TOY1-CON004 requirement, VO and debt coverage

| Item | v4 treatment | Owner / evidence | State |
|---|---|---|---|
| CON003-F01 | CON-AP2-001-v4 orders loss report, handoff, final consumer checks and commit under a shared exclusion; specifies atomic result visibility and session transition order. Producer may not hand off a later record while loss is unreported. | DE-AP2-SHARED / INGRESS; prove protocol and reader visibility under VO-005 | Semantics specified with explicit integration preconditions; independent review required |
| CON003-F02 | Each successful handoff restarts receiver elapsed-time bound; first session record starts it. Timeout invalidates output without task scheduling. `B=(2^32-1) ms`; target must prove conservative conversion, positive margin, timer range and latest invalidation strictly before `B-M`. | DE-AP2-IRQ / SHARED; target timer and response evidence, VO-004/VO-005 | Contract conditions specified; target evidence remains open |
| CON003-F03 | Existing 128-byte shared cap retained. Required object classes enumerated, but sizes/capacity/representation are not established. | DE-AP2-SHARED; numerical inventory, owner and overlap plan under VO-002 | **Unresolved blocker**; no fit or cap change claimed |
| CON003-F04 | Persistent inventory remains 71 bytes under 72-byte cap. | DE-AP2-STATE; physical layout under VO-002 | Contract-level closure retained; physical evidence open |
| VO-001 | Synthetic ADC legal domain only | Accepted receipt | Discharged only within accepted scope |
| VO-002 | Shared numeric fit, layout, padding, stack/interrupt and attribution | Implementation-agent | Open |
| VO-003 | Integer arithmetic implementation | Implementation-agent | Open |
| VO-004 | 1 ms timing and watchdog response | Verification-agent | Open |
| VO-005 | Exact contiguous output and fault behavior | Verification-agent | Open |
| VO-006 | Range and arithmetic invariants | Proof-reviewer | Open |
| AD-003 | F comparison due before final acceptance | Evaluation-agent / engineering authority | Accepted; unchanged |

No VO is discharged, no AD accepted, and AP/AS/F/C-002 authority is unchanged. Because CON003-F03 remains unresolved, status is `CONTRACTS_UNRESOLVED`; minimum next evidence is a concrete, bounded shared-object allocation and ownership plan within the approved 128-byte ceiling, or controlled authority revision if infeasible.
