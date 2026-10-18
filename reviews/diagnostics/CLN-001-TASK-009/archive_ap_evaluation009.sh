#!/usr/bin/env bash
# CLN-001 Stage 9: restartable archival of original independent evaluator outputs.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-cln001-ap-eval-009/out"
dst="reviews/diagnostics/CLN-001-TASK-009"
md="AP-EVALUATION-009.md"
js="AP-EVALUATION-009.json"
brief="AP-EVALUATION-BRIEFING-009.md"
manifest="AP_EVALUATION009_SHA256SUMS"
for f in "$md" "$js" "$brief"; do
  [[ -s "$src/$f" ]] || { echo "STOP: missing original $src/$f" >&2; exit 1; }
  if [[ -e "$dst/$f" ]]; then
    cmp -- "$src/$f" "$dst/$f" || { echo "STOP: conflicting prior archive $f" >&2; exit 1; }
    echo "Verified original: $f"
  else
    cp -- "$src/$f" "$dst/$f"
    echo "Copied: $f"
  fi
done
python3 - "$dst/$js" <<'PY'
import json, sys
with open(sys.argv[1], encoding="utf-8") as fh:
    j=json.load(fh)
if j.get("evaluation_id")!="CLN-001-AP-EVALUATION-009":
    raise SystemExit("STOP: incorrect evaluation ID")
for k in ("AP_selected","all_full_interface_gate_PASS","target_verified","product_verified","formal_cleanroom_qualified"):
    if j.get(k) is not False:
        raise SystemExit("STOP: required false evidence-limit flag "+k)
if j.get("vo_discharged") != []:
    raise SystemExit("STOP: no VO may be discharged by this evaluation")
print("PASS: structural evidence-limit flags")
PY
if [[ ! -e "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "$md" "$js" "$brief" > "$manifest")
fi
(cd "$dst" && sha256sum -c "$manifest")
while IFS= read -r staged; do
  case "$staged" in
    "$dst/$md"|"$dst/$js"|"$dst/$brief"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged file $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/$md" "$dst/$js" "$dst/$brief" "$dst/$manifest"
git diff --cached --stat
if ! git diff --cached --check; then
  echo "NOTICE: reviewer output whitespace warning; do not rewrite immutable evaluator bytes"
fi
if git diff --cached --quiet; then
  echo "All outputs already committed; nothing to recommit"
else
  git commit -m "Archive independent CLN-001 Stage-9 AP feasibility evaluation"
fi
git push origin "$branch"
echo "SUCCESS: original Stage-9 evaluation evidence archived remotely."
