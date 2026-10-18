#!/usr/bin/env bash
# Restartable archive: Stage-6 independent AP review, preserving exact raw bytes.
# Run from the real Archbot experiment-branch checkout.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || {
  echo "STOP: wrong branch, expected $branch" >&2; exit 1
}
src="$HOME/archbot-cln001-ap-review-006/out"
dst="reviews/diagnostics/CLN-001-TASK-006"
md="REVIEW-AP-006.md"
js="REVIEW-AP-006.json"
manifest="REVIEW_AP006_SHA256SUMS"

# Copy only when necessary. On a retry, compare bytes, never overwrite.
for f in "$md" "$js"; do
  [[ -s "$src/$f" ]] || { echo "STOP: missing original $src/$f" >&2; exit 1; }
  if [[ -e "$dst/$f" ]]; then
    cmp -- "$src/$f" "$dst/$f" || { echo "STOP: different existing copy $f" >&2; exit 1; }
    echo "Verified existing copy: $f"
  else
    cp -- "$src/$f" "$dst/$f"
    echo "Copied original: $f"
  fi
done
python -m json.tool "$dst/$js" >/dev/null

# Check source identity. Keep the first manifest stable on retries.
if [[ ! -e "$dst/$manifest" ]]; then
  ( cd "$dst" && sha256sum "$md" "$js" > "$manifest" )
  echo "Created raw-byte checksum manifest."
fi
( cd "$dst" && sha256sum -c "$manifest" )

# The Git index is the staging area. Never include other staged changes.
while IFS= read -r staged; do
  case "$staged" in
    "$dst/$md"|"$dst/$js"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged file: $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)

git add -- "$dst/$md" "$dst/$js" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: whitespace style findings; original reviewer bytes preserved."
fi

# A commit snapshots staged content. No new diff means already committed.
if git diff --cached --quiet; then
  echo "Nothing new staged; no duplicate commit required."
else
  git commit -m "Archive independent CLN-001 Stage-6 AP candidate review"
fi

# Publish this branch only. A repeated successful push is safe.
git push origin "$branch"
echo "SUCCESS: Stage-6 independent AP review on remote branch."
