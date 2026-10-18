# REVIEW-PROOF-004 — Independent review of PO-003-2

Review ID: CLN-001-REVIEW-PROOF-004  
Disposition: **ACCEPT_WITH_CLARIFICATIONS**  
Candidate: inputs/PROOF-ATTEMPT-004.md  
Companion: inputs/PROOF-BRIEFING-004.md

T1 is **ACCEPTED** as the exact future-numeric equivalence on arbitrary finite unsigned histories. T2 is **ACCEPTED CONDITIONALLY**, with its stated complete deterministic information boundary A4 and unrestricted future continuations. No blocking mathematical flaw, first invalid proof line, or counterexample to either stated theorem was found. No mathematical repair is required.

The clarifications concern application and evidence: complete-state capacity is not a detector-local SRAM lower bound without establishing the information boundary; finite epoch limits and externally supplied indices must be assessed precisely; historical source and execution assertions cannot be authenticated from the current package. These do not add hypotheses silently to T1/T2. They are recorded in findings R4–R6 below. This disposition accepts only the exact mathematical propositions, not a realization, AS amendment, architecture, or product.

## 1. Review basis and definitions

I read AGENTS.md and TASK.md, the supplied inputs/PROOF_REVIEWER_ROLE.md, inputs/SHA256SUMS and all 14 manifest-listed files. The role file is supplied under inputs/, not at the root. Technical context came only from inputs/. The candidate and prior opportunity review were treated as claims to examine, not accepted lemmas.

D001 requirements.R1/R2, assumptions.A1, interface_and_lifecycle_Q4, delivery_and_exceptions_Q6, and AS PS give the mathematical model: D = {0,...,4095}; accepted histories are arbitrary finite sequences from D, including the empty sequence. Initialization/reset begins a new epoch. For h = (x_1,...,x_m), put x_j = 0 only for j <= 0, and define the ordered padded tail t_i(h) = x_(m-31+i), i = 1,...,31. Padding is not a sequence of accepted zero events.

For u = (u_1,...,u_r) with r >= 1, F_h(u) is the exact sum of squares on the last accepted event of hu. The continuation is in the same epoch, with no reset or invalid event. It may have any finite length and any values in D. F excludes the current already-emitted energy, optional E_0 publication, and logical index. The definition does not restrict h and g to equal lengths. The fixed-length restriction is used in T2, as required by TASK-PROOF-004, despite the scout's introductory same-length wording.

Equality of the functions F_h is an equivalence relation. Observing their last outputs for every nonempty continuation also compares every output along every future stream: each nonempty prefix is among the quantified continuations. No infinite computation, actual experiment observing all continuations, or rewindable machine is assumed.

ACT is the supplied accepted synthetic-baseline record for the exact AS bytes. It supersedes draft-era pending wording for this task. Its historical activation assertions are not independently authenticated. D001's delegation does not transfer to this reviewer. The present TASK authorizes this review; no old stage prohibition is treated as cancellation of that authorization.

## 2. Independently reconstructed T1

### R1 — Window decomposition and sufficiency: ACCEPT

At the final event of u, the 32 specification positions are m+r-31 through m+r, inclusive. For 1 <= r <= 31, the historical positions end at m and number 32-r. Solving m-31+i = m+r-31 gives i = r. Therefore

    F_h(u) = sum(i=r,...,31) t_i(h)^2
             + sum(k=1,...,r) u_k^2.                         (1)

For r >= 32, the first position is at least m+1, so

    F_h(u) = sum(k=r-31,...,r) u_k^2.                       (2)

This independently accounts for all window positions. At r=1, all 31 tail entries and the new sample contribute; x_(m-31) has already expired. At r=31, only t_31 remains from h. At r=32, no historical value remains. At larger r, the first r-32 continuation values have also expired. For m<31, the historical terms at nonpositive positions are exactly the tail's padded zeros. For m=0, (1) is just the incoming-square sum.

If t(h)=t(g), (1) gives equal outputs for all r in 1..31, and (2) gives equal outputs for every r >= 32. This proves sufficiency without equal accepted lengths, equal current energies, a fill flag, or a recurrence premise. Candidate §4 lines 76–93 and §5 lines 97–103 agree with this derivation.

### R2 — Recovery, injectivity and necessity: ACCEPT

Set y_j(h) = F_h(0^j), j=1,...,31. Zero is a valid accepted value. From (1),

    y_j(h) = sum(i=j,...,31) t_i(h)^2.                     (3)
    t_j(h)^2 = y_j(h)-y_(j+1)(h),  j=1,...,30.             (4)
    t_31(h)^2 = y_31(h).                                  (5)

These are 31 future observations, 30 differences, and one final isolated square. No current output or empty continuation is used. They can also be successive outputs on one path of 31 accepted zeros. A 32nd zero would give zero and is unnecessary to the proof.

For 0 <= a < b <= 4095, (b-a)(b+a)>0, so b^2>a^2. Thus squaring is injective on D, including zero. This property is needed only to recover values from the individually recovered squares; decomposition, sufficiency and square recovery do not require it.

If F_h=F_g on every nonempty continuation, all y_j coincide; (4)/(5) give equal ordered tail squares, and injectivity gives t(h)=t(g). Conversely, if the tails differ, at least one of the 31 y_j differs. The corresponding single continuation 0^j distinguishes that pair. This is an existential continuation for each pair, not a claim that every continuation distinguishes them or that the same final length distinguishes every pair.

Candidate §6 lines 107–131 is valid. The dependency graph is sound: the exact window relation yields (1)/(2), these give (3)–(5), and unsigned injectivity completes necessity. Neither PO-003-1 nor PO-003-3 is a lemma or accepted result in this review.

## 3. Independently reconstructed T2

### R3 — Reachability, complete state and counting: ACCEPT under A4

Fix any accepted length n>=32. For each a in D^31, form h_a = 0^(n-31) followed by a. It has length n and padded tail exactly a. The chosen values are valid, repeated values are permitted, and the accepted contract imposes no relation restricting their independent choices. All these histories and any common future prefixes have the same indices n and n+j, respectively. This proves L3 at the stated n, without using index differences.

A4 fixes an initial state and deterministic functions delta(q,b) and lambda(q,b). Its q is the complete retained state after the current output, not an arbitrarily selected memory array. If two histories reach equal q, one common next value gives equal outputs and equal next states. Induction repeats this for every nonempty common continuation. Required exactness then implies their F functions coincide. This proves L4; a machine may have redundant state, so tail equality need not imply machine-state equality.

For a != b, R2 supplies a distinguishing continuation for h_a and h_b. L4 forbids equal states for them. Hence the map a -> q(h_a) is injective and

    |Q_n| >= |D^31| = (4096)^31 = (2^12)^31 = 2^372.

T1 also shows that there are exactly 2^372 semantic future-numeric classes at each stated fixed n; an implementation can have more states. Q was not assumed finite.

A fixed binary store with b bits has at most 2^b configurations, so b>=372. This is distinguishability capacity, not expected compression length or Shannon entropy under an assumed distribution. Encoding length, address, registers and control position cannot serve as uncounted history. If all the counted information occupies fixed whole eight-bit octets, 8B>=372 gives B>=47; 46 octets provide only 368 bits, while 47 provide 376.

Candidate §7 lines 135–153 is valid. The theorem counts complete retained information; it neither establishes a 47-byte sufficient detector allocation nor says 47 bytes of SRAM alone are necessary if some counted information resides elsewhere. No additional index/control/scratch/stack allocation has been derived. No 2048-byte fit, arithmetic representation, update algorithm or AP follows.

## 4. Assumptions, countermodels and mathematical boundaries

### R4 — Observation and domain boundaries: nonblocking clarification

All candidate §8.1–8.6 numerical examples and the two scoped corrected equivalences check out. The following audit identifies precisely what each challenge changes.

| Challenge | Independent check | Theorem or applicability affected |
| --- | --- | --- |
| Equal current energy | h=(1,0), g=(0,1) both have energy 1 and index 2; after 31 zeros the energies are 0 and 1. At length 1, equal current energies imply equal unsigned values, so length 2 is minimal at equal length. | Refutes current-energy-only sufficiency; supports T1 necessity. |
| Oldest of previous 32 | h=(1,0^31), g=0^32 have current energies 1/0 and the same 31-tail. Equations (1)/(2) give equal futures for every nonempty u. | Refutes a 32-value/384-bit necessity claim based solely on future energies. Does not merge current outputs. |
| Include current output | Requiring equal E_m as well as all future energies determines the extra oldest square by subtracting the shared 31-tail square sum. Injectivity recovers that value. | The corrected mathematical equivalence is equality of padded 32-tails if the empty observation is defined as mathematical current energy, with E_0=0. This does not mandate actual E_0 publication or change T1. |
| Oldest tail impulse | h=(0,1,0^30), g=0^32: a single zero gives 1/0; lengths 2..31 give 0/0. | Omitting j=1 misses t_1. Confirms boundary in (3)/(4). |
| Newest tail impulse | h=(0^31,1), g=0^32: after 31 zeros energies are 1/0; after 32, 0/0. | Confirms history is present through r=31 and absent at r=32. |
| Signed-domain replacement | h=(1), g=(-1) have different values but equal squared tails and all future energies in a domain allowing both signs. | T1 value necessity fails under the changed domain. With zero allowed, the corrected invariant is the ordered tail of squares. T2 must count distinct squared contributions, not blindly the size of a signed alphabet to power 31. Negative input is invalid in the actual model. |
| Empty versus accepted zero | h=empty and g=(0) have identical numeric futures; after b their pairs are (1,b^2) and (2,b^2). | T1 covers startup; tail sufficiency does not cover indexed-interface equivalence across unequal lengths. |
| Reset | After (4095), reset then accept 1: the new pair is (1,1), not energy 16,769,026. | Reset changes the epoch. T1/T2 operate within an epoch; a compulsory reset before future observations would change the admissible-continuation problem. |
| Invalid input | After (1), reject -1 then accept 31 zeros: last pair (32,1). Incorrectly accepting a zero for -1 instead gives (33,0). | Explicit rejection/precondition exposure and unchanged accepted history/index are required. Invalid events are not elements of u. Mathematical analysis does not verify an API. |
| Delivery faults | Identical numeric values may be distinct valid events; missing/duplicate/out-of-order deliveries are outside the accepted contract. | No operational zero-fill or invisible-fault-detection guarantee follows from startup padding. Applicable detectable faults must still be reported. |
| Inexact or modular arithmetic | For example, under output reduction modulo 2, tails differing by value 0 versus 2 have equal square contributions modulo 2. | Exact-integer observation is essential. Modular arithmetic is a changed relation; candidate T1/T2 are not machine-overflow correctness proofs. |

Startup lengths 0,1,2,30,31,32,33 and longer histories were explicitly considered. At m=31 all tail entries are accepted values; m=32 and m=33 retain exactly the latest 31. Optional initial publication, nominal timing, and explicit reset do not create any finite maximum epoch length.

### R5 — Information boundary, index and finite horizon: nonblocking clarification

**Upstream replay.** A source could keep the latest samples and permit rereading them on every event. A detector could discard its local history after emitting each output, then obtain different historical data after identical local retained states. The first invalid step in an unconditional local-state proof would be L4, candidate line 141: lambda would depend on omitted upstream history as well as local q and the new value. T1 remains a statement about specified histories, and T2 remains true under A4; that detector-local boundary does not satisfy A4. Counting an expanded complete state can restore L4, but the resulting lower bound concerns the expanded boundary. AS R5 excludes exclusively upstream-owned memory from detector RAM and does not prohibit replay.

**Readable past outputs.** Any actually consulted output register/log is retained output-affecting information and belongs in the counted complete state, or else A4 does not hold for the proposed local boundary. Write-only outputs do not belong to future causal inputs. Keeping a current energy inside q is allowed but insufficient by the equal-energy example. No assertion that an arbitrary prior-output log alone is sufficient is needed.

**External logical index.** A machine receiving n externally is outside the literal input signature delta/lambda(q,b) unless that input is accounted for. However, supplying only the correct logical index does not by itself eliminate the numeric state bound: for the fixed-n witness histories, future supplied indices are the identical n+1,n+2,..., so the equal-state induction and numeric distinctions persist in that extended model. Such an index can change the applicability of PO-003-3's closed-machine index question. It is not legitimate to infer that every extra input destroys the 372-bit argument, nor to regard a history-bearing oracle as merely an index.

**Finite epoch limit.** The accepted model grants arbitrary finite histories and all nonempty continuations; it supplies no lifetime cap. If a different authorized contract capped an epoch at L, then at n=L there are no permitted nonempty continuations, so a future-only equivalence would be vacuous and a correct machine could clear its retained numeric history after its final output. At n=L-30, tails 0^29,1,0 and 0^29,0,1 give equal outputs for every continuation of lengths 1..30: both relevant squares remain in each such window, whatever the continuation values. They separate only at length 31, which that changed contract would forbid. Thus capped-horizon value necessity and the corresponding all-n T2 inference do not follow. Where all 31 future events remain permitted, the stated witness argument still works at fixed n>=32. This is a boundary analysis, not insertion of an epoch cap, wrap rule, or modified theorem.

Determinism, exactness for every valid stream, unrestricted sample choices, and completeness of q are explicit hypotheses. Fixed program constants are permitted but do not encode a changing history. Q need not be finite. Registers, control, readable outputs, counters, history-dependent timing or hidden storage cannot be omitted if they affect future outputs. Nominal cadence supplies no independent historical oracle or execution bound. The no-replay boundary is additional analysis from PO/TASK, not an adopted AS restriction or established realization fact.

## 5. Author executable supplement and independent checks

The author's bounded Python is internally consistent with its report. Direct slicing of the last 32 actual entries is a valid startup specification because omitted pre-epoch entries are zeros. Tail slicing starts at r-1 in zero-based Python, matching i=r in (1). Recovery has exactly 30 differences and one last square; no signed square root is used. The reduced Cartesian product has 3^4=81 tails, the impulse loop has 31 instances, and four impulses overlap the reduced set: 112 recovery instances represent 108 distinct tails. The author correctly labels them instances and claims only 81 distinct reduced observation vectors.

There are 8*4=32 history instances and 7*3=21 continuation instances, so 672 formula comparisons; duplicates at short lengths are intentional. The oldest-value loop has 81*21*2=3,402 comparisons. Its selected counterexample assertions exercise only specific arithmetic, not universal signed-domain behavior or lifecycle APIs. The reported counts and scope are accurate.

I inspected and reran the exact embedded author code using the extraction command in Appendix A. It exited 0 and reproduced exactly:

    PASS: formula_checks=672
    PASS: recovery_tails=112, distinct_reduced_vectors=81
    PASS: oldest_value_comparisons=3402
    PASS: selected counterexample arithmetic and cardinality/octet arithmetic

The extracted code bytes including the terminal newline have SHA-256 43e7de3753f9c84999d53ca29fc8eab1e74e25aea26a229cfd536779f12188af. This is a present reproduction, not authentication that the historical author invocation occurred.

I also wrote and ran the distinct in-memory queue reference in Appendix B. It advances a 32-position zero-initialized deque one event at a time, rather than evaluating the final specification by slicing the combined history. It compares all 672 formula instances; checks the 112 recovery instances and 108 distinct tails; compares all per-event outputs for 3,402 oldest-position variations; distinguishes all 3,240 unordered pairs among the 81 reduced tails; checks 243 fixed-length reachability instances at n=32,33,64; checks all 4,096 unsigned squares are distinct; and checks selected counterexamples, startup, rejection-as-stutter arithmetic, reset exclusion, finite-horizon examples and bit/octet arithmetic. Exit 0, all assertions passed. The results are reproduced in Appendix B.

Both commands ran from /home/easy/archbot-cln001-proof-review-004, with Python 3.14.7 (main, Aug 10 2026, 07:46:56), GCC 16.1.1 20260728, executable /usr/sbin/python3, on Linux-7.1.8-arch1-3-x86_64-with-glibc2.44. Python integers provide exact arithmetic. Commands used -B, no random inputs, no generated script files, and no network. Test data and exact formulas are in the commands. These are finite supplements, not universal proofs, proof-assistant checking, lifecycle API tests, target execution, implementation validation, or feasibility evidence.

## 6. Source integrity and independence

### R6 — Verified present bytes; historical claims remain unverified

From the inputs directory, “sha256sum -c SHA256SUMS” exited 0 with all 14 entries OK. A separate Python SHA-256 audit, reproduced in Appendix C, also passed. It verifies the candidate and briefing identities and ACT's recorded AS SHA-256 against the current AS bytes.

The author briefing lists a historical 12-entry package. Ten supplied files match its listed hashes. PO-BRIEFING-003.md and PROOF_ENGINEER_ROLE.md are absent from this review package; their historical hashes are only supplied assertions. The proof's PB source row (line 23) cannot be resolved here. Neither missing document is a mathematical dependency: definitions, exact requirements, the complete derivation and task are supplied. No unavailable source was fetched. The author's TASK hash matches the supplied inputs/TASK-PROOF-004.md. Its original AGENTS.md, original manifest bytes and command environment were not supplied for verification; the current review AGENTS/TASK/manifest are different stage artifacts, not mismatches against an expected common identity.

The initial Python source-audit wrapper twice failed an assertion because its broad table regex counted the author's historical inputs/SHA256SUMS control row as a thirteenth package entry. Restricting extraction to the explicitly labeled 12-entry source table corrected the audit; the corrected command passed. This was a reviewer audit-script scope error, not a source-hash mismatch or mathematical failure.

No Git objects/history, cited archives, other workspaces, older solved Toy 1 artifacts, hidden evaluator, network, connected system, external identity evidence, or real hardware was accessed. Prior opportunity-review checks and the author's historical 12-entry/command assertions were not independently authenticated. ACT's historical independent review/disposition files, remote activation condition and claimed checks were not retrieved or reenacted. D001 discloses sponsor-delegate prior-solution familiarity; this review does not certify that actor's blindness or the historical independence of any actor.

This invocation is an independent mathematical review of supplied claims; it authored neither candidate, delegated to no agent, and assumed no Proof Engineer, Proof Scout, AS-decision or sponsor role. Directory-based source isolation establishes neither OS/runtime/connector isolation nor formally qualified cleanroom independence. Host configuration, external identities and physical isolation were not verified.

### Verified current input hashes

| Input (relative to inputs/) | SHA-256 |
| --- | --- |
| PO-OPPORTUNITIES-003.md | 088f079a0d1476f65722eb3bd6e207333412dbbec985764e1864171495c3ccd9 |
| TASK-PROOF-004.md | 1338519f2c11accd4d27fa1dd38a5691d4b3eb5f3d5f5ec0a37d9eec2dc1ac86 |
| REVIEW-PO-003.md | 18362d90284743886be5da35c88de16838429a6fb088527dd6b7330ea3e837e9 |
| DECISION-001.yaml | 1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36 |
| adc.md | 284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 |
| AS-REV-002.md | 36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830 |
| REVIEW-PO-003.json | 78b9d60165e29331f3328f291b29cac85999df6894bc760e88c4d1b8cdcba15a |
| DECISION-TRACE-002.md | 90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2 |
| problem-origin.md | 90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 |
| PROOF_REVIEWER_ROLE.md | b7fbb874b81f7efd86b4d7977c0a5ff11846076c7ab2609d5fcd2172f6ee8bb5 |
| PROOF-ATTEMPT-004.md | be8ac09d8252a8b14accb9a9baafcc0bea2f091c12286a52ef0f409586345c99 |
| target.md | c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 |
| PROOF-BRIEFING-004.md | ce7c29202141e68c6c99e919efe454112958ae61e97d2d1a9638eeb93654ae9a |
| AS-ACTIVATION-002.yaml | d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c |

Current review control hashes (not historical author-control authentication):

| File | SHA-256 |
| --- | --- |
| AGENTS.md | 146d801716e9c68c4e18e0eb32cab37077c3ad97ae0ff6a5b8fc1ca4c2633cf0 |
| TASK.md | 7336ddadc808870be8079b2912cda90cf28f584684d706b01108864a06f874b0 |
| inputs/SHA256SUMS | ad28c4043d0277dca5bc44673d95da8a98438b97e1c144e287241422de2673bb |

Historical unavailable input assertions, not verified hashes of available files:

| Historical name | Claimed SHA-256 |
| --- | --- |
| PO-BRIEFING-003.md | 1d45d40c5328b16514fc1bd5a1396110cb8be055c4a80a88b1c2bef09644d9e2 |
| PROOF_ENGINEER_ROLE.md | cf538167f1d6bccdde325c33c66c2458be2af476826673e3d56cb31b708116fb |

## 7. Prior findings, remaining obligations and next gate

PO-R3 is resolved for the exact T1 theorem by R1/R2, including startup, every nonempty length, all 31 recovery positions and unsigned injectivity. PO-R4's conditional cardinality is resolved by R3; its realization-specific replay/ownership warning remains open under R5. The prior review was readiness, not proof acceptance. PO-R1/PO-R2 concerning PO-003-1 and PO-R5 concerning PO-003-3 have not been promoted to accepted proofs by this review. PO-003-1 and PO-003-3 remain separate unproven opportunities.

| Open item | Still required; nothing discharged here |
| --- | --- |
| T002-2 | Concrete numeric realization verification against an independent specification, including boundary/randomized streams. |
| T002-3 | Concrete startup/reset behavior and prior-epoch exclusion. |
| T002-4 | One energy with correct logical index per accepted event; concrete interface and index mechanism. |
| T002-5 | Actual invalid rejection/precondition exposure, unchanged accepted state/index, and applicable detectable-fault reporting. |
| T002-6 | Detector memory ownership, actual persistent/scratch/owned-stack accounting, hardware dependency analysis, RAM ceiling evidence, and applicability of the complete-information boundary. |
| T002-7 | Target/toolchain and applicable performance/resource evidence; no invented deadline or optimization threshold. |
| T002-8 / R4 | Threshold, duration, boolean decision and integration specification/verification before whole-detector completion. |

PO-003-3's unbounded exact-index question remains distinct and unproven; this review supplies no finite-state impossibility proof or unconditional AS-defect conclusion. No epoch cap or wrap interpretation is selected.

Next gate: a separately authorized realization-specific applicability/interface review must establish the permitted information sources and ownership boundary before using T2 as a local resource bound. Any further Proof Engineer task, AP/CON/DE/C work or product qualification requires separate authorization; none runs automatically from this review. AS/F/D001 remain unchanged. No AP is selected, no complete detector is established, and no product RAM, timing, compute, power or hardware compliance is proved.

Receipt flags: cleanroom_qualified=false; product_verified=false; implementation_verified=false; vo_discharged=[]. Mathematical acceptance is restricted to the exact T1 and conditional T2 stated above. Work stops with the two requested review artifacts.

## Appendix A. Exact author-code reproduction command

Shell: bash, login disabled; working directory and environment as in §5.

```bash
python3 -B - <<'PY'
import ast
import contextlib
import hashlib
import io
import json
import os
import platform
import sys
from pathlib import Path

brief = Path('inputs/PROOF-BRIEFING-004.md').read_text()
code = brief.split("```bash\npython3 -B - <<'PY'\n", 1)[1].split('\nPY\n```', 1)[0] + '\n'
tree = ast.parse(code)
imports = [ast.unparse(n) for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
assert imports == ['from itertools import product']
assert not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in {'open', 'eval', 'exec', '__import__'} for n in ast.walk(tree))
output = io.StringIO()
with contextlib.redirect_stdout(output):
    exec(compile(tree, 'inputs/PROOF-BRIEFING-004.md:python-block', 'exec'), {})
expected = 'PASS: formula_checks=672\nPASS: recovery_tails=112, distinct_reduced_vectors=81\nPASS: oldest_value_comparisons=3402\nPASS: selected counterexample arithmetic and cardinality/octet arithmetic\n'
assert output.getvalue() == expected
print(json.dumps({'check': 'author_code_reproduction', 'cwd': os.getcwd(), 'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(), 'code_sha256': hashlib.sha256(code.encode()).hexdigest(), 'stdout': output.getvalue(), 'result': 'PASS'}, indent=2))
PY
```

## Appendix B. Exact independently authored bounded check

```bash
python3 -B - <<'PY'
from collections import deque
from itertools import product
import json
import os
import platform
import sys

def run(history, future):
    window = deque([0] * 32, maxlen=32)
    for value in history:
        window.append(value)
    result = []
    for value in future:
        window.append(value)
        result.append(sum(value * value for value in window))
    return result

def padded_tail(history):
    return tuple(([0] * 31 + list(history))[-31:])

histories = []
for length in (0, 1, 2, 30, 31, 32, 33, 64):
    histories += [
        (0,) * length,
        (4095,) * length,
        tuple(4095 if i % 2 else 0 for i in range(length)),
        tuple((197 * i + 17) % 4096 for i in range(length))]
futures = []
for length in (1, 2, 30, 31, 32, 33, 64):
    futures += [(0,) * length, (4095,) * length,
                tuple((211 * i + 23) % 4096 for i in range(length))]
formula_checks = 0
for history in histories:
    tail = padded_tail(history)
    for future in futures:
        r = len(future)
        expected = (sum(x*x for x in tail[r-1:]) + sum(x*x for x in future)
                    if r < 32 else sum(x*x for x in future[-32:]))
        assert run(history, future)[-1] == expected
        formula_checks += 1

tails = []
for values in product((0, 1, 4095), repeat=4):
    tail = [0] * 31
    for index, value in zip((0, 9, 19, 30), values):
        tail[index] = value
    tails.append(tuple(tail))
recovery_tails = tails + [
    tuple(4095 if index == pos else 0 for index in range(31))
    for pos in range(31)]
vectors = []
for tail in recovery_tails:
    observations = run((0,) + tail, (0,) * 32)
    squares = tuple(observations[i] - observations[i+1] for i in range(31))
    assert observations[31] == 0
    assert squares == tuple(x*x for x in tail)
    vectors.append(tuple(observations[:31]))
assert len(set(vectors[:81])) == 81
assert len(set(recovery_tails)) == len(set(vectors)) == 108

oldest_checks = 0
for tail in tails:
    for future in futures:
        for oldest in (1, 4095):
            assert run((oldest,) + tail, future) == run((0,) + tail, future)
            oldest_checks += 1

pair_checks = 0
for i, first in enumerate(tails):
    for second in tails[i+1:]:
        a, b = run((0,) + first, (0,) * 31), run((0,) + second, (0,) * 31)
        assert any(x != y for x, y in zip(a, b))
        pair_checks += 1
reachability_checks = 0
for n in (32, 33, 64):
    for tail in tails:
        history = (0,) * (n-31) + tail
        assert len(history) == n and padded_tail(history) == tail
        reachability_checks += 1
assert len({x*x for x in range(4096)}) == 4096
assert run((1, 0), (0,)*31)[-1] == 0
assert run((0, 1), (0,)*31)[-1] == 1
assert run((), (7,)) == run((0,), (7,)) == [49]
assert run((1,), (0,)*31)[-1] == 1
assert run((1, 0), (0,)*31)[-1] == 0
for future in futures:
    assert run((1,), future) == run((-1,), future)
assert run((4095,), (1,)) == [16769026]
assert run((), (1,)) == [1]
a = (0,)*29 + (1, 0)
b = (0,)*29 + (0, 1)
assert run(a, (0,)*30) == run(b, (0,)*30)
assert run(a, (0,)*31)[-1] == 0
assert run(b, (0,)*31)[-1] == 1
assert 4096**31 == 2**372 and 46*8 < 372 <= 47*8
print(json.dumps({
    'check': 'independent_queue_reference',
    'cwd': os.getcwd(), 'python': sys.version,
    'executable': sys.executable, 'platform': platform.platform(),
    'history_instances': len(histories), 'continuation_instances': len(futures),
    'formula_checks': formula_checks,
    'recovery_instances': len(recovery_tails), 'distinct_recovery_tails': 108,
    'distinct_reduced_vectors': 81, 'oldest_history_comparisons': oldest_checks,
    'reduced_tail_pairs_distinguished': pair_checks,
    'fixed_length_reachability_checks': reachability_checks,
    'unsigned_squares_distinct': 4096,
    'counterexamples_and_capacity': 'PASS', 'result': 'PASS'}, indent=2))
PY
```

Result (exit 0):

```json
{
  "check": "independent_queue_reference",
  "cwd": "/home/easy/archbot-cln001-proof-review-004",
  "python": "3.14.7 (main, Aug 10 2026, 07:46:56) [GCC 16.1.1 20260728]",
  "executable": "/usr/sbin/python3",
  "platform": "Linux-7.1.8-arch1-3-x86_64-with-glibc2.44",
  "history_instances": 32,
  "continuation_instances": 21,
  "formula_checks": 672,
  "recovery_instances": 112,
  "distinct_recovery_tails": 108,
  "distinct_reduced_vectors": 81,
  "oldest_history_comparisons": 3402,
  "reduced_tail_pairs_distinguished": 3240,
  "fixed_length_reachability_checks": 243,
  "unsigned_squares_distinct": 4096,
  "counterexamples_and_capacity": "PASS",
  "result": "PASS"
}
```

## Appendix C. Exact corrected source-audit command

Shell/environment as in §5, working directory the review workspace. Exit 0; all 14 hashes matched, ten historical source entries matched, two were unavailable, author task and activated AS identities matched. Initial-wrapper scope correction is disclosed in §6.

```bash
python3 -B - <<'PY'
import hashlib
import json
import re
from pathlib import Path

manifest = {}
for line in Path('inputs/SHA256SUMS').read_text().splitlines():
    digest, name = line.split(maxsplit=1)
    manifest[name.strip()] = digest
actual = {name: hashlib.sha256((Path('inputs') / name).read_bytes()).hexdigest()
          for name in manifest}
assert manifest == actual and len(manifest) == 14
brief = Path('inputs/PROOF-BRIEFING-004.md').read_text()
brief = brief.split('The exact inspected control/manifest hashes', 1)[0]
historical = dict(re.findall(r'\| `inputs/([^`]+)` \| `([0-9a-f]{64})` \|', brief))
matched = {name: digest for name, digest in historical.items()
           if name in actual and actual[name] == digest}
missing = {name: digest for name, digest in historical.items() if name not in actual}
assert len(historical) == 12 and len(matched) == 10 and len(missing) == 2
assert actual['TASK-PROOF-004.md'] == '1338519f2c11accd4d27fa1dd38a5691d4b3eb5f3d5f5ec0a37d9eec2dc1ac86'
activation = Path('inputs/AS-ACTIVATION-002.yaml').read_text()
assert 'source_AS_sha256: ' + actual['AS-REV-002.md'] in activation
control = {name: hashlib.sha256(Path(name).read_bytes()).hexdigest()
           for name in ('AGENTS.md', 'TASK.md', 'inputs/SHA256SUMS')}
print(json.dumps({'current_manifest_entries': 14, 'source_hashes': actual,
                  'author_historical_entries': 12, 'historical_entries_matched': 10,
                  'historical_entries_not_supplied': missing,
                  'control_hashes': control,
                  'author_task_bytes_match': True, 'activation_AS_hash_matches': True,
                  'result': 'PASS'}, indent=2))
PY
```

