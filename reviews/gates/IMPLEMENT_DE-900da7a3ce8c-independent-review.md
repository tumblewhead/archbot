# Independent implementation review: Toy 1

## Scope and disposition

**Disposition: ACCEPT_WITH_CLARIFICATIONS.** The examined C implementation is
consistent with the accepted CON-v6 and DE-v7 behavior for legal samples on
the host C99 environment reviewed. This does not qualify a target build,
establish physical resource fit, or discharge any verification obligation.

The task manifest and authoring receipt pin implementation input revision
`aad9208420dc3962ddc583999b9464e6a9e3a16b`. That revision and the DE trigger
revision `5a20d0ecd957bdfdcabb89fbd6d1446a3da665fc` are ancestors of reviewed
HEAD `4a3546df9ecbe06c21eaf9b9c24fe8e2faa187d6`; the source hashes match the
authoring receipt. This is expected descendant history, not a revision gate
failure. The receipt's report that an inner task-runner failed to initialize
does not conflict with its separately recorded outer checks or this review.

## Findings

- **IR-001 — C recurrence and arithmetic (nonblocking).** Initialization
  zeroes all 32 slots and the accumulator. Each accepted legal sample reads
  the current oldest slot, widens both `uint16_t` operands to `uint32_t`
  before multiplication, replaces exactly that slot, advances modulo 32,
  stores the updated accumulator, and returns it. The `uint8_t` index
  expression is promoted to `int` on the reviewed host, masked by 31, then
  converted back; it remains in `[0,31]`. In C99, the explicit `uint32_t`
  casts ensure the square products use an unsigned type with at least 32 bits.
  From a valid state, the add-before-subtract transient is at most
  `553,377,825`, and the final sum at most `536,608,800`; both fit in
  `uint32_t`. No signed overflow or narrowing issue was identified for this
  host build. The documented legal-domain precondition is not dynamically
  checked, as allowed by the contracts; callers must satisfy it.
- **IR-002 — Behavior test (nonblocking).** The assertion-based host test
  compares each result with a shift-based 32-value reference model and covers
  startup zero padding, reset, maximum samples, eviction after a full maximum
  window, mixed legal values, and repeated ring wraps. I independently built
  and ran it with GCC 16.2.1 using C99, strict warnings as errors, pedantic
  mode, and `-O2`; assertions were enabled (no `NDEBUG`). It passed and
  reported `sizeof(detector_t)=72` host bytes. This is host behavioral
  evidence only.
- **IR-003 — Target and integration evidence open.** No intended target,
  target compiler output, linker map, stack/nesting analysis, physical
  publisher evidence, or integrated memory inventory was examined. The 72
  byte host `sizeof` does not establish the conditional DE subceilings or
  C-002's charged-SRAM fit. No reset-quiescence enforcement or external
  concurrent-reader behavior is claimed by this source.

## Obligation status and next action

VO-002 remains open for complete target/integration charged-SRAM attribution,
including relevant stack, interrupt, overlap, shared, and dynamic allocations
against the approved category ceilings and 2,048-byte total. VO-003 remains
open for target/compiler evidence supporting the no-floating-point-hardware
requirement. VO-004 and VO-005 correspondence is supported for the reviewed
single-call source behavior and host reference-test cases, but end-to-end
accepted-publisher delivery and integration evidence remain outside this
review. VO-006's legal-domain arithmetic and C promotion/overflow behavior
were reviewed for this host C99 build; target compiler and full integration
evidence remain due. This receipt discharges no VO and changes no AS, AP, F,
CON, DE, or AD authority.

**Next eligible action:** collect the intended target/compiler and integration
evidence for VO-002 and VO-003, then submit an implementation evidence review
that preserves the outstanding VO states. Do not represent this host review
as target qualification or final acceptance.
