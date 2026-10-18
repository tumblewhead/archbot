# CLN-001 comparison and separate symbolic F worksheet 006

All candidates are **AP_CANDIDATE_NOT_SELECTED**. This is author analysis of AP-006-A/B/C in AP-CANDIDATES-006, not independent review, proof acceptance, candidate admission or AP selection. Baseline: activated AS-REV-002, D001, F-DISPOSITION-003's scoped acceptance of F-DRAFT-003 P1-P6, PD's T1/conditional T2 and D002. The existence of a proposal supplies no compliance evidence.

## Hard constraints before costs

Evidence notation: **CS** = conditional symbolic design rationale only, not verified behavior; **UNKNOWN** = candidate gate qualification unestablished. No host realization or target evidence was obtained. The following entries apply at full candidate/interface scope; none is a PASS. Conditional numeric operation counts below do not upgrade a gate.

| Gate and authority | A: raw tail | B: squared tail + total | C: upstream snapshot | Evidence still needed |
| --- | --- | --- | --- | --- |
| H1 exactness; D001 R1/A1 | UNKNOWN; CS direct 32-term reduction | UNKNOWN; CS tail-total invariant/update | UNKNOWN; CS reduction conditional on exact snapshot | Independent specification comparisons; arithmetic/transition analysis; C snapshot fidelity. T002-2. |
| H2 startup/reset; R2/Q4 | UNKNOWN; zero padded tail/order | UNKNOWN; zero tail and aggregate/order | UNKNOWN; jointly reset history, snapshot and ordinal context | Required boundary positions and reset exclusion, including in-flight outputs. T002-3. |
| H3 one exact indexed pair per event; R3/Q4 | UNKNOWN; RI rank refinement pending | UNKNOWN; RI rank refinement pending | UNKNOWN; RN exact external ordinal unavailable | Index-interface authority, event/result bijection, reset association, no silent loss. T002-4. No hard deadline inferred. |
| H4 invalid/fault behavior; Q6 | UNKNOWN; validate before local transition | UNKNOWN; validate before all coupled updates | UNKNOWN; validate before joint append/index advance | State/index invariance and explicit rejection; report observable faults, document unobservable ones and recovery limits. T002-5. |
| H5 owned RAM <=2048 bytes; R5/A4 | UNKNOWN; local tail plus all overhead | UNKNOWN; larger-value tail plus aggregate and overhead | UNKNOWN; all owned/shared client resources and possible snapshots | Ownership/lifetimes/scratch/callee/stack evidence; external exclusion cannot be presumed. T002-6. |
| H6 no hardware FPU dependence; R6/A3 | UNKNOWN; CS integer intent | UNKNOWN; CS integer intent | UNKNOWN; CS integer reduction, service/client dependencies unresolved | Dependency/build/execution evidence for claimed scope. No target selected. T002-6. |

No gate is established by the known input range or by a tail payload smaller than 2048 bytes. Unknown stack, queues, index state or service dependencies can block the entire candidate. Optimization gains never compensate for failure of H1-H6.

## F worksheet: model, RAM in bytes and ownership

Active vector is exactly `(RAM_peak, compute_effort, device_energy_consumption)` with compatible Pareto preferences. Electrical device energy is not the signal sum of squares. Flash/code footprint is **inactive, UNKNOWN**, without an adopted budget. No scalar weights, measured costs, MCU cycle estimates, hard WCET, power target or winning candidate are supplied.

Define symbolic allocation sizes in **bytes** under a later declared representation/model `m`: `b_x` raw-sample slot, `b_q` square slot, `b_S` tail-total slot, `b_E` reduction/result slot. Their value capacities must cover 12, 24 and 29 bits respectively; packing, object alignment and allocation overhead are additional model choices. These symbols are not actual build sizes. A packed theoretical bit count is not an implementation RAM result.

For candidate `c`, let `O_c` be order/control persistent bytes; `T_c` persistent transaction, queue, reset and index-association bytes; `S_c(t)` live non-stack scratch (including any transient input/result, stream staging, transport/library allocations and buffers not already counted); `K_c(t)` owned live call-stack bytes including callees; and `G_c(t)` shared/otherwise attributable allocations not already counted. Include every allocation once. Unknown ownership is not zero attribution. Where a numerator/index requires length-dependent storage, write `T_c(n)` or `S_c(t,n)` instead of assuming a constant. RI observer resources and RN numeral resources are explicit external dependencies; detector-owned parts stay in these local terms.

`RAM_peak_c(m) = max_t [P_c(t,m) + S_c(t,m) + K_c(t,m) + G_c(t,m)]`.

If all persistent payloads remain allocated, the following are conditional expressions, not proven upper bounds. If lifetimes change, use the maximum formula rather than silently asserting overlap savings.

| Candidate | Detector persistent payload included in `P_c` | Symbolic RAM_peak expression, bytes | Exclusively upstream-owned resources, excluded only on established ownership | Actual result / H5 |
| --- | --- | --- | --- | --- |
| A | `31 b_x + O_A + T_A` | `31 b_x + O_A + T_A + max_t(S_A+K_A+G_A)` | Publisher acquisition resources; any RI observer association/trace resources; any later RN adapter's external portion | UNKNOWN; expression must be <=2048 with evidence |
| B | `31 b_q + b_S + O_B + T_B` | `31 b_q + b_S + O_B + T_B + max_t(S_B+K_B+G_B)` | Same external responsibilities as A; no external numeric history in B-NUM | UNKNOWN; expression must be <=2048 with evidence |
| C | `O_C + T_C`; no retained numeric tail in C-DET | `O_C + T_C + max_t(S_C+K_C+G_C)` | C-HIST tail `31 b_x^U`, publisher control/validity, snapshots/retries/pinned copies, exact ordinal representation `I_U(n)`, service stack/buffers | UNKNOWN; no automatic exclusion of shared snapshots or client libraries |

For C, serial streaming may need only one sample's staging and an accumulator conceptually, but `S_C` is not assumed to equal `b_x+b_E`: framing, validation, result staging, transport and index data may add more. If concurrency permits `p` pinned snapshots, an outside term may scale with `p`; no approved bound on `p` is given. C's local memory savings are conditional on actual ownership, bounded live work and reviewed services, not the word “upstream.”

For any candidate, choosing a local explicit arbitrary-length `n` would add length-dependent storage at least for that representation and would reopen H5. Choosing a bounded word without a reviewed refinement leaves H3 unresolved. A trace-rank abstraction avoids claiming a stored numeral but still requires an accepted interpretation and an actual association interface. None of these possibilities is a completed index solution.

## F worksheet: typed compute expressions

Model `M0` is a serial, quiescent, fault-free valid event with a padded 31-entry tail, full recomputation for A/C, and an intact B invariant. It does not exploit startup zeros. Work classes are abstract exact operations, not instructions: `SQ_x` square, `ADD_E` total addition, `SUB_E` total subtraction, `RD_x/RD_q` local raw/square read, `WR_x/WR_q` local write, `ADV_31` cursor/order advance, `FETCH_x` one externally supplied tail entry, and `OPEN_SNAP` snapshot session. Entries with different types are not interchangeable prices. Widening, packing and loop/address/control work belong to explicit overhead terms, not fabricated zero costs.

Let `V_c` be validation work; `J_c` index/association work; `D_c` response/acceptance coordination; `L_c` other control, addressing, representation conversion and staging work. Each is an **UNKNOWN typed vector**, not a scalar constant. C's validation includes snapshot consistency checks as well as current-value validation.

| Candidate | Conditional detector work per valid event under M0 | Separate outside work |
| --- | --- | --- |
| A | `32 SQ_x + 31 ADD_E + 31 RD_x + WR_x + ADV_31 + V_A + J_A + D_A + L_A` | Publisher acquisition and association/consumer work UNKNOWN |
| B | `SQ_x + ADD_E + SUB_E + RD_q + WR_q + ADV_31 + V_B + J_B + D_B + L_B` | Publisher acquisition and association/consumer work UNKNOWN |
| C | `32 SQ_x + 31 ADD_E + OPEN_SNAP + 31 FETCH_x + V_C + J_C + D_C + L_C` | Accepted-tail maintenance, snapshot consistency/retention, data delivery and RN ordinal generation/serialization UNKNOWN |

Read/write widths and transport sessions matter: 31 `FETCH_x` entries could share one transaction; this table does not assert 31 independent round trips. Local and external read costs are different types. Likewise B's square reads/writes can be wider than A's raw reads/writes. No count assumes one MCU cycle per operation or hardware multiplication availability.

| Event class | A | B | C |
| --- | --- | --- | --- |
| Startup valid events | Same padded work as M0 if padding physically represented; alternate validity optimization unchosen | Same M0 work if zero invariant established | Same reduction if zero-padded snapshot supplied; service validity work UNKNOWN |
| Initialization/reset | Establish 31 zero raw positions, order and association; physical work `R_A` UNKNOWN | Establish 31 zero square positions, zero S, order and association; `R_B` UNKNOWN | Joint history/snapshot/index reset and local cancellation/association work `R_C`, outside `R_U` UNKNOWN |
| Invalid attempt | `V_A^bad + report_A`; no sequence transition | `V_B^bad + report_B`; no sequence transition | `V_C^bad + report_C` plus coordinated no-append/no-index-advance obligations |
| Observable fault/stall | `F_A` UNKNOWN; report, no invented recovery | `F_B` UNKNOWN; report, no invented recovery | `F_C` and upstream `F_U` UNKNOWN; no loss-padding or service guarantee |

For a workload `w` over interval `Delta` with `N>0` accepted events, `N_bad` invalid attempts, `N_reset` resets and specified fault occurrences, the detector's amortized typed vector is

`Compute_c(w,m) = [sum_valid C_c(event,m) + sum_bad B_c(attempt,m) + sum_reset R_c(reset,m) + sum_fault F_c(fault,m)] / N`.

Frequency, concurrency, stalls and reset/fault distributions are UNKNOWN. Mean work, observed maximum and justified upper bounds are different quantities; none is measured here. For `N=0`, report total interval work, not joules/accepted-event or work/accepted-event with a zero denominator. Nominal 1 ms cadence is only a labeled possible workload scenario.

## F worksheet: attributable electrical device energy

For a common pinned target/accounting scope, a possible conditional model is

`DeviceEnergy_c(w,m) = [sum_j epsilon_j(m) * N_c,j(w,m) + E_baseline_attr,c(Delta,m) + E_wait_attr,c(w,m) + E_transport_attr,c(w,m) + E_other_attr,c(w,m)] / N` joules per accepted event.

`N_c,j` includes relevant lifecycle, invalid and fault operations. Coefficients `epsilon_j`, baseline attribution, wait behavior, transport energy, residual effects, uncertainty and coverage are all **UNKNOWN**. Allocation must avoid double counting transport work already priced in `epsilon_j`; additive operation pricing itself needs validation. Communication, memory traffic and waiting need not track arithmetic counts. This expression supplies neither measured energy nor a power target.

Report upstream history/index/acquisition energy separately as `E_U,c`, with component/device ownership and attribution UNKNOWN. If an upstream component runs on the same device, accounting must resolve its attributable device cost rather than silently excluding it with the RAM ownership rule. A detector-only device scope, whole-device scope and multi-device service scope are **incomparable** until reconciled. External service energy is not zero merely because it is outside local RAM. No claim of overall Pareto dominance follows from any table here.

## Conditional comparisons and counterexamples

Write `h_c = O_c+T_c+max_t(S_c+K_c+G_c)` in the fixed-lifetime RAM model. Under common ownership and compatible representations, B minus A RAM is `31(b_q-b_x)+b_S+h_B-h_A`. B uses more RAM only where this expression is positive; overhead or representation differences may change the sign. C's local RAM is below A only where `h_C < 31 b_x+h_A`, after all owned/shared allocations are included. These are conditional inequalities, not fit or eligibility results.

Within M0's arithmetic projection only, B uses fewer squares/additions than A and introduces one subtraction. To compare scalar compute cost one would need a common operation-cost model. For example, ignoring no terms silently, B has lower instantiated detector compute only where

`31 c_SQ + 30 c_ADD - c_SUB + 31 c_RDx - c_RDq + c_WRx - c_WRq + cost(V_A+J_A+D_A+L_A) - cost(V_B+J_B+D_B+L_B) > 0`.

Here `c_*` and each overhead cost are UNKNOWN under that hypothetical common model. A/B cursor costs cancel only if truly equal. This condition is not a measured-cycle result, an adopted scalar F, or full-vector dominance. C shares A's reduction counts but substitutes external reads and service coordination; that change can outweigh any local-memory saving. Without compatible targets, services and workloads, compare those domains as **incomparable**, not tied.

| Tempting shortcut | Counterexample / unresolved case | Consequence |
| --- | --- | --- |
| Retain only the latest energy/total | Two 31-entry tails `(1,0,...,0)` and `(0,1,0,...,0)` have equal totals and equal next energy with a zero continuation's first sample; the second zero continuation expires different entries and separates outputs | Order and the full latest-31 distinctions matter; total alone fails. These are 31-entry tails, consistent with D002's clarification. |
| Keep the oldest member of a full 32-window for all future behavior | Two histories differing only at that oldest member may have different already-emitted energy but identical padded latest-31 tails | T1 concerns nonempty future numeric outputs, not the current output or complete interface. |
| Any valid-width arithmetic works | Narrow multiplication before widening, or B subtracting an unrelated/incorrectly reset square, yields overflow/underflow or wrong totals | Range bounds do not prove arithmetic/transition correctness. |
| Zero is a harmless substitute | Inserting zero for an invalid attempt, service loss or missing sample advances the sequence and changes expiration/index association | Only pre-sequence padding is authorized; H2/H4 and possibly H1/H3 fail under that shortcut. |
| A/B local history solves the interface | A finite counter wraps while a valid sequence continues; responses may still have correct energy but wrong `n` | H3 remains unresolved without an accepted exact refinement; no forced reset authorized. |
| RN can use acquisition sequence numbers | An invalid acquisition followed by a valid one makes acquisition count differ from accepted ordinal | Index service must track acceptance, not all attempts. |
| C reads any 31 valid samples | A concurrent overwrite mixes two snapshot versions; every entry is in range but the sum belongs to no accepted window | Range checks do not supply snapshot consistency or ordering. |
| Reporting a service fault completes an accepted event | Snapshot eviction after acceptance leaves no exact result available | Fault reporting is necessary where observable but does not replace H3; retention/availability coordination remains blocking. |
| Small local state beats T2 | C's next outputs consult retained upstream history | The local state is not a closed complete-state boundary. No local 47-byte inference is valid. |
| External index removes numeric history needs | At one fixed `n`, distinct tails still have distinct possible future numeric behavior | Index association alone does not discharge T1/T2 numeric distinctions. |
| Arithmetic saving proves energy saving | Wider memory traffic, different wait states, index work or communication/baseline costs dominate | Energy and full compute coordinates stay UNKNOWN. |
| Nominal arrivals imply capacity or WCET | A stalled consumer/history service allows pending valid work to accumulate | Need later delivery/queue evidence; neither a 1 ms deadline nor infinite buffering is approved. |

## PD, D002 and T002 crosswalk

| Source obligation | A | B | C | Status / remaining evidence |
| --- | --- | --- | --- | --- |
| PD T1 | Ordered raw latest-31 tail | Injective square-tail representation; aggregate alone insufficient | Ordered tail retained/read in C-HIST | Accepted mathematical scope only; not a proof of these transitions, current output or metadata |
| PD T2; D002-4 | Conditionally closed A-NUM, no replay | Conditionally closed B-NUM, no replay | Local C-DET is replay-open; larger closure unestablished | Fixed `n>=32`, deterministic complete numeric state, unrestricted futures required; 372 bits/47 octets is capacity minimum only |
| PD PO-003-1 / PO-003-3 | No proof adopted | No proof adopted | No proof adopted | Both remain UNPROVEN; no new impossibility or index theorem asserted |
| D002-1 | Observable pair via RI only if authorized | Same | Exact RN decoding if service established | No narrowed sequence domain, bounded epoch, wrap or preapproved index service |
| D002-2 | Raw tail/order/transient/result/association inventory | Square tail/aggregate/order/transient/result/association inventory | C-DET plus C-HIST snapshot/history/reset/index inventory | Retention, validation, failure and refinement disclosures are proposals, not reviewed contracts |
| D002-3 | All local allocations plus attributable shared costs | Same, including redundant aggregate | Outside exclusion only for exclusively upstream-owned resources | Ownership/lifetimes/scratch/stack remain UNKNOWN |
| D002-5 | RI ambiguity; RN alternative dependency if needed | Same | Snapshot and RN contracts absent | New D003/additive AS clarification before concrete index/service or operating restriction commitment |
| D002-6 | H/F worksheet above | H/F worksheet above | H/F worksheet above | Compatible costs only; all obligations retained |
| T002-2 / H1 | Direct reduction against independent specification | Incremental invariant and results against independent specification | Snapshot fidelity plus reduction against independent specification | OPEN; boundary and randomized streams later |
| T002-3 / H2 | Tail/order reset | Tail/S/order reset | Cross-component reset and stale snapshot/result exclusion | OPEN; zero, first, 31st, 32nd, 33rd and restarted sequences |
| T002-4 / H3 | RI association and one response/event | Same plus coherent aggregate commit | RN accepted ordinal, snapshot and response agreement | OPEN; no latency bound invented |
| T002-5 / H4 | Rejection invariance, observable reports | Same across coupled state | Same across detector and history/index owner | OPEN; no unobservable-fault guarantee or recovery policy invented |
| T002-6 / H5/H6 | Owned resources and no-FPU dependency evidence | Same, including aggregate and square representation | Same, including client/service ownership and dependencies | OPEN; conditional numeric bounds are not build/RAM evidence |
| T002-7 / compute and device energy | Target/workload/attribution characterization | Same | Same plus service/communication scope reconciliation | OPEN; target/toolchain, measured timing/energy and uncertainty absent |
| T002-8 / R4 | Primitive output only | Primitive output only | Primitive output only | OPEN/DEFERRED; threshold, duration, boolean decision and integration verification required before whole-detector claim |

## Blocking clarifications and later gate

These are questions for the sponsor-delegate and later independent feasibility work, not authored D003 decisions or completed contracts:

1. **Exact index interface, all candidates:** does RI's ordered request/response rank supply the required logical index, or must a numeral be physically delivered? What reset/consumer-lifetime evidence makes association exact? If a numeral is required, who owns its potentially growing state and transport? Neither finite epochs nor bounded counters nor an external service are approved. D003/additive AS clarification is needed before a concrete commitment; changing the accepted behavior requires separate authority.
2. **Acceptance and publication coordination, all candidates:** how are valid arrival, acceptance, history change and one required response coordinated through stalls/reset/failure? What backpressure and buffering contract is acceptable without dropping otherwise-valid events or inventing a deadline? Fault reporting alone is not a recovery/omission policy. This blocks a complete physical-interface commitment, not generation of these conditional proposals.
3. **Publisher-history and RN service, especially C:** is a new service authorized and realizable? Who guarantees exact ordered snapshots, accepted-event counting, retention, reset consistency, access, concurrency and observable fault reporting? A normal publisher is not evidence of these guarantees. New reviewed contracts and authority are needed; exhaustion restrictions or changed accepted input behavior require AS clarification as appropriate.
4. **Ownership and measurement scope:** which buffers, shared/pinned allocations, libraries, index resources and stacks are detector-attributable? What device-energy attribution and compatible workload/target model will be used? Preserve R5 rather than excluding costs by location/name. If F definitions must change, use a new versioned decision; no alteration is made here.

Recommend later independent feasibility analysis of **all three** with these questions visible: A for direct history reconstruction, B for redundant-state versus arithmetic tradeoffs, and C for the separate ownership/replay/service problem. C's service investigation is prerequisite to any claim of local-memory advantage. Resolve blocking index/contract questions before freezing a physical interface; keep alternatives reversible. No candidate is admitted, rejected as an entire architecture, ranked as a Pareto winner, or selected here.
