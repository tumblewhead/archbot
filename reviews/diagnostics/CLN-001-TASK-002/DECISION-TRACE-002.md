# DECISION-TRACE-002 — CLN-001 revision trace

Status: DRAFT authoring trace accompanying AS-REV-002; not an independent review, decision record amendment, AS acceptance or verification discharge.

References S1/S2/S3 and V1 are defined in AS-REV-002. D001 is numbered record `CLN-001-DIAGNOSTIC-DECISIONS-001` at `process/decisions/DECISION-001.yaml`; dotted references below name its exact entries. Paths are relative to the CLN-001 project unless stated otherwise. New authority is the sponsor-delegate's synthetic requirements clarification, not an intrinsic property of the original draft BKP. This author has no authority to make additional decisions.

## Q1–Q7 decision trace

| Question / V1 uncertainty | Originating evidence | Decision, rationale and resulting boundary | Remaining issue / due stage |
| --- | --- | --- | --- |
| Q1 / U1: authority and adoption | S1 draft invented brief; S2/S3 synthetic models; V1 R1–R6/A1–A4 | D001 authority, decision_method, requirements and assumptions: sponsor explicitly delegated CLN-001 diagnostic requirements choices; all dispositions are below. This establishes new project-owned synthetic authority without real stakeholder endorsement or retroactive AS approval. Delegation is not transferred to author/reviewer. | AS acceptance pending independent review and delegated disposition; no real product qualification or cryptographic authentication claimed. |
| Q2 / U2: timing | S1 R3; S2 A2 | D001 requirements.R3 and assumptions.A2 explicitly revise “updated every 1 ms” to one logical result per accepted sample. A nominal arrival period does not define an execution deadline; no hard latency or jitter bound is imposed. | Verify per-event result association at later authorized verification; obtain separate runtime/target evidence before real-hardware operation claims. No invented deadline or missed-deadline policy. |
| Q3 / U3: detection scope | S1 R4 | D001 requirements.R4 narrows this delivery to exact window energy. Threshold, duration and boolean decision are deferred rather than silently considered satisfied. | UNRESOLVED integration obligation before claiming a complete sustained-energy detector. |
| Q4 / U4: lifecycle and output | S1 R1/R2; V1 conditional sequence relation | D001 interface_and_lifecycle_Q4 with requirements.R1/R2: no initial accepted samples; reset begins fresh history; one exact energy and logical index per accepted event. Initial energy is zero with no required pre-first-sample publication. Logical indexing describes association, not verified timestamps or an API. | Verify startup, reset and event/output relation later; concrete interface deferred to an authorized later stage. |
| Q5 / U5: resources, target and numeric restrictions | S1 R5/R6; S3 A3/A4 | D001 requirements.R5/R6 and assumptions.A3/A4 define a hypothetical 2048-byte detector RAM ceiling, including owned persistent state, scratch and owned call stack, excluding exclusively upstream-owned memory. No numeric compute/power threshold or algorithm is approved. No FPU dependency; target remains generic. | Exact accounting/ownership assumptions, eventual measurements and hardware-dependency evidence remain pending later realization/verification. Host evidence must be distinguished from target evidence. |
| Q6 / U6: delivery and invalid inputs | S2 A1/A2; S1 R1/R2 | D001 delivery_and_exceptions_Q6: upstream owns acquisition timing; valid accepted inputs are in intended order without omissions. Invalid domain values leave state unchanged and explicitly expose rejection/precondition violation. Detectable gaps/order faults must be reported. No guarantee of detecting unobservable drops/duplicates, and no loss zero-fill rule. | Verify invalid-input behavior and applicable fault reporting later. Duplicates/missing/out-of-order delivery are outside the accepted contract; recovery remains unspecified. |
| Q7 / U7: review and disposition | V1 draft exit and Q7; current task prior-gate statement | D001 review_and_next_gate_Q7: prior gate is recorded as READY_FOR_HUMAN_QUESTIONS, not acceptance; revision needs a distinct later review against original BKP, D001 and V1, then delegated disposition. | Revised independent review and AS acceptance remain pending. Local review provenance discrepancy below remains UNRESOLVED; author does not supply reviewer independence or approval. |

## Disposition of original requirement/model candidates

These are entries in D001, not newly invented numbered decisions. Each AS-REV-002 register row carries the same dual origin/decision trace.

| V1 ID | Originating BKP | D001 entry / disposition | Rationale and revised scope |
| --- | --- | --- | --- |
| R1 | S1 exact latest-32 sum of squares | requirements.R1: ADOPT; Q4 clarification | Retain exactness; specify accepted-sample ordering and indexed output. |
| R2 | S1 absent startup history is zero | requirements.R2: ADOPT; Q4 clarification | Retain startup padding and apply afresh on reset; never infer operational loss padding. |
| R3 | S1 1 ms updates; S2 cadence | requirements.R3: REVISE_EXPLICITLY; assumptions.A2 | Separate nominal arrivals from unmeasured hard completion timing. Each accepted sample has a logically new result. |
| R4 | S1 sustained-energy objective | requirements.R4: NARROW_AND_DEFER_WITH_TRACKING | Numeric primitive is current scope; full detection is an unresolved later integration obligation. |
| R5 | S1 conserve RAM/compute; S3 2 KiB | requirements.R5: ADOPT_WITH_DEFINED_BOUNDARY | Supply a testable RAM ceiling/ownership boundary; no quantitative compute/power acceptance threshold supplied. |
| R6 | S1 no floating-point hardware requirement | requirements.R6: ADOPT | Retain hardware independence without selecting arithmetic, representation or storage. |
| A1 | S2 unsigned [0, 4095] model | assumptions.A1: ADOPT_SYNTHETIC_MODEL; Q6 clarification | Adopt diagnostic domain; invalid values are rejected explicitly without state change. |
| A2 | S2 arrivals every 1 ms | assumptions.A2: ADOPT_AS_NOMINAL_MODEL_ONLY; requirements.R3 | Illustrative cadence does not establish uninterrupted delivery or execution guarantee. |
| A3 | S3 32-bit Cortex-M-class/no FPU | assumptions.A3: ADOPT_SYNTHETIC_MODEL | Generic hypothetical envelope; device/compiler remain unselected. |
| A4 | S3 detector 2 KiB budget | assumptions.A4: ADOPT_SYNTHETIC_MODEL_BOUND; requirements.R5 | 2048-byte ceiling with explicit accounting, not a measured footprint. |

## Remaining verification and integration obligations

The labels below are local checklist labels for this trace only, not historical VO identities or a newly approved verification plan. All are OPEN / UNRESOLVED; none is discharged. Due stages are evidence/claim boundaries, not authorization to execute later work now.

| Local item | Decision / requirement basis | Evidence still needed | Due stage |
| --- | --- | --- | --- |
| T002-1: revision fidelity and gate | D001 review_and_next_gate_Q7; all revised requirements | Distinct independent review of C/R/PS, dual trace, R3 revision and R4 deferral; subsequent delegated AS disposition. | Next gate, before acceptance or progression. |
| T002-2: exact numeric outputs | D001 requirements.R1 and verification | Compare every output with an independent 32-sample specification on boundary and randomized streams. | Later authorized functional verification, before correctness claims. |
| T002-3: startup/reset | D001 requirements.R2 and verification; Q4 | Check zero-history, first, 31st, 32nd and 33rd accepted-sample cases, plus reset sequence restart and prior-history exclusion. | Later authorized lifecycle/functional verification. |
| T002-4: logical event relation | D001 requirements.R3 and verification; Q4 | Check one result with the correct logical index per accepted ordered sample, without inventing wall-clock bounds. | Later authorized interface/functional verification. |
| T002-5: exceptional input and fault reporting | D001 Q6; A1/A2 | Check invalid input leaves history/index/state unchanged and exposes rejection/precondition violation. Check reporting of faults the chosen surrounding interface can detect; record detection limitations. | Later authorized interface verification, before claiming input-contract compliance. |
| T002-6: RAM and hardware dependency | D001 requirements.R5/R6; A3/A4 | Exact memory accounting/ownership assumptions for persistent state, scratch and owned call stack; evidence of ceiling compliance and no floating-point hardware dependency. Classify host and target evidence separately. | Later authorized realization/verification; target evidence before target-compliance claims. |
| T002-7: performance and target qualification | D001 requirements.R3/R5; A2/A3 | If a concrete target is later selected, report measured runtime separately; comparisons/measurements when feasible. Device/compiler/linker/stack and timing evidence are unavailable now. No compute/power threshold or deadline is approved. | Before real-hardware operation/qualification claims; measurements at the applicable later authorized stage. |
| T002-8: full sustained-energy detection | D001 requirements.R4 and due_stage | Obtain criteria for threshold, duration, decision output and integration, then appropriate verification; do not conflate primitive correctness with detection completion. | Before claiming a complete sustained-energy detector. |

## Provenance limits and stop

TASK-002 and D001 report prior READY_FOR_HUMAN_QUESTIONS review. The available `out/REVIEW-001.json` instead describes an UNRESOLVED self-review with missing independent-review evidence; D001's cited historical review path/commit has not been inspected here. The discrepancy is recorded, not resolved or rewritten. The project spine also remains the original NEW/no-approved-authority snapshot; this author does not edit it or infer acceptance from it. Current authoring authority is TASK-002 using D001's new requirements decisions.

No previous Toy 1 solution, historical proof, architecture, implementation or historical VO is used. Delegate prior-solution familiarity and externally unauthenticated review independence are disclosed by D001 and do not become cleanroom qualifications. No proof, Proof Scout, AP/P selection, CON/DE or implementation has been performed. The next action is a distinct later review, followed by the authorized decision maker's AS disposition; future proof/implementation remain NOT_YET_AUTHORIZED.
