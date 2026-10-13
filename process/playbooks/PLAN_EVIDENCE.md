# PLAN_EVIDENCE: Resolve a stage-blocking knowledge or feasibility gap

**Reusable operation:** PLAN_EVIDENCE
**Role:** evidence-planning-agent
**Trigger:** A versioned stage submission receipt explicitly marked UNRESOLVED.

## Procedure

1. Verify the originating task, artifact revision, accepted authority and precise
   unresolved claim. Recover upstream context by reference, not recursively copied text.
2. Identify the **smallest missing evidence** required at the current gate.
   Separate what is knowable symbolically, what requires a DE design, and
   what cannot be verified until implementation or target validation.
3. Develop an explicit evidence candidate: bounded allocation model,
   mathematical derivation, trusted source requirement, test method,
   or a conditional feasibility argument. Label unknown coefficients and
   assumptions. Where helpful compare simpler alternatives.
4. If a resource budget is needed, enumerate every charged category,
   ownership, maximum size, concurrency/overlap and margin. Do not
   invent actual compiler layout, hardware availability or target timing.
5. Preserve all binding AS/F obligations, accepted source/proof scope,
   approved architecture and existing VO/AD authority. An evidence plan
   cannot relax limits or discharge a VO.
6. Make findings actionable for the original stage author: specific
   proposed constraints, acceptance checks, required inputs and owners.
   If no defensible bound is possible, record a precise blocker and the
   minimal authority or human-source question instead of fabricating PASS.
7. Create a versioned plan and concise receipt, including originating
   task ID, Git revision, exact evidence references and one of:
   - schema: pc-evidence-plan/v1
   - status: EVIDENCE_PLAN_READY_FOR_REVISION (with actionable evidence)
   - status: EVIDENCE_STILL_UNRESOLVED (with a precise blocker)
8. No artifact produced here is independently accepted merely by
   being generated. The original producer must revise its versioned
   artifact, followed by the applicable independent review.

## Forbidden actions

Do not rewrite an approved AS/F/AP, overwrite reviewed artifacts, accept
Architectural Debt, discharge verification obligations, approve contracts
or design elements, or implement firmware.

The operation is reusable for proofs, APs, contracts, DEs, and code: the
problem-specific source and verification policy come from the task manifest.
