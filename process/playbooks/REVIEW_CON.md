# REVIEW_CON: Independent contract gate

**Reusable operation:** `REVIEW_CON`  
**Role:** `verification-agent`. Reviewer must be independent of the contract-authoring invocation.

## Inputs and authority

Start from the task manifest's architecture spine, selected-AP authority receipt,
draft contract spine, selected AP, AS, applicable proof assumptions and acceptance
scope, verification plan, VO and AD ledgers, and the contract-coverage matrix.

Validate sources and revisions. A draft contract is not approved merely because
it has valid Markdown/YAML or a green structural check. Never auto-accept
an architecture, settle an unapproved tradeoff, discharge a VO, or implement code.

## Review questions

When the submitted authoring receipt is `CONTRACTS_UNRESOLVED`,
**review the draft rather than assuming that every listed uncertainty
is a blocker**. Classify each unresolved item as (a) a present contract
semantic blocker, (b) an external interface assumption with a separately
assigned integration owner, (c) an implementation- or target-stage VO,
or (d) an unsupported new requirement. Cite exactly which AS/authority
clause makes an item binding *at this gate*. A missing final linker map
cannot by itself block CON approval when implementation evidence is not
due, but a missing credible resource-category envelope or a contradictory
interface precondition may. If a target execution topology is unspecified,
do not silently install one merely to fill in a memory table.



1. **Complete boundary:** For each contract, are producers, consumers, legal input
   and output ranges, units, ownership, reset behavior, timing, fault/error
   semantics and publication ordering precise enough to implement independently?
2. **Composable behavior:** Are preconditions satisfiable and compatible with
   other contracts? Does one component's postcondition imply the next component's
   precondition? Detect gaps, duplicate ownership, races and circular promises.
3. **Invariant preservation:** Identify the exact approved theorem assumptions.
   Ensure a design may implement them without relying on unstated initialization,
   concurrency, sample-ordering, arithmetic or fault-handling behavior.
4. **Stage maturity:** Distinguish platform-neutral contract semantics from
   physical target choices. If the latter are deferred, require a named owner,
   verifiable acceptance condition, and due stage. **Never defer a semantic
   ambiguity that could change an approved requirement or interface behavior.**
5. **Resource contracts:** Verify the **authorized** memory/timing model,
   charged categories, simultaneous peaks, overlap/attribution rules,
   declared margins and demonstrable bounded assumptions. Evaluate the
   maturity of numeric allocations against the actual gate and VO due stages.
   Treat zero-heap, stack/ISR topology, atomic publication and watchdog
   claims as conditions **only when expressly adopted by an approved
   integration contract**. A projected allocation is not a measured
   physical upper bound. Do not confuse state SRAM under F with the
   total detector-attributable C-002 accounting boundary.
6. **Obligation coverage:** Map every AS constraint/requirement, outstanding VO
   and accepted AD to a contract or explicitly controlled external integration
   obligation, a DE responsibility, verification owner, method and due stage.
7. **Independent checks:** Recalculate numerical limits and compare all
   source references to their authority. Run structural/tests applicable to the
   gate. Do not conflate host tests with target evidence.

## Outcomes and written receipt

Write an additive, versioned independent review with:
- exact input revision and relevant artifact paths/hashes;
- per-CON finding with a minimal counterexample where possible;
- a requirement/VO/AD coverage verdict;
- `ACCEPT`, `ACCEPT_WITH_CLARIFICATIONS`, `REVISE`, or `REJECT`;
- independent next-stage recommendation:
  `CON_ACCEPTABLE_FOR_DE_REFINEMENT` or `CON_REVISION_REQUIRED`;
- all continuing verification obligations and interface assumptions;
- exact commands, test results and uninspected material.

A favorable outcome **accepts interface definitions only**. DE internals,
C implementation and final target verification remain separate gates.

Do not modify the CON drafts under review. If flawed, produce concrete
review findings for a later, versioned Contract Agent correction.
