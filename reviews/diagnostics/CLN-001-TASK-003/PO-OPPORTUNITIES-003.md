# CLN-001 proof opportunities 003

Classification: **DRAFT_OPPORTUNITIES_NOT_PROOFS**. All three propositions below are **UNPROVEN**. This is authorized cooperative pre-freeze diagnostic scouting, not independent proof, acceptance, architecture selection, implementation, measured target fit or formal cleanroom qualification. Directory separation does not establish runtime/filesystem isolation.

## Authority and observable contract

Source identifiers here resolve only to supplied files: S1 = `inputs/problem-origin.md` (BKP-NEED-001), S2 = `inputs/adc.md` (BKP-ADC-001), S3 = `inputs/target.md` (BKP-TARGET-001), D001 = `inputs/DECISION-001.yaml`, AS = `inputs/AS-REV-002.md`, TRACE = `inputs/DECISION-TRACE-002.md`, ACT = `inputs/AS-ACTIVATION-002.yaml`. Exact subsection/entry references below provide the clause trace; file hashes are in the companion briefing.

AS and TRACE retain draft-era pending-acceptance language. ACT `status`, `activation.approved_baseline` and `newly_authorized_exploration` subsequently establish the accepted synthetic AS and authorize draft opportunity discovery. This report relies on that additive record, without rewriting either earlier document or independently authenticating the review/disposition artifacts named by ACT. D001 requirements choices are granted constraints, not findings of feasibility.

Let D = {0,...,4095}. In each initialized/reset epoch, accepted samples are x_1,x_2,... in intended publisher order, with x_i in D. Define x_j = 0 for j <= 0 solely for pre-epoch absent history. The required logical observation on accepted event n >= 1 is exactly

\[
(n,E_n),\qquad E_n=\sum_{k=0}^{31}x_{n-k}^2.
\]

E_0 = 0 mathematically; its publication is optional. Initialization/reset starts with no accepted samples; reset discards all previous-epoch contributions and restarts the logical indexing relation. Only accepted events advance n. Invalid values outside D leave detector state and n unchanged and explicitly expose rejection or precondition violation; silently treating them as zero is forbidden. The reporting mechanism is unspecified. Here “state unchanged” refers to the detector state governed by the contract; an observable rejection is still required. No stored-counter format or API is prescribed. Sources: AS R1/R2/A1, “Lifecycle, outputs and exceptional inputs” and PS; D001 `requirements.R1`, `requirements.R2`, `assumptions.A1`, `interface_and_lifecycle_Q4`, `delivery_and_exceptions_Q6`.

Publisher ownership of timing and intended ordered delivery without omissions are adopted environmental assumptions, not established device behavior. Missing, duplicate and out-of-order delivery are outside the accepted contract. Detectable gaps/order faults must be reported; an interface without sequence identifiers need not detect invisible faults. Startup padding grants no operational loss-padding policy. Nominal 1 ms arrival cadence imposes no hard execution deadline, jitter bound or wall-clock output schedule. Sources: AS R3/A2 and lifecycle clauses; D001 `requirements.R3`, `assumptions.A2`, `delivery_and_exceptions_Q6`; TRACE Q2/Q6.

D001 `requirements.R5`/`assumptions.A4` impose RAM <= 2048 bytes, counting owned persistent state, scratch and detector-owned call stack, excluding memory exclusively owned upstream. D001 `requirements.R6` prohibits floating-point hardware dependence, without selecting arithmetic or banning software floating point. S2/S3 and D001 A1–A3 are synthetic domain/cadence/generic MCU assumptions. None guarantees hardware operation, memory fit, speed or power. No quantitative compute/power optimization target is approved. Exact output, RAM ceiling and no FPU hardware dependency are requirements; the opportunities below are speculative mathematical tools for later comparison.

## PO-003-1 — Exact numeric envelope and conditional intermediate bounds

**UNPROVEN.** Domain/state: any valid epoch prefix, mathematical E_n above, incoming b = x_n and outgoing a = x_(n-32). All arithmetic in the proposition is over integers, not an implicit machine type. Let M = 4095^2 = 16,769,025.

**Candidate proposition with quantifiers.** For every accepted stream over D and every n >= 0,

\[
0\le E_n\le \min(n,32)M\le32M=536,608,800<2^{29}.
\]

The full-window upper bound is attained by 32 samples equal to 4095. For every n >= 1, the following candidate identity and bounds hold:

\[
E_n=E_{n-1}-a^2+b^2,\quad
0\le E_{n-1}-a^2\le31M,
\]
\[
0\le E_{n-1}+b^2\le33M=553,377,825<2^{30}.
\]

Thus the candidate value-width bounds are 24 unsigned bits for an individual square, 29 for energy and 30 for the addition-first intermediate; the displayed expressions would also fall within signed 32-bit value range. These are proposed mathematical bounds, not a prescription of evaluation order or representation.

**Assumptions.** Exact contract history, valid D inputs and correct identification of outgoing a, including startup zeros. An eventual finite-width realization must separately establish operand widths, multiplication semantics, promotions, signedness and evaluation behavior. A 32-bit MCU model alone does not establish those properties.

**Architectural value.** Could bound arithmetic realization risk and distinguish output width from transient width for multiple candidate realizations. It neither establishes RAM compliance nor chooses an update algorithm.

**Prospective proof strategy.** Independently bound each square and window sum; inspect extremal streams; derive the identity by aligning adjacent specification sums. Check each intermediate independently under its stated evaluation expression. Do not use the identity or containment bounds as already established lemmas.

**Attempted counterexample/adversarial case.** With a full all-4095 window and another 4095 input, a 29-bit addition-first temporary would encounter 33M even though the final result remains 32M. A narrower multiplication can fail before accumulation. At n = 33 an incorrectly selected outgoing value can violate exactness despite every value fitting. Reset followed by maximum input tests the assumption that a is an epoch-local startup zero. These challenge weakened hypotheses or realizations; they are not reported executed tests.

**Missing facts and independent evidence.** No concrete language/type model, outgoing-sample mechanism or compiler exists. A later independently checked integer derivation, explicit boundary cases n = 0,1,31,32,33 and a separate realization-level arithmetic analysis are needed. Any future proof would support, not discharge, TRACE T002-2/3/6; T002-4/5/7/8 remain open.

**Exact source trace.** AS R1/R2/A1 and PS; D001 `requirements.R1`, `requirements.R2`, `assumptions.A1`, `interface_and_lifecycle_Q4`; resource/dependency context D001 `requirements.R5`, `requirements.R6`, `assumptions.A3`, `assumptions.A4`; TRACE Q4/Q5 and T002-2/3/6. The numeric intermediate bounds are new conjectured consequences, not source requirements.

## PO-003-2 — Minimal information for future numeric outputs

**UNPROVEN.** This proposition isolates energy outputs after the current output has already been emitted; it excludes logical-index production, fault metadata and reset/reporting control. It compares histories at the same accepted length, so index differences cannot supply distinguishing information.

For any finite valid history h, define its padded ordered tail t(h) in D^31 as its latest 31 values, with leading pre-epoch zeros if needed. For a nonempty continuation u in D^+, let F_h(u) be the energy output on the last event of u after h. Define future numeric equivalence by

\[
h\sim g\quad\Longleftrightarrow\quad
\forall u\in D^+,\ F_h(u)=F_g(u).
\]

**Candidate proposition with quantifiers.** For all finite valid histories h,g,

\[
h\sim g\iff t(h)=t(g).
\]

Consequently, for a deterministic online machine whose future numeric outputs depend only on its retained state and subsequent input values, exactness for all streams requires at least 4096^31 = 2^372 distinguishable reachable states after a fixed length n >= 32. Conversely, t(h) is a sufficient mathematical summary for all future energy outputs. Its information payload is 372 bits, or 47 eight-bit octets when packed; that is not a RAM footprint or full-interface sufficiency claim.

**Assumptions.** Unrestricted valid continuations; deterministic retained state; no re-reading past publisher data, output log or external historical oracle. A past output available for future consultation counts as retained state/resources, rather than free evidence. No execution-time restriction is added. “State count” measures all retained information in this model, independent of encoding. Outputs for the already completed current event need not be regenerated. Reset and invalid events can be modeled separately as tail clearing and state stuttering, but their full interface obligations are excluded from the minimality claim.

**Architectural value.** Could establish an information lower bound and a sufficient abstract history summary without selecting storage layout or arithmetic. It could prevent treating current energy alone as sufficient, or incorrectly claiming that retaining all 32 past samples is information-theoretically necessary. It supplies no measured comparison or architecture preference.

**Prospective proof strategy.** For sufficiency, express every future window in terms of the tail and continuation. For necessity, study the sequence of future outputs under 31 zero inputs and whether successive differences recover each tail square; separately establish injectivity of squaring on D. Then apply distinguishability to histories with fixed n and independently variable tails. Each step requires proof; none is inherited as a lemma here.

**Attempted counterexample/adversarial case.** Histories (1,0) and (0,1) have identical current energy but yield different numeric outputs after 31 further zeros. Conversely, two length-32 histories differing only in their oldest value have different current energies but the same future numeric behavior. The latter challenges a 384-bit lower bound based on all 32 past samples. Allowing signed samples would challenge recovery from squares; D excludes that case. External replay of history would invalidate the retained-state model, so upstream ownership must be examined before applying this bound.

**Missing facts and independent evidence.** The architecture boundary has not fixed replay access, external retained outputs or actual encoding. Needed: an independently checked equivalence/distinguishability argument with startup cases, explicit state-model review and a later ownership/total-memory account. The 47-octet payload excludes working storage, control, index, alignment and stack. It proves neither an implementation nor <=2048-byte fit. Relevant open items are T002-2/3/6; full event association T002-4 and the other obligations remain separate.

**Exact source trace.** AS R1/R2, C publisher/subsystem boundary and PS; D001 `requirements.R1`, `requirements.R2`, `interface_and_lifecycle_Q4`, `delivery_and_exceptions_Q6`, `requirements.R5`; TRACE Q4/Q5 and T002-2/3/6. Minimal-state cardinality and the restricted no-replay model are proposed analysis, not accepted requirements or a selected data structure.

## PO-003-3 — Finite retained state versus an unbounded exact logical index

**UNPROVEN.** This is conditional impossibility under an explicit interface model, not a finding that the accepted AS is inconsistent.

**Defined model and proposition.** Let Q be any finite set of retained machine states, q_0 its reset state, delta: Q x D -> Q its deterministic accepted-input transition, and lambda: Q x D -> (N_(>=1) x N) its deterministic emitted pair. Assume all information affecting the next pair is included in Q and the current input value. For every such machine, there exists n >= 1 such that its nth output on the infinite all-zero stream differs from (n,0). Equivalently, no such finite-state machine supplies the required exact index for every n in an unbounded epoch.

**Assumptions.** Unlimited accepted epoch length; exact unbounded natural-number index is required in the emitted pair; no supplied index, clock oracle, external growing log, hidden mutable state or externally retained counter; output is computed only from the stated arguments. A finite RAM budget implies finite state only if every other retained information source is also fixed and finite. AS PS explicitly does not prescribe a stored counter; this closed-machine model is an additional analytical hypothesis, not an AS amendment.

**Architectural value.** Could identify whether logical association is supplied by the surrounding interface or requires a bounded-lifetime/index representation decision before later architecture comparison. It prevents conflating a small energy-history summary with sufficiency for the complete indexed contract. No lifetime limit, wrap rule, external index mechanism or API is selected here.

**Prospective proof strategy.** Analyze repeated states along zero-input execution and their deterministic emitted indices; use finite-state repetition against strict index growth. Independently check whether a proposed concrete interface actually meets the closed-machine hypotheses before applying the result.

**Attempted counterexample/adversarial case.** A 32-bit counter might appear adequate on short streams, but an unbounded epoch eventually requires an index beyond its representation. A publisher-supplied arbitrary index or an external growing log defeats the closed-machine argument, rather than refuting the stated proposition. Reset can restart an epoch but is not mandated to occur within a finite number of accepted samples. Nominal 1 ms arrivals do not bound lifetime.

**Missing facts and independent evidence.** Maximum epoch length, index encoding/association mechanism, permitted external information and associated ownership accounting are unspecified. Needed: independent finite-state impossibility proof and a separate contract/interface interpretation review. Any proposed finite lifetime or wrap policy would require later authorized clarification, not insertion by this report. This opportunity does not resolve T002-4 or T002-6, and grants no permission to change D001/AS.

**Exact source trace.** AS PS one-based logical relation and non-prescription of stored counter; AS R3/R5 and lifecycle clauses; D001 `interface_and_lifecycle_Q4.output`, `.reset`, `requirements.R3`, `requirements.R5`; TRACE Q2/Q4/Q5 and T002-4/6. ACT `scope_exclusions` prohibits treating this as architecture approval.

## Obligations and evidence classification

All displayed new propositions, width implications, equivalence/cardinality statements and impossibility statements are unproven draft opportunities. Source hash consistency is provenance evidence only. No tests, independent proofs, hardware measurements, RAM accounting, algorithm selection or implementation are supplied.

ACT `open_obligations` leaves **T002-2 through T002-8 ALL_OPEN**: numeric exactness; startup/reset; logical event/output association; invalid-input and applicable fault reporting; RAM/no FPU dependency; performance/target qualification; full detection. TRACE T002-1 describes the historical revision gate; ACT records its later activation, without independently authenticating review separation here. R4 remains **UNRESOLVED_BEFORE_COMPLETE_DETECTOR_CLAIM**: threshold, duration, boolean decision and integration verification are deferred. Even future proofs of all three candidates would not establish whole-detector functionality, actual target feasibility or discharge these verification obligations.
