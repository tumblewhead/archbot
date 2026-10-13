---
type: Verification Plan
id: VP-001
title: AS-001 staged evidence requirements
status: draft
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-001.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-002.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-003.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-004.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-005.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-006.md
---
# VP-001: Stage-appropriate evidence

This plan annotates AS-001 without modifying its historical text. All original hard constraints remain binding. `first_assessable_at` and `verification_due_at` are process-specific metadata, not standard OKF fields.

| Requirement | First assessable | Final due | AP-stage evidence | Final evidence |
|---|---|---|---|---|
| C-001 | AS | AS | ADC domain from BKP | BKP specification |
| C-002 | AP | IMPLEMENTATION | Conservative complete-memory budget and margin, with named unknowns | Map/static accounting plus stack and runtime bounds |
| C-003 | AP | IMPLEMENTATION | Integer-only algorithm | Build/inspection confirms no reliance on FPU |
| R-001 | AP | TARGET_VALIDATION | Bounded work model and credible 1-ms timing plan | WCET argument or representative target timing with margin |
| R-002 | AP | IMPLEMENTATION | Abstract correctness proof or explicit AP-stage demonstration | C-to-model correspondence and integration tests |
| R-003 | AP | IMPLEMENTATION | Universal mathematical bound with assumptions | C expression-type and state-invariant verification |

**C-002 scope to resolve at AP gate:** define which bytes count in the 2048-byte budget, including persistent state, call stack, interrupt context and shared services where charged to the detector. A model that omits an unbounded contributor is `UNRESOLVED`, not `DEFERRED`.

**Gate rule:** AP-stage requirements must have acceptable stage evidence. `DEFERRED` only applies when the due stage is later and a credible method, owner, assumptions, and escalation are recorded. `VIOLATED` never advances. The original F-001 hard conditions and Pareto dimensions do not change.
