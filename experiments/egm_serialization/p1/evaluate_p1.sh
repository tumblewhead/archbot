#!/usr/bin/env bash
# EGM P1 evaluator-side structural test. Never writes in Goldfish workspace.
# A structural match is not semantic equivalence, authority, or verified isolation.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
workspace="${1:-$HOME/archbot-egm-p1-001}"
audit_dir="${2:-$HOME/archbot-egm-p1-audit-001}"
[[ -d "$workspace/inputs" ]] || { echo "STOP: no prepared worker inputs" >&2; exit 2; }
[[ -s "$workspace/out/GOLDFISH_RECONSTRUCTION.json" ]] || { echo "STOP: no independent reconstruction" >&2; exit 2; }
[[ -s "$workspace/out/GOLDFISH_BRIEFING.md" ]] || { echo "STOP: no human briefing" >&2; exit 2; }
[[ ! -e "$audit_dir" ]] || { echo "STOP: audit destination already exists" >&2; exit 2; }
(cd "$workspace/inputs" && sha256sum -c SHA256SUMS)
mkdir -p "$audit_dir"
set +e
python3 experiments/egm_serialization/assess.py \
  --reference experiments/egm_serialization/p1/REFERENCE.json \
  --reconstruction "$workspace/out/GOLDFISH_RECONSTRUCTION.json" \
  > "$audit_dir/STRUCTURAL_ASSESSMENT.json"
rc=$?
set -e
python3 - "$workspace" "$audit_dir" "$rc" <<'PY'
import hashlib,json,pathlib,sys
w=pathlib.Path(sys.argv[1]);a=pathlib.Path(sys.argv[2]);code=int(sys.argv[3])
refs={
  "worker_spine":w/"SPINE.md",
  "worker_task":w/"TASK.md",
  "worker_input_manifest":w/"inputs/SHA256SUMS",
  "goldfish_reconstruction":w/"out/GOLDFISH_RECONSTRUCTION.json",
  "goldfish_briefing":w/"out/GOLDFISH_BRIEFING.md",
  "evaluator_reference":pathlib.Path("experiments/egm_serialization/p1/REFERENCE.json"),
  "evaluator_comparator":pathlib.Path("experiments/egm_serialization/assess.py"),
  "assessment":a/"STRUCTURAL_ASSESSMENT.json"
}
def sha(path):
 return hashlib.sha256(path.read_bytes()).hexdigest()
r={"schema":"pc-egm-p1-evaluator-receipt/v0",
   "structural_checker_exit":code,"source_sha256":{k:sha(v) for k,v in refs.items()},
   "runtime_isolation_verified":False,"semantic_review":"NOT_PERFORMED",
   "authority_accepted":False,"fresh_agent_identity":"NOT_EXTERNALLY_VERIFIED",
   "qualified_cleanroom":False}
(a/"RECEIPT.json").write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"audit_dir":str(a),"check_exit":code,
                  "semantic_review":"NOT_PERFORMED",
                  "runtime_isolation_verified":False},sort_keys=True))
PY
# rc=0 matched, rc=1 structural discrepancies, rc=2 invalid source/schema.
exit "$rc"
