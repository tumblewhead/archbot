# REVIEW-PO-003 — Independent opportunity-quality review

Disposition: **READY_FOR_PROOF_ENGINEER**. This is readiness for a later separately authorized, distinct proof task. All three propositions remain **UNPROVEN**; proofs_accepted: false. No architecture is selected.

The accepted synthetic baseline is the exact AS hash activated by ACT-002. Older pending language in AS/TRACE does not override that supplied activation record. Historical activation evidence was not retrieved or independently authenticated.

## PO-003-1

The opportunity supplies universal stream/event quantifiers, exact integer hypotheses, an explicit outgoing sample, a prospective alignment/bounds proof route and implementation counterexample risks. No obvious mathematical counterexample was found in this screening.

Independent arithmetic gives M=16,769,025; 31M=519,839,775; 32M=536,608,800; 33M=553,377,825. The proposed unsigned value widths are 24, 29 and 30 bits for a square, energy and addition-first intermediate. Every displayed value also fits signed 32-bit range. The all-maximum full window and next maximum attain 32M and addition-first 33M; the subtract-first maximum is 31M. Lower extrema are zero.

Indexing is epoch-local: outgoing a=x_(n-32) is zero through n=32; at n=33 it is x_1. Thus n=1,31,32 use startup padding, n=33 is the first eviction, and reset restarts this reasoning. E_0=0 is consistent with the bound at n=0. Spot checks included these boundaries and 102 accepted events across maximum, increasing and alternating streams.

**Separate realization obligation:** bounded mathematical results do not establish language overflow safety. Narrow multiplication can fail before assignment, promotions/signedness matter, and a 29-bit addition-first intermediate cannot hold 33M. No language, compiler or operand type is supplied. A later proof and realization analysis must remain distinct; no RAM fit follows.

## PO-003-2

The equivalence quantifies over every **nonempty** continuation and observes its last output. This excludes the already-emitted current output deliberately. Equal padded 31-tails appear sufficient under the stated relation: future windows of lengths 1..31 use a tail suffix and continuation; lengths at least 32 use continuation samples alone. This is a screening assessment, not an accepted proof.

For an oldest-to-newest tail t_1..t_31, set y_j=F_h(0^j), j=1..31. The candidate recovery check is y_j=sum(t_i^2, i=j..31): y_j-y_(j+1) isolates t_j^2 for j=1..30, and y_31 isolates t_31^2. This explicitly tests **all 1..31 zero continuations**, including the oldest tail value at j=1. Squaring is injective on the adopted nonnegative domain; allowing signed samples would invalidate that recovery of values. Startup zeros require no additional historical-length marker for numeric-only futures.

Bounded in-memory checks recovered 243 tails padded from five varying positions over {0,1,4095}, with distinct observation vectors, and all 31 single-maximum impulse positions. These checks are neither exhaustive over D^31 nor external proof evidence. Equal-current-energy histories (1,0) and (0,1) give F(0^31)=0 and 1. Length-32 histories differing only in the oldest value can differ in current energy while sharing all future numeric outputs. Neither example refutes the stated proposition.

At each fixed n>=32, choose an n-31-length zero prefix followed by an arbitrary tail: index differences do not explain distinguishability. The proposed 4096^31=2^372 count concerns all retained information in the specified deterministic no-replay model. Packed information occupies at least 47 eight-bit octets; this does not count working storage, control, logical index, alignment or stack and is not a RAM implementation footprint. Consulting upstream history or prior outputs requires examining the model and ownership; it cannot be treated as free retained information. Full-interface sufficiency is explicitly excluded.

The route, adversarial cases and limitations are precise enough for a later proof task. No obvious counterexample to the proposition as stated was found; every general argument still needs distinct proof and review.

## PO-003-3

The opportunity explicitly closes the machine: finite Q, deterministic delta and lambda, and all output-affecting information in Q plus the current input. Repeated pre-event states on all-zero inputs would force identical emitted pairs at distinct event positions, challenging exact strictly increasing indices. This is an appropriate prospective impossibility route, not an accepted theorem here.

Finite detector RAM alone does not establish this closed model. A supplied arbitrary index, external growing information, or a bounded epoch would change applicability. Optional reset supplies no maximum epoch length, and nominal 1 ms specifies no maximum lifetime. A finite counter eventually exhausts its index range under an unbounded epoch. The possible full-interface specification gap needs later authorized interpretation; it is **not an unconditional AS defect**. This reviewer supplies no wrap, lifetime, index mechanism or AS amendment.

## Independent next-proof priority

1. **PO-003-2 — highest next proof ROI.** Moderate proof effort offers the strongest representation-independent information bound and can prevent both energy-only sufficiency mistakes and an unjustified 32-sample necessity claim. Main risks are the nonempty/current-output distinction, square injectivity, fixed-length reachability and replay assumptions.
2. **PO-003-1.** Cheap and useful arithmetic risk reduction, with less comparative value. Type-level overflow remains unresolved even after any mathematical proof.
3. **PO-003-3.** Valuable interface warning; applicability depends most heavily on added hypotheses and authority clarification.

No opportunity is silently repaired or accepted. All have precise hypotheses, proof routes, adversarial challenges and scope exclusions suitable for distinct proof work. T002-2..T002-8 remain open, including R4 threshold/duration/decision/integration before whole-detector completion.

## Receipt and limits

Read AGENTS.md, TASK.md and only the positive-allowlisted inputs, including both author tasks and both draft products. All 14 supplied manifest entries checked OK. Checks were arithmetic, bounded counterexample screening and source/quantifier review, not target measurements, an implementation, or checked external proof evidence. This invocation authored neither candidate and assumes no Proof Engineer, sponsor-delegate or AS-review role. No old solution, Git history, other workspace, network, connected system or hidden evaluator was accessed. Supplied archival assertions and independence were not externally authenticated; directory location does not enforce OS isolation.

Next gate: separately authorize a distinct Proof Engineer task, preferably PO-003-2, followed by independent proof and applicability review. cleanroom_qualified: false; product_verified: false; vo_discharged: []; proofs_accepted: false.

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
