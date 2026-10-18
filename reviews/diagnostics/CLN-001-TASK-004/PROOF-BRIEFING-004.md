# PROOF-BRIEFING-004 — PO-003-2 handoff

Author's assessment: **CLAIMED_PROOF_PENDING_REVIEW**. This Proof Engineer claims a mathematical derivation of the exact future-numeric equivalence and its conditional state-cardinality consequence. Independent proof acceptance is not claimed or performed. No counterexample to the exact statement was found; broader variants fail as documented in the proof attempt.

## Outputs and findings

Only these two artifact files were written:

- `out/PROOF-ATTEMPT-004.md`: precise epoch/history/observation/state definitions; universal sufficiency and necessity proofs; fixed-length reachability and state distinguishability; 372-bit/47-octet capacity interpretation; explicit counterexamples, dependencies, evidence classes and limitations.
- `out/PROOF-BRIEFING-004.md`: this source receipt, executable-check record and review/applicability handoff.

The argument derives every future energy directly from the latest padded 31-tail and the continuation. Zero continuations of lengths 1 through 31 recover the individual tail squares, and nonnegative square injectivity recovers their values. At any fixed accepted length n>=32, arbitrary tails are reachable and pairwise distinguishable by numeric outputs, requiring at least 2^372 complete retained states under the explicitly deterministic, complete-information, no-replay model. The minimum whole-octet information capacity is 47; it is not an implementation allocation or proof of resource fit.

The equivalence excludes the already-emitted current output and logical index. Same current energy does not suffice; the oldest of the previous 32 values can change current energy without changing any future numeric output. Signed inputs would invalidate value recovery. Startup zeros need no numeric fill marker, but histories of different lengths with equal tails can require different next indices. Replay and external logs require a different information-boundary analysis. The possible unbounded indexed-interface issue in PO-003-3 remains a separate unproven opportunity.

## Exact inspected files and hashes

Read `AGENTS.md`, `TASK.md`, the supplied role at `inputs/PROOF_ENGINEER_ROLE.md`, and the input manifest, then the supplied package. The role is in inputs, not at the root path initially attempted. No alternate role or external instructions were imported.

The following are the exact inspected package files. Every one of the 12 entries matched the current supplied manifest. The command was `sha256sum -c SHA256SUMS`, with working directory `/home/easy/archbot-cln001-proof-engineer-004/inputs`; exit status 0, all 12 entries `OK`.

| Inspected file | SHA-256 |
| --- | --- |
| `inputs/PO-OPPORTUNITIES-003.md` | `088f079a0d1476f65722eb3bd6e207333412dbbec985764e1864171495c3ccd9` |
| `inputs/REVIEW-PO-003.md` | `18362d90284743886be5da35c88de16838429a6fb088527dd6b7330ea3e837e9` |
| `inputs/PO-BRIEFING-003.md` | `1d45d40c5328b16514fc1bd5a1396110cb8be055c4a80a88b1c2bef09644d9e2` |
| `inputs/DECISION-001.yaml` | `1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36` |
| `inputs/adc.md` | `284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7` |
| `inputs/AS-REV-002.md` | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` |
| `inputs/REVIEW-PO-003.json` | `78b9d60165e29331f3328f291b29cac85999df6894bc760e88c4d1b8cdcba15a` |
| `inputs/DECISION-TRACE-002.md` | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` |
| `inputs/problem-origin.md` | `90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333` |
| `inputs/target.md` | `c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64` |
| `inputs/PROOF_ENGINEER_ROLE.md` | `cf538167f1d6bccdde325c33c66c2458be2af476826673e3d56cb31b708116fb` |
| `inputs/AS-ACTIVATION-002.yaml` | `d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c` |

The exact inspected control/manifest hashes were obtained with `sha256sum AGENTS.md TASK.md inputs/SHA256SUMS` from the workspace root, exit status 0:

| Inspected file | SHA-256 |
| --- | --- |
| `AGENTS.md` | `616363028bc48dc1c800e593aaed46af7ccb7d17612d42a7e3f0b23d79814702` |
| `TASK.md` | `1338519f2c11accd4d27fa1dd38a5691d4b3eb5f3d5f5ec0a37d9eec2dc1ac86` |
| `inputs/SHA256SUMS` | `3198a15cf89fd53a66fe248409b16a439a768c0f2d9f6067972b3acea8a7ec29` |

The supplied prior review reports 14 entries in its own earlier package; this invocation verified only the current 12-entry package. Files mentioned in that report but absent from the current manifest were not retrieved or inspected. Cited archival paths, Git objects, remote activation evidence and older Toy 1 artifacts were not accessed. SHA-256 consistency establishes local byte agreement with the supplied manifest, not external authenticity or proof acceptance.

ACT records acceptance of this AS for the synthetic energy primitive and supersedes the older pending-acceptance wording in AS/TRACE. Its recorded historical verification was not repeated. D001 discloses delegate prior-solution familiarity; this author used no older solution. The role here is Proof Engineer, not scout, independent proof reviewer, AS reviewer or sponsor delegate. No sub-agents, external sources, network, connected applications, Git history, prior chat or hidden rubric were used. Directory separation is a context allowlist, not qualified OS isolation or formal cleanroom evidence.

## Executable supplement actually run

One bounded Python calculation was run in memory with arbitrary-precision integer arithmetic. No script file, implementation or target test was produced. Its purpose was to catch indexing/arithmetic mistakes in the displayed formulas and examples; the universal mathematical argument is in the proof attempt.

Parameters and coverage:

- History lengths 0, 1, 2, 30, 31, 32, 33, 64, with four deterministic shapes: all zero, all 4095, alternating zero/4095 and a modular arithmetic pattern. These are 32 history instances, including duplicates at short lengths.
- Continuation lengths 1, 2, 30, 31, 32, 33, 64, with three shapes: all zero, all 4095 and a modular pattern. All 672 history/continuation instance pairs compare direct latest-32 square sums with W1/W2.
- All 81 tails whose one-based positions 1, 10, 20 and 31 vary independently over {0,1,4095}, with all other positions zero. For each, 31 zero-continuation observations recover its squares. These 81 observation vectors are distinct.
- Thirty-one additional single-4095 impulse instances, one at each tail position, check recovery. The total is 112 recovery instances, not 112 distinct tails; some impulse cases overlap the 81-tail set.
- For each of the 81 reduced tails and 21 continuation instances, compare a length-32 history beginning with zero against histories beginning with 1 or 4095. All 3,402 comparisons verify that changing only the oldest historical position does not affect the selected future observations.
- Selected equal-current-energy and signed counterexample arithmetic, and the exponent/octet arithmetic, are asserted. The negative sample is used only in the hypothetical signed-domain challenge, never as an accepted sample under D.

Exact command, run from `/home/easy/archbot-cln001-proof-engineer-004`:

```bash
python3 -B - <<'PY'
from itertools import product

Dmax = 4095

def tail(h):
    return ((0,) * 31 + tuple(h))[-31:]

def spec(h, u):
    assert len(u) > 0
    return sum(v * v for v in (tuple(h) + tuple(u))[-32:])

def expression(t, u):
    r = len(u)
    if r <= 31:
        return sum(v * v for v in t[r - 1:]) + sum(v * v for v in u)
    return sum(v * v for v in u[-32:])

lengths_h = (0, 1, 2, 30, 31, 32, 33, 64)
lengths_u = (1, 2, 30, 31, 32, 33, 64)
histories = []
for m in lengths_h:
    histories.extend(((0,) * m, (Dmax,) * m,
                      tuple(Dmax if i % 2 else 0 for i in range(m)),
                      tuple((197 * i + 17) % 4096 for i in range(m))))
continuations = []
for r in lengths_u:
    continuations.extend(((0,) * r, (Dmax,) * r,
                          tuple((211 * i + 23) % 4096 for i in range(r))))
formula_checks = 0
for h in histories:
    for u in continuations:
        assert spec(h, u) == expression(tail(h), u)
        formula_checks += 1

tails = []
for values in product((0, 1, Dmax), repeat=4):
    t = [0] * 31
    for pos, value in zip((0, 9, 19, 30), values):
        t[pos] = value
    tails.append(tuple(t))
observations = set()
recovery_checks = 0
for t in tails:
    y = tuple(spec((0,) + t, (0,) * j) for j in range(1, 32))
    recovered = tuple(y[i] - y[i + 1] for i in range(30)) + (y[-1],)
    assert recovered == tuple(v * v for v in t)
    observations.add(y)
    recovery_checks += 1
assert len(observations) == 81
for pos in range(31):
    t = tuple(Dmax if i == pos else 0 for i in range(31))
    y = tuple(spec((0,) + t, (0,) * j) for j in range(1, 32))
    recovered = tuple(y[i] - y[i + 1] for i in range(30)) + (y[-1],)
    assert recovered == tuple(v * v for v in t)
    recovery_checks += 1
oldest_checks = 0
for t in tails:
    for u in continuations:
        baseline = spec((0,) + t, u)
        for a in (1, Dmax):
            assert spec((a,) + t, u) == baseline
            oldest_checks += 1
assert spec((1, 0), (0,) * 31) == 0
assert spec((0, 1), (0,) * 31) == 1
assert spec((1,), (0,) * 31) == spec((-1,), (0,) * 31) == 1
assert sum(v * v for v in (1, 0)) == sum(v * v for v in (0, 1)) == 1
assert 4096 ** 31 == 2 ** 372
assert (372 + 7) // 8 == 47
print('PASS: formula_checks=' + str(formula_checks))
print('PASS: recovery_tails=' + str(recovery_checks) + ', distinct_reduced_vectors=' + str(len(observations)))
print('PASS: oldest_value_comparisons=' + str(oldest_checks))
print('PASS: selected counterexample arithmetic and cardinality/octet arithmetic')
PY
```

Result: exit status 0, with output:

```text
PASS: formula_checks=672
PASS: recovery_tails=112, distinct_reduced_vectors=81
PASS: oldest_value_comparisons=3402
PASS: selected counterexample arithmetic and cardinality/octet arithmetic
```

These are finite synthetic checks, not exhaustive D^31 coverage, arbitrary-history coverage, randomized-stream verification, independent formal verification, lifecycle API tests, target execution or feasibility evidence. Reset and invalid-event behavior were analyzed mathematically, not exercised through a concrete API. The earlier review's checks are its supplied historical assertions and are not reported as tests run here.

## Questions for a distinct proof reviewer

These are handoff questions, not a request to this author to review or accept its own proof:

1. Does the window-position derivation justify W1 for every startup length and r=1 through 31, and W2 beginning exactly at r=32?
2. Do all 31 zero-continuation observations, their 30 differences and the final square recover every ordered entry without using an empty continuation or assuming signed-square injectivity?
3. Does the fixed-n construction reach every D^31 tail, and does complete deterministic state equality force equality of every future output under the exact information-source model?
4. Is the 372-bit/47-octet capacity interpretation valid without smuggling in a current output, a free encoding-length field, index differences, external replay or an implementation footprint claim?
5. Are current-versus-future observations, arbitrary-versus-fixed history lengths, reset/invalid semantics and numeric-versus-indexed outputs kept distinct throughout?
6. Are the supplied authority/provenance limits and all remaining obligations preserved, with no dependence on the scout's conjectures as proven lemmas?

## Open applicability requirements and next gate

A later realization must identify every output-affecting information source and its ownership, including publisher-history access, retained outputs, counters, registers and control data. AS's exclusion of exclusively upstream-owned memory does not impose the no-replay model. Applying T2 to local detector state requires establishing A4 for that boundary; otherwise any expanded-state conclusion must be labeled with its actual boundary.

The eventual interface must clarify exact logical-index association/production, available external information and any authorized epoch limits. This artifact chooses no stored counter, finite lifetime, wrap rule or external-index mechanism. PO-003-3 requires a separate authorized proof and interface-interpretation task; this numeric proof does not establish a defect in AS.

The following remain open under ACT: T002-2 numeric realization verification; T002-3 startup/reset; T002-4 per-event indexed association; T002-5 invalid/fault behavior; T002-6 actual RAM, scratch, owned stack, ownership and hardware-dependency accounting; T002-7 target/performance evidence; T002-8 full sustained-energy detection. R4's threshold, duration, boolean decision and integration are deferred until before any whole-detector completion claim. No item is discharged by the proof attempt or bounded checks.

Required next gate: a distinct independent proof reviewer must examine the exact submitted T1/T2 arguments and assumptions and issue its own disposition. Readiness for proof engineering is not acceptance of this proof; the author's assessment is not that disposition. Realization-specific applicability review and later authorized implementation/verification remain separate.

No AP or accepted F was selected, no C implementation was produced, and no decisions were modified. No hardware compliance, historical VO discharge, qualified cleanroom, externally authenticated reviewer independence, product verification or independent proof acceptance is claimed. Work stops with these two artifacts.
