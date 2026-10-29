# EGM-P0 independent checker and P1 projection audit

**Scope:** one independent source/evidence review, not general
framework acceptance or a requirement to rerun Toy1.

Use only `AGENTS.md`, `TASK.md`, `inputs/SHA256SUMS` and
its source-pinned files. Distinct from the author/test reporter.

1. Inspect `inputs/assess.py`, `inputs/test_assess.py`, and
   `inputs/P0_USER_TEST_REPORT_001.json`. Independently run the
   10-test suite with assertions enabled and record exact command,
   interpreter, counts, stdout/stderr and exit code. A user-reported
   10/10 is not itself a separate independent review.
2. Challenge comparator scope: missing typed edges, proof conditions,
   source allowlist, duplicate keys and IDs, unsupported assertions,
   malformed JSON and explicit UNKNOWN. Identify false-positive
   structural matches, valid semantic alternatives it might reject,
   and whether it ever grants authority or claims runtime isolation.
3. Inspect all three proposed source docs, `SPINE.md`,
   `TASK_GOLDFISH.md` and `REFERENCE.json`. For each expected fact
   and edge in the author-created reference, require source-backed
   provenance. Flag underdetermined classifications and inferred
   relations; do not declare the reference automatically canonical.
4. Inspect `prepare_p1.sh` and `evaluate_p1.sh` without executing
   a Goldfish. Check intended allowlist, source pins, worker-only
   vs evaluator-only material, error exits and whether the scripts
   actually establish runtime filesystem/network isolation. A fresh
   directory does NOT.
5. Recommend the smallest fix or say if the source-pinned **P1
   diagnostic** can proceed with clear limits. Do not turn EGM into
   a mandatory gate, self-authorize worker tooling, access old Toy1
   solved source or rewrite protected files.

Output ONLY:
- `out/REVIEW_EGM_P0_001.md`: tested claims, actual commands/exits,
  exact source evidence, reference fidelity concerns and next action.
- `out/REVIEW_EGM_P0_001.json`: `review_id` equal to
  `EGM-P0-REVIEW-001`; `disposition` one of
  `READY_FOR_SCOPED_EGM_P1_DIAGNOSTIC`, `REVISE_P0_P1_INPUTS`,
  `UNRESOLVED`; source hashes, commands, exit statuses, findings,
  and flags `structural_match_is_semantic_proof:false`,
  `authority_accepted:false`, `runtime_isolation_verified:false`,
  `generic_gate_activated:false`.

STOP after both review outputs. A favorable review permits the
source-bounded *diagnostic* pilot only; it does not qualify Goldfish
isolation, semantics or general process authority.
