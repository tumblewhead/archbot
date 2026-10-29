#!/usr/bin/env bash
# EGM P1 diagnostic: positive-allowlist fresh worker package, no reviewer oracle.
# Creating a directory does NOT prove OS/network/connector isolation.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="work/cln001-integration-c-kernel-harness"
[[ "$(git branch --show-current)" == "$branch" ]] || { echo "STOP: wrong branch" >&2; exit 1; }
root="${1:-$HOME/archbot-egm-p1-001}"
[[ ! -e "$root" ]] || { echo "STOP: workspace exists $root; preserve prior work" >&2; exit 1; }
check_blob() {
  local path="$1" expected="$2" actual
  [[ -f "$path" ]] || { echo "STOP: source missing $path" >&2; exit 1; }
  actual="$(git hash-object "$path")"
  [[ "$actual" == "$expected" ]] || { echo "STOP: source identity mismatch $path" >&2; exit 1; }
}
check_blob docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md 5f58749f30df9eca7d8a85eb8b64f7d9b655f2ce
check_blob docs/IMPLEMENTATION_SKELETON_FIRST_001.md 6663144e26949a635d3887fbdccf39158b8e35af
check_blob docs/EGM_GOLDFISH_SERIALIZATION_001.md b84d06847eb8b7a6ca8118df3238a069c053a757
check_blob experiments/egm_serialization/p1/SPINE.md a74c19c5111e2efd0ec5c4f86a16fcaf24f7feff
check_blob experiments/egm_serialization/p1/TASK_GOLDFISH.md f53a82c03349ace00cb6a07d4e40f6fc71ea4d31
# Deliberately DO NOT copy REFERENCE.json or comparator into worker.
mkdir -p "$root/inputs" "$root/out"
cp docs/ARCHBOT_HARNESS_ARCHITECTURE_001.md "$root/inputs/HARNESS.md"
cp docs/IMPLEMENTATION_SKELETON_FIRST_001.md "$root/inputs/SKELETON.md"
cp docs/EGM_GOLDFISH_SERIALIZATION_001.md "$root/inputs/EGM.md"
cp experiments/egm_serialization/p1/SPINE.md "$root/SPINE.md"
cp experiments/egm_serialization/p1/TASK_GOLDFISH.md "$root/TASK.md"
cat > "$root/AGENTS.md" <<'ROLE'
# EGM-P1 fresh Goldfish reconstruction diagnostic
Read SPINE.md, TASK.md and inputs/SHA256SUMS. Read ONLY those inputs.
Reconstruct independently, report UNKNOWN on unsupported assumptions.
Do NOT read original Archbot repo, chat memory, Git history, any other
workspace, evaluator-only REFERENCE.json, connected app or network.
No architecture approval, implementation or Toy1 qualification.
A new directory is not itself an isolated process or OS sandbox.
Write only the two output files requested by TASK.md.
ROLE
(cd "$root/inputs" && sha256sum HARNESS.md SKELETON.md EGM.md > SHA256SUMS && sha256sum -c SHA256SUMS)
printf 'PREPARED_DIAGNOSTIC_ONLY %s\n' "$root"
printf 'AUDITOR_REFERENCE_STAYS_OUTSIDE_WORKER experiments/egm_serialization/p1/REFERENCE.json\n'
