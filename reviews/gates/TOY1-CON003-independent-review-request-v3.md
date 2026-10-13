# Independent review request: TOY1-CON003

Review the v3 draft against `reviews/gates/TOY1-CON002-independent-review-v2.json`, especially CON002-F01.

Please determine whether:

1. The monotonic saturating `loss_epoch` has race-safe producer update, read-only consumer observation, and safe session reset semantics, including concurrent losses and the point at which a changed epoch invalidates records/publication.
2. The independent receiver-side timeout is a checkable, enforceable bound against a 2^32-period alias, including when the detector task is unscheduled; assess whether its stated deadline (`< 2^32-1` acquisition periods without successful handoff) and failure behavior are unambiguous.
3. The additional epoch/watchdog state is fully accounted to the existing shared-memory ceiling and remains within the approved envelope without silently changing it.
4. CON002-F02 remains closed at contract level while VO-002 physical layout evidence remains open.

The timeout mechanism and target evidence are intentionally not claimed as already verified. If their enforceability cannot be established at contract level, return `REVISE` or `UNRESOLVED` and name the minimum required interface guarantee/evidence. Do not infer physical ADC, MCU, scheduler, or atomic-instruction properties. VO-002 through VO-006 remain open; AD-003 remains accepted. No DE refinement or firmware implementation is authorized by this request.
