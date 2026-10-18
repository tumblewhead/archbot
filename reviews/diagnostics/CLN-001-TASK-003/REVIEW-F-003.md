# REVIEW-F-003 — Independent candidate-F review

Disposition: **READY_FOR_DELEGATED_F_DISPOSITION**. This is draft readiness only. **f_accepted: false; proofs_accepted: false.** No architecture proposal or selection is made. The reviewer has no sponsor-delegate authority and cannot confer it on itself.

## Constraints and authority

H1/H2 faithfully retain exact latest-32 integer outputs, startup-only absent-history zeros, reset exclusion of earlier history and optional pre-first publication. H3 preserves one logical indexed output per accepted event; it adds no stored-counter requirement, hard WCET, jitter or target throughput threshold. H4 retains explicit invalid rejection/precondition exposure with state/history/index invariance and reporting of observable delivery faults, without adding recovery or unobservable-fault guarantees. H5 retains at most 2048 bytes including owned persistent state, scratch and owned call stack, excluding exclusively upstream-owned memory. H6 preserves hardware-FPU independence without banning software floating point. No blocking inheritance defect was found.

P1 explicitly proposes **F=(RAM_peak, compute_effort, energy)**. Those are proposed objectives, not accepted requirements. Two authority decisions must be explicit before binding F disposition:

- **Energy as an active axis needs a new objective decision.** The BKP asks to conserve RAM and compute. Its sum-of-squares signal energy is distinct from consumed device energy. D001's absence of a numeric power threshold does not authorize energy minimization, and TASK-FOM authorizes draft exploration rather than adoption. The delegate must adopt, revise or defer this axis, with scope/model recorded. If deferred, version the active vector and affected comparisons.
- **RAM minimization within the ceiling needs explicit F adoption.** It has direct qualitative BKP conservation support, unlike a device-energy objective, but the 2048-byte ceiling alone does not establish a binding Pareto preference below that limit. Adopting this formal preference can occur through delegated F disposition without changing the R5 ceiling.

These are required authority actions, not reviewer approvals or demands to rewrite the current clearly labeled draft. P1/P2 and F-TRACE expressly identify new proposals, and the exit requires an authorized versioned disposition of new objectives. That makes the candidate ready to present for that decision; it does not mean its axes are already approved. Compute conservation has qualitative support but its metric/statistic/model also remains subject to F disposition. No new hard compute, power or deadline threshold is approved.

## Accounting, evidence and comparison

RAM_peak uses bytes with minimization subject to the ceiling. P2 accounts for simultaneously live persistent/scratch/owned-stack storage, allocations and callee/library contributions; overlapping lifetimes need justification and unknown stack is never zero. A conservative sum of established bounds is distinguished from a measured peak and from an exact live maximum.

Compute uses operation-class counts or scoped cycles/time per accepted sample. Counts with different costs are not interchangeable; means, maximum observed values and justified bounds are separate. Proposed consumed energy uses joules per accepted sample with workload, baseline, attribution and interval declared, including relevant startup/reset/invalid/fault work. No target, cost coefficients, statistic, measurement protocol or energy attribution is fixed. Energy reduction cannot be inferred from fewer operations. All numerical axis values remain UNKNOWN; no fabricated RAM, stack, cycles, energy, power or flash measurements were found. Flash remains outside the active vector.

The proposed rule evaluates hard gates first; optimization cannot offset failure. Missing eligibility remains pending, not compliant or failed. SUPPORTED/CONTRADICTED/UNKNOWN is qualified by evidence scope. Conditional symbolic results, host evidence and target evidence do not automatically transfer. Measurements do not establish all-path bounds.

Pareto dominance requires no-worse values on every active comparable coordinate and a strict improvement on at least one. An unknown coordinate prevents full dominance; projections remain explicitly partial. Symbolic claims require the declared parameter domain; uncertain inequalities need supporting bounds. Incompatible workloads, statistics, environments and host/target evidence are not ranked as equivalent. No scalar weights or total ordering are invented. Versioned definitions and recomparison protect against changing objectives when target evidence arrives. The rule is adequate as a proposal pending authority disposition and metric instantiation.

## Obligation crosswalk

| Open item | Candidate coverage | Remaining claim boundary |
| --- | --- | --- |
| T002-2 | H1 | Independent numeric specification comparisons before correctness claims |
| T002-3 | H2 | Startup positions and reset/history exclusion verification |
| T002-4 | H3 | Per-event logical index association; no invented deadline |
| T002-5 | H4 | Invalid-state invariance, explicit rejection and applicable fault reporting |
| T002-6 | H5/H6, RAM/P2 | Complete ownership/lifetime/stack and dependency evidence; target scope before target compliance |
| T002-7 | Compute and proposed energy, P2-P4 | Later scoped target/toolchain/workload evidence; energy evidence if claiming energy; no mandatory power threshold inferred |
| T002-8 | Explicit R4 exclusion and integration register | Detection criteria, threshold, duration, decision and integration verification before complete-detector claims |

All remain OPEN. Primitive correctness or F disposition cannot discharge full sustained-energy detection or establish the whole detector's resource compliance.

## Receipt and next gate

The review compared H1-H6, P1-P6 and both draft traces against D001, the three BKP files and activated AS/TRACE. It checked units, accounting, unknown handling, compatible-model requirements and each T002 row. All 14 manifest entries checked OK; no measurements, implementation or AP comparisons were performed. ACT-002 establishes the supplied accepted synthetic baseline despite retained earlier draft text; its historical referenced evidence was not retrieved or independently authenticated.

Next gate: the authorized diagnostic sponsor-delegate must explicitly adopt, revise or defer the proposed objectives, especially consumed energy and within-ceiling RAM minimization, and issue a versioned F disposition. This review grants no authority or subsequent AP/implementation authorization.

The single review invocation authored neither product and acts only as Stage-3 reviewer. Only AGENTS.md, TASK.md and allowlisted inputs were accessed; no old solutions, Git history, other workspaces, external sources, connected systems or hidden evaluator. Hash consistency is not authenticated isolation or independent historical evidence. cleanroom_qualified: false; product_verified: false; vo_discharged: []; f_accepted: false; proofs_accepted: false.

### Supplied source hashes

| Input | SHA-256 |
| --- | --- |
| `PO-OPPORTUNITIES-003.md` | `088f079a0d1476f65722eb3bd6e207333412dbbec985764e1864171495c3ccd9` |
| `PO-BRIEFING-003.md` | `1d45d40c5328b16514fc1bd5a1396110cb8be055c4a80a88b1c2bef09644d9e2` |
| `DECISION-001.yaml` | `1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36` |
| `adc.md` | `284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7` |
| `TASK-FOM-003.md` | `318e5abed7b31cd453ed9b99ab707477f1312f313827aa95d74ecbba93cd8b58` |
| `TASK-PO-SCOUT-003.md` | `320f14fc20e3aabc35a09ad09c6c2e59458e60674ddc9e80adcb0ed6739a3ee3` |
| `AS-REV-002.md` | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` |
| `verification-agent.md` | `7f6463b5a54278230dbd73c5f49fc68cb4192ca83c48de191b22674f8d3ae1f3` |
| `DECISION-TRACE-002.md` | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` |
| `problem-origin.md` | `90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333` |
| `F-TRACE-003.md` | `9855a2d82f707257e5870dfe53738a13c86ee7810ee5ba9cda1065622952c67e` |
| `F-DRAFT-003.md` | `9b74bac301e917fbee0f28b246b67a39dc308e66ab808353d3097601915b6a59` |
| `target.md` | `c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64` |
| `AS-ACTIVATION-002.yaml` | `d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c` |
