# CLN-001 Stage 8 briefing: the interface is part of the proof boundary

**Decision:** A bounded D003 disposition was issued after the
independent Stage-7 review, but the logical-index interpretation and
reset/publication interface are not active. The follow-on
`AS-ADDENDUM-008.md` is a **proposal awaiting independent review**.

## What we have learned

A local numerical recurrence can be exact while the full subsystem
fails to supply the right `(n,E_n)` to the consumer. A transaction
handle and a mathematical event rank are insufficient if the consumer
cannot reconstruct the accepted ordinal across reset and restart.
Likewise a reset that correctly clears the 31-sample numerical tail
can still corrupt the interface if an old `(1,E)` is delivered as
the new sequence's first result. Accepted history and owed output
history have separate lifetimes.

## Review targets and falsifiers

- **Index:** two possible zero-input traces produce the same visible
  energy after a consumer restart but require different indices.
  Require evidence of real consumer-visible distinction.
- **Acceptance:** committing accepted sample 1 then losing its output
  leaves an owed result; a fault report and replay-as-new-input are
  not substitutes for correct delivery.
- **Reset:** delayed old and new results can both have ordinal 1.
  Require reset/association guarantees without inventing infinite
  generation tags, finite epochs or mandatory resets.
- **Resources:** Q+1 outstanding results exceed a Q-entry queue if
  there is no other retention, service or acceptance coordination.
  Source-owned snapshot memory is not zero device energy or proof
  of ownership.
- **Authority:** test whether this is a faithful additive AS
  interpretation, or an additional obligation/relaxation requiring
  a revised delegate decision.

The target remains an exact latest-32 sum-of-squares energy primitive
on a hypothetical 32-bit no-FPU platform under 2048 detector-owned
bytes, not a complete sustained-energy detector.

## Next gate

Run a fresh, independent **AS addendum source/authority review**
against pinned synthetic BKP, D001, activated AS, D002, reviewed
D003 and its scoped disposition. The reviewer cannot activate the
addendum or select an AP.

After actual review evidence is pushed, the delegate will decide
activation/revision. Only then commission an independently authorized
stage-appropriate AP feasibility evaluation of A/B/C, preserving
the accepted three-axis F and all open obligations.
