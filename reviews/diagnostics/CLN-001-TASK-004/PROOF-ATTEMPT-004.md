# PROOF-ATTEMPT-004 — PO-003-2

Author's assessment: **CLAIMED_PROOF_PENDING_REVIEW**.

This is a Proof Engineer's mathematical argument for the exact numeric-only equivalence and conditional retained-state lower bound in TASK.md. No counterexample to those statements was found. This author cannot accept this proof. Independent proof acceptance, applicability to a realization, and product verification remain pending. PO-003-1 and PO-003-3 remain separate unproven opportunities in this package.

## 1. Authority, sources and scope

Only the supplied local input package and the current task/role instructions were used. The scout and opportunity review supply conjectures and challenges, not accepted lemmas. Every mathematical step used below is derived here from the specified energy relation.

Source names in this artifact resolve to these supplied files:

| Name | File and relevant clauses | Use |
| --- | --- | --- |
| S1 | `inputs/problem-origin.md`, stakeholder need | Original exact latest-32 energy and startup need |
| S2 | `inputs/adc.md`, ADC assumptions | Synthetic unsigned domain |
| S3 | `inputs/target.md`, target assumptions | Synthetic resource context, not a proof premise about actual hardware |
| D001 | `inputs/DECISION-001.yaml`, requirements.R1/R2/R3/R4/R5/R6, assumptions.A1, interface_and_lifecycle_Q4, delivery_and_exceptions_Q6 | Granted requirements, lifecycle and exceptional-input contract |
| AS | `inputs/AS-REV-002.md`, C, R1/R2/A1, lifecycle and PS | Exact observable relation |
| TRACE | `inputs/DECISION-TRACE-002.md`, Q2–Q6 and T002-2 through T002-8 | Open verification/integration obligations |
| ACT | `inputs/AS-ACTIVATION-002.yaml`, status, activation.approved_baseline, open_obligations, scope_exclusions | Supplied accepted synthetic baseline and scope limits |
| PO | `inputs/PO-OPPORTUNITIES-003.md`, PO-003-2 | Conjecture and explicit analytical no-replay model |
| PB | `inputs/PO-BRIEFING-003.md`, open questions and next proof task | Scope and applicability questions |
| REVIEW | `inputs/REVIEW-PO-003.md` and `.json`, PO-003-2 / PO-R3 / PO-R4 | Opportunity readiness only |

ACT records acceptance of the supplied AS bytes despite their earlier draft language. Its archival references and activation assertions are accepted as supplied diagnostic records, not independently authenticated here. This proof does not amend AS or D001. TASK.md separately authorizes this proof attempt; older stage-specific prohibitions on future proof do not constitute a new acceptance gate for this author.

## 2. Definitions and exact assumptions

**A1 — Domain and accepted epoch.** Let `D = {0,...,4095}`. An epoch begins at initialization or explicit detector reset and contains only the accepted samples since that boundary. Write a finite valid history as `h = (x_1,...,x_m) in D*`, allowing the empty history `epsilon` with `m=0`. Accepted order is the intended publisher order without omissions under the diagnostic contract. Repeated numeric values are permitted; they are not evidence of a duplicate delivery event.

**A2 — Padding and lifecycle.** For specification only put `x_j=0` for every `j<=0`. These are absent pre-epoch positions, not inserted accepted samples. Reset starts a fresh epoch with empty history and restarts indexing; no prior epoch contributes. Invalid values outside D are rejected or expose an explicit precondition violation: they do not alter detector state, append a zero, or advance the accepted index. Missing, duplicated or out-of-order delivery is outside the accepted input contract. Detectable gaps/order faults must be reported; no recovery or operational zero-fill policy is assumed.

**A3 — Exact observation.** At accepted event `n>=1`, AS requires `(n,E_n)` where

`E_n = sum(x_(n-k)^2, k=0,...,31)`.

All arithmetic here is exact integer arithmetic. `E_0=0` mathematically, but publication before the first accepted sample is optional. No machine integer width, overflow behavior, deadline, execution-time bound, or implementation is assumed. Nominal 1 ms arrivals do not restrict the histories below.

**D1 — Tail.** Define `t(h)=(t_1,...,t_31)` by

`t_i = x_(m-31+i), 1<=i<=31`.

The order is oldest to newest: `t_1=x_(m-30)` and `t_31=x_m`, using padding for indices at most zero. Equivalently this is the last 31 entries of 31 zeros followed by h. Thus `t(epsilon)=0^31`. This definition also applies when `m<31`.

**D2 — Continuation and observation.** A continuation is any nonempty finite tuple `u=(u_1,...,u_r) in D+`, with `r>=1`, appended in the same epoch with no reset or invalid event. Let z be the concatenation `hu`, padded before its epoch. Define

`F_h(u) = sum(z_(m+r-k)^2, k=0,...,31)`.

This is the numeric energy at the last accepted event of u. Its associated index is `m+r`, but that index is excluded from F. No already-emitted current output is included, and `F_h(epsilon)` is undefined. The quantifier includes all lengths and all values in D; there is no bounded remaining lifetime or restriction to a particular future stream.

**D3 — Semantic state equivalence.** Define

`h ~ g iff for every u in D+, F_h(u)=F_g(u)`.

This is an equivalence relation: equality of the associated functions is reflexive, symmetric and transitive. Although each F observes only the last output, its quantification covers every future per-event energy, since each nonempty prefix of a continuation is itself an allowed continuation. This equivalence is defined on histories of arbitrary, possibly unequal lengths. Same-length histories will be used for the lower bound.

**A4 — Additional machine hypotheses for the conditional consequence only.** A fixed deterministic machine has a complete retained state q after processing each accepted event and emitting its current output, initial state `q_0`, transition `delta: Q x D -> Q`, and numeric output function `lambda: Q x D -> N`. For every valid stream it emits the specified energy at each accepted event. Its next state and output depend only on q and the next sample value. All retained output-affecting information must be included in q: memory, registers, control position, persistent counters, readable retained outputs and any other history-dependent data. Fixed history-independent program constants are allowed.

There is no access to excluded old publisher histories, output logs, external historical oracle, hidden mutable storage or other information source. Retaining historical data inside q counts its distinguishable configurations; it is not free replay. A previously emitted output that is available for later consultation must be counted as retained information, rather than treated as a free external log. Write-only emitted outputs cannot influence later computation. Uncounted external readback violates A4. There is no execution-time restriction. The theorem does not require a particular encoding or data structure, or initially assume that Q is finite.

## 3. Theorems

**T1 — Future numeric equivalence, exactly as posed.** For all finite valid histories h and g,

`[for every nonempty u in D+, F_h(u)=F_g(u)] iff t(h)=t(g)`.

**T2 — Conditional retained-state consequence.** For any fixed accepted length `n>=32`, a machine satisfying A4 has at least

`|D|^31 = 4096^31 = 2^372`

distinct reachable complete retained states after length-n histories. This is at least 372 bits of distinguishability capacity in that model. If this information is held in a fixed store of whole eight-bit octets, its capacity requires at least 47 octets. These statements exclude any claim about the extra resources required for logical-index production, fault handling, working scratch, stack, alignment or actual implementation allocation. They are not evidence of <=2048-byte fit.

## 4. L1 — Every future window in terms of the tail

Fix arbitrary h of length m and u of length r. The last window has positions from `m+r-31` through `m+r`, inclusive: exactly 32 positions.

1. Suppose `1<=r<=31`. The part of this window at or before m is `x_(m+r-31),...,x_m`, with `32-r` entries, including any padded zeros. Under `t_i=x_(m-31+i)`, those positions correspond exactly to `i=r,...,31`.
2. The remaining r positions are exactly `u_1,...,u_r`. No preceding history position is in the last window.
3. Consequently,

   `F_h(u) = sum(t_i^2, i=r,...,31) + sum(u_k^2, k=1,...,r)`.  (W1)

4. At `r=1`, W1 uses all 31 tail entries plus `u_1`. The excluded 32nd-oldest historical position `x_(m-31)` is already outside the new window.
5. At `r=31`, W1 uses only `t_31=x_m` plus the 31 continuation values. It does not yet discard the newest historical value.
6. Suppose instead `r>=32`. The earliest position `m+r-31` is at least `m+1`, so the window lies wholly within u. Thus

   `F_h(u) = sum(u_k^2, k=r-31,...,r)`.  (W2)

7. In particular `r=32` uses `u_1,...,u_32`, with no historical term. Lengths above 32 merely select the last 32 continuation values.
8. For `m<31`, all nonpositive x positions in steps 1–3 are the very zeros used in D1. There is no separate fill flag or accepted-length term in W1. For `m=0`, W1 reduces to the sum of the r incoming squares; W2 handles a filled continuation window.

This derives W1/W2 directly from AS PS; no recurrence or range result from PO-003-1 is used.

## 5. Proof of T1, sufficiency

1. Assume `t(h)=t(g)` and choose any nonempty u of length r.
2. If `1<=r<=31`, W1 has equal tail terms for h and g and the identical continuation terms. Hence `F_h(u)=F_g(u)`.
3. If `r>=32`, W2 is independent of either history, so the same equality holds.
4. The two cases exhaust all allowed r and explicitly include r=31 and r=32. L1 already includes empty and short startup histories.
5. Since u was arbitrary, `h~g`. No equality of history lengths or current energies was required.

Thus the ordered padded tail is a sufficient mathematical summary for future numeric outputs. This does not assert that an actual machine stores it in any particular form or that equality of tails forces equality of implementation states; a machine may retain redundant information.

## 6. L2 and proof of T1, necessity

**L2 — Injectivity of squaring on D.** If `a,b in D` and `a<b`, then

`b^2-a^2=(b-a)(b+a)>0`.

Here `b-a>0` and `b+a>0` because b is a positive integer and a is nonnegative. Therefore `a^2=b^2` implies `a=b` on D. No signed-domain injectivity is assumed.

Now assume `h~g`.

1. Zero belongs to D. For each `j=1,...,31`, the tuple `0^j` is an allowed nonempty continuation. Define `y_j(h)=F_h(0^j)` and likewise for g.
2. Applying W1 with r=j and zero continuation terms gives

   `y_j(h)=sum(t_i(h)^2, i=j,...,31)`.  (Z)

3. From equivalence, `y_j(h)=y_j(g)` for every one of these 31 observations.
4. For `j=1,...,30`, subtract the instance of Z at j+1 from the instance at j. Cancellation yields

   `y_j(h)-y_(j+1)(h)=t_j(h)^2`.

   The same calculation for g and step 3 imply `t_j(h)^2=t_j(g)^2` for each j in this range.
5. At j=31, Z is simply `y_31(h)=t_31(h)^2`. Step 3 therefore also gives `t_31(h)^2=t_31(g)^2`.
6. All tail entries lie in D, including startup padding. L2 converts equality of each square to equality of its value. Hence `t(h)=t(g)`.

This proves necessity and completes T1. Recovery uses only future observations at lengths 1 through 31, with no current output and no empty continuation. At length 1, the whole 31-tail contributes; the difference of lengths 1 and 2 isolates its oldest entry. At length 31, the newest entry is isolated directly. At length 32 every old entry is gone, so an additional zero observation would be zero and is unnecessary. The y values can also be read as the successive outputs on one path of 31 zeros, without resetting that path.

In particular, if two tails differ, at least one zero continuation of length at most 31 distinguishes their energies: otherwise all y values would coincide and the recovery above would make their tails equal.

## 7. L3/L4 and proof of T2

**L3 — Fixed-length reachability.** Fix an arbitrary integer `n>=32`. For each `a=(a_1,...,a_31) in D^31`, choose

`h_a = 0^(n-31) a_1 ... a_31`.

This has exactly n accepted valid values, requires no reset or invalid event, and has `t(h_a)=a`. The zero prefix has length at least one. Nothing in the accepted input contract restricts these independent sample choices. All these histories have the identical current logical index n.

**L4 — Equal complete machine states have equal future numeric outputs.** Suppose `q(h)=q(g)` in a machine satisfying A4. For any common input value b, lambda gives the same emitted energy and delta gives the same next state. Induct on the length of a common finite continuation: equality persists after each prefix and each emitted energy is equal. Hence `F_h(u)=F_g(u)` for every nonempty u, by required exactness. This induction uses complete information in q and the current value; it would not follow for a state that omits a readable external source.

Now apply these lemmas:

1. If `a!=b`, T1 or its zero-continuation consequence shows `h_a` and `h_b` are distinguishable by some common continuation of length at most 31.
2. If `q(h_a)=q(h_b)`, L4 would force equality on that continuation, a contradiction. Therefore the mapping `a -> q(h_a)` is injective.
3. All images are reachable after exactly n accepted events by L3, so `|Q_n| >= |D^31|`, where `Q_n={q(h):h in D^n}`.
4. Every chosen history has index n, and along any common length-j continuation the required indices are both n+j. The distinction is in numeric energy, not an unequal index or time since initialization. Even a common known fixed n cannot supply the missing tail information.
5. Since `|D|=4096=2^12`, the bound is `(2^12)^31=2^372` states.
6. A complete binary encoding with capacity b bits has at most `2^b` configurations, so `2^b>=2^372` implies `b>=372`. This is a capacity statement, not a Shannon average under an assumed input distribution. Encoding length, location and control data cannot be free extra information.
7. A store of B whole eight-bit octets has at most `2^(8B)` configurations, so `B>=ceil(372/8)=47`. Forty-six octets offer only 368 bits. The 47-octet number is a lower bound on information capacity, not a sufficient implementation allocation or a proposed RAM layout.

T2 follows. Separately, T1 and L3 show exactly `2^372` semantic future-numeric equivalence classes at fixed n, even though an implementation may have more states. No claim that all 32 prior samples are information-theoretically necessary follows. No index-bit overhead is added to 372 here without a separate model and argument.

## 8. Counterexample challenges and bounded corrections

The examples below are exact mathematical evaluations. A limited executable supplement is recorded separately; it does not test every example or prove their universal assertions.

### 8.1 Same current energy is insufficient

Take `h=(1,0)` and `g=(0,1)`. Both have length 2, current energy 1 and current index 2. With `u=0^31`, the final window contains only the last original value and the 31 zeros. Thus `F_h(u)=0` and `F_g(u)=1`.

This refutes the weakened claim that current energy alone determines all future numeric outputs. It does not refute T1 because the tails differ. The shortest nonempty histories of equal length with equal squares already have equal tails on D, so length 2 is minimal for this equal-length counterexample. If desired at length 32, prefix both histories with 30 zeros.

### 8.2 The oldest of the previous 32 need not affect any future output

Take length-32 histories `h=(1,0^31)` and `g=0^32`. Their current energies are 1 and 0, respectively, but both 31-tails are zero. W1/W2 show equality for every nonempty continuation, not just zero inputs.

This refutes extending T1 to include the current output while retaining only 31-tail equality. It also defeats a purported 384-bit necessity argument based solely on all 32 prior sample values: that argument would distinguish this pair without any future numeric observation doing so.

If a different observation definition includes the empty continuation as the current mathematical energy, the corrected equivalence is equality of padded 32-tails on D. To see the correction, empty plus nonempty equality gives equal current energy and, by T1, equal 31-tails. Subtracting the shared 31-tail square sum from current energy recovers the remaining oldest square; L2 recovers its value. Conversely equal padded 32-tails give equal current energy and equal 31-tails. This is a scoped mathematical variant, not a change to authority or to T1.

### 8.3 All recovery positions and the 31/32 boundary matter

Let `h=(0,1,0^30)` and `g=0^32`. The sole differing tail entry is its oldest, `t_1`. Then `F_h(0)=1`, `F_g(0)=0`, but every zero continuation of length 2 through 31 gives zero for both. Omitting the length-1 observation loses this entry.

For the newest entry, use `h=(0^31,1)` and `g=0^32`. At length 31 the zero-continuation outputs are 1 and 0; at length 32 both are zero. Thus discarding all old contributions already at length 31 would be an off-by-one error. The recovery must include the oldest tail square as well as the newest.

### 8.4 Signed samples break value recovery

In a hypothetical changed domain containing both -1 and 1, the one-sample histories `(1)` and `(-1)` have different tails but identical square contributions in every future window, and so have equal future numeric outputs. One sample is enough. The negative history is invalid under A1, so it is not a counterexample to T1.

For such a signed-domain variant with zero permitted, the corrected statement is equality of the ordered padded tail of squares, rather than equality of values. W1/W2 prove sufficiency and Z recovers the individual squares without L2. No signed-domain correction is inserted into the accepted unsigned model.

### 8.5 Startup padding merges numeric futures without merging indices

The histories `epsilon` and `(0)` have the same zero tail and identical future numeric outputs for every continuation. For the next accepted value b, however, their required pairs are `(1,b^2)` and `(2,b^2)`. Tail equality does not imply full indexed-interface equivalence across arbitrary accepted lengths. No numeric fill flag is needed to distinguish absent startup zeros from accepted zero values; logical association remains separate.

The argument also covers histories of lengths 1, 30, 31, 32 and 33 without changing definitions. At length 31 the tail has no absent entries; at lengths 32 and 33 it still retains exactly the latest 31. The full-interface index and any lifecycle metadata are not encoded by this observation equivalence.

### 8.6 Reset and invalid input are not additional accepted samples

After a history `(4095)`, explicit reset followed by accepted value 1 starts a new epoch and requires `(1,1)`. Including the old square would violate R2. The proofs apply anew to the empty history after reset; they do not equate different reset histories by retaining prior contributions.

After history `(1)`, reject an invalid value such as -1, then accept 31 zeros. The rejection leaves the accepted length at 1, so the last valid event has index 32 and energy 1. Silently converting that rejected event to an accepted zero instead would yield index 33 and energy 0 after the same 31 valid zeros. Such behavior violates the contract and is not a history allowed in T1. Reporting the invalid input is still required even though the detector state stutters.

Operational missing samples are not pre-initialization absent history. No assumption about detecting an invisible delivery fault, forcing a reset on a fault, or padding a loss with zero is introduced.

### 8.7 Replay and external output access change applicability

As a countermodel to an unconditional detector-RAM interpretation, suppose an upstream source retains the recent samples and allows the detector to reread them on each accepted event. Their distinguishing information then resides outside the detector's proposed local state. A detector-local-state-only application of L4 is invalid: equal local states can consult different upstream histories and emit different energies.

Similarly, readable prior output logs or an external historical oracle are output-affecting retained information. Counting only the local cache while consulting these sources does not meet A4. Keeping a previous energy inside counted q is permitted, but that single value is insufficient by section 8.1. The proof does not assume every output log by itself is sufficient; it requires every source actually consulted to be accounted for.

AS R5 excludes memory owned exclusively by the upstream publisher from detector-attributable RAM. That ownership rule does not itself prohibit replay or make externally retained information part of local detector RAM. Thus A4 is an additional analytical hypothesis requiring later realization-specific scrutiny, not an accepted AS restriction. One may analyze an enlarged complete state including external sources, but its information lower bound would then concern that enlarged boundary, not automatically the detector's 2048-byte allocation.

## 9. Dependency graph and evidence classification

The proof dependencies are:

```text
AS PS + A1/A2/A3 + D1/D2
  -> L1 (W1/W2) -> T1 sufficiency
  -> L1 (zero continuations Z) + L2 (square injectivity)
       -> T1 necessity -> distinguishing zero continuation
A1 + unrestricted histories + fixed n>=32 -> L3 (reachability)
A4 determinism/completeness + exactness -> L4 (same state => same futures)
T1 distinction + L3 + L4 -> injective reachable states
  -> T2 cardinality -> binary capacity -> whole-octet lower bound
```

Neither PO-003-1 nor PO-003-3 is a dependency. Source acceptance and authorization are supplied records, not conclusions of these mathematical lemmas.

| Claim | Evidence class and present disposition |
| --- | --- |
| Domain, padded exact energy, lifecycle, indexed output | Granted synthetic D001/AS contract; ACT supplies activation |
| No-replay complete deterministic machine | Explicit additional conditional hypothesis from PO/TASK, not an AS requirement or measured property |
| T1, W1/W2, Z, L2, and counterexample evaluations | Mathematical derivations authored here; CLAIMED_PROOF_PENDING_REVIEW |
| Fixed-n reachability, L4, T2, 372 bits and 47 octets | Conditional mathematical derivations authored here; CLAIMED_PROOF_PENDING_REVIEW |
| Bounded Python checks | Supplemental finite arithmetic evidence only, with exact command and scope in the briefing |
| SHA-256 checks | Local byte consistency with the supplied manifest; no external authentication |
| Implementation memory fit, execution behavior, interface correctness, no FPU dependency, detection completion | Unestablished; no implementation or target evidence supplied |
| Independent proof acceptance | Not performed and not claimed; required distinct next gate |

## 10. Full-interface limitations and remaining obligations

The numeric theorem applies for arbitrary finite accepted epoch lengths. It supplies no mechanism for producing the required logical index and no finite epoch bound. A later fixed-width counter can exhaust its representable indices while energies remain numerically correct. An external index mechanism, epoch limit, encoding or other interpretation requires later authorized interface clarification and applicability review. Optional reset and nominal 1 ms cadence supply no maximum lifetime. There is no authorized wrap policy here.

PO-003-3's proposed unbounded-index problem remains a separate unproven opportunity under its additional closed finite-state model. This artifact neither proves that opportunity nor declares the accepted AS inconsistent. Finite detector RAM alone does not establish closure of all interface information sources.

ACT keeps the following items open; this proof attempt discharges none:

| Obligation | Remaining evidence |
| --- | --- |
| T002-2 | Actual output comparisons against an independent 32-sample specification on boundary and randomized streams |
| T002-3 | Realization startup, reset, first/31st/32nd/33rd events, and prior-epoch exclusion |
| T002-4 | One exact energy with correct logical index per accepted event; interface/index interpretation |
| T002-5 | Explicit invalid rejection with unchanged state/index, applicable detectable-fault reporting and recorded limitations |
| T002-6 | Actual persistent/scratch/owned-stack accounting, ownership/replay boundary, RAM ceiling and no floating-point hardware dependency |
| T002-7 | Concrete target/toolchain and applicable runtime/resource evidence; no invented deadline or quantitative optimization threshold |
| T002-8 / R4 | Threshold, duration, boolean detection decision and integration criteria/verification before any whole-detector completion claim |

TRACE's earlier T002-1 acceptance status is superseded by supplied ACT, without independently authenticating the historical gate here. There is no AP selection, accepted F, C implementation, hardware compliance, inherited historical VO discharge or cleanroom qualification. The required next step is a distinct proof review of T1/T2 followed by a separate applicability assessment when a concrete interface and information boundary exist.
