# archbot project spine

## Status
Repository: `tumblewhead/archbot`, canonical nonvolatile project memory.
The locally developed Codex prototype and versioned architecture/evaluation evidence were imported in commit `aa2bbb5ec2e7`. The role-specific spine-filter correction was committed as `ca65eafda715`. Consult current repository artifacts and review receipts rather than treating older status notes as current.

## Latest independent AS-v2 review: favorable, controlled authority pending
Commit `a41052d6af2b` added
`reviews/gates/TOY1-AS002-independent-review-v3.json`.
It reports `ACCEPT_WITH_CLARIFICATIONS` and
`AS_CANDIDATE_ACCEPTABLE_WITH_EXPLICIT_CONDITIONS`.
The versioned AS-v2 is correct under approved sample-indexed newest-32
publisher input semantics, and VP-v3 / proposed VO-004-v2 both put
detector-side R-001 evidence due at IMPLEMENTATION. The independent
review does **not** activate the new AS, modify the VO ledger, reaffirm
AP-002 selection or discharge any VO.

The old approved AP-002 selection protects the superseded 1-ms
cadence. Engineering-authority disposition of its applicability to AS-v2
is now required before a new CON baseline. The precise, **unapproved**
request is
`process/decisions/AP-002-AS-V2-APPLICABILITY-REQUEST-v1.md`.
Option A would provisionally reaffirm AP-002 only for CON-first under
the corrected sample-indexed AS, retain AD-003 and C-002/F-001,
and authorize controlled open VO-004 rescoping. Old selection,
AS/VP/VO ledgers, proof and CON history remain unchanged.

**Next:** obtain explicit engineering-authority decision for Option A,
B (reopen AP selection) or revisions. On approval, create a versioned
superseding decision, align the active AS/VP/VO-004 index and open ledger
through controlled review, then generate only minimal new CON drafts.
Never resurrect obsolete loss epochs, sequence watchdogs or invented
1-ms obligations. No DE/firmware work is authorized yet.

## Current gate: AS-v2 and VP-v3 package submitted for review
Commit `b1206705e12e` added a corrected versioned
`knowledge/architecture/AS-001/verification_plan-v3.md` and
`reviews/gates/TOY1-AS002-revision1-authoring-receipt.json`.
The authoring agent addressed independent finding ASR-001 by aligning
detector-side once-per-accepted-sample R-001 verification with the
`IMPLEMENTATION` due stage in VO-004-v2. Any rate, overload or
deadline requirement remains a separately authorized integration
obligation. The AS-001-v2 draft, original AS, accepted C-002 scope,
PR-002, F-001, AP-002 historical approval, AD-003 and open VO ledger
were preserved.

**Next:** independently review the submitted package with the
unchanged generic `REVIEW_AS` playbook. Invoke `tools/next_task.py`
with `reviews/gates/TOY1-AS002-revision1-authoring-receipt.json`;
the receipt declares `review_subject:
knowledge/architecture/AS-001/statement-v2.md` because AS wording
is unchanged. This creates a new review task based on the new receipt,
not a duplicate of the previous AS-v2 review.

No independent acceptance of the revised package has occurred yet.
If accepted, resolve the original AP-002 selection's protected 1-ms
condition through explicit engineering-authority disposition, then
version/update VO authority before returning to a *minimal* CON.
Do not reuse obsolete CON v4 loss-epoch/watchdog obligations.

## Workflow correction: versioned re-review identity
The generic task planner now identifies an already-planned transition by
**source submission receipt**, not solely by target concept path. This
permits a subsequent independent AS review when a new versioned VP/VO
proposal leaves the original draft AS unchanged. Re-running the same
submission remains idempotent. The new tests for the route, receipt
naming and repeated-subject identity require local execution.

## Independent AS-002 review: REVISE (2026-10-13)
Commit `59e582c6564f` records
`reviews/gates/TOY1-AS002-independent-review-e239ff6.json`, disposition
`REVISE` with `gate_status: AS_REVISION_REQUIRED`, independently reviewed.
The AS-001 v2 candidate correctly carries the approved newest-32
sample-indexed publisher boundary, unsigned 12-bit toy input domain,
2 KiB detector-attributable SRAM, no-FPU, and applicable abstract PR-002.

The actionable blocker `ASR-001` is **only** the mismatch between
`verification_plan-v2.md` R-001 conditional `INTEGRATION_VALIDATION`
and `VO-004-v2.md` detector-side `IMPLEMENTATION` due stage.
The latter must be explicit in the next versioned VP proposal; any future
throughput/overload/deadline requirement is a **separate** integration
obligation, not R-001. `ASR-002` is a downstream AP-002 authority condition
that cannot be silently revised; handle after favorable AS review.
`ASR-003` remains an external, unverified publisher promise, not an
algorithmic loss detector.

**Next:** use `tools/next_task.py inspect/emit --receipt
reviews/gates/TOY1-AS002-independent-review-e239ff6.json` to generate
the generic `REVISE_AS` task. The controller now matches the reviewer's
`gate_status` rather than an absent `next_stage_recommendation`.
The reusable `REVISE_AS` playbook permits a **versioned VP/VO-only
correction**, preserving the correct AS v2 draft. A new authoring receipt
should declare `review_subject:
knowledge/architecture/AS-001/statement-v2.md` and put the newly
versioned dependent evidence in `changed_artifacts`; generic
`REVIEW_AS` can then independently re-review that package.

The current AS has NOT been accepted or activated; original
AP-002 protected timing condition and historical VO-004/AD-003 remain,
pending controlled independent review and necessary human authority.
C-002 is still approved and VO-002..VO-006 remain open.
Tests for the updated generic router must run on the developer workstation.

## Latest submitted AS correction and independent review (2026-10-13)
Commit `29d1b8864796` contains a *draft* revised AS,
`knowledge/architecture/AS-001/statement-v2.md`, new synthetic-BKP
provenance annotation, versioned VP and VO-004 candidates, and
`reviews/gates/TOY1-AS002-authoring-receipt.json`. Authoring
disposition is `AS_REVISION_READY_FOR_INDEPENDENT_REVIEW`, not
accepted. Original AS, C-002 authority, AP-002 approval and AD-003,
PR-002, VO ledger and CON v1-v4 history remain unchanged.

The submission matches the approved newest-32 publisher boundary and
removes invented 1 ms algorithmic rate, loss epochs and watchdogs.
Independent review must check especially that the new VO-004 due stage
(`IMPLEMENTATION`) agrees with the VP's conditional
`INTEGRATION_VALIDATION` wording, and whether prior AP-002's
protected 1 ms selection premise needs a superseding human decision.

**Next:** from `reviews/gates/TOY1-AS002-authoring-receipt.json`,
use generic `tools/next_task.py inspect` then `emit`; it routes
to registered `REVIEW_AS` using
`process/playbooks/REVIEW_AS.md`. Only a submitted, receipt-backed
draft AS can enter that review; an independently confirmed blocking
AS review can route back to `REVISE_AS` without a bespoke prompt.
No new CON/DE/firmware work before accepted AS and authority/VO
disposition. These new routes need developer-workstation unit tests.

## Engineering authority: sample-indexed detector scope approved (2026-10-13)

The human explicitly approved the corrected input boundary with:
"yes, newest 32 samples, it is the responsibility of the upstream sample
publisher to give uninterrupted samples".

Controlled records:
- `process/decisions/AS-001-SCOPE-CORRECTION-001.md`
- `process/decisions/AS-001-SCOPE-CORRECTION-001.yaml`
- Source request `process/decisions/AS-001-SCOPE-CORRECTION-REQUEST-v1.md`.
- Independent audit `reviews/gates/TOY1-SCOPE-AUDIT-002-receipt.json`.

The authority permits a versioned AS correction: compute over the newest
32 delivered/published legal samples, ordered by acceptance; update once
per received sample irrespective of elapsed interval. Uninterrupted ordered
sample publication is the **upstream publisher's external responsibility**,
not a requirement for detector-side reconstruction, sequence counters or
watchdogs. This does not claim verified physical loss-free transport, nor
an infinite sampling throughput guarantee.

The original AS/VP, VO-004, AP-002 selection and AD-003 remain historical
records. The fixed 1 ms algorithmic requirement is **superseded in scope
by authority**, but no revised AS or VO disposition is independently
accepted yet. C-002's 2 KiB attribution, 12-bit synthetic domain, no FPU,
exact 32-sample recurrence and F-001 are retained.

**Next execution:** `process/tasks/TOY1-AS002.yaml` invokes reusable
`REVISE_AS` using the guarded `AS_SCOPE_CORRECTION_APPROVED` trigger.
It must produce versioned *draft* AS/BKP-provenance/VP/VO-004 corrections,
AP/AD impact and independent review request. It cannot silently discharge
a VO or approve contracts. Do not continue legacy CON v4 repair until
corrected AS is reviewed and accepted.

## Scope audit accepted as findings; authority decision pending

Commit `a03293dcb130` adds
`reviews/gates/TOY1-SCOPE-AUDIT-002.md`,
its receipt and candidate AS wording. Audit disposition is
`SCOPE_REDUCTION_CANDIDATE_WITH_AUTHORITY_CLARIFICATION_REQUIRED`,
**not engineering approval**. The independent audit concludes the
1-ms requirement came from synthetic demonstration provenance, while
the 32-sample recurrence is mathematically sample-indexed. It finds
the loss-epoch, sequence-wrap watchdog and external-reader protocol
unsupported as *binding* requirements absent separately approved
integration semantics. C-002 remains approved, VO-002..VO-006 open,
and the provisional AP-002 selection/AD-003 unchanged.

Proposed protected decision request:
`process/decisions/AS-001-SCOPE-CORRECTION-REQUEST-v1.md`.
It asks human engineering authority to approve sample-indexed accepted-input
R-001 with timing and overload left for separately approved integration,
and to preserve 32-sample exact arithmetic and authorized resource scope.
Do not mutate AS, VO-004, selected AP, F, contract history or protected
decisions until explicit approval and controlled versioned revision.
No further CON v4 repair is scheduled while source authority is disputed.

## Active specification-origin correction (human objection, 2026-10-13)
The human engineering authority disputes the source and necessity of the
one-sample-per-millisecond assumption and the security-grade continuity
protocol. The repository's `knowledge/bkp/problem-origin.md` expressly
calls its 1 ms source **"invented for the demonstration"**, yet
`AS-001/R-001` treated it as binding. This is an upstream authority
and provenance defect, not just an unfinished CON resource plan.

Open correction record: `process/change_requests/CR-001-SYNTHETIC-REQUIREMENT-AUTHORITY.md`.
Use `process/tasks/TOY1-SCOPE-AUDIT-002.yaml`, the revised task
that covers *both* sample-rate independence and the invented continuity
constraints; it supersedes `TOY1-SCOPE-AUDIT-001.yaml` for the next run
without deleting that historical task.

Until the source audit and an authorized revised AS baseline are complete:
do not launch another repeated CON v4 repair from the old chain.
Do not silently change R-001, VO-004, selected AP-002, accepted AD-003,
F-001 or prior proof/contract receipts. Verify the impact graph and
preserve mathematical claims unaffected by input timing. C-002 Option B
is independently approved accounting scope and remains binding.

## Current qualification intervention: Scope audit
The latest local evidence run was pushed as `cf0ec21f0548`.
`EP-003-CON004-SHARED-ALLOCATION` and
`reviews/gates/PLAN_EVIDENCE-668abfbc4056-receipt.json`
report `EVIDENCE_STILL_UNRESOLVED`. They identify a missing
bounded 128-byte shared-memory allocation; no CON acceptance or DE
authorization has occurred.

Repeated CON review has generated additional requirements for loss
epochs, atomic publication and watchdog behavior. The original
AS-001 explicitly requires 1-ms input acceptance and exact 32-sample
squared sums but does **not explicitly require comprehensive upstream
loss detection**. Whether the added fault guarantees are necessary
derived obligations, integration assumptions or discretionary robustness
is a scope question requiring independent audit.

Next task: `process/tasks/TOY1-SCOPE-AUDIT-001.yaml`.
Its role/playbook are reusable `AUDIT_SCOPE`, registered under
`process/operations.yaml`. The audit compares AS/proof/contract
provenance and reports recommendations without editing accepted
authority, contracts or VO/AD state. It is a deliberate escalation,
**not** a rule routing every unresolved evidence plan to scope
reduction. If a proposed simplification changes the accepted AS,
request engineering-authority approval separately.

## General iteration decision (2026-10-13)
Human engineering direction: iteration must be available at **any stage**
producing reviewable or verifiable claims, not only CON. A stage-independent
model is documented in `docs/PROGRESSIVE_ITERATION.md`.

The receipt planner now resolves `changed_concept` targets using type
information from transition policy, retaining compatibility with prior CON
rules. Generated tasks now reference their predecessor manifest instead of
recursively copying historical task context. A synthetic proof-package test
checks cross-artifact routing. Stage-specific operations for proof, DE and
implementation are *not* automatically deployed; only the existing CON
transitions are registered for local use. Tests need local confirmation.

Latest pushed human-run commit `4122bc18d638` added only the
generated `process/tasks/REVISE_CON-d811f94c033e.yaml` manifest.
**The associated CON correction has not been pushed yet.** The next run is
`python tools/task.py run --manifest
process/tasks/REVISE_CON-d811f94c033e.yaml` after a fast-forward pull
and full local validation. Its source remains the independent CON-003
review `REVISE`; DE and firmware stages remain blocked.

## Live state: CON-004 evidence gap
Commit `4a426ac06de5` adds active draft contracts v4 and
`reviews/gates/TOY1-CON004-receipt-v4.json`. Their authoring status
is `CONTRACTS_UNRESOLVED`: contract semantics for loss and watchdog
are more specific, but a bounded numeric inventory for the 128-byte
detector-attributable shared allocation remains missing.

Use the general receipt planner, not another handwritten CON prompt:
`python tools/next_task.py inspect --receipt
reviews/gates/TOY1-CON004-receipt-v4.json`. On the current policy,
this routes to stage-independent `PLAN_EVIDENCE`, rather than
`REVIEW_CON`. The evidence planner must seek a credible shared
allocation/ownership envelope under the existing cap, or report the
minimal blocker without inventing hardware facts. No CON acceptance,
DE refinement, C implementation or VO discharge is authorized.
The tests for this new transition still require the user's local run.

## Current gate and next action (2026-10-13)
Latest reviewed CON version: v3. Independent CON-003 review at
`reviews/gates/TOY1-CON003-independent-review-v3.json` records
`REVISE` / `CON_REVISION_REQUIRED`, with publication linearization,
watchdog start/response semantics, and bounded shared-memory allocation
still unresolved. The previously resolved 71-byte persistent-state
contract claim remains closed; physical layout remains VO-002.

The next cycle must be created from the review receipt, **not from a
handwritten new prompt**. Use `python tools/next_task.py inspect --receipt
reviews/gates/TOY1-CON003-independent-review-v3.json`, then `emit`
and execute the reported task manifest. Source is
`process/loop_transitions.yaml`; reusable methodology is documented in
`docs/CONTRACT_LOOP.md`. Tests are authored but not yet executed on
the developer workstation.

The current process scope is iterative contract closure. Whole-contract
analysis and optimization follow an independently reviewed baseline.
No independent CON acceptance, DE refinement, C implementation or final
target verification has occurred. VO-002..VO-006 remain open; AD-003 remains
accepted; the original AS/F and provisional AP-002 authority remain binding.

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

## Independent contract review: CON001
Commit `e60893c25253` added independent CON-001 review `REVISE`, with
`CON_REVISION_REQUIRED`. Two blocking issues:
`CON001-F01` discontinuity cannot be detected without sequence/overrun
information or an independently enforceable producer guarantee;
`CON001-F02` the 72-byte state cap does not yet account for every named
control, fault and publication field. CON-AP2-003's overall accounting
was accepted subject to correcting these issues. Target queue/IRQ/scheduler
implementation choices may remain deferred if the interfaces are precise.

**Next:** `process/tasks/TOY1-CON002.yaml` invokes generic `REVISE_CON`
from the independent-review receipt. It must produce versioned corrected
contracts, preserve v1 and keep VO-002..VO-006 open. A new independent review
is required before DE refinement. No firmware is authorized by this gate.

## Deferred design proposal: human-agent interrogation
`docs/HUMAN_AGENT_INTERROGATION_PROPOSAL.md` records a proposed,
**not implemented** bidirectional inquiry protocol. A human or an agent may
initiate an evidence-traceable question, challenge, what-if exploration,
or protected decision request; answers are classified and promoted to
binding knowledge only through existing authority/verification gates.
This is intentionally deferred until after Toy 1 end-to-end and Toy 2
retargeting qualification, except for necessary human gate questions.
It must not interrupt the active `TOY1-CON002` correction cycle or
be represented as working CLI/REPL functionality.

## Revised contracts: CON-002 at edffca69e8e7
The Contract Agent responded to independent CON-001 review `REVISE`
with additive contracts `CON-AP2-001-v2`, `CON-AP2-002-v2`,
`CON-AP2-003-v2` and `contracts/spine-v2.md`. It added a per-acquisition
sequence counter and persistent overrun signal for continuity, and a
71-byte field inventory within the 72-byte persistent-state allocation.
Result publication and expected-sequence metadata are allocated to the
separate shared-memory cap. Original CON v1 files remain history.

The authoring receipt `reviews/gates/TOY1-CON002-receipt-v2.json`
states `CONTRACTS_READY_FOR_INDEPENDENT_REVIEW`, *not approved*;
VO-002..VO-006 remain open and AD-003 remains accepted.

**Next:** run `process/tasks/TOY1-CON002-REVIEW.yaml` with unchanged,
reusable `REVIEW_CON` playbook. Verify F01 closure including counter wrap,
the 2^32-gap qualification and persistent overrun semantics; verify F02
with concrete field counts and nonoverlapping shared ownership. No
DE internals or C implementation may advance before accepted review.

## Independent CON-002 review: 0f9a2921d8f0

The independent review `reviews/gates/TOY1-CON002-independent-review-v2.json`
returned `REVISE` / `CON_REVISION_REQUIRED`. Finding `CON002-F02`
confirmed the 71-byte field accounting closes the original F02 contract-level
defect; physical layout remains VO-002. `CON002-F01` is **blocking**:
a non-atomic acknowledgement can erase a newer overrun indication, and the
32-bit modulo sequence alone cannot reveal a full counter-period gap unless
the producer/handoff enforces a checkable maximum gap or equivalent evidence.

Next invocation: `process/tasks/TOY1-CON003.yaml` using the unchanged
`REVISE_CON` playbook, with the independent review as the trigger.
The agent should produce additive, versioned contract drafts that specify
race-safe observation/acknowledgement and an enforceable continuity bound, or
record an unresolved producer/integration requirement. Do not invent physical
hardware guarantees. Preserve v1/v2, open VO-002 through VO-006, accepted
AD-003, approved AP-002 and original AS/F. DE refinement and implementation
remain blocked pending favorable independent contract review.

## Contract revision candidate: CON-003 at d995e15fe453
The Contract Agent produced CON-AP2-001/002/003-v3 and spine-v3,
preserving v1/v2 history, the provisional AP-002 selection, accepted
AD-003, and open VO-002 through VO-006. Its submission receipt reports
`CONTRACTS_READY_FOR_INDEPENDENT_REVIEW`, not approval.

The revisions replace clearable overrun acknowledgement with a
producer-owned saturating loss epoch, and propose an independently
operating watchdog to rule out a full 32-bit sequence-counter period of
undetected acquisition gaps. The 71-byte persistent inventory remains,
and additional shared/watchdog state still requires accounting evidence.

**Next:** `process/tasks/TOY1-CON003-REVIEW.yaml` invokes the same
reusable `REVIEW_CON` playbook. The independent reviewer must evaluate
correctness, feasible ownership, concurrency, resource attribution, and
whether the added mechanism has unjustified complexity. Avoid treating
unverified target capabilities as present. No DE refinement or firmware
approval follows solely from the author's receipt.
