#!/usr/bin/env bash
# Preserve original Stage-11 IF11 evidence, restartable and selective.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-if11/out"
dst="reviews/diagnostics/CLN-001-TASK-011"
files=("IF11_TRACE_MODEL.py" "IF11_FEASIBILITY.md" "IF11_RECEIPT.json" "IF11_BRIEFING.md")
manifest="IF11_SHA256SUMS"
for file in "${files[@]}"; do
  [[ -s "$src/$file" ]] || { echo "STOP: missing $src/$file" >&2; exit 1; }
  if [[ -e "$dst/$file" ]]; then
    cmp -- "$src/$file" "$dst/$file" || { echo "STOP: archived bytes differ $file" >&2; exit 1; }
  else
    cp -- "$src/$file" "$dst/$file"
  fi
done
python3 - "$dst/IF11_RECEIPT.json" "$dst/IF11_TRACE_MODEL.py" <<'PY'
import json,sys,pathlib
j=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8"))
if j.get("study_id")!="CLN-001-IF11":
    raise SystemExit("STOP: incorrect study_id")
for key in ["AP_selected","AS_changed","RI_RN_C_HIST_approved","full_H1_H6_PASS","target_verified","product_verified","formal_cleanroom_qualified"]:
    if j.get(key) is not False:
        raise SystemExit(f"STOP: required false flag {key}")
if j.get("vo_discharged")!=[]:
    raise SystemExit("STOP: IF11 cannot discharge VOs")
compile(pathlib.Path(sys.argv[2]).read_text(encoding="utf8"),sys.argv[2],"exec")
print("PASS: JSON scope flags and Python syntax")
PY
if [[ ! -f "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "${files[@]}" > "$manifest")
fi
(cd "$dst" && sha256sum -c "$manifest")
while IFS= read -r staged; do
  case "$staged" in
    "$dst/IF11_TRACE_MODEL.py"|"$dst/IF11_FEASIBILITY.md"|"$dst/IF11_RECEIPT.json"|"$dst/IF11_BRIEFING.md"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged path $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/IF11_TRACE_MODEL.py" "$dst/IF11_FEASIBILITY.md" "$dst/IF11_RECEIPT.json" "$dst/IF11_BRIEFING.md" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: raw evidence whitespace preserved; inspect warning"
fi
if git diff --cached --quiet; then
  echo "Evidence already committed"
else
  git commit -m "Archive CLN-001 IF11 new interface feasibility evidence"
fi
git push origin "$branch"
echo "SUCCESS: IF11 exact evidence on experiment branch"
