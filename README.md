# archbot: Progressive Concretization

Proof-driven, evidence-traceable firmware architecture work using OKF v0.2 concepts, typed spines, agent roles, staged verification, and architectural debt.

## Source of truth

**This Git repository is the canonical nonvolatile project memory.** Every agent should fetch the current branch, inspect `AGENTS.md`, and follow the architecture spine instead of reconstructing the project from chat history.

## Initial import

The existing working prototype and run history currently live on the developer workstation under `progressive-concretization-codex/`. This repository is being initialized as the permanent home. Preserve and import locally generated OKF artifacts, proof reviews, verification receipts, and tests; do not overwrite them with an older reference snapshot.

## Workflow

ChatGPT commits source changes here. The developer pulls, performs tests and Codex experiments locally, then pushes generated evidence. Review the pushed evidence before initiating the next architectural gate. Large datasets and telemetry raw logs should remain outside Git; version small manifests, hashes, result summaries, and review receipts.
