# TOY1-CON005 requirement, VO and debt coverage (v6)

| Item | v6 treatment | Owner / evidence | State |
|---|---|---|---|
| C-001 | Legal detector domain `[0,4095]`; out-of-domain behavior excluded | ingress DE / accepted VO-001 scope | VO-001 discharged only in accepted synthetic scope |
| C-002 / VO-002 | 2,048-byte charged-SRAM cap; category ceilings total 1,792 bytes plus 256-byte reserve | resource contract and DE; implementation inventory later | Open |
| C-003 / VO-003 | No reliance on floating-point hardware | source/build evidence | Open |
| R-001 / VO-004 | Exactly one update per accepted sample; independent of elapsed time | ingress/update DEs; implementation correspondence | Open; no deadline/throughput claim |
| R-002 / VO-005 | Exact newest 32 accepted samples, zero-padded startup | state/update/result DEs | Open |
| R-003 / VO-006 | Mathematical bounds; safe C expression widths; domain enforcement protects arithmetic | update DE and source evidence | Open |
| Reset lifecycle | Acceptance quiesced; no update in progress; quiescence through reset completion | state DE | Contract precondition; mechanism deferred |
| Result handoff | Coherent full-range post-update result associated with completed accepted-sample operation | result DE | Contract-defined; separate concurrent reader remains unapproved |
| Publisher continuity | Upstream publisher owns uninterrupted ordered delivery | external assumption | Unverified; no detector loss machinery |
| PR-002 | Abstract recurrence and bounds under stated assumptions | proof review | Mathematical scope only |
| AD-003 / F-001 | Preserve accepted debt and final comparison checkpoint | existing authority | Accepted; due before final acceptance |

No contract or DE is accepted and no VO is discharged by this draft or its
structural checks.
