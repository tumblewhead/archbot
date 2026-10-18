#!/usr/bin/env bash
# Make a *new* CLN-001 Stage-5 author workspace from pinned inputs.
# Working directory: your actual Archbot Git checkout.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
if [[ "$(git branch --show-current)" != "$branch" ]]; then
  printf 'STOP: expected branch %s\n' "$branch" >&2
  exit 1
fi

root="$HOME/archbot-cln001-interface-005"
if [[ -e "$root" ]]; then
  printf 'STOP: %s already exists. Never overwrite an agent workspace.\n' "$root" >&2
  exit 1
fi

bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s5="reviews/diagnostics/CLN-001-TASK-005"

# Git blob identities must match the approved source versions.
# 'git hash-object' computes an object's ID WITHOUT adding it to Git.
check_blob() {
  local file="$1" expected="$2" actual
  [[ -f "$file" ]] || { printf 'STOP: missing %s\n' "$file" >&2; exit 1; }
  actual="$(git hash-object "$file")"
  if [[ "$actual" != "$expected" ]]; then
    printf 'STOP: %s blob %s, expected %s\n' "$file" "$actual" "$expected" >&2
    exit 1
  fi
}

check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s2/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s5/TASK-INTERFACE-005.md" 42f3fcf6fe9ae8aa5d1dfc4f0e6be7fac7ba0149

# The BKP sources are the original unsolved synthetic project inputs.
(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    | sha256sum -c -
)

# Make a positive-allowlist workspace (not a qualified OS sandbox).
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$s2/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s5/TASK-INTERFACE-005.md" "$root/TASK.md"

cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 Stage-5 interface and theorem-applicability analyst

Read TASK.md and inputs/SHA256SUMS, then only the inputs/ files.
You have no authority to change the accepted diagnostic AS, F or D001.
All option selections are proposals for later human-delegate disposition.
You are not a Proof Engineer, independent reviewer or AP author.
No older solved Toy 1, other repository/workspace, Git history,
connected tools, network or hidden evaluation rubric may be consulted.
Write ONLY out/INTERFACE-OPTIONS-005.md,
out/DECISION-PROPOSAL-005.yaml and out/BRIEFING-005.md.
A separate directory is an input boundary, NOT proven OS isolation.
ROLE

(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'Created source-pinned Stage-5 workspace: %s\n' "$root"
printf 'Next: cd %q && codex (new session, not resume)\n' "$root"
