---
type: Figure of Merit
id: F-001
title: Detector architecture ranking policy
status: draft
tags: [merit, selection]
relations:
  - kind: addresses
    target: /architecture/AS-001/statement.md
---
# F-001: Predeclared selection policy

**Hard feasibility first:** all C-001..C-003 and R-001..R-003 must be met. Unmeasured or unknown properties are **UNRESOLVED**, not PASS.

For feasible candidates, prefer the Pareto frontier of (state SRAM bytes, worst-case cycles per update, flash bytes). If incomparable, request a documented stakeholder trade-off before selection. Do not invent target cycle numbers.

A proposal with better expected complexity is not declared the winner until evidence addresses performance on the target.
