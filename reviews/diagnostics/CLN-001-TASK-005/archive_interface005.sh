#!/usr/bin/env bash
# Restartable archive of original Codex Stage-5 output files.
# Run from the REAL Archbot Git checkout, not from the Codex workspace.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="experiment/toy1-pipe-cleaner-001"
if [[ "$(git branch --show-current)" != "$branch" ]]; then
  printf 'STOP: wrong Git branch; expected %s\n' "$branch" >&2
  exit 1
fi

src="$HOME/archbot-cln001-interface-005/out"
dst="reviews/diagnostics/CLN-001-TASK-005"
names=(INTERFACE-OPTIONS-005.md DECISION-PROPOSAL-005.yaml BRIEFING-005.md)
manifest="STAGE5_OUTPUT_SHA256SUMS"
allowed=("$dst/${names[0]}" "$dst/${names[1]}" "$dst/${names[2]}" "$dst/$manifest")

# A previous attempt may have copied or STAGED some of these files.
# Rather than silently failing, accept identical copies, and reject
# any unrelated staged files. Never rewrite the agent's original bytes.
for name in "${names[@]}"; do
  [[ -s "$src/$name" ]] || {
    printf 'STOP: original agent output missing/empty: %s\n' "$src/$name" >&2
    exit 1
  }
  if [[ -e "$dst/$name" ]]; then
    cmp -- "$src/$name" "$dst/$name" || {
      printf 'STOP: existing repo file differs from agent original: %s\n' "$name" >&2
      exit 1
    }
  else
    cp -- "$src/$name" "$dst/$name"
    printf 'Copied original: %s\n' "$name"
  fi
done
# Confirm the proposal is explicitly still UNAPPROVED.
grep -q 'PROPOSED_NOT_APPROVED' "$dst/DECISION-PROPOSAL-005.yaml" || {
  echo 'STOP: decision proposal does not identify itself as unapproved' >&2
  exit 1
}

# Create a manifest once. On subsequent runs, verify it, don't rewrite.
if [[ ! -e "$dst/$manifest" ]]; then
  ( cd "$dst" && sha256sum "${names[@]}" > "$manifest" )
  printf 'Created %s\n' "$dst/$manifest"
fi
( cd "$dst" && sha256sum -c "$manifest" )

# 'git diff --cached --name-only' lists the INDEX / staging area,
# not all edited files. Reject staged paths outside the intended four.
while IFS= read -r staged; do
  [[ -z "$staged" ]] && continue
  ok=false
  for path in "${allowed[@]}"; do
    [[ "$staged" == "$path" ]] && ok=true
  done
  if [[ "$ok" != true ]]; then
    printf 'STOP: unrelated file staged: %s\n' "$staged" >&2
    exit 1
  fi
done < <(git diff --cached --name-only)

git add -- "${allowed[@]}"
printf '\nStaged evidence for next commit:\n'
git diff --cached --stat

# Git's whitespace style warnings are NOT grounds to modify immutable
# reviewer/author evidence. Report them; preserve exact hashed bytes.
if ! git diff --cached --check; then
  echo 'NOTICE: Git reports whitespace style warnings; original hashed evidence is preserved.'
fi

# 'git diff --cached --quiet' returns 0 if no staged content differs
# from HEAD. That makes this script safe to rerun after a partial push.
if git diff --cached --quiet; then
  echo 'No new staged changes: these exact artifacts are already committed.'
else
  git commit -m "Archive fresh CLN-001 Stage-5 interface applicability analysis"
fi

# Publish commits; repeating an already-successful push is harmless.
git push origin "$branch"
echo 'SUCCESS: Stage-5 original artifacts committed/pushed or already current.'
