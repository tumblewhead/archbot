# CLN-001 focused independent review: AS-ADDENDUM-008-R1

**Independent reviewer**, not author/delegate or the original Stage-8
reviewer. Source-quality and authority scope only, pre-freeze synthetic
diagnostic. Original Stage-8 independent review returned
`REVISE_AS_ADDENDUM`, with sole blocking `R008-3` (S28 mandatory
reset-acknowledgment). No additive AS has been activated.

Read AGENTS.md, TASK.md and inputs/SHA256SUMS and the supplied inputs
only. Do not consult other workspaces, solved Toy 1 source, Git history,
connected apps, network or hidden evaluator.

Required checks:

1. Independently compare original `AS-ADDENDUM-008.md` with
   `AS-ADDENDUM-008-R1.md`. Assert that only title suffix and exact S28
   replacement described in `R008-3-CORRECTION-NOTE.md` differ.
   Disposition cannot be favorable if unrelated changes are present.
2. Determine whether R1 **removes the unapproved mandatory
   acknowledgment requirement**, while still requiring observable reset
   ordering, correct old/new sequence association and no stale result
   aliasing. A reset marker or acknowledgment remains a *candidate*
   mechanism, not one supplied by the accepted AS.
3. Check exact accepted-event index is consumer-decodable, not an
   omniscient observer rank; invalid attempts do not advance rank;
   old accepted results remain owed without new universal delivery
   or crash-recovery guarantees. Check no forced reset, finite epoch,
   unapproved flow control, retained-state oracle, or physical
   protocol is invented.
4. Recheck against original synthetic BKP, D001, active AS,
   AS-ACTIVATION-002, accepted D002, guarded delegated D003 and
   original Stage-8 review. Apply R008-1/R008-2/R008-4/5/6
   appropriately, but do NOT expand into an unbounded new audit.
   Distinguish source-level conformity from actual physical
   feasibility and separate human/agent authority.
5. Keep H1-H6 UNKNOWN for realized A/B/C; preserve adopted
   `RAM_peak`, `compute_effort`, `device_energy_consumption`,
   T1/T2 scope, T002-2..8 OPEN and R4 deferred.
6. Report actual source checks/hashes and finite probes, if any,
   honestly. A favorable verdict does not activate the R1 AS
   addendum, approve RI/RN/C-HIST, select AP, start CON/DE/C or
   discharge an obligation.

Write ONLY
`out/REVIEW-AS-ADDENDUM-008-R1.md` and
`out/REVIEW-AS-ADDENDUM-008-R1.json`.

JSON must include `review_id: CLN-001-REVIEW-AS-ADDENDUM-008-R1`,
`disposition` one of
`READY_FOR_DELEGATED_AS_ADDENDUM_DISPOSITION`,
`REVISE_AS_ADDENDUM`, `UNRESOLVED`;
`R008_3_resolved`, exact-diff check, source digests,
residual findings, and `AS_addendum_activated:false`,
`RI_approved:false`, `AP_selected:false`,
`target_verified:false`, `product_verified:false`,
`formal_cleanroom_qualified:false`, `vo_discharged:[]`.

**STOP** after these original reviewer outputs exist.
