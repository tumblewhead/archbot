#!/usr/bin/env bash
# Stage 10: preserve raw independent review evidence exactly and selectively.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-ap-eval-review-010/out"
dst="reviews/diagnostics/CLN-001-TASK-010"
md="REVIEW-AP-EVALUATION-010.md"
js="REVIEW-AP-EVALUATION-010.json"
sum="REVIEW_AP_EVALUATION010_SHA256SUMS"
for f in "$md" "$js"; do
 [[ -s "$src/$f" ]] || { echo "STOP: missing original review $src/$f" >&2; exit 1; }
 if [[ -e "$dst/$f" ]]; then
   cmp -- "$src/$f" "$dst/$f" || { echo "STOP: conflicting archived bytes $f" >&2; exit 1; }
 else
   cp -- "$src/$f" "$dst/$f"
 fi
done
python3 - "$dst/$js" <<'PY'
import json, sys
with open(sys.argv[1], encoding="utf-8") as stream:
    j=json.load(stream)
if j.get("review_id") != "CLN-001-REVIEW-AP-EVALUATION-010":
    raise SystemExit("STOP: incorrect review_id")
allowed={"READY_FOR_DELEGATED_AP_EVIDENCE_DISPOSITION","REVISE_AP_EVALUATION","UNRESOLVED"}
if j.get("disposition") not in allowed:
    raise SystemExit("STOP: unknown review disposition")
for key in ("AP_selected","APs_finally_compliant","target_verified","product_verified","formal_cleanroom_qualified"):
    if j.get(key) is not False:
        raise SystemExit("STOP: "+key+" must be false")
if j.get("vo_discharged") != []:
    raise SystemExit("STOP: Stage-10 review cannot discharge VOs")
print("PASS: scope and output JSON flags")
PY
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
 echo "NOTICE: raw reviewer whitespace warning; do not alter immutable outputs"
fi
if git diff --cached --quiet; then
 echo "Already committed; no duplicate commit"
else
 git commit -m "Archive independent CLN-001 Stage-10 AP evaluation review"
fi
git push origin "$branch"
echo "SUCCESS: pushed Stage-10 independent review to experiment branch."
