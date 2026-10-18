#!/usr/bin/env bash
# Prepare CLN-001 Stage-5 independent reviewer from pinned, allowlisted inputs.
# Run from the REAL Archbot Git checkout, not a Codex author workspace.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

expected_branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$expected_branch" ]] || {
  printf 'STOP: expected branch %s\n' "$expected_branch" >&2
  exit 1
}
root="$HOME/archbot-cln001-interface-review-005"
[[ ! -e "$root" ]] || {
  printf 'STOP: %s exists. Do not reuse an independent review session.\n' "$root" >&2
  exit 1
}

bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
role="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/framework/agents/verification-agent.md"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s5="reviews/diagnostics/CLN-001-TASK-005"

# Git blob SHA identifies exact contents, without using 'git add'.
check_blob() {
  local actual
  [[ -f "$1" ]] || { printf 'STOP: source missing %s\n' "$1" >&2; exit 1; }
  actual="$(git hash-object "$1")"
  [[ "$actual" == "$2" ]] || {
    printf 'STOP: Git blob mismatch: %s\nActual %s, expected %s\n' "$1" "$actual" "$2" >&2
    exit 1
  }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s2/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s5/INTERFACE-OPTIONS-005.md" b64ece52ada5963f5196800b81ddb816904602e0
check_blob "$s5/DECISION-PROPOSAL-005.yaml" 3846119f191ee4776e1242100d003d91a32da7b2
check_blob "$s5/BRIEFING-005.md" 9dec948faa94ab6982e87801816b3b0ce49b982b
check_blob "$s5/STAGE5_OUTPUT_SHA256SUMS" ad9751445d4fb37ddd828f930a6736316fb5b9c7
check_blob "$s5/TASK-REVIEW-INTERFACE-005.md" fcc3f1d4da57cee0132fce8279953f3a1adf9bf7

# SHA-256 verifies the original author bytes, independently of Git's blob IDs.
( cd "$s5" && sha256sum -c STAGE5_OUTPUT_SHA256SUMS )
(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    | sha256sum -c -
)
printf '%s  %s\n' \
  7f6463b5a54278230dbd73c5f49fc68cb4192ca83c48de191b22674f8d3ae1f3 "$role" \
  | sha256sum -c -

# A separate directory limits supplied context, NOT the OS's accessible files.
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$role" "$root/inputs/verification-agent.md"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$s2/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s5/INTERFACE-OPTIONS-005.md" "$s5/DECISION-PROPOSAL-005.yaml" \
  "$s5/BRIEFING-005.md" "$root/inputs/"
cp -- "$s5/TASK-REVIEW-INTERFACE-005.md" "$root/TASK.md"

cat > "$root/AGENTS.md" <<'ROLE'
# Independent CLN-001 Stage-5 proposal reviewer

Read TASK.md and inputs/SHA256SUMS, then only inputs/.
You are not the interface analyst or the CLN-001 delegated decision maker.
Technical sources are pinned. Do not inspect previous solved Toy 1,
old repository history, other workspaces, connected apps, external
sources or evaluator data. You cannot approve D002 or select an AP.
Write ONLY out/REVIEW-INTERFACE-005.md and
out/REVIEW-INTERFACE-005.json; leave inputs unchanged.
A new Codex session is required. Directory isolation is NOT a
verified OS/container/connector isolation boundary.
ROLE

(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'SUCCESS: new Stage-5 reviewer workspace created at %s\n' "$root"
printf 'Start a distinct Codex session there; do not resume the author.\n'
