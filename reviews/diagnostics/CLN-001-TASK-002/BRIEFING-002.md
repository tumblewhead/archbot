# BRIEFING-002 — Revised Architecture Statement handoff

Status: TASK-002 authoring complete. AS-REV-002 remains DRAFT, not yet independently reviewed or accepted. Synthetic CLN-001 diagnostic only.

## Produced artifacts

Paths in this briefing are relative to `package/workspace/`.

- `projects/CLN-001/out/AS-REV-002.md`: versioned C/R/PS, coherent R1–R6/A1–A4 register, adopted synthetic model, logical input/output/reset semantics, exceptional-input behavior and dual BKP/D001 trace.
- `projects/CLN-001/out/DECISION-TRACE-002.md`: Q1–Q7 dispositions, original requirement/model dispositions, rationale, subsystem boundary, provenance limitations and open verification/integration obligations with due stages.
- `projects/CLN-001/out/BRIEFING-002.md`: this source identity and handoff record.

Only these three permitted output files were written. Earlier draft, questions, briefing, BKP, decision record, review receipt and project authority files were left unchanged.

## Source identities

SHA-256 values identify bytes read in this authoring workspace; they are not signatures, proof of historical authorship or independent review receipts.

| Identity | Source path | SHA-256 |
| --- | --- | --- |
| BKP-NEED-001 | `projects/CLN-001/knowledge/bkp/problem-origin.md` | `90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333` |
| BKP-ADC-001 | `projects/CLN-001/knowledge/bkp/adc.md` | `284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7` |
| BKP-TARGET-001 | `projects/CLN-001/knowledge/bkp/target.md` | `c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64` |
| V1 statement | `projects/CLN-001/out/AS-DRAFT-001.md` | `e231a55be07631c3c089434ec7502bc9cad833340ef5cd97813d5852372aa9e3` |
| V1 questions | `projects/CLN-001/out/QUESTIONS-001.md` | `6d30b661f3e1542a779ef2a9fdad3eafc8aa6d87cb7e3290f8ac7624162c4fce` |
| V1 briefing | `projects/CLN-001/out/BRIEFING-001.md` | `8f30a6f672cc6883fe74cc246bcffa9935ce258a4c639ae834c9b9eda32402de` |
| D001: CLN-001-DIAGNOSTIC-DECISIONS-001 | `projects/CLN-001/process/decisions/DECISION-001.yaml` | `1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36` |
| Authoring instructions | `AGENTS.md` | `15a7a2c8256b492d73199741fd9a8a92f53a1d375d9b5e0202ce7fd0eba17c4a` |
| Current task | `TASK-002.md` | `246918b8d2e9acf29d54b5cde4ed78fe15220cdb04ae818d22d8471d528eba46` |
| Role | `framework/agents/architecture-agent.md` | `eaff05e88bc80edc89ac70a70b57a45baf1041ca413760a09a25196882c732fe` |

Additional context examined: `TASK-001.md`, `projects/CLN-001/PROJECT_SPINE.md` and local `projects/CLN-001/out/REVIEW-001.json`. No prior Toy 1 solution or historical design/proof/implementation was consulted. No external technical sources were used.

## Changes and authority

D001 is new sponsor-delegate synthetic requirements authority; it is not an approval hidden in the old BKP and does not accept either AS version. The original brief and hardware sources remain draft demonstration/model inputs. The first draft remains an earlier candidate, not an accepted engineering baseline. This author has no transferred requirements-decision authority.

R1/R2 retain exact latest-32 accepted-sample energy and startup zeros. D001 clarifies explicit reset, ordered accepted events and one exact energy/index pair per accepted sample. Invalid domain values must leave detector state unchanged and explicitly expose rejection/precondition violation. Upstream owns acquisition timing; delivery irregularities are outside the accepted contract, with detectable faults reported and no invented operational zero filling.

R3 explicitly revises the old update wording to one logically new result per accepted sample. Nominal 1 ms arrival cadence does not establish a hard completion deadline, jitter bound or real-time feasibility. R4 separately defers sustained-energy decisions, thresholds and duration; that integration obligation is due before whole-detector completion claims.

R5/A4 adopt the 2048-byte detector-attributable RAM ceiling including owned persistent state, scratch and owned call stack, excluding memory owned exclusively upstream. A ceiling is not measured use or target qualification. The no-FPU synthetic MCU model and R6 hardware independence remain adopted without prescribing an algorithm, storage, C API or integer representation. No numeric compute/power optimization threshold is approved.

## Limitations and unresolved evidence

The supplied task and D001 record the prior review gate as READY_FOR_HUMAN_QUESTIONS. The local REVIEW-001.json instead records an UNRESOLVED limited self-review; the distinct historical review path/commit cited by D001 was not examined. This provenance discrepancy remains UNRESOLVED and is disclosed in both new companion artifacts. No historical review is reconstructed, no authority file is corrected, and neither prior-review account means AS acceptance. TASK-002 explicitly authorizes the present revision.

No independent review of version 002 has occurred. No functional test, proof, timing, RAM, WCET, cycle, compiler, linker, stack or power measurement has been performed, and no feasibility, cleanroom qualification or product verification is claimed. Exactness, lifecycle/interface compliance, invalid-input handling, resource compliance and hardware independence remain unverified. Detection criteria and concrete target/toolchain qualification remain UNRESOLVED at their stated future stages. No historical VO identity or discharge is inherited; local trace checklist labels only record pending work.

Authoring checks confirmed the three expected artifacts exist and cover C/R/PS, all Q1–Q7 and R1–R6/A1–A4, dual source/decision trace, deferred R4, revised R3 and future evidence boundaries. Those completeness checks are not independent review or verification of a realization.

## Next gate and stop

A distinct later reviewer must compare AS-REV-002 and its trace with D001, original BKP and the first draft, especially the R3 revision and R4 deferral, and assess the disclosed provenance limitation. Only after that review may the human-delegated diagnostic decision maker issue an AS disposition. Review scheduling/identity and acceptance remain pending; this author does not confer either.

Stopped after the three authorized documents. No Proof Scout, proof, architectural selection/AP/P, CON/DE or implementation was performed. Future proof and implementation remain NOT_YET_AUTHORIZED.
