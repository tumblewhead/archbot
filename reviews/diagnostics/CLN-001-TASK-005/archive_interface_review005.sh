#!/usr/bin/env bash
# Restartable archival: exact Stage-5 reviewer files. Run from Git checkout.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
if [[ "$(git branch --show-current)" != "$branch" ]]; then
  echo "STOP: wrong Git branch" >&2
  exit 1
fi
src="$HOME/archbot-cln001-interface-review-005/out"
dst="reviews/diagnostics/CLN-001-TASK-005"
md="REVIEW-INTERFACE-005.md"
js="REVIEW-INTERFACE-005.json"
manifest="REVIEW_INTERFACE005_SHA256SUMS"

# Check and copy original bytes. A repeated run must not overwrite them.
for name in "$md" "$js"; do
  if [[ ! -s "$src/$name" ]]; then
    echo "STOP: source is missing or empty: $src/$name" >&2
    exit 1
  fi
  if [[ -e "$dst/$name" ]]; then
    if ! cmp -- "$src/$name" "$dst/$name"; then
      echo "STOP: destination differs from original: $name" >&2
      exit 1
    fi
    echo "Verified existing copy: $name"
  else
    cp -- "$src/$name" "$dst/$name"
    echo "Copied: $name"
  fi
done
python -m json.tool "$dst/$js" >/dev/null
if [[ ! -e "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "$md" "$js" > "$manifest")
  echo "Created checksum manifest."
fi
(cd "$dst" && sha256sum -c "$manifest")

# The index (staging area) must contain only these intended paths.
while IFS= read -r staged; do
  case "$staged" in
    "$dst/$md"|"$dst/$js"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged path: $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)

git add -- "$dst/$md" "$dst/$js" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: whitespace warnings only; preserving immutable source bytes."
fi
if git diff --cached --quiet; then
  echo "Evidence already committed; no duplicate commit necessary."
else
  git commit -m "Archive independent CLN-001 interface applicability review"
fi
git push origin "$branch"
echo "SUCCESS: review evidence pushed."
