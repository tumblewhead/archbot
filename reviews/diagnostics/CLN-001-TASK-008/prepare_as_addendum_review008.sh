#!/usr/bin/env bash
# Prepare a new source-allowlisted independent AS addendum review (no execution).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="$HOME/archbot-cln001-as-addendum-review-008"
[[ ! -e "$root" ]] || { echo "STOP: fresh reviewer path already exists: $root" >&2; exit 1; }
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"
s7="reviews/diagnostics/CLN-001-TASK-007"
s8="reviews/diagnostics/CLN-001-TASK-008"

check_blob() {
 local path="$1" expected="$2" actual
 [[ -f "$path" ]] || { echo "STOP: missing $path" >&2; exit 1; }
 actual="$(git hash-object "$path")"
 [[ "$actual" == "$expected" ]] || { printf 'STOP: mismatched blob %s expected %s actual %s\n' "$path" "$expected" "$actual" >&2; exit 1; }
}
check_blob "$s1/DECISION-001.yaml" ab85ffd98a08b00ff289bf95a2baba51741cad88
check_blob "$s2/AS-REV-002.md" fd8f89072f4f90522f8c54a649d6da7fa272cf62
check_blob "$s3/AS-ACTIVATION-002.yaml" cab44926ba877376415cf10f96e13d23e7016d60
check_blob "$s4/F-DISPOSITION-003.yaml" 59d6783b4d8440b009bfb006eeef6401c94c70be
check_blob "$s4/PROOF-DISPOSITION-004.yaml" b7387af29628e9f87d3e0269381c1902bb6d6fff
check_blob "$s6/D002-INTERFACE-DISPOSITION.yaml" 75dd7cf29529ecf73d8ae0382e1744ab18cbcb23
check_blob "$s7/D003-PROPOSAL-007.yaml" c907591125d5ec12d8a49c141c6c47ebecea179c
check_blob "$s7/REVIEW-D003-007.md" c547568d347567b84d9091f5f66ac92f6edb000c
check_blob "$s7/REVIEW-D003-007.json" e768428a1dc104a15a2f26e98432e3ea347cc371
check_blob "$s7/REVIEW_D003007_SHA256SUMS" 80d7af64c8f77c1c3a59845e9a9c971a295ca2b4
check_blob "$s8/D003-DISPOSITION-007.yaml" 5e840fe9946e3c6199e2676c7a2df758e8601ba0
check_blob "$s8/AS-ADDENDUM-008.md" 2719cff80295bf4e9eaf9ab99754a72191c295ec
check_blob "$s8/BRIEFING-008.md" 9e106879a2c5efd651a3de2acccec6170cc615da
check_blob "$s8/TASK-REVIEW-AS-ADDENDUM-008.md" 34dd606ecc716663b77abf2c6559a62f3f50c178

( cd "$s7" && sha256sum -c REVIEW_D003007_SHA256SUMS )
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
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s7/D003-PROPOSAL-007.yaml" "$s7/REVIEW-D003-007.md" \
 "$s7/REVIEW-D003-007.json" "$root/inputs/"
cp -- "$s8/D003-DISPOSITION-007.yaml" "$s8/AS-ADDENDUM-008.md" \
 "$s8/BRIEFING-008.md" "$root/inputs/"
cp -- "$s8/TASK-REVIEW-AS-ADDENDUM-008.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# CLN-001 independent additive-AS source review
Read TASK.md, inputs/SHA256SUMS, then supplied inputs only.
Independent reviewer, not delegate, addendum author or architecture selector.
The AS addendum and RI/RN/snapshot services are not accepted.
No old solved Toy1 AP/CON/DE/C, other workspace, Git history,
network, connected apps, hidden reference or evaluator.
Write ONLY out/REVIEW-AS-ADDENDUM-008.md and
out/REVIEW-AS-ADDENDUM-008.json. Stop there.
Positive-allowlist files do not prove OS/connector isolation.
ROLE
( cd "$root/inputs" && sha256sum -- * | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS )
printf 'SUCCESS: source-pinned independent review workspace %s\n' "$root"
