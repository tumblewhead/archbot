# TOY1 DE decomposition rationale and coverage v7

## Design rationale

The decomposition follows observable contract boundaries. INGRESS owns the
one accepted operation boundary; STATE owns history and reset invariants;
UPDATE sequences the recurrence; RESULT associates the post-update value
with the completed operation; RESOURCE owns cross-element accounting and
evidence reconciliation. Separating these responsibilities permits
independent correspondence checks while keeping the mathematical state
single-owned.

Alternatives considered: combining ingress and update would obscure the
exactly-once interface check; combining state and sequencing would make the
ring invariant harder to review independently; a persistent result mirror
would duplicate state without being required for the operation-return
contract. The selected conceptual boundaries do not dictate source modules,
physical storage, or concurrency mechanisms.

Assumptions that would invalidate or require revisiting this design include
failure of the publisher's uninterrupted ordered delivery assumption,
addition of a separately concurrent result reader, inability to enforce
quiescent reset in the integration, or inability to satisfy any conditional
resource category ceiling. These are explicitly unverified/deferred where
appropriate; the design does not claim they are true. A changed contract or
authority is required before adding detector loss handling or reader
semantics.

## Composition

`accept(x)` in INGRESS invokes UPDATE once. UPDATE reads/changes STATE once
according to the newest-32 recurrence and passes the resulting accumulator
to RESULT. RESULT returns that operation-associated value to INGRESS's
caller. Reset can occur only under the contract's quiescent lifecycle.
RESOURCE reconciles all simultaneously live memory across these elements,
including relevant nesting, and owns evidence assembly. No execution rate,
deadline, platform topology, or concrete storage layout is assumed.

## Traceability

| Source requirement / interface | Design element(s) | Obligation and evidence state |
|---|---|---|
| C-001 legal `[0,4095]` domain; VO-001 scope | INGRESS, UPDATE | VO-001 discharged only for accepted synthetic domain; no out-of-domain behavior added |
| C-002 2,048 B charged SRAM; VO-002 | RESOURCE, all elements as inventory owners | Open; conditional category limits total 1,792 B plus 256 B reserve; target inventory/fit due at IMPLEMENTATION |
| C-003 integer-only; VO-003 | UPDATE, RESOURCE | Open; source/build evidence due at IMPLEMENTATION |
| R-001 exactly one update per accepted sample; VO-004 | INGRESS, UPDATE | Open; implementation correspondence due; publisher continuity external/unverified; no time deadline |
| R-002 newest 32 accepted samples, zero-padded start; VO-005 | STATE, UPDATE, RESULT | Open; implementation correspondence due |
| R-003 bounded exact result and safe arithmetic; VO-006 | UPDATE, STATE, RESULT | Open; legal-domain enforcement and C expression correspondence due |
| CON-001-v6 input, completion handoff, init/reset lifecycle | INGRESS, STATE, UPDATE, RESULT | Defined at interface; concrete enforcement and handoff implementation remain obligations |
| CON-002-v6 recurrence and integer bounds | STATE, UPDATE | PR-002 supports abstract math only; C/firmware correspondence unproved |
| CON-003-v6 resource and evidence plan | RESOURCE and all elements | Budget ceilings are conditional commitments, not measured fit |
| AD-003 / F-001 | RESOURCE | Accepted debt unchanged; final comparison due before final acceptance |
| Upstream uninterrupted ordered delivery | INGRESS boundary | External assumption remains unverified; no detector continuity mechanism claimed |

## Resource composition plan

Use the v6 category ceilings without redefining them: persistent 256 B,
scratch 128 B, stack 512 B, attributable interrupt context 256 B, shared
256 B, dynamic 128 B, other attributable 256 B, total allocated 1,792 B,
reserve 256 B, cap 2,048 B. Use the proposed per-element subceilings in
DE-AP2-RESOURCE-v7.md, whose columns sum exactly to the category ceilings.
The implementation inventory must
account for every byte once, document object lifetimes and peak overlap,
attribute shared storage conservatively, bound any dynamic peak, and cover
worst-case detector stack and relevant context nesting. No per-element
physical byte measurements are asserted at this stage.

## Correspondence and review focus

Independent review should check the one-to-one operation/result association,
the reset quiescence lifecycle, abstract state/index invariant and modulo
wrap, arithmetic bounds and C promotion hooks, nonoverlapping resource
accounting, and full traceability of open obligations. Structural checks
cannot establish mathematical acceptance beyond PR-002's scope, C safety,
physical fit, publisher continuity, or target behavior.
