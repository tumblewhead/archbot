# TOY1-CON003 requirement, VO and debt coverage (draft)

| Item | v3 contract coverage | Responsibility / evidence owner | State |
|---|---|---|---|
| CON002-F01 race-safe loss observation | CON-AP2-001-v3: saturating monotonic producer loss epoch; consumer never clears/acks; session reset only after producer quiescence and drain. CON-AP2-003-v3 charges epoch and synchronization to existing shared cap. | DE-AP2-SHARED / DE-AP2-INGRESS; atomicity and concurrency evidence under VO-002/VO-005 | Addressed in draft; independent review required |
| CON002-F01 full-period sequence alias | CON-AP2-001-v3: independent receiver-side elapsed-time watchdog faults before 2^32-1 acquisition periods without successful handoff, including while task is unscheduled. Explicitly unresolved if independent operation and strict bound cannot be demonstrated. | DE-AP2-INGRESS / DE-AP2-IRQ / DE-AP2-SHARED; target evidence under VO-004 and integration review VO-005 | Enforceable obligation specified; evidence remains due |
| CON002-F02 | Carried forward unchanged: persistent inventory remains 71 bytes within 72-byte cap; shared objects charged once within existing 128-byte cap. | DE-AP2-STATE / DE-AP2-SHARED; target layout under VO-002 | Prior contract-level closure retained; target evidence open |
| C-001 / VO-001 | Synthetic ADC legal domain; accepted receipt remains limited to synthetic scope. | DE-AP2-INGRESS | Discharged within accepted scope only |
| C-002 / VO-002 | Full categorized envelope unchanged; new loss epoch/watchdog allocations included in shared inventory. | All DE owners / implementation-agent | Open; layout, map, stacks, shared attribution pending |
| C-003 / VO-003 | Integer-only widened arithmetic carried forward. | DE-AP2-UPDATE / implementation-agent | Open |
| R-001 / VO-004 | 1 ms period and bounded watchdog response. | DE-AP2-TASK, IRQ, SHARED / verification-agent | Open; target WCET and watchdog evidence pending |
| R-002 / VO-005 | Exact contiguous 32-sample output; continuity fault invalidates output and blocks updates until session reset. | STATE, UPDATE, TASK, SHARED / verification-agent | Open; concrete correspondence/integration review pending |
| R-003 / VO-006 | Range and arithmetic invariants carried forward. | UPDATE, STATE / proof-reviewer | Open |
| AD-003 | Allocation/timing checkpoints retained; no change to accepted debt. | All DE owners / evaluation-agent | Accepted; due before final acceptance |

No VO is discharged. AP, AS, F, C-002 authority, and AD-003 are unchanged. `loss_epoch` and watchdog fit within existing ceilings only if later target accounting demonstrates that; no cap increase is proposed.
