# Independent compiler evidence review: TOY1 VC-001

**Disposition: ACCEPT_WITH_CLARIFICATIONS**, limited to the submitted host
source/compiler evidence and its stated scope. This is an independent evidence
judgment, not product verification or VO acceptance.

## Inputs and integrity

- Task: `REVIEW_COMPILER_EVIDENCE-TOY1-VC001`; project/spine: `AS-001`,
  `/architecture/AS-001/spine.md`.
- Reviewed submission:
  `reviews/verification/TOY1-VO003006-20261015T031625Z.json`.
  Its SHA-256 is
  `5a98d1d3f4c06a78134e17c123abc7883468ff74cedb5bfccd83248016540b9b`;
  its Git blob SHA-1 matches the task pin
  `899f08ef9793373dc36a98406079e0a4c774d546`.
- Pinned source revision: `6e3a6c330d663081b7e8fad33f17fe731b563569`;
  it is an ancestor of review HEAD
  `3a831bb115aba6d162d75ae46beb0b1f52e4ea8b`. All five submitted source
  SHA-256 pins (header, implementation, probe, assertion test, and evidence
  tool) match the checkout. The prior implementation review is present and its
  detector source pins match.
- Reviewer: independent verification agent, current invocation. The evidence
  authoring run and this review run are separate.

## Findings

1. **Source and host arithmetic correspondence: supported for the examined
   host C99 environment.** `uint32_t` casts occur before both square
   multiplications. With legal samples, each square is at most 16,769,025;
   the add-before-subtract transient is bounded by 553,377,825 from a valid
   ring state, below `UINT32_MAX`. The final rolling sum is at most
   536,608,800. The host's reported `CHAR_BIT=8`, `UINT16_MAX=65535`, and
   `UINT32_MAX=4294967295` are consistent with the required exact-width types.
   Initialization, single indexed replacement, index wrap, and reset logic
   match the reviewed source contract, conditional on legal ingress and
   quiescent reset.
2. **Producer-reported execution integrity: verified for available files.**
   The submitted raw stdout/stderr files exist and match every declared
   SHA-256 and byte count. The three positive executions report 8192 checks;
   the deliberately bad reference reports `MISMATCH case=0 sample=4095`,
   consistent with its nonzero exit being a detected mismatch rather than a
   missing executable or signal.
3. **Independent reproduction: passed.** On review HEAD, GCC
   `16.2.1 20260810` compiled the pinned detector and correspondence probe
   with the recorded strict C99 warnings and `-O2`; the executable reported
   `HOST_PROBE_OK checks=8192`. Command:
   `cc -std=c99 -Wall -Wextra -Wconversion -Werror -pedantic -O2 implementation/toy1/detector.c implementation/toy1/correspondence_probe.c -o /tmp/toy1-vc001-review && /tmp/toy1-vc001-review`.
4. **Registered task runner limitation.** `python tools/task.py inspect` and
   the prescribed unit tests passed. `python tools/task.py run` returned
   failure before any reviewer turn (zero completed turns, no gate decision,
   no output artifacts). This report is the direct independent review from
   this invocation; the runner failure is not evidence against the submitted
   host result.
5. **Scope boundary.** Target compilation was `NOT_REQUESTED`. No target ABI,
   linked image, instruction audit, target execution, whole-application
   floating-point dependency analysis, or integration evidence was reviewed.
   Host results do not establish target correspondence, external publisher
   continuity, reset-quiescence enforcement, charged SRAM/stack/nesting, or
   product qualification.

## Engineering briefing and unresolved obligations

The source-level implementation and the submitted independent shifting-queue
probe are consistent for legal unsigned 12-bit inputs on the reproduced host
compiler configuration. The negative control detects the injected reference
error. Preserve the external publisher boundary, legal-input precondition, and
quiescent-reset precondition; no timing/watchdog or out-of-domain behavior is
added by this review.

VO-002, VO-003, VO-004, VO-005, and VO-006 remain **OPEN**. In particular,
target compiler/build and integration evidence remains outstanding for VO-003
and VO-006; target/integration charged-SRAM, attribution, stack and nesting
evidence remains outstanding for VO-002; and end-to-end publisher and
integration correspondence remains outstanding for VO-004/VO-005. No VO is
discharged, no AD is accepted, and `product_verified` is false.

**Next eligible action:** route a separate authorized target/integration
evidence task from the active project policy and its reviewed receipt. This
review receipt does not automatically route broader verification execution.
