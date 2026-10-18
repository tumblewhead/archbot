# CLN-001 TASK-AP-006: fresh competing architectural proposals

**Role:** proposal-agent; author, NOT reviewer or engineering decision maker.
**Status:** Authorized AP **draft generation only**. No AP selection.
**Project:** synthetic CLN-001 diagnostic energy-computation primitive.
**Inputs:** ONLY `inputs/` and `TASK.md` and `AGENTS.md`, no old solved Toy 1 data, code, old F-001 or AP candidates.

## Authority

Accepted synthetic AS-REV-002 via AS-ACTIVATION-002.
D001 synthetic requirements, accepted F with H1-H6 and
(RAM_peak,compute_effort,device_energy_consumption) as compatible
Pareto preferences, and D002 policy that requires information
and logical-index refinement disclosures. T1 accepted for future
numeric outputs; conditional T2's 372-bit complete-state minimum
applies ONLY at a fully closed no-replay information boundary.
No physical device, compiler, runtime, local RAM fit, performance,
service availability or exact index implementation was proven.

## Author's job

1. Independently invent **at least two, preferably three,
   structurally distinct AP candidates** that can be traced to the
   same mathematical observable relation and D001 input contract.
   Consider both detector-local complete history and external
   publisher-history services when useful, but do NOT assume an
   external service is already available. Do NOT import the
   historic Toy 1 design or preselect a known winner. Avoid
   implementation source/C API or fully specified DE/CON.
2. For each AP, define:
   - data/control boundary and which component retains or reads
     history, including the latest-31 T1 information needs;
   - data acceptance, startup/reset, rejection without state
     advancement, ordered delivery, potential loss/fault reporting;
   - how the exact logical (n,E_n) output is refined into a
     physical interface **without** silently imposing an epoch
     bound, counter wrap or pre-existing external index service;
   - explicit external contracts, conditional dependencies,
     potential failure handling and assumptions needing new
     sponsor-delegate authority before a concrete commitment;
   - memory ownership: detector persistent + scratch + owned
     stack under 2048 bytes, outside exclusively upstream-owned
     resources separately accounted; no assumed fit;
   - no hardware FPU dependency and precise arithmetic/range/
     overflow risks, but no asserted target build evidence;
   - where T1 and T2 apply and where history replay/index
     externalities break their application;
   - outstanding local obligations T002-2..8 and R4 deferred
     whole-detector detection.
3. Produce a **separate symbolic F worksheet** for all candidates:
   H1..H6 qualification evidence level, RAM_peak in bytes
   (expressions/UNKNOWN), compute_effort typed operation expressions
   (not fabricated MCU cycles), attributable electrical device
   energy with UNKNOWN coefficients/attribution, flash inactive.
   No measured values, hard WCET, scalar weights, hard power target
   or Pareto winner may be fabricated.
4. Compare tradeoffs and counterexamples, clearly distinguishing
   conditional cost results from claims of admissibility.
   Mark incompatible cost domains as incomparable. Report no
   evidence of compliance from the sheer existence of an AP.
   Prefer reversibility when information or index interfaces
   remain unresolved.
5. Explicitly identify any **blocking contract ambiguities**
   needing a new D003 or additive AS clarification; do not fix
   them by silently narrowing the accepted source. Make a
   recommendation about which APs deserve later independent
   feasibility analysis, not which one is officially selected.
6. Provide a source-by-source trace and evidence-limit receipt.
   Role `PROPOSAL_AGENT_ROLE.md` is process guidance only.

## Output only

- `out/AP-CANDIDATES-006.md`: at least two distinct AP drafts,
  explicitly labeled AP_CANDIDATE_NOT_SELECTED.
- `out/AP-COMPARISON-006.md`: H1..H6/F axes,
  symbolic tradeoffs, assumptions, counterexamples, unknowns
  and T002/PD/D002 mapping.
- `out/AP-BRIEFING-006.md`: exact sources/hashes read,
  outputs, missing authority/evidence and next review gate.

**Stop before selecting an AP, modifying AS/D001/D002/F,
authoring contracts, DE, C or proof acceptance.**
This is a source-bounded pre-freeze diagnostic, not a formal
cleanroom or hardware qualification.
