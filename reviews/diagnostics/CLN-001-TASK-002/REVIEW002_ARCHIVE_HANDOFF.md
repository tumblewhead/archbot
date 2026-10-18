# CLN-001: archive REVIEW-002 and activate scoped AS disposition

The distinct second reviewer returned
**READY_FOR_DELEGATED_AS_DISPOSITION**. The delegated decision maker
inspected both user-uploaded original reviewer outputs and issued
[AS-DISPOSITION-002.yaml](AS-DISPOSITION-002.yaml):
`ACCEPT_WITH_NONBLOCKING_PROVENANCE_CLARIFICATION`, limited to
the synthetic CLN-001 AS=(C,R,PS). **This Git-pinned acceptance does
not activate until original reviewer outputs are archived and verified.**

## Original uploaded reviewer files

| Filename | SHA-256 | Git blob SHA-1 |
|---|---|---|
| REVIEW-002.json | `09ed9606c571d468138b8f7709ada2c625fc7c63b39a2002d1d0a85ece71afca` | `dcacb5f0d0135940e7410c735c58d4ecf632394e` |
| REVIEW-002.md | `b9f9f4a0c110768592d7999a3d92c272a8acacc779b2c74bc873078a664b0e61` | `4b5a8006555f49cdb002a89518c0a7ae96c6f1db` |

**Preserve the exact original files**, not text retyped or normalized
from conversation. Reviewer source crosswalk verified all 15 inputs.
Finding F3 documents the stale original same-conversation self-review
as a separate artifact; the real REVIEW-001 question-readiness review
was already independently archived at
`e01f91177c20e14f3aea3a11d9025821156dd971`.
No author statements are retrospectively corrected and no
separation/isolation guarantees are fabricated.

## Human archive steps

Run in the local Archbot checkout on the experiment branch. The
reviewer source directory is the one created by the independent
review handoff, **not** the earlier `archbot-as-review-001` nor the
original Toy 1 author workspace.

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

src="$HOME/archbot-as-review-002/out"
dst="reviews/diagnostics/CLN-001-TASK-002"

test -z "$(git diff --cached --name-only)"
test -s "$src/REVIEW-002.json"
test -s "$src/REVIEW-002.md"
test ! -e "$dst/REVIEW-002.json"
test ! -e "$dst/REVIEW-002.md"

(
  cd "$src"
  printf '%s  %s\n' \
    09ed9606c571d468138b8f7709ada2c625fc7c63b39a2002d1d0a85ece71afca REVIEW-002.json \
    b9f9f4a0c110768592d7999a3d92c272a8acacc779b2c74bc873078a664b0e61 REVIEW-002.md \
    | sha256sum -c -
)

cp -- "$src/REVIEW-002.json" "$dst/"
cp -- "$src/REVIEW-002.md" "$dst/"

python -m json.tool "$dst/REVIEW-002.json" >/dev/null

test "$(git hash-object "$dst/REVIEW-002.json")" = \
  dcacb5f0d0135940e7410c735c58d4ecf632394e
test "$(git hash-object "$dst/REVIEW-002.md")" = \
  4b5a8006555f49cdb002a89518c0a7ae96c6f1db

git add -- "$dst/REVIEW-002.json" "$dst/REVIEW-002.md"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Archive independent CLN-001 AS-REV-002 review evidence"
git push origin experiment/toy1-pipe-cleaner-001
)
```

If a source hash does not match, **STOP**. Report the actual hashes;
do not alter the files to force a match. Do not stage unrelated
untracked FR-002 files.

## Next gate after verified remote archive

The delegated scoped AS disposition becomes an active, source-pinned
synthetic baseline after confirming both reviewer blobs are pushed.
The coordinator then prepares new fresh-agent inputs for:

1. **Proof Scout:** propose 1–3 high-value, explicitly *unproven*
   properties/bounds/representation-independent invariants linked to
   R1–R6, model assumptions and evidence obligations; include possible
   counterexamples. Do not claim a proof exists yet.
2. **Figure of Merit:** derive the *fresh* numeric axes, resource
   hard constraint, unknown target costs, and symbolic feasibility
   decision criteria without importing older Toy 1 F-001/AP values.
   Any criterion not justified by D001 remains UNKNOWN or proposal,
   not adopted authority.

Use a separate role/session and input allowlist for each stage.
Keep unresolved R4 whole-detector detection integration as a
continuing obligation. No implementation, target qualification,
formal cleanroom, historical Toy 1 VO discharge, or framework
freeze follows from accepting this diagnostic AS.
