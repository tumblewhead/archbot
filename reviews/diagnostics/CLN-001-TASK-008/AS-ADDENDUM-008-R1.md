# CLN-001 proposed AS addendum 008-R1: index supply and event lifecycle

**State:** PROPOSED, NOT ACTIVE. Additive clarification of accepted
`AS-REV-002` as activated by `AS-ACTIVATION-002`, submitted for a
**distinct independent source/authority review**. This is not a replacement
AS and does not amend D001 or activate D003-P1. Its author is the
CLN-001-only delegated engineering decision maker, not the reviewer.

## Authority and purpose

Read together with D001 `DECISION-001.yaml`, accepted `AS-REV-002.md`,
`AS-ACTIVATION-002.yaml`, accepted D002, reviewed D003 proposal,
the independent `REVIEW-D003-007`, and the guarded delegated
`D003-DISPOSITION-007.yaml`. All three original BKP files are synthetic.
The independent Stage-7 review returned
`READY_FOR_DELEGATED_D003_DISPOSITION` at **proposal-review scope only**.
The delegate issued a bounded disposition for an AS clarification,
not an operative index service or an AP selection.

## Additive C: consumer and event interface boundaries

A physical *consumer* is the component that must obtain the logical
`(n,E_n)` association for each accepted input event. Distinguish the
producer's acquisitions, the detector's accepted sample sequence, the
numeric state, pending result obligations, and the consumer's actually
available sequence/reset information. A mathematically reconstructible
index available only to an omniscient trace observer does not satisfy
the consumer's output contract.

A valid input presented to an acquisition interface need not be called
accepted until the proposed physical acceptance event is defined and
reviewed. That boundary cannot be chosen retrospectively to excuse
already accepted events, lost data or unsupported buffering. D001's
assumption of intended ordered omission-free publisher delivery remains
in force. No additional publisher suspension, backpressure, history
service, retry mechanism, crash model or lossless storage is assumed.

## Additive R: output index, delivery and reset interpretation

**A008-R1, proposed exact index representation.** The required logical
observable remains exactly `(n,E_n)`, with one-based `n` counting
**accepted valid** events since explicit initialization/reset.
An implementation need not transmit a literal numeral if and only if a
fully defined concrete interface makes the **actual consuming component**
uniquely determine the exact `n` for every accepted event from
information it actually possesses, throughout the contract's supported
sequence/reset/restart lifetime. Such a refinement needs an explicit
decoder, accepted-event/result bijection, consumer reset association,
unrestricted-rank argument, and independently reviewed evidence.
A response attached to a fresh transaction alone is insufficient when
the consumer cannot know the transaction's accepted rank. This clause
does not claim any particular RI design has met those conditions.

**A008-R2, proposed accepted-result debt.** For every accepted valid
event, exactly one correctly associated energy result is owed. Numeric
state commitment and result delivery are not interchangeable. A fault
report, delivery stall, consumer restart, or later explicit reset does
not retrospectively discharge an owed accepted-event result. Invalid
input must be rejected or explicitly violate its precondition without
advancing accepted history, index, or pending association; invalid
attempt count is not accepted ordinal. No new deadline or universal
fault recovery is implied.

**A008-R3, proposed reset framing.** Explicit reset begins a new
zero-padded numeric history and new one-based accepted rank. Old
accepted-event output obligations remain distinguishable from new ones.
The eventual physical contract must establish consumer-visible reset
ordering and unambiguous association between old and new sequences,
and prove that old in-flight outputs cannot alias new ones. A distinct
acknowledgment event is optional, not required; any chosen mechanism
must establish the required observable ordering and association. Draining prior outputs or preserving
old-sequence identity are alternatives for later review, not
selected mechanisms. Consumer restart alone does not reset the
detector. Wrapping finite generation tags alone cannot prove
unrestricted safe non-aliasing.

## Additive PS: unchanged numeric relation

For valid accepted stream `x_1,x_2,...` in a single explicit
initialization/reset sequence, with conceptual zeros only at `j<=0`,
retain exactly

`E_n = sum_{k=0}^{31} x_{n-k}^2`, paired with the exact logical
accepted-event rank `n>=1`.

No new index field, finite epoch limit, required periodic reset,
rejection of otherwise-valid events, loss padding, fixed deadline
or forced backpressure is introduced. An all-zero history before
consumer restart cannot distinguish rank 1 from rank 2 absent
retained association. A delayed old `(1,1)` after reset cannot be
mistaken for a new `(1,4)`.

## Open feasibility and authority conditions

The addendum specifies **required observable semantics**, not a
completed protocol. Whether they are realizable on the hypothetical
finite embedded platform remains UNKNOWN. Independent review must
determine whether A008-R1..R3 faithfully clarify accepted D001/AS
or introduce a material requirement change needing a further
sponsor-delegate decision before activation.

In particular, arbitrary accepted histories plus indefinite stalls
and finite queues expose an unresolved liveness/capacity interface
question. That question must not be "solved" by treating a fault
report as delivery, silently rejecting valid events, or postulating
an unapproved service. A fully specified acceptance/delivery contract
and independent feasibility evidence remain due later.

RN external exact numeral provider and C-HIST publisher snapshot
service are unapproved, unmeasured candidate dependencies. For each,
provider, accepted-event binding, consistency, retention, reset
fencing, availability, error semantics and attributable resources
must be reviewed before reliance. D002's ownership disclosure and
the accepted RAM boundary remain unchanged.

All H1–H6 realized gates and active F measurements
(`RAM_peak`, `compute_effort`, `device_energy_consumption`)
remain UNKNOWN for AP-006-A/B/C. T1 covers future numeric
continuations only; T2's 372-bit/47-octet conditional capacity
minimum is not a sufficient target allocation or local RAM bound
for externally replayed history. T002-2 through T002-8 stay OPEN,
R4 complete detection stays DEFERRED, PO-003-1/3 unproven.

**Activation condition:** independent review of this exact addendum,
followed by a separate explicit delegated AS-addendum disposition.
No addendum or D003 interpretation is made effective merely by
authoring this file. No AP, contract, implementation, product,
target or formal cleanroom is accepted.
