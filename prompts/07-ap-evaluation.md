# AP-001 versus AP-002: evidence-grounded downselection review

Read `AGENTS.md`, `agents/evaluation-agent.md`, and (because this task evaluates process compliance) `theory_of_operation.md` if present. Start at `/architecture/AS-001/spine.md` with the `evaluation-agent` view. If the proof-review artifact or machine-readable gate record is not in the view, load only those specific documents and record why.

1. Run `python tools/pc.py check --fast` and the evaluation-agent spine view.
2. Review AS-001, F, AP-001 and AP-002 and the independent proof acceptance PR-002. If `reviews/gates/proof-PR-002.json` exists, check its SHA-256 `source_sha256` against the actual PR-002 and report any mismatch.
3. Construct an AS constraint/requirement compliance matrix, with `PASS`, `FAIL`, `UNRESOLVED` for *each candidate*; cite the exact underlying artifacts and evidence. An accepted abstract theorem does not establish execution time or C compliance.
4. Apply the *existing, predeclared* F only to candidates that satisfy all hard constraints. Do not alter its weights, criteria, or thresholds. If F cannot yet choose, explicitly return `NO_DOWNSELECTION` and identify the minimum missing evidence.
5. Create a versioned `knowledge/architecture/AS-001/evaluations/AE-001.md` and `reviews/AE-001.md`, with any needed typed relations added to the spine. Do not create a `selected` relation unless selection is justified by the applicable gate.
6. Run structural checks and unit tests. Do not modify AS, F, the accepted proof, or firmware.

Report exactly what was and was not established, including scope restrictions and any missing target measurements.
