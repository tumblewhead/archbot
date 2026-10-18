# CLN-001 Stage 11: first evidence acquisition, not another review of UNKNOWN

Source review Stage 10 archived at
`e5d2cfde2c856cc84192b294ac8c42a8746ba5aa`.
Disposition: `READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION`,
limited to reproducible Stage-9 model results. No actual consumer
index, pending output/lifecycle or C external service is shown.
See [delegated evidence decision](AP-EVIDENCE-DISPOSITION-010.yaml).

**Next stage is to create NEW interface feasibility evidence (IF11)**,
not to select an AP or merely review the same assumptions again.
The task explicitly constructs alternative *hypothetical*
consumer-facing contracts, an executable trace model, conditional
proofs/counterexamples, and a ledger tying missing evidence to the
next engineering decision. Actual source behavior and unapproved
external assumptions must remain visibly distinct. Separate
NUM11 C-kernel feasibility and SVC11 C-provider investigation are
authorized directions, but NOT silently completed by IF11.

The [process retrospective](../../../docs/CLN001_PROGRESS_GAP_AND_ORCHESTRATOR_PILOT_001.md)
preserves the case for a deterministic evidence-acquisition
routing rule and an orchestrator that automates mechanical
handoffs. This note is **not** framework-policy or autonomous
orchestrator approval, and **not** a fresh Toy1 restart.

## 1. Update and prepare bounded work

From the actual Archbot checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
git status -sb
git show --stat --oneline HEAD

bash -n reviews/diagnostics/CLN-001-TASK-011/prepare_if11.sh
bash -n reviews/diagnostics/CLN-001-TASK-011/archive_if11.sh
bash reviews/diagnostics/CLN-001-TASK-011/prepare_if11.sh
```

STOP on nonzero output; do not reset, force-push, clean unrelated
work or delete a previous workspace to hide a failure. Preparation
pins source identities and creates
`$HOME/archbot-cln001-if11`. Positive-allowlist context is not
proof of OS or connector isolation.

## 2. Launch distinct evidence-producing engineering agent

New terminal and fresh Codex session, NOT `codex resume`:

```bash
cd "$HOME/archbot-cln001-if11" || exit 1
codex
```

Prompt:

> Read AGENTS.md, TASK.md, and inputs/SHA256SUMS. Do the
> IF11 evidence-acquisition task: construct two truly explicit,
> consumer-visible index/acceptance/reset interface candidates;
> build and execute a stdlib-only trace model with independent
> expected behavior and negative controls; prove or falsify narrow
> feasibility claims under named assumptions; account for event
> identity, outstanding results, retained state and ownership.
> Do not treat a hypothetical provider or observer rank as an
> existing service. Write ONLY the four outputs requested in
> TASK.md, including executed commands and evidence counts.
> Do not select an AP, approve external capabilities or change AS.

Expected NEW outputs, not yet verified:
`IF11_TRACE_MODEL.py`, `IF11_FEASIBILITY.md`,
`IF11_RECEIPT.json`, `IF11_BRIEFING.md`.

## 3. Archive and push actual outputs

After all four files exist and the agent has completed its own checks:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
bash reviews/diagnostics/CLN-001-TASK-011/archive_if11.sh
git show --stat --oneline HEAD
```

Archive is restartable and selective; validates JSON limits, hashes
and Python source syntax, preserves original bytes, and pushes the
experiment branch only. The human may inspect any finding.

## After IF11

A **different independent reviewer** will inspect the NEW trace model,
reproduce the claimed results, and evaluate source/authority scope.
A positive review then permits the CLN-001 delegate to decide whether
an interface refinement/required external capability is supported,
a material AS clarification is needed, or another evidence package
is required. In parallel, a distinct bounded C numeric kernel
prototype can measure chosen representations and stack/compilation
without presenting it as a completed AP/CON/DE/C.

All H1-H6 fully realized and measured F values remain UNKNOWN
until actual evidence qualifies them. All T002-2..8 OPEN, R4
full sustained detection DEFERRED, AP A/B/C UNSELECTED. No product
qualification, full cleanroom or old Toy1 VO discharge.

**Longer-term:** finish current CLN-001 end-to-end, develop
orchestrator offline/live on a separate authorized track, then
run an uncontaminated fresh Toy1 with orchestrator and compare
cycle time and human interventions.
