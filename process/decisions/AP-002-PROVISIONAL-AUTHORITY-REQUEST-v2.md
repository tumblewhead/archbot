# AP-002 provisional selection: engineering authority request v2

**Record:** `AP-002-PROVISIONAL-AUTHORITY-REQUEST-v2`  
**State:** `PENDING_AUTHORITY` (not approved, not a selection)  
**Architecture:** AS-001, sliding-window detector

## Evidence and decision context

- `knowledge/architecture/AS-001/evaluations/AE-004.md`: `NO_DOWNSELECTION`
  under the currently incomplete F-001 comparison.
- `reviews/AE-004-review-v3.json`: independent evaluation
  `ACCEPT_WITH_CLARIFICATIONS` and recommendation
  `ELIGIBLE_FOR_AUTHORITY_DECISION`.
- `knowledge/architecture/AS-001/evaluations/AP-002-assessment-v3.yaml`:
  all AP-stage technical obligations are supported conditionally; the existing
  comparison mode is `incomplete`.
- `process/decisions/C-002-scope.yaml`: approved Option B; the total
  detector-attributable SRAM ceiling remains 2048 bytes.
- `process/ledgers/vo_ledger.yaml`: VO-001 discharged for the *synthetic*
  C-001 domain; VO-002 through VO-006 remain open.
- `knowledge/architecture/AS-001/merit.md`: F-001 unchanged; state SRAM,
  worst-case cycles per update and flash bytes are its ranking dimensions.

The proposed 1928-byte charged-SRAM envelope (904 bytes of category caps
plus 1024 bytes reserve, leaving 120 bytes additional headroom) is a
**budget**, not a measured physical bound. AP-002's accepted recurrence and
overflow arguments cover **abstract mathematics**, not C or target behavior.

AP-001 remains AP-ineligible pending R-002 and R-003 arguments. Neither
candidate has an established Pareto ranking. AP-002 is a candidate for a
**reversible commitment to CON-first decomposition**, not a declared winner
under the final F-001.

## Exact decision requested

Does the engineering authority authorize:

1. **Provisionally select AP-002 for CON-first decomposition** without
   declaring it final or Pareto-optimal.
2. **Accept AD-003**, the risk that AP-002 is later inferior or infeasible
   when real cycle, flash, or total SRAM evidence arrives.
3. Preserve **all applicable C/R obligations and VO-002..VO-006** without
   relaxing the 2048-byte ceiling, 1 ms cadence, exact sum, arithmetic safety,
   or integer-only constraints.
4. Keep final F-001 verification and comparison due **before final acceptance**,
   and require a comparison/risk review when comparable evidence becomes
   available. Do **not** require completed firmware before CON approval.
5. Require CON to allocate enforceable memory/timing responsibilities and
   define a practical measurement/verification plan. Require later DE,
   implementation, and target verification gates to discharge their due VOs.
6. If evidence reveals hard infeasibility, an unjustified architecture
   tradeoff, or a failed due-stage VO, **suspend affected downstream
   commitments and reopen AP selection**.

### Proposed Architectural Debt: AD-003

- **Trigger:** Provisional AP-002 commitment before a supported F-001
  three-dimensional ranking.
- **Owner:** Evaluation Agent for evidence tracking and comparative review;
  engineering authority for acceptance/rejection of protected tradeoffs.
- **Risk:** AP-002 might use more flash or cycles, or prove unsuitable for
  the target, despite its favorable abstract update workload.
- **Due stage:** `TARGET_VALIDATION` and **strictly before final architecture/
  firmware acceptance** for final comparative evidence and AD disposition.
- **Intermediate checkpoints:** At CON, verify allocated budgets, obligation
  ownership, and evidence plan. At IMPLEMENTATION, review actual memory,
  compiler/toolchain behavior, C correctness, and available cycle/flash data.
  Do not demand final measured F comparison at CON.
- **Fallback:** If the selected architecture fails any binding requirement,
  cannot satisfy an allocated CON budget, or fails agreed risk criteria,
  reopen AP selection, revise affected CON/DE as necessary, and preserve
  evidence from the failed branch.
- **No auto-approval:** Creating this document does not add accepted debt to
  `process/ledgers/ad_ledger.yaml`, update AP-002 assessments, authorize
  CON, or mark AP-002 selected.

This version **supersedes the proposed deadline wording** in
`process/decisions/AE-004-AP-TRADEOFF-PROPOSAL.md` *only as a recommendation*.
The older proposal remains historical evidence. This proposal corrects the
earlier "before CON approval" deadline, which would reintroduce the
implementation-before-selection circular dependency.

## Response and recording

Authority may explicitly `APPROVE`, `REJECT`, or `REQUEST_REVISIONS`.
If approved, record a **separate** source-referenced, versioned accepted
decision naming AP-002 and AD-003. An independent policy/gate review must
check the resulting acceptance and its carried VOs. Do not rewrite AE-004,
PR-002, or the original AS/F/VO records.
