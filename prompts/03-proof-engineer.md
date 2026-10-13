Read `AGENTS.md`, the proof-engineer role definition, and the current architecture spine.

Perform an independent mathematical review of `PO-001`.

Verify the candidate accumulator bound and rolling-window invariant from first principles. Do not assume the Proof Scout's reasoning is correct.

Explicitly examine startup, ring-buffer wraparound, subtraction order, integer widths, and C integer-promotion behavior.

Produce a versioned proof artifact with assumptions, theorem statements, proof or counterexample, and unresolved implementation obligations.

Update the architecture spine only with relationships justified by the verification result. Do not select an architectural proposal or change the AS or F.

Run the structural checks and record a review receipt.