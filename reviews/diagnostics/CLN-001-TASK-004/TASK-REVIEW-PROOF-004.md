# CLN-001 TASK-REVIEW-PROOF-004: independent mathematical proof review

**Role:** independent Proof Reviewer. Not Proof Scout, Proof Engineer,
AS/F decision-maker, or implementation author.
**Current status:** author claims `CLAIMED_PROOF_PENDING_REVIEW`.
**Review target:** `inputs/PROOF-ATTEMPT-004.md`, with
`inputs/PROOF-BRIEFING-004.md`.
**Scope:** PO-003-2's exact future-NUMERIC-output equivalence
and its conditional 2^372 retained-state information bound.
This is pre-freeze, synthetic CLN-001 diagnostic.

## Inputs and authority

Technical basis: `inputs/` only. Three original BKP files,
new sponsor-delegated D001, accepted synthetic
`AS-REV-002.md` and `AS-ACTIVATION-002.yaml`, trace,
`PO-OPPORTUNITIES-003.md`, first
`REVIEW-PO-003` report/receipt and the two Proof Engineer
outputs. Neutral `PROOF_REVIEWER_ROLE.md` supplies role, not
additional technical requirements. Do not open old solved Toy 1
artifacts, prior proofs, F/AP/CON/DE/C, original Git history,
other workspaces, network, external sources or hidden evaluator.

## Independent review procedure

Do not accept the author's proof by paraphrasing it. Rebuild these
from definitions and check the precise quantifiers and boundaries:

1. **Definitions:** D={0,...,4095}; arbitrary finite accepted
   histories including empty/startup; 31-padded oldest-to-newest
   tail t; EVERY nonempty continuation; numeric output at its LAST
   event. Current (empty continuation) energy and full logical
   output index are deliberately excluded. Reset defines a new
   epoch; invalid inputs do not create accepted events.
2. **Sufficiency:** independently derive the r=1..31 window as
   a suffix of t plus r continuation values; independently
   derive r>=32 (no historical contribution). Challenge r=1,
   31 and 32 and short/empty histories for off-by-one errors.
3. **Necessity:** show or refute recoverability of all 31 tail
   values from future zero continuations of lengths 1..31.
   Independently derive y_j and y_j-y_(j+1); verify unsigned
   square injectivity is used exactly where required.
   Determine whether all pairs of differing tails admit
   one distinguishing continuation.
4. **State bound:** establish or challenge that every 31-tail
   is reachable at the SAME accepted length n>=32, and that
   equal complete machine states force equal future numeric
   outputs under the additional deterministic/no-replay model.
   Check the 2^372 distinct states, bit/47-octet translation.
   Ensure no assumption that 47 bytes suffices for an actual
   detector; do not infer 2048-byte compliance.
5. **Countermodels:** scrutinize at least equal-current-energy
   unequal-tail histories, differing oldest of previous 32,
   signed-domain replacement, startup vs accepted zero,
   reset/invalid input semantics, replayable upstream data,
   readable prior outputs, externally supplied index, and
   finite epoch limit. Identify which change invalidates
   WHICH theorem or applicability statement.
6. **Executable supplement:** audit the claimed bounded Python
   checks and their reported counts/scope. If you execute an
   independently authored test, report exact command, inputs,
   environment and result. Tests are not universal proofs.
7. **Independence/source integrity:** verify the listed pinned
   source hashes and author artifact identities against inputs.
   State which original historical conditions, external identities
   and host isolation you did NOT verify. Directory restriction
   is not evidence of an OS-level cleanroom.
8. **Separation:** A review may find T1/T2 mathematically sound
   while their no-replay information boundary is not an accepted
   realization restriction. Keep PO-003-3 (unbounded exact
   index in a finite closed machine) distinct and unproven.
   Mathematical proof acceptance never discharges T002-2..8,
   proves RAM/timing/power, selects an AP or establishes
   a complete detector.

Review the theorem **as stated**, without strengthening it,
silently changing the accepted AS or inserting a restricted
maximum epoch length. For any blocking flaw, identify the first
invalid line, minimal counterexample or missing hypothesis, and
whether a bounded repair is possible. Do not edit author artifacts.

## Required outputs (only these two)

- `out/REVIEW-PROOF-004.md`: theorem-by-theorem T1/T2 disposition
  with independently reconstructed key equations, numbered
  findings, audit of edge cases and author checks, source/hypothesis
  applicability, remaining obligations and next gate.
- `out/REVIEW-PROOF-004.json`: a machine-readable receipt with:
  `review_id=CLN-001-REVIEW-PROOF-004`,
  `candidate=inputs/PROOF-ATTEMPT-004.md`,
  `disposition` from `ACCEPT`,
  `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, `REJECT`,
  `UNRESOLVED`; scope of mathematical acceptance;
  per-theorem findings, source hashes, independent checks actually
  performed, explicit assumptions, limitations/independence,
  `cleanroom_qualified=false`,
  `product_verified=false`, `vo_discharged=[]`,
  `implementation_verified=false`.

Even an ACCEPT applies to the EXACT conditional mathematical
T1/T2 propositions only. No subsequent Proof Engineer, AP/CON/DE/C
or product qualification may run from this review automatically.

**Stop after these two output files.**
