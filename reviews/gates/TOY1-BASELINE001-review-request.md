# AS-001 v2: controlled baseline reconciliation review request

**Status:** Pending independent review, NOT an accepted active baseline.

## Proposed activation set

- `process/baselines/AS-001-v2-candidate.yaml`
- `process/ledgers/vo_ledger-AS-001-v2-candidate.yaml`
- `knowledge/architecture/AS-001/statement-v2.md`
- `knowledge/architecture/AS-001/verification_plan-v3.md`
- `knowledge/architecture/AS-001/verification/VO-004-v2.md`
- `process/decisions/AP-002-AS-V2-RECONFIRMATION-001.yaml`
- `reviews/gates/TOY1-AS002-independent-review-v3.json`

## Review questions

1. Is the proposed active AS exactly the independent-review-acceptable,
   sample-indexed newest-32 candidate? Is its publisher boundary external?
2. Does the later explicit human Option A decision correctly supersede
   only the old AP-002 1 ms applicability premise? Are C-002, C-003,
   PR-002 and F-001 unchanged?
3. Are all VO identities, owners, states and applicable due stages
   carried without discharge? Does VO-004 remain OPEN at IMPLEMENTATION
   with an appropriate source/authority chain? Is VO-001 limited to its
   synthetic input domain?
4. Does AD-003 remain accepted risk with unchanged F comparison,
   final-acceptance deadline, owner and fallback? Are historical records
   immutable?
5. Does the baseline deliberately exclude unsupported loss epochs,
   watchdogs, 1 ms deadlines and unverified concurrent-reader guarantees?
6. Would a new minimal CON task now be traceable to the corrected
   AS and approved AP-002 selection without reviving old CON-v4 scope?

## Exit

Return an additive independent receipt identifying approved candidate
hashes, blocking findings or explicitly limited acceptance. No firmware,
DE implementation, physical publisher verification or VO discharge.
Do not mutate the authoritative ledger within the review invocation.
If accepted, an explicit *activation* operation can apply the reviewed
VO/AS index and then launch the minimal CON task.
