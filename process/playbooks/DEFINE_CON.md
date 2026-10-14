# DEFINE_CON: Contract-first architectural decomposition

**Reusable operation:** `DEFINE_CON`
**Role:** `contract-agent`
**Inputs:** Task manifest, project spine, approved provisional or final AP selection,
applicable AS/P/F, current verification obligations, accepted architectural debt,
and the selected proposal's independently accepted assumptions.

## Authority and startup

1. Resolve the task's spine and the task-specific **accepted** selection receipt.
   Confirm selected AP, accepted AD, applicable VO ledger, and approval scope.
2. Refuse to treat an unapproved proposal, an agent recommendation, or a green
   structural check as authorization to design.
3. If accepted proofs depend on uncertain assumptions, turn the assumptions
   into explicit testable contracts. Preserve every due-stage obligation.
4. Follow only task-relevant spine relationships, expanding to required
   assumption and authority inputs, not to irrelevant raw histories.
   If the manifest names an active baseline, resolve its reviewed effective
   dependency links and **active VO ledger**, rather than treating an older
   spine edge or historical VO index as a current requirement.

## Contract-first construction

Define **externally observable contracts before designing DE internals**.

Every contract must define, as applicable:

- Stable ID, version, parent AS clauses and selected AP obligations.
- Producer/consumer and authority for each datum; representation, units,
  legal domain, ordering and reset/startup behavior. Include rate or
  timestamps **only when required by the approved AS or integration contract**;
  otherwise explicitly record that they are unspecified.
- Functional preconditions, postconditions, invariants and bounded failure
  behavior; never silently accept out-of-domain values.
- Concurrency, reentrancy, ISR/task ownership, mutation ordering and
  atomicity; any no-heap, non-nesting or single-writer assumptions.
- Execution-work bounds and any timing budget, execution context or
  interrupt interference **actually required** by approved authority.
  Do not manufacture a real-time deadline, ISR topology, independent
  watchdog, producer-loss protocol or concurrent-reader atomicity merely
  because those mechanisms appeared in an older draft. Explicitly mark
  unapproved integration details as unspecified.
- Resource allocation, category ownership, lifetime, stack/interrupt/shared
  attribution and no-double-counting rules. Treat allocation caps as
  contractual limits, not proven physical usage.
- The proof theorem(s) used, their exact domain assumptions, and the
  eventual implementation correspondence obligation.
- Verification plan: tests, proofs, static checks or target observations;
  acceptance thresholds, owner, due stage and fallback on failure.

Model inter-element collaboration explicitly as typed interfaces. Define
DE responsibility **placeholders** only once contracts are consistent.
A design element may refine internals later but may not change CON
semantics or redistribute budgets without an approved review.

## Assurance and outputs

- Create versioned OKF **draft** CON concepts and an interface/contract spine.
  Every artifact links to its AS, AP and relevant accepted mathematical evidence.
- Create versioned DE placeholders recording owners and adopted contracts,
  with no algorithm/source implementation yet.
- Produce a responsibility matrix mapping every inherited C/R and open VO
  to at least one contract and assigned DE/verification owner.
- Produce a contract review request and brief evidence receipt. Flag
  contradictions, unverifiable preconditions, unstated target behavior and
  uncategorized memory allocations as `UNRESOLVED`.
- Use the approved project's resource-envelope caps without changing them
  unilaterally; if credible enforcement is impossible, escalate for AP review.
- Do not write firmware, discharge VOs, accept new AD, claim final F performance,
  or declare contracts approved.

## Exit

`CONTRACTS_READY_FOR_INDEPENDENT_REVIEW` if complete and consistent,
otherwise `CONTRACTS_UNRESOLVED` with minimal blockers.

Run structural checks and applicable contract schema checks. No structural
PASS substitutes for independent contract acceptance. The next phase
(`DECOMPOSE_DE`) requires a separate accepted contract review receipt.

This playbook is deliberately hardware-agnostic. The particular MCU,
ADC, solver or scheduler requirements come from the task's **spine**.
