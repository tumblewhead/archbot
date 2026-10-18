#!/usr/bin/env bash
# CLN-001 first fresh Proof Engineer workspace; pre-freeze diagnostic only
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001" || {
  echo "STOP: expected CLN-001 experiment branch" >&2
  exit 1
}
root="$HOME/archbot-cln001-proof-engineer-004"
test ! -e "$root" || {
  echo "STOP: $root already exists; no reviewer or author workspace reuse" >&2
  exit 1
}
one="reviews/diagnostics/CLN-001-TASK-001"
two="reviews/diagnostics/CLN-001-TASK-002"
three="reviews/diagnostics/CLN-001-TASK-003"
four="reviews/diagnostics/CLN-001-TASK-004"
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"

check_blob() {
  local actual
  actual="$(git hash-object "$1")"
  if test "$actual" != "$2"; then
    printf 'STOP: source mismatch at %s (actual %s)\n' "$1" "$actual" >&2
    exit 1
  fi
}
check_blob "$one/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$two/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$two/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$three/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$three/PO-OPPORTUNITIES-003.md" 607ba5af4c25903d899d727b05641d1894d814b9
check_blob "$three/PO-BRIEFING-003.md" dfcb25386019624d07963f8baf1ecae2b8fdedfb
check_blob "$three/REVIEW-PO-003.md" 6cc6c0a6f318f73054d3cf4d601cc4e100ed8582
check_blob "$three/REVIEW-PO-003.json" 481be4c2943a74df962ddbd141441ef4e8527569
check_blob "$four/TASK-PROOF-004.md" 1b4c511a5fa2a3f8426ad52907fb4643900c6967
(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    | sha256sum -c -
)
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$one/DECISION-001.yaml" "$root/inputs/"
cp -- "$two/AS-REV-002.md" "$two/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$three/AS-ACTIVATION-002.yaml" "$three/PO-OPPORTUNITIES-003.md" \
  "$three/PO-BRIEFING-003.md" "$three/REVIEW-PO-003.md" \
  "$three/REVIEW-PO-003.json" "$root/inputs/"
cp -- "$four/TASK-PROOF-004.md" "$root/TASK.md"
cp -- "agents/proof-engineer.md" "$root/inputs/PROOF_ENGINEER_ROLE.md"

cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 separate Proof Engineer, Stage-4 diagnostic
Read TASK.md, PROOF_ENGINEER_ROLE.md, then inputs/SHA256SUMS.
Use only the supplied input package, no older solved Toy 1, Git
history, external sources, network, prior chat or hidden rubric.
You are not the Proof Scout, independent proof reviewer or human
sponsor delegate. The scout's opportunities remain unproven.
Write only out/PROOF-ATTEMPT-004.md and out/PROOF-BRIEFING-004.md.
This directory is a context allowlist, not a qualified OS sandbox.
ROLE
(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml *.json | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'Proof Engineer workspace created: %s\n' "$root"
printf 'Use a new Codex invocation here; do not reuse scout/reviewer sessions.\n'
