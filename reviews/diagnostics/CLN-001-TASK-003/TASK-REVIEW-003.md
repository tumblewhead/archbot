# CLN-001 TASK-REVIEW-003: independent Stage-3 scope review

**Role:** new verification reviewer, independent of both Stage-3 authors.
**Scope:** pre-freeze synthetic CLN-001 diagnostic; no formal cleanroom.
**Evidence:** only `inputs/` and this task. Do not access prior solved Toy 1
solutions, proof reviews, AP/CON/DE/C, Git history, hidden rubric or network.

Inspect independently:
- three original BKP documents;
- D001 synthetic decisions; AS-REV-002, TRACE-002 and ACT-002;
- TASK-PO-SCOUT-003.md, TASK-FOM-003.md;
- PO-OPPORTUNITIES-003.md, PO-BRIEFING-003.md;
- F-DRAFT-003.md, F-TRACE-003.md.

You are reviewing **two draft products**, not performing their roles.
Produce two **separately scoped** reviews and independent verdicts.
Use the supplied source hashes in your receipts. The supplied
SHA256SUMS checks byte consistency, not authenticated isolation.

## A. Proof-opportunity quality, not proof acceptance

For EACH PO-003-1, PO-003-2, PO-003-3:
- Verify it is genuinely an unproven candidate, with precise quantifiers,
  hypotheses, proof route, adversarial challenges and scope limitations.
- Independently check algebra and quantifiers for obvious counterexamples.
- In PO-003-1 audit startup and outgoing-sample indexing, extremal
  bounds, and arithmetic intermediate width claims. Report distinction
  between mathematical bounds and language/implementation overflow.
- In PO-003-2 challenge the future-output equivalence as stated using
  `F_h(u)` for nonempty continuations, the 31-tail necessity/sufficiency,
  same-length reachability, square injectivity and the no-replay model.
  Examine recovery using 1..31 appended zeros, not merely intuition.
- In PO-003-3 challenge the finite-state index impossibility against
  the added closed-machine assumptions. Distinguish a possible
  full-interface specification gap from an unconditional AS defect.
  A nominal 1 ms interval is not a maximum epoch length.
- Report which opportunity would have the highest **next proof ROI**,
  with explicit priority/rationale and counterexample risks.
- Do not declare any mathematical proposition proved or accepted.
  If a proposition is false or incomplete, give a concrete counterexample
  or a bounded gap, and classify it honestly. Do not covertly edit the PO.

Proof-opportunity verdict:
`READY_FOR_PROOF_ENGINEER`, `REVISE_OPPORTUNITIES`, or `UNRESOLVED`.
Even READY authorizes **a later distinct proof task**, not a proved theorem.

## B. Figure-of-Merit candidate, not F acceptance

- Check H1..H6 exactly inherit D001/AS constraints without adding
  a hard WCET, a software-FP ban or target performance requirements.
- Check P1 vector `RAM_peak, compute_effort, energy` is explicitly
  proposed. Decide whether 'energy' as an active axis or RAM minimization
  within the 2048-byte ceiling requires a *new authority decision*.
  The BKP expresses RAM and compute conservation, not an approved
  quantitative energy objective; do not silently elevate energy.
- Check units, cost-model comparability and lifetime/owned-stack RAM
  accounting; don't invent measured bytes, cycles, energy, power.
- Check F partial order with evidence-scoped UNKNOWN, constraints-first,
  symbolic vs later target results, incompatible workloads, and no
  fabricated scalar weights.
- Check trace of T002-2..T002-8, especially R4 deferred whole detector.
- Distinguish reviewer advice from actual F acceptance and missing
  authority. No architectural proposal or selection is allowed.

F disposition:
`READY_FOR_DELEGATED_F_DISPOSITION`, `REVISE_F_DRAFT`, or `UNRESOLVED`.
Even READY is only readiness for sponsor-delegate disposition.

## Outputs (write only these four)

- `out/REVIEW-PO-003.md`
- `out/REVIEW-PO-003.json`
- `out/REVIEW-F-003.md`
- `out/REVIEW-F-003.json`

Each JSON must have unique review_id, candidate, disposition,
disposition_scope, source hashes, findings (severity, source refs,
required action), checks actually performed, reviewer independence
limits, next gate, and `cleanroom_qualified:false`,
`product_verified:false`, `vo_discharged:[]`.
State `proofs_accepted:false`; for F state `f_accepted:false`.
A reviewer cannot grant sponsor-delegate authority to itself.

**Stop** after four outputs. No proof derivation claimed as checked
external evidence, F approval, AP selection, code or further roles.
