---
type: Architecture Decision
id: AP-002-SELECTION-001
title: Approved provisional selection for CON-first decomposition
status: stable
sources:
  - id: evaluation
    resource: /architecture/AS-001/evaluations/AE-004.md
    title: Post VO-001 architecture evaluation
  - id: proof
    resource: /architecture/AS-001/proofs/PR-002.md
    title: Abstract proof acceptance
relations:
  - kind: selected
    target: /architecture/AS-001/proposals/AP-002.md
  - kind: addresses
    target: /architecture/AS-001/statement.md
  - kind: evaluated_by
    target: /architecture/AS-001/merit.md
  - kind: supported_by
    target: /architecture/AS-001/evaluations/AE-004.md
  - kind: constrained_by
    target: /architecture/AS-001/decisions/C-002-SCOPE-001.md
  - kind: assumes
    target: /architecture/AS-001/verification_plan.md
---

# Provisional architectural commitment

**Selected for decomposition:** [AP-002](/architecture/AS-001/proposals/AP-002.md).

**Authority:** `process/decisions/AP-002-PROVISIONAL-SELECTION-001.yaml`
and companion `process/decisions/AP-002-PROVISIONAL-SELECTION-001.md`.

This selection is provisional, not a claim of final F-001 optimality.
The evaluated evidence supports the architecture-stage obligations under
specified assumptions.[^evaluation] The accepted theorem scope remains
abstract, not verified C firmware.[^proof]

## Inherited obligations

- Preserve C-002's 2048-byte detector-attributable SRAM boundary.
- Preserve 1 ms cadence, exact zero-padded squared sum, no overflow and
  no FPU reliance.
- Carry open VO-002 through VO-006 into contracts and later stages.
- Record accepted AD-003 and its deadline before final acceptance.
- Reopen affected decisions if a key assumption is contradicted.

[^evaluation]: AE-004 evaluation and its independent review
[^proof]: PR-002 abstract proof review
