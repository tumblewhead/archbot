# CLN-001 AP feasibility evaluation 009

**Independent evaluation of three unselected candidates; synthetic scope only.** The conducted numeric models agree with an independent exact specification. Complete physical interfaces, detector RAM fit, build dependencies and target F values remain **UNKNOWN for every candidate**. No AP, contract or AD is accepted; no target, product or formal cleanroom qualification is claimed.

## Authority and evidence boundary

The active requirements are the original [AS-REV-002](../inputs/AS-REV-002.md), activated by [AS-ACTIVATION-002](../inputs/AS-ACTIVATION-002.yaml), **plus** [AS-ADDENDUM-008-R1](../inputs/AS-ADDENDUM-008-R1.md), separately activated by its [disposition](../inputs/AS-ADDENDUM-008-R1-DISPOSITION.yaml). Neither original source is rewritten. Their preserved DRAFT/PROPOSED labels describe authoring-time status; the supplied activation records establish current scoped authority. Historical activation executions and archive identities were not independently authenticated here.

[DECISION-001](../inputs/DECISION-001.yaml) supplies the synthetic requirements authority. [F-DISPOSITION-003](../inputs/F-DISPOSITION-003.yaml) establishes H1–H6 and the three active F axes. [D002](../inputs/D002-INTERFACE-DISPOSITION.yaml) requires explicit refinement, ownership and dependency disclosure. [PROOF-DISPOSITION-004](../inputs/PROOF-DISPOSITION-004.yaml) accepts T1 and conditional T2 only within their stated mathematical boundaries. [D003's disposition](../inputs/D003-DISPOSITION-007.yaml) is proposal-scope referral, not an effective AS amendment or physical contract. R1's later activation establishes the observable clarification, not a service.

The [candidate review](../inputs/REVIEW-AP-006.md), [D003 review](../inputs/REVIEW-D003-007.md) and focused R1 [report](../inputs/REVIEW-AS-ADDENDUM-008-R1.md)/[receipt](../inputs/REVIEW-AS-ADDENDUM-008-R1.json) are supplied prior source-review evidence. Their old next-gate and pending labels are read in chronological context under current dispositions. This evaluation independently challenges models rather than importing prior test counts or treating favorable source review as eligibility. Unavailable historical artifacts named inside them were not retrieved. The supplied [scope](../inputs/AP-EVALUATION-SCOPE-009.yaml) and [Stage-9 briefing](../inputs/STAGE9_BRIEFING.md) authorize this evaluation only.

For accepted valid samples within one initialized/reset sequence:

- H1: exact E_n = sum of squares of x_(n-31)..x_n.
- H2: absent pre-sequence positions alone contribute zero; explicit reset starts new history and one-based rank.
- H3: exactly one correct consumer-decodable logical (n,E_n) is owed per accepted event, without silent loss. Numeric commitment, publication and acquisition are distinct.
- H4: values outside 0..4095 are explicitly rejected or expose precondition violation, without advancing history, rank or association. Observable ordering/gap faults must be reported; unobservable faults have no invented detection guarantee.
- H5: at most 2048 bytes of complete detector-attributable peak-live RAM, including owned persistent state, scratch and call stack, queues, index association and attributable shared allocations.
- H6: no hardware-FPU dependency; no additional prohibition on software floating point is inferred.

R1 requires a decoder using information actually available to the actual consumer for unrestricted accepted rank and reset/restart lifetime. Observer rank and a fresh request handle alone are insufficient. Accepted-result debt persists across stalls, fault reports, restart and reset. Old results must not alias new-sequence work. A separate acknowledgment is **optional**; observable reset ordering and association are required. No finite epoch, forced reset, wrap, valid-event filtering, publisher pause, backpressure, universal crash survival, infinite availability or exactly-once physical transport is supplied. One logical owed result does not forbid retransmission of that same logical result under a later reviewed retry mechanism.

The nominal 1 ms cadence is not a hard deadline or latency bound. R4 threshold/duration/boolean detection and integration remain deferred. The original [brief](../inputs/problem-origin.md), [ADC](../inputs/adc.md) and [target](../inputs/target.md) are synthetic origins, not hardware evidence.

| Evidence level | Evidence actually available |
| --- | --- |
| CONDITIONAL_SYMBOLIC | Algebra, declared preconditions, information-flow/resource expressions, conditional falsifiers. |
| FINITE_MODEL | Fresh inline Python exact-integer models, shortcut witnesses and small interleaving models below. |
| HOST_SPECIFIC | No realized candidate allocation, build, execution-cost or host-energy evidence. Python version records reproducibility, not a candidate host realization. |
| TARGET_SPECIFIC | None; no concrete target/toolchain selected, built or measured. |

## Independent experiments actually conducted

The exact executed inline programs are preserved in the JSON receipt under experiments.numeric.source and experiments.races.source, with full commands, source digests and results. They create no code/test files. Reproduction from the repository root:

~~~bash
python3 -B - <<'PY'
import json
with open("out/AP-EVALUATION-009.json") as f:
    receipt = json.load(f)
for key in ("numeric", "races"):
    source = receipt["experiments"][key]["source"]
    exec(compile(source, "<evaluation-009-" + key + ">", "exec"), {})
PY
~~~

The independent oracle retains **all valid accepted samples in the current sequence** and sums its latest 32 squares. It never uses a candidate tail, cursor or aggregate. A uses raw31 circular storage and reduction before overwrite. B uses square31, S and an oldest-first circular cursor. C uses a separate **ASSUMED hypothetical** service with immutable pre-event tuple, coordinated service rank and reset. This service is scaffolding, not an authorized provider or service-feasibility evidence.

Each accepted transition compares all three energies to the oracle, checks chronological A/B tails against the oracle suffix, checks B's S against both stored slots and the oracle suffix, and checks the simulated service's tail/rank. Test-harness n, full history and service state are instrumentation and assumptions, not RI decoders, candidate memory allocations or supplied external information.

| Run | Scope | Valid events | Rejected attempts | Explicit resets |
| --- | --- | ---: | ---: | ---: |
| E01 | All 6,561 length-8 streams over {0,1,4095} | 52,488 | 0 | 6,561 |
| E02 seed 9009 | 120,000 actions | 105,633 | 12,001 | 2,366 |
| E02 seed 9010 | 120,000 actions | 105,460 | 12,155 | 2,385 |
| E03 | Ones, maxima, impulse, distinct expiry: 65 each; alternating: 66 | 326 | 0 | 0 |
| E04 | 0..4095 repeated eight times, uninterrupted | 32,768 | 0 | 0 |
| E05 | Reset from every pre-reset cursor 0..30, then sample 2 | 2,418 | 0 | 62 |
| E06 | Reject before/after reset at prefixes 0,1,31,32,33,100 | 203 | 36 | 12 |
| **Total** | Correct models | **299,296** | **24,192** | **11,386** |

There were **897,888 energy comparisons and zero correct-model mismatches** in the completed numeric run. Random actions draw randrange(100): <2 reset; 2..11 choose invalid from (-1,4096,65536); otherwise draw randrange(4096). No invalid attempt enters oracle or candidate/service state. Whole represented sequence state is compared before/after rejection; this tests a modeled branch, not a physical API or unsupplied association subsystem. Initial construction is not counted as an explicit reset.

At n=1/31/32/33, E is 1/31/32/32 for ones, Q/31Q/32Q/32Q for maxima, and Q/Q/Q/0 for a maximum impulse followed by zeros, Q=16,769,025. B's retained S for the impulse is Q/Q/0/0: output 32 still contains the first sample although the next pre-tail does not. Boundary values at 63/64/65 are also in JSON.

Startup enumeration ends at 8 and cannot establish 31-slot expiry. Random sequences reached lengths 335 and 380; the uninterrupted stream reached 32,768. These are not exhaustive over tails, schedules, unrestricted n, reset generations, failures or arithmetic representations. Python exact integers exclude target overflow, language promotions, alignment and interrupt behavior. These runs do not discharge T002 obligations.

The fresh witness suite contains **21 named groups**, **20 refuting shortcuts** and one confirming permutation invariance of a current sum. The race program enumerates four legal acceptance/reset/publication orders for each pair (1,2) and (1,1): eight schedules. Observer-ledger debt is preserved in all; relabeling old output with the current sequence fails in six, and clearing pending debt on reset loses work in six. The observer ledger is not a candidate association mechanism. Equal sample values show old/new pairs can share both n and E.

A live-read snapshot model places an append at every cut k=0..31 through a 31-entry read. With pre-tail (1,0,...,0) and current 2, required E=5. All-post k=0 gives 8; k=1..30 gives 9; only all-pre k=31 gives 5. Thus **31 of 32 cut points are wrong** for this deliberately unprotected read. This is a finite interleaving falsifier, not a concurrent service realization.

An exploratory first run stopped at M04 because a proposed single-impulse frozen-cursor witness produced 0 in both paths. That witness did not distinguish the fault. The corrected prefix (1,2,29 zeros) exposes required 0 versus observed 4 later. Only the completed rerun supplies reported totals; preliminary work is not added. Both source identities and the setup correction are recorded in JSON.

## AP-006-A dossier: raw31 recomputation

Source: [candidate A](../inputs/AP-CANDIDATES-006.md). **Numeric feasibility: conditional, supported by finite models. Full physical feasibility: UNKNOWN.**

Before event n, T=(x_(n-31),...,x_(n-1)), padded only before sequence start. Reducing T with current x_n gives precisely 32 terms. Evicting the oldest after reduction and appending x_n establishes the next pre-tail. This conditional inductive argument is not a representation/build proof. The model verified the ordered next tail at every accepted transition.

Q=4095²=16,769,025<2²⁴; 31Q=519,839,775; 32Q=536,608,800<2²⁹. Nonnegative reduction partial sums fit the full-window bound. Abstract 32-bit unsigned arithmetic suffices **with correct widening before squaring and correct state/order**. These bounds do not validate language promotions, narrowing or target instructions.

M01 overwrites oldest 1 before reducing with new 2: required 5 becomes 8. M02 has pre-tail (1,2,29 zeros) and wrongly evicts the second value: current E remains 5 but the next becomes 1 instead of 4. Summing every slot can conceal a wrong age cursor until later. Reset must exclude old raw slots and staging coherently.

A's history is detector-owned. Its conditional numeric representation is 31 raw slots, not total RAM. Order/control, input/accumulator/result staging, index association, pending work, transport, owned callees/stack and shared attribution remain additional. RI still needs publisher/consumer coordination. No actual consumer inventory or decoder is supplied. Numeric history sufficiency does not establish result debt retention or delivery.

T1's latest-31 future distinctions are directly represented. T2 can apply to complete closed A-NUM at fixed n>=32 only after all output-affecting state, determinism, no replay and unrestricted continuations are established. External ordinal association does not remove fixed-n numeric distinctions. Full-interface closure is unestablished.

## AP-006-B dossier: square31 and aggregate

Source: [candidate B](../inputs/AP-CANDIDATES-006.md). **Numeric feasibility: conditional, supported by finite models. Full physical feasibility: UNKNOWN.**

Let Q_n be the chronological square31 pre-tail, S_n=sum(Q_n), cursor pointing to oldest q_old. Then q=x_n², E_n=S_n+q and S_(n+1)=E_n-q_old. Replace that oldest slot and advance the age cursor. With coherent updates these facts establish the next invariant. Exact squaring is injective on the nonnegative domain, so ordered squares preserve T1 distinctions; S alone does not. The redundant aggregate changes work and consistency obligations without reducing distinguishability.

Under the invariant, 0<=q_old<=S_n<=31Q and 0<=E_n-q_old<=31Q. Abstract 32-bit unsigned value capacity suffices; it does not guarantee multiplication promotion, real reset, chronological eviction or safe partial updates.

M03 emits correct current E=5 then retains S=1 after wrong-age eviction, with S still equal to the sum of stored slots; next required E=4 becomes 1. **S=sum(slots) alone is too weak.** M04 freezes an age advance and fails later. M05 clears tail/cursor but leaves S=9, producing 9 instead of 0. M06 clears S but leaves an expiring square 1: current E=0 looks correct, retained S becomes -1, and the next zero fails; uint32 wrap would be 4,294,967,295. M07/M08 exercise both halves of a torn tail/S update. These refute shortcuts and identify transition/reset obligations; they add no arbitrary-corruption recovery requirement.

B retains square31 plus S and all order, transaction/index, pending, scratch/stack/shared costs. RI barriers are shared with A; coherent tail/S/cursor, acceptance and owed response add coupling. No atomic primitive, transaction mechanism or crash-safe update is supplied. T2's conditional numeric closure is analogous to A; redundant S does not reduce required numeric distinctions.

## AP-006-C dossier: externally retained pre-tail

Source: [candidate C](../inputs/AP-CANDIDATES-006.md). **Numeric feasibility: conditional on a simulated service. Actual service and full physical feasibility: UNKNOWN.**

If a provider supplies exactly pre-event x_(n-31)..x_(n-1), bound to the same current sample, accepted ordinal and reset context, fresh integer reduction yields E_n. Correct-model tests deliberately supply that assumption. They establish arithmetic compatibility **under the assumption**, not C-HIST existence, authorization, fidelity, availability or cost.

M09/M10 separate mixed versions (9 rather than 5) and a coherent wrong-event snapshot (8 rather than 5). M11 uses an old-sequence snapshot after reset, giving 5 instead of 4. All terms remain in range. M12 confirms that permutation of a correct term set leaves the current sum unchanged; range/length and current-sum agreement therefore cannot prove chronology or source truth. Chronology still governs future tails and expiration. Version validation can detect some interference but does not itself prove correct event identity, bounded retries or progress.

C-HIST must retain requested information until reduction and required response association finish, or provide a reviewed exact recovery path. A rolling live tail may overwrite unread data; pins/copies/retries can grow with simultaneous work. Sole-source eviction after acceptance leaves output owed; a reported service loss does not reconstruct it. No automatic retry, infinite retention or publisher suspension is assumed.

RN would decode an exact losslessly framed accepted numeral, but no provider, transport, parser or accepted-event binding is supplied. Acquisition/attempt/retry count is not accepted rank. Streaming proves neither bounded local staging nor finite provider capacity/work. An ordinary binary numeral has floor(log2(n))+1 bits; storing or transmitting that representation has length-dependent costs over unrestricted n.

C-DET's absence of retained numeric history is a conditional ownership/representation choice. Validation, accumulator/current context, stream/session references, handles, staged results/debt, parser/framing, queues, owned callees/stack and shared/pinned costs remain. Only demonstrated exclusively upstream-owned memory can be excluded. C-DET reads C-HIST, so detector-local T2 no-replay does not hold. A larger boundary qualifies only with all numeric sources included and closure demonstrated. T1 still requires the joint system to preserve/retrieve latest-31 distinctions.

## H gates and continuing obligations

Every realized gate below remains UNKNOWN. Finite success is evidence for a model, never compatibility-grade PASS.

| Gate | A | B | C | Missing full-scope evidence |
| --- | --- | --- | --- | --- |
| H1 | FINITE_MODEL reduction/ordered tail | FINITE_MODEL recurrence/chronological invariant | FINITE_MODEL with assumed exact pre-tail | Representation and realized transitions; C fidelity/event binding. |
| H2 | FINITE_MODEL numeric reset | FINITE_MODEL tail/S/cursor reset | FINITE_MODEL reset hypothetical service | Real reset linearization, old work association/exclusion and restart lifetime. |
| H3 | CONDITIONAL_SYMBOLIC RI, ambiguity/debt falsifiers | Same plus coupled commit | CONDITIONAL_SYMBOLIC RN, unsupplied provider | Actual consumer/decoder, acceptance/result bijection, unrestricted rank, no loss/reset/retry semantics. |
| H4 | FINITE_MODEL rejection branch | FINITE_MODEL coupled-state rejection | FINITE_MODEL no append/rank advance | Physical API, complete association invariance, observable fault reports and detection limits. |
| H5 | CONDITIONAL_SYMBOLIC raw31+overhead | CONDITIONAL_SYMBOLIC square31+S+overhead | CONDITIONAL_SYMBOLIC client/shared/external boundary | Complete peak-live bound <=2048; no actual allocation/stack measurements. |
| H6 | CONDITIONAL_SYMBOLIC integer intent | CONDITIONAL_SYMBOLIC integer intent | CONDITIONAL_SYMBOLIC integer intent; dependencies unknown | Scoped dependency/build/execution evidence; no target evidence. |

| Obligation | Status | Evidence due and claim boundary |
| --- | --- | --- |
| T002-2 | OPEN | Realized A reduction/B ordered recurrence/C requested snapshot and reduction versus independent specification before correctness claims. |
| T002-3 | OPEN | Startup/boundaries/reset, old snapshot/result exclusion and association, consumer-visible order; later authorized lifecycle verification. |
| T002-4 | OPEN | Exact consumer rank and one result per accepted event through commit/stall/restart/retry/reset; later physical interface verification. |
| T002-5 | OPEN | Real rejection invariance/reporting of faults detectable by the chosen interface before input-contract compliance claims; no invented recovery guarantee. |
| T002-6 | OPEN | Complete ownership/peak allocations/stack and no-FPU dependency evidence at later realization; target evidence before target claims. |
| T002-7 | OPEN | Compatible workload/device/toolchain/attribution timing, compute and device-energy evidence before real-hardware claims; no hard 1 ms bound or numeric compute/power target. |
| T002-8 | OPEN/DEFERRED | Threshold, duration, boolean output and integration criteria plus verification before complete sustained-energy detector claim. |
| R4 | OPEN/DEFERRED | Same full detection integration boundary; numeric primitive correctness does not complete it. |

Mapping uses supplied [DECISION-TRACE-002](../inputs/DECISION-TRACE-002.md) with current activation/F/D002/R1 records. Older T002-1 draft gate language is not evidence that the activated AS remains unaccepted. No local obligation or historical VO is discharged.

## Interface and service dependency matrix

No physical consumer component or retained consumer-state inventory is identified in the candidates. This table distinguishes contemplated observations from required decoder inputs; **it supplies no candidate decoder**.

| Boundary | Contemplated or supplied information | Required evidence | Status |
| --- | --- | --- | --- |
| A/B RI consumer | Proposed request-linked response and observable reset; no implemented interface or consumer state supplied | Accepted rank of request, accepted-only ordering, result bijection, reset context, prior accepted prefix across restart, delayed/duplicate handling and unrestricted-rank decoder using actual state | UNKNOWN; observer trace rank is not consumer evidence. |
| C RN provider | Ordinary publisher supplies current ordered values; no ordinal service | Authorized exact accepted-event generation, invalid/retry exclusion, current/snapshot/result binding, reset/lifetime and retention | UNSUPPLIED/UNAPPROVED. |
| C RN transport/consumer | Proposed lossless variable-length numeral; no channels/framing/parser supplied | Lossless framing/termination/integrity, malformed/truncated/replay handling, event/reset association, exact decoding and client/provider bounds | UNSUPPLIED/UNAPPROVED. |
| C-HIST snapshot | Hypothetical service in model only | Correct-event pre-tail, startup validity, chronological source maintenance, coherent snapshot linearization and faithful data | UNSUPPLIED/UNAPPROVED; coherence is not identity. |
| C-HIST retention | No concrete store/lifetime supplied | Pin/copy/replay retention/release through handoff, concurrency/eviction limits, provider/client restart, availability/error/interference behavior | UNKNOWN; live31 alone does not retain arbitrary delayed requests. |
| All acceptance/handoff | Obligations only; no transaction/scheduling boundary | Acquisition, validation, acceptance, numeric commitment and publication points; preservation of every accepted debt | UNKNOWN; no retrospective unacceptance or fault-as-delivery. |
| All reset/restart | Explicit semantics active; drain/marker/identity mechanisms unselected | Consumer-visible linearization, old/new association, finite-tag retirement/reuse and continued old debt | UNKNOWN; distinct acknowledgment optional. |
| Ownership/attribution | Conditional descriptions | Account every live local/shared allocation and device/service activity; justify exclusive upstream exclusions | UNKNOWN; location or allocator identity is insufficient. |

Acceptance/lifetime trace obligations:

1. Validate before narrowing/squaring or sequence/association mutation. Attempts 7,4096,8 owe (1,49), rejection, (2,113), never ordinal 3 for 8.
2. A defined valid acceptance creates a result obligation. Numeric commitment must correspond to that event. Capacity failure cannot retrospectively rename it unaccepted. Ordered omission-free delivery remains; publisher pause/backpressure/storage is not supplied.
3. Preserve enough result/replay and identity state until correct handoff. Latest-31 state alone loses old debt: 1 or 2 followed by 32 zeros yields the same current (33,0), but old debts differ as (1,1)/(1,4).
4. Reset restarts numeric history/rank without canceling old debt. Old (1,1) and new (1,4), or two identical (1,1) pairs in different sequences, cannot be relabeled by arrival time. Drain or retained identity remain unselected; a stalled drain has no established completion bound.
5. Consumer restart does not reset the detector: 1 then 0 still owes (2,1). An energy-only restarted consumer with the same state sees zero for required ranks 1 or 2 on zero histories. No decoder of that state/observation can recover both. This is conditional impossibility for that **narrow information boundary**, not all RI services.
6. With only Q pending entry slots and no other retention/replay/compression/acceptance coordination, Q+1 accepted debts cannot fit. The Q=2 model retains (1,1),(2,5), leaving (3,14) owed but unretained. This refutes queue-alone claims under stated hypotheses, not every finite architecture, and authorizes no input restriction.
7. Retrying old 1 as a fresh acceptance yields (2,2), not recovery of old (1,1); accepting next sample 2 should yield (2,5). A retry protocol, if chosen later, needs retained identity, duplicate and retirement rules. One logical result is distinct from exactly-once transport.
8. A sole b-bit rank repeats at 1 and 1+2^b; a sole g-bit generation repeats after 2^g resets. Safe live-work lifetime/retirement/reuse or additional state needs evidence. No epoch cap, forced reset or retained oracle is inferred.

At a **closed finite complete consumer/detector boundary**, with identical zero input observations, no external/growing trace and a decoder using only finite internal state/current observation, unrestricted exact rank forces a repeated observation/state and hence ambiguity. This is a conditional boundary argument, not adoption of PO-003-3 or blanket AP rejection. Whether an actual reviewed service can supply sufficient information is UNKNOWN.

Fault reports are necessary for observable failures but do not discharge accepted debt. Permanent absence or arbitrary destruction of all information can leave debt unpaid; the requirement is not a universal recovery service. Missing liveness/capacity contracts must not be hidden by treating no deadline as infinite storage.

## Full resource accounting and symbolic Figure-of-Merit

The [comparison worksheet](../inputs/AP-COMPARISON-006.md) defines:

~~~text
RAM_peak_c = max_t [P_c(t)+S_c(t)+K_c(t)+G_c(t)]
~~~

P is owned persistent state; S live non-stack scratch/buffers; K owned stack including callees; G attributable shared allocations counted nowhere else. Stack locals belong in K, not also S. Count simultaneous live allocations once. Separate maxima are not an exact peak; overlap/reuse savings require actual lifetimes.

| Candidate | Conditional numeric payload | Other detector-attributable state | External-only resources, conditional on established ownership |
| --- | --- | --- | --- |
| A | 31 b_x raw slots | Order/validity/cursor; input/reduction/result staging; transaction/reset/index association; queues/retries, client/transport/library state, owned stack/callees, shared attribution | Acquisition; external consumer association/index state if genuinely exclusively external. |
| B | 31 b_q square slots +b_S | Same classes plus aggregate/cursor consistency and coupled update staging | Same as A; no assumed external numeric replay. |
| C | No retained detector numeric history **only at proposed boundary** | Current/accumulator/stream position, sessions/handles, parser/framing, result/debt/ordinal/reset state, buffers, queues/retries, owned stack/callees, shared/pinned copies | C-HIST raw31/current/validity/control; snapshot versions/pins/copies/retries; RN numeral storage/generation/transport, provider buffers/stack/control. |

b_x,b_q,b_S are representation sizes, not measurements; required value capacities are 12,24,29 bits. No packing/alignment/allocation has been selected. If numeric payload is fixed allocated and overhead h_c=O_c+T_c+max_t(S_c+K_c+G_c) is complete:

~~~text
R_A = 31 b_x + h_A
R_B = 31 b_q + b_S + h_B
R_C = h_C
R_B > R_A iff 31(b_q-b_x)+b_S+h_B-h_A > 0
R_C < R_A iff h_C < 31 b_x+h_A
R_C < R_B iff h_C < 31 b_q+b_S+h_B
~~~

All inequalities are conditional after complete ownership attribution; none is instantiated or proves <=2048. With changing payload lifetimes use the general maximum formula.

T_c and scratch may depend on rank n, pending debt d, snapshots p, retries r and outstanding reset contexts e. Stored binary numerals grow with log n; arbitrary pending results can grow with d; retained traces grow with sequence length; a separate-copy snapshot model can grow roughly as p times tail storage. Shared/versioned stores, variable-length allocations, retry interference and allocator overhead can be nonlinear. No constant h or linear implementation is presumed. Streaming reduces some staging only under a concrete parser/transport contract. External costs are never phantom-free.

T2 is a conditional 2^372 complete-state distinguishability / 372-bit / 47-whole-octet capacity minimum at fixed n>=32, **not a sufficient 47-byte SRAM implementation**. It does not count full index/reset/fault/scratch/stack. T1 excludes current already-emitted outputs and interface metadata. C's readable upstream history defeats detector-local no-replay; a larger complete closed boundary remains unestablished. External index alone does not remove fixed-n numeric distinctions. PO-003-1/3 remain unproven.

### Typed compute comparison

M0 consistently means a serial, quiescent, fault-free valid event, padded31, full A/C recomputation and intact B invariant. Initialize the reduction with current square for 31 additions; a literal zero-seeded 32-term loop would have 32 and needs its own cost.

| Candidate | Partial detector typed work per M0 valid event | Additional UNKNOWN work |
| --- | --- | --- |
| A | 32 SQ_x +31 ADD_E +31 RD_x +WR_x +ADV_31 | V_A validation; J_A index; D_A acceptance/publication; L_A conversion/packing/address/control/staging, accumulator/result/cursor accesses. |
| B | SQ_x +ADD_E +SUB_E +RD_q +WR_q +ADV_31 | V_B+J_B+D_B+L_B, including S reads/writes and coupled commit. |
| C | 32 SQ_x +31 ADD_E +OPEN_SNAP +31 FETCH_x | V_C snapshot/current/framing validation; J_C RN; D_C coordination; L_C streaming/client/control; outside tail/snapshot/ordinal/transport work. |

Square/raw reads have different widths. FETCH is an externally supplied entry, not 31 proven round trips. Local reads and external fetches have distinct types. No target cycles, joules, currents or scalar F weights are invented.

Arithmetic projection A minus B is 31 SQ_x +30 ADD_E -SUB_E. Under a **sensitivity model only**, mapping every class to common scalar costs and retaining all overhead, B's detector compute is lower only if:

~~~text
31c_SQ+30c_ADD-c_SUB+31c_RDx-c_RDq+c_WRx-c_WRq
+Delta_overhead(A-B) > 0
~~~

Delta includes validation, index, delivery, conversions, S/result/cursor traffic and unequal cursor work. Cursor cost cancels only if actually equal. Coefficients stay UNKNOWN. This is neither measured target cost, adopted scalar F nor full compute/energy dominance. C shares A's reduction counts but adds distinct external reads/snapshot/RN/provider work.

For a common workload w, interval Delta and N>0 accepted events:

~~~text
Compute_c(w) =
[I_c + sum C_valid + sum C_reject + sum C_reset
 + sum C_fault + C_pending] / N
~~~

I includes initialization. Reset includes raw31 versus square31+S clearing/validity and association fencing, or C joint history/index reset and old work. Rejection includes validation/report with no accepted transition. Faults, stalls, retries and pending work remain chargeable. Compare equal opening/closing debt or complete equivalent owed work; do not favor an AP by ending before deferred work. If N=0 report interval totals, not a division.

### Electrical device energy and evidence compatibility

For common pinned device/build/workload/attribution, a **sensitivity expression** is:

~~~text
J_c = [sum_j epsilon_j N_c,j + E_baseline_attr,c + E_wait_attr,c
       + E_transport_attr,c + E_other_attr,c] / N
~~~

Coefficients, baseline/wait effects, transport and residuals remain UNKNOWN. Include valid/rejection/initialization/reset/fault/retry/pending work on equivalent intervals and debt closure. Avoid double counting transport already priced in operation classes. Additive operation pricing itself needs validation. Memory traffic/waiting may outweigh arithmetic. J is device electrical consumption, not signal E_n.

Report external-only RAM/work/energy separately. If history/index service runs on the same device, its attributable device energy cannot disappear because its RAM is upstream-owned. Detector-only, whole-device and multi-device scopes need reconciliation; off-device service energy is not zero.

| Comparison | Compatible evidence available | Permitted conclusion |
| --- | --- | --- |
| A/B ideal kernels | Common finite oracle, conditional algebra | Both match tested numeric relation; no full gate PASS. |
| A/B arithmetic projection | Common M0 typed counts | Repeated squares/additions versus subtraction tradeoff; no full compute/energy dominance. |
| A/B complete RAM | Symbolic formula, unknown representations/overhead | Conditional difference only; no realized ordering or fit. |
| C versus A/B arithmetic | Common reduction projection, different memory/service types | Reduction comparison only; complete work unknown. |
| C versus A/B complete RAM | Ownership/lifetimes/services not established | Conditional local inequalities only; realized scopes not comparable. |
| Any realized compute/device energy | No common device/build/cost/workload measurements | UNKNOWN, neither favorable tie nor dominance. |

All realized F coordinates remain UNKNOWN for A/B/C. H gates precede F. There is no full evidence-compatible Pareto comparison/downselection, no weights or new numeric threshold; flash is inactive/unknown.

## Decision-relevant next evidence

This orders experiments by information gain and engineering cost, **not candidates**, and grants no new contract/implementation authority.

1. **Distinct Stage-10 review of these exact three outputs.** Check authority chronology, source coverage, oracle independence, witness boundaries and F scopes; reproduce receipt programs. Low cost before reliance on this evaluation. Any later AP commitment needs separate authority after review.
2. **Actual consumer information/lifecycle inventory for all candidates.** Identify component/state and require an explicit proposed decoder/refinement plus acceptance/commit/publication/reset/restart/retry events. Challenge hidden zero prefixes at ranks 1/2, invalid attempts, delayed old/new identical pairs, tag reuse, restart and Q+1 debts. Indistinguishable observations with distinct required n falsify the narrow interface. Do not invent a decoder or lifetime cap.
3. **C service existence and ownership inquiry before building one.** Obtain provider/ordinal/transport/history capability and authorization, if any; seek exact event-bound pre-tail, consistency, retention/release, reset/restart, availability/error and costs. A current-value-only publisher, wrong-event snapshot or sole-source eviction falsifies the reliance. No provider leaves C conditional, not universally impossible.
4. **Bound live work and account resources for each proposed interface.** Establish queues, concurrency, parser/index lengths, owned stack/callees/shared attribution, old contexts and safe identity reuse. Continued acceptance beyond exact retention without an authorized preservation path falsifies no-loss/2048 claims. This can expose a necessary operating-contract decision before target expense.
5. **After separate realization authorization, test actual representation/lifecycle.** Compare chosen-width transitions to oracle at expiry/reset positions; exercise B coupled updates and C read/append/reset interference; verify consumer association and actual rejection/fault reports. Check future expiration as well as current energy/S=sum(slots); event identity as well as coherence.
6. **After concrete target/build/common workloads are authorized, close H5/H6/F evidence.** Obtain allocation/linker and stack/callee bounds; appropriate dependency/build/disassembly/execution evidence; equivalent debt-closed timing and electrical measurements with uncertainty. Include same-device services and report external costs separately. Python models and payload estimates supply none of these results.
7. **Before a complete-detector claim, resolve T002-8/R4.** Obtain threshold/duration/boolean/integration criteria and verification through the authorized decision process.

## Source receipt, independence and stop

All **21/21 current payload hashes matched** inputs/SHA256SUMS using direct Python SHA-256 comparison. The JSON contains expected/observed digests, byte counts, instruction/manifest identities and source roles. Current agreement establishes byte consistency, not approval, authenticated provenance, historical execution or physical isolation.

| Supplied payload | SHA-256 (expected = observed) |
| --- | --- |
| [PROOF-DISPOSITION-004.yaml](../inputs/PROOF-DISPOSITION-004.yaml) | 0ee6dd20aadc60e6d88ac497992cf3467177e6a4763084d818710d4c671ebb94 |
| [DECISION-001.yaml](../inputs/DECISION-001.yaml) | 1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36 |
| [AP-EVALUATION-SCOPE-009.yaml](../inputs/AP-EVALUATION-SCOPE-009.yaml) | 20c41f16470efee2d0680d12dfb6729a5ab4645645e9335e7696f2c5118995fd |
| [adc.md](../inputs/adc.md) | 284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 |
| [STAGE9_BRIEFING.md](../inputs/STAGE9_BRIEFING.md) | 2b2497633b9b9580f053047387a1f3b644ee5aef01bc48bc5951ce244eca0835 |
| [D003-DISPOSITION-007.yaml](../inputs/D003-DISPOSITION-007.yaml) | 369f6a27ba6ed9344865c9363df2009239ed3694a8d088699b2dce2baa4b5b76 |
| [AS-REV-002.md](../inputs/AS-REV-002.md) | 36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830 |
| [AS-ADDENDUM-008-R1-DISPOSITION.yaml](../inputs/AS-ADDENDUM-008-R1-DISPOSITION.yaml) | 42a8f3a0c138cb4646c107c2a9519cef16a8faddb3b11f299596286ca9553618 |
| [REVIEW-AP-006.md](../inputs/REVIEW-AP-006.md) | 49da5d3fceecf43d46a83d576f6929ce09943ac8f9a7a4bac413df0657b8566b |
| [REVIEW-D003-007.md](../inputs/REVIEW-D003-007.md) | 54c9d6e308589fc9a7a0621f46f9d58bc384233c528df9993d48a726a6c793cf |
| [AP-CANDIDATES-006.md](../inputs/AP-CANDIDATES-006.md) | 74ff94508f61c8a36957fc33f232624ad921e219482887194e4ef5434e693c00 |
| [AP-COMPARISON-006.md](../inputs/AP-COMPARISON-006.md) | 83105ae06ca91a6861e45391a5b9a93ccc831a919f12e81d356c4ca0241fb439 |
| [DECISION-TRACE-002.md](../inputs/DECISION-TRACE-002.md) | 90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2 |
| [problem-origin.md](../inputs/problem-origin.md) | 90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 |
| [F-DISPOSITION-003.yaml](../inputs/F-DISPOSITION-003.yaml) | ad3802e8672fc1366a04ff1e141aeef2951968cc7dd972e25f97512ea1d9eb2f |
| [target.md](../inputs/target.md) | c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 |
| [D002-INTERFACE-DISPOSITION.yaml](../inputs/D002-INTERFACE-DISPOSITION.yaml) | cd3879ca943e48108c331a610ad9565f9a3d1037deeb6b55fcd66abea42cf5a1 |
| [AS-ADDENDUM-008-R1.md](../inputs/AS-ADDENDUM-008-R1.md) | d0faf69b08c0ae08f74773cd711658641fcecaa47c2762b9c45dd3322fdda550 |
| [AS-ACTIVATION-002.yaml](../inputs/AS-ACTIVATION-002.yaml) | d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c |
| [REVIEW-AS-ADDENDUM-008-R1.md](../inputs/REVIEW-AS-ADDENDUM-008-R1.md) | e3900f30ab7550ddda079b401a8e377668f5bfa826521320d10ce0f73ce44e84 |
| [REVIEW-AS-ADDENDUM-008-R1.json](../inputs/REVIEW-AS-ADDENDUM-008-R1.json) | f6e732ad5e91b5bd72b2acca79acf884283f9a2ab59b6543551aee667bc90549 |

Only AGENTS.md, TASK.md, the current manifest and supplied allowlisted payloads informed this evaluation. No Git history, old solved Toy1 AP/CON/DE/C, other workspace, network, connected app, hidden reference/evaluator or subagent was used. Historical delegation, review/proof executions, archive identities and external agent separation remain unauthenticated. The positive allowlist is not OS isolation; neither OS nor connector isolation is verified.

Only the three requested outputs were written. All APs remain unselected; full realized H1–H6 and realized F remain UNKNOWN; T002-2..8 remain OPEN and R4 OPEN/DEFERRED. No contract/AD acceptance, CON/DE/C, target/product qualification or VO discharge occurred. Next gate: **distinct independent Stage-10 review of evaluation evidence before any separately authorized AP commitment**.
