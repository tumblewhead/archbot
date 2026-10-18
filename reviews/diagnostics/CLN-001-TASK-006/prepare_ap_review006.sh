#!/usr/bin/env bash
# CLN-001 Stage-6: prepare distinct AP candidate reviewer, source-allowlisted.
# Run in the real Archbot experiment branch checkout. No tests are run here.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || {
  echo "STOP: check out $branch first" >&2
  exit 1
}
root="$HOME/archbot-cln001-ap-review-006"
[[ ! -e "$root" ]] || {
  echo "STOP: $root already exists; do not reuse an author/reviewer session" >&2
  exit 1
}
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"

# Compute blob identities without staging. Stop on stale or altered evidence.
check_blob() {
  local file="$1" expected="$2" actual
  [[ -f "$file" ]] || { echo "STOP: missing $file" >&2; exit 1; }
  actual="$(git hash-object "$file")"
  [[ "$actual" == "$expected" ]] || {
    printf 'STOP: blob mismatch for %s, got %s\n' "$file" "$actual" >&2
    exit 1
  }
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
check_blob "$s6/AP-CANDIDATES-006.md" 6a87f5a8f44c736bf32b19338843b4e3c84f47fd
check_blob "$s6/AP-COMPARISON-006.md" 4ab222da90473b868f5e4432603e05f0b5b88fe2
check_blob "$s6/AP-BRIEFING-006.md" a9ea9ac483f9e868cc7ad841e368896782724e04
check_blob "$s6/AP006_OUTPUT_SHA256SUMS" d0944075e8164d5f2068614d6b6e8d9af5b34479
check_blob "$s6/TASK-REVIEW-AP-006.md" e064094bfe82962cb9c4848ef4fcfa8a23191ab9
check_blob "agents/verification-agent.md" b29c1bff90cefcc7e9bf34a65bcfa9a77bd6c8cb
(
  cd "$s6"
  sha256sum -c AP006_OUTPUT_SHA256SUMS
)
(
  cd "$bkp"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    | sha256sum -c -
)

# Copy source ONLY; the accepted evidence remains in the canonical repo.
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$s2/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$s3/F-DRAFT-003.md" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$s6/TASK-AP-006.md" \
  "$s6/AP-CANDIDATES-006.md" "$s6/AP-COMPARISON-006.md" \
  "$s6/AP-BRIEFING-006.md" "$root/inputs/"
cp -- agents/verification-agent.md "$root/inputs/VERIFICATION_AGENT_ROLE.md"
cp -- "$s6/TASK-REVIEW-AP-006.md" "$root/TASK.md"

cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 Stage-6 independent AP-candidate review

Read TASK.md, inputs/SHA256SUMS and only supplied inputs/.
You are neither Stage-6 AP author nor evaluator/selector nor sponsor.
Keep source math, requirements, scope and project authority separate.
Do not access old solved Toy 1 AP/CON/DE/C, Git history, other
workspaces, connected apps, network, hidden reference solution.
Write ONLY out/REVIEW-AP-006.md and out/REVIEW-AP-006.json.
You cannot approve a candidate, change authority or discharge VOs.
New terminal + directory are not proof of OS/connector isolation.
ROLE
(
  cd "$root/inputs"
  sha256sum -- *.md *.yaml | LC_ALL=C sort > SHA256SUMS
  sha256sum -c SHA256SUMS
)
printf 'SUCCESS: created independent AP-review workspace %s\n' "$root"
printf 'Next: a separate NEW Codex session in this directory.\n'
