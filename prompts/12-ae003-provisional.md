# AE-003: Provisional AP selection under Progressive Concretization v2

Read `AGENTS.md`, `agents/evaluation-agent.md`, `theory_of_operation.md` and
`process/policies/AP_SELECTION_v2.yaml`. Start at the AS spine and inspect
AS-001, F-001, proof acceptance, AP-001, AP-002, VP, VO/AD ledgers, AE-001,
AE-002, EP-001 and EP-002. Preserve history.

First verify that C-002's scope is explicitly approved. If it is not, report
`NO_DOWNSELECTION`, identify the needed authority decision, and stop short of
selection. If approved, build a candidate-specific AP-stage evidence matrix
including conservative memory envelope, abstract correctness and intermediate
bounds, work model and explicit future verification obligations.

Distinguish provisional AP commitment from final F-001 ranking. If F components
are unknown/incomparable, obtain a documented authorized provisional tradeoff,
record its architectural debt, and do not claim a Pareto winner.

Produce AE-003 with cited sources, outstanding VOs, accepted AD risks and exact
revisit triggers. Run the deterministic stage gate on a completed assessment
packet and structural tests. The gate script checks policy completeness but does
not replace independent acceptance. Do not select by default, invent missing
approval, weaken AS/F or rewrite earlier evaluations.
