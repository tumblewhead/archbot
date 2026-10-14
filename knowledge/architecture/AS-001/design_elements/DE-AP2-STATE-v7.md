---
type: Design Element
id: DE-AP2-STATE-v7
title: Rolling-window state and reset lifecycle
status: draft
version: 7
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-002-v6.md
  - kind: supported_by
    target: /architecture/AS-001/proofs/PR-002.md
---
# DE-AP2-STATE-v7

**Purpose and boundary.** Own the abstract window of the latest 32 accepted
samples, the index identifying the oldest slot, and the exact square-sum
accumulator. The boundary isolates history and reset invariants from ingress
and arithmetic sequencing.

**State and invariant.** The conceptual state is 32 legal sample values,
an oldest-slot index in `[0,31]`, and an accumulator in
`[0,536608800]`. An implementation representation must preserve the
correspondence between slots and the latest 32 accepted samples in order;
before 32 samples, absent older history is zero. The accumulator equals
the sum of squares of those conceptual values. This is a language-independent
model, not a mandate for a physical ring layout or specific C types.

**Lifecycle.** Initialization establishes all-zero history, index and
accumulator before the first acceptance. Reset is permitted only with
acceptance quiesced and no operation in progress; quiescence continues
through reset completion. Completion establishes the same all-zero state,
and subsequent acceptance begins a fresh sequence. The mechanism enforcing
quiescence is an implementation/integration obligation; no ISR, lock,
atomic, scheduler, or other topology is selected.

**Interface and composition.** `oldest()` supplies the value to be evicted
for the next accepted sample. `commit(sample, squared_value)` replaces that
oldest conceptual slot, advances the oldest index modulo 32, and updates
the accumulator exactly once. Its caller must establish a legal sample and
the exact square; concrete expression correctness remains VO-006. The
element does not independently publish results. `DE-AP2-UPDATE-v7` sequences
the transition and `DE-AP2-RESULT-v7` hands back the resulting accumulator.

**Verification hooks.** Check initialization and reset boundaries, index
wrap, slot order, one replacement/advance per accepted sample, and the
accumulator invariant against a simple newest-32 reference model. These
checks support VO-005 and VO-006 but do not establish concrete C or target
correctness.
