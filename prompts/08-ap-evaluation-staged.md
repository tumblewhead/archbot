# AE-002: Stage-aware architecture evaluation

Read AGENTS.md, agents/evaluation-agent.md and theory_of_operation.md. Begin at the AS-001 spine; follow the relation to VP-001 and the six VO documents. Read AS-001, unchanged F-001, candidate AP-001/AP-002, and accepted proof scope as available. Review AE-001 only as historical context and **do not modify it**.

1. Check graph links (`python tools/pc.py check --fast`).
2. Build an AP-stage evidence matrix for every C and R using five states: SATISFIED, CONDITIONALLY_SATISFIED, DEFERRED, UNRESOLVED, VIOLATED.
3. For C-002 specifically, establish a conservative whole-subsystem memory model. A 64-byte sample array is not a complete model. Enumerate additional state, stack, alignment, and unknown overhead; mark AP-stage evidence UNRESOLVED if its accounting boundary or credible estimate is missing.
4. For each DEFERRED item, cite VO id, due stage, method, owner, assumptions, and escalation. A requirement due later is never automatically DEFERRED.
5. Identify stage-admissible proposals only when all AP-stage obligations are satisfied or conditionally satisfied and all legitimate future obligations are documented. Apply F-001 unchanged to those proposals. If comparative evidence is missing, return NO_DOWNSELECTION and the smallest set of tests/analyses that would enable selection.
6. Create `knowledge/architecture/AS-001/evaluations/AE-002.md` and `reviews/AE-002.md`, link from spine using `evaluated_by`; no `selected` relation unless earned. Do not overwrite AE-001, AS-001, F-001, or accepted proofs.
7. Run checks/tests and report explicit gate outcome, conditions, and VOs carried forward.
