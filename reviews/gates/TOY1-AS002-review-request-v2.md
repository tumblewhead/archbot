# Independent AS review request: TOY1-AS002 revision 1

**Requested gate:** Independent review of draft `AS-001-v2` and its linked
correction candidates. This authoring submission does not accept its own
revision.

## Review inputs

- Approved scope authority: `process/decisions/AS-001-SCOPE-CORRECTION-001.yaml`
- Original AS, original BKP sources, and provenance annotation
- Draft `knowledge/architecture/AS-001/statement-v2.md`
- Corrected candidate `knowledge/architecture/AS-001/verification_plan-v3.md`
- Candidate `knowledge/architecture/AS-001/verification/VO-004-v2.md`
- Existing VO/AD ledgers, accepted PR-002, C-002 authority, F-001, AP-002 authority, and contract history
- Impact analysis: `reviews/gates/TOY1-AS002-impact-v2.md`
- Authoring receipt: `reviews/gates/TOY1-AS002-revision1-authoring-receipt.json`
- Blocking review: `reviews/gates/TOY1-AS002-independent-review-e239ff6.json`

## Questions for independent reviewer

1. Does VP-001-v3 assign detector-side one-update-per-accepted-sample
   evidence an unambiguous `IMPLEMENTATION` due stage consistent with
   VO-004-v2?
2. Is any future integration throughput, overload, or deadline requirement
   clearly separate, conditional on authority, and assigned its own owner,
   acceptance criterion, VO, and due stage if approved?
3. Does the unchanged AS-v2 and its provenance remain within the approved
   scope, including the explicit external publisher assumption?
4. Are AP-002 applicability, accepted AD-003, F-001, and open VOs preserved
   with the required authority actions clearly identified?

## Scope limits

This review cannot approve CON, implement firmware, amend F-001 or C-002,
change AP authority, accept new AD, discharge a VO, or verify physical
publisher performance. A favorable AS review does not perform those actions.

Please record input revision and candidate hashes, findings, unresolved
obligations, review limits, actual checks, disposition, and next eligible
action. Structural validation is not engineering acceptance.
