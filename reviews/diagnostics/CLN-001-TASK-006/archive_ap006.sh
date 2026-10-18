#!/usr/bin/env bash
# Restartable archive of original Stage-6 proposal-agent outputs.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-ap-006/out"
dst="reviews/diagnostics/CLN-001-TASK-006"
names=(AP-CANDIDATES-006.md AP-COMPARISON-006.md AP-BRIEFING-006.md)
manifest="AP006_OUTPUT_SHA256SUMS"

# Read source bytes; copy only if no existing destination, otherwise compare.
for n in "${names[@]}"; do
  [[ -s "$src/$n" ]] || { echo "STOP: missing $src/$n" >&2; exit 1; }
  if [[ -e "$dst/$n" ]]; then
    cmp -- "$src/$n" "$dst/$n" || { echo "STOP: different existing copy $n" >&2; exit 1; }
    echo "Verified copy: $n"
  else
    cp -- "$src/$n" "$dst/$n"
    echo "Copied: $n"
  fi
done
grep -q "AP_CANDIDATE_NOT_SELECTED" "$dst/AP-CANDIDATES-006.md" || {
  echo "STOP: missing AP candidate/not selected status" >&2; exit 1;
}

# The manifest records original file bytes. On retry, verify, never regenerate.
if [[ ! -e "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "${names[@]}" > "$manifest")
fi
(cd "$dst" && sha256sum -c "$manifest")

# Staging area (index): reject any file unrelated to this commit.
while IFS= read -r path; do
  case "$path" in
    "$dst/AP-CANDIDATES-006.md"|"$dst/AP-COMPARISON-006.md"|"$dst/AP-BRIEFING-006.md"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged path: $path" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)

git add -- "$dst/AP-CANDIDATES-006.md" "$dst/AP-COMPARISON-006.md" "$dst/AP-BRIEFING-006.md" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: whitespace style warnings. Original hashed source is preserved."
fi
if git diff --cached --quiet; then
  echo "No staged change; evidence already committed."
else
  git commit -m "Archive fresh CLN-001 competing AP candidates and symbolic comparison"
fi
git push origin "$branch"
echo "SUCCESS: AP draft evidence published."
