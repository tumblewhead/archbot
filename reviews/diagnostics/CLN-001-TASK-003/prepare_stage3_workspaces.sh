#!/usr/bin/env bash
# CLN-001 Stage 3 source-only agent workspace preparation
# This is a pre-freeze diagnostic preparation, not an OS sandbox.
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001" || {
  echo "STOP: wrong branch" >&2
  exit 1
}

author_workspace="$HOME/archbot-toy1-Q9RnZlCE/package/workspace"
source_bkp="$author_workspace/projects/CLN-001/knowledge/bkp"
stage1="reviews/diagnostics/CLN-001-TASK-001"
stage2="reviews/diagnostics/CLN-001-TASK-002"
stage3="reviews/diagnostics/CLN-001-TASK-003"
proof_root="$HOME/archbot-cln001-proof-003"
fom_root="$HOME/archbot-cln001-fom-003"

# Workspaces must be fresh and not recycled between role invocations.
for p in "$proof_root" "$fom_root"; do
  test ! -e "$p" || {
    printf 'STOP: existing directory, will not overwrite: %s\n' "$p" >&2
    exit 1
  }
done

# Preflight source hashes BEFORE creating workspaces.
# BKP files come from the *original diagnostic* unsolved package.
(
  cd "$source_bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c -
)
printf '%s  %s\n' \
  1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36 "$stage1/DECISION-001.yaml" \
  36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830 "$stage2/AS-REV-002.md" \
  90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2 "$stage2/DECISION-TRACE-002.md" \
| sha256sum -c -
test "$(git hash-object "$stage3/AS-ACTIVATION-002.yaml")" = \
  cab44926ba877376415cf10f96e13d23e7016d60
test "$(git hash-object "$stage3/TASK-PO-SCOUT-003.md")" = \
  b4360f74cfb53f1b6d248b7a56f1e7c48f50699e
test "$(git hash-object "$stage3/TASK-FOM-003.md")" = \
  df32ddefa021aafa61a8b2266612c7fc6838fcc1
test "$(git hash-object "$stage2/REVIEW-002.json")" = \
  dcacb5f0d0135940e7410c735c58d4ecf632394e
test "$(git hash-object "$stage2/REVIEW-002.md")" = \
  4b5a8006555f49cdb002a89518c0a7ae96c6f1db

make_workspace() {
  local dest="$1"
  local task="$2"
  mkdir -p "$dest/inputs" "$dest/out"
  cp -- "$source_bkp/problem-origin.md" "$dest/inputs/"
  cp -- "$source_bkp/adc.md" "$dest/inputs/"
  cp -- "$source_bkp/target.md" "$dest/inputs/"
  cp -- "$stage1/DECISION-001.yaml" "$dest/inputs/"
  cp -- "$stage2/AS-REV-002.md" "$dest/inputs/"
  cp -- "$stage2/DECISION-TRACE-002.md" "$dest/inputs/"
  cp -- "$stage3/AS-ACTIVATION-002.yaml" "$dest/inputs/"
  cp -- "$stage3/$task" "$dest/TASK.md"

  cat > "$dest/AGENTS.md" <<'ROLE'
# CLN-001 Stage 3 fresh diagnostic agent
Read TASK.md and its input manifest, then only inputs/.
These are accepted synthetic requirements, not a solved design.
Read no other project, old Toy 1 solution, old Git history or
external sources. Do not use connector/network tools.
Write only the named files in out/. Do not modify any input or
claim an independent proof, measured target fit, AS change,
AP selection, implementation or formal cleanroom.
This is a cooperative pre-freeze diagnostic; directory separation
by itself is NOT runtime/filesystem isolation.
ROLE

  (
    cd "$dest/inputs"
    sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS
    sha256sum -c SHA256SUMS
  )
  printf 'Prepared %s\n' "$dest"
}

make_workspace "$proof_root" "TASK-PO-SCOUT-003.md"
make_workspace "$fom_root" "TASK-FOM-003.md"
printf '\nStage 3 proof and FOM workspaces prepared.\n'
printf 'Proof: %s\n' "$proof_root"
printf 'FOM:   %s\n' "$fom_root"
printf 'Separate Codex sessions must be started by the user.\n'
