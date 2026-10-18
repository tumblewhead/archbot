# CLN-001 TASK-PO-SCOUT-003: first fresh proof opportunity discovery

**Role:** Proof Scout, not Proof Engineer and not reviewer.
**Status:** AUTHORIZED DRAFT OPPORTUNITY DISCOVERY ONLY.
**Project:** synthetic CLN-001 diagnostic, current accepted AS-REV-002.
**Authoritative sources:** read only `inputs/`, then `AGENTS.md`.
**Do not retrieve** any older solved Toy 1 materials, older Po/F/AP/CON/DE/C,
legacy Git tree or evaluator. No network needed.

## Inputs

The external workspace's `inputs/` contains original three BKP
problem inputs, the new CLN-001 sponsor-delegated D001 requirements
record, accepted AS-REV-002, its decision trace and the additive
AS-ACTIVATION-002 record. Paths are filenames within `inputs/`.
They are a **synthetic accepted specification**, not accepted design,
proven theorem or measured hardware.

## Task

1. Restate the precise mathematical observable contract for accepted
   samples, reset, invalid values, and the latest-32 window. Reference
   clause/source IDs; distinguish model assumption from guaranteed
   product behavior.
2. Find **one to three** high-value proof opportunities that could
   influence a later architecture comparison or bound realization risk.
   Opportunities may concern exactness invariants, quantitative
   ranges, state sufficiency, memory feasibility, update complexity or
   impossibility under a precisely stated model. **Do not preselect**
   a winning algorithm or implementation.
3. For EACH opportunity: give ID, crisp proposition with quantifiers,
   defined state/domain, assumptions, potential architectural value,
   prospective proof strategy, an attempted counterexample or
   adversarial edge case, missing facts, and required independent
   proof/review evidence. Explicitly label `UNPROVEN` even when a
   derivation appears straightforward. Do not smuggle hypotheses in
   as already proven lemmas.
4. Distinguish `D001` granted constraints (exact output, RAM <=2048,
   no FPU hardware dependency) from speculative optimization
   opportunities. No target hardware evidence exists.
5. Preserve deferred whole-detector detection R4, and open T002
   verification obligations. Their presence must not be erased merely
   because a proposition applies to the numeric primitive.
6. Mark scope, provenance and classification limits. Include one
   Mermaid diagram only if it removes ambiguity in state/observation
   relationships.

## Output files (ONLY these)

- `out/PO-OPPORTUNITIES-003.md`: 1–3 candidate propositions with
  equations, assumptions, proof routes, counterexamples, evidence
  classification and exact source trace.
- `out/PO-BRIEFING-003.md`: examined source files with hashes,
  outputs, open questions and recommended next independent proof task.

**Forbidden:** proving acceptance; selecting AP/F, introducing new
requirements, altering the AS/D001, measuring or claiming hardware
feasibility, implementing C, editing `inputs/`, writing outside
`out/`, or calling this formal cleanroom qualified.

**Stop** after generating both files. No review or downstream role.
