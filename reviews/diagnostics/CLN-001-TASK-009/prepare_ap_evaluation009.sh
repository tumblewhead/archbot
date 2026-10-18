#!/usr/bin/env bash
# CLN-001 Stage-9 independent AP feasibility evaluator; source-allowlisted inputs.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="$HOME/archbot-cln001-ap-eval-009"
[[ ! -e "$root" ]] || { echo "STOP: reviewer/evaluator workspace already exists: $root" >&2; exit 1; }
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"
s7="reviews/diagnostics/CLN-001-TASK-007"
s8="reviews/diagnostics/CLN-001-TASK-008"
s9="reviews/diagnostics/CLN-001-TASK-009"
check_blob() {
 local p="$1" expected="$2" actual
 [[ -f "$p" ]] || { echo "STOP: missing source $p" >&2; exit 1; }
 actual="$(git hash-object "$p")"
 [[ "$actual" == "$expected" ]] || {
   printf 'STOP: source mismatch %s expected %s found %s\n' "$p" "$expected" "$actual" >&2
   exit 1
 }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s2/DECISION-TRACE-002.md" 6c888449bb321d15b96fd64e600b0bd195a8fd11
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s6/D002-INTERFACE-DISPOSITION.yaml" 75dd7cf29529ecf73d8ae0382e1744ab18cbcb23
check_blob "$s6/AP-CANDIDATES-006.md" 6a87f5a8f44c736bf32b19338843b4e3c84f47fd
check_blob "$s6/AP-COMPARISON-006.md" 4ab222da90473b868f5e4432603e05f0b5b88fe2
check_blob "$s6/REVIEW-AP-006.md" 007e8a50bcc639aef07ebda82928aadb276b5821
check_blob "$s7/REVIEW-D003-007.md" c547568d347567b84d9091f5f66ac92f6edb000c
check_blob "$s8/D003-DISPOSITION-007.yaml" 5e840fe9946e3c6199e2676c7a2df758e8601ba0
check_blob "$s8/AS-ADDENDUM-008-R1.md" 0357f82bd8754e88aac3c79224cdb2c770e3e0f1
check_blob "$s8/REVIEW-AS-ADDENDUM-008-R1.md" 9fe541786dba1e93593f26b56428e50292bd4a6c
check_blob "$s8/REVIEW-AS-ADDENDUM-008-R1.json" acf370ef4b310e70ff6340292cc4b4ddf5f23352
check_blob "$s8/REVIEW_AS_ADDENDUM008_R1_SHA256SUMS" bb3d8574c61859502dc28f6f2e68559b5b071fcb
check_blob "$s9/AS-ADDENDUM-008-R1-DISPOSITION.yaml" ae3ab0fc557b0de4b4961a790f6c94f7ddc5acf6
check_blob "$s9/AP-EVALUATION-SCOPE-009.yaml" c0633c252f52ca0bf50c8f8e8665bc830d83f883
check_blob "$s9/TASK-AP-EVALUATION-009.md" 1570b406bbe1639c16830a01dc94e64fbce73bf8
check_blob "$s9/STAGE9_BRIEFING.md" e516d1353f9c6cdeb4c4966930eaa0e681a67a94
(cd "$s8" && sha256sum -c REVIEW_AS_ADDENDUM008_R1_SHA256SUMS)
(cd "$bkp" && printf '%s  %s\n' \
  90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
  284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
  c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c -)
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$root/inputs/"
cp -- "$s2/DECISION-TRACE-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$root/inputs/"
cp -- "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s6/AP-CANDIDATES-006.md" "$root/inputs/"
cp -- "$s6/AP-COMPARISON-006.md" "$root/inputs/"
cp -- "$s6/REVIEW-AP-006.md" "$root/inputs/"
cp -- "$s7/REVIEW-D003-007.md" "$root/inputs/"
cp -- "$s8/D003-DISPOSITION-007.yaml" "$root/inputs/"
cp -- "$s8/AS-ADDENDUM-008-R1.md" "$root/inputs/"
cp -- "$s8/REVIEW-AS-ADDENDUM-008-R1.md" "$root/inputs/"
cp -- "$s8/REVIEW-AS-ADDENDUM-008-R1.json" "$root/inputs/"
cp -- "$s9/AS-ADDENDUM-008-R1-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s9/AP-EVALUATION-SCOPE-009.yaml" "$root/inputs/"
cp -- "$s9/STAGE9_BRIEFING.md" "$root/inputs/"
cp -- "$s9/TASK-AP-EVALUATION-009.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 Stage-9 independent AP feasibility evaluator
Read TASK.md, inputs/SHA256SUMS and only supplied inputs/.
Independent evaluator, not AP author, candidate reviewer, delegate or selector.
Activated original AS and independently reviewed additive R1 apply.
Explicit index/consumer association obligations apply; physical RI/RN/C-HIST
remain unapproved and unproved. All realized H1-H6 UNKNOWN.
No solved old Toy1 AP/CON/DE/C, other workspaces, Git history, network,
connected apps or hidden solutions. Write ONLY the three requested
out/AP-EVALUATION-009.md, out/AP-EVALUATION-009.json and
out/AP-EVALUATION-BRIEFING-009.md. Do not select AP, approve a contract
or claim target qualification. Positive allowlist is not OS isolation.
ROLE
(cd "$root/inputs" && sha256sum -- * | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS)
printf 'SUCCESS: fresh bounded Stage-9 AP-evaluation workspace %s\n' "$root"
