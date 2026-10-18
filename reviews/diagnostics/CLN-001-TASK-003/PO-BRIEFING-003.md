# CLN-001 proof scout briefing 003

Classification: **DRAFT_OPPORTUNITIES_NOT_PROOFS**. Authorized discovery only; three UNPROVEN candidates, no proof or downstream role performed.

## Examined material and provenance

Read `AGENTS.md`, `TASK.md` and `inputs/SHA256SUMS`, then only the seven supplied input documents below. No other project, historical Git content, old Toy 1 solution, evaluator, connector, network or external source was consulted. All seven files matched the supplied SHA-256 manifest using `sha256sum -c SHA256SUMS`. This establishes local byte consistency with that manifest, not external authenticity or independent review.

| Examined input | SHA-256 | Use |
| --- | --- | --- |
| `inputs/DECISION-001.yaml` | `1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36` | D001 synthetic requirements, authority and scope |
| `inputs/adc.md` | `284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7` | S2 domain/cadence assumptions |
| `inputs/AS-REV-002.md` | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` | AS contract, lifecycle and resource boundary |
| `inputs/DECISION-TRACE-002.md` | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` | Q1–Q7 trace and T002 obligations |
| `inputs/problem-origin.md` | `90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333` | S1 original invented need |
| `inputs/target.md` | `c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64` | S3 hypothetical MCU/resource envelope |
| `inputs/AS-ACTIVATION-002.yaml` | `d7bdf51424b25e768f1438d382f499f28ecead706208ece37d0737c7e8fafb1c` | ACT accepted baseline and scouting authorization |

ACT is additive evidence of synthetic activation despite older pending-acceptance text in AS/TRACE/D001. Its references to archived review/disposition artifacts and its recorded remote verification were read as statements in the supplied record; those artifacts and remote history were not accessed or independently verified. ACT's nonblocking provenance clarification is preserved. D001 discloses delegate prior-solution familiarity; this fresh scout did not consult that solution. Neither agent independence nor physical/runtime isolation is externally authenticated. This is a cooperative pre-freeze diagnostic, not formal cleanroom qualification.

## Outputs

Only the two named output files were written:

- `out/PO-OPPORTUNITIES-003.md`: precise indexed latest-32 contract, invalid/reset semantics, granted constraints and three UNPROVEN propositions with hypotheses, counterexample attempts, value, proof routes, missing facts, independent evidence needs and clause trace.
- `out/PO-BRIEFING-003.md`: this provenance record, output inventory, open questions and next-task recommendation.

The candidates are: PO-003-1, integer output/intermediate bounds; PO-003-2, equivalence and information bounds for future numeric outputs using the latest 31 accepted values; PO-003-3, conditional finite-state impossibility for unbounded internally generated exact indices. They do not prescribe an algorithm, data structure, arithmetic representation, candidate AP/F or implementation. No Mermaid diagram is included because the equations and explicit boundary definitions state the relationships directly.

## Open questions and obligations

1. What index/association mechanism will a later interface use, and is epoch length bounded? Neither a lifetime limit nor counter wrapping is currently authorized. PO-003-3 applies only under its additional closed finite-state model.
2. May a candidate consult publisher history or externally retained outputs? PO-003-2's lower bound requires its explicit no-replay model; any external storage/ownership must be accounted for honestly.
3. What language arithmetic, evaluation order and type widths will a later realization use? Mathematical range claims cannot establish multiplication/promotion correctness by themselves.
4. What concrete device/toolchain, total persistent/scratch/stack accounting and timing evidence will later be available? The hypothetical 2048-byte ceiling and no FPU dependency are constraints, not observed compliance. Nominal 1 ms cadence is not a deadline. No quantitative compute/power threshold exists.
5. How will invalid rejection and detectable ordering/gap faults be exposed? State stuttering and logical-index preservation remain to be verified; no recovery or operational zero-fill policy is defined.
6. What future threshold, duration, decision output and integration requirements will complete R4? They remain unresolved before any whole-detector completion claim.

ACT explicitly leaves T002-2/3/4/5/6/7/8 all open. No candidate discharges numeric, lifecycle, per-event association, exceptional-input, memory/dependency, target/performance or detection verification. TRACE's earlier T002-1 gate is superseded in activation status by ACT, without this scout conducting an acceptance review. No historical VO discharge is inherited.

## Recommended next independent proof task

After separate authorization, assign **PO-003-2** to a distinct proof role: prove or refute the stated future-output equivalence and 2^372-state lower bound, checking same-length histories, startup padding, nonnegative-square injectivity, the current-versus-future output distinction and external-replay assumptions. Require a written independent argument, explicit adversarial cases and a separate review of applicability to the accepted subsystem boundary. A valuable rejection would precisely identify a failed hypothesis or counterexample rather than silently strengthen the contract.

This recommendation prioritizes a representation-independent comparison tool; it selects no architecture. PO-003-1 and PO-003-3 remain separate unproven candidates. No proof, independent review, AS change, AP/F selection, implementation, measured target fit or qualification is performed here. Stop after these two files.
