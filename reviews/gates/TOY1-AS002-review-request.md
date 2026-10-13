# Independent AS review request: TOY1-AS002

**Requested gate:** AS review of draft `AS-001-v2` and its linked correction
candidates. The authoring agent requests review and does not accept its own
revision.

## Review inputs

- Approved scope authority: `process/decisions/AS-001-SCOPE-CORRECTION-001.yaml`
- Authority evidence and bounded scope: `process/decisions/AS-001-SCOPE-CORRECTION-001.md`
- Source request: `process/decisions/AS-001-SCOPE-CORRECTION-REQUEST-v1.md`
- Independent scope-audit findings: `reviews/gates/TOY1-SCOPE-AUDIT-002.md` and receipt
- Original AS, original BKP sources, VP-001, VO-004, current VO/AD ledgers
- Accepted abstract proof PR-002, C-002 authority, F-001, AP-002 authority,
  and contract spine v4
- Candidate artifacts listed in `TOY1-AS002-authoring-receipt.json`

## Questions for independent reviewer

1. Does candidate R-001 express exactly one update per legal detector-
   accepted sample, independent of elapsed time, without implying unlimited
   throughput or a deadline?
2. Does R-002 clearly define the newest 32 accepted published samples,
   acceptance order, and zero-padded startup, while separating physical
   acquisition history and publisher integrity from detector guarantees?
3. Are C-001..C-003 and R-003 preserved with correct authority and scope?
   Does PR-002 remain applicable under its stated abstract assumptions?
4. Does the provenance annotation accurately distinguish invented demo
   cadence from the newly approved publisher boundary, without claiming
   physical continuity evidence?
5. Is the VP/VO-004 candidate a legitimate proposed supersession that keeps
   current ledger state open and assigns no false PASS or discharge?
6. Is the AP-002/AD-003/F/CON impact analysis complete, especially the old
   AP authority's protected one-millisecond condition and the need for any
   superseding human authority decision?
7. Are there ambiguities requiring return to engineering authority before a
   corrected AS can become the baseline?

## Scope limits

This review cannot approve CON, implement firmware, amend F-001 or C-002,
change AP authority, accept new AD, discharge a VO, or verify physical
publisher performance. A favorable AS review does not itself perform those
separate actions.

## Requested receipt fields

Record input revision and candidate artifact hashes, disposition, findings
with severity, unresolved obligations, explicit limits of the review, and
the next eligible action. Distinguish structural validation from engineering
acceptance.
