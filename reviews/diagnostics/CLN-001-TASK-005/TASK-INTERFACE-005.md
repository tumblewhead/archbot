# CLN-001 TASK-INTERFACE-005: theorem applicability and output-index boundary

**Status:** authorized bounded pre-AP diagnostic analysis, NOT an AS amendment.
**Role:** independent-of-prior-authors interface and proof-applicability analyst.
**Authority:** accepted synthetic CLN-001 AS, D001 sponsor-delegate decisions,
accepted diagnostic F and scoped mathematical T1/T2 disposition.
**No new technical authority is delegated to this agent.**

## Why this task exists

T1 is accepted for future NUMERIC output equivalence: histories have
the same future numeric energies for every nonempty continuation iff
their padded ordered 31-tails agree. T2 is accepted only under
determinism, complete accounted retained information, unrestricted
future continuations and NO uncounted history replay/readback.
`2^372` distinguishable configurations and 372 information bits
are NOT a proven detector-local SRAM lower bound.

The accepted AS specifies `(n,E_n)` for each accepted event with n
a logical index, without prescribing a stored counter, bounded epoch,
external association mechanism or index encoding. R5 counts the
detector's owned persistent state, scratch and owned stack under
2048 bytes, but excludes memory owned exclusively upstream.
PO-003-3's unbounded-index impossibility remains UNPROVEN.

## Allowed technical inputs

Read `AGENTS.md`, `TASK.md`, and only the positive-allowlist sources
in `inputs/`: three original unsolved BKP files, D001, accepted
AS-REV-002, DECISION-TRACE-002, AS-ACTIVATION-002,
F-DISPOSITION-003, and PROOF-DISPOSITION-004.
The mathematical propositions' accepted scope is stated by
PROOF-DISPOSITION-004. Do NOT import earlier solved Toy 1 code,
architectural proposals, proofs, budgets, decisions, evaluator,
repository history, other workspaces, or network information.

## Questions to analyze, without deciding them

1. **Information boundary and replay.** Compare at least:
   A. Detector owns sufficient state and receives only the new
      accepted sample (no readback of older publisher values).
   B. Upstream publisher retains history and offers explicit,
      charged-to-upstream readback/replay.
   C. An explicitly *shared* or externally retained information
      service, with ownership/access and costs not yet fixed.
   For each, state precisely whether A4/no-replay is satisfied;
   where the T2 lower bound applies (complete system vs
   detector-local); the latency/energy/RAM-accounting implications;
   and the needed interface evidence. Do not declare any one
   implementation faster or smaller without a model.
2. **Logical-index interpretation.** Compare:
   I. Logical n as a mathematical event association supplied by a
      wider publisher/consumer protocol, without detector-generated
      unbounded integers.
   II. Detector-generated finite-width index and an EXPLICIT bounded
      epoch length or specified error behavior before exhaustion.
   III. Literal exact natural-number n for arbitrarily long epochs
      generated solely by finite closed internal state.
   Clearly distinguish the accepted *abstract* PS from candidate
   concrete contracts. Analyze when III is impossible under the
   closed-machine assumptions, without calling PO-003-3 proven.
   Never invent a lifetime, wrap rule, external index or new hard
   1ms deadline as existing authority.
3. **Specification compatibility.** Identify what is already
   permitted by D001/AS; which variants need an explicit new
   synthetic decision, additive AS clarification, or separate
   contract; and what would require independent review.
   Prefer preserving exact numeric outputs, startup/reset,
   invalid-input state invariance and no silently padded losses.
4. **Figure of Merit.** For each information/index combination,
   label RAM_peak, compute_effort and device_energy_consumption
   with conditional symbolic considerations and UNKNOWN target
   values. Distinguish resource ownership from resources consulted.
   Don't infer universal Pareto ranking or target fit.
5. **Applicability register.** Provide the precise assumptions
   under which T1/T2 can be applied to an AP and when they cannot.
   Track T002-2..8, especially R4 deferred whole-detector detection.
   Explain what a later AP comparison needs as evidence.
6. **Recommendation and decision handoff.** Recommend a minimally
   constraining, auditable interpretation for the synthetic
   diagnostic, with alternatives and consequences, and a draft
   numbered decision **PROPOSAL ONLY**. It must not silently
   narrow the AS or bind the delegate. Also report any actual
   contradiction requiring renewed AS-level review.

## Outputs, only these three files

- `out/INTERFACE-OPTIONS-005.md`: grounded option matrix, analysis
  of theorem applicability and exact index semantics, resource/
  assumption boundaries, countermodels and F/VO crosswalk.
- `out/DECISION-PROPOSAL-005.yaml`: status `PROPOSED_NOT_APPROVED`;
  proposed new diagnostic decision, alternatives, source references,
  due-stage obligations, review and authority gates.
- `out/BRIEFING-005.md`: exact inspected source identities/hashes,
  what was and wasn't examined, requested independent review,
  unresolved questions, and stop statement.

**Stop** after the three outputs. No AS edits, no accepted D002,
no new theorem, AP selection, CON/DE/C or target feasibility claim.
