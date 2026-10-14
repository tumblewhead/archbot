# VS-002: Verification and the Human Interface

**Date:** 2026-10-14  
**Base:** `13f9ac4c5b334efba69daa8b8ff037a0b1ce6120`  
**Status:** Worked design study and self-adversarial review, not independently accepted.  
**Related:** [VS-001](VERIFICATION_DESIGN_STUDY_VS001.md), [verification theory](THEORY_OF_VERIFICATION.md), [human-agent interrogation](HUMAN_AGENT_INTERROGATION_PROPOSAL.md), [project archives](PROJECT_INTERACTION_ARCHIVE_PROPOSAL.md).  
**Production boundary:** Documentation only. No new executable stages, UI, firmware changes, or VO discharge.

## Executive result

VS-001 proposed a small typed evidence checker. This second pass found that a correct evidence result can still be misrepresented when the UI summarizes it, invites an approval, changes a filter, or reuses a stale screen. The UI must preserve scope and authority, not merely display tool status.

Keep three distinct records: what was said or proposed; what the team authorized; and what evidence establishes. Conversation is source material, not automatically an active requirement. Approval of an assumption does not verify physical behavior. A valid conditional theorem does not automatically establish product safety.

The complete companion study packet supplied in the conversation contains a roughly 4,800-word notebook, an offline HTML reader, `probes_vs002.py`, deterministic JSON results, and an integrity manifest. Those executable study fixtures are not installed in this repository. **37 standalone checks matched their stated expectations**, including two orderings of a scope change and approval. No repository suite, target compiler, actual UI, human study, NLP interpreter, or trusted proof backend was exercised. These are bounded self-authored probes, not independent qualification.

## Breadcrumbs: candidate, attack, revision

| Round | Candidate idea | Attack | Revision |
|---|---|---|---|
| 1 | Correct evidence can be summarized freely | Qualifiers disappear from the headline | Structured scope-preserving result card |
| 2 | Human approval settles a missing fact | Assumption approval becomes hardware evidence | Separate authority from evidential support |
| 3 | Reuse the queue proof after a clarification | Resume preserves initial backlog | Mode/state-specific claims and targeted inquiry |
| 4 | Repeated questions establish consistency | Different modes or statement kinds appear contradictory | Scoped proposition comparison |
| 5 | Every important result requires approval | Paperwork and repeated acknowledgments create little information | Material-commitment approval; authorized work continues |
| 6 | Aggregate confidence summarizes progress | Filters and optional checks hide essential failures | Claim-level evidence, readiness and denominators |
| 7 | Interactive sliders can edit the active model | Hypothetical changes or stale approvals become actual authority | Separate exploration, proposals and transactions |
| 8 | Event history supplies meaning and causality | Provenance is confused with implication or causal proof | Typed projections and inert archive replay |
| 9 | More explanation guarantees better judgment | Persuasion and repeated agreement mimic comprehension | Consequence-focused dialogue and actual user evaluation |

These rounds are an inspectable reconstruction of design alternatives and counterexamples, not private model reasoning transcripts.

## 1. Scope must survive the display

Suppose the actual finding is: examined host C99 cases passed; the abstract recurrence has a valid conditional argument; target memory and integration remain open. A headline saying "Detector verified; ready for deployment" is false even if the underlying evidence checker was correct.

A consequential result card should expose subject/build, domain/mode, method, supported conclusion, assumptions, unresolved dependencies, snapshot, actual-versus-hypothetical view, and current applicability. Generated prose may explain these fields, but it must not independently choose the authoritative status or permitted action.

The standalone card probes reject missing scope, host-to-target promotion, and a hypothetical result presented as product acceptance. They do not verify the logical entailment of arbitrary English explanations. That limitation remains explicit.

The evidence checker must also not be overstated: metadata consistency is not theorem checking. Exact conclusions still depend on sound primitive checks, model translation and correspondence as identified in VS-001.

## 2. Authority and evidence are orthogonal

An assumption may be authorized for development and still unverified in hardware. An observed counterexample may be valid evidence without authorizing a product-scope change. Responsibility assignment is not a physical guarantee.

Distinguish the actions `ACKNOWLEDGE`, `ANSWER`, `AUTHORIZE_PROPOSAL`, `ACCEPT_REVIEWED_EVIDENCE`, and `ACCEPT_STATED_RISK`. These are proposed semantic actions, not installed APIs. A conversational reply may express an action, but a consequential transition must bind the exact proposition, subject and scope.

Do not block all conditional engineering until the environment is fully verified. Do not label authorized assumptions as measured facts. Both mistakes recreate prior process failures in opposite directions.

## 3. Worked queue example: initial state matters

This is an illustrative queue after packet assembly, not an instantaneous physical-UART arrival model. New arrivals obey `alpha(t)=b+r*t`; existing backlog `q0` is separate and not counted twice. Service is at least the rate-latency envelope with rate `mu` after latency `T`, and `r<=mu`.

Under those assumptions:

```text
q_bound = q0 + b + r*T
margin = B - q_bound
```

Set `B=256 bytes`, `b=160 bytes`, `r=9000 bytes/s`, `mu=12000 bytes/s`, and `T=8 ms`.

| Mode | q0 | Bound | Margin |
|---|---:|---:|---:|
| Empty cold initialization | 0 | 232 bytes | 24 bytes |
| Resume with retained data | 64 | 296 bytes | -40 bytes |

The cold-start theorem can remain true while failing to cover resume. A concrete model witness starts with 64 retained bytes, adds a 160-byte batch and then nine bytes each millisecond, with no departure before 8 ms. Required occupancy is 251 bytes at 3 ms and **260 bytes at 4 ms**. This is an abstract admissible witness, not physical test evidence.

The symbolic threshold is `q0<=24 bytes`. The useful inquiry is therefore:

> Can resume at this enqueue boundary begin with more than 24 bytes already queued? The empty-start argument leaves only that much margin; I have not found a resume-state guarantee.

After a reply of "up to 64 bytes," candidate design directions include 296 usable bytes, latency at most approximately 3.556 ms, a burst bound at most 120 bytes, or an enforceable entry-state bound. None is automatically authorized. Flushing, dropping data or excluding resume might violate other requirements.

Through the three stages: ERS distinguishes modes and initial-state ownership; planning adds the hyperedge `{mode, initial_backlog, burst, latency, capacity}` directly from the equation; execution preserves the cold-start result and records the new witness with its precise model scope.

## 4. Check scoped consistency, not isolated sentences

"Cold initialization clears the queue" and "resume preserves queued bytes" can both hold. "The publisher owns continuity" and "a publisher error was observed" concern different kinds of propositions. Maximum occupancy and minimum free space have the same units but different semantic roles.

Before raising an inconsistency, compare project, subject, mode, effective time/version, units, reference/sign convention, semantic role, and statement kind. Show both original statements and the interpretation being compared. Allow compatible, different-scope, superseded, ambiguous, and genuinely conflicting outcomes.

The human must be able to correct the agent, identify a hypothetical statement, describe a new requirement, or answer unknown. Forced-choice menus cannot replace free-form engineering communication.

Revisit commitments when a relevant new consequence appears: a mode, counterexample, threshold, target or consumer changed. Repeating "are you sure?" without new context does not establish understanding. Proactive interviews still belong in discovery; not every valuable question must unblock a current gate.

## 5. Approval everywhere was a dead end

Requiring another approval for every completed rung creates procedural load without proving comprehension. Prefer: agents act within authorized scope and budget; independent checks assess actual evidence; humans approve material protected choices or explicit risk. Acknowledging a briefing is not blanket acceptance of its assumptions.

An unanswered question need not block unrelated work. If all currently plausible interpretations justify the same action, work may continue conditionally while preserving the question. When justified actions differ, ask, compare cheap branches, or collect evidence. This is a decision-stability test, not a fabricated numerical information-gain score.

Evidence reuse also needs scope. An exact property proved on `[0,255]` applies on `[0,63]` for the same subject and semantics; it does not automatically apply on `[0,511]`, another binary, or another property. Statistical distribution changes require separate reasoning even when textual ranges narrow.

Approvals should bind relevant dependency fingerprints and authority-policy versions rather than the entire repository HEAD. Unrelated documentation must not invalidate every decision. The standalone probe used a simpler coarse snapshot token; finer dependency reuse remains to qualify.

## 6. Denominators and readiness must not disappear

Construct 1,000 illustrative cases: 100 are accepted, of which 50 are covered and 50 are not; 900 are rejected and all 900 are covered. Overall coverage is 95%, accepted-case coverage is **50%**, and availability is 10%. These are exact constructed counts, not deployment statistics.

A "95% calibrated" badge hides the key failure. Filters may change the estimand, so the display must bind the selected population, denominator, model/build, selection rule and sampling/stopping protocol. Changes create a new view or proposal, not an invisible reinterpretation of an old result.

Similarly, 99 optional checks passing does not overcome one essential unresolved memory obligation. Keep execution progress, coverage, evidence support, unresolved assumptions, contradictions and authorized readiness distinct.

A sparse interaction plot must show omitted/fixed variables, mode, horizon, subject and evidence type. Absent cells are unknown, not green; interpolation is not proof. A what-if sweep and a frozen confirmatory campaign must remain distinguishable. If an engineer uses holdout results to tune a model, record that dependency rather than treating later validation as untouched.

## 7. Hypothetical exploration and stale clicks

An exploratory slider can immediately show a 512-byte buffer model, but it must not rewrite the actual 256-byte requirement or imply changed hardware. Keep actual recorded state, exploratory branches and explicit proposed changes separate.

A consequential command should bind project/scope, proposal ID and content digest, relevant snapshot, policy/role version, action kind and request identity. Check those at application time. If the screen showed r1 and the scope is now r2, explain the semantic change; do not silently rebase the approval.

The probes check both orderings of approval and change. Approval followed by change remains historical authority for the earlier state; change followed by approval rejects the stale command. Duplicate delivery returns the prior receipt without a second effect; reusing an ID for different content is rejected.

A late run still supplies evidence about its frozen inputs. Keep it and test applicability; do not discard useful history or let it unlock a materially changed current claim. Content hashes prove identity, not truthfulness.

These safeguards protect ordinary retry/resume behavior in the engineering tool. They impose no sequence counter, watchdog or security architecture on Toy 1 firmware.

## 8. UI, project spine and archive

Keep the six VS-001 verification objects: Claim, Model Binding, Rung Plan, Execution Record, Evidence Judgment and Engineering Briefing. Add project-owned interaction/decision events referencing them instead of duplicating all engineering knowledge into a chat database.

Record original statement, interpretation, authority action and evidence separately. Preserve parent events, relevant versions and explicit supersession. Distinguish when an operating assertion applies from when the team learned it when that matters.

Timeline order is not logical implication or causal proof. Use distinct projections for chronology, premise dependencies, experiment motivation, supersession, and proposed causal explanations. W3C PROV's entities/activities/agents distinction is informative but does not supply Archbot's inference or authority rules [S3].

A compact root spine links constituent dialogue, evidence, studies and event streams. Do not let it grow into a duplicate of all history. For the first local version, files and a transactional local index can suffice; a distributed broker or elaborate new service architecture is not required. Event sourcing offers historical reconstruction but brings concurrency, schema and projection costs [S2].

Archive replay must be inert by default: it must not rerun tests, execute commands, send messages or reapply approvals. Explicit reruns are new executions. Public exports may redact private content, but must declare completeness and the evidence limitations of unavailable sources. Original event records are not equivalent to all conversations being published to GitHub.

## 9. Explanation quality needs human evaluation

The existing explanation/correction design aligns with Microsoft's human-AI guidance [S1]. That does not prove that more explanation improves engineering decisions.

A 199-person experiment found cognitive-forcing interventions reduced overreliance relative to simple explainable-AI designs, but did not eliminate it; effective interventions could be less preferred, and overall team-performance improvement was not established in that comparison [S4]. A 2026 study of writing-plan review found benefits for an assumption-focused intervention in its setting [S5]. Neither validates this proposed firmware-engineering UI.

Use consequence-based questions to help the human improve the model, not repeated assertions of understanding or a score of human consistency. At meaningful ambiguities, invite the engineer's experience before presenting a favored design. Keep dissent, unknown and deferral legitimate.

The return-after-absence view should show new evidence and its scope, changed assumptions, which previous results still apply, the smallest open decision, and independent work that can continue. Acknowledgment anchors the digest; it does not prove comprehension.

Future user evaluation should measure detection of seeded scope/authority errors, decision quality, false inconsistency alarms, intervention time and avoidable rework, not just satisfaction, verbosity or self-reported understanding. No human study was run here.

## 10. Resulting stage-to-UI contract

| Stage | Durable output | Human interaction | Must not hide |
|---|---|---|---|
| ERS | Scoped claims, bidirectional source coverage, implementation gaps | Explain the interpretation; ask about modes and responsibility | Missing authority or omitted obligation |
| Planning | Rung DAG, hyperedges, model/oracle and sampling contracts | Explain why the experiment matters; explore alternatives | Unknown domain or physical assumptions |
| Execution/judgment | Frozen run, typed evidence, counterexample and limitations | Scoped result, consequence, next action | Timeout, stale applicability or target-evidence gap |

Every stage produces project-owned records. None automatically promotes conversation, authorization, process exit status or a modeled scenario into stronger evidence.

### Conditional assurance argument

Assume correct normative interpretation, primitive evidence checks, structured-status rendering and command validation. If consequential transitions require exact proposal/snapshot authorization and display status comes from the corresponding judgment, induction over accepted commands establishes that acknowledgments, hypothetical edits, duplicate deliveries and stale approvals do not activate protected commitments in this bounded model. Assumption adoption cannot verify hardware because no permitted transition makes that promotion.

This is conditional on those components. It is not a proof of arbitrary English interpretation, human comprehension, distributed atomicity, or physical model validity.

## 11. Remaining adversarial limits and next experiment

Realistic residual risks include wrong formalization, shared oracle defects, persuasive misleading prose, untested higher-order interactions, distribution shift, stale real-system projections, and missing/redacted evidence. They are not dismissed as absurd and are not all solved by more approval steps.

Preserve the roadmap: finish Toy 1, genericity audit/freeze, cleanroom replay without the future dialogue layer, implement dialogue, replay with it, then Toy 2 and scale. Build UI-compatible verification records now; do not require the full UI before the three-stage vertical slice or secretly include it in the no-dialogue qualification baseline.

The next useful vertical test is: correctly extract an obligation; identify an initial-state ambiguity; explain its threshold; receive a mode correction; update only affected applicability; preserve old evidence; execute the new witness; and store its briefing and source-linked discussion. Begin with scripted interaction fixtures, then evaluate actual engineers.

## References and claim limits

Project basis: VS-001 and the existing interrogation/archive proposals at the base revision. The calculations, UI contracts and protocol tests in VS-002 are new study proposals, not facts independently established by those documents.

- S1: Microsoft Research, Guidelines for human-AI interaction design: https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/
- S2: Microsoft Azure Architecture Center, Event Sourcing pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
- S3: W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- S4: Bucinca, Malaya and Gajos, To Trust or to Think (2021): https://arxiv.org/abs/2102.09692
- S5: Ghosh, Sarkar, Lindley and Poelitz, Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (2026): https://arxiv.org/abs/2601.18033

These sources ground borrowed concepts and cautionary lessons, not the correctness of this proposed Archbot integration. The full study packet remains a conversation artifact; this repository document preserves the worked results and intended contracts for later implementation and independent review.
