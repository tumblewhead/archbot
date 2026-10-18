#!/usr/bin/env bash
# Stage 7: prepare source-allowlisted INDEPENDENT review of proposed D003.
# Use real Archbot checkout, not an active Codex workspace.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || {
  echo "STOP: switch to $branch" >&2; exit 1;
}
root="$HOME/archbot-cln001-d003-review-007"
[[ ! -e "$root" ]] || { echo "STOP: reviewer workspace exists; do not reuse" >&2; exit 1; }
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"
s7="reviews/diagnostics/CLN-001-TASK-007"

check_blob() {
  local path="$1" expected="$2" actual
  [[ -f "$path" ]] || { echo "STOP: missing $path" >&2; exit 1; }
  actual="$(git hash-object "$path")"
  [[ "$actual" == "$expected" ]] || {
    printf 'STOP: source blob mismatch %s: %s\n' "$path" "$actual" >&2; exit 1;
  }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s6/D002-INTERFACE-DISPOSITION.yaml" 75dd7cf29529ecf73d8ae0382e1744ab18cbcb23
check_blob "$s6/AP-CANDIDATES-006.md" 6a87f5a8f44c736bf32b19338843b4e3c84f47fd
check_blob "$s6/AP-COMPARISON-006.md" 4ab222da90473b868f5e4432603e05f0b5b88fe2
check_blob "$s6/REVIEW-AP-006.md" 007e8a50bcc639aef07ebda82928aadb276b5821
check_blob "$s6/REVIEW-AP-006.json" c21f87b9e87a31aeae6883bff6f4690e4ef372da
check_blob "$s6/REVIEW_AP006_SHA256SUMS" d4047f0d0a849116d5792b4a2f587c5c97ec907c
check_blob "$s7/D003-PROPOSAL-007.yaml" c907591125d5ec12d8a49c141c6c47ebecea179c
check_blob "$s7/D003-BRIEFING-007.md" 8d40b687a033d10adcf98f2dc56f67ed932197c3
check_blob "$s7/TASK-REVIEW-D003-007.md" 181fedecd15f05880bfb9d19c1e41cd654cb1b03

( cd "$s6" && sha256sum -c REVIEW_AP006_SHA256SUMS )
( cd "$bkp" && printf '%s  %s\n' \
  90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
  284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
  c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c - )

mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$s6/AP-CANDIDATES-006.md" \
  "$s6/AP-COMPARISON-006.md" "$s6/REVIEW-AP-006.md" \
  "$s6/REVIEW-AP-006.json" "$root/inputs/"
cp -- "$s7/D003-PROPOSAL-007.yaml" "$s7/D003-BRIEFING-007.md" "$root/inputs/"
cp -- "$s7/TASK-REVIEW-D003-007.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 D003 independent authority/source review

Read TASK.md, inputs/SHA256SUMS and only supplied inputs.
You are not the author, delegate or architecture selector.
The D003 proposal is NOT EFFECTIVE. Do not look up prior solved
Toy 1 AP/CON/DE/C, Git history, other workspaces, external services,
network, connected apps or hidden evaluators.
Write only out/REVIEW-D003-007.md and out/REVIEW-D003-007.json.
Do not amend the AS, approve D003, select an AP or discharge VOs.
This positive allowlist is not a proof of OS/connector isolation.
ROLE
( cd "$root/inputs" && sha256sum -- * | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS )
printf 'SUCCESS: %s\n' "$root"
printf 'Launch FRESH Codex session in that directory, not codex resume.\n'
