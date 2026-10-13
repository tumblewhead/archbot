---
type: Architecture Statement
id: AS-001
title: Exact sliding-window squared-sum detector
status: draft
tags: [as, firmware]
sources:
  - id: adc
    resource: /bkp/adc.md
    title: Hypothetical ADC specification
  - id: target
    resource: /bkp/target.md
    title: MCU budget assumption
  - id: need
    resource: /bkp/problem-origin.md
    title: Toy stakeholder decision
relations:
  - kind: constrained_by
    target: /bkp/adc.md
  - kind: constrained_by
    target: /bkp/target.md
  - kind: motivated_by
    target: /bkp/problem-origin.md
---
# AS = (C, R, PS)

## Constraints

- **C-001:** All ADC samples are unsigned 12-bit integers, 0..4095.[^adc]
- **C-002:** Detector state must fit within 2 KiB SRAM.[^target]
- **C-003:** No floating-point hardware is available.[^target]

## Requirements

- **R-001:** Accept one sample per millisecond.[^need]
- **R-002:** Compute the exact sum of squares of the newest 32 samples. Before 32 samples have arrived, older samples are zeros.[^need]
- **R-003:** Overflow must not occur for any legal input sequence.[^need]

## Problem Statement

Implement a small, deterministic signal-energy detector on the hypothetical MCU.[^need]

## Unknowns

- Hardware WCET is not yet determined.
- The downstream alarm threshold is outside this example.

[^adc]: Hypothetical ADC specification
[^target]: MCU budget assumption
[^need]: Toy stakeholder decision
