# CLN-001 TASK-PROOF-004: prove/refute PO-003-2

**Status:** Authorized **proof attempt only**; theorem NOT yet accepted.
**Role:** Distinct Proof Engineer, neither author nor opportunity reviewer.
**Project:** CLN-001 synthetic diagnostic energy-computation primitive.
**Selected opportunity:** PO-003-2, future numeric output equivalence
and retained-state cardinality under its explicit no-replay model.
**Evidence limit:** All inputs must come from local `inputs/`, no prior
solved Toy 1 solution, proof, code, Git history or evaluator.

## Inputs and exact scope

- Original unsolved BKP: `problem-origin.md`, `adc.md`, `target.md`.
- Newly delegated `DECISION-001.yaml`; accepted scoped
  `AS-REV-002.md`, `DECISION-TRACE-002.md`,
  `AS-ACTIVATION-002.yaml`.
- Scout `PO-OPPORTUNITIES-003.md` and
  `PO-BRIEFING-003.md` (all three remain UNPROVEN).
- Independent `REVIEW-PO-003.md` and `REVIEW-PO-003.json`;
  verdict READY_FOR_PROOF_ENGINEER, which is **not proof**.

Keep the potential unbounded indexed-output problem in PO-003-3
visible as separate future interface clarification, not part of
the numeric-only theorem. Do not modify the accepted AS.

## Statement to establish or refute

Let `D={0,...,4095}`. For any finite valid history `h`,
let `t(h) in D^31` be its latest 31 values with startup
left-padding by zeros, ordered oldest to newest.
For each **nonempty** continuation `u in D^+`,
let `F_h(u)` be the **numeric** energy observed on the last
accepted event of `u` after `h`, not the full pair
`(index, energy)` and not any previously emitted current output.

Claim:
`forall h,g: [forall nonempty u, F_h(u)=F_g(u)] iff t(h)=t(g)`.

Conditional consequence for any fixed accepted length `n>=32`
and deterministic retained-state machine with complete information
in its state and current input, no replay of old source histories,
output logs or external oracle: at least `|D|^31=2^372`
distinguishable reachable retained states, hence >=372 bits of
information in that model. This excludes full-interface logical
index, fault metadata, stack/scratch, alignment and real SRAM fit.

## Required analysis

1. Write precise definitions of accepted epoch, padded history,
   continuation, energy observation, state equivalence and permitted
   information sources. Handle reset only by starting a fresh epoch;
   invalid input events must not masquerade as accepted samples.
2. Prove (or refute) **sufficiency** for every length of nonempty
   continuation. Split `1<=|u|<=31` and `|u|>=32`, including
   the boundary and startup tails.
3. Prove (or refute) **necessity** by zero continuations of length
   1..31, deriving suffix-square values from observed energy.
   Audit off-by-one indexing and squaring's injectivity only on D.
4. Prove (or refute) fixed-length reachability for all 31-tails
   at `n>=32`. Apply distinguishability using two histories
   with same index, so the index cannot fake the lower bound.
   Translate the cardinality into minimum information bits and
   minimum whole octets but **not** an implementation allocation.
5. Challenge with concrete counterexamples and weakened assumptions:
   histories same current energy/different tails, differing oldest
   of previous 32, signed ADC domain, upstream replay/external output,
   zero-padded startup, current-vs-future output scope, reset/invalid.
   If any claim fails, give a minimal counterexample and bounded
   corrected statement rather than modifying authority.
6. Explain exactly how a later realization might violate no-replay,
   external-state assumptions or fail the full indexed interface.
   Maintain T002 obligations including R4 whole-detector deferral.
7. Optional finite bounded executable checks may supplement, not
   replace, the universal mathematical argument. If tests are
   actually run, state command, scope, parameters and result.
   Do not claim target tests, arbitrary-history coverage, external
   proof acceptance or feasibility.

## Outputs: only these files

- `out/PROOF-ATTEMPT-004.md` containing definitions, formal theorem/
  conditional theorem or counterexample, line-by-line reasoning,
  assumptions, lemmas and dependency graph, edge challenges,
  claim evidence classification, references and limitations.
  Give the author's assessment `CLAIMED_PROOF_PENDING_REVIEW`,
  `COUNTEREXAMPLE_FOUND`, or `UNRESOLVED`, not
  `PROVEN_ACCEPTED`.
- `out/PROOF-BRIEFING-004.md` with exact inspected file hashes,
  outputs, any actual tests, reviewer questions, open applicability
  requirements and required distinct proof-review gate.

**Stop after writing exactly these two artifacts.**
Do not select AP, accept F, modify existing decisions, implement C,
review your own proof, claim hardware compliance or qualify cleanroom.
