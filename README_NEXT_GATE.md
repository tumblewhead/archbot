# Next gate: proof acceptance record and AP evaluation

This update adds two first-class roles, selective graph views, a proof-disposition recorder, and the AP evaluation prompt. It does **not** auto-approve gates or select architecture.

Your local repository already contains PR-002. First record its stated disposition (without claiming implementation acceptance):

```bash
python tools/gate_record.py --review knowledge/architecture/AS-001/proofs/PR-002.md
```

Then launch Codex:

```bash
python tools/pc.py view --role evaluation-agent --spine /architecture/AS-001/spine.md
python tools/telemetry.py run --role evaluation-agent --prompt prompts/07-ap-evaluation.md
python tools/telemetry.py export --run latest
```

Upload the resulting `pc-review-*.zip` for independent review. If the accepted proof or evaluation rubric is not fully reachable by the spine, the agent should state that and explicitly fetch the narrow missing artifact, not silently omit it.

To apply to an existing checkout, from its root:

```bash
patch -p1 < /path/to/pc-next-gate.patch
python -m unittest discover -s tests -v
python tools/pc.py check --fast
```

The patch was generated against the supplied starter snapshot; existing files may have moved on. Inspect any patch rejects. Commit or stash local changes first so rollback is easy.

## Next experiment: Progressive Verification / AE-002

The new staged verification plan lives in `knowledge/architecture/AS-001/verification_plan.md`, with six VOs in `knowledge/architecture/AS-001/verification/`. See root `theory_of_operation.md` for rationale. Older AE-001 and F-001 stay unchanged.

```bash
python tools/pc.py check --fast
python tools/telemetry.py run --role evaluation-agent --prompt prompts/08-ap-evaluation-staged.md
python tools/telemetry.py export --run latest
```

A `NO_DOWNSELECTION` may still be correct: the new gate permits credible deferrals, not unsupported estimates.
