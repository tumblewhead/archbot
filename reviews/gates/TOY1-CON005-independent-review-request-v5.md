# Independent review request: TOY1-CON005 minimal CON v5

Review additive drafts `CON-AP2-001-v5` through `CON-AP2-003-v5`, their
relationship spine, coverage matrix, and five DE placeholders against active
AS-v2, VP-v3, AP-002 authority, C-002-SCOPE-001, PR-002, and active VO ledger.

Please determine whether the externally observable sample/result semantics
are sufficient and consistent; verify exact newest-32/zero-padding and
arithmetic/C-expression obligations; confirm publisher continuity remains an
external unverified assumption; and check that no fixed cadence, detector
loss protocol, watchdog, topology, or reader atomicity guarantee was
reintroduced. Check resource attribution against the binding 2,048-byte
scope and whether its intentionally unresolved numeric allocation is
properly bounded for this gate. Confirm VO-002..VO-006 and AD-003 remain in
their authoritative states.

The drafts intentionally leave invalid-input reporting, reset concurrency,
result representation/readers, integration owner, numeric resource
allocation, and target implementation evidence unresolved. Decide whether
any is a contract semantic blocker before DE refinement. This request seeks
independent review only; it authorizes no acceptance, VO discharge, authority
change, or implementation.
