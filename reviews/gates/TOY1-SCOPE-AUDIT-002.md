# TOY1-SCOPE-AUDIT-002: Source and obligation scope audit

**Disposition:** `SCOPE_REDUCTION_CANDIDATE` for the continuity protocol and the 1 ms timing interpretation; `AUTHORITY_CLARIFICATION_REQUIRED` before any baseline changes.

**Input revision:** `883b5aab496ec86b0a28fdd0d54a900c7fa1d65f`
**Task:** `process/tasks/TOY1-SCOPE-AUDIT-002.yaml`
**Trigger:** `process/change_requests/CR-001-SYNTHETIC-REQUIREMENT-AUTHORITY.md` (manifest trigger revision `a210f119fdec00f26bef9773ff2614d925e9ec54`)

## Findings and source traceability

| Claim | Classification | Evidence and reasoning |
|---|---|---|
| One accepted sample every 1 ms | `UNSUPPORTED_SCOPE_EXPANSION` as binding stakeholder authority; it is demonstrative provenance | `knowledge/bkp/problem-origin.md` labels the need “invented for the demonstration”; `knowledge/bkp/adc.md` calls the cadence synthetic. AS R-001 and VO-004 promoted this to a hard requirement without a separate approval found in the inspected authority records. The human objection requests rate independence, but is a change signal, not approval. |
| Exact newest-32 sum of squares, zero-padded startup | Existing AS R-002 scope, with 32 being the toy fixture parameter pending authority clarification | Recurrence is indexed by accepted sample order; no elapsed-time variable occurs in its definition. A fixed count window spans different elapsed durations at different rates. There is no approved alarm threshold or real-time-duration window in the inspected AS. |
| Integer recurrence, sum bound and wrap invariant | Accepted abstract mathematical result under its stated domain and ring assumptions | `PR-002` / `PE-001-v2` depend on unsigned 0..4095 values, a 32-slot ring, initialization, oldest-slot order and one update per input value. They do not depend on an interval between values. The accepted review explicitly limits itself to abstract mathematics and leaves C, concurrency, WCET and resource evidence open. Preserve it; assess only if the approved sample domain/window semantics change. |
| Detect every upstream missing acquisition with sequence counter and producer loss epoch | `OPTIONAL_ROBUSTNESS` absent a declared acquisition-loss model; otherwise an `ENVIRONMENT_PRECONDITION` only if an approved requirement says acquisition continuity is required | AS R-002 speaks of newest samples, but does not define a physical acquisition stream, a loss event, or a guarantee to detect losses. Synthetic ADC source explicitly assumes no sample-loss guarantee. Sequence/session/loss-epoch protocol in CON v1-v4 therefore has no demonstrated upstream authority. A source that supplies accepted samples in order suffices for the sample-index recurrence. If “newest” means physical ADC acquisitions despite dropped handoffs, that semantics needs an explicit approved source and producer integration contract. |
| 32-bit sequence wrap recovery via independent watchdog | `UNSUPPORTED_SCOPE_EXPANSION` under current AS; a mitigation for the added sequence protocol, not a derivation of R-002 | The watchdog and `B=(2^32-1)P` bound are introduced in CON v3/v4. No period-based continuity requirement or watchdog appears in AS, approved selection, or PR-002. Once sequence/loss tracking is removed, the counter-wrap problem disappears. Any independent watchdog is a new robustness/application requirement requiring authority. |
| Atomic externally visible publication and fail-closed invalidation | `UNKNOWN` / interface-dependent | A complete accumulator update must be internally coherent. AS does not specify concurrent readers, an external validity flag, or invalidation on an upstream loss. Atomic publication may be necessary if the approved integration interface has concurrent readers, but its form and memory allocation are not implied by the mathematical requirement alone. Define this only from a reviewed interface contract. |
| 1 ms WCET/timing plan (VO-004) | Derived solely from disputed R-001 and requires controlled VO revision if R-001 is changed | `verification_plan.md` ties VO-004 to R-001; it is open in the ledger. Do not delete/discharge it. Re-scope its evidence after an authorized AS decision, retaining target throughput evidence if separately approved. |
| Detector-attributable 2 KiB SRAM accounting (C-002) | `REQUIRED_BY_AS` and separately approved | `process/decisions/C-002-scope.yaml` records explicit engineering-authority approval, boundary and attribution rules. Keep unchanged regardless of the synthetic 1 ms defect. The 128-byte shared cap is a v4 allocation within that scope, not an independently authorized relaxation. |
| AP-002 selection and AD-003 | Approved historical authority, impact review needed | The approved selection explicitly protects R-001 and conditions CON on its constraints. A changed AS requires impact review of that decision and accepted AD-003; neither can be silently amended by this audit. |

## Minimum candidate semantics

See [AS-001 corrected-scope candidate](TOY1-SCOPE-AUDIT-002-AS-CANDIDATE.md). In short, define one update per legal sample accepted by the detector interface; define the rolling window by the last 32 accepted samples in order, with zero padding before 32 have been accepted; make numerical behavior independent of time between invocations. Treat achievable throughput, overload behavior, source-loss reporting, reader concurrency and timing deadlines as separate integration requirements only if an authority supplies them.

This preserves the mathematical recurrence and bounds while avoiding a promise of infinite implementation throughput. It does not assert that the application should ignore dropped physical acquisitions; that distinction is unresolved until the engineering authority defines the input boundary/semantics.

## Impact graph and smallest affected set

1. **AS R-001 and its provenance:** authority must decide whether to replace fixed cadence with sample-invocation semantics. R-002's 32-sample count, zero padding, C-001 domain, R-003 arithmetic, and C-003 remain unchanged unless authority separately directs otherwise.
2. **VP / VO-004:** revise evidence scope and due method against the approved R-001. Keep the obligation open through controlled versioning; target throughput/timing evidence remains necessary for any approved throughput requirement.
3. **CON v1-v4 and reviews:** preserve unchanged as historical evidence. Once an AS candidate is approved, contract owner should version a minimal correction. Remove sequence, session, loss-epoch and counter-wrap/watchdog obligations unless separately authorized. Retain precise sample ordering/range and internal update semantics. Specify coherent output only to the extent required by an approved consumer interface.
4. **Shared allocation plan / VO-002:** re-plan from the approved contract. The current EP-003 128-byte inventory includes mechanisms whose necessity is disputed; it cannot establish the reduced design's numeric fit. C-002's 2 KiB attribution remains binding, and VO-002 remains open pending actual stage evidence.
5. **DE placeholders:** ingress/shared/IRQ responsibilities are linked to v3/v4 contracts. Re-map or retire those responsibilities only after authority and contract review; no DE refinement is approved here.
6. **AP-002 / AE history / AD-003:** selection and debt remain accepted history. Assess whether their conditions and deadline still fit revised R-001; do not rewrite past assessments or the approved decision. AP-002's provisional selection is not automatically revoked.
7. **PR-002:** retain accepted abstract proof for the same legal value range, 32-slot rolling recurrence, and update ordering. Its sample-index mathematics is timing-independent. Re-review only any changed mathematical/interface assumptions; implementation, concurrency and target evidence stay open.
8. **VO-001, C-002, F-001, R-003 and other accepted/history artifacts:** preserve their exact scope and receipts; no scope audit finding discharges obligations or changes F.

## Unresolved questions and next eligible action

- Engineering authority must approve or reject the changed R-001 semantics and decide whether samples mean accepted interface inputs or every physical acquisition.
- If loss detection, atomic external publication or watchdog behavior is required, authority must identify its source and scope. A producer guarantee must be enforceable and independently verifiable; it cannot be presumed from absent evidence.
- After that decision, create versioned AS/VP/VO and contract candidates through their controlled workflows, then obtain independent review. Do not resume v4 shared-allocation repair against disputed semantics.

Structural validation passed (`python tools/pc.py check --fast`: 57 concepts, 248 typed links, zero warnings/errors; raw hashes skipped). This is a structural result only, not mathematical acceptance, engineering approval, contract acceptance, or evidence of fit. No tests were requested or run. No accepted authority, AS/F, proof, contract, VO/AD ledger or firmware was modified.
