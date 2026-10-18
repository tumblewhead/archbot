#!/usr/bin/env bash
# Restartable archival of independent raw D003 review. Do not change reviewer bytes.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || {
  echo "STOP: wrong branch" >&2; exit 1;
}
src="$HOME/archbot-cln001-d003-review-007/out"
dst="reviews/diagnostics/CLN-001-TASK-007"
md="REVIEW-D003-007.md"
js="REVIEW-D003-007.json"
sum="REVIEW_D003007_SHA256SUMS"
for file in "$md" "$js"; do
  [[ -s "$src/$file" ]] || { echo "STOP: missing $src/$file" >&2; exit 1; }
  if [[ -e "$dst/$file" ]]; then
    cmp -- "$src/$file" "$dst/$file" || { echo "STOP: differing archived $file" >&2; exit 1; }
  else
    cp -- "$src/$file" "$dst/$file"
  fi
done
python -m json.tool "$dst/$js" >/dev/null
if [[ ! -e "$dst/$sum" ]]; then
  (cd "$dst" && sha256sum "$md" "$js" > "$sum")
fi
(cd "$dst" && sha256sum -c "$sum")
while IFS= read -r p; do
  case "$p" in
    "$dst/$md"|"$dst/$js"|"$dst/$sum") ;;
    *) echo "STOP: unrelated staged file $p" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/$md" "$dst/$js" "$dst/$sum"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: raw review whitespace preserved; inspect warnings."
fi
if git diff --cached --quiet; then
  echo "Already archived, no duplicate commit."
else
  git commit -m "Archive independent CLN-001 Stage-7 D003 proposal review"
fi
git push origin "$branch"
echo "SUCCESS: raw D003 review pushed."
