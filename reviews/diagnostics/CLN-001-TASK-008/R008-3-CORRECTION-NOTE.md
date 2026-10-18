# CLN-001 Stage 8 focused correction R1

**Disposition basis:** independent `REVIEW-AS-ADDENDUM-008.md/json`,
archived at commit `0d7f83b4e6b9d912562de93ea268eb1575f41f88`,
returned `REVISE_AS_ADDENDUM` with exactly one blocking finding:
`R008-3`, original source sentence S28 in A008-R3.

The exact original `AS-ADDENDUM-008.md` is IMMUTABLE and remains
`PROPOSED_NOT_ACTIVE`. Its original independent review and raw SHA
receipts remain unchanged.

## Authorized bounded correction

New candidate: `AS-ADDENDUM-008-R1.md`, also
`PROPOSED_NOT_ACTIVE`.

The revision changes only (1) the document heading's revision suffix
and (2) the following span in A008-R3.

Original:

> The eventual physical contract must identify reset order and
> acknowledgment at the consumer boundary, and prove that old in-flight
> outputs cannot alias new ones.

R1:

> The eventual physical contract must establish consumer-visible reset
> ordering and unambiguous association between old and new sequences,
> and prove that old in-flight outputs cannot alias new ones. A distinct
> acknowledgment event is optional, not required; any chosen mechanism
> must establish the required observable ordering and association.

The revised requirement is **observable old/new association**. An
explicit acknowledgment is a **possible interface mechanism**, not a
silently authorized or mandatory service. This narrow correction does
not approve ordered markers or any other implementation either.

The focused reviewer must check that the byte-level comparison of
original versus R1 admits *only* the heading and S28 correction; then
judge the corrected source against D001, activated AS, D002, delegated
D003 and the independent R008 findings. Recheck especially reset
ordering, owed old results, consumer indexing and preservation of
unknown feasibility. Do not auto-accept merely because the textual
diff is small.

## Stop and further gate

Independent outcome options:
`READY_FOR_DELEGATED_AS_ADDENDUM_DISPOSITION`,
`REVISE_AS_ADDENDUM`, `UNRESOLVED`.

A favorable **review** enables a separate CLN-001 sponsor-delegate
disposition. It does not activate this candidate itself. A/B/C remain
unselected; H1-H6 and realized F costs UNKNOWN, T002-2..8 OPEN and
R4 deferred. No old Toy 1 artifacts, CON/DE/C or full cleanroom.
