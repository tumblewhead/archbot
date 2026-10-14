# Verification Framework Requirements
## Generic ERS and Runged Verification with Sparse Symbolic Interaction Analysis

**Document ID:** VFR-001  
**Version/status:** v0.1, proposed for process review, 2026-10-14. **Not** an approved product AS or an installed executable process gate.  
**Companion:** [Theory of Verification](THEORY_OF_VERIFICATION.md).  
**Scope:** Reusable Progressive Concretization workflow, not a particular firmware design.  
**Input inspiration:** User-supplied Engineering Requirements Spec v0.10.0 and Verification Plan v0.10.0 (partial-cycle battery-capacity examples). Their numerical thresholds and battery-specific requirements are **not** inherited here.

## 1. System claim

The proposed framework shall derive a verification-facing Engineering Requirements Specification (ERS) from an approved engineering baseline, design an evidence-dependent verification ladder, symbolically screen plausible parameter interactions, execute applicable rungs when separately authorized, and produce independently reviewable evidence with explicit claim scope, reproducibility and residual uncertainty.

It shall **not** convert hypothetical failures, model assumptions, human speculation or implementation accidents into binding product requirements without the established engineering-authority process. It shall not report final acceptance merely because tests passed.

## 2. Authority and applicability

The process requirements below use **shall** for mandatory future framework behavior and **should** for design preferences that require justification when not followed. Because this document is proposed, these are *candidate process requirements* until reviewed and adopted through the normal process authority. Product constraints remain governed by each project's active AS, decisions, CON, DE and VOs.

The framework must preserve the distinction between:
- **Product authority:** AS/CON/DE, approved decisions and due-stage VOs.
- **Verification design:** ERS claims, hypotheses, test choices and diagnostic thresholds.
- **Evidence:** accepted theorem, symbolic proof, empirical result, host test or target measurement, each with its own scope.
- **Human contribution:** question, opinion, operational assumption, observation, and explicit approval as distinct records.

## 3. Functional requirements

| ID | Proposed requirement | Evidence at framework qualification |
|---|---|---|
| VFR-001 | The ERS generator **shall** resolve the project's active AS, accepted CON/DE, proof assumptions, implementation revision, BKP sources, VO/AD state and authority receipts. | Provenance/fixture audit |
| VFR-002 | Every normative derived ERS claim **shall** identify an accepted source authority, exact scope and applicable due stage. | Orphan-claim rejection test |
| VFR-003 | New or conflicting product behavior **shall not** be activated by ERS generation; it shall be reported as a proposed question/change for the authorized stage. | Synthetic invented-requirement canary |
| VFR-004 | The ERS **shall** identify claim, admissible domain, input/output ownership, evidence-access boundary, failure hypothesis, acceptance criterion and explicit non-claims. | ERS schema and reviewer audit |
| VFR-005 | The framework **shall** distinguish implementation-visible inputs, verifier/scorer-only truth, diagnostics and forbidden inputs where applicable. | Leakage test |
| VFR-006 | The verification planner **shall** map each applicable claim and open VO to one or more evidence methods, or document why the method is not applicable or not yet available. | Coverage matrix |
| VFR-007 | Rungs **shall** declare prerequisite evidence and form an acyclic dependency graph; they need not be a rigid total order. | DAG validation and parallel-branch fixture |
| VFR-008 | Each rung **shall** record its claim, failure hypothesis, domain, oracle, evidence method, stopping condition, expected artifacts and next-step rationale. | Rung manifest validation |
| VFR-009 | The framework **shall** support deterministic, boundary, interaction, adversarial, ablation, mutation, population/calibration, platform and synthesis themes as selectable methods, not mandatory fixed stages. | Two-domain applicability test |
| VFR-010 | A rung's receipt **shall** preserve scoped positive/negative findings, counterexamples, unknowns, prerequisite versions and reproducibility references. | Receipt round-trip audit |
| VFR-011 | Later rungs **shall** be able to select experiments using predecessor findings and failure boundaries; a new counterexample **shall** be able to narrow earlier acceptance without deleting historical evidence. | Revision/invalidation test |
| VFR-012 | The framework **shall** provide a sparse pairwise interaction catalog over typed parameters and promote justified higher-order hyperedges. Missing edges shall not imply independence. | Sparse matrix and hyperedge fixture |
| VFR-013 | Parameter definitions **shall** include units/type, legal domain, operating mode, provenance and ownership before interaction evaluation. | Dimensional/type rejection tests |
| VFR-014 | Symbolic screening **shall** support dimension/type, polarity/sign, magnitude/scale, temporal/resource coupling and joint feasibility checks when models permit. | Symbolic canary suite |
| VFR-015 | Symbolic findings **shall** state method, assumptions, source equations, result scope and status (safe, witness, infeasible, inconclusive or invalid model). | Soundness/provenance review |
| VFR-016 | A symbolic safety claim **shall not** be accepted if the relevant implementation correspondence or domain assumptions are missing. | Deliberately mismatched-model canary |
| VFR-017 | Joint sweeps **shall** respect authorized constraints; excluded combinations require cited feasibility evidence, not merely an LLM assertion. | Constrained UART fixture |
| VFR-018 | The planner **shall** support prioritizing sparse interactions by severity, plausibility, sensitivity, coupling, uncertainty, cost and human insight, without presenting heuristic scores as risk proof. | Deterministic priority fixture |
| VFR-019 | The framework **shall** support higher-order escalation and counterexample minimization without requiring exhaustive Cartesian search. | Triple/quadruple interaction fixture |
| VFR-020 | Ablation (feature necessity) and mutation (verifier defect detection) **shall** be reported separately, including classification of equivalent mutants. | Mutation/ablation control tests |
| VFR-021 | A rung **shall not** claim success when it stopped for budget, timeout, missing oracle, insufficient domain coverage or unresolved model assumptions. | Timeout and incomplete-evidence tests |
| VFR-022 | Each completed rung **shall** generate a bounded Engineering Briefing for the human, including learned facts, changed interpretation, uncertainty and consequential questions. | Briefing quality audit |
| VFR-023 | All rung evidence, explanations and human interactions **shall** be attributable to the originating project spine and archiveable with integrity metadata. | Orphan-event and offline archive audit |
| VFR-024 | Independent reviewers **shall** judge the ERS, rung plan and evidence before any scoped acceptance or controlled VO status change. | Unauthorized self-approval canary |
| VFR-025 | A favorable review **shall** explicitly separate host, abstract, statistical and target/integration claims, and retain unmet VOs and non-claims. | Target-vs-host evidence canary |
| VFR-026 | Verification failures **shall** route to the smallest affected stage and preserve source decisions and historical receipts. | Scoped-revision routing fixture |
| VFR-027 | The framework **shall** support project-neutral roles/playbooks and project-supplied domain validators; no Toy 1 identifiers, SRAM buckets or battery thresholds may be embedded in generic gate semantics. | Cleanroom Toy 1 and Toy 2 retargeting |
| VFR-028 | Large raw campaign artifacts **shall** remain retrievable through hashes and manifest references without being forced into ordinary agent context. | Selective-spine retrieval test |
| VFR-029 | Test or proof oracles **shall** identify independence limitations and potential shared-mode defects with the implementation. | Deliberately correlated-oracle canary |
| VFR-030 | The framework **shall** distinguish statistical input covariance from deterministic parameter interactions and from smooth mixed sensitivities. | Matrix semantic/label audit |

## 4. Candidate artifact contracts

### 4.1 Derived ERS record

Required fields: `project_id`, `ers_id`, `source_baseline`, `source_hashes`, `claim_id`, `authority_ref`, `claim_text`, `domain`, `assumptions`, `evidence_access`, `failure_hypotheses`, `dangerous_failure`, `due_stage`, `acceptance`, `non_claims`, `status`, `review_receipt`. A schema can use linked records rather than duplicating long content.

### 4.2 Verification rung record

Required fields: `rung_id`, `claim_ids`, `theme`, `prerequisite_receipts`, `failure_hypothesis`, `parameter_domain`, `oracle`, `method`, `resource_budget`, `stopping_rule`, `artifacts`, `briefing_ref`, `outcome`, `limitations`, `next_rung_reason`, `review_receipt`.

### 4.3 Sparse interaction edge/hyperedge record

Required fields: `edge_id`, `parameter_ids`, `parameter_versions`, `joint_admissibility`, `coupling_kind`, `symbolic_model_ref`, `analysis_method`, `assumptions`, `symbolic_status`, `witness_or_bound`, `priority_rationale`, `experiment_refs`, `source_refs`. An `UNKNOWN` interaction is distinct from `SYMBOLICALLY_EXCLUDED`.

### 4.4 Evidence and archive record

Required fields: `project_id`, `claim_id`, `rung_id`, `source_revision`, `tool_versions`, `commands_actually_run`, `input_manifest`, `output_manifest`, `hashes`, `oracle_provenance`, `counterexample_refs`, `limitations`, `independent_review`, `open_VOs`. Private content can be excluded from public exports only with a visible redaction/completeness declaration.

These field lists are **proposed schemas**, not yet implemented interfaces.

## 5. Symbolic interaction acceptance tests

| Test | Expected conclusion |
|---|---|
| Add volts to amperes without an authorized conversion | MODEL_INVALID / unit mismatch |
| Opposite-polarity terms cancel only under a stated common-mode condition | Conditional cancellation, not universal safety |
| Unsigned square/accumulator magnitude crosses width bound | SAT_COUNTEREXAMPLE or bounded overflow witness |
| Legal maximum UART message length and legal maximum arrival rate overload a bounded consumer jointly | Joint failure, even if isolated sweeps pass |
| Large/fast UART combination prohibited by an approved, verified protocol envelope | INFEASIBLE_COMBINATION within that envelope |
| Bursty traffic and service pause jointly exceed a buffer despite safe average throughput | Temporal higher-order failure |
| Smooth mixed derivative is small but a hard threshold exists | Do not infer safety from local derivatives |
| SMT/interval model is incomplete or times out | INCONCLUSIVE, not PASS |
| Symbolic proof valid but target C violates representation assumptions | Correspondence failure; proof does not discharge target claim |

These are framework qualification fixtures. The UART numerical values are illustrative, not a newly approved operating envelope.

## 6. Gate definitions and independent review

| Proposed gate | Input | Output / condition |
|---|---|---|
| ERS_AUTHOR | Reviewed implementation and active authority | Draft ERS, source map, open questions |
| ERS_REVIEW | Draft ERS + accepted source hashes | ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE or UNRESOLVED |
| LADDER_AUTHOR | Accepted ERS and open VOs | Rung DAG, interaction graph, symbolic screening plan, evidence budget |
| LADDER_REVIEW | Proposed rungs and oracles | Independent plan adequacy, coverage and feasibility judgment |
| RUNG_EXECUTE | Accepted rung plan and prerequisites | Reproducible evidence, counterexamples and Engineering Briefing |
| RUNG_REVIEW | Evidence and exact inputs | Scoped independent outcome and next action |
| CLAIM_SYNTHESIS | Reviewed rung receipts + authoritative VOs | Claim-by-claim evidence summary, unresolved/non-claims and proposed VO actions |

No authoring gate self-approves. A review outcome does not discharge VOs automatically; existing protected authority still governs.

## 7. Traceability and qualification strategy

| Requirement group | First qualification evidence |
|---|---|
| VFR-001..006 | Source-authority and ERS projection fixtures |
| VFR-007..011 | Rung dependency DAG, scoped supersession and evidence-inheritance tests |
| VFR-012..019, VFR-030 | Sparse interaction, symbolic UART and Toy 1 arithmetic canaries |
| VFR-020..021, VFR-029 | Mutant/ablation and unreliable-oracle fixtures |
| VFR-022..028 | Engineering Briefing, project archive, independent gate and retargeting tests |

**Toy 1** should exercise legal newest-32 arithmetic, reset, index wrap, C promotion, and target resource obligations without inventing sample timing or publisher-loss requirements. The current independent C review accepts host behavior only and leaves VO-002 through VO-006 open. **Toy 2** should challenge the same generic machinery with a different algorithm and interaction structure. Cleanroom replays measure the friction of retargeting, process-specific code changes, agent/human attention and evidence quality.

## 8. Explicit non-requirements and non-claims

This proposed framework document does not:
- change Toy 1 AS, accepted AP, F, CON, DE or current VO states;
- require every project to run Monte Carlo, calibration or all possible pairwise combinations;
- assert that symbolic safety automatically implies hardware safety;
- require a full interactive UI before ERS or ladder authoring;
- certify any UART design, battery estimator or embedded target;
- authorize source changes or installation of new workflow operations in the current documentation-only milestone.

## 9. Planned implementation sequence (after review of these documents)

1. Approve/refine the generic theory and candidate requirements.
2. Implement `DERIVE_ERS` and independent `REVIEW_ERS`, including source-authority validation.
3. Implement `DESIGN_VERIFICATION_LADDER` and independent `REVIEW_VERIFICATION_LADDER`, including sparse symbolic interaction schemas and a rung DAG.
4. Implement `EXECUTE_VERIFICATION_LADDER` and `REVIEW_VERIFICATION_RUNG` with bounded evidence receipts, replay and Engineering Briefings.
5. Test on Toy 1, retain target VOs honestly, then perform cleanroom genericity and Toy 2 transfer experiments.

**Open design questions:** What symbolic backends are available locally? Which target/compiler and integration boundaries are authorized? What evidence budgets and human-question escalation policy should be adopted? These are inputs to future design, not values to invent here.
