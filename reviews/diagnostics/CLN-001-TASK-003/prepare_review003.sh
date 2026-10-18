#!/usr/bin/env bash
# CLN-001 Stage-3 dual-output independent diagnostic reviewer preparation
# Run from the real archbot Git checkout, NOT either Stage-3 author workspace.
set -euo pipefail
repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001" || {
  echo "STOP: expected experiment/toy1-pipe-cleaner-001 branch" >&2
  exit 1
}
root="$HOME/archbot-cln001-review-003"
test ! -e "$root" || {
  echo "STOP: reviewer directory exists; do not reuse a session or overwrite it" >&2
  exit 1
}

bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
role="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/framework/agents/verification-agent.md"
one="reviews/diagnostics/CLN-001-TASK-001"
two="reviews/diagnostics/CLN-001-TASK-002"
three="reviews/diagnostics/CLN-001-TASK-003"

# Check immutable Git input identities before creating the reviewer package.
check_blob() {
  local path="$1"
  local expected="$2"
  local actual
  actual="$(git hash-object "$path")"
  test "$actual" = "$expected" || {
    printf 'STOP: source blob mismatch %s: %s != %s\n' "$path" "$actual" "$expected" >&2
    exit 1
  }
}
check_blob "$one/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$two/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$two/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$three/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$three/TASK-PO-SCOUT-003.md" b4360f74cfb53f1b6d248b7a56f1e7c48f50699e
check_blob "$three/TASK-FOM-003.md" df32ddefa021aafa61a8b2266612c7fc6838fcc1
check_blob "$three/PO-OPPORTUNITIES-003.md" 607ba5af4c25903d899d727b05641d1894d814b9
check_blob "$three/PO-BRIEFING-003.md" dfcb25386019624d07963f8baf1ecae2b8fdedfb
check_blob "$three/F-DRAFT-003.md" 5ec007bf45140d415dc105b71cd45c25f434adc2
check_blob "$three/F-TRACE-003.md" 9aa486f174152d7ac7e1cbcf8e82b251fe94f6db
check_blob "$three/OUTPUT_SHA256SUMS" d8028e91515ad53566b61f6eb0b8c4516c10df2a
check_blob "$three/TASK-REVIEW-003.md" d3e10553dedbda2f28da12b092dfcef565871727

(
  cd "$three"
  sha256sum -c OUTPUT_SHA256SUMS
)
(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    | sha256sum -c -
)
(
  cd "$(dirname "$role")"
  printf '%s  %s\n' \
    7f6463b5a54278230dbd73c5f49fc68cb4192ca83c48de191b22674f8d3ae1f3 verification-agent.md \
    | sha256sum -c -
)

mkdir -p "$root/inputs" "$root/out"
for name in problem-origin.md adc.md target.md; do
  cp -- "$bkp/$name" "$root/inputs/"
done
cp -- "$role" "$root/inputs/verification-agent.md"
cp -- "$one/DECISION-001.yaml" "$root/inputs/"
cp -- "$two/AS-REV-002.md" "$two/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$three/AS-ACTIVATION-002.yaml" "$three/TASK-PO-SCOUT-003.md" \
  "$three/TASK-FOM-003.md" "$three/PO-OPPORTUNITIES-003.md" \
  "$three/PO-BRIEFING-003.md" "$three/F-DRAFT-003.md" \
  "$three/F-TRACE-003.md" "$root/inputs/"
cp -- "$three/TASK-REVIEW-003.md" "$root/TASK.md"

cat > "$root/AGENTS.md" <<'ROLE'
# Independent Stage-3 reviewer, CLN-001
Read TASK.md, then the positive-allowlist files in inputs/.
This is one review agent assessing two separately authored DRAFT products.
You are NOT their author, Proof Engineer, sponsor-delegate or AS reviewer.
Do not access previous solved Toy 1 files, old Git history, other
workspaces, connected systems, external sources or hidden evaluator.
Only write out/REVIEW-PO-003.md/json and out/REVIEW-F-003.md/json.
No proof acceptance, F approval, design/implementation selection,
formal cleanroom qualification, or product VO discharge.
Actual operating-system isolation requires separate runtime controls;
being in this directory alone does not enforce it.
ROLE

(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'Created independent Stage-3 review package: %s\n' "$root"
printf 'New Codex session only. Expected four out/REVIEW-* files.\n'
