# Independent review request: TOY1-CON004

Review the v4 draft contracts against `reviews/gates/TOY1-CON003-independent-review-v3.json` and specifically determine:

1. Whether CON003-F01's ordered loss/handoff/check/commit protocol closes the race without relying on an unstated producer guarantee, and whether result readers and session transition are covered.
2. Whether CON003-F02's successful-handoff restart event, `2^32-1` period bound, conservative conversion, margin, and task-independent invalidation are sufficiently checkable while correctly leaving target capability as evidence due.
3. Whether CON003-F03 is correctly left unresolved absent numeric allocation evidence, and what minimum bounded object inventory is needed before DE refinement.
4. Whether v4 preserves the 71-byte persistent contract-level accounting and all approved authority, VO and AD boundaries.

Do not treat the draft's semantic preconditions as target evidence. No DE refinement or implementation is authorized by this request.
