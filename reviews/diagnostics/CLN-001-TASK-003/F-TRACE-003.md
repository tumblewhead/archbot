# F-TRACE-003 — Provenance, authority boundary and open obligations

Status: **DRAFT_FOM_NOT_ACCEPTED_OBJECTIVES**; accompanies F-DRAFT-003. No independent review, proof, verification discharge, AP selection, implementation or target fit is claimed.

## Sources and integrity

Read scope: AGENTS.md, TASK.md, inputs/SHA256SUMS, then the seven manifested files in inputs/. No other project, historical solution, Git history, external source, connector or network was used. Source paths mentioned inside supplied artifacts are citations only; their referenced files were not opened. Writes are limited to out/F-DRAFT-003.md and out/F-TRACE-003.md.

`sha256sum -c SHA256SUMS` in inputs/ reported **OK for all seven files**. This verifies correspondence to the supplied manifest, not authenticity, historical reviewer independence, proof validity or target behavior.

| Input | SHA-256 verified against supplied manifest | Use |
| --- | --- | --- |
| DECISION-001.yaml | `1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36` | D001 requirements/assumptions, Q4/Q6 refinements, delegated-authority limits |
| adc.md | `284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7` | Original BKP-ADC-001 synthetic input domain/cadence |
| AS-REV-002.md | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` | Accepted synthetic C/R/PS through activation record; observable relation and boundary |
| DECISION-TRACE-002.md | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` | T002-2 through T002-8, original/delegated decision trace and evidence due stages |
| problem-origin.md | `90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333` | Original BKP-NEED-001 exact-window/startup/detection/resource/no-FPU interests |
| target.md | `c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64` | Original BKP-TARGET-001 generic MCU/2 KiB envelope and absent measurements |
| AS-ACTIVATION-002.yaml | `d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c` | Active accepted synthetic AS status; authority for draft F exploration only; all obligations open |

AGENTS.md and TASK.md are task-scope instructions, not new technical requirements. The manifest supplies no hashes for those instruction files or itself; none is asserted here.

## Accepted baseline versus retained historical status text

AS-REV-002 and its accompanying trace retain draft/pending-review text from their authoring stage. AS-ACTIVATION-002 expressly records activation of that exact AS hash after the delegated conditional disposition, and authorizes CLN-001-FOM-003 as draft exploration. Accordingly this work uses an accepted **synthetic primitive AS**, not an unaccepted baseline and not an accepted F.

The activation record describes the earlier local self-review and archived review as distinct artifacts and records a nonblocking provenance clarification. This author relies on that supplied record, does not independently authenticate its archival checks, and does not reopen historical paths. Diagnostic acceptance does not establish a formal cleanroom, runtime/filesystem isolation, externally authenticated agent independence, product qualification or historical VO discharge. Directory separation alone supplies no runtime/filesystem isolation.

## Explicit authorized-versus-proposed boundary

| Item | Authority and disposition |
| --- | --- |
| H1/H2 exactness, startup/reset | D001 R1/R2, A1, Q4; AS R1/R2/PS. Restated, not amended. |
| H3 per-sample output; nominal timing only | D001 R3/A2/Q4 explicitly revises original BKP timing. No hard WCET/deadline/jitter requirement added. |
| H4 invalid input and applicable fault reporting | D001 Q6, AS lifecycle/exception clauses. No recovery policy or observability guarantee added. |
| H5 at most 2048 bytes with ownership boundary | D001 R5/A4; AS R5. Existing hypothetical ceiling, not an author-proposed limit or evidence of fit. |
| H6 no hardware FPU dependency | D001 R6/A3; AS R6. No representation/algorithm/software-floating-point prohibition added. |
| R4 narrowed and deferred | D001 R4; AS R4; T002-8. Primitive completion cannot imply full detector completion. |
| P1 objective vector, units and reporting definitions | **New proposal:** RAM minimization within the ceiling; compute and energy coordinates; energy normalization and workload/statistic reporting. Conservation aims have source support, but these F definitions are not accepted numeric objectives. Flash remains an unresolved optional resource interest with no limit or active coordinate. |
| P2 symbolic expressions and evidence categories | **New proposal:** peak live accounting expression, parameterized compute/energy models, separation of conditional, host and target evidence. Not a resource calculation or independent proof. |
| P3 uncertainty/gate labels | **New proposal:** evidence-scoped SUPPORTED/CONTRADICTED/UNKNOWN bookkeeping; unknown values never PASS or zero. No accepted gate discharged. |
| P4 comparison procedure | **New proposal:** constraint-first Pareto/partial ordering, compatible model requirements, conservative uncertainty handling, reversible comparison records and separate later selection authority. No weights, ranking or AP selected. |
| P5 missing-information register | **New diagnostic assessment:** current evidence gaps, not new requirements or target findings. |
| P6 F crosswalk | **New proposed organization** of existing T002 labels; no new historical VO identities or approved verification plan. |

P1–P6 cover the author-defined structure and procedural details throughout F-DRAFT-003. D001's sponsor delegation is not transferred to the F author. Neither these outputs nor baseline AS activation make F binding.

## Unresolved choices and evidence needed

| Choice / missing information | Consequence and responsible future boundary |
| --- | --- |
| F definitions, active coordinates and evidence/comparison rules | Distinct reviewer should check source fidelity and usefulness; authorized diagnostic decision maker must accept, revise or reject F. |
| Weights, exchange rates and preferences among incomparable coordinates | Absent. No weighted score or total ordering is permissible in this draft; future authority may resolve choices explicitly. |
| Concrete target/device, compiler/linker/options, libraries/runtime and configurations | UNKNOWN; needed for meaningful target resource, timing and dependency claims at later authorized realization/verification. Generic Cortex-M class does not resolve them. |
| AP identities and candidate-specific analysis | None supplied or created. Future authorized proposals need separate gate/axis evidence; this work provides no favored construction. |
| Ownership, allocation lifetimes, scratch and owned stack/call paths | UNKNOWN; unresolved components preclude a complete RAM value or target ceiling-compliance claim. Shared costs cannot be silently assigned upstream. |
| Workload, runtime statistic, operation costs, instrumentation and uncertainty | UNKNOWN; must be declared before numerical comparison. Worst observed timing is distinct from WCET; nominal cadence is not a timing limit. |
| Energy attribution, baseline, averaging interval and lifecycle/fault workload | UNKNOWN; required before meaningful energy comparison. Compute reduction does not by itself prove energy reduction. |
| Flash relevance, accounting and any limit | UNKNOWN; no flash objective/constraint accepted. Keep outside active F until explicit disposition. |
| Numeric compute/power thresholds or hard timing deadline | None approved. Introducing them would need explicit requirements authority, not metric filling or F-author inference. |
| Full detection threshold, duration, decision output and integration contract | UNKNOWN; T002-8 remains unresolved before whole-detector completion. A future complete-detector boundary needs its own resource/behavior evidence. |

## Open obligation register

All rows are **OPEN / UNRESOLVED**, as recorded in activation. Due stages describe claim boundaries, not present authorization to execute verification.

| Trace item | D001 / AS basis; F mapping | Outstanding evidence and due stage |
| --- | --- | --- |
| T002-2 | R1; H1 | Independent specification comparison for every output on boundary/randomized streams; later authorized functional verification before correctness claims. |
| T002-3 | R2/Q4; H2 | Zero history; first/31st/32nd/33rd accepted cases; reset restart and exclusion of earlier history; later lifecycle verification. |
| T002-4 | R3/Q4; H3 | One output with correct logical index per accepted ordered sample; later interface/functional verification. No fabricated wall-clock deadline. |
| T002-5 | Q6/A1/A2; H4 | Invalid-domain rejection/precondition exposure with state/history/index invariance; reporting of detectable faults and explicit detection limitations; before input-contract compliance claims. |
| T002-6 | R5/R6/A3/A4; H5/H6, RAM/P2 | Exact ownership/resource accounting including persistent state, scratch, owned stack; hardware-independence evidence. Host evidence separately classified; target evidence before target-compliance claims. |
| T002-7 | R3/R5/A2/A3; compute/energy/P2–P4 | Later selected target and reproducible timing/resource characterization, with energy evidence for any energy claim; no current values, deadline or compute/power threshold. Before real-hardware operation/qualification claims. |
| T002-8 | R4; deferred-scope entry | Authorized detection criteria, integration contract and verification before complete sustained-energy detector claims. Primitive exactness does not discharge this item. |

The earlier T002-1 AS review/activation gate is addressed in the supplied activation record; this author does not claim to have performed or independently verified it. A **separate F review and disposition** remains required.

## Reviewer and authority gate before F acceptance

Proposed next gate: a distinct later reviewer checks these pinned inputs and both drafts for D001/AS fidelity, explicit treatment of revised R3 and deferred R4, complete RAM ownership boundary, UNKNOWN handling, non-prescriptive objectives, symbolic/measurement limitations, and T002-2..T002-8 coverage. The authorized diagnostic decision maker then issues an explicit versioned F disposition; any new threshold, objective or tradeoff must be identified and authorized rather than silently attributed to D001.

This is a description of the later gate, not a request to perform it now, a review result, or permission for subsequent proof, AP selection, implementation or qualification. Work stops after the two requested draft files.
