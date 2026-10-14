# VS-001: Worked and adversarial design of the verification stages

**Date:** 2026-10-14  
**Base:** `10aa677ca6ac58924d1f948333eacbdfdb22659a`  
**Status:** Design study; self-adversarial review, not independent acceptance.  
**Scope:** ERS derivation, verification-rung planning, execution/evidence adjudication. No changes to installed operations, the live runner, product requirements, or VO states.

Companions: [Theory of Verification](THEORY_OF_VERIFICATION.md), [Verification Framework Requirements](VERIFICATION_FRAMEWORK_REQUIREMENTS.md).

## Result

Implement a bounded vertical slice across all three stages, centered on a **small typed evidence checker**. Do not begin with a universal symbolic solver or three document-generating agents whose outputs are accepted by prose review alone.

The intended chain is:

> Accepted claims -> verification-facing ERS -> typed experiment plan -> executed evidence -> checked scope-limited conclusions.

The study worked three different examples: exact rolling arithmetic, coupled queue demand, and statistical calibration. Twenty-two adversarial failure mechanisms were examined. Several forced design changes; the remaining boundaries are explicitly acknowledged below rather than dismissed as absurd.

## Execution and evidence limits

Small standalone Python mathematical/reference probes were executed. No Archbot test suite, repository C build, target build, or hardware simulation was executed by this study. Results below are **not** independent verification or a VO discharge.

Executed checks included 4,096 one-step transitions for each of six reduced-ring variants; four queue-envelope corner calculations; a discrete queue-overflow witness; a pairwise covering suite with a hidden triple; analytic Gaussian coverage; exact zero-failure statistical bounds; and ten proposed result-type classification cases. The latter test a design contract, not a solver implementation.

The uploaded ERS and verification-plan examples supply claim-first framing, evidence isolation, rung themes, ablation, replay and non-claims. Their battery-specific thresholds are not imported. Their original source hashes are `ad5db37d4b2ceb31d58894ced1ce9de9f285d515f96e5a6dd334507a763e44b8` (ERS) and `a86cb527d2906a88023ebc17333a073acf044be9db30f2244a1dc991b492ff12` (plan). They remain external attachments, not a complete archived reference package here.

## Breadcrumb 1: ERS must not let the code define its examination

**Candidate:** generate an ERS from accepted design plus implementation.

**Attack:** accepted requirements include reset, newest-window behavior and legal arithmetic. Buggy code omits reset; a code-centered ERS omits reset too. Every emitted requirement has a source, yet a real requirement is untested.

**Repair:** separate normative extraction from observed implementation behavior. Require bidirectional coverage: every normative ERS claim has authority, and every applicable source obligation has an explicit disposition. Do not erase missing behavior or promote incidental code behavior into requirements.

A universal claim remains universal even when the currently available tests cover only a short trace. Natural-language-to-formal-model translation remains an explicit review obligation; source IDs alone do not prove semantic faithfulness.

## Breadcrumb 2: Evidence composition requires rules and compatible scopes

Arithmetic proved on `0..7` and ordering proved on `0..3` establish their conjunction only on `0..3`. Different properties generally combine on the domain intersection; the same property proved over distinct regions can combine over their union. Subject, semantics and assumptions must agree or have a checked bridge.

An empty domain, such as `x>=1 and x<=0`, makes a counterexample query unsatisfiable. That is vacuity, not meaningful application safety. Check domain consistency/applicability separately from failure-query satisfiability.

P supported by Q and Q supported by P is an ungrounded cycle, not a proof. Induction is different: it supplies initial-state and transition-preservation obligations under an explicit rule.

The initial evidence rules should be few: scope restriction; conjunction; same-property domain union; implication through checked correspondence; induction; admissible counterexample refutation; and explicitly modeled statistical inference. No rule promotes finite tests into arbitrary universal safety.

## Breadcrumb 3: Exact rolling arithmetic through the three stages

### Stage 1: ERS

For Toy 1, N=32 and M=4095. From a valid initialized state and legal, serialized accepted calls, return the exact squared sum of the newest N accepted samples, with zero startup padding. Physical publisher continuity and unrestricted throughput are not established by this claim.

Split initial state, eviction/order, arithmetic, return behavior and implementation correspondence. A useful invariant is:

```text
0 <= r[j] <= M
0 <= i < N
S = sum_j r[j]^2
oldest-first history = (r[i], r[(i+1) mod N], ..., r[(i+N-1) mod N])
```

### Stage 2: plan

Check initialization; invariant preservation; magnitude and representation; independent finite reference cases; mutation; and a separate C/target correspondence argument. A diagnostic run may follow a failed run without assuming the failed claim true.

### Stage 3: result

Replacing `old=r[i]` with x gives `S'=S-old^2+x^2=sum_j r'[j]^2`. Advancing i preserves chronological order. Zero initialization gives the induction base.

For the original mathematical parameters:

```text
M^2       = 16,769,025
N*M^2     = 536,608,800
(N+1)*M^2 = 553,377,825 < 2^32
```

The add-first intermediate also fits the stated unsigned arithmetic model. This is not a target measurement or proof of compiler correctness.

The executable reduced example uses N=4, M=3: 256 histories, four oldest-index encodings and four next inputs, giving 4,096 transitions per variant. Its oracle shifts chronological history and recomputes the sum rather than copying the rolling recurrence.

| Variant | Mismatches |
|---|---:|
| Correct transition | 0 |
| Wrong eviction slot | 3,072 |
| Omit eviction subtraction | 3,072 |
| Return preceding result | 3,072 |
| Five-bit accumulator | 16 |
| Wrong index mask | 2,048 |

This checks the reduced finite model, not the full C binary. The generic induction argument and its implementation bridge are separate evidence.

**Attack:** independent ranges allow S=0, old=3, x=0, giving -9. The state is impossible because S includes old squared. A symbolic witness can identify an inadequate abstraction rather than a product bug. Include invariants/reachability or validate and refine the witness [S4].

**Attack:** removing casts before squaring can survive on a 32-bit-int implementation because 4095 squared fits signed 32-bit arithmetic. Under unsigned 16-bit multiplication it becomes 57,345. Classify an environment-sensitive mutant instead of demanding that every mutation fail everywhere. Integer promotions belong to the recorded semantics [S1].

## Breadcrumb 4: Passing every pair does not justify ignoring triples

Let failure be `a*b*c == 1` for Boolean parameters. The suite `000, 011, 101, 110` covers every value pair of every parameter pair. All pass; 111 fails. Pair sweeps with the third variable held at zero also pass. For J=abc, mixed pair derivatives at the origin are zero.

**Repair:** higher-order edges need two creation routes: evidence-guided promotion from observed pairs and model-guided creation from any shared formula, resource inequality, guard or mode. Higher-order coverage cannot depend on first finding a bad pair. NIST's higher-strength combinatorial testing is relevant here [S2].

An edge is more than parameter names: include joint constraints, state/trace semantics, a failure predicate, quantifier, horizon, approximation direction and source authority. Budgeted sparse exploration must retain uncovered regions/order as unknown, not silently claim completeness.

## Breadcrumb 5: Queue example through the three stages

All numbers are illustrative fixtures, not UART requirements. The boundary is batch enqueue after packet assembly, not instantaneous bits on a serial wire.

### Stage 1: ERS

Claim: initially empty queue occupancy does not exceed B under arrival envelope `alpha(t)=b+r*t` and service guarantee `beta(t)=mu*max(t-T,0)`. These must be valid interval/busy-period envelopes, not just measured average rates.

### Stage 2: plan and symbolic screen

For r<=mu, the maximum vertical difference is `b+r*T`: before T it increases; after T its slope is r-mu<=0 [S3]. Define margin `m=B-b-r*T`.

```text
dm/db = -1; dm/dr = -T; dm/dT = -r
d2m/(dr dT) = -1
utilization u = r/mu
reserve consumption v = (b+r*T)/B
```

The signs, units and product expose a dangerous interaction. A milliseconds-to-seconds error changes the calculation by three orders of magnitude.

### Stage 3: corners and witness

Set r=9000 bytes/s, mu=12000 bytes/s, B=256 bytes.

| Burst | Latency | Backlog bound | Fits? |
|---:|---:|---:|---|
| 64 B | 0 ms | 64 B | yes |
| 160 B | 0 ms | 160 B | yes |
| 64 B | 16 ms | 208 B | yes |
| 160 B | 16 ms | 304 B | no |

Every case has utilization 0.75. Either individual change fits; their combination does not satisfy the bound.

**Attack on our own conclusion:** an upper bound above capacity need not prove actual overflow if the bound is loose. Supply a feasible witness separately. A 160-byte initial enqueue, nine bytes each millisecond and no departures until 16 ms gives 250 bytes at 10 ms and 259 bytes at 11 ms. That is a concrete overflow witness in this abstract enqueue model.

Physical UART framing, line rate and packetization could invalidate that witness at a different observation boundary. Require correspondence before calling it a physical defect. Likewise, r>mu implies unbounded backlog only under an unbounded eligible horizon; a finite-duration test may finish before overflow.

## Breadcrumb 6: Statistical calibration through the three stages

This small estimator is not the battery example. Let `X_i=theta+b+epsilon_i`, epsilon iid N(0,1), fixed batch bias b, and fixed n.

### Stage 1: ERS

Distinguish coverage at b=0, coverage uniformly over a bias range, and coverage on the deployment population. A 95% procedure-level guarantee is not a posterior probability statement about one interval.

### Stage 2: plan

Compute model coverage, jointly sweep bias and sample count, then separately design deployment validation. Keep model assumptions, sampling units, tuning data, confirmatory data and stopping rules explicit.

### Stage 3: analytic result

For the naive interval `mean +/- z/sqrt(n)`, z=Phi^-1(0.975), coverage is:

`Phi(z-b*sqrt(n)) - Phi(-z-b*sqrt(n))`.

| n | b | Actual model coverage |
|---:|---:|---:|
| 4 | 0 | 95% |
| 4 | 0.3 | 90.7845% |
| 100 | 0 | 95% |
| 100 | 0.3 | 14.9161% |
| 400 | 0.3 | 0.0026721% |

These are analytic normal-CDF evaluations, not Monte Carlo or physical calibration evidence. More data narrows the interval while common bias persists. If a bound |b|<=B is genuinely justified, radius `B+z/sqrt(n)` gives a conservative model guarantee by the triangle inequality. It does not establish the physical bias bound.

For zero failures among n independent fixed-sample Bernoulli cases, the one-sided 95% upper limit is `1-0.05^(1/n)` [S5]: 25.8866% at n=10; 4.95076% at n=59; 2.95130% at n=100. Ten cases replayed ten times are still ten independent cases, not one hundred. Unique seeds also do not remove shared latent error.

Adaptive adversarial cases do not automatically estimate deployment risk. Repeatedly peeking until an ordinary fixed-sample interval passes invalidates naive confidence accounting. Use frozen independent validation initially; time-uniform methods are an optional later adapter [S6]. Report the denominator and acceptance rate: rejecting everything does not establish useful accepted-case accuracy.

## Breadcrumb 7: Execution and inference must be different objects

An UNSAT answer concerns its submitted formula, not the faithful encoding of a real system [S7]. With a checked property mapping, a sound overapproximation can transfer universal safety to the concrete system; its SAT witnesses may be spurious. No-failure results in an underapproximation or finite horizon do not establish arbitrary universal claims.

The ten executed classification fixtures covered: empty domain; unresolved domain; timeout; unchecked backend; bounded/unbounded scope mismatch; underapproximation; abstract-only witness; spurious witness; validated witness; conditional model safety. This is a small proposed type contract, not a trusted backend.

Record the actual source, model, oracle, generator, headers/configuration, build recipe, target semantics, tools and results. A source hash alone does not identify the tested binary. Hashes detect drift, not the truth of a fabricated receipt.

Require known failing controls and expected check counts where meaningful. Disabled assertions can produce successful process exit without performing intended checks. Separate-agent invocation is not independence of assumptions or failure modes.

Distinguish `requires_established_claim` from `scheduled_after_result`. This permits diagnosis after failure without using that failure as a true premise. An adaptive execution history may iterate; the support derivation must not become circular.

## Three-stage contracts after the revisions

| Stage | Inputs | Output | Must refuse |
|---|---|---|---|
| ERS | Accepted authority and obligations; separate implementation observations | Quantified claims, source coverage, gaps, assumptions, non-claims | Omitted requirements, invented authority, code-shaped expectations |
| Plan | Reviewed ERS, model bindings, known evidence, budgets | Themed rungs, hyperedges, oracles, premise/scheduling edges, statistical protocol | Unsupported claim strength, false joint admissibility, pairwise completeness |
| Execute/adjudicate | Accepted plan and immutable subjects/models/oracles | Raw execution record, checked scoped evidence, replay witness, briefing | Timeout-as-PASS, vacuous safety, stale inputs, empirical-to-universal promotion |

Six durable objects suffice initially: **Claim; Model Binding; Rung Plan; Execution Record; Evidence Judgment; Engineering Briefing.** The hypergraph belongs inside models/plans, not above requirements as another authority.

A narrow soundness statement is possible: given correct translations, trusted primitive evidence checks and sound inference rules, an acyclic derivation preserves exact conclusions within scope, by induction over the derivation DAG. This is conditional and does not turn a review label into proof. Statistical composition additionally requires valid dependence and simultaneous-error accounting; a justified union bound differs from multiplying confidence numbers.

## Adversarial coverage ledger

| Attack | Resolution or explicit boundary |
|---|---|
| A01 Code-shaped ERS omits reset | Bidirectional source coverage |
| A02 Hypothetical failure becomes requirement | Separate authority from investigation |
| A03 Different evidence domains merged | Typed intersection/union rules |
| A04 Empty assumptions yield safety | Nonvacuity/applicability check |
| A05 Unreachable ring counterexample | Invariant and witness validation |
| A06 Bounded check becomes unbounded proof | Horizon plus induction obligation |
| A07 Underapproximation UNSAT is lifted | Approximation-direction check |
| A08 Abstract SAT becomes physical fault | Concrete/model correspondence |
| A09 All pairs pass, triple fails | Model-guided higher-order exploration |
| A10 Local derivatives miss thresholds | Structural and nonsmooth methods |
| A11 Loose upper bound treated as failure | Feasible witness or tighter proof |
| A12 Serial wire confused with enqueue boundary | Boundary-specific models |
| A13 Average throughput hides overflow | Burst/latency/resource analysis |
| A14 More data hides systematic bias | Statistical claim and model scope |
| A15 Replayed evidence counted independently | Sampling-unit/dependence identity |
| A16 Adaptive testing becomes naive confidence | Frozen validation or valid sequential inference |
| A17 Every mutant must fail everywhere | Equivalent/environment-sensitive classification |
| A18 Process success implies tests executed | Negative controls; execution vs judgment |
| A19 Stale oracle/recipe/binary reuse | Full evidence fingerprint |
| A20 P supports Q supports P | Grounded inference; explicit induction |
| A21 Diagnostics require previous PASS | Scheduling vs logical premise |
| A22 Hash/second reviewer treated as truth | Explicit trusted-computing/model boundary |

Not every row is an automated test. Some are exact semantic counterexamples or obligations for the future implementation. This is self-review, not independent acceptance.

## Remaining non-absurd risks

Natural-language formalization can still be wrong. External application facts can be missing. Translators, solvers and oracles can share defects. Sparse discovery may miss unknown high-order interactions. Empirical results may not transfer to the deployment distribution. These are real limits; the revised architecture is valuable because it preserves them instead of concealing them inside a confidence number.

## Implementation recommendation

Build one thin vertical slice across all three stages, with typed claims, immutable model bindings, a small evidence/result checker, deterministic and bounded-exhaustive probes, validated witnesses and a fixed-sample statistical adapter. Hand-author the three worked fixtures against the same outer protocol before allowing agents to generate new rungs. Domain models remain adapters; no Toy 1 IDs, UART rates or Gaussian assumptions belong in generic gate code.

Proposed refinements to VFR v0.1: quantify scope and horizon; add nonvacuity/reachability; separate scheduling and inference; type abstraction direction; permit model-derived hyperedges without pair failures; preserve statistical sampling/selection semantics; fingerprint the complete experiment; and distinguish a valid conditional model theorem from an unsupported claim about the actual product. In particular VFR-016 should forbid an unjustified **lift to product safety**, not prevent acceptance of useful conditional mathematics before target correspondence exists.

No product requirement, accepted decision, or current VO is changed by this study. The standalone calculations and broader narrative are design evidence, not installation or qualification of the future framework.

## Technical sources

[S1] CMU SEI INT02-C: https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/recommendations/integers-int/int02-c/  
[S2] NIST, Practical Combinatorial Testing: Beyond Pairwise: https://csrc.nist.gov/pubs/journal/2008/06/practical-combinatorial-testing-beyond-pairwise/final  
[S3] Maile et al., Network Calculus Results for TSN: https://arxiv.org/html/2508.18855v1  
[S4] Ball and Rajamani, Spurious Counterexamples in C Programs: https://www.microsoft.com/en-us/research/publication/generating-abstract-explanations-of-spurious-counterexamples-in-c-programs/  
[S5] NIST, Proportion Confidence Interval: https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/propconf.htm  
[S6] Howard et al., Time-uniform confidence sequences: https://arxiv.org/html/1810.08240  
[S7] SMT-LIB official examples: https://smt-lib.org/examples.shtml

These sources ground borrowed techniques, not independent approval of this study's proposed architecture.