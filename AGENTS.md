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
continuity (independently accepted with clarifications, scoped)** → FR-003 historical integrity
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
**Current checkpoint:** independent FR-002 cooperative baseline-continuity
review `REVIEW_FR002_BASELINE_CONTINUITY_001` returned
`ACCEPT_WITH_CLARIFICATIONS`, committed at
`2dbd7b003ed515b916595287b8d29478fc1aa805`. This qualifies the
bounded implementation under its cooperative operating scope only.
The ROOT-002 canary has no protected validator; registration is separately
tested, so full non-Toy-1 domain-validator qualification remains outside
this review. Toy 1's continuity projection is still a candidate and
NOT ACTIVATED. Historical first FR-002 `REVISE` and old hostile-forgery
`REVIEW_FR002_GATE_ADAPTER_R1-001` paused task are preserved.
**Current FR-003 checkpoint:** independent review
`REVIEW_FR003_HISTORICAL_INTEGRITY_001` at
`f33cd51bddc3c415293899d0350b469e67403823` returned
**REVISE** for a single blocking malformed-path defect
`FR003-REVIEW-FINDING-001`: a JSON escaped lone UTF-8 surrogate can
raise `UnicodeEncodeError` instead of bounded `UNRESOLVED`.
The reviewer independently reran 87 unit tests and confirmed source-time
identity, current applicability separation and reviewer overlays.
**Current FR-003 outcome:** independent R1 review at
`ff9c723882b88dd9e5589c745768a1590e0cc9eb` returned
`ACCEPT` within `FR003_R1_FOCUSED_UNICODE_PATH_CORRECTION_ONLY`,
resolving `FR003-REVIEW-FINDING-001`. This is a narrowly accepted
correction, not a broad product/firmware qualification; the original
`REVISE` receipt remains immutable. The reviewer independently ran
91 test methods and real malformed-Unicode probes.

**CURRENT PRIORITY: separate CLN-001 Proof Reviewer.**
A distinct Proof Engineer produced `PROOF-ATTEMPT-004.md` and
`PROOF-BRIEFING-004.md` at
`2026cb251353285d8fe63671b9ce2b25c9fa9be6`.
Classification is `CLAIMED_PROOF_PENDING_REVIEW`; no accepted
theorem. Source scope: future numeric outputs over nonempty
continuations; conditional 31-tail/372-bit retained-state lower
bound under deterministic no-replay. Not full indexed interface,
real resource fit or product proof.
From the experiment checkout pull latest and run
`reviews/diagnostics/CLN-001-TASK-004/prepare_proof_review004.sh`
to CREATE `~/archbot-cln001-proof-review-004/`, then new
Codex independent proof reviewer. See
`reviews/diagnostics/CLN-001-TASK-004/PROOF_REVIEW_HANDOFF.md`.
Preserve actual outputs with truthful disposition and selective
push. No AP/CON/DE/C, implementation, qualified cleanroom,
historical VOs or previous solved Toy 1 leakage.
The finite-state/unbounded-index PO-003-3 issue remains open.

**PORTABILITY WORK PAUSED.** The last project-registry source at
`b6839c7fedea5bede7b485976b6590fdece6fca8` now has
[local producer evidence](reviews/qualification/PROJECT_SUBMODULE_FOUNDATION-local-test-receipt.json)
pushed in `a6bb262e609dfeb609616e895a3925358d2dffd3`:
12 exit-zero commands and 9 source pins verified. It has NOT been
independently reviewed. Do not launch its review, migrate Toy 1 to a
submodule, or make second-project work a prerequisite for pipe-cleaner.

**Cleanroom distinction:** removing an active project directory does
not remove its prior Git history, backups or connected data. FR-005
requires a separately isolated, positive-allowlist project package.

**Delivery priority:** qualify only the needed independent-review mode
(FR-004), make the permanent-framework / removable-project boundary
real, and get a fresh unsolved project to boot under FR-005. FR-006
is the independent integrated freeze; project migration does not confer
its approval. Do not expand accepted FR-003 into open-ended polishing.

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
