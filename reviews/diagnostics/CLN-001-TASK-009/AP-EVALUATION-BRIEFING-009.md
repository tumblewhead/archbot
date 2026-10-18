# CLN-001 engineering briefing 009

The independent models support all three candidates' **conditional numeric kernels**. They do not establish a complete physical interface or a target implementation. Every realized H1–H6 gate and every realized Figure-of-Merit value remains **UNKNOWN**. A, B and C remain unselected.

The [full evaluation](AP-EVALUATION-009.md) separates candidate dossiers, interface dependencies, resource expressions and next experiments. The [receipt](AP-EVALUATION-009.json) preserves exact source hashes, executed programs, seeds, counts, witnesses and structured findings.

## What changed

The original [AS](../inputs/AS-REV-002.md) remains active through its [activation](../inputs/AS-ACTIVATION-002.yaml). The separately reviewed [R1 clarification](../inputs/AS-ADDENDUM-008-R1.md) is now active through a separate [disposition](../inputs/AS-ADDENDUM-008-R1-DISPOSITION.yaml). Older draft/proposed labels remain preserved in the source documents; they do not override those activation records.

R1 clarifies three observables. The actual consumer must decode exact accepted-event rank from information it possesses. Every accepted valid event continues to owe a correctly associated result through stalls, faults, restart and reset. Reset begins new numeric history and rank while keeping old work distinguishable. A distinct acknowledgment is optional; consumer-visible reset ordering and correct association are required.

This resolves the source-level interpretation question without supplying RI, RN, a history service, a retry protocol or a queue/flow-control guarantee. The focused [R1 review](../inputs/REVIEW-AS-ADDENDUM-008-R1.md) was source review; the later disposition activates its clarification. Neither makes a physical service available. No finite epoch, mandatory reset, valid-event loss or hard 1 ms deadline has been added.

## What the independent runs establish

An exact oracle retained the full accepted stream and summed its latest 32 squares. A separate model retained raw31 for A; B retained ordered square31 plus S and an oldest-first cursor. C was tested with an **assumed immutable correct-event pre-tail service**. That service was supplied by the experiment, not found in the evidence.

The completed run compared 299,296 accepted transitions, producing 897,888 candidate-to-oracle energy comparisons with no mismatch. It exercised 24,192 explicit invalid rejections and 11,386 resets, exhaustive length-8 startup streams, random seeds 9009 and 9010, every pre-reset cursor, boundary positions 1/31/32/33 and a 32,768-event uninterrupted stream containing every domain value eight times. Exact program text and limits are in the receipt. Rejection checks cover the modeled state, not an actual API or unsupplied consumer association.

A separate suite contains 21 witness groups: 20 expose shortcut failures and one confirms that permuting the correct term set leaves a current sum unchanged. Eight observer-ledger reset/publication schedules show six failures each for clearing pending results at reset or relabeling old results with the current sequence. A live-tail read/append experiment produces wrong energy at 31 of 32 cut points. These are finite counterexamples to particular shortcuts, not physical protocol tests or all-architecture impossibility proofs.

One exploratory cursor witness initially failed to distinguish correct and faulty outputs: both were zero. Replacing its single impulse with two different values exposed the fault. The corrected completed run supplies the reported counts; the receipt records the correction without pooling preliminary execution.

Python exact integers do not verify compiler widths, interruption safety, dependency builds, RAM/stack, timing or electrical device energy. None of the open T002 obligations is discharged.

## Information, interface and ownership have different lifetimes

The three [candidates](../inputs/AP-CANDIDATES-006.md) preserve the same future numeric distinctions in different ways:

| Candidate | Conditional numeric state | Main unresolved dependency |
| --- | --- | --- |
| A | Ordered raw31; recompute with current sample | Actual RI consumer, exact accepted-rank decoder and no-loss lifecycle. |
| B | Ordered square31 plus redundant S | Same RI dependencies, plus coherent tail/S/cursor commitment. |
| C | No detector-owned retained tail only if an upstream service supplies it | Authorized correct-event snapshot and RN accepted-ordinal services, retention and ownership. |

Future numeric state, old unpaid output and consumer identity are different information. After either 1 or 2 followed by 32 zeros, current energy and tails agree, but the first owed result differs. Keeping the latest tail therefore does not preserve arbitrary old output debt. The accepted [T1/T2 mathematics](../inputs/PROOF-DISPOSITION-004.yaml) addresses future numeric behavior at stated boundaries, not complete interface state.

A request handle can identify a transaction without revealing its accepted rank. A restarted energy-only consumer sees the same zero whether the required result is (1,0) or (2,0). Without retained association, that narrow boundary cannot decode both. This falsifies that information-starved interface; it does not prove every RI refinement impossible. No actual consumer or decoder is supplied for A/B.

C's snapshot can be coherent yet belong to the wrong event. With prior tail (1,0,...,0) and current 2, the correct sum is 5; a coherent post-append snapshot gives 8 and a mixed read can give 9. Range validation does not establish event identity. A separate numerical check cannot manufacture a truthful provider.

B's current sum can be correct while its cursor evicts the wrong age. Even S=sum(stored slots) can remain true. The next result then fails. Tests must establish chronological expiry and future outputs, as well as aggregate consistency.

Reset discards numeric history for new work, not old result obligations. Old and new results can even share both rank and energy. Consumer restart alone does not reset the detector. Finite generation tags need evidence that old work is retired before reuse; field width alone cannot guarantee it. Draining is an unselected possibility whose completion under stalls is unknown.

A Q-entry queue alone cannot retain Q+1 debts under the explicit assumption of no other store, replay, compression or acceptance coordination. This does not authorize publisher pause, dropped valid events or retrospective unacceptance. Those remain contract and, where behavior changes, authority questions.

## What can be compared economically

The accepted [F disposition](../inputs/F-DISPOSITION-003.yaml) keeps three axes: detector-attributable peak RAM, compute effort and device electrical energy. The [comparison worksheet](../inputs/AP-COMPARISON-006.md) supplies symbolic accounting, not measured costs.

A conditionally has 31 raw slots; B has 31 square slots plus S; C has no detector-owned retained numeric tail only under its proposed service boundary. Every design additionally needs all owned persistent state, scratch, stack/callees, buffers, queues, index/reset/transaction state and attributable shared resources. Pending work, exact numerals and concurrent snapshot retention can grow. Unknown ownership is not zero.

T2's 372 information bits / 47 whole octets is a conditional complete-state capacity minimum, not a sufficient 47-byte SRAM implementation or a local bound for replay-open C. Moving history outside the detector does not remove it from the joint system.

Under a common serial integer kernel model, A/C perform 32 squares and 31 additions; B performs one square, one addition and one subtraction. Wider memory traffic, aggregate updates, actual index association, coordination, snapshots and pending work remain additional. Fewer squares alone proves neither complete compute dominance nor lower device energy.

Electrical energy is distinct from signal sum-of-squares energy. No device cost coefficients, target cycles, joules or numerical power targets were invented. If an upstream service runs on the same device, its attributable electrical consumption cannot be excluded merely because its RAM is outside the detector ownership boundary. Detector-only, whole-device and external-service scopes must be reconciled before comparisons. There is no evidence-compatible full Pareto ordering or downselection.

## Next independently reviewable step

The immediate gate is a **distinct Stage-10 independent review of these exact three evaluation artifacts**, including reproduction of the receipt programs and assessment of the falsifiers' stated boundaries. This evaluation accepts no contract/AD and authorizes no implementation or AP commitment.

After that review and separate authorization, the most economical new evidence is an actual consumer information/lifecycle inventory for all candidates and a C provider/capability/ownership inquiry. Require explicit proposals and evidence for decoding, acceptance/commit/publication, reset/restart, retained debt, retry identity and resource lifetimes. Challenge zero-prefix ambiguity, wrong-event snapshots, stale old results, tag reuse and queue saturation before undertaking target measurements. These are ordered evidence tasks, not a ranking of candidates.

A later authorized realization can then be checked with chosen-width arithmetic, lifecycle interference and complete allocation/stack/dependency evidence. Comparable target timing and electrical measurements need a concrete build, workload, attribution and equivalent pending work. The [T002 trace](../inputs/DECISION-TRACE-002.md) remains open for T002-2..8; R4 threshold/duration/boolean detection remains deferred before any whole-detector claim.

All 21 current payload digests match the supplied manifest. This establishes byte consistency, not historical provenance, review execution, external independence or OS/connector isolation. Only the supplied allowlisted evidence was used; no Git history, other workspace, network, connected app, hidden solution or subagent was accessed. No candidate was selected, no target/product/formal cleanroom qualification claimed, and no VO discharged.
