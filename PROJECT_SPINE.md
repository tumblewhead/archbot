# archbot project spine

## Status
Repository: `tumblewhead/archbot`, canonical nonvolatile project memory.
The locally developed Codex prototype and versioned architecture/evaluation evidence were imported in commit `aa2bbb5ec2e7`. The role-specific spine-filter correction was committed as `ca65eafda715`. Consult current repository artifacts and review receipts rather than treating older status notes as current.

## Theory
Progressive Concretization:
BKP -> AS = (C,R,PS), with independent Proofs (P/T), Proof Opportunities (PO), and Figure of Merit (F) -> competing APs -> provisional selection -> Contracts (CON) -> Design Elements (DE) -> Firmware -> final acceptance.

Every transition preserves obligations and supporting evidence. Proofs are conditional on stated assumptions. Requirements become binding immediately but demand stage-appropriate evidence: first_assessable_at, verification_due_at. Verification Obligations (VO) travel with artifacts. Architectural Debt (AD) records uncertainty and fallback plans associated with early commitment. An architecture may be provisionally selected for CON-first decomposition without completed firmware; final acceptance discharges all due VOs.

## Knowledge and agents
Google OKF v0.2 Markdown concepts with project-defined typed relationships. Spines select role-specific graph projections without deleting source artifacts. `agents/` defines roles; `process/` defines policies and gates; `tools/` contains deterministic structural checks, telemetry, and stage-gate validation. The LLM proposes; independent reviews and checkers gate accepted status.

## Authority
C-002 Option B was explicitly approved by the engineering authority: limit of 2,048 bytes **detector-attributable SRAM**, including owned state, scratch, charged stack/interrupt, and allocated shared memory under documented ownership rules. This does not approve an AP or discharge VO-002.
Approved authority record: `process/decisions/C-002-scope.yaml` (present in this repository).

## Historical experiment status through the imported working tree
- Proof Scout PO-001 proposed 32-sample / 12-bit squared-sum bound.
- PE-001-v2 corrected an invalid add-before-subtract overflow counterexample and addressed C integer promotion. PR-002 accepted the *abstract mathematics* with clarifications. Firmware remains unverified.
- AE-001 / AE-002: no downselection. EP-001 / EP-002: stage-appropriate planning and candidate memory envelopes.
- AE-003: no downselection; outstanding VO-001 source-adequacy review. C-002 approved scope and candidate-level envelopes now available, not target-verified.
- The spine-filter correction (`ca65eafda715`) makes default Proof Scout context concept-only, with explicit opt-in to auxiliary references. A subsequent VO-001 review receipt reports 27 unit tests passing, and an OKF structural check with 31 concepts, 114 links, and zero errors. These test results are reported by the local agent, not rerun here.
- VO-001 (C-001, synthetic ADC domain only) has an accepted review receipt `reviews/gates/VO-001-AS-ACCEPTANCE-001.json`; `process/ledgers/vo_ledger.yaml` marks it `discharged`. The acceptance does not verify physical ADC hardware or select an AP. The original AE-003 and candidate v2 assessments still record VO-001 as unresolved and are immutable history.

## Immediate next steps
1. Pull current `main`, run the full unit suite and `python tools/pc.py check --fast` locally.
2. Run `prompts/17-ae004-post-vo001.md` to create new v3 AP assessment artifacts carrying VO-001's scoped acceptance, then run the AP-stage checker. Preserve AE-003 and v2 assessments unchanged.
3. If AP-002 meets AP-due obligations, prepare an independently reviewable provisional-selection recommendation. Unknown F-001 target-cycle/flash comparisons require a separate explicit human tradeoff decision and accepted AD; do not auto-select.
4. Once a provisional AP is authorized, proceed to CON-first decomposition while carrying VO-002 through VO-006 and accepted AD forward.

## Source-of-truth rule
Chat summaries are navigation aids only. Once imported, the live versioned source, spines, authority decisions, and receipts supersede this bootstrap status. Update this file with concise status pointers after each substantive gate. Never duplicate large experimental evidence here.

## Reusable workflow initiative
The early numbered prompts are experimental task tickets, not the intended
steady-state interface. See `docs/REUSABLE_WORKFLOWS.md` for the planned
separation of role, reusable playbook, task manifest, and architecture spine.
The pilot runner and AP gate still contain AS-001/C-002-specific logic; this
initiative is documented but not yet an implemented generic dispatcher.

## Full-loop and retargeting qualification
See `docs/QUALIFICATION_CAMPAIGN.md` for Toy 1's remaining AP → CON → DE →
firmware → final acceptance gates and the planned Toy 2 root-solver retarget.
The first reusable dispatcher slice is `tools/task.py` + `process/tasks/TOY1-AE004.yaml`
using `process/playbooks/EVALUATE_AP.md`. This does not yet generalize
AS-001-specific telemetry or C-002-specific stage-gate validators. The user
runs and pushes local tests, Codex tasks and evidence receipts.

## Latest evaluated gate: AE-004 at ccb514117b11
The locally run post-VO-001 reevaluation created new AP-001/AP-002 v3
assessments and AE-004 without changing the v2 history. VO-001 is discharged
within the synthetic-domain authority. AP-002's AP-due technical obligations
are conditionally satisfied, but F-001 target-cycle/flash evidence is incomplete.
AE-004 records `NO_DOWNSELECTION`; the AP-002 tradeoff and AD-003 are
**proposed, not approved**. The review receipt reports a clean structural
check; a complete unit-test run was not recorded in the v2 receipt.

Next: run `process/tasks/TOY1-AE004-REVIEW.yaml` using the
reusable `REVIEW_AP_EVALUATION` playbook. An independent positive review
may bring the provisional AP-002 commitment to engineering authority; the
reviewing agent cannot select an architecture or accept debt.

## Latest independent review and protected decision gate
The imported independent receipt `reviews/AE-004-review-v3.json` reports
`ACCEPT_WITH_CLARIFICATIONS` for AE-004 and
`ELIGIBLE_FOR_AUTHORITY_DECISION` for AP-002 consideration. It does **not**
select AP-002, authorize AD-003, or discharge VO-002..VO-006. Its local
structural validation passed; a full unit-suite run was not part of that review.

The v1 proposed AD-003 deadline requiring F evidence *before CON approval*
would recreate our circular dependency. The still-unapproved
`process/decisions/AP-002-PROVISIONAL-AUTHORITY-REQUEST-v2.md` instead
proposes final comparative F evidence due before final acceptance, with
intermediate CON and implementation checkpoints. Explicit engineering-authority
approval is required before any selected-AP or accepted-AD state change.

## Controlled decision: AP-002 provisional CON-first selection
The engineering authority explicitly approved CON-first work after the
revised v2 AP-002 provisional selection and AD-003 request. Controlled
records: `process/decisions/AP-002-PROVISIONAL-SELECTION-001.yaml` and
`.md`. AD-003 is accepted in `process/ledgers/ad_ledger.yaml`, with
final F comparison due before final acceptance; no final F-001 ranking is
claimed. The architecture spine now references the accepted decision and
selected AP-002. VO-002 through VO-006 remain open.

**Next execution:** `process/tasks/TOY1-CON001.yaml`, operation
`DEFINE_CON` using reusable `process/playbooks/DEFINE_CON.md`.
First run structural validation and the AP-002 v4 policy gate; treat its
eligibility as a completeness check, not as independent correctness proof.
The Contract Agent produces drafts for independent review, not firmware.

**Proposed process refinement:** `docs/STAGED_FIGURE_OF_MERIT.md` and
`process/proposals/F_STAGES_001.yaml` separate symbolic `F_s` at
architecture stage from evidence-backed final `F_f`. This is a
reviewable proposal; F-001 was not amended by the authority decision.
A prior accepted VO-001 receipt hashes the old AS spine; newly added
navigation edges should be assessed for claim-level relevance without
silently changing that receipt's recorded hash or C-001 scope.

## Contract gate: TOY1-CON001
Commit `5013f9af7030` added draft CON-AP2-001/002/003, a contract spine,
seven DE responsibility placeholders and a VO/AD coverage matrix.
The authoring receipt states `CONTRACTS_UNRESOLVED`, not acceptance.
Next: run the generic `REVIEW_CON` playbook through task manifest
`process/tasks/TOY1-CON001-REVIEW.yaml`. Independent review must examine
whether unsettled queue/ISR/platform choices are deferrable engineering
implementation details or contract semantic blockers. Review also must
check that the proposed 72-byte persistent state cap accounts for all
specified state/control fields. No implementation work is authorized by
this review alone.
