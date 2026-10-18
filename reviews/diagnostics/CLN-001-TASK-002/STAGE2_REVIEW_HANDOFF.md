# CLN-001 TASK-002: submitted AS revision and independent review route

**Stage:** second architecture-agent authoring task completed in an external
diagnostic workspace; the three source files have been uploaded to the
coordinator but have **not yet been pushed to the experiment Git branch**.

**Branch:** `experiment/toy1-pipe-cleaner-001`.
**Sponsor-delegate synthetic authority:** `reviews/diagnostics/CLN-001-TASK-001/DECISION-001.yaml`.
**Initial review:** `reviews/diagnostics/CLN-001-TASK-001/REVIEW-001.json`
(`READY_FOR_HUMAN_QUESTIONS`, NOT accepted AS).
**Formal cleanroom:** NOT QUALIFIED.

## Original submitted Stage-2 artifacts

User-uploaded original-file SHA-256 and byte lengths (not text-extracted,
normalized copies):

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `AS-REV-002.md` | `36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830` | 10610 |
| `DECISION-TRACE-002.md` | `90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2` | 10459 |
| `BRIEFING-002.md` | `5761ba769da25df216779e443136e4a9f501e70735369e4e80e62641079589d2` | 6468 |

Do not reconstruct these files by copying text extracted into chat.
Such representations can normalize bytes. **Copy the actual authored
files from the external workspace and verify the original hashes.**

## Preliminary engineering inspection (not independent review)

The author:
- retained the latest-32 exact sum and startup zero padding;
- traced adopted requirements to both original S1/S2/S3 BKP and delegated D001;
- revised R3 from an ambiguous 1 ms update to one result per accepted sample,
  with nominal 1 ms arrivals and no fabricated hard deadline;
- kept R4 whole-detector thresholds, duration and boolean output as a
  tracked deferred integration question, rather than silently passing it;
- defined logical indexing/reset and invalid-input rejection without
  choosing a ring buffer, numeric representation, API, AP, proof or C code;
- retained the hypothetical 2048-byte RAM ceiling, while admitting no
  resource or timing measurements;
- stopped after the authorized three draft outputs.

**Provenance discrepancy:** the authoring workspace's
`projects/CLN-001/out/REVIEW-001.json` was an earlier
`UNRESOLVED` same-invocation self-review. The real separately
invoked `READY_FOR_HUMAN_QUESTIONS` review exists in the experiment
branch at `e01f91177c20e14f3aea3a11d9025821156dd971`, but it
was not inside the authoring workspace. The author accurately reports
the discrepancy as unresolved; do not rewrite those authoring claims.
The next reviewer can inspect BOTH records' identities if needed,
but the earlier self-review is not the authority for TASK-002.
D001 and TASK-002 expressly authorize the revised diagnostic draft;
neither makes it accepted.

## Human push of original Stage-2 artifacts

Run from the **Archbot experiment-branch checkout**, not the external
workspace. Preserve unrelated untracked FR-002 files:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
git pull --ff-only origin experiment/toy1-pipe-cleaner-001

src="$HOME/archbot-toy1-Q9RnZlCE/package/workspace/projects/CLN-001/out"
dst="reviews/diagnostics/CLN-001-TASK-002"
test -z "$(git diff --cached --name-only)"
mkdir -p "$dst"

for n in AS-REV-002.md DECISION-TRACE-002.md BRIEFING-002.md; do
  test -s "$src/$n"
  test ! -e "$dst/$n"
  cp -- "$src/$n" "$dst/$n"
done

(
cd "$dst"
printf '%s  %s\n' \
  36bf5e3fcad1e183a976991943e186bb5cb56d4e9647e7d027e5c70eb89a6830 AS-REV-002.md \
  90bbfc0c1de5333c90015696a3a8dd871a762e6e096cf2ad7328534a1e07acc2 DECISION-TRACE-002.md \
  5761ba769da25df216779e443136e4a9f501e70735369e4e80e62641079589d2 BRIEFING-002.md \
    | tee SHA256SUMS | sha256sum -c -
)
git add -- "$dst/AS-REV-002.md" "$dst/DECISION-TRACE-002.md" \
  "$dst/BRIEFING-002.md" "$dst/SHA256SUMS"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record second Toy 1 AS diagnostic authoring result"
git push origin experiment/toy1-pipe-cleaner-001
)
```

If any hash mismatch occurs, STOP and provide the actual `sha256sum`.
Do not edit the submitted file simply to make the comparison pass.
The copied outputs remain DRAFT.

## The next independent review (only after source push)

Prepare an isolated **new reviewer workspace** with a positive allowlist:

1. The original three BKP files from the existing diagnostic package.
2. `DECISION-001.yaml` from the experiment branch, pinned to the
   sponsor-delegated authority record.
3. `AS-DRAFT-001.md`, `QUESTIONS-001.md` and `BRIEFING-001.md`
   (the initial draft, not its prior hidden solution).
4. The three **now Git-pinned** TASK-002 output artifacts.
5. The real prior independent diagnostic `REVIEW-001.json`, explicitly
   marked not an accepted baseline.
6. Generic `verification-agent.md` and `REVIEW_AS.md`, plus a
   small fresh TASK-REVIEW-002 instruction.

Do not include original solved Toy 1 AS/AP/CON/DE/C, old decisions,
old framework project spine, evaluator oracle or Git history.
The reviewer must be a distinct Codex invocation and must
**not** see the AS author's prior conversation.

Reviewer-specific questions:
- Does the revised R1–R6/A1–A4 register exactly implement the new
  D001 decisions while tracing the original BKP?
- Is the revised R3 truly a deliberate sponsor-delegate decision, with
  no unmeasured deadline smuggled into the AS?
- Is deferred R4 still traceable with a due claim/stage?
- Are the interface, invalid-input and RAM ownership requirements
  coherent without premature algorithm/API design?
- Did the author avoid retroactively rewriting source authority
  or claiming AS acceptance?
- Does the stale local `UNRESOLVED` self-review matter to the validity
  of the **TASK-002 authoring authorization**, given the real external
  `READY_FOR_HUMAN_QUESTIONS` receipt? Distinguish provenance
  documentation issues from substantive source or decision defects.
- Record exactly which input files/hashes and source authority
  were inspected, and which independence/isolation claims remain unverified.

Expected reviewer output is a scoped diagnostic report and JSON receipt
with disposition `READY_FOR_DELEGATED_AS_DISPOSITION`,
`REVISE_DRAFT` or `UNRESOLVED`. No reviewer may autonomously
approve the AS, start Proof Scout or discharge a VO.

The human-delegated engineering decision maker will consider
the actual independent result before issuing an explicit AS
disposition and deciding whether progression into P/F/AP is authorized.

**Not claimed:** formal cleanroom isolation, FR-005/FR-006 completion,
hardware verification, independent acceptance of version 002,
target qualification, AS baseline activation or VO discharge.
