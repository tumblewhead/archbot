# CLN-001 process retrospective: evidence progress, human attention and orchestration

Status: **ENGINEERING PROCESS IMPROVEMENT NOTE / PROPOSAL, NOT AN ACTIVATED FRAMEWORK POLICY**.
Date: 2026-10-18.
Repository workstream: `experiment/toy1-pipe-cleaner-001`.
Scope: current synthetic, pre-freeze CLN-001 diagnostic and planning for a
future *distinct* orchestrated Toy 1 replay. This note changes no active
AS, proof, F, AP, gate, VO, baseline, orchestrator permissions or framework
freeze status.

## 1. Latest actual evidence and user-identified problem

The original Stage-9 AP feasibility results were independently audited in
`reviews/diagnostics/CLN-001-TASK-010/REVIEW-AP-EVALUATION-010.md` and
`REVIEW-AP-EVALUATION-010.json`, archived at commit
`e5d2cfde2c856cc84192b294ac8c42a8746ba5aa` (source-review scope).
Review disposition: `READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`.
The reviewer reproduced the Stage-9 finite-model programs with matching
completed outputs: 299,296 accepted events, 24,192 invalid attempts,
11,386 resets and 897,888 A/B/C oracle comparisons. Model evidence,
counterexamples and output-byte provenance were qualified only to their
declared scope.

Remaining HIGH findings:
- `R010-4`: no actual consumer rank decoder, acceptance/publication/
  outstanding-result lifecycle, restart/reset association or safe
  information lifetime demonstrated.
- `R010-5`: candidate C's RN and C-HIST snapshot providers, retention,
  availability and exclusive upstream ownership are UNSUPPLIED.
- `R010-6`: no complete peak-live owned/shared RAM, actual stack,
  chosen-width build, compute cycles or device-energy measurement.
  No full evidence-compatible Pareto order.

All realized H1–H6 and F values remain UNKNOWN for A/B/C;
T002-2..8 remain OPEN and R4 detection is deferred. Candidate selection,
CON/DE/C, target/product verification and formal cleanroom did not follow
from favorable source review.

**Process shortcoming:** repeated high-quality source/evidence review can
advance *confidence in the UNKNOWN* without materially reducing
decision-relevant uncertainty. Reviews are still necessary for
independence and authority, but should not replace the experiment,
contract inquiry or realization that creates the next evidence.

**Human time issue:** the human repeatedly performs mechanical
pull/prepare/Codex launch/archive/push/recovery. These actions use
human attention without normally contributing engineering decisions.
The manual agent bootstrap and occasional local/remote branch skew
have interrupted continuity (e.g. the Stage-9 push-fast-forward
handoff); no source evidence was lost. These are orchestration targets,
not arguments for weaker review gates.

## 2. Recommended sequencing, subject to separate process authorization

1. **Fix evidence progression in the current diagnostic now** without
   changing accepted claims. After the independently reviewed Stage-10
   evidence, the CLN-001 delegate may authorize a bounded *evidence
   acquisition* task: actual consumer information/lifecycle contract
   candidates, source-anchored impossibility/feasibility findings,
   and a small chosen-width C numeric-kernel prototype as
   conditional realization evidence. Query C's external-service
   ownership/availability separately, not by assumption.
2. **Complete the current CLN-001 end-to-end diagnostic** through
   evidence-supported reversible AP commitment, CON, DE, C and
   appropriate independent verification. Record exact residual
   qualification limits and stop at truthful scope. Do not silently
   skip protected gates to finish faster.
3. **In parallel, build a constrained orchestrator pilot** on a
   separate authorized implementation branch, first through
   deterministic offline replay of existing CLN-001 event/receipt
   history. Demonstrate accurate routing, source pins, genuine
   reviewer independence, restartable archiving and escalation.
   Then authorize a small live dispatch/repair slice. No general
   auto-write/auto-push or autonomous human-equivalent decisions
   follow from this note.
4. **After obtaining a complete baseline and a qualified minimum
   orchestrator**, run a distinct Toy 1 from original unsolved BKP
   under reviewed context and runtime isolation. Never contaminate
   its agent workspace with the prior architecture, worked answers,
   repository history or hidden evaluator. Compare against the
   baseline, not against a post-hoc memory reconstruction.

Reason not to restart immediately: doing so sacrifices the first
end-to-end reference and confounds the orchestrator's effect with
concurrent changing architecture rules. Reason not to postpone
all orchestration work: recorded receipts already allow useful
offline execution and recovery tests without redoing the problem.

## 3. Proposed Evidence Acquisition Gate

A *material decision-blocking unknown* should have a typed evidence
acquisition plan, in addition to its VO/ERS and status. Example
record (PROPOSED, not executable policy):

```yaml
schema: proposed-pc-evidence-acquisition/v0
unknown_id: R010-4
scope: CLN-001
affected_claims: [H2, H3, H4, H5]
decision_blocked: "Provisional AP/full interface feasibility"
evidence_owner_role: interface-feasibility-engineer
producer_task: "Consumer/debt/reset information boundary and trace experiments"
minimum_falsifier:
  - "Two admitted accepted histories, same consumer-visible state, different required n"
  - "Old owed result aliases a new reset-sequence result"
method: "Construct actual consumer information-flow/refinement; test witness traces"
resource_scope: "Detector-owned, shared and exclusively upstream-owned independently"
due_gate: "Before a concrete full-interface/AP commitment"
expected_output: "Source-pinned model/contract proposal plus bounded feasibility result"
independent_review: REQUIRED
authority_on_changed_AS_or_service: SEPARATE_EXPLICIT_DECISION
next_action_if_inconclusive: "State minimal missing operating assumption or service"
```

At a proposed progress gate, classify each high-impact UNKNOWN into:
- **RESOLVE_NOW:** blocks the next admissible decision; create
  discriminating evidence with a named owner and output.
- **DEFER_WITH_DUE_STAGE:** acceptable under a reversible commitment,
  with an explicit due-stage evidence activity and risk/AD if required.
- **ESCALATE_AUTHORITY:** solving it would change accepted operation,
  constraints, F or external dependencies; request scoped human/delegate
  decision rather than guessing.

A new generic *review of unchanged UNKNOWNs* should not be proposed
as a surrogate for evidence acquisition. Required independent review
of **new** evidence or a new authorized decision remains binding.
The rule must recognize genuine cross-cutting counterexamples and
blockers; it must not demand final hardware tests before a stage that
creates hardware. It should surface conditional feasibility conflicts
without declaring universal impossibility.

### Concrete discriminators from Stage 10

- Consumer `n`: does the ACTUAL consumer have sufficient
  accepted-only event history and reset identity to decode the
  exact rank, including consumer restart and indefinitely long
  accepted sequences? This is not discharged by harness oracle `n`.
- Output debt: which component retains each accepted result
  through stalls/reset, and under what explicit accepted/publisher
  scheduling assumptions? A Q-entry queue alone fails under Q+1
  accepted unpublished distinct results with no other storage/replay
  or lossless coordination. This conditional conflict does not
  automatically falsify all possible architectures.
- Candidate B: does a fixed-width C kernel preserve the age cursor,
  square tail and S invariant across reset, rejection and valid
  transitions with verified memory operations?
- Candidate C: is there an AUTHORIZED provider for immutable
  correct-event prior history and exact ordinal? Which resources,
  retry/pinning costs, availability and device electrical energy
  are owned by which side? No external service is assumed.

## 4. Proposed minimum orchestrator, not a fictional all-powerful agent

Existing proposal: `docs/PROCESS_ORCHESTRATOR_HUMAN_ATTENTION_PROPOSAL.md`.
Existing bounded mechanisms: `tools/task.py`, `tools/next_task.py`,
`VK-001`, repository spines, gate and archive receipts. They are
not an installed autonomous process orchestrator.

**Deterministic transition/execution engine**:
- Resolve next eligible task using exact active authority, DAG
  prerequisites, review dispositions and evidence-acquisition state.
- Build minimal positive-allowlist context and verify hashes.
- Launch separate authorized author/reviewer invocations with
  recorded runtime identity and truthful isolation limitations.
- Validate actual output schema and source identities, preserve
  original bytes, and recover idempotently from partial archive/
  commit/push failures.
- Route `REVISE` to a bounded correction, `UNRESOLVED` to a
  missing-evidence task, and favorable *review* only to the correct
  independent authority decision. Do not self-approve.
- Preserve retries, stop states and exact Git revisions in a
  durable event log; require safe fast-forward handling and report
  contradictory refs. No force push.

**Sensemaking dialogue agent**:
- Emit concise, source-linked stage briefings, surprises, contrasts
  with prior understanding, and evidence-to-decision relationships.
- Surface genuinely new human choices: changed requirements,
  competing engineering objectives, AP/AD commitment, high-impact
  risks, source contradictions, rejected operating assumptions.
- May suggest experiments and insight, but cannot manufacture
  approvals, new providers, security isolation or product evidence.
- Allow a human to inspect and intervene at any time, and interrupt
  work on critical falsifiers while unrelated eligible tasks can
  proceed.

**Human attention policy**: keep human in oversight and discretionary
engineering decisions, not obligatory shell scripting. Automate
mechanical steps *after* scoped execution/credential policy is
approved. Do not give unbounded LLM authority to launch arbitrary
agents, edit protected baselines or push unknown output.

## 5. Pilot stages and measurable comparison

- P0: replay current Toy 1 receipts without acting on Git or Codex;
  assert next-state choices, source identity, stop/revise/accept
  boundaries and recovery from synthetic missing/duplicate outputs.
- P1: new bounded live task; agent prepare/execute/review/archive
  with real separate invocations, permissions and sandbox evidence.
  Exercise interruptions, review REVISE and remote-ahead push.
- P2: complete fresh unsolved Toy 1 with orchestration; verify
  noncontamination and compare final obligations/qualification.

Metrics for both baseline and orchestrated run:
- Elapsed time from task eligibility to reviewed next decision, and
  from original BKP to end-to-end terminal scope.
- Human minutes and interruptions: oversight versus mechanical.
- Number of retries, task launches, source/manifest failures,
  context leaks, reversions, authority escalations and recovery time.
- New decision-blocking unknowns resolved per iteration and per
  engineering hour, distinguished from UNKNOWNs merely re-reviewed.
- Agent/tool invocations, token/compute cost, review cycles, code
  defects, passed/failed evidence rungs and remaining obligations.
- Independent correctness and provenance quality versus baseline.
  **Do not sacrifice correctness/authority for throughput.**

Retrospective numeric/time values are intentionally not invented:
many earlier local run durations and human-intervention timings
were not instrumented. Record them prospectively from P0/P1 onward.

## 6. Decision / authorization status

- This note is a preservation artifact and route proposal.
- The Stage-10 source review at the referenced commit authorizes
  a separate CLN-001 delegated **evidence disposition**, not AP
  selection, CON/DE/C or framework-process activation.
- A generic Evidence Acquisition Gate and autonomous orchestrator
  need separate reviewed process-policy/implementation authorization.
- Restarting Toy 1 needs its own context-isolation and project
  authorization. The existing experiment branch is a valuable
  baseline; do not repurpose it as a fresh-agent cleanroom.
- All open T002-2..8, deferred R4 and historical Toy 1 VOs remain
  binding with their original due/qualification scope.
