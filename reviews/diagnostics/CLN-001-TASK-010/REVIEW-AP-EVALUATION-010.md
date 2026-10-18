Review ID: `CLN-001-REVIEW-AP-EVALUATION-010`

Disposition: **READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION**, limited to independent review of the exact three supplied Stage-9 evaluation outputs. Their completed numerical results and finite counterexamples reproduced without discrepancies. No material contradiction was found across the report, JSON receipt and briefing, or against the supplied active synthetic baseline. No source revision is required for this bounded referral.

This permits a **separate delegated evidence disposition only**. It does not select or approve A/B/C, approve an interface/service/contract, authorize CON/DE/C, qualify a target or product, or discharge verification. All 18 realized H1–H6 gates and all realized F coordinates remain **UNKNOWN**. HIGH findings below block later realization/commitment claims; they do not block review of evidence that expressly preserves those unknowns.

**Source identities and authority.** I read AGENTS.md, TASK.md, the current manifest and supplied inputs only. I used terminal tools for source inspection, hashing and in-memory Python replay. I used no other workspace, Git history, network, connected app, hidden evaluator/reference, old solved Toy1 artifact or subagent. I did not act as Stage-9 evaluator, AP author/reviewer, delegate or selector.

Both `sha256sum -c` and independent Python SHA-256 comparison succeeded: **28/28** current manifest entries, **3/3** original Stage-9 output-manifest entries and **2/2** R1-review-manifest entries. These overlapping checks are not 33 distinct payloads. Current manifest digest is `9f71b90fcdfdb81bc4bf6ceb04d7b2be41700429534d5ebd1838df35b8ada8c1`. Complete expected/observed identities, sizes and commands appear in the companion JSON.

| Original Stage-9 output | Verified SHA-256 |
| --- | --- |
| `inputs/AP-EVALUATION-009.md` | `25b028f1181fd6f597ee1e76b4b2de79bbd7bd61ad35d88a68f36686bf9c6c78` |
| `inputs/AP-EVALUATION-009.json` | `58b3b69dad323296cf218ff7247b4145784f03782afb66642c85592326710d89` |
| `inputs/AP-EVALUATION-BRIEFING-009.md` | `71407bc42a992351dfed4c25179d3b9116dd671fc96a2c11d3c01d8ae5c7fc03` |

All **21** payloads in Stage-9 JSON `/source_hash_checks/payloads` are present and their recorded hashes match current bytes. Reconstructing that earlier manifest from its ordered entries yields its recorded digest `f12cad24c1cdfc4dae81c3c36a6936ccd8b10fdeeec9091f72dee1b58b542d8e`. Supplied `TASK-AP-EVALUATION-009.md` matches the receipt's former TASK.md digest. The difference between Stage-9's 21-payload source package and today's 28-entry package is therefore not a count contradiction. Historical citations inside supplied sources are references, not additional authenticated inputs; no unavailable historical artifact was retrieved. The former Stage-9 AGENTS.md was not supplied as an independent historical copy.

The governing baseline is D001 and AS-REV-002 through AS-ACTIVATION-002, plus AS-ADDENDUM-008-R1 through its separate disposition; F-DISPOSITION-003, D002 and PROOF-DISPOSITION-004 retain their scoped authority. The AS/addendum/prior-review DRAFT, PROPOSED and pending labels are preserved authoring-time text, governed by the later supplied activation records. D003's proposal disposition alone supplies neither activation nor a service. The R1-review pair's matching manifest verifies its bytes; it does not independently reperform that earlier original-versus-R1 source comparison, whose old source package is incomplete here. Current hash agreement authenticates neither historical execution, delegation nor reviewer separation. OS and connector isolation remain **unverified**; the allowlist does not establish either.

**Inspected programs and actual replay.** Before execution I read both complete embedded programs, reviewed their imports, transitions, loops, assertions and output, then compared the complete preliminary source with the final numeric source. They contain finite in-memory computation and JSON printing, with no explicit filesystem mutation, network call or process launch. The final numeric source imports itertools/random/json/sys/hashlib; races imports itertools/json. The reviewer wrapper launches those inspected exact strings in separate Python subprocesses, captures stdout/stderr and exit status, and applies a 180-second timeout per child. No program/test file was created.

Actual tool was `functions.exec` using `exec_command` and `write_stdin`; replay shell used `login:false`. Interpreter was `/usr/sbin/python3`, Python **3.14.7 (main, Aug 10 2026, 07:46:56) [GCC 16.1.1 20260728]`, invoked with `-B`, without optimization; assertions were enabled. Numeric randomness is local `random.Random(9009)` and `random.Random(9010)`. The race suite is deterministic enumeration.

| Exact receipt source | Source SHA-256 | Actual child exit / result |
| --- | --- | --- |
| `/experiments/numeric/source` | `8f1227441436f96e0a279d879448c40a1224e4c9093ef0fae5675826eade5d72` | 0; every parsed output field equals recorded result |
| `/experiments/races/source` | `a09a57175984f941d85e811e79b014c0853fc4054b02ffef0c4752ee9fa9cd1d` | 0; every parsed output field equals recorded result |
| `/experiments/setup_correction/initial_source` | `044b312b8404602f0865e70dbfaf765ff176f72d64e9f3bbb63164582cb747b6` | 1; disclosed `AssertionError: ('M04', 0, 0)` reproduced |

The replay wrapper itself exited 0 after recording all three child outcomes. The JSON preserves the exact wrapper command, executable/version, source and stdout hashes, full successful results, comparison differences (empty) and preliminary traceback. Both original recorded inline commands also match their source strings byte for byte. The initial shell used for some read/hash operations emitted a denied pyenv rehash diagnostic; later commands disabled login-shell startup. This was not a numeric-program discrepancy or evidence of OS isolation.

A compact equivalent replay, after the same source inspection, is:

~~~python
import json, subprocess, sys
p = json.load(open("inputs/AP-EVALUATION-009.json"))
for key, field in (("numeric", "source"), ("races", "source"),
                   ("setup_correction", "initial_source")):
    r = subprocess.run([sys.executable, "-B", "-c",
                        p["experiments"][key][field]],
                       capture_output=True, text=True, timeout=180)
    print(key, r.returncode, r.stdout, r.stderr)
~~~

| Completed numeric run | Accepted | Invalid attempts | Explicit resets |
| --- | ---: | ---: | ---: |
| E01: 6,561 length-8 streams over {0,1,4095} | 52,488 | 0 | 6,561 |
| E02: 120,000 actions, seed 9009 | 105,633 | 12,001 | 2,366 |
| E02: 120,000 actions, seed 9010 | 105,460 | 12,155 | 2,385 |
| E03: ones/maxima/impulse/distinct expiry, 65 each; alternating, 66 | 326 | 0 | 0 |
| E04: 0..4095 eight times without reset | 32,768 | 0 | 0 |
| E05: reset from every cursor, then sample 2 | 2,418 | 0 | 62 |
| E06: rejection around six boundary/reset prefixes | 203 | 36 | 12 |
| **Final totals only** | **299,296** | **24,192** | **11,386** |

There are **897,888** candidate/oracle energy comparisons: three per accepted event. The printed zero mismatch count is a constant reached only after all relevant assertions succeed; it is not a separately accumulated mismatch detector. Successful asserted completion supports zero encountered mismatches. Initial construction is not an explicit reset. Witness operations and preliminary execution are excluded from the completed counts.

The oracle retains the entire current accepted stream and recomputes its latest 32 squares. It does not consult candidate storage, cursor or aggregate. A retains raw31; B square31 plus S and cursor. Their chronological next tails are checked against an independently sliced oracle suffix, and B's S against both that suffix and stored slots. This catches age errors hidden by a correct current sum. Oracle independence is structural within this supplied experiment; it does not establish independent human authorship, interpreter correctness or full formal proof. C's immutable pre-tail, service rank and coordinated reset are supplied by the harness as assumptions; its agreement cannot discover or validate RN/C-HIST.

At n=1/31/32/33, ones produce 1/31/32/32; maxima Q/31Q/32Q/32Q; maximum impulse Q/Q/Q/0, where Q=16,769,025. For that impulse B's retained next S is Q/Q/0/0: output32 includes the impulse while its next pre-tail already excludes it. E01 ends at eight and covers startup, not 31-slot expiry. E02 maximum uninterrupted lengths are 335 and 380; E04 reaches 32,768 and includes each domain value eight times. These are genuine long finite checks, not exhaustive histories, unrestricted ranks, generation lifetimes, faults or schedules.

**Witness review.** Exact source reference for every row is `inputs/AP-EVALUATION-009.json#/experiments/numeric/source`, identified by its M label; observed values are under `/experiments/numeric/results/witnesses`.

| Group | Reproduced classification | Independently assessed scope |
| --- | --- | --- |
| M01 | Shortcut refuted | A premature overwrite gives 8 rather than 5; read before eviction. |
| M02 | Shortcut refuted | A wrong oldest cursor gives correct current 5, next 1 rather than 4. |
| M03 | Shortcut refuted | B same age error; S=sum(slots)=1 still holds, next 1 rather than 4. |
| M04 | Shortcut refuted | Frozen cursor: event32=5, event33=4, event34 faulty 4 rather than 0. |
| M05 | Shortcut refuted | Cleared tail/cursor with stale S=9 emits 9 rather than 0. |
| M06 | Shortcut refuted | Cleared S with stale expiring 1: first zero looks correct, next -1; unsigned wrap would be 4294967295. |
| M07 | Shortcut refuted | Injected tail-updated/S-stale state emits 0 rather than 4; no actual interrupt schedule tested. |
| M08 | Shortcut refuted | Injected S=4/zero-tail state never expires contribution; 33rd zero emits 4 rather than 0; no crash recovery realization. |
| M09 | Shortcut refuted | Mixed pre/post snapshot emits 9 rather than 5. |
| M10 | Shortcut refuted | Coherent post-event snapshot emits 8 rather than 5; atomicity alone is insufficient. |
| M11 | Shortcut refuted | Prior-sequence snapshot after reset emits 5 rather than 4. |
| M12 | Permutation confirmed | Correct-set reversal keeps current energy 5; does not prove chronology or future expiry. |
| M13 | Shortcut refuted | 65536 narrowed to 16 bits becomes accepted zero rather than REJECT. |
| M14 | Shortcut refuted | Invalid-as-zero changes final (32,1) to (33,0). |
| M15 | Shortcut refuted | Consumer restart is not detector reset: required (2,1), reset shortcut (1,0). |
| M16 | Shortcut refuted | Freshly accepting retry changes required (2,5) to (2,2); no physical retry protocol tested. |
| M17 | Shortcut refuted | Same energy-only restarted observation 0 needs n=1 versus n=2; narrow information impossibility, not universal AP impossibility. |
| M18 | Shortcut refuted | Old (1,1) cannot substitute for new (1,4); equal-energy ambiguity separately covered by race suite. |
| M19 | Shortcut refuted | 1 or 2 followed by 32 zeros have equal current numeric state/(33,0), but old debt differs (1,1)/(1,4). |
| M20 | Shortcut refuted | Two-bit rank/generation fields collide at 1/5 and 0/4; no safe reuse theorem without lifetime evidence. |
| M21 | Shortcut refuted | Q=2 entry-only stalled queue loses owed third (3,14), excluding other retention, replay, compression and acceptance coordination. |

Thus **21 groups = 20 refutations + one confirmation**. M07/M08 inject inconsistent abstract state; they do not execute an actual torn write or establish crash-schedule reachability. M17 is an indistinguishability argument at a specifically energy-only, association-starved restarted consumer, not an implemented decoder or universal RI impossibility. M19 concerns retained numeric state, not the oracle's full diagnostic history. M20 establishes a sole-field collision; a safe retirement/reuse argument might avoid coexistence but is unsupplied. M21 excludes additional storage, replay, compression and acceptance coordination; it does not prove every finite AP impossible.

The race source `/experiments/races/source` enumerates four legal acceptance/reset/publication orders for each of (1,2) and (1,1), **eight schedules** total. Preserving the observer ledger delivers both owed triples. Relabeling by current generation would fail in **six**, and clearing the then-pending ledger at reset would lose old work in **six**. The cancellation implementation is inferred from a recorded pending list; the program does not execute a complete destructive cancellation protocol. Equal values demonstrate old/new results may share both rank and energy. Sequence labels are observer instrumentation, not actual consumer information.

For the vulnerable logical-tail read, append is atomic between entry reads: cut0 reads all post-event entries and returns 8; cuts1..30 mix versions and return 9; cut31 reads all pre-event entries and returns required 5. **31/32 failures** is exact for this chosen cut model and witness, not a failure probability, all physical ring-buffer schedules or a working snapshot service.

The preliminary defect is separately disclosed in all three original outputs (report:73; briefing:25; JSON `/experiments/setup_correction`). Its single impulse had already ceased distinguishing the stale cursor. Final source changes that prefix to (1,2,29 zeros), and expected intermediate energies from 1/0 to 5/4; no other program difference was found. I replayed both versions, including the **entire completed corrected program**. Neither the failed run nor one repaired witness becomes formal verification.

**Candidate/gate assessments.** Each cell describes positive conditional/model evidence and the remaining full-scope gap. Every realized status is UNKNOWN. JSON records all six gates separately for each candidate.

| Gate | A | B | C |
| --- | --- | --- | --- |
| H1 exactness | Conditional pre-tail reduction, FINITE_MODEL agreement and ordered tail assertions; chosen-width realized transition absent. | Conditional ordered recurrence, FINITE_MODEL agreement and chronological S/tail assertions; coherent realized commitment absent. | Conditional reduction, FINITE_MODEL agreement only under assumed exact event-bound pre-tail; provider fidelity absent. |
| H2 startup/reset | FINITE_MODEL zero-tail/cursor reset; physical linearization and old debt exclusion absent. | FINITE_MODEL tail/S/cursor reset; partial reset/update and old debt handling unrealized. | FINITE_MODEL hypothetical service reset; real joint reset, old sessions/snapshots and restart fencing absent. |
| H3 indexed result/event | Conditional RI obligation only; no actual consumer/state/decoder or delivery contract. | Same RI gap plus coupled numeric commitment/publication. | Conditional RN decoding only; provider, framing, parser, accepted ordinal and response binding absent. |
| H4 invalid/observable faults | FINITE_MODEL reject branch preserves represented state; physical API/association/fault reports absent. | Same, including represented tail/S/cursor; actual complete pending state absent. | Harness rejects without service append/rank advance; real coordinated rejection and service-error behavior absent. |
| H5 <=2048 attributable bytes | Conditional raw31 + complete overhead expression; allocation/lifetime/stack bound absent. | Conditional square31 + S + complete overhead; allocation/lifetime/stack bound absent. | Conditional no local retained numeric tail; client/shared/pinned/stack ownership and peak bound absent. |
| H6 no hardware-FPU dependency | Conditional exact-integer intent; build/dependency/execution evidence absent. | Conditional exact-integer recurrence; build/dependency/execution evidence absent. | Conditional integer reduction; client/library/provider dependencies and build boundary absent. |

There is **no HOST_SPECIFIC realized-candidate allocation, timing, dependency or energy evidence**, and **no TARGET_SPECIFIC evidence**, for any of the 18 gate cells. Running Python on a host provides FINITE_MODEL evidence and reproducibility metadata, not host realization of the AP. A separate structured check confirmed every Stage-9 realized gate remains UNKNOWN with compatibility-grade PASS false, all realized F values UNKNOWN, all approval/qualification flags false and no VO discharged. Neither the briefing's “conditional numeric kernels” nor the dossiers promote finite success to physical PASS. C is consistently hypothetical across the three outputs. The shortcut counterexamples do not contradict the full conditional proposals.

**Consumer association, reset and feasibility.** R1 requires a decoder using information the actual consumer possesses, an accepted-event/result bijection, unrestricted accepted rank, and correct reset/restart association. A request handle identifies a request but supplies no rank by itself. An omniscient observer's stream length, harness return (n,E), or hypothetical service counter is not that decoder. An invalid acquisition or retry message cannot increment accepted rank. Zero prefixes expose ambiguity even when all numeric outputs are correct.

Numeric commitment and publication must be distinguished prospectively; already accepted work cannot be renamed unaccepted after loss. Every accepted valid event continues to owe its correctly associated logical result through stall, fault report, restart and reset. A fault report is not delivery; fresh acceptance of a retry is not recovery. This does not impose universal crash survival, exactly-once physical transport or permanent availability. Unsupported destruction/absence can leave debt unpaid; it does not demonstrate compliance.

Reset starts fresh numeric history and rank, while old debts remain distinguishable. Consumer restart alone does not reset the detector. A separate acknowledgment is optional; consumer-visible ordering/nonaliasing is mandatory. Draining, markers, versions and tags remain unselected possibilities, and a stalled drain has no proved completion guarantee. No finite epoch, mandatory reset, publisher pause/backpressure, valid-event loss or arbitrary lifetime cap follows from this review.

C needs an actual authorized provider binding current input, exact prior tail, accepted ordinal, reset context and output. Coherence alone can yield the wrong event; range/length validation cannot prove truth. Snapshot retention is needed until sufficient owed-result information is preserved or handed off; pins/copies/versioning/retries can extend lifetimes and costs. The ordinary publisher role does not supply those services. Missing contracts imply UNKNOWN feasibility, not universal impossibility.

**Theorem and resource audit.** T1 concerns equality of all nonempty future numeric outputs iff padded latest31 tails agree. It excludes the current already-emitted output, rank, old debt and full interface metadata. A's raw tail and B's injective square tail preserve those distinctions conditionally; S alone does not. C shifts their retention/retrieval into the joint system.

T2 applies at fixed n>=32 to complete deterministic retained output-affecting state with no external replay/readable uncounted history and unrestricted continuations. 4096^31=2^372, giving 372 information bits and ceil(372/8)=47 octets of capacity. This is **not sufficient 47-byte implementation RAM** and counts no particular layout, stack, scratch, index or output-debt mechanism. A/B numeric closure still requires evidence; external ordinal association alone cannot eliminate fixed-n numeric distinctions. C-DET reads C-HIST and fails local no-replay; a larger complete boundary could qualify only after every hypothesis is established. PO-003-1/3 remain UNPROVEN.

The Stage-9 symbolic RAM expressions are algebraically consistent with D002/R5 and the supplied worksheet:

~~~text
RAM_peak_c = max_t[P_c(t)+S_c(t)+K_c(t)+G_c(t)]
R_A = 31*b_x + h_A
R_B = 31*b_q + b_S + h_B
R_C = h_C
h_c = O_c + T_c + max_t[S_c+K_c+G_c]  (fixed complete payload only)
R_B-R_A = 31*(b_q-b_x)+b_S+h_B-h_A
~~~

P includes owned numeric/control/transaction/index/reset/debt state; S is non-stack scratch and buffers; K includes owned stack and callees; G is other attributable shared/pinned allocation. Count each live allocation once. A sum of separate maxima is not an exact simultaneous peak; claimed overlap savings require lifetimes. All b and h values are unknown representation sizes, not measured allocations. Raw/square/total capacities are 12/24/29 bits; Q=16,769,025, 31Q=519,839,775, 32Q=536,608,800<2^29. Correct widening, promotions, signs, packing and B's subtraction invariant remain unverified in a target language.

Stored ordinary binary rank grows as floor(log2 n)+1; pending debt, old reset contexts, concurrent snapshot versions/copies and retries can enlarge or nonlinearly change allocations. No constant h is established. Shared memory is not excluded merely because a publisher allocated it. Only established exclusive upstream ownership supports the R5 exclusion; upstream resources still require separate disclosure. C's local-history absence is conditional, not zero client or joint-system cost. No bound <=2048 follows.

M0 compute counts also reconcile: A/C 32 squares and 31 additions using a first-term-seeded reduction; B one square, one addition and one subtraction. This symbolic model is not literal Python instruction counting (Python's zero-seeded sum has its own work). The A-minus-B arithmetic projection is 31 SQ +30 ADD -SUB. Wider square traffic, S/cursor/result accesses, control/conversion, validation, accepted-index coordination, initialization, reset/rejection/fault/stall/retry work and pending work remain chargeable. C additionally needs snapshot fetch/open and provider/RN maintenance. One FETCH entry does not imply a separate transport round trip. The scalar sensitivity inequality has unknown coefficients and overhead; it establishes no complete compute dominance.

Device electrical energy is distinct from signal E_n. No cycles, joules, current, cost constants, hard power target or hard 1 ms deadline were supplied or invented. Compare the same target/build/workload/interval/attribution with equivalent opening and closing debt, or completion of equivalent owed work; otherwise deferred work can bias the result. Include initialization and lifecycle/fault work. For N=0 report interval totals without per-accepted division. Avoid double counting transport; validate additive pricing before reliance. Same-device upstream compute and electrical consumption do not disappear under a detector-RAM exclusion. Off-device service costs remain separately reported, not zero. Detector-only, whole-device and multi-device scopes must be reconciled. Therefore there is **no compatible full Pareto conclusion**, favorable tie or AP ranking. Flash remains inactive/unknown; no F weights or criteria changes are made.

**Findings and next eligible gate.** Severity denotes the consequence for later claims, separately from suitability of the current evidence referral.

| Finding | Severity | Result / exact source reference |
| --- | --- | --- |
| R010-1 | INFORMATIONAL | Completed numeric reproduction exact; `AP-EVALUATION-009.json#/experiments/numeric`, report:33, briefing:15. |
| R010-2 | LOW, corrected | Preliminary M04 source defect disclosed and independently reproduced; final complete rerun verified; JSON `/experiments/setup_correction`, report:73, briefing:25. No new source correction requested. |
| R010-3 | INFORMATIONAL | Witness/race counts exact within limited abstract boundaries; JSON `/experiments/numeric/results/witnesses` and `/experiments/races`. No physical protocol or statistical claim follows. |
| R010-4 | HIGH, OPEN | Actual consumer/index/acceptance/debt/reset/restart interface missing; R1:20,38; R1 disposition `/accepted_clarifications`; Stage-9 JSON `/interface_dependencies`. Blocks physical H3 and associated claims. |
| R010-5 | HIGH, OPEN | C provider, event binding, availability, retention and ownership absent; candidates:65; report:101; numeric source `HypotheticalC`; D002-2/3/5. |
| R010-6 | HIGH, OPEN | Full RAM/stack/build/no-FPU and comparable F evidence absent; report:171,204,235; F `/decision`; proof disposition `/accepted_mathematical_claims`. |
| R010-7 | INFORMATIONAL | Current-byte consistency established; historical provenance and OS/connector isolation unverified; current manifests and Stage-9 JSON `/source_hash_checks`, `/independence`. |

No material uncorrected evaluation-source defect or unsupported realized PASS was found. The corrected preliminary witness defect and the still-open engineering conditions are explicitly retained; readiness applies only to separate delegated **evidence** disposition.

| Obligation | Preserved status / evidence due |
| --- | --- |
| T002-2 | OPEN: later realized exactness versus independent specification before correctness claims. |
| T002-3 | OPEN: startup/reset, prior-history and old-work exclusion at lifecycle verification. |
| T002-4 | OPEN: actual decoder, accepted-event/result bijection, unrestricted rank and retained debt at interface verification. |
| T002-5 | OPEN: physical rejection invariance and applicable observable-fault reporting before input-contract compliance claims. |
| T002-6 | OPEN: complete attributable peak/stack and no-FPU build/dependency evidence; target evidence before target claims. |
| T002-7 | OPEN: compatible target/build/workload/attribution timing, compute and device-energy evidence before real-hardware claims. |
| T002-8 / R4 | OPEN/DEFERRED: authorized threshold/duration/boolean/integration criteria and verification before whole-detector claims. |
| PO-003-1 / PO-003-3 | UNPROVEN; no new theorem accepted. |

These preserve DECISION-TRACE-002:36 and current F/proof/D002/R1 dispositions; the original draft T002-1 next-gate wording is not evidence against the supplied later activation.

The immediate eligible step is a **separate delegated disposition of these reviewed evaluation artifacts**. The smallest proposed new evidence gate is an actual consumer information and acceptance/lifecycle inventory covering all three alternatives: identify the consumer and retained state, explicit decoder and accepted-event/result map, reset/restart observations, debt retention and safe identity reuse. Challenge hidden zero prefixes, invalid/retry counts, delayed equal old/new pairs and Q+1 debt before target expense. If C remains under investigation, a separately authorized provider capability/ownership inquiry should establish whether RN and exact event-bound history are available, with retention, reset, error and resource evidence. Neither proposed inquiry approves or creates a service. Only later separately authorized realization can provide chosen-width lifecycle/build/stack evidence and compatible debt-closed target measurements. This orders evidence tasks, not APs.

Only the two requested review outputs are written. **AP_selected=false; APs_finally_compliant=false; target_verified=false; product_verified=false; formal_cleanroom_qualified=false; vo_discharged=[].** No contract or external service is approved, no AP is selected, no CON/DE/C is started, and every verification obligation remains open.

