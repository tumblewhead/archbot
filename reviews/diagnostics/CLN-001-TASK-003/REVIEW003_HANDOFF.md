# CLN-001 Stage 3: independent review of proof opportunities and F candidate

**State:** Stage-3 authors pushed exact four source artifacts at
`1f7645135581ede5696596ab8abc1034e75a53cd`.
Proof opportunities are **UNPROVEN** and proposed F is **not accepted**.
This is the first post-AS synthetic diagnostic; no formal cleanroom,
target qualification, AP/CON/DE/C or historical VO discharge.

## Evidence archived

- `PO-OPPORTUNITIES-003.md` blob `607ba5af4c25903d899d727b05641d1894d814b9`
- `PO-BRIEFING-003.md` blob `dfcb25386019624d07963f8baf1ecae2b8fdedfb`
- `F-DRAFT-003.md` blob `5ec007bf45140d415dc105b71cd45c25f434adc2`
- `F-TRACE-003.md` blob `9aa486f174152d7ac7e1cbcf8e82b251fe94f6db`
- `OUTPUT_SHA256SUMS` pinned in same stage. Authoring reported
  seven source inputs verified against its positive allowlist.

The source scout proposed three mathematically distinct possibilities:
**PO-003-1** exact numeric and intermediate width bounds,
**PO-003-2** future-output equivalence from the last 31 samples
(`2^372` proposed lower-bound state count without replay), and
**PO-003-3** conditional impossibility of generating indefinitely
growing exact logical indices from finite closed internal state.
The third can expose a *real interface scoping decision* even if the
energy calculation is finite-state; it is conditional on the declared
closed model, not an unconditional conflict in the accepted AS.

The F analyst proposed hard gate H1..H6 plus a provisional Pareto
objective `(RAM_peak, compute_effort, energy)`. The first two axes
are related to resource conservation; **energy** as a distinct
active objective is an explicit additional proposal requiring
disposition, not source-granted authority. All candidate evidence
is currently UNKNOWN. R4 full detection is still deferred.

## One preparation script, one NEW reviewer session, two verdicts

From your **real Archbot Git checkout**:

```bash
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
bash reviews/diagnostics/CLN-001-TASK-003/prepare_review003.sh
```

The preparation **creates**, rather than assumes, the directory
`$HOME/archbot-cln001-review-003`. It verifies the stage-3
output hashes, source BKP and Git blob pins before writing inputs,
then records a reviewer input manifest. It refuses an existing
review directory rather than silently reusing a previous invocation.

In a **new Codex terminal/session**:

```bash
cd "$HOME/archbot-cln001-review-003" || exit 1
codex
```

Prompt:

> Read AGENTS.md and TASK.md. Independently check the three proof
> opportunities and candidate F against original BKP, synthetic
> D001, accepted AS and task scope. Produce the separately scoped
> four review files in out/ and stop. Do not prove a theorem,
> accept F, select an AP or change requirements.

Expected files:

```text
out/REVIEW-PO-003.md
out/REVIEW-PO-003.json
out/REVIEW-F-003.md
out/REVIEW-F-003.json
```

Each reviewer outcome is distinct:
- PO `READY_FOR_PROOF_ENGINEER`, `REVISE_OPPORTUNITIES` or `UNRESOLVED`.
- F `READY_FOR_DELEGATED_F_DISPOSITION`, `REVISE_F_DRAFT` or `UNRESOLVED`.

`READY` is **not** approval of a theorem or acceptance of F.
This is one separately invoked reviewer evaluating both unrelated
drafts, not two independently authenticated reviewers. Filesystem
isolation and connector access are not independently verified
unless the user arranges a restricted runtime and records evidence.

## Preserve and push real review files

After the reviewer finishes, from the real experiment-branch checkout:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
src="$HOME/archbot-cln001-review-003/out"
dst="reviews/diagnostics/CLN-001-TASK-003"
test -z "$(git diff --cached --name-only)"

for name in REVIEW-PO-003.md REVIEW-PO-003.json REVIEW-F-003.md REVIEW-F-003.json; do
  test -s "$src/$name"
  test ! -e "$dst/$name"
done
python -m json.tool "$src/REVIEW-PO-003.json" >/dev/null
python -m json.tool "$src/REVIEW-F-003.json" >/dev/null

for name in REVIEW-PO-003.md REVIEW-PO-003.json REVIEW-F-003.md REVIEW-F-003.json; do
  cp -- "$src/$name" "$dst/$name"
done
(
  cd "$dst"
  sha256sum REVIEW-PO-003.md REVIEW-PO-003.json \
    REVIEW-F-003.md REVIEW-F-003.json > REVIEW_OUTPUT_SHA256SUMS
  sha256sum -c REVIEW_OUTPUT_SHA256SUMS
)

git add -- \
  "$dst/REVIEW-PO-003.md" "$dst/REVIEW-PO-003.json" \
  "$dst/REVIEW-F-003.md" "$dst/REVIEW-F-003.json" \
  "$dst/REVIEW_OUTPUT_SHA256SUMS"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record independent diagnostic Stage-3 PO and F reviews"
git push origin experiment/toy1-pipe-cleaner-001
)
```

The reviewer may return different decisions on the two products.
Preserve its actual findings; do not fabricate a JSON when a report
is missing. Leave old accepted Toy 1, unrelated FR-002 untracked
files, and the original authored sources untouched.

## Next gate

The coordinator inspects the exact pushed reviewer files and
then, within its delegated synthetic CLN-001 authority, may
dispose F while retaining all missing objective authority explicitly.
For PO, a separate Proof Engineer can be instructed to attempt
one theorem only after its candidate survives opportunity review.
Even a favorable Proof Engineer draft requires separate proof
review before any theorem acceptance.

Do not prematurely select AP or implement C.
