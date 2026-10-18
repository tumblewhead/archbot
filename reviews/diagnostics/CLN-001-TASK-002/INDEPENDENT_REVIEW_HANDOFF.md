# CLN-001 TASK-002: independent AS-REV-002 review

**Status:** REVIEW HANDOFF AUTHORED / NOT EXECUTED.
**Branch:** `experiment/toy1-pipe-cleaner-001`.
**Source commit:** `50abb5f57d4e049825bb565d53f477fc303d08dd`.
**Scope:** Diagnostic requirement/decision fidelity and AS readiness only.
Neither this handoff nor a favorable review is stakeholder AS acceptance.

## Pinned Stage-2 source

| Source file | Git blob SHA-1 | SHA-256 |
|---|---|---|
| `AS-REV-002.md` | `fd8f89072f4f90522f8c54a649d6da7fa272cf62` | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` |
| `DECISION-TRACE-002.md` | `6c888449bb321d15b96fd64e600b0bd195a8fd11` | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` |
| `BRIEFING-002.md` | `b1f5ec18d088ddb75faa25126d346196fc875b7c` | `5761ba769da25df216779e443136e4a9f501e70735369e4e80e62641079589d2` |

Earlier v1 authoring artifacts remain pinned at
`57c49628dfca12e30315eb7b08f63c478379cc68`.
The real independent diagnostic v1 review is recorded at
`e01f91177c20e14f3aea3a11d9025821156dd971` with
`READY_FOR_HUMAN_QUESTIONS`, NOT acceptance. Delegated synthetic
D001 authority is versioned on the experiment branch; do not import
the previous *solved* Toy 1 baseline.

## Prepare separate reviewer workspace

**Run from the Archbot experiment-branch checkout**, in a terminal
separate from any Codex author session. This script creates a stable,
non-reused path. Do not use an unspecified old `$review_root`.

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

review_root="$HOME/archbot-as-review-002"
workspace="$HOME/archbot-toy1-Q9RnZlCE/package/workspace"
stage1="reviews/diagnostics/CLN-001-TASK-001"
stage2="reviews/diagnostics/CLN-001-TASK-002"

test ! -e "$review_root" || {
  echo "STOP: $review_root exists; do not reuse a prior reviewer"
  exit 1
}
test -s "$stage2/AS-REV-002.md"
test -s "$stage2/DECISION-TRACE-002.md"
test -s "$stage2/BRIEFING-002.md"

mkdir -p "$review_root/inputs" "$review_root/out"
cp -- "$workspace/projects/CLN-001/knowledge/bkp/problem-origin.md" "$review_root/inputs/"
cp -- "$workspace/projects/CLN-001/knowledge/bkp/adc.md" "$review_root/inputs/"
cp -- "$workspace/projects/CLN-001/knowledge/bkp/target.md" "$review_root/inputs/"
cp -- "$stage1/AS-DRAFT-001.md" "$review_root/inputs/"
cp -- "$stage1/QUESTIONS-001.md" "$review_root/inputs/"
cp -- "$stage1/BRIEFING-001.md" "$review_root/inputs/"
cp -- "$stage1/DECISION-001.yaml" "$review_root/inputs/"
cp -- "$stage1/TASK-002.md" "$review_root/inputs/"
cp -- "$stage1/REVIEW-001.md" "$review_root/inputs/"
cp -- "$stage1/REVIEW-001.json" "$review_root/inputs/"
cp -- "$stage2/AS-REV-002.md" "$review_root/inputs/"
cp -- "$stage2/DECISION-TRACE-002.md" "$review_root/inputs/"
cp -- "$stage2/BRIEFING-002.md" "$review_root/inputs/"
cp -- "$workspace/framework/agents/verification-agent.md" "$review_root/inputs/"
cp -- "$workspace/framework/playbooks/REVIEW_AS.md" "$review_root/inputs/"

(
  cd "$review_root/inputs"
  printf '%s  %s\n' \
    90d0fe3d56c4eecaae63a7c9291d7e51eec9ccd767b335a07da1109914ce5333 problem-origin.md \
    284d6c28e1566874c07793d5947028f58ec827e1117e94b24052d0024e9627d7 adc.md \
    c42eefa19ff0032d624fc8c92f209e97273bfd41f5744a52d8e785d17cd0ac64 target.md \
    e231a55be07631c3c089434ec7502bc9cad833340ef5cd97813d5852372aa9e3 AS-DRAFT-001.md \
    6d30b661f3e1542a779ef2a9fdad3eafc8aa6d87cb7e3290f8ac7624162c4fce QUESTIONS-001.md \
    8f30a6f672cc6883fe74cc246bcffa9935ce258a4c639ae834c9b9eda32402de BRIEFING-001.md \
    1da2009c5363fcb47e07c9e607d3b024cbe8a11871617e30216f12c03ea55e36 DECISION-001.yaml \
    246918b8d2e9acf29d54b5cde4ed78fe15220cdb04ae818d22d8471d528eba46 TASK-002.md \
    36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830 AS-REV-002.md \
    90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2 DECISION-TRACE-002.md \
    5761ba769da25df216779e443136e4a9f501e70735369e4e80e62641079589d2 BRIEFING-002.md \
    7f6463b5a54278230dbd73c5f49fc68cb4192ca83c48de191b22674f8d3ae1f3 verification-agent.md \
    6f08ad6ddf98a0c25c08bb695da5207a2564631f6eed560499c1efc04b7b0bfa REVIEW_AS.md \
    | sha256sum -c -
)

# Check the actual versioned, separately invoked first reviewer identity.
test "$(git hash-object "$review_root/inputs/REVIEW-001.json")" = \
     "dd12ad934bf7b1e99d80a3da42e1a14ed41c4494"
test "$(git hash-object "$review_root/inputs/REVIEW-001.md")" = \
     "d82a929f204b63124bda3d439147f75ebe3279f7"

cat > "$review_root/AGENTS.md" <<'EOF'
# CLN-001 second independent diagnostic AS reviewer

Read TASK-REVIEW-002.md. Use inputs/ only for technical source
and sponsor-delegate authority. You are a new verification agent, not
the AS author nor the delegated engineering decision-maker.
Do not search for prior solved Toy 1 files, old repo, Git history,
evaluation oracle, or prior author/reviewer conversations.
Write only out/REVIEW-002.md and out/REVIEW-002.json.
Do not approve the AS or proceed to proof/AP/CON/DE/C.
EOF

cat > "$review_root/TASK-REVIEW-002.md" <<'EOF'
# TASK-REVIEW-002: second diagnostic Architecture Statement review

You are separate from the author of AS-REV-002. Use only inputs/.
Compare AS-REV-002.md, DECISION-TRACE-002.md and BRIEFING-002.md
against the three original BKP files, DECISION-001.yaml, the first
draft/questions/briefing, and TASK-002.md.

Check:
1. Every R1-R6/A1-A4 follows both the original BKP and delegated D001.
2. R3 no longer invents a hard deadline from nominal 1 ms cadence.
3. R4 deferred whole-detector behavior is not silently discharged.
4. Reset, accepted ordering, logical output pair, invalid input and
   2048-byte owned RAM boundary are coherent without design selection.
5. Stage 2 stopped at AS revision; no proof, AP, CON/DE or C is claimed.
6. Investigate the provenance discrepancy: the author saw a stale
   UNRESOLVED self-review in its local workspace, while actual
   independently invoked REVIEW-001 is present in inputs/ as a
   separately archived diagnostic question-readiness review.
   Classify any impact accurately. Do not rewrite history.
7. State what source identity, reviewer separation and filesystem
   isolation you actually verified and what remains unverified.

Write ONLY:
- out/REVIEW-002.md: concise findings, original BKP/D001 crosswalk,
  specific change requests, limitations and next gate.
- out/REVIEW-002.json: schema pc-as-review/v1, review_id REVIEW-002,
  gate AS_REVIEW, candidate inputs/AS-REV-002.md,
  disposition READY_FOR_DELEGATED_AS_DISPOSITION, REVISE_DRAFT
  or UNRESOLVED, scoped rationale, findings, exact input identities,
  actual checks, independent-of-authoring claim with limits,
  cleanroom_qualified=false, product_verified=false,
  vo_discharged=[], stakeholder_approval_claimed=false.

READY_FOR_DELEGATED_AS_DISPOSITION does NOT accept or activate the AS.
Only the separately delegated CLN-001 decision maker may issue the
actual diagnostic AS disposition after inspecting this review.
Stop after both files exist; do not invoke a downstream role.
EOF

printf 'Reviewer workspace ready: %s\n' "$review_root"
find "$review_root" -maxdepth 2 -type f | sort
)
```

**Note:** This preparation operates from the existing Archbot checkout,
which contains historical solved data, but places no such data into the
reviewer directory. Actual isolation requires a restricted runtime:
a new `codex` invocation with only `$HOME/archbot-as-review-002`
accessible. `cd` is not a security boundary. If running ordinary
host Codex without isolation, classify this as a **diagnostic**
review with unverified host/connector reachability.

## Launch (new session, not `codex resume`)

```bash
cd "$HOME/archbot-as-review-002" || exit 1
codex
```

Prompt:

> Read AGENTS.md and TASK-REVIEW-002.md. Independently review
> AS-REV-002 against the original BKP and DECISION-001.
> Write both requested review outputs, then stop.

## After reviewer execution

```bash
review_root="$HOME/archbot-as-review-002"
test -s "$review_root/out/REVIEW-002.md" &&
test -s "$review_root/out/REVIEW-002.json" &&
python -m json.tool "$review_root/out/REVIEW-002.json"
```

From the Archbot experiment-branch checkout, only if both actual
files exist and are complete:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
src="$HOME/archbot-as-review-002/out"
dst="reviews/diagnostics/CLN-001-TASK-002"
test -z "$(git diff --cached --name-only)"
for f in REVIEW-002.md REVIEW-002.json; do
  test -s "$src/$f"
  test ! -e "$dst/$f"
  cp -- "$src/$f" "$dst/"
done
python -m json.tool "$dst/REVIEW-002.json" >/dev/null
git add -- "$dst/REVIEW-002.md" "$dst/REVIEW-002.json"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record independent CLN-001 AS revision diagnostic review"
git push origin experiment/toy1-pipe-cleaner-001
)
```

If the reviewer reports `UNRESOLVED` or `REVISE_DRAFT`, preserve
its actual artifacts unchanged. No self-review acceptance, no
automatic AS promotion, no VO discharge, and no formal cleanroom
claim. The coordinator inspects pushed evidence and then makes the
next bounded diagnostic decision as delegated by the human.
