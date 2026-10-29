#!/usr/bin/env bash
# Distinct EGM-P0 source/evidence reviewer. Source allowlist != verified isolation.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
[[ "$(git branch --show-current)" == "work/cln001-integration-c-kernel-harness" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="$HOME/archbot-egm-p0-review-001"
[[ ! -e "$root" ]] || { echo "STOP: reviewer workspace exists $root" >&2; exit 1; }
check_blob() {
  local source="$1" expected="$2" actual
  [[ -f "$source" ]] || { echo "STOP: missing $source" >&2; exit 1; }
  actual="$(git hash-object "$source")"
  [[ "$actual" == "$expected" ]] || { echo "STOP: source mismatch $source" >&2; exit 1; }
}
check_blob experiments/egm_serialization/assess.py 1764be471ef0e789132c2a93286f09972bf9ff82
check_blob experiments/egm_serialization/tests/test_assess.py db21f4a15b83a33859664bf8103531c2229840a9
check_blob experiments/egm_serialization/P0_USER_TEST_REPORT_001.json 099f9c28274e652111f92b572aed9438b1fcde63
check_blob experiments/egm_serialization/p1/REFERENCE.json 91bc07ea4491ad450fca3baf8869d4c218ecd527
check_blob experiments/egm_serialization/p1/TASK_GOLDFISH.md f53a82c03349ace00cb6a07d4e40f6fc71ea4d31
check_blob experiments/egm_serialization/p1/SPINE.md a74c19c5111e2efd0ec5c4f86a16fcaf24f7feff
check_blob experiments/egm_serialization/p1/prepare_p1.sh a6b0e1c4880bd3bdc9c4bebb006f0ca3f03cff06
check_blob experiments/egm_serialization/p1/evaluate_p1.sh 956c7d3a121756889514b77924b45dba8678ef6e
check_blob docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md 5f58749f30df9eca7d8a85eb8b64f7d9b655f2ce
check_blob docs/IMPLEMENTATION_SKELETON_FIRST_001.md 6663144e26949a635d3887fbdccf39158b8e35af
check_blob docs/EGM_GOLDFISH_SERIALIZATION_001.md b84d06847eb8b7a6ca8118df3238a069c053a757
mkdir -p "$root/tests" "$root/inputs" "$root/out"
cp experiments/egm_serialization/assess.py "$root/assess.py"
cp experiments/egm_serialization/tests/test_assess.py "$root/tests/test_assess.py"
cp experiments/egm_serialization/P0_USER_TEST_REPORT_001.json "$root/inputs/"
cp experiments/egm_serialization/p1/REFERENCE.json "$root/inputs/"
cp experiments/egm_serialization/p1/TASK_GOLDFISH.md "$root/inputs/"
cp experiments/egm_serialization/p1/SPINE.md "$root/inputs/"
cp experiments/egm_serialization/p1/prepare_p1.sh "$root/inputs/"
cp experiments/egm_serialization/p1/evaluate_p1.sh "$root/inputs/"
cp docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md "$root/inputs/HARNESS.md"
cp docs/IMPLEMENTATION_SKELETON_FIRST_001.md "$root/inputs/SKELETON.md"
cp docs/EGM_GOLDFISH_SERIALIZATION_001.md "$root/inputs/EGM.md"
cp experiments/egm_serialization/p0_review/TASK.md "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# Independent EGM-P0 checker/reconstruction-source reviewer
Read TASK.md then inputs/SHA256SUMS. Inspect only supplied source files.
Independently reproduce exact tests and challenge authored reference.
No user-equivalent approvals, no Toy1 solution or other workspaces.
Positive allowlist is not OS/network/connector isolation.
Write only out/REVIEW_EGM_P0_001.md and out/REVIEW_EGM_P0_001.json.
ROLE
(cd "$root" && sha256sum assess.py tests/test_assess.py inputs/* | LC_ALL=C sort > inputs/SHA256SUMS)
# Manifest uses root-relative paths; check from root.
(cd "$root" && sha256sum -c inputs/SHA256SUMS)
printf 'PREPARED_EGM_P0_REVIEW %s\n' "$root"
