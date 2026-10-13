# Run telemetry and review handoffs

This is a **local-only observability layer** for Progressive Concretization. It writes files under ignored `runs/`; there is no analytics service, analytics SDK, or remote log sink. The Codex CLI itself may contact its configured model provider. Review packets only leave your machine if **you choose to upload them**.

## Recommended: a measured Codex run

From the initialized repository with `codex` installed and signed in:

```bash
python tools/telemetry.py run --role proof-scout --prompt prompts/01-proof-scout.md
python tools/telemetry.py list
python tools/telemetry.py export --run latest
```

The wrapper invokes `codex exec --json --sandbox workspace-write --output-last-message <local path> -` and sends the prompt over stdin. It records the Codex JSONL stream, counts events and available token usage, then runs a **fast** structure check and the unit tests. It also snapshots relevant files before/after and records content changes. Run times, failed commands, and output counters are observations, **not proof or architecture acceptance**. A structural pass cannot approve a theorem or an AP.

You can ask Codex to do the second experiment using:

```bash
python tools/telemetry.py run --role verification-agent --prompt prompts/02-proposal-review.md
python tools/telemetry.py export --run latest
```

Use a fresh Codex invocation for this to test persistent knowledge handoff rather than conversational state.

## If you prefer interactive Codex

```bash
python tools/telemetry.py start --role proof-scout --prompt prompts/01-proof-scout.md
# The command prints a run ID; save it.
codex
python tools/telemetry.py finish --run YOUR_RUN_ID
python tools/telemetry.py export --run YOUR_RUN_ID
```

Manual sessions **cannot automatically expose** Codex token usage, tool events, or exit status. The report explicitly marks these as unavailable. If you separately captured a Codex `exec --json` JSONL stream, pass `--events path/to/events.jsonl` to `finish`. If you know its exit status, also pass `--exit-code N`.

## What is recorded

| Field | Source | Interpretation |
|---|---|---|
| Wall time, exit code | Local wrapper | Observed runtime and process status |
| Input/output/cached tokens | `codex exec --json` turn-completed events | Observed where Codex emits usage; otherwise unavailable |
| Tool completions, failed commands | JSONL events | Counts, not a judgment of correctness |
| Spine projection size | Role view configuration | Eligible context, **not** evidence it was read |
| Files changed | Before/after file snapshots | Files changed *during* run, not necessarily by Codex |
| PO files and review receipts | Diffed paths | Output quantity, not artifact quality |
| Graph errors/warnings | `pc.py check --fast` | Structure and file-size checks; skips raw SHA-256 |
| Tests run/passed | Python `unittest` | Local unit tests only |
| Gate approval | Independent review | **Always `not_evaluated` by this recorder** |

`tools/pc.py check` (without `--fast`) streams raw data while checking SHA-256. It does not load the entire dataset into memory. Use that stronger integrity check when dataset provenance is in question.

## Review packet to send here

```bash
python tools/telemetry.py export --run latest
```

Creates `pc-review-<run-id>.zip` containing:

- `review.md`: compact execution, graph-view, structural-test, and change summary.
- `summary.json`: machine-readable metrics, hashes, artifact manifests, and missing-data indicators.
- `artifacts/`: bounded copies of changed Markdown/YAML/JSON/source artifacts from `knowledge/` and `reviews/`.
- `context/`: bounded role-specific **eligible** OKF concepts, so a fresh reviewer can understand AS, evidence summaries, and POs without the full repository.

The packet **excludes** raw JSONL events, command stdout/stderr logs, original prompts, environment variables, binary files, raw datasets, and oversized documents. It does **not** scan all copied prose/code for secrets. Always inspect the archive before sharing, particularly outside this synthetic trial. Use `export --no-context` for a smaller, more private packet. Neither spines nor packet filtering are security access controls.

These are size-bounded review packets, not archival backups. Missing files are documented with a reason and source path; the local originals remain available for selective follow-up.

## Compare runs

```bash
python tools/telemetry.py list
python tools/telemetry.py compare --baseline FIRST_RUN_ID --candidate SECOND_RUN_ID
```

This reports differences in observed token counts, wall time, changed-file counts, and validation exits. It is descriptive: comparisons across different prompts, source states, models, or hardware are **not controlled experiments**.

## How a reviewer should use the packet

Inspect the structured telemetry first, then read `artifacts/` and `context/`. Look for unsupported claims, missing assumptions, uninspected evidence, graph breaks, changes to AS/F/BKP, and whether the PO has a measurable effect on architecture. Treat all `UNRESOLVED` states as unresolved regardless of whether all unit tests pass. Request selected additional source artifacts only when the packet lacks essential evidence.
