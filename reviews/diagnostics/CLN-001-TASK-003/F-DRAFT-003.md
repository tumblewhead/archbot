# F-DRAFT-003 — Proposed Figure of Merit

Status: **DRAFT_FOM_NOT_ACCEPTED_OBJECTIVES**. This is a fresh candidate F for the CLN-001 synthetic numeric primitive, not acceptance of F, an architectural proposal (AP), a feasibility finding, proof, implementation, or target qualification.

## Baseline and authority

The baseline is AS-REV-002 as activated by AS-ACTIVATION-002, grounded in D001 and original BKP-NEED-001, BKP-ADC-001 and BKP-TARGET-001. The activation record establishes diagnostic acceptance despite older draft/pending language retained in AS-REV-002 and DECISION-TRACE-002. Its recorded historical activation checks are supplied provenance, not checks independently repeated here. No historical paths or repositories were consulted.

D001's requirements authority is limited to this synthetic diagnostic and does not transfer to this author. The hard requirements below restate that authority. All F structure, metric definitions, evidence categories and comparison rules labeled P1–P6 are **new proposals for review**, not new accepted requirements. No new numeric acceptance threshold is proposed.

## Authorized hard constraints, outside the optimization vector

Each gate's current candidate compliance is **UNKNOWN**: no AP or implementation is supplied. A requirement's known limit is distinct from evidence that a realization meets it.

| Gate | Authorized requirement and model | Required evidence and claim boundary |
| --- | --- | --- |
| H1 Exact observable energy | R1/A1 and Q4: accepted unsigned samples are in [0,4095]. For each initialized/reset sequence, output `(n,E_n)` for every accepted event, with `E_n = sum(x_(n-k)^2, k=0..31)` and specification-only `x_j=0` for `j<=0`. Exact integer equality is required; approximation error is not an optimization axis. | T002-2: independent specification comparisons on boundary and randomized streams at later authorized functional verification, before correctness claims. Tests support only their demonstrated scope; no proof is asserted. |
| H2 Startup and reset | R2/Q4: only absent pre-sequence positions contribute zero. Reset excludes all earlier sequence history. Mathematical initial energy is zero; pre-first-event publication is optional. | T002-3: zero history, first, 31st, 32nd, 33rd accepted events and reset restart/prior-history exclusion, at later lifecycle verification. |
| H3 Event/output association | Revised R3/Q4: one logically new exact energy and associated logical accepted-sample index per valid accepted sample. A logical index does not prescribe a stored counter or timestamp. Nominal 1 ms arrivals impose no hard WCET, latency, jitter or wall-clock publication bound. | T002-4: event/output count and association checks at later interface/functional verification. Separate performance evidence is needed before real-hardware operation claims. |
| H4 Invalid inputs and applicable fault reporting | Q6: out-of-domain values explicitly expose rejection or precondition violation, without changing state/history/index or conversion to zero. Publisher owns acquisition timing; accepted order has no omissions. Duplicates, gaps and out-of-order delivery are outside the accepted contract; detectable faults must be reported. No detection guarantee without observability, recovery policy, or operational-loss padding is added. | T002-5: invalid-input checks and reporting checks for faults observable through the eventual interface; document detection limitations before input-contract compliance claims. |
| H5 RAM ceiling | R5/A4: detector-attributable RAM at most **2048 bytes**, including owned persistent state, working scratch and owned call stack. Exclusively upstream-owned memory is excluded. This is a hypothetical model bound, not measured fit. | T002-6: exact ownership/accounting and resource evidence at later authorized realization/verification; target evidence before target-compliance claims. Shared ownership and overlapping lifetimes require explicit accounting, not silent exclusion. |
| H6 Hardware independence | R6/A3: no hardware FPU dependency under the generic 32-bit Cortex-M-class/no-FPU model. No algorithm, representation, data structure or software-floating-point ban is inferred. | T002-6: dependency analysis and appropriate build/execution evidence for the claimed environment at later realization/verification; target evidence before target-compliance claims. |

R4 is an unresolved integration obligation, **not a primitive completion gate or optimization score**. Threshold, duration and boolean detection criteria must be specified and verified before any whole sustained-energy detector completion claim (T002-8). Passing primitive gates would not discharge R4 or qualify a complete detector's resources.

## P1 — Proposed objective vector and unquantified interests

Propose `F = (RAM_peak, compute_effort, energy)` subject to H1–H6. R5 authorizes qualitative conservation, not numeric compute/power thresholds or weights. These coordinates become comparable numbers only under explicit compatible models and evidence. The RAM objective adds a proposed minimization preference within the existing ceiling; reducing RAM never compensates for a failed gate.

| Axis / interest | Unit and direction | Allowed model | Source | Admissible evidence | Current value | Due stage for real target claim |
| --- | --- | --- | --- | --- | --- | --- |
| RAM_peak | bytes; minimize, subject to H5 | Peak detector-attributable live RAM, with owned persistent/scratch/stack accounting and explicit lifetimes; synthetic symbolic or concrete target model | BKP need conservation; BKP target; D001 R5/A4; AS R5 | Conditional accounting first; later build/map, ownership, stack bounds or appropriately scoped measurements. Host figures remain host evidence; observed stack peaks alone do not establish an all-path bound. | **UNKNOWN**; authorized ceiling is 2048 bytes | T002-6, before target RAM-compliance claims |
| compute_effort | Qualitative until model fixed; operation counts by operation class for symbolic work; cycles/accepted sample or time/accepted sample for a defined target; minimize within each declared model | Exact workload/event classes and cost model; distinguish ordinary, startup, reset, invalid and fault paths as applicable. Counts of different operations are not interchangeable target costs. Mean, maximum observed and justified upper bounds are separate statistics. | BKP need conserving compute; D001 R3/R5/A2; AS R3/R5 | Explicit symbolic expressions and assumptions; later reproducible target timing/cycle evidence, with workload, toolchain and measurement method | **UNKNOWN** | T002-7, before real-hardware operation/qualification claims; no approved performance threshold |
| energy | Qualitative until measurement model fixed; joules/accepted sample over a declared workload and accounting interval; minimize | Detector-attributable energy with explicit attribution, baseline, activity and averaging policy. Interval includes relevant lifecycle/fault work. Nominal cadence may be a labeled scenario, not a delivery guarantee. | TASK-FOM-003 qualitative energy/resource aim; D001 R5's absence of numeric power threshold; original resource/compute conservation context | Conditional energy models only with stated coefficients and limits; later attributable target energy measurements with uncertainty and workload. Operation counts alone do not establish energy. | **UNKNOWN** | T002-7 at later authorized target characterization, before target energy claims |
| Flash/code footprint — unresolved resource interest, not active F coordinate | bytes; proposed preference to minimize only if later adopted | Detector-attributable code/read-only footprint with linked library attribution and build settings | Broad TASK resource aim; D001 specifies no flash limit/objective; BKP target supplies no flash budget | Later scoped build/link evidence if adopted; no footprint asserted now | **UNKNOWN** | Before any target flash-fit claim; authority must first settle relevance and any limit |
| Full sustained-energy detection — deferred function, not an optimization coordinate | Unit/direction **UNKNOWN**; threshold and duration undecided | Future integration contract, outside primitive scope | Original BKP R4; D001 R4; AS R4 | Later authorized criteria and integration verification, not primitive output evidence alone | **UNKNOWN** | T002-8, before complete-detector claims |

Energy normalization and compute statistics are proposed reporting definitions, not accepted numeric objectives. No power, latency or flash constraint is silently added. The tradeoff between operation classes, between runtime statistics, and between axes remains unresolved; do not compress them into a fabricated scalar.

## P2 — Symbolic accounting and evidence maturity

For a future candidate `c`, use conditional expressions such as:

`RAM_peak(c,m) = max_over_allowed_execution_points [P_live(c,m) + S_live(c,m) + K_owned_live(c,m)]`.

The terms describe accounting categories, not a storage or execution design. Include owned allocations and library/callee contributions in their appropriate categories, avoid double counting, and justify permitted overlaps. If lifetimes are unknown, the peak remains UNKNOWN; a stated conservative sum of proven component bounds may instead provide a conditional upper bound. Unknown stack or scratch is never zero.

Compute may be expressed as `C(c,w,m) = sum_j N_j(c,w,m) * cost_j(m)` plus explicitly modeled overhead. Unresolved costs remain symbolic. Energy may be expressed as an attributed workload function with unknown target coefficients. No coefficients, resource sizes or target counts are supplied here.

Propose these evidence categories, each retaining environment, scope and assumptions:

1. **Requirement/model:** a limit or behavior is specified; this is not candidate evidence.
2. **Conditional symbolic analysis:** an expression or bound follows only under declared assumptions; it may support a conditional comparison, not measured fit.
3. **Host evidence:** measurements/tests concern the stated host and build; no automatic target transfer.
4. **Target evidence:** measurements or justified bounds concern a pinned device, build, configuration and workload, with uncertainty and coverage limits.

An observation is not a universal bound, and a bound is not a measurement. These categories are not automatic acceptance levels. Later target values instantiate or test the same RAM, compute and energy definitions; they do not change conservation objectives or turn nominal 1 ms into a deadline. If metric definitions must change, version the proposed F, seek disposition and recompute comparisons rather than silently changing the objective.

## P3 — Uncertainty and gate policy

Use **SUPPORTED**, **CONTRADICTED**, or **UNKNOWN** for each candidate gate, qualified by evidence category and claim scope. These labels are proposed bookkeeping, not acceptance decisions. Missing, incompatible, conditional-but-unestablished or inadequate evidence remains UNKNOWN. No UNKNOWN becomes PASS, zero, infeasible, or a favorable tie. All gates are currently UNKNOWN; all T002 obligations remain open.

A conditional symbolic RAM bound within 2048 bytes may support a model-scoped conditional statement only. Target compliance requires target-scope evidence. A measured value below the ceiling does not establish unexamined paths. Evidence contradicting a hard gate prevents eligibility for that scope; optimization gains cannot compensate. Unknown eligibility permits further investigation, never a feasibility or completion claim.

## P4 — Reversible comparison rule, without AP selection

For eventual AP candidates, record a versioned comparison sheet containing baseline/F revision, candidate identity, gate evidence, axis expressions/values, model parameters, provenance, uncertainties and unresolved assumptions. This draft supplies no candidates or implementation sketches.

Compare constraints first for the stated evidence scope. Keep candidates with unresolved gates visible as pending rather than declaring them compliant or discarding them as failures. For candidates with adequately supported gates, use a **Pareto partial order** over mutually comparable F coordinates: A dominates B only when A is no worse on every active coordinate and strictly better on at least one, under the same stated model and evidence scope. Unknown coordinates prevent a full dominance claim; projection onto known coordinates must be explicitly labeled partial, not an overall ranking.

For symbolic expressions, dominance must hold throughout the declared parameter domain; otherwise show conditions/regions or leave candidates incomparable. For bounded uncertain values, claim dominance only if bounds justify the relevant inequalities; overlapping uncertainty remains unresolved. Do not mix a host measurement with a target estimate or different workloads as if equivalent. No weights or tradeoff coefficients are supplied, so incomparable candidates remain alternatives. Equal measured coordinates do not establish equal behavior or evidence coverage.

When target evidence arrives, reevaluate the same definitions and assumptions and retain prior conditional results with their scope. A changed target/workload can reverse comparisons without changing the objectives. Preserve revisions and reasons; no irreversible architecture choice follows from this F draft. Any eventual selection requires separate authority and authorization after F review; this author selects no AP.

## P5 — Missing comparison information and scope

No APs, device, compiler/linker/options, runtime/library configuration, stack/call paths, memory ownership details, workload distribution, measurement protocol, energy attribution method, metric tradeoffs or selection preferences are supplied. Numerical RAM/stack/flash/cycles/runtime/energy/power values are UNKNOWN. Measurement uncertainty and coverage are also UNKNOWN. No numeric target feasibility or measured fit is established.

## P6 — Trace crosswalk and exit

| Obligation | F coverage | Open evidence / due boundary |
| --- | --- | --- |
| T002-2 | H1 exactness; excluded from optimization tradeoffs | Independent boundary/randomized specification comparisons before correctness claims |
| T002-3 | H2 startup/reset | Required event positions and sequence restart checks at lifecycle verification |
| T002-4 | H3 per-event logical association; compute evidence separate | Functional association checks; no added time bound |
| T002-5 | H4 invalid values and observable faults | State/index invariance, explicit rejection and applicable reporting checks before compliance claims |
| T002-6 | H5/H6; RAM coordinate; P2 accounting | Ownership, scratch/stack evidence and hardware-dependency evidence; target evidence before target claims |
| T002-7 | Compute/energy coordinates; P2–P4 evidence/comparison | Target/toolchain/workload and separately reported timing/resource/energy evidence before relevant target claims |
| T002-8 | R4 exclusion and unresolved integration entry | Detection criteria and integration verification before whole-detector completion |

All remain OPEN. F acceptance requires a distinct later review and authorized disposition; see F-TRACE-003. This draft ends at F specification and does not authorize later proof, AP selection or implementation.
