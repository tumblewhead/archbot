# CLN-001 TASK-REVIEW-AP-006: independent candidate-quality review

**Role:** new independent verification agent. Not the AP author, evaluator,
engineering sponsor/delegate, architect, or implementation author.
**Scope:** source and candidate-quality review of three *unselected*
architectural proposals for synthetic CLN-001, BEFORE any AP selection.
**Prior artifacts:** `AP-CANDIDATES-006.md`, `AP-COMPARISON-006.md`,
`AP-BRIEFING-006.md` all remain `AP_CANDIDATE_NOT_SELECTED`.

Use only `inputs/`, `TASK.md`, `AGENTS.md`. This is a positive-allowlist
diagnostic, not formally proven filesystem isolation. Do not retrieve
the solved original Toy 1 AP, F, code, historical reviews, other
workspaces, external datasets, network or evaluator.

## Review basis

The original three BKP files are invented/synthetic inputs.
D001 and activated AS-REV-002 grant exact 32-event sum-of-squares,
startup/reset, invalid-input state invariance, one indexed result
per accepted event, no hardware-FPU dependence, and a detector-owned
2048-byte RAM limit. R3's nominal 1 ms cadence is not a hard WCET
deadline; R4 full sustained-energy detection remains deferred.
F-DISPOSITION-003 grants H1–H6 gates and objective axes
`RAM_peak`, `compute_effort` and `device_energy_consumption`,
but supplies no weights, measurements or target. Mathematical
T1 applies to future numeric outputs, conditional T2's 372-bit
information capacity only to a complete deterministic **no-replay**
closed state boundary; T2 is not a 47-byte implementation.
D002 is an **accepted disclosure/refinement policy**, not an
accepted external index provider, bounded epoch or history service.

## Independent checks

1. **Independent proposal distinction.** Verify A's local 31 raw
   values + recomputation; B's 31 squared values plus tail aggregate
   + incremental total; C's publisher-owned consistent snapshot +
   detector-side computation. Challenge whether differences are
   architectural rather than merely cosmetic, and whether C
   assumes unapproved external capabilities as facts.
2. **All hard gates, for EACH AP.** Check H1 exactness of latest-32
   and arithmetic/range assumptions; H2 startup/reset; H3 one
   correct (n,E_n) indexed association per accepted event; H4
   invalid rejection without mutation, observable faults and
   report semantics; H5 all detector-owned persistent, scratch,
   stack, queues, index and shared attribution under 2048; H6
   no hardware-FPU dependency. No realized gate is PASS simply
   because its design is plausible. State which evidence is
   missing and whether any candidate contradicts a gate.
3. **B invariant challenge.** Independently write/check the proposed
   pre-event S=sum(last 31 squares), E=S+q_new, S_next=E-q_old
   including events n=1,31,32,33, reset, rejected sample,
   maximum values and a stale/corrupt order cursor. Distinguish
   a plausible algebraic invariant from a reviewed proof or
   representation-level signed overflow guarantee.
4. **A/C computation and service challenge.** Audit 32-square
   recomputation, tail age/eviction and C's exact accepted-history
   snapshot. C's snapshot consistency, ordinal generation,
   reset fencing, in-flight operations, no silent loss and
   source ownership are unverified dependencies. Determine
   what is impossible under *declared* assumptions and what
   is merely unproven/externally unsupported.
5. **Index refinement across all APs.** Check RI ordered-response
   rank interpretation and RN external exact numeral proposal
   against the AS demand to *supply* logical (n,E_n).
   Distinguish a mathematical abstraction map from physical
   caller/consumer guarantees. Mark any unresolved D003/AS
   clarification without silently approving RI/RN, wraps,
   epoch limits or accepting dropped valid events.
6. **Theorem applicability.** T1 concerns ONLY future numeric
   equivalence, not current output or full logical index.
   Conditional T2 applies to A/B only if their entire
   output-affecting numeric state is closed, with no replay.
   A C detector reading upstream history does not satisfy
   detector-local no-replay; total system may, with all
   retained sources included. Don't claim raw 31 samples
   are information-theoretically necessary, or that 47
   octets suffice for actual RAM.
7. **F worksheet.** Independently check A/B/C peak RAM expressions
   and ownership, typed counts (A 32 squares/31 adds, B one
   square/add/sub plus state upkeep under stated M0, C 32
   squares plus service work), startup/reset/error work,
   and device electrical energy as distinct from signal energy.
   Check no zero-cost omissions, hidden external cost, fabricated
   cycles, target power, WCET, flash budget or Pareto winner.
   Unknown or incompatible axes must remain UNKNOWN/incomparable.
8. **Obligation and authority fidelity.** Trace every AP to
   T002-2..8 and deferred R4. Identify which additional
   service/index/acceptance/ownership contracts require actual
   delegated authority before provisional downselection.
   A favorable review cannot select an AP or accept AD.
   Review whether the *next* stage should be an independent
   evidence/feasibility evaluation or an explicit D003
   requirements clarification, with source-linked reasoning.
9. **Independence/receipt honesty.** Record exact file source
   identities, checks performed, finite experiments if any,
   and which prior/runtime claims were NOT independently
   authenticated. Do not claim full cleanroom from a directory.

## Output ONLY these two files

- `out/REVIEW-AP-006.md`: candidate-by-candidate source
  audit, calculation challenges, concrete findings and
  counterexamples, severity/required corrections,
  unresolved gate/authority/evidence table, and next gate.
- `out/REVIEW-AP-006.json`: structured receipt with
  `review_id=CLN-001-REVIEW-AP-006`,
  `candidate_set=inputs/AP-CANDIDATES-006.md`,
  `disposition` one of:
  `READY_FOR_INDEPENDENT_AP_EVALUATION`,
  `REVISE_AP_DRAFTS`, or `UNRESOLVED`.
  Separate per-candidate findings and source/hash checks.
  Fields `AP_selected:false`, `APs_finally_compliant:false`,
  `all_candidate_hard_gate_compliance:UNKNOWN` (unless an
  actual contradiction is found, identify the contradicted gate),
  `cleanroom_qualified:false`, `target_verified:false`,
  `product_verified:false`, `vo_discharged:[]`.
  A READY verdict permits a later separately authorized AP
  evaluation, **not** an AP acceptance or selection.

Do not edit D001, AS, F, D002, original AP draft or prior proof;
do not author AE/CON/DE/C, award product qualification, self-select
a winner or accept debt.

**STOP after both review files exist.**
