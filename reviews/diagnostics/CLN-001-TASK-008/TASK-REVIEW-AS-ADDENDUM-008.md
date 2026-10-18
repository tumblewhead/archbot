# CLN-001 TASK-REVIEW-AS-ADDENDUM-008

**Role:** Independent architecture/requirements source reviewer. You are
not the D003 delegate/author, Stage-7 reviewer or AP selector.
This is a synthetic pre-freeze diagnostic, not formal cleanroom proof.

Read ONLY AGENTS.md, TASK.md, inputs/SHA256SUMS and the supplied
allowlisted inputs. Do not access old solved Toy 1 AP/CON/DE/C, other
workspaces, Git history, network, connected apps or hidden evaluator.

The new `AS-ADDENDUM-008.md` is NOT EFFECTIVE. The recorded D003
disposition authorizes bounded source review; it does not approve RI,
a snapshot/index service, a physical protocol or an AP. Review
additive A008-R1/R2/R3 individually against original BKP,
D001 Q4/Q6, activated AS, D002 and the full independent Stage-7
findings. Do not silently repair or add assumptions.

Required independent challenges:

1. Identify the ACTUAL index consumer and whether rank decoding is
   exact with *only its actual state*, through invalid inputs,
   consumer restart, reset and arbitrary supported event count.
   Distinguish faithful representation clarification from materially
   weaker observer-only indexing and a new requirement.
2. Review result debt, numerical state commit and publication.
   Test accept/lose/fault-report/retry, finite queue under stalls,
   and invalid attempt. Does A008-R2 add failure guarantees not
   authorized by D001? Is clarification versus amendment explicit?
3. Reset linearization: test delayed old `(1,E)`, new `(1,E)`,
   generation-tag reuse, consumer restart without detector reset.
   Does A008-R3 preserve obligations without assuming an unavailable
   synchronization/acknowledgment service or impossible delivery?
4. Check numeric PS/R1-R6/A1-A4, nominal-not-hard 1 ms,
   no extra power/compute threshold, 2048 owned RAM, deferred R4,
   all open T002-2..8, conditional T1/T2 and no AP selection.
5. Independently classify every new sentence as (a) already accepted
   behavior, (b) necessary interpretation requiring addendum,
   (c) material new requirement/restriction needing new delegated
   amendment, or (d) mechanism/evidence question for later AP work.
   Point out any hidden assumption or unresolved contradiction.
6. Record source hashes, actual test/probe evidence and independence
   limits. Do not claim physical implementation, OS isolation,
   hardware qualification or review of inaccessible historical files.

Write ONLY
`out/REVIEW-AS-ADDENDUM-008.md` and
`out/REVIEW-AS-ADDENDUM-008.json`.

JSON must contain `review_id: CLN-001-REVIEW-AS-ADDENDUM-008`,
`disposition` one of `READY_FOR_DELEGATED_AS_ADDENDUM_DISPOSITION`,
`REVISE_AS_ADDENDUM`, `UNRESOLVED`; clause findings and AS impact,
source/hash checks, `AS_addendum_activated:false`,
`RI_approved:false`, `AP_selected:false`,
`target_verified:false`, `product_verified:false`,
`formal_cleanroom_qualified:false`, `vo_discharged:[]`.

**STOP after both outputs.** Do not approve/activate the addendum,
make RI/RN/C-HIST effective, select AP, author contracts or begin DE/C.
