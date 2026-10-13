# EVALUATE_AP: Reusable architecture evaluation playbook

**Applies to:** any Architecture Statement whose spine provides candidate APs, an F, applicable verification policy and VO/AD authority.

**Role:** `evaluation-agent`. **Scope:** evidence evaluation and recommendations, never automatic architectural approval.

## Inputs

Resolve the task's declared spine and initiating change/receipt. Retrieve current AS, F, the verification maturity plan, due-stage VO ledger, accepted theorem/decision receipts, candidate APs, and prior evaluations. Use selective traversal. If mandatory evidence is missing, report `UNRESOLVED`, not `PASS`.

## Procedure

1. Record source Git revision, active scope decisions, and the exact accepted evidence under review. Reject a stale acceptance receipt if its relevant source claims changed.
2. Detect the smallest affected set of obligations and proposals. Preserve earlier assessments and evaluation records as historical artifacts.
3. Create versioned, candidate-specific assessment packets: one record for each applicable AS requirement, with the AP-stage status, cited support, assumptions, final verification maturity, and carried VO.
4. Classify each AP-stage requirement as `SATISFIED`, `CONDITIONALLY_SATISFIED`, `DEFERRED`, `UNRESOLVED`, or `VIOLATED` under the authoritative project policy. Never defer an obligation whose evidence is due now.
5. Evaluate declared feasibility checks, including any domain-specific validator configured by policy. An allocation budget is not a measurement; an accepted mathematical theorem is not source-level C verification.
6. Only compare APs admissible at this stage. Use the predeclared F dimensions, distinguishing bounds, estimates, measured results, and missing dimensions. Do not fabricate a Pareto ranking.
7. If only an authorized provisional tradeoff can justify commitment, prepare a **proposed** Architectural Debt item and authority decision. No agent may accept its own debt or select an AP.
8. Produce a new versioned evaluation, update the architecture spine additively, and write a concise review receipt. Run the existing structural and applicable stage-gate checks.

## Possible outcomes

- `NO_DOWNSELECTION`: due evidence or authority missing, with minimal next action.
- `ELIGIBLE_FOR_INDEPENDENT_REVIEW`: candidate appears gate-admissible, awaits independent review.
- `AUTHORITY_DECISION_REQUIRED`: proposed risk/tradeoff would permit reversible commitment only after explicit approval.

Only a **separate accepted authority record** can mark an AP provisionally selected. Final firmware acceptance is a later, independent gate.

## Completion record

Include artifacts created, source revision, accepted assumptions, results of deterministic checks, all open VOs and proposed/accepted AD, the next eligible transition, and any uninspected datasets.

This playbook contains **no architecture identifier, hardware-specific limit, or special-case requirement**.
