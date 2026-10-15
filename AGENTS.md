# archbot: agent operating contract

This repository is the canonical nonvolatile memory for Progressive Concretization. The human operator pulls the latest Git revision before launching local Codex. Agents inspect the checked-out HEAD and its source evidence; do not reconstruct the current architecture from a chat transcript or assume a failed `git fetch` inside a read-only Codex sandbox implies stale evidence.

## Durable program roadmap and restart checkpoint

**Read at every new-agent handoff**, immediately after `PROJECT_SPINE.md`:
`process/roadmaps/PC_ROADMAP_CURRENT.yaml` (machine-readable milestones,
status, next eligible action, authority boundaries and full campaign), then
`docs/QUALIFICATION_CAMPAIGN.md` for detailed long-term objectives.
This file is the stable operating contract; `PROJECT_SPINE.md` is the
latest checkpoint and the roadmap YAML is the status index. Check the
current remote HEAD and later reviews/decisions before trusting any
checkpoint. Neither roadmap grants source-edit approval.

**Framework path:** genericity audit → FR-001 project context (independently
accepted with clarifications) → **FR-002 generic gate/project baseline
continuity (active redesign, NOT accepted)** → FR-003 historical integrity
→ FR-004 reviewer execution qualification → FR-005 cleanroom input package
→ FR-006 independent integrated framework-freeze review.

**Whole-program path:** finish Toy 1's end-to-end evidence and honest
qualification scope → complete and freeze the generic process → cleanroom
Toy 1 **without** dialogue → implement project-owned human/agent dialogue
and archive → cleanroom Toy 1 **with** dialogue → distinct Toy 2 and scaling.
Toy 1 has host-reviewed implementation but open VO-002..VO-006, unsettled
target evidence and final F-001 comparison. Framework pre-freeze work is
not Toy 1 product acceptance; no cleanroom or freeze is authorized yet.

**Active checkpoint:** user adopted the cooperative-audience assumption.
Human engineering authority approved the bounded baseline-continuity
replacement `FR002-BASELINE-CONTINUITY-REPLACEMENT-001`; see
`process/decisions/FR002_BASELINE_CONTINUITY_REPLACEMENT-AUTHORIZATION-001.yaml`.
**Current task:** source candidate authored but NOT LOCALLY TESTED and
NOT INDEPENDENTLY REVIEWED. The human pulls, runs focused gate and
continuity regressions, and pushes a bounded evidence receipt only when
every check passes. The prior FR-002 `REVISE` review remains historical;
the hostile-forgery `REVIEW_FR002_GATE_ADAPTER_R1-001` task is paused.
Next after validated local evidence is a **new**, independent review of
cooperative project-owned baseline continuity. Do not freeze the engine.

**Update rule:** on each independently reviewed milestone or authorized
change of direction, update `PROJECT_SPINE.md` and the roadmap YAML
together; amend this short section only when the long-term goal, sequence
or operating contract changes. Do not copy long test logs into any spine
or infer approval from a test outcome.

## Startup
1. Read this file, then `PROJECT_SPINE.md` and `process/roadmaps/PC_ROADMAP_CURRENT.yaml`.
2. Read `theory_of_operation.md` when architectural rationale, process modifications, or an unfamiliar gate require it.
3. Find the current architecture spine in `knowledge/` and follow only task-relevant typed relationships.
4. Read the assigned role definition in `agents/` and the relevant `process/` policy.
5. Review authoritative decisions, VO/AD ledgers, and review receipts; do not infer approval from a successful Codex run.
6. Identify the smallest necessary artifact change, and preserve prior versioned evidence.

## Roles and authority
- Human engineering authority approves requirement interpretations and architectural commitments.
- Proof Scout produces proof opportunities, never accepted theorems.
- Independent proof review may accept mathematical scope, not automatically C or firmware correctness.
- Evaluation uses the declared F and stage-specific gates. Do not require final firmware evidence to make an authorized provisional AP commitment.
- Verification Obligations remain binding; Architectural Debt records uncertainty and the risk of a reversible commitment.
- Contracts precede DE implementation. Implementation must preserve CON, DE, and AS obligations.

## Cooperative operating assumption

This framework assumes cooperative users and agents who follow the declared
engineering process. Preserve accepted requirements, review independence,
source provenance, active baselines and open obligations against accidental
omission, stale evidence or unintended changes. Do **not** expand a task into
defending against deliberate repository forgery, malicious self-repinning or
hostile rewriting of trusted engine files unless a specific project separately
requires that security property.

Project authority belongs to versioned accepted baselines and controlled
decisions; Git content hashes show identity, not approval. Generic engine
source must not accumulate a hardcoded allowlist of Toy 1 project authorities.
See `process/decisions/PC-COOPERATIVE-AUDIENCE-001.yaml` and
`docs/PC_COOPERATIVE_OPERATING_MODEL.md`. This assumption does not relax
product safety constraints, required independent reviews, or accidental
cleanroom solution-isolation obligations.

## Context and evidence
Spines are compact relationship indexes, not huge summaries. Exclude raw data and auxiliary artifacts from default agent context unless needed. Preserve access to source data and mandatory dependency closure. Do not equate graph reachability with context inclusion.
Do not attribute unstated facts to source documents. A structural check or successful test suite is not a proof or stakeholder approval.

## Human-machine work split
Assistant commits changed source/architecture artifacts to GitHub. Human pulls, runs tests and Codex locally, then pushes generated artifacts, reviewed receipts, and concise results. Raw datasets and full telemetry generally stay local; keep manifests, hashes, and bounded summaries.

## Required pull–run–push handoff

Read `process/pull_run_push_contract.v1.json` before issuing instructions for
the human's local tests, builds, simulations, review tasks, or evidence pushes.
This is the canonical machine-readable collaboration protocol.

The assistant authors/reviews and commits remote changes when connected GitHub
write access is available. The human operator pulls, performs local execution,
inspects generated artifacts, selectively stages and commits, then pushes.
**Every handoff must contain exact runnable pull, inspect/run, and selective
stage/commit/push commands for the current task.** No invented manifest IDs,
unresolved placeholders in live commands, force-push, `git add -A`, or
assumed green results. If a task is documentation-only, explicitly say that
no local run or push is needed.

For interactive Bash diagnostics use `set +e` and capture `$?` so a nonzero
task validation result does not terminate the user's shell. If a task fails,
stop dependent gates and identify the actual error before rerunning. A response
of "pushed" means fetch the latest remote HEAD, inspect its artifacts and review
receipts, and only then choose the next authorized action.

## Review execution without recursive Codex sessions

Follow [review execution modes](docs/REVIEW_EXECUTION_MODES.md). When an
already-running Codex agent is carrying out its assigned review, use
`python tools/task.py inspect --manifest ...` and
`python tools/task.py render --manifest ...` and perform that exact
task **within the present invocation**. Do not run `task.py run` from
inside Codex just to spawn a second Codex agent. From an outer host
shell, `task.py run` remains the registered launcher.

A rendered prompt is not evidence of execution, and a failed registered
launch is not a completed review. Label any direct review honestly,
identify its actual invocation and checks, and retain the original
failed-run record. Do not weaken sandbox permissions to hide a launch
failure. Preserve independent author/reviewer separation.

## Safe restart
A new agent must inspect repository HEAD, open `PROJECT_SPINE.md`, read applicable authority receipts and the live spine, then identify the next unresolved gate. If files described in the project spine have not yet been imported, report that explicitly. Never fabricate missing artifacts.
