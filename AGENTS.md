# archbot: agent operating contract

This repository is the canonical nonvolatile memory for Progressive Concretization. The human operator pulls the latest Git revision before launching local Codex. Agents inspect the checked-out HEAD and its source evidence; do not reconstruct the current architecture from a chat transcript or assume a failed `git fetch` inside a read-only Codex sandbox implies stale evidence.

## Startup
1. Read this file, then `PROJECT_SPINE.md`.
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

## Context and evidence
Spines are compact relationship indexes, not huge summaries. Exclude raw data and auxiliary artifacts from default agent context unless needed. Preserve access to source data and mandatory dependency closure. Do not equate graph reachability with context inclusion.
Do not attribute unstated facts to source documents. A structural check or successful test suite is not a proof or stakeholder approval.

## Human-machine work split
Assistant commits changed source/architecture artifacts to GitHub. Human pulls, runs tests and Codex locally, then pushes generated artifacts, reviewed receipts, and concise results. Raw datasets and full telemetry generally stay local; keep manifests, hashes, and bounded summaries.

## Safe restart
A new agent must inspect repository HEAD, open `PROJECT_SPINE.md`, read applicable authority receipts and the live spine, then identify the next unresolved gate. If files described in the project spine have not yet been imported, report that explicitly. Never fabricate missing artifacts.
