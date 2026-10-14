# REVISE_CON: Correct contracts after independent review

**Reusable operation:** `REVISE_CON`  
**Role:** `contract-agent`  
**Trigger:** A separately recorded, independent contract-review receipt with `REVISE`.

## Responsibilities

1. Read the task's architecture spine, approved AP selection, original contract
   set, independent review receipt, proof assumptions, VO/AD ledgers and applicable
   resource contract. Ensure the review references the relevant original revision.
   Where an active baseline exists, use its **reviewed effective AS/VP
   relationships and active VO ledger**; older contract and resource
   documents provide provenance, not authority for superseded conditions.
2. Address **every material finding by ID** with an explicit change, a supported
   justification, or a clearly labelled unresolved blocker. For rejected
   interpretations, preserve a counterexample. Do not declare the reviewer mistaken
   without a concrete argument.
3. Create **new versioned contract concepts**, preserving all earlier contracts
   byte-for-byte as historical evidence. Use explicit version relations or
   a versioned contract spine to identify the active candidate without deleting
   historical edges.
4. Treat interface semantics as first-class obligations. An upstream
   publisher's approved environmental promise may remain an explicit,
   unverified **external precondition**. Do not translate it into
   downstream detection, reconstruction, watchdogs, timestamps or fault
   machinery without separate authority. Define sufficient input/output
   completion, initialization and legal-domain semantics for independent
   implementation. Do not invent error handling for values outside an
   interface's approved input domain.
5. Enumerate every owned state, control and output field against the approved
   resource accounting boundary. Record byte widths, alignment assumptions,
   ownership, lifetimes, overlap and detector-attributable allocations.
   At a contract/AP budget gate, supply credible **category ceilings,
   positive reserve and enforceable conditional assumptions**, not
   invented measurements or mandatory platform topology. Do not copy
   an old budget's ISR/task/heap assumptions into a new contract
   without establishing their applicability. Explicitly distinguish
   charged SRAM from F's state-SRAM metric and implementation-stage
   stack/linker measurements. If the approved cap cannot support
   required state, propose a controlled resource/architecture revision;
   **do not enlarge the cap silently**.
6. Update contract coverage and DE responsibility placeholders only where the
   corrected external obligations change, retaining open VOs and accepted AD.
7. Request an independent review of the new contract version. Provide an
   itemized mapping: `finding_id -> correction -> evidence -> status`.
8. Run structural and applicable checks and record what was inspected and
   which obligations remain open.

## Exit

- `CONTRACTS_READY_FOR_INDEPENDENT_REVIEW` if all blocking review findings are
  addressed with independently reviewable contracts, or
- `CONTRACTS_UNRESOLVED` with the minimum unresolved decision/evidence needed.

This playbook **does not specify how to repair any particular detector,
solver, driver or scheduler**. All problem-specific counterexamples and limits
come from the selected review receipt and architecture spine.

A Contract Agent cannot approve its own revision, implement firmware, discharge
VOs, accept Architectural Debt, or change an approved AS/F/AP. DE internals
remain blocked until an accepted independent contract review.
