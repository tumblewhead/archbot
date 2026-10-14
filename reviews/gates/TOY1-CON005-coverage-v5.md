# TOY1-CON005 requirement, VO and debt coverage

| Item | v5 treatment | Owner / evidence | State |
|---|---|---|---|
| C-001 | Legal detector input is unsigned 12-bit `[0,4095]`; synthetic scope only | DE-AP2-INGRESS-v5 / accepted VO-001 scope | Binding domain; VO-001 discharged only in accepted scope |
| C-002 | At most 2,048 unique detector-attributable SRAM bytes under C-002-SCOPE-001, all categories and simultaneous peak accounted once | DE-AP2-RESOURCE-v5; numeric and target evidence under VO-002 | Limit binding; allocation unresolved |
| C-003 | No reliance on floating-point hardware | DE-AP2-RESOURCE-v5 / implementation build evidence | Binding; VO-003 open |
| R-001 | Exactly one update per accepted legal sample, independent of elapsed time | ingress/update DEs; one-to-one evidence | VO-004 open; no deadline or throughput claim |
| R-002 | Exact newest 32 accepted samples, zero-padded startup | state/update/result DEs; recurrence correspondence | VO-005 open |
| R-003 | No overflow for legal inputs; validate before square, safe C expression types | update DE; source and arithmetic evidence | VO-006 open |
| Publisher boundary | Publisher owns uninterrupted ordered delivery; detector does not detect/reconstruct losses | external integration owner not assigned | Unverified assumption |
| PR-002 | Abstract integer recurrence, bounds, initialization and wrap assumptions | accepted proof review | Mathematical scope only; not implementation proof |
| AD-003 / F-001 | Preserve accepted debt and final comparison before final acceptance | evaluation-agent / existing authority | Accepted; unresolved until existing checkpoint |

All active VO-002 through VO-006 remain OPEN. This matrix and structural
checks do not accept the contracts, prove implementation correctness, or
establish publisher/target evidence.
