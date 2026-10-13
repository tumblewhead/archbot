---
type: Experiment Summary
id: RESULT-001
title: Synthetic fixture summary
status: draft
tags: [results, synthetic]
sources:
  - id: fixture
    resource: /architecture/AS-001/evidence/raw/samples.csv
    title: Synthetic toy ADC fixture
relations:
  - kind: derived_from
    target: /architecture/AS-001/evidence/raw/samples.csv
---
# Result summary

The raw CSV contains a deterministic synthetic sample stream within the assumed ADC range.[^fixture]

The data can test an implementation but **cannot establish** the worst-case bound for *every* 12-bit input. No actual silicon or timing measurement has occurred.

[^fixture]: Synthetic toy ADC fixture
