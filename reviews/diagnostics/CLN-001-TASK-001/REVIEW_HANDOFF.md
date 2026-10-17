# CLN-001 TASK-001: independent diagnostic Architecture Statement review

**Status:** REVIEW HANDOFF PREPARED / NOT EXECUTED.  
**Branch:** `experiment/toy1-pipe-cleaner-001`.  
**Authoring output commit:** `57c49628dfca12e30315eb7b08f63c478379cc68`.  
**Scope:** pre-freeze Toy 1 pipe-cleaner, *not* formal cleanroom qualification, not an approval of stakeholder requirements.

The authoring run produced three versioned outputs under
`reviews/diagnostics/CLN-001-TASK-001/`:

| File | Pinned Git blob SHA-1 | SHA-256 (human manifest) |
|---|---|---|
| `AS-DRAFT-001.md` | `8310aceec17b5df5922e10b0f1ac4fb23979ffb2` | `e231a55be07631c3c089434ec7502bc9cad833340ef5cd97813d5852372aa9e3` |
| `QUESTIONS-001.md` | `c648bd0e40c36f14f9242f94dceba51f06d3c899` | `6d30b661f3e1542a779ef2a9fdad3eafc8aa6d87cb7e3290f8ac7624162c4fce` |
| `BRIEFING-001.md` | `89a5c3ae8525a54efc9e2b3055e093871002ae77` | `8f30a6f672cc6883fe74cc246bcffa9935ce258a4c639ae834c9b9eda32402de` |

`RUN-NOTES.md` says **runtime filesystem isolation was not independently
verified**; `cleanroom_qualified=false` remains binding. The package
preflight PASS checked file presence/identity, not host or connector
reachability.

## Task and independence contract

Review **only** the first AS draft and the fresh-agent's questions for
fidelity to the original three BKP sources. Do not expose earlier
Toy 1 AS, scope correction, AP, P, F, CON, DE, implementation,
evaluator oracle, accepted reviews or Git history. The reviewer
must be a distinct Codex invocation from the author and must not
edit the original source/draft.

The original source inputs are:
- `knowledge/bkp/problem-origin.md`, Git blob `d5ae64168585475e0307d34c1eab8713ad56615d`
- `knowledge/bkp/adc.md`, Git blob `91321092a99e24c2dee325877a8ea6196e5d1f6e`
- `knowledge/bkp/target.md`, Git blob `052f765d0c72f5d805e9fd49bdb19197ee6aa170`

Only source-derived conclusions may be endorsed as source-derived.
A valid numeric specification or competent list of questions is
**not** stakeholder approval, feasibility evidence, or product verification.

The reviewer should decide:
1. Are C, R and PS complete **as a first draft** and faithful to S1–S3?
2. Does each proposed requirement accurately identify its source and
   authority status, including any unsupported interpretations of cadence,
   startup, acquisition, error/loss cases and memory budget?
3. Does the mathematical specification describe the requested observable
   behavior without selecting an implementation?
4. Are missing stakeholder decisions and next gates stated concretely?
5. Does the author stop at the correct boundary, with no proof, selected
   AP, CON/DE, or implementation masquerading as an approved result?
6. Which changes, if any, block handing the draft to the human?

Return `READY_FOR_HUMAN_QUESTIONS`, `REVISE_DRAFT` or `UNRESOLVED`
for the **diagnostic authoring result only**. Do not return `ACCEPT`
as though protected AS authority or formal review had been conferred.
Indicate whether independent source/identity checks were actually run,
not just copied from the human manifest.

## Reviewer-only workspace preparation

Run in a *new terminal*, with `output` set to the already prepared
package root `/home/easy/archbot-toy1-Q9RnZlCE/package`:

```bash
set -euo pipefail
output="/home/easy/archbot-toy1-Q9RnZlCE/package"
src="$output/workspace"
review_root="$(mktemp -d "$HOME/archbot-as-review-XXXXXXXX")"
mkdir -p "$review_root/inputs" "$review_root/out"

cp -- "$src/projects/CLN-001/knowledge/bkp/problem-origin.md" "$review_root/inputs/"
cp -- "$src/projects/CLN-001/knowledge/bkp/adc.md" "$review_root/inputs/"
cp -- "$src/projects/CLN-001/knowledge/bkp/target.md" "$review_root/inputs/"
cp -- "$src/projects/CLN-001/out/AS-DRAFT-001.md" "$review_root/inputs/"
cp -- "$src/projects/CLN-001/out/QUESTIONS-001.md" "$review_root/inputs/"
cp -- "$src/projects/CLN-001/out/BRIEFING-001.md" "$review_root/inputs/"
cp -- "$src/framework/agents/verification-agent.md" "$review_root/inputs/"
cp -- "$src/framework/playbooks/REVIEW_AS.md" "$review_root/inputs/"

(
  cd "$review_root/inputs"
  printf '%s  %s\n' \
    e231a55be07631c3c089434ec7502bc9cad833340ef5cd97813d5852372aa9e3 AS-DRAFT-001.md \
    6d30b661f3e1542a779ef2a9fdad3eafc8aa6d87cb7e3290f8ac7624162c4fce QUESTIONS-001.md \
    8f30a6f672cc6883fe74cc246bcffa9935ce258a4c639ae834c9b9eda32402de BRIEFING-001.md \
      | sha256sum -c -
)

cat > "$review_root/AGENTS.md" <<'EOF'
# Independent CLN-001 diagnostic reviewer

Read TASK-REVIEW-001.md. Use only the sources in inputs/.
You are not the AS author. Do not search, fetch or load previous Toy 1
solution files, source repository, Git history, saved project memory or
the earlier author's Codex conversation.
Write only out/REVIEW-001.md and out/REVIEW-001.json.
Do not create or approve engineering requirements on behalf of the human.
Record isolation limitations, actual commands, and unsupported claims.
EOF

cat > "$review_root/TASK-REVIEW-001.md" <<'EOF'
# REVIEW-001: independent source-fidelity and authority review

Use inputs/problem-origin.md, inputs/adc.md and inputs/target.md as
the only engineering source inputs. Read the three submitted authoring
artifacts in inputs/ and the generic verification-agent role and
REVIEW_AS playbook in inputs/.

Check first-stage Architecture Statement source fidelity, C/R/PS,
requirements and assumption classification, mathematical statement,
missing decisions, and correct stopping boundary. Do not bring in the
old solved Toy 1 architecture or prior decisions.

Write:
- out/REVIEW-001.md: observations, specific findings and source
  references, requirement/assumption checks, next gate and limits.
- out/REVIEW-001.json: status, diagnostic scope, reviewer invocation
  independence, sources actually inspected, findings, unresolved human
  decisions, cleanroom_qualified=false, product_verified=false,
  and vo_discharged=[].

Status is READY_FOR_HUMAN_QUESTIONS, REVISE_DRAFT or UNRESOLVED.
None conveys final AS acceptance or stakeholder authority. Stop here.
EOF

printf 'Reviewer workspace: %s\n' "$review_root"
find "$review_root" -type f | sort
```

The last two generated instruction files are intentionally **reviewer
instructions**, not the author workspace's `AGENTS.md` or the prior
Toy 1 root. Do not copy the root `PROJECT_SPINE.md` or any file beyond
those explicitly named.

### Launch a distinct Codex reviewer

The reviewer must see only `review_root`, with no access to the prior
package parent, original Git checkout, previous Codex sessions or
connected historical project memory. In a properly restricted
container/VM, set the working directory to `review_root` and launch
a *new* Codex session. A plain `cd` plus `codex` without enforced
filesystem restrictions is a **diagnostic review with unverified
isolation**, not a certified cleanroom.

Reviewer launch prompt:

> Read AGENTS.md and TASK-REVIEW-001.md. Independently review the
> three first-stage Architecture Statement artifacts against the
> three included original BKP sources. Write only the designated
> review outputs, and stop.

After completion, use the **original source checkout terminal** to
copy the two generated reviewer outputs to
`reviews/diagnostics/CLN-001-TASK-001/`, then selectively stage
and push only those files. Keep the author files and SHA256SUMS
unchanged. Inspect the reported status before deciding if the next
human authority decision or a bounded draft correction is appropriate.

## Run outcomes we do *not* claim

- No verified physical container or filesystem isolation yet.
- No validated connector isolation, Codex sandbox permissions or
  hidden agent history isolation.
- No requirement, AS, target or VO acceptance.
- No formal cleanroom FR-005 / FR-006 qualification.
- No human approval to progress past the AS review gate.
