# AS-DRAFT-001 — Toy 1 Architecture Statement

Status: DRAFT; unreviewed and unaccepted. Role: architecture-agent.
Scope: first Architecture Statement (C, R, PS) from the supplied problem inputs.
No stakeholder approval, feasibility result, or verification discharge is asserted.

## Source and authority index

Paths below are relative to `package/workspace/` (the task workspace).

| Ref | Source | Evidence and authority limitation |
| --- | --- | --- |
| S1 | `projects/CLN-001/knowledge/bkp/problem-origin.md`, BKP-NEED-001 | Metadata says “Stakeholder Decision,” but status is draft and heading says “invented for the demonstration.” Contains explicit brief statements; does not establish actual stakeholder endorsement. |
| S2 | `projects/CLN-001/knowledge/bkp/adc.md`, BKP-ADC-001 | Draft, synthetic ADC model; explicitly a declared assumption rather than a measurement. |
| S3 | `projects/CLN-001/knowledge/bkp/target.md`, BKP-TARGET-001 | Draft, synthetic target and resource envelope; measurements and compiler settings unavailable. |
| G1 | `projects/CLN-001/PROJECT_SPINE.md` | Project is NEW; no accepted authority or approved artifacts. Missing questions require engineering authority. |
| G2 | `AGENTS.md` and `TASK-001.md` | Require C/R/PS, traceability, explicit uncertainty, and a stop after this draft and questions. |
| G3 | `framework/agents/architecture-agent.md` | Architecture agent owns AS, not candidate designs; unsupported constraints remain unresolved; draft exits with review request. |

S1–S3 are the only technical problem inputs used. G1–G3 govern the process and do not supply additional technical requirements. An explicit statement in S1 is recorded below as a **brief requirement candidate**, not as an approved stakeholder requirement. No authenticated stakeholder requirements have been established by these inputs.

## C — Context

The toy problem concerns processing a stream of ADC samples to compute an exact sum of squares over a recent window. The brief connects this computation to detecting sustained energy and conserving RAM and compute (S1). Whether detection itself is a deliverable, and what constitutes detection, remain unresolved.

The input model supplies unsigned integer samples in [0, 4095] with an assumed arrival interval of 1 ms (S2). It supplies no analog accuracy, distortion, or sample loss guarantee. The target model assumes a 32-bit Cortex-M-class MCU without an FPU and a 2 KiB SRAM budget for the detector subsystem (S3). Neither model is evidence about deployed hardware.

The tentative boundary is ADC sample delivery into the detector subsystem and production of the requested computation result. The result interface, ownership of acquisition and scheduling, detector boundary for resource accounting, and any downstream detection behavior require decisions. This boundary is an organizing interpretation for this draft, not an approved allocation.

## R — Requirements and constraints register

| ID | Statement | Classification and source | Open issue |
| --- | --- | --- | --- |
| R1 | Compute the exact sum of squares over the latest 32 ADC samples. | Explicit brief requirement candidate, S1 | Confirm stakeholder authority, output interface, and meaning of latest when delivery is irregular (Q1, Q4, Q6). |
| R2 | Initially, absent history samples count as zero. | Explicit brief requirement candidate, S1 | Confirm startup/reset boundary and first output event (Q4). |
| R3 | Update every 1 ms. | Explicit brief requirement candidate, S1; timing authority UNRESOLVED | Confirm whether adopted, and specify release/cadence/deadline semantics, reference event, and tolerance (Q1, Q2). |
| R4 | Detect sustained energy. | Explicit qualitative brief objective, S1 | Threshold, duration, output, and acceptance criteria absent; deliverable scope unresolved (Q3). |
| R5 | Conserve RAM and compute. | Explicit qualitative brief objective, S1 | No compute limit or optimization criterion supplied; cannot assess satisfaction (Q5). |
| R6 | Do not require floating-point hardware. | Explicit brief requirement candidate, S1 | Does not itself prohibit software floating point or prescribe an implementation; confirm intended restriction (Q5). |
| A1 | Each sample is an unsigned integer in [0, 4095]. | Hypothetical model assumption, S2 | Requires adoption or replacement for the intended device (Q1, Q6). |
| A2 | Samples arrive every 1 ms. | Hypothetical model assumption, S2 | Not an independently authorized timing requirement or a sample loss guarantee (Q2, Q6). |
| A3 | Target is a 32-bit Cortex-M-class MCU with no FPU. | Hypothetical model assumption, S3 | Specific device, execution environment, and toolchain unspecified (Q5). |
| A4 | Detector subsystem has a 2 KiB SRAM budget. | Hypothetical resource constraint, S3 | Requires authority and a defined accounting boundary (Q1, Q5). |

### Timing authority

The phrase “updated every 1 ms” is explicit in S1, but its source is an invented demonstration brief in draft status. Its metadata alone does not establish an authorized stakeholder decision. G1 explicitly records no accepted authority. Thus R3 must remain a timing requirement candidate pending human decision, rather than an approved hard real-time constraint.

S2 separately assumes sample arrivals every 1 ms. Agreement between two draft statements does not establish stakeholder authority or show that an update finishes before the next arrival. Neither source specifies whether 1 ms denotes a result publication interval, processing deadline, sampling period, or some combination. No jitter allowance, latency reference, missed-deadline policy, or timing acceptance method is supplied. This draft neither adopts nor relaxes a hard 1 ms deadline.

## PS — Problem statement

Subject to confirmation of R1–R2 and adoption of A1, define the requested numeric behavior as follows: at a logical sample update, take the latest 32 sample values in sequence, treating history positions preceding initialization as zero, and return the exact mathematical sum of their squares. A concise notation for that behavior is

`E(n) = sum(x(n-k)^2 for k = 0,...,31)`, with unavailable pre-initialization history equal to zero.

Here `n` denotes a logical sample position, not a specified wall-clock instant. This is a specification expression, not an algorithm, storage choice, numeric representation, or proof. Treatment of missing samples after initialization and the mapping from sample arrival to result publication remain undecided.

The engineering problem is to satisfy the confirmed numeric behavior and any authorized timing and resource constraints on the adopted target, while clarifying the intended sustained-energy detection function. R3–R6 and A2–A4 remain recorded with their source status; this statement does not claim they form an approved or complete acceptance baseline.

## Assumptions and uncertainty index

| ID | Uncertainty / limitation | Trace and decision reference |
| --- | --- | --- |
| U1 | No named stakeholder or engineering decision authority, endorsement, or approved baseline is available. | S1–S3, G1; Q1 |
| U2 | Authority and operational meaning of the 1 ms statements are unresolved; no timing feasibility evidence exists. | R3, A2, S3; Q2 |
| U3 | Sustained-energy detection has no operational definition or acceptance criteria. | R4; Q3 |
| U4 | Initialization, resets, output availability, and interface semantics are incomplete. | R1–R2; Q4 |
| U5 | Target specificity, SRAM accounting, compute/power goals, toolchain, and numeric restrictions are incomplete or unmeasured. | R5–R6, A3–A4, S3; Q5 |
| U6 | Delivery irregularities and invalid inputs have no specified handling. No analog or sample loss guarantees may be inferred. | S2, R1, A1–A2; Q6 |
| U7 | Independent review and human disposition have not occurred. No verification obligation is discharged. | G1–G3; Q7 |

No additional hardware guarantees, timing tolerance, thresholds, loss policy, or stakeholder approvals are assumed. This draft uses the sequence interpretation in PS only to express the stated numeric operation; Q4 and Q6 must settle its operational use.

## Draft exit and review request

Request a separate independent review of source fidelity, authority classification, C/R/PS completeness, and the questions in `QUESTIONS-001.md`. Submit the draft and questions for human engineering decisions and disposition after review. The role framework's reference to a parallel Proof Scout does not authorize proof work in this task: the explicit task stop governs. Stop here; no proof, architecture selection, contracts, or implementation is authorized by this draft.
