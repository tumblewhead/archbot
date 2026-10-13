# Progressive Concretization: two-toy qualification campaign

**Status:** Planned; no end-to-end qualification has yet been demonstrated.

## Goal

Finish a complete evidence → AS/P/F → AP → provisional selection → CON → DE →
C implementation → independently reviewed verification → final acceptance
cycle with Toy 1. Retarget the **same process, roles, playbooks, task runner
and generic gate infrastructure** to a different Toy 2, then publish a
user-tested retargeting guide with measured human friction.

An LLM's successful completion message, structural checker success, or
synthetic host simulation is **not** final hardware acceptance.

## Separation of concerns

- **Reusable engine:** agent roles, playbooks, task schema and launcher,
  selective traversal, stage-gate primitives, receipts, telemetry.
- **Per-project knowledge:** BKP, AS, P/PO, F, APs, CON, DE, implementation,
  target evidence, scope decisions, VO/AD ledgers, and architecture spine.
- **Per-invocation manifest:** initiating change, operation, role, spine,
  gate, authorized outputs.
- **Domain validators:** custom numerical/physical checks loaded by policy
  when needed; never compiled into a universal evaluation agent.

Current limitations requiring correction before calling the tool generic:
`tools/telemetry.py` assumes AS-001 for reporting; `tools/stage_gate.py`
encodes C-002 and the toy's SRAM buckets; numbered pilot prompts refer to
particular versions. The new task launcher only generalizes **dispatch
input**, not the complete stage gate or telemetry yet.

## Toy 1: 12-bit sliding-window detector

| Gate | Required evidence | Status / exit |
|---|---|---|
| T1-G0 | BKP, AS, F and approved C-002 scope | Established for pilot; inspect current Git |
| T1-G1 | PO, theorem and independent review | PR-002 accepted abstract mathematics |
| T1-G2 | AP-due evidence; provisional commitment | VO-001 now scoped/accepted; **AE-004 pending**; human selection still required |
| T1-G3 | Contract-first interface and resource ownership | Not started |
| T1-G4 | Design elements traceably implement CON and AP | Not started |
| T1-G5 | C reference/target-specific implementation conforms to DE/CON; no silent requirement changes | Not started |
| T1-G6 | Independent implementation and target evidence discharges every due VO; F evaluated with real support | Not started |
| T1-G7 | Final acceptance record with evidence revisions and any unresolved claims explicitly scoped | Not started |

T1-G2 does **not** need completed firmware, linker output or measured WCET.
The 2048-byte detector-attributable SRAM requirement remains binding for
the final implementation. Proposal costs are not measured costs.

If actual target hardware/toolchain is unavailable, finish a host-qualified
reference demonstration, and **leave physical target VOs open**. Never claim
complete target qualification based solely on the host.

## Genericity checkpoints

G-A. One manifest-driven runner can assign Toy 1's current evaluation without
rewriting the agent role or playbook. It must reject missing/malicious paths.

G-B. Refactor context telemetry to accept task-defined spines; test distinct
architecture trees do not contaminate each other's context.

G-C. Refactor stage gates into **common mechanics + domain validators**:
requirement maturity, accepted receipts, VO/AD, protected decisions and
F comparison are common; ADC/SRAM rules are one opt-in validator. All prior
negative gate tests must still pass.

G-D. CON, DE, implementation and verification stages must run through
reusable playbooks, with gated independent reviews and no ad-hoc prompt edits.

G-E. Full Toy 1 can be reproduced from repository HEAD, a task manifest and
bounded run outputs, without relying on chat-memory instructions.

## Toy 2: a fresh numerical root solver

Candidate problem: a bounded scalar Newton–Raphson/root-finding firmware
solver, with explicit domain, derivative/zero handling, convergence/failure
contract, numerical representation, iteration and timing/resource bounds.
The exact AS will be authored independently from new BKP evidence. Do not
copy Toy 1's 12-bit ADC, SRAM budget, or acceptance claims.

Qualification requires:

1. A fresh OKF spine, BKP, AS, F, VOs and candidate APs.
2. The **same** agent role and playbook text as Toy 1.
3. Only new domain knowledge, policies, and domain validators where justified.
4. Proof Scout opportunities (e.g. convergence conditions or impossibility
   of universal convergence without sufficient assumptions).
5. Full CON → DE → implementation → verification chain at the evidence
   level the stated target actually permits.
6. An independent retargeting audit: no leakage of AS-001/C-002 assumptions,
   no silent relaxation and no copied proof authority.

Toy 2 is not an automatic next branch until Toy 1's process is stable.

## Measure human friction

For each toy and every gate, record:

| Metric | Definition |
|---|---|
| human_minutes | Wall-clock human setup, decisions, fixes, and interventions (exclude unattended runtime) |
| interventions | Manual edits/corrections other than creating BKP/AS/F or authorizing protected decisions |
| bespoke_prompts | New task-specific procedural prompts authored |
| engine_edits | Source edits in generic roles/playbooks/runner/gates needed only because of this problem |
| domain_inputs | New problem-specific OKF/policies/validators (expected, not friction by itself) |
| rework_loops | Gate failures followed by another attempt |
| context_bytes | Eligible, selected, and excluded context; identify unknown actual reads |
| token_cost | Input, cached input and output where available |
| elapsed_runtime | Automated execution time by agent/gate |
| trace_coverage | Fraction of due obligations linked to evidence and reviewer decision |
| final_verification | Clear separation of host, simulation, formal proof, and target claims |

Track the human friction as a lightweight, versioned file per gate (not a
huge raw transcript). Avoid inferring actual LLM file reads from selected
context estimates.
The run label is the task manifest ID; record human observations using
`process/examples/qualification-observation-v1.yaml` as a template, then
place the completed observation alongside its versioned review receipt.
Human minutes must be recorded by the human, never guessed by the LLM.

## Acceptance tests for **reusability**

- Toy 2 reaches its evaluation gate with **zero changes to reusable role,
  playbook or generic prompt texts**.
- Toy 2's context projection never loads Toy 1 unless explicitly requested.
- Due VOs without accepted evidence block both toys.
- Deferred obligations require due stage, owner, acceptance criterion,
  assumptions, verification method and escalation.
- A successful tool run cannot silently select an AP, close a VO or accept AD.
- Toy 1 historical artifacts stay immutable when Toy 2 is created.
- A new agent can resume both from Git HEAD and project spines alone.

If a shared engine change proves necessary, record it as a framework defect
and rerun relevant regression tests for **both** toys.

## Next action

Run Toy 1's pending post-VO-001 evaluation through the generic manifest.
Compare its results with the prior numbered AE-004 ticket. The
`process/tasks/TOY1-AE004.yaml` manifest identifies the task; the
`process/playbooks/EVALUATE_AP.md` playbook supplies reusable procedure.

Do not launch **both** numbered AE-004 and manifest-driven AE-004 on the same
unchanged state; use one execution and preserve its receipt.
