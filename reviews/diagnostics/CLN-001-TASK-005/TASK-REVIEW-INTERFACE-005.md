# CLN-001 TASK-REVIEW-INTERFACE-005: independent D002 proposal review

**Role:** independent diagnostic interface and proof-applicability reviewer.
**Status:** authorized **review only**; no delegated engineering authority.
**Project:** CLN-001 synthetic pre-freeze diagnostic, not formal cleanroom.
**Candidate:** `inputs/INTERFACE-OPTIONS-005.md` and
`inputs/DECISION-PROPOSAL-005.yaml` with `BRIEFING-005.md`.
**Prior status:** D002-PROPOSAL-005 is `PROPOSED_NOT_APPROVED`.

Read `AGENTS.md`, `TASK.md`, `inputs/SHA256SUMS`, and only
the source files in `inputs/`. Do not access previous solved Toy 1,
old git history, other workspaces, external sources, connected apps
or hidden evaluator. Original BKP and versioned D001/AS/F/proof
dispositions are supplied explicitly as inputs.

## Review requirements

1. **Origin and authority.** Verify the Stage-5 agent preserves
   the exact accepted AS and D001 requirements, mathematical
   T1/T2 scope and accepted F objective definitions. Is D002
   visibly a new PROPOSAL, not an assumed existing decision?
   Are the six proposed disclosure clauses a process/contract
   refinement, or do any covertly impose new AS obligations?
2. **Information boundaries.** Audit options A (local history),
   B (exclusively upstream retained/readable history), and C
   (shared/unspecified service). In each, distinguish complete
   output-affecting retained information, detector-attributable
   RAM, consulted external resources, and full-system energy
   costs. Is the T2 no-replay hypothesis claimed ONLY for an
   actually complete closed named boundary? Check that sharing
   and detector readback cannot evade the state bound by
   uncounted external information.
3. **Index semantics.** Audit I (wider protocol), II (bounded
   detector index with explicit epoch/exhaustion semantics), and
   III (closed finite state internally generates exact unbounded
   natural-number index). Check that III's finite-state
   impossibility is a **conditional analysis**, not falsely
   recorded as accepted proof of PO-003-3 or an AS contradiction.
   Does proposal I rely on genuinely unspecified external
   protocol support? Does II require new delegated authority
   when it restricts otherwise-valid accepted events?
4. **Counterexamples and horizon.** Independently challenge
   sample-order examples, future-output versus current-output,
   zero padding, no-replay, finite horizons, index overflow
   and state/metadata ownership. If a specific example is false,
   identify a minimal counterexample with source line and scope.
   Do NOT quietly correct the author's outputs.
5. **F and resources.** Check all nine history/index combinations
   A-I...C-III against H1-H6 eligibility, declared
   `(RAM_peak,compute_effort,device_energy_consumption)`,
   compatible evidence scopes, shared RAM attribution and
   no fabricated timing/target metrics or Pareto winner.
   Distinguish signal energy from device electrical energy.
6. **Obligations/next gate.** Confirm T002-2..8 and R4 remain
   OPEN. Explain whether the recommended minimal disclosure
   policy can be separately adopted by the CLN-001 delegate
   **without** changing the AS or selecting an AP. List any
   clauses requiring AS clarification, new contract guarantees,
   formal proof, reviewer action, or additional human decisions.
7. **Audit of independence.** State the exact sources/hashes
   actually inspected, tests (if any), whether the reviewer is
   distinct from Stage-5 author, and limits. Working-directory
   isolation alone does not authenticate filesystem/connector
   reachability, actor identity or a formal cleanroom.

## Disposition

Choose EXACTLY one:
- `READY_FOR_DELEGATED_D002_DISPOSITION`
- `REVISE_PROPOSAL`
- `UNRESOLVED`

READY means only that the proposal is suitable for a **separate**
CLN-001 engineering decision; it does not bind or accept D002.

## Write ONLY

- `out/REVIEW-INTERFACE-005.md`: substantive clause-by-clause
  review, independent challenges, severities and fixes, source
  trace, limitations and next gate.
- `out/REVIEW-INTERFACE-005.json`: machine-readable receipt with
  `review_id=CLN-001-REVIEW-INTERFACE-005`, candidate, explicit
  disposition, findings/source references, source hashes, checks
  actually performed, independence limits, `d002_approved:false`,
  `as_modified:false`, `ap_selected:false`,
  `cleanroom_qualified:false`, `product_verified:false`,
  `vo_discharged:[]`.

**Stop.** Do not change D001/AS/F/proofs, approve D002, select
AP, generate CON/DE/C, or claim target qualification.
