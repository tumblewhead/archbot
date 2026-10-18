#!/usr/bin/env bash
# CLN-001 separate Stage-4 mathematical Proof Reviewer workspace
# Run from real Archbot experiment-branch checkout. Diagnostic only.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001" || {
  echo "STOP: expected experiment/toy1-pipe-cleaner-001" >&2
  exit 1
}
root="$HOME/archbot-cln001-proof-review-004"
test ! -e "$root" || {
  echo "STOP: $root exists; do not reuse or overwrite a reviewer workspace" >&2
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
    printf 'STOP: %s: blob mismatch, actual %s\n' "$1" "$actual" >&2
    exit 1
  fi
}

check_blob "$one/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$two/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$two/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$three/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$three/PO-OPPORTUNITIES-003.md" 607ba5af4c25903d899d727b05641d1894d814b9
check_blob "$three/REVIEW-PO-003.md" 6cc6c0a6f318f73054d3cf4d601cc4e100ed8582
check_blob "$three/REVIEW-PO-003.json" 481be4c2943a74df962ddbd141441ef4e8527569
check_blob "$four/TASK-PROOF-004.md" 1b4c511a5fa2a3f8426ad52907fb4643900c6967
check_blob "$four/PROOF-ATTEMPT-004.md" 005c57a539369cb4e62699a7a806974a81eb235b
check_blob "$four/PROOF-BRIEFING-004.md" 24c8fafa4fdeefdc541972aa3de0f10ffc262ad0
check_blob "$four/PROOF004_SHA256SUMS" 1a6c97d97117d9e1e3b38906681d96ce1d3afa2e
check_blob "$four/TASK-REVIEW-PROOF-004.md" a8bf8ff61804d97414903d0b18ab6f77cd9b11f8
check_blob "agents/proof-reviewer.md" d368c6aa11d4dae83a0133322c7a31ee4f8b9e8d

(
  cd "$four"
  sha256sum -c PROOF004_SHA256SUMS
)
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
cp -- "$three/AS-ACTIVATION-002.yaml" \
  "$three/PO-OPPORTUNITIES-003.md" "$three/REVIEW-PO-003.md" \
  "$three/REVIEW-PO-003.json" "$root/inputs/"
cp -- "$four/TASK-PROOF-004.md" "$four/PROOF-ATTEMPT-004.md" \
  "$four/PROOF-BRIEFING-004.md" "$root/inputs/"
cp -- "agents/proof-reviewer.md" "$root/inputs/PROOF_REVIEWER_ROLE.md"
cp -- "$four/TASK-REVIEW-PROOF-004.md" "$root/TASK.md"

cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 independent mathematical Proof Reviewer

Read TASK.md, PROOF_REVIEWER_ROLE.md and inputs/SHA256SUMS.
You are not the proof author, Proof Scout, or human sponsor delegate.
All mathematical claims in PROOF-ATTEMPT-004 are pending review.
Use ONLY inputs/ for technical context; no older Toy 1 solutions,
other workspaces, Git history, network, connected systems or evaluator.
Only write out/REVIEW-PROOF-004.md and out/REVIEW-PROOF-004.json.
Do not change AS/F/D001, prove product compliance or select an AP.
Directory-based source isolation does not establish OS or connector
isolation and must not be called formally cleanroom qualified.
ROLE

(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml *.json | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'New Proof Reviewer workspace: %s\n' "$root"
printf 'Start a distinct, new Codex invocation.\n'
