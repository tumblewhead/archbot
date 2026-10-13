# Independent Proof Review: PE-001-v1

Read `AGENTS.md`, the architecture spine, AS-001, PO-001, and PE-001-v1.

Act as an independent mathematical proof reviewer.

Your objective is to find errors, missing assumptions, invalid counterexamples, and unsupported conclusions.

Do not assume the Proof Engineer is correct.

In particular:

1. Independently derive the universal accumulator bound.
2. Independently establish or refute the rolling-window invariant.
3. Examine startup, ring-buffer wraparound, and intermediate arithmetic.
4. Verify every overflow claim, including claims concerning add-before-subtract.
5. Examine the treatment of C integer promotions and unsigned arithmetic.
6. Separate mathematical results from implementation-specific obligations.

Produce a review with one disposition:

- ACCEPT
- ACCEPT_WITH_CLARIFICATIONS
- REVISE
- REJECT

Cite precise claims and provide counterexamples where applicable.

Do not modify the existing proof. Create a review artifact and link it through the architecture spine.

Run structural checks and record the review receipt.

Do not approve an architectural proposal or firmware implementation.