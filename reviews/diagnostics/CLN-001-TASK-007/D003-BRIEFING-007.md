# CLN-001 Stage 7: D003 proposal and engineering briefing

**Status:** Source-grounded *proposal*, not accepted D003, amended AS,
selected AP or authorization to implement.

The independent Stage-6 AP review archived at commit
`45d85dad82aaf3b1a74b856138d4bc0ccd8e4b47` returned
`READY_FOR_INDEPENDENT_AP_EVALUATION` for draft/source quality only.
No written conditional proposal contradicted an accepted hard gate;
all realized H1–H6, target RAM, compute and device electrical energy
remain UNKNOWN. Original review evidence is preserved unmodified.

## New understanding

An index can be carried as a numeral or recoverable from a uniquely
associated accepted transaction. These are not automatically equivalent
to a *physical consumer*. A mathematical observer can number all
accepted events in a trace, while a restarted consumer observing only
zero energies cannot know the correct rank. D003-P1 proposes eligibility
of exact request/response association only under proven consumer-visible
sequence identity. The independent reviewer must decide if that reading
is faithful to the accepted AS or needs additive AS authority.

Acceptance, history commit, output publication and reset are distinct.
A response owed for an accepted event cannot disappear merely because
the service stalls or reset occurs. No queue, backpressure, crash model
or reset synchronization has been approved; these remain explicit
contract questions, not invented mechanisms.

The B candidate exchanges repeated arithmetic for a coupled
sum/cursor-age invariant, so checking the aggregate against stored
values does not detect all chronological errors. C relocates retained
history and snapshot/index costs across a boundary; external state
is not free. The reviewer demonstrated concrete A early-eviction,
B wrong-age and C mixed-snapshot failure cases. These guide the
later feasibility evaluation but do not invalidate the written
conditional AP drafts.

## Decision sequence and stop rule

Independent review D003-P1..P5 against accepted D001, AS, D002
and REVIEW-AP-006. Only a favorable source review allows a separate
delegated D003 disposition with explicit AS-impact judgment. Then
commission stage-appropriate AP feasibility evaluation of A/B/C
under compatible Figure-of-Merit scopes. Any future AP selection
requires additional evidence and separate authority.

**Preserve:** T002-2..8 OPEN; deferred R4; no finite wrap/epoch,
mandatory reset, dropped valid events, invented 1 ms deadline,
unsupplied history/index service, 47-byte implementation claim or
product/cleanroom qualification.
