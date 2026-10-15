# Toy 1 ERS revision 2: explicit coverage of accepted CON/DE obligations

Status: candidate inventory correction, not independent ERS acceptance.
Base: `830f91a98d4adf93c03079bc326286601a789e1f`.
Review: [REVIEW_ERS-1d5aeec83447](../reviews/gates/REVIEW_ERS-1d5aeec83447-receipt.json), disposition REVISE.
Input: [toy1-input-v2.json](../process/verification/toy1-input-v2.json).
Task: [TOY1-VERIFY-ERS002](../process/tasks/TOY1-VERIFY-ERS002.yaml).

## What the review found

The first candidate faithfully carried eight declared items, but the declared
inventory omitted finer accepted CON/DE obligations. F-ERS-001 identifies concrete
C expression, multiplication-promotion and legal-domain correspondence. F-ERS-002
identifies conditional SRAM category budgets and attribution/evidence duties.
These are failures of inventory completeness, not findings that the C is wrong.

This correction changes project input, not the generic kernel. No operation,
playbook, schema, test, firmware, accepted source or VO/AD state is changed.
The first inventory, generated artifact/briefing/receipt and independent review
are preserved. The new inventory pins the old input and the review receipt.

## Candidate change map

The eight original normative statements and projection IDs are retained.
Thirteen named facets bring the inventory to 21 requirements and 21 claims.
These identifiers identify projections of existing authority, not new product
requirements or newly approved contract versions.

| Finding | Added projection IDs | Existing source / obligation |
|---|---|---|
| F-ERS-001 | CON-ARITH-BOUNDS | CON-AP2-002-v6: square, final-sum and add-first bounds from valid state; R-003/VO-006 |
| F-ERS-001 | CON-C-EXPRESSIONS | CON-AP2-002-v6 and DE-AP2-UPDATE-v7: actual widths, conversions, evaluation order and correspondence; R-003/VO-006 |
| F-ERS-001 | CON-C-MULTIPLICATION | CON-AP2-002-v6: widen before multiplication unless concrete promotion rules establish safety; R-003/VO-006 |
| F-ERS-001 | CON-C-DOMAIN | CON-AP2-002-v6: legal-domain protection and representation correspondence; R-003/VO-006 |
| Completeness associated with F-ERS-001 | CON-ROLLING-TRANSITION | CON-AP2-002-v6: valid state, oldest-slot replacement and modulo-32 advance; VO-004/005/006 |
| F-ERS-002 | CON-SRAM-CATEGORIES | CON-AP2-003-v6: all seven ceilings, 1,792-byte allocation and 256-byte reserve |
| F-ERS-002 | CON-SRAM-INVENTORY | CON-AP2-003-v6 and DE-AP2-RESOURCE-v7: each byte, owner, category, lifetime, nonoverlap and full charged-SRAM scope; VO-002 |
| F-ERS-002 | CON-SRAM-NESTING | CON-AP2-003-v6: worst-case activity and applicable stack/context nesting, without selecting a topology; VO-002 |
| F-ERS-002 | CON-SRAM-SHARED | CON-AP2-003-v6: conservative attribution and no double-counting; VO-002 |
| F-ERS-002 | CON-SRAM-DYNAMIC | CON-AP2-003-v6: bounded live peak if dynamic allocations are used, not a heap prohibition; VO-002 |
| F-ERS-002 | CON-SRAM-EXCLUSIONS | CON-AP2-003-v6: evidence for exclusion of unrelated allocations; VO-002 |
| F-ERS-002 | CON-SRAM-INFEASIBLE | CON-AP2-003-v6: reviewed revision, not silent budget overrun; VO-002 |
| F-ERS-002 | DE-SRAM-PARTITIONS | DE-AP2-RESOURCE-v7: complete per-element accounting table and review on infeasibility; VO-002 |

## Evidence maturity is not changed

The category budget is an existing conditional contract commitment. Concrete
inventory, actual integration, overlap/nesting and physical fit remain due at
IMPLEMENTATION. DE subceilings remain reviewable accounting assignments, not
measured capacities; preserve the clarification DE007-C01 in
[the accepted DE review](../reviews/gates/TOY1-DE-independent-review-v7.json).
No target, task/ISR arrangement, heap prohibition or buffer is invented.

The existing mathematical rung now targets `ERS-CON-ARITH-BOUNDS` explicitly,
rather than appearing to cover every facet of R-003. It still has a MODEL_ONLY
binding. It cannot establish C promotions, concrete domain enforcement, generated
code, memory fit or any product VO. Those claims remain unplanned by this limited
adapter and must stay open. Planning is still a separately reviewed later stage.

The source documents leave out-of-domain behavior unspecified. The legal-domain
facet must not be interpreted as a new requirement for rejection, clamping,
watchdogs or runtime range reporting. Quiescent reset remains unchanged.

## Assumptions and annotations

The prior blanket publisher-continuity text is removed from individual claim
assumption lists and retained as external context in the non-claims. The legal
input, valid-state and lifecycle restrictions are explicit in the relevant claim
domains and statements. An unrelated publisher promise must not condition SRAM,
no-FPU or initialization obligations. Initialization does not assume that its
own postcondition already holds. This interpretation remains subject to review.

Only the original six source/host observation annotations are retained. The new
facets are not marked observed just because their requirements have been written.
Consequently, more annotation gaps in the briefing are expected. They are not
new product defects, proof of absent code, or a reason to demand target evidence
before reviewing the ERS's semantic coverage.

## Next local action

Use the existing documented VK-001 correction path: new input, new task ID,
deterministic DERIVE_ERS, then the existing independent REVIEW_ERS operation.
Do not feed the REVISE receipt into an advance-to-planning transition. Automatic
revision generation remains outside VK-001; this is an explicit versioned project
input correction, not a new framework branch or a bespoke reviewer prompt.

```bash
python tools/task.py inspect --manifest process/tasks/TOY1-VERIFY-ERS002.yaml
python tools/task.py run --manifest process/tasks/TOY1-VERIFY-ERS002.yaml
cat reviews/verification/TOY1-VERIFY-ERS002/briefing.md
manifest="$(python tools/next_task.py emit --receipt reviews/verification/TOY1-VERIFY-ERS002/receipt.json | jq -er '.manifest_path')"
python tools/task.py inspect --manifest "$manifest"
python tools/task.py run --manifest "$manifest"
```

The independent reviewer determines whether F-ERS-001 and F-ERS-002 are addressed
and whether other accepted obligations remain missing. This note is not that
verdict. Neither Archbot tests nor the new DERIVE_ERS task were run by the authoring
assistant. Local execution, semantic review and actual target qualification remain
separate evidence.
