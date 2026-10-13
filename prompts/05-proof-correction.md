# PE-001-v2: Corrective Proof Engineering

Read AGENTS.md and the Proof Engineer role definition.

Start from the AS-001 architecture spine.

Read:
- PO-001
- PE-001-v1
- PR-001
- Relevant AS and BKP assumptions

Create PE-001-v2. Do not overwrite PE-001-v1.

Requirements:

1. Preserve the valid mathematical accumulator bound.
2. Preserve the rolling-window induction and startup/wraparound analysis.
3. Remove the invalid 32-bit add-before-subtract overflow counterexample.
4. Establish the correct upper bound for the add-before-subtract intermediate.
5. Correct the C integer-promotion discussion.
6. State the requirement to widen operands before multiplication, unless the target's arithmetic rules establish an equivalent guarantee.
7. Separate mathematical theorems from implementation-specific obligations.
8. Address every material finding from PR-001.
9. Do not select an architectural proposal or approve firmware.

Update the spine with an `addresses` relationship to PE-001-v2.

Run structural checks and record a review receipt.

Report the remaining obligations and the precise claims ready for independent acceptance.