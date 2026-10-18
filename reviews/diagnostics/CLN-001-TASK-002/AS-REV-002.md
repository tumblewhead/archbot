# AS-REV-002 — Revised Architecture Statement, CLN-001

Status: DRAFT; not yet independently reviewed or accepted. Version 002 revises AS-DRAFT-001 additively for TASK-002. AS = (C, R, PS). This is a synthetic, pre-freeze diagnostic, not product qualification. No proof, feasibility finding, architecture selection or verification discharge is asserted.

## Sources and authority

All paths are relative to `package/workspace/`.

| Ref | Identity and path | Role |
| --- | --- | --- |
| S1 | BKP-NEED-001, `projects/CLN-001/knowledge/bkp/problem-origin.md` | Original draft demonstration brief; originating candidates R1–R6, not authenticated real stakeholder requirements. |
| S2 | BKP-ADC-001, `projects/CLN-001/knowledge/bkp/adc.md` | Original synthetic ADC domain/cadence assumptions; no actual hardware measurements. |
| S3 | BKP-TARGET-001, `projects/CLN-001/knowledge/bkp/target.md` | Original synthetic MCU/resource envelope; no qualification evidence. |
| D001 | CLN-001-DIAGNOSTIC-DECISIONS-001, `projects/CLN-001/process/decisions/DECISION-001.yaml` | New sponsor-delegate requirements authority, limited to this synthetic diagnostic; stage REQUIREMENTS_CLARIFICATION_NOT_AS_ACCEPTANCE. |
| V1 | `projects/CLN-001/out/AS-DRAFT-001.md`, `QUESTIONS-001.md`, `BRIEFING-001.md` | First draft, questions and briefing; preserve original candidate IDs and uncertainties, not an accepted baseline. |
| G | `AGENTS.md`, `TASK-002.md`, `framework/agents/architecture-agent.md` | Authoring scope, permitted outputs and stop boundary. |

Decision references below identify numbered decision record D001 and its exact YAML entry, for example `D001 requirements.R3`. Its requirements and Q4/Q6 clarifications are new delegated choices; they were not already present in the BKP. This authoring role has no transferred decision delegation and cannot amend D001 or accept this AS.

TASK-002 and D001 record the prior gate as READY_FOR_HUMAN_QUESTIONS. The local `out/REVIEW-001.json` instead records an UNRESOLVED limited self-review; D001 cites a separate historical review path/commit not examined here. This provenance discrepancy remains UNRESOLVED. The supplied current task authorizes this revision; neither account establishes acceptance, and this author does not reconstruct or certify historical independent review.

## C — Context and subsystem boundary

The original need connects exact recent-window energy to sustained-energy detection and conserving RAM and compute (S1). D001 narrows this stage to an energy-computation primitive serving a potential downstream detection consumer. A complete sustained-energy detector is outside current delivery scope, with R4 retained as an unresolved integration obligation.

The upstream sample publisher owns acquisition timing and supplies values in intended order without omissions under the diagnostic input contract. The numeric subsystem accepts valid logical samples, maintains their specified observable history across accepted events, responds to explicit reset, and supplies exact energy with its logical sample index. The boundary describes responsibilities and observable behavior, not an API or storage design (S1/S2; D001 interface_and_lifecycle_Q4 and delivery_and_exceptions_Q6).

The adopted environment is synthetic: unsigned samples 0 through 4095, nominal arrivals every 1 ms, and a 32-bit Cortex-M-class MCU without an FPU. No specific device, compiler or uninterrupted real delivery is established. Analog accuracy and distortion guarantees remain absent (S2/S3; D001 assumptions.A1–A3).

## R — Requirements and adopted model

Every row retains its originating V1 candidate and BKP evidence and identifies the new authority for its disposition. Adoption here means a delegated diagnostic requirement/model, not acceptance of this AS.

| ID | Revised statement / disposition | Origin and delegated decision |
| --- | --- | --- |
| R1 | ADOPT: after each accepted unsigned sample, provide the exact integer sum of squares over that sample and its 31 preceding accepted samples, using R2 for startup. | V1 R1; S1; D001 requirements.R1, interface_and_lifecycle_Q4. |
| R2 | ADOPT: only absent positions preceding initialization of the current logical sequence contribute zero. Explicit reset starts a new sequence with zero previous history. Initial mathematical energy is zero; publication before the first accepted sample is not required. | V1 R2; S1; D001 requirements.R2, interface_and_lifecycle_Q4. |
| R3 | REVISE_EXPLICITLY: compute one logically new result per accepted sample. Assume nominal 1 ms arrivals; impose no unmeasured hard completion deadline or jitter bound. Record performance evidence separately before claiming real-hardware operation. | V1 R3/A2; S1 “updated every 1 ms” and S2 arrival model; D001 requirements.R3, assumptions.A2. |
| R4 | NARROW_AND_DEFER_WITH_TRACKING: supply exact window energy to a potential detection consumer. No boolean sustained-energy decision, threshold or duration is required at this stage. Their specification and verification remain unresolved before any claim of complete sustained-energy detector functionality. | V1 R4; S1; D001 requirements.R4 and its due_stage. |
| R5 | ADOPT_WITH_DEFINED_BOUNDARY: detector-attributable RAM shall be at most 2048 bytes, including owned persistent state, working scratch and detector-owned call stack. Memory owned exclusively by an upstream publisher is outside the boundary. No numeric compute/power optimization threshold is approved; provide comparisons/measurements when feasible. | V1 R5/A4; S1 qualitative conservation aim and S3 2 KiB envelope; D001 requirements.R5, assumptions.A4. |
| R6 | ADOPT: do not depend on floating-point hardware. No particular integer algorithm, data structure, C API or integer representation is prescribed here; no additional ban on software floating point is inferred. | V1 R6; S1; D001 requirements.R6. |
| A1 | ADOPT_SYNTHETIC_MODEL: each accepted sample is an unsigned integer in [0, 4095]. | V1 A1; S2; D001 assumptions.A1, delivery_and_exceptions_Q6. |
| A2 | ADOPT_AS_NOMINAL_MODEL_ONLY: 1 ms is an illustrative nominal arrival cadence, without proven uninterrupted delivery or real-time execution guarantees. | V1 A2; S2; D001 assumptions.A2, requirements.R3. |
| A3 | ADOPT_SYNTHETIC_MODEL: assume a 32-bit Cortex-M-class MCU without hardware FPU; no specific device or compiler selected. | V1 A3; S3; D001 assumptions.A3. |
| A4 | ADOPT_SYNTHETIC_MODEL_BOUND: 2048-byte detector-attributable RAM ceiling using R5 accounting; no measured footprint or target qualification asserted. | V1 A4; S3; D001 assumptions.A4, requirements.R5. |

### Lifecycle, outputs and exceptional inputs

These are refinements of R1/R2 and A1/A2, not facts retrospectively attributed to S1/S2. Authority is D001 interface_and_lifecycle_Q4 and delivery_and_exceptions_Q6; originating BKP candidates are S1 R1/R2 and S2 A1/A2.

- Initialization has no accepted samples and 32 logical pre-initialization positions contributing zero. An explicit detector reset discards the previous logical history and begins a new sequence.
- Each accepted event supplies one valid sample. Accepted order is the intended publisher order under the diagnostic contract. Its index is logical, not a verified timestamp. One exact energy value and its associated accepted-sample index are supplied for each accepted event.
- Values outside [0, 4095] are invalid. They must not change detector state, advance the accepted-sample index, or be silently converted to zero. The eventual interface must explicitly expose rejection or a precondition violation; the mechanism is not selected here.
- Duplicate, missing and out-of-order delivery are outside the accepted input contract. If the surrounding interface can detect gaps or ordering faults, it must report them rather than present the sequence as fully accepted. No recovery or zero-filling policy is invented. Interfaces without sequence identifiers have no promised ability to detect dropped or duplicated samples.

The nominal delivery assumption does not establish fault detection capability or permit zero padding operational losses. Output association is logical; no periodic wall-clock publication schedule, deadline reference, latency tolerance or missed-deadline policy is added beyond revised R3.

## PS — Problem statement and observable relation

For one initialized or reset sequence, let accepted samples be `x_1, x_2, ...` in accepted order, with `x_i` in [0, 4095]. For specification only, define `x_j = 0` for `j <= 0`. On accepted event `n >= 1`, supply the logical pair

`(n, E_n)`, where `E_n = sum(x_(n-k)^2 for k = 0,...,31)`.

Before the first accepted sample the mathematical energy is `E_0 = 0`; publishing it is optional. Reset starts this relation afresh with no retained prior-sequence contribution. Invalid values do not create an accepted event or alter this relation. The choice of one-based notation specifies logical association without prescribing a stored counter, integer format or interface signature (S1/S2; D001 requirements.R1–R3, interface_and_lifecycle_Q4, delivery_and_exceptions_Q6).

The engineering problem is to realize that exact observable relation and exceptional-input behavior under the adopted synthetic model, within the defined RAM ceiling and without floating-point hardware dependence. R3 requires a result for each accepted event but supplies no hard elapsed-time bound. R4's full detection function remains separately deferred. The mathematical relation specifies behavior only; it supplies no algorithm, data structure, architecture selection, proof or feasibility result.

## Remaining obligations and exit

`DECISION-TRACE-002.md` tracks Q1–Q7, dispositions and future evidence stages. Exactness/startup/reset, exceptional-input behavior, resource accounting, hardware independence and eventual performance all remain unverified. Threshold/duration/detection criteria remain UNRESOLVED and due before whole-detector completion claims. Specific target/toolchain selection and target timing/resource evidence remain UNRESOLVED before qualification claims. No historical Toy 1 VO identifier or discharge is inherited.

Request a distinct later independent review against D001, the original BKP and V1, emphasizing revised R3 and deferred R4. After that review, the human-delegated diagnostic decision maker may issue an AS disposition. This candidate has neither independent review nor acceptance. Stop before Proof Scout, proof, AP/P selection, CON/DE or implementation; future stages require separate authorization.
