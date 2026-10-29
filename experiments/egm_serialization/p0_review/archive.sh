#!/usr/bin/env bash
# Selective immutable archiving, independent EGM-P0 review.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="work/cln001-integration-c-kernel-harness"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
src="$HOME/archbot-egm-p0-review-001/out"
dst="experiments/egm_serialization/p0_review/evidence"
files=(REVIEW_EGM_P0_001.md REVIEW_EGM_P0_001.json)
manifest="REVIEW_EGM_P0_001_SHA256SUMS"
for f in "${files[@]}"; do
  [[ -s "$src/$f" ]] || { echo "STOP: missing reviewer output $src/$f" >&2; exit 1; }
done
mkdir -p "$dst"
for f in "${files[@]}"; do
  if [[ -e "$dst/$f" ]]; then
    cmp -- "$src/$f" "$dst/$f" || { echo "STOP: conflicting archived bytes $f" >&2; exit 1; }
  else
    cp -- "$src/$f" "$dst/$f"
  fi
done
python3 - "$dst/REVIEW_EGM_P0_001.json" <<'PY'
import json,sys
with open(sys.argv[1],encoding="utf-8") as f:r=json.load(f)
if r.get("review_id")!="EGM-P0-REVIEW-001":
 raise SystemExit("STOP: wrong review_id")
if r.get("disposition") not in {"READY_FOR_SCOPED_EGM_P1_DIAGNOSTIC","REVISE_P0_P1_INPUTS","UNRESOLVED"}:
 raise SystemExit("STOP: unknown disposition")
for k in ["structural_match_is_semantic_proof","authority_accepted","runtime_isolation_verified","generic_gate_activated"]:
 if r.get(k) is not False:
  raise SystemExit("STOP: forbidden elevation "+k)
print("PASS: scope and authority flags")
PY
if [[ ! -e "$dst/$manifest" ]]; then
  (cd "$dst" && sha256sum "${files[@]}" > "$manifest")
fi
(cd "$dst" && sha256sum -c "$manifest")
while IFS= read -r staged; do
  case "$staged" in
    "$dst/REVIEW_EGM_P0_001.md"|"$dst/REVIEW_EGM_P0_001.json"|"$dst/$manifest") ;;
    *) echo "STOP: unrelated staged file $staged" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only)
git add -- "$dst/${files[0]}" "$dst/${files[1]}" "$dst/$manifest"
git diff --cached --stat
if git diff --cached --quiet; then
  echo "Review already committed"
else
  git commit -m "Archive independent EGM-P0 checker and P1 reference review"
fi
git push origin "$branch"
