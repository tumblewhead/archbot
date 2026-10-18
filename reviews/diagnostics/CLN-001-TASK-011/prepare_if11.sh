#!/usr/bin/env bash
# CLN-001 Stage-11 IF11: independently authored NEW interface feasibility evidence.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="$HOME/archbot-cln001-if11"
[[ ! -e "$root" ]] || { echo "STOP: workspace already exists $root" >&2; exit 1; }
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"
s8="reviews/diagnostics/CLN-001-TASK-008"
s9="reviews/diagnostics/CLN-001-TASK-009"
s10="reviews/diagnostics/CLN-001-TASK-010"
s11="reviews/diagnostics/CLN-001-TASK-011"
check_blob() {
 local f="$1" expected="$2" got
 [[ -f "$f" ]] || { echo "STOP: missing $f" >&2; exit 1; }
 got="$(git hash-object "$f")"
 [[ "$got" == "$expected" ]] || { echo "STOP: unexpected source $f $got" >&2; exit 1; }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s6/D002-INTERFACE-DISPOSITION.yaml" 75dd7cf29529ecf73d8ae0382e1744ab18cbcb23
check_blob "$s6/AP-CANDIDATES-006.md" 6a87f5a8f44c736bf32b19338843b4e3c84f47fd
check_blob "$s6/AP-COMPARISON-006.md" 4ab222da90473b868f5e4432603e05f0b5b88fe2
check_blob "$s8/AS-ADDENDUM-008-R1.md" 0357f82bd8754e88aac3c79224cdb2c770e3e0f1
check_blob "$s9/AS-ADDENDUM-008-R1-DISPOSITION.yaml" ae3ab0fc557b0de4b4961a790f6c94f7ddc5acf6
check_blob "$s9/AP-EVALUATION-BRIEFING-009.md" bc02e48daba2f73cf8594ea21eb81a36faf296b5
check_blob "$s10/REVIEW-AP-EVALUATION-010.md" 9987766af48841d1889b8cb282cca5f2105f3ef2
check_blob "$s11/AP-EVIDENCE-DISPOSITION-010.yaml" fd5078fe819e7782e8b1d42e585df5731ea98060
check_blob "$s11/TASK-IF11.md" c4b104804c1b1376c468123439d0947329136063
(cd "$bkp" && printf '%s  %s\n' \
  90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
  284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
  c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c -)
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$root/inputs/"
cp -- "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s6/AP-CANDIDATES-006.md" "$root/inputs/"
cp -- "$s6/AP-COMPARISON-006.md" "$root/inputs/"
cp -- "$s8/AS-ADDENDUM-008-R1.md" "$root/inputs/"
cp -- "$s9/AS-ADDENDUM-008-R1-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s9/AP-EVALUATION-BRIEFING-009.md" "$root/inputs/"
cp -- "$s10/REVIEW-AP-EVALUATION-010.md" "$root/inputs/"
cp -- "$s11/AP-EVIDENCE-DISPOSITION-010.yaml" "$root/inputs/"
cp -- "$s11/TASK-IF11.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 IF11 evidence acquisition role
Read TASK.md and inputs/SHA256SUMS, then only these supplied inputs.
You are the engineer producing NEW conditional feasibility evidence;
do not act as an independent reviewer, sponsor, AP selector or approver.
No solved old Toy1 AP/CON/DE/C, Git history, other workspaces,
connected apps, network or hidden reference solution.
Write ONLY four allowed out/ files. Any model can assume hypothetical
services only when stated; it cannot create an authorized provider.
An allowlisted directory is not OS/connector isolation.
ROLE
(cd "$root/inputs" && sha256sum -- * | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS)
printf 'SUCCESS: IF11 fresh feasibility workspace %s\n' "$root"
