# CLN-001 TASK-REVIEW-AP-EVALUATION-010: independent evaluation audit

**Role:** a NEW independent verification reviewer, distinct from Stage-9
evaluator, AP author/reviewer, delegate and selector. Synthetic pre-freeze
diagnostic; no formal cleanroom or product qualification. Review the
**Stage-9 evaluation evidence**, not the three APs as approval candidates.

Read only `AGENTS.md`, `TASK.md`, `inputs/SHA256SUMS` and supplied
`inputs/`. Never use old solved Toy 1 AP/CON/DE/C, another workspace,
Git history, network, connected apps or hidden evaluator. A directory
allowlist does not establish OS/connector isolation.

## Authoritative inputs and distinctions

Original D001/AS-REV-002 and its activation plus the separately
independently reviewed and delegated-accepted R1 AS addendum establish
the **actual consumer-decodable** `(n,E_n)` with accepted-result debt,
reset ordering/nonaliasing and optional distinct acknowledgment. D002
sets disclosure boundaries; F adopts H1–H6 and `RAM_peak`,
`compute_effort`, `device_energy_consumption`. T1 concerns future
numeric continuations, T2's 372-bit conditional complete-state
capacity is not a 47-byte implementation or detector-local bound
under external replay.

The evaluator's reports and JSON are author evidence, not an
accepted independent review. A/B/C remain **UNSELECTED**.
Every realized H1–H6 and all measured F values are UNKNOWN.

## Required independent review

1. **Source identities and scope.** Validate all supplied
   `inputs/SHA256SUMS` entries and the original Stage-9 MD/JSON/briefing
   against their separately supplied output SHA-256 manifest. Check
   the evaluator cited only inputs available in its source package,
   and distinguish current byte consistency from historical
   authenticated provenance and isolated execution.
2. **Independent numeric reproduction.** Inspect the `experiments.numeric.source`
   and `experiments.races.source` in the JSON before execution.
   Reproduce these precise source programs if safe and practical,
   capturing actual tool/interpreter, deterministic seeds, exit codes,
   test counts and discrepancies. Validate or challenge totals
   (299,296 accepted, 24,192 invalid, 11,386 resets,
   897,888 energy comparisons), model oracle independence,
   correct A/B chronological tails, conditional C snapshot service,
   startup versus expiration horizons and 32,768 uninterrupted events.
   If full rerun cannot be completed, report PARTIAL or UNREPRODUCED,
   not an invented pass.
3. **Witnesses and counterexamples.** Audit the claimed 21 witness
   groups, 20 refuting shortcuts, and one confirming permutation;
   verify counts versus source and the exact logical scope. Challenge
   B's wrong-age/current-E deception, torn updates and reset
   invariants, A early eviction, C mixed/wrong-version snapshots,
   zero-history/consumer restart ambiguity, old debt, finite-tag
   reuse, invalid-as-zero and queue exhaustion. Verify reported
   31/32 read-cut failures and eight abstract reset/publication
   schedules (six erroneous relabel/cancel cases each). No
   hypothetical harness state becomes an actual decoder/provider.
4. **Preliminary-run provenance.** Check whether the reported
   earlier failed M04 witness and corrected complete rerun are
   separately disclosed. Do not pool failed preliminary evidence
   into final counts or silently treat one changed witness as
   complete formal verification.
5. **Every realized hard gate.** For each A/B/C, evaluate H1–H6,
   separately describing conditional symbolic math, FINITE_MODEL
   evidence, HOST_SPECIFIC evidence and TARGET_SPECIFIC evidence.
   Explicitly test whether finite success was promoted to physical
   PASS or whether C's hypothetical snapshot became an asserted
   service. Source-review suitability is not AP selection/acceptance.
6. **Information and feasibility boundaries.** Challenge whether
   actual consumer index `n`, accepted-only event rank, reset
   association, old result debt and service availability are supplied
   by the evidence. Distinguish impossibility at a named
   information-starved boundary from universal AP impossibility;
   do not invent external RN, RI, C-HIST, crash recovery, finite
   epochs, mandatory reset or publisher backpressure.
7. **F and resource attribution.** Independently audit the
   RAM `max_t[P+S+K+G]` symbolic expressions, allocation lifetimes,
   stack, shared/pinned resources, ordinal/debt growth, typed
   arithmetic work and device electrical consumption. Test
   whether unknown ownership, upstream compute or device energy
   was misclassified as zero. Check compatible work, interval,
   target and pending-debt closure before any Pareto conclusion.
8. **Evidence-to-next-step gate.** Carry forward T002-2..8,
   deferred R4, PO-003-1/3 and proof scope. Recommend the smallest
   additional information/contract/evidence gate. Do NOT select
   an AP or make a provisional commitment. State source defects,
   material contradictions, reproductions and open conditions
   with severity and exact source references.

## Output ONLY

- `out/REVIEW-AP-EVALUATION-010.md`: independent audit, replay
  results/limits, candidate/gate table, counterexample review,
  F/theorem/resource audit, findings, next eligible gate.
- `out/REVIEW-AP-EVALUATION-010.json`: structured receipt with
  `review_id: "CLN-001-REVIEW-AP-EVALUATION-010"`,
  `disposition` one of
  `READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`,
  `REVISE_AP_EVALUATION` or `UNRESOLVED`.
  Include source hashes, replay commands/exits, counts,
  per-candidate/gate assessments, findings, open dependencies and
  follow-up. Explicitly set `AP_selected:false`,
  `APs_finally_compliant:false`, `target_verified:false`,
  `product_verified:false`, `formal_cleanroom_qualified:false`,
  `vo_discharged:[]`.

A READY result only permits **separate delegated evidence
disposition**, possibly a bounded follow-up experiment. It does
not mandate downselection or permit self-acceptance. STOP after
both review outputs. No CON/DE/C or implementation.
