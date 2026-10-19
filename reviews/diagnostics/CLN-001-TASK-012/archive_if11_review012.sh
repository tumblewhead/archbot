#!/usr/bin/env bash
# Restartable, selective archive of independent IF11 evidence review.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-if11-review-012/out"
dst="reviews/diagnostics/CLN-001-TASK-012"
md="REVIEW-IF11-012.md"
js="REVIEW-IF11-012.json"
sum="REVIEW_IF11_012_SHA256SUMS"
for f in "$md" "$js"; do
  [[ -s "$src/$f" ]] || { echo "STOP: missing original $src/$f" >&2; exit 1; }
  if [[ -e "$dst/$f" ]]; then
    cmp -- "$src/$f" "$dst/$f" || { echo "STOP: conflicting prior archive $f" >&2; exit 1; }
  else
    cp -- "$src/$f" "$dst/$f"
  fi
done
python3 - "$dst/$js" <<'PY'
import json,sys,pathlib
j=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8"))
if j.get("review_id")!="CLN-001-REVIEW-IF11-012":
    raise SystemExit("STOP: bad review ID")
if j.get("disposition") not in {"READY_FOR_DELEGATED_IF11_EVIDENCE_DISPOSITION","REVISE_IF11_EVIDENCE","UNRESOLVED"}:
    raise SystemExit("STOP: invalid review disposition")
for k in ("AP_selected","AS_changed","RI_RN_C_HIST_approved","all_full_H1_H6_PASS","target_verified","product_verified","formal_cleanroom_qualified"):
    if j.get(k) is not False:
        raise SystemExit("STOP: forbidden approval/qualification "+k)
if j.get("vo_discharged")!=[]:
    raise SystemExit("STOP: no VO discharge permitted")
print("PASS: evidence-review scope flags")
PY
if [[ ! -e "$dst/$sum" ]]; then
  (cd "$dst" && sha256sum "$md" "$js" > "$sum")
fi
(cd "$dst" && sha256sum -c "$sum")
while IFS= read -r staged; do
  case "$staged" in
    "$dst/$md"|"$dst/$js"|"$dst/$sum") ;;
    *) echo "STOP: unrelated staged path $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/$md" "$dst/$js" "$dst/$sum"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: raw review whitespace preserved; report warnings without rewriting bytes"
fi
if git diff --cached --quiet; then
  echo "Evidence already committed"
else
  git commit -m "Archive independent CLN-001 IF11 Stage-12 evidence review"
fi
git push origin "$branch"
echo "SUCCESS: review evidence archived remotely"
