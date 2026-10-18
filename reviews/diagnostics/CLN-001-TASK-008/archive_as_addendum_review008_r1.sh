#!/usr/bin/env bash
# Preserve independent R1 review bytes; selective, idempotent archive.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-as-addendum-review-008-r1/out"
dst="reviews/diagnostics/CLN-001-TASK-008"
md="REVIEW-AS-ADDENDUM-008-R1.md"
js="REVIEW-AS-ADDENDUM-008-R1.json"
manifest="REVIEW_AS_ADDENDUM008_R1_SHA256SUMS"
for f in "$md" "$js"; do
  [[ -s "$src/$f" ]] || { echo "STOP: missing $src/$f" >&2; exit 1; }
  if [[ -e "$dst/$f" ]]; then
    cmp -- "$src/$f" "$dst/$f" || { echo "STOP: different prior archive $f" >&2; exit 1; }
  else
    cp -- "$src/$f" "$dst/$f"
  fi
done
python3 -m json.tool "$dst/$js" >/dev/null
if [[ ! -e "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "$md" "$js" > "$manifest")
fi
(cd "$dst" && sha256sum -c "$manifest")
while IFS= read -r staged; do
  case "$staged" in
    "$dst/$md"|"$dst/$js"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged file $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/$md" "$dst/$js" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: preserve original reviewer bytes; whitespace warning is not authorization to rewrite"
fi
if git diff --cached --quiet; then
  echo "Evidence already committed; no duplicate commit."
else
  git commit -m "Archive independent CLN-001 Stage-8 R1 focused AS review"
fi
git push origin "$branch"
echo "SUCCESS: focused independent review pushed."
