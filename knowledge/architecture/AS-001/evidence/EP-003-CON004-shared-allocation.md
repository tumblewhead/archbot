---
type: Evidence Plan
id: EP-003-CON004-SHARED-ALLOCATION
title: Evidence plan for CON-004 shared allocation blocker
status: draft
sources:
  - id: contract
    resource: /architecture/AS-001/contracts/CON-AP2-003-v4.md
    title: Shared allocation classes and unchanged cap
  - id: ingress
    resource: /architecture/AS-001/contracts/CON-AP2-001-v4.md
    title: Handoff, epoch, publication and watchdog semantics
  - id: envelope
    resource: /architecture/AS-001/proposals/envelopes/AP-002-SRAM-ENVELOPE-001.md
    title: AP-002 categorized SRAM envelope
  - id: vo
    resource: /architecture/AS-001/verification/VO-002.md
    title: Shared allocation verification obligation
relations:
  - kind: addresses
    target: /architecture/AS-001/contracts/CON-AP2-003-v4.md
  - kind: specifies
    target: /architecture/AS-001/verification/VO-002.md
---
# EP-003: CON-004 shared allocation evidence plan

## Disposition

`EVIDENCE_STILL_UNRESOLVED`. The current source set establishes a 128-byte
detector-attributable shared-allocation cap and identifies the required object
classes, but supplies neither a selected handoff capacity nor concrete
representations/widths for session, synchronization, publication and watchdog
state. The platform's atomic/exclusion primitive and reader visibility mechanism
are also unspecified. Consequently a numeric peak allocation or a fit claim
cannot be derived without inventing implementation facts. A proposed byte
budget by category would be a constraint to meet, not evidence that the required
semantics fit.

The blocker is limited to the shared allocation plan. The AP-002 envelope's
other caps and C-002's unique-byte attribution and simultaneous-peak rules remain
unchanged. This plan does not modify the approved architecture, cap, contracts,
or authority, and does not discharge VO-002 or any other VO.

## Minimum evidence package for the contract author / integration owner

Provide one bounded inventory with a row per distinct object and the following
fields: object/owner; count and capacity; representation and byte width; required
alignment and padding; lifetime; maximum concurrent instances; whether storage
is shared or exclusive; and the evidence source for the size. Include at least:

| Required class | Contract requirement to preserve | Missing evidence needed |
|---|---|---|
| Handoff storage | Bounded record(s) containing sample, sequence and session; producer/consumer ownership | Selected capacity, per-record layout, ring/mailbox metadata and peak occupancy bound |
| Continuity state | Producer-owned saturating 64-bit loss epoch; expected sequence and active session/control | Concrete widths, alignment, session representation, and whether fields can share an object |
| Publication | Value, sequence, session and validity/status; coherent reader-visible atomic commit | Concrete publication representation and storage cost of the required reader/exclusion mechanism |
| Watchdog | Receiver-side elapsed-time state, restart/expiry control and independent invalidation | Timer representation/counter width, control state and any extension/interrupt-owned storage |
| Synchronization | One exclusion protocol covering loss decision, handoff, checks, commit and readers | Selected primitive/object footprint, ownership, nesting/ISR constraints and any implementation-owned state |

The inventory must show a **nonoverlapping peak** no greater than 128 bytes.
Shared bytes are charged once under C-002's documented attribution rule;
mutually exclusive lifetimes may share storage only with a justified lifetime
argument. Include padding and every implementation-owned byte, avoid counting
stack bytes again as shared storage, and state positive remaining headroom after
the maximum. If any required object or concurrency contribution is unbounded or
unknown, the total remains unresolved rather than being treated as zero.

## Evidence method, owners, and acceptance checks

1. **Contract author plus target/integration owner (before independent
   REVIEW_CON):** select a bounded handoff organization and representation
   satisfying v4 semantics; cite platform-independent interface sizes only
   where established by an accepted source. For target-specific synchronization
   or timer state not yet available, record explicit symbolic upper bounds and
   an owner/due stage; these cannot be counted as zero or used to claim current
   numeric fit.
2. **Resource accounting reviewer:** independently sum aligned object sizes at
   the simultaneous peak, reconcile ownership/overlap, verify `total <= 128 B`
   and positive headroom, and check no shared bytes were omitted or charged
   twice. A table or deterministic size calculation is sufficient for this
   planning gate; it is not physical layout or implementation verification.
3. **Implementation gate / VO-002 owner:** later verify concrete declarations,
   linker/map placement, alignment/padding, stack and interrupt attribution,
   and actual shared-service ownership. Retain VO-002 until its independent
   acceptance receipt; this plan supplies no such evidence.

Acceptance for clearing CON003-F03 at contract revision requires the complete
bounded numeric inventory above and a credible fit under 128 bytes. If the
integration owner cannot provide finite sizes within that cap, the contract
author must keep the blocker open and route a controlled authority request;
this planner does not authorize a cap change. Independent REVIEW_CON must then
review the complete v4 candidate and this evidence. No DE refinement,
implementation, VO discharge, AD change, or AP/AS/F authority change follows
from this plan.

## Provenance and carried items

This plan was created at Git revision `afeacd890cfd8a4b7267064721056471d634c485`.
Its trigger receipt records originating task `REVISE_CON-d811f94c033e` and
input revision `53ff985b2d3b980f668d9a8bc1c35051d16e02a3`; the receipt is present
in the current checkout and is the evidence being resolved. Manifest inspection
resolved the assigned role, playbook, spine and gate. Structural validation of
this new plan is recorded separately in its review receipt.

Carry VO-002 through VO-006 open and AD-003 accepted with its existing
final-acceptance deadline. The separate need for independent review of v4
semantics (CON003-F01/F02) remains. The only next eligible action is for the
contract/integration owner to supply the missing bounded shared allocation
inventory (or leave CON unresolved and request controlled authority revision if
infeasible), then submit the complete candidate for independent REVIEW_CON.
