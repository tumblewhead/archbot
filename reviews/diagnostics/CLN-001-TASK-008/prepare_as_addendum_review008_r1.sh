#!/usr/bin/env bash
# Prepare a distinct independent R008-3 focused review; no local tests run here.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="$HOME/archbot-cln001-as-addendum-review-008-r1"
[[ ! -e "$root" ]] || { echo "STOP: workspace exists; no reviewer reuse: $root" >&2; exit 1; }
bkp="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/knowledge/bkp"
s1="reviews/diagnostics/CLN-001-TASK-001"
s2="reviews/diagnostics/CLN-001-TASK-002"
s3="reviews/diagnostics/CLN-001-TASK-003"
s4="reviews/diagnostics/CLN-001-TASK-004"
s6="reviews/diagnostics/CLN-001-TASK-006"
s7="reviews/diagnostics/CLN-001-TASK-007"
s8="reviews/diagnostics/CLN-001-TASK-008"
check_blob() {
 local file="$1" expected="$2" got
 [[ -f "$file" ]] || { echo "STOP: missing $file" >&2; exit 1; }
 got="$(git hash-object "$file")"
 [[ "$got" == "$expected" ]] || { echo "STOP: Git source mismatch $file $got" >&2; exit 1; }
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
check_blob "$s8/REVIEW-AS-ADDENDUM-008.md" 0223d0f0ae69973c113a32b1755fd59bce8cdf2c
check_blob "$s8/REVIEW-AS-ADDENDUM-008.json" d12577016390bf3a52ca4539331547ca53777f6c
check_blob "$s8/REVIEW_AS_ADDENDUM008_SHA256SUMS" c49c6ab867087b3e11088b4bdc1e7df42bdbd2e2
check_blob "$s8/AS-ADDENDUM-008-R1.md" 0357f82bd8754e88aac3c79224cdb2c770e3e0f1
check_blob "$s8/R008-3-CORRECTION-NOTE.md" b019624e27c605bff855dda53aa10ed5adf62174
check_blob "$s8/TASK-REVIEW-AS-ADDENDUM-008-R1.md" 9f8edf5b05bec7545993b0677b7085387c79dab4
(cd "$s7" && sha256sum -c REVIEW_D003007_SHA256SUMS)
(cd "$s8" && sha256sum -c REVIEW_AS_ADDENDUM008_SHA256SUMS)
(cd "$bkp" && printf '%s  %s\n' \
  90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
  284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
  c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
  | sha256sum -c -)
python3 - "$s8/AS-ADDENDUM-008.md" "$s8/AS-ADDENDUM-008-R1.md" <<'PY'
from pathlib import Path
import sys
a=Path(sys.argv[1]).read_text(encoding="utf-8")
b=Path(sys.argv[2]).read_text(encoding="utf-8")
title0="# CLN-001 proposed AS addendum 008: index supply and event lifecycle"
title1="# CLN-001 proposed AS addendum 008-R1: index supply and event lifecycle"
old="""The eventual physical contract must identify reset order and
acknowledgment at the consumer boundary, and prove that old in-flight
outputs cannot alias new ones."""
new="""The eventual physical contract must establish consumer-visible reset
ordering and unambiguous association between old and new sequences,
and prove that old in-flight outputs cannot alias new ones. A distinct
acknowledgment event is optional, not required; any chosen mechanism
must establish the required observable ordering and association."""
if a.count(title0)!=1 or a.count(old)!=1:
    raise SystemExit("STOP: original text mismatch")
expected=a.replace(title0,title1,1).replace(old,new,1)
if b!=expected:
    raise SystemExit("STOP: R1 contains edits outside the title and S28")
print("PASS: R1 exact correction only")
PY
mkdir -p "$root/inputs" "$root/out"
cp -- "$bkp/problem-origin.md" "$bkp/adc.md" "$bkp/target.md" "$root/inputs/"
cp -- "$s1/DECISION-001.yaml" "$root/inputs/"
cp -- "$s2/AS-REV-002.md" "$root/inputs/"
cp -- "$s3/AS-ACTIVATION-002.yaml" "$root/inputs/"
cp -- "$s4/F-DISPOSITION-003.yaml" "$s4/PROOF-DISPOSITION-004.yaml" "$root/inputs/"
cp -- "$s6/D002-INTERFACE-DISPOSITION.yaml" "$root/inputs/"
cp -- "$s7/D003-PROPOSAL-007.yaml" "$s7/REVIEW-D003-007.md" "$s7/REVIEW-D003-007.json" "$root/inputs/"
cp -- "$s8/D003-DISPOSITION-007.yaml" "$s8/AS-ADDENDUM-008.md" \
 "$s8/AS-ADDENDUM-008-R1.md" "$s8/REVIEW-AS-ADDENDUM-008.md" \
 "$s8/REVIEW-AS-ADDENDUM-008.json" "$s8/R008-3-CORRECTION-NOTE.md" "$root/inputs/"
cp -- "$s8/TASK-REVIEW-AS-ADDENDUM-008-R1.md" "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# Focused independent CLN-001 R008-3 reviewer
Read TASK.md and inputs/SHA256SUMS and only supplied inputs.
Not the author, prior reviewer, delegate, architecture selector or evaluator.
Original review REVISE remains immutable; revised addendum NOT ACTIVE.
Do not access solved Toy1 AP/CON/DE/C, other workspaces, Git history,
network, connected apps or hidden reference/evaluator.
Write ONLY out/REVIEW-AS-ADDENDUM-008-R1.md and
out/REVIEW-AS-ADDENDUM-008-R1.json. Do not activate or select.
A directory allowlist does not prove OS or connector isolation.
ROLE
(cd "$root/inputs" && sha256sum -- * | LC_ALL=C sort > SHA256SUMS && sha256sum -c SHA256SUMS)
printf 'SUCCESS: prepared fresh focused review workspace %s\n' "$root"
