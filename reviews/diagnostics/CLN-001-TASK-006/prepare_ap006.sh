#!/usr/bin/env bash
# CLN-001 Stage-6: create source-only fresh Proposal Agent workspace.
# Run from the real Archbot experiment-branch checkout.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
if [[ "$(git branch --show-current)" != "$branch" ]]; then
  echo "STOP: checkout must be $branch" >&2; exit 1
fi
root="$HOME/archbot-cln001-ap-006"
if [[ -e "$root" ]]; then
  echo "STOP: $root exists; do not reuse a previous proposal session" >&2; exit 1
fi
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"

# Validate each authority against the Git blob pinned by an earlier gate.
check_blob() {
  local actual
  [[ -f "$1" ]] || { printf 'STOP: missing file %s\n' "$1" >&2; exit 1; }
  actual="$(git hash-object "$1")"
  [[ "$actual" == "$2" ]] || { printf 'STOP: identity mismatch: %s\n' "$1" >&2; exit 1; }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s2/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s3/F-DRAFT-003.md" 5ec007bf45140d415dc105b71cd45c25f434adc2
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s6/D002-INTERFACE-DISPOSITION.yaml" 75dd7cf29529ecf73d8ae0382e1744ab18cbcb23
check_blob "$s6/TASK-AP-006.md" 69f9d844b8e57ad99153aa7ab08a1753382e0778
check_blob "agents/proposal-agent.md" 511474b436e0a0f970d4b28e414d00c3c38027a9

(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c -
)

# These are the ONLY technical sources supplied to the new agent.
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$s2/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$s3/F-DRAFT-003.md" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$root/inputs/"
cp -- "agents/proposal-agent.md" "$root/inputs/PROPOSAL_AGENT_ROLE.md"
cp -- "$s6/TASK-AP-006.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 fresh Stage-6 Proposal Agent

Read TASK.md then inputs/SHA256SUMS and ONLY inputs/.
You have no authority to approve AS, modify D001/D002/F, select AP,
complete proof, implement C, or claim target/cleanroom qualification.
Produce structurally distinct proposals without old solved Toy 1
artifacts, other workspaces, Git history, external sources, network,
connected apps or evaluators. Role is author, not reviewer.
Write only out/AP-CANDIDATES-006.md,
out/AP-COMPARISON-006.md, out/AP-BRIEFING-006.md.
A directory allowlist is NOT an OS-level sandbox.
ROLE
(cd "$root/inputs" && sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS)
printf 'SUCCESS: created %s\n' "$root"
printf 'Launch NEW Codex session, not resume.\n'
