# CLN-001 Stage-12: independent audit of NEW IF11 interface evidence

**Role:** new independent evidence reviewer. You are not the IF11
author, CLN-001 delegated decision maker, AP selector or implementer.
Synthetic, pre-freeze diagnostic. Review new executable feasibility
evidence, NOT the complete hardware interface as an accepted AP.

Read only AGENTS.md, TASK.md, inputs/SHA256SUMS and supplied inputs.
Do not access earlier solved Toy1 AP/CON/DE/C, Git history, other
workspaces, connected apps, network or hidden evaluator. Positive
source allowlist does not verify OS/connector isolation.

## Authority and scope

The accepted AS is activated AS-REV-002 plus separately accepted
AS-ADDENDUM-008-R1; D002, scoped F and T1/conditional T2 still apply.
Stage-10 independent audit returned
`READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`.
The delegated Stage-10 disposition authorized IF11 acquisition, not
selection or a physical service contract. All A/B/C remain UNSELECTED;
all fully realized H1–H6 and measured F coordinates remain UNKNOWN.

## Evidence audit required

1. **Integrity and independence:** verify pinned input manifest,
   raw four IF11 outputs against `IF11_SHA256SUMS`, declared commands,
   exact program version, and apparent source/authority boundaries.
   Hash equality proves matching bytes only. Record paths and actual
   runtime; do not authenticate historical separation by assertion.
2. **Replay before endorsement:** inspect full
   `inputs/IF11_TRACE_MODEL.py` source for I/O and effects before
   running. Reproduce `python3 -B` from a safe working directory
   and compare complete outputs/exit/14,327 cases/group counts to the
   receipt. Reproduce the documented in-memory wrap mutation only if
   safe and fully reconstructible, and record both expected/actual.
   If anything cannot be reproduced, label PARTIAL/UNREPRODUCED.
   Do not rewrite the original model/receipt.
3. **Decoder/refinement:** independently trace what consumer S and X
   actually know, not oracle labels. Check S ordered success/rejection
   rank and drain/marker with persistence assumptions; X exact framed
   rank/reset, retry, dedup and potentially growing source and
   consumer state. Challenge consumer restart, invalid attempts,
   equal old/new payloads, tag reuse and reset completion.
4. **Interface lifecycle and completeness:** audit the distinction
   between attempt, accept, commit, publish, receipt, retry, reset.
   Examine actual implementation of these semantics in IF11, not
   only prose. Identify any untested action order, implicit assumed
   provider/flow or state omitted from consumption.
5. **Information claims:** check the proposed `2^m` unpaid-result
   construction at equal numeric state and rank, including
   m=1..5 finite witnesses. Independently assess the conditional
   general bound: distinguish the hypothesis (no external history,
   replay, clock, timing, restricted acceptance or publication)
   from an unconditional theorem. No new theorem is accepted by
   this review. Check Q+1 capacity and finite ordinal arguments.
6. **A/B/C boundary:** A/B numeric models and C's hypothetical
   snapshot must not be upgraded to a supplied RN/C-HIST provider,
   complete resource bound or realized gate PASS. Audit
   observable failure for unavailable/wrong-event C snapshots.
7. **F, engineering follow-up and decision:** verify all 18
   realized H cells remain UNKNOWN, RAM includes owned/shared
   stack, pending debt, retry/index/reset and pinned buffers,
   external same-device energy isn't free. Identify the *smallest
   evidence-producing successor* or precise defect; recommend
   a narrowly scoped physical integration or C-kernel experiment,
   not another general review of unresolved UNKNOWN.
   Carry forward T002-2..8 and R4 deferred.

## Output ONLY

- `out/REVIEW-IF11-012.md`: review and replay audit, necessary
  assumptions, exact findings with severity and source references,
  obligation/F boundaries and next evidence-producing gate.
- `out/REVIEW-IF11-012.json`: structured receipt:
  `review_id: CLN-001-REVIEW-IF11-012`;
  `disposition` exactly one of
  `READY_FOR_DELEGATED_IF11_EVIDENCE_DISPOSITION`,
  `REVISE_IF11_EVIDENCE` or `UNRESOLVED`.
  Include source SHA-256 results, executable/replay result counts,
  mutation test status, contract/claim findings and open dependencies,
  honest unknowns and next gate. Keep
  `AP_selected:false`, `AS_changed:false`,
  `RI_RN_C_HIST_approved:false`,
  `all_full_H1_H6_PASS:false`, `target_verified:false`,
  `product_verified:false`, `formal_cleanroom_qualified:false`,
  `vo_discharged:[]`.

A favorable independent review permits a separate delegated *IF11
evidence* disposition only. Reviewer cannot approve S/X, select A/B/C,
activate new services, claim formal cleanroom or start binding CON/DE/C.
STOP after both outputs.
