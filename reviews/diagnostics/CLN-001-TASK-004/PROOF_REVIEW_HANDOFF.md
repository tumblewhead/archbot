# CLN-001 Stage 4: independent review of the conditional proof

**Proof attempt archived:** `2026cb251353285d8fe63671b9ce2b25c9fa9be6`
on `experiment/toy1-pipe-cleaner-001`.

- `PROOF-ATTEMPT-004.md`: blob
  `005c57a539369cb4e62699a7a806974a81eb235b`;
  SHA-256 `be8ac09d8252a8b14accb9a9baafcc0bea2f091c12286a52ef0f409586345c99`.
- `PROOF-BRIEFING-004.md`: blob
  `24c8fafa4fdeefdc541972aa3de0f10ffc262ad0`;
  SHA-256 `ce7c29202141e68c6c99e919efe454112958ae61e97d2d1a9638eeb93654ae9a`.
- Manifest: `reviews/diagnostics/CLN-001-TASK-004/PROOF004_SHA256SUMS`,
  blob `1a6c97d97117d9e1e3b38906681d96ce1d3afa2e`.

**Author's classification: CLAIMED_PROOF_PENDING_REVIEW.**
No theorem is accepted yet. The author independently derived T1
(the last 31 samples determine every future numeric output under
the exact contract) and T2 (2^372 distinct complete retained
states under a deterministic no-replay information boundary).
The reported finite supplemental checks do not prove a universal
statement. They are useful bounded indexing canaries only.

This proof does **not** establish a 47-byte realization, total
RAM use, hardware correctness, complete sustained-energy
detector, exact unbounded indexed interface, timing or power.
It does not prove PO-003-3, and no obligations are discharged.

## Create new review directory (one command)

From your actual Archbot experiment checkout:

```bash
git switch experiment/toy1-pipe-cleaner-001
git pull --ff-only origin experiment/toy1-pipe-cleaner-001
bash reviews/diagnostics/CLN-001-TASK-004/prepare_proof_review004.sh
```

**The script creates the directory.** It refuses to reuse an
existing directory and checks source blobs/hashes before
writing the review package:

```text
~/archbot-cln001-proof-review-004/
  AGENTS.md
  TASK.md
  inputs/
    SHA256SUMS
    original BKP, D001, accepted AS/ACT, PO, scoped review,
    TASK-PROOF-004, PROOF-ATTEMPT-004, PROOF-BRIEFING-004,
    PROOF_REVIEWER_ROLE.md
  out/
```

A separate context-only directory is not a demonstrated OS-level
sandbox. Formal cleanroom qualification remains false.

## Invoke a distinct Proof Reviewer

In a **new** terminal/session, NOT `codex resume`:

```bash
cd "$HOME/archbot-cln001-proof-review-004" || exit 1
codex
```

Prompt:

> Read AGENTS.md and TASK.md. Independently check the
> mathematical proof of PO-003-2 from first principles, especially
> zero-continuation recovery of all 31 tail values and the
> fixed-length state-count lower bound. Check assumptions and
> countermodels, and audit claimed finite checks. Write only
> out/REVIEW-PROOF-004.md and out/REVIEW-PROOF-004.json.
> Return an honest ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE,
> REJECT or UNRESOLVED disposition, then stop.

Reviewer's declared theorem scope is *future numeric outputs for
every nonempty continuation*, not the current output or complete
logical-indexed interface. Check no-replay as a separate conditional
model and do not smuggle it into accepted AS.

## Verify and archive the review

Once **both** files exist, from your original Archbot
experiment-branch checkout:

```bash
(
set -euo pipefail
test "$(git branch --show-current)" = "experiment/toy1-pipe-cleaner-001"
src="$HOME/archbot-cln001-proof-review-004/out"
dst="reviews/diagnostics/CLN-001-TASK-004"

test -z "$(git diff --cached --name-only)"
for name in REVIEW-PROOF-004.md REVIEW-PROOF-004.json; do
  test -s "$src/$name"
  test ! -e "$dst/$name"
done
python -m json.tool "$src/REVIEW-PROOF-004.json" >/dev/null

cp -- "$src/REVIEW-PROOF-004.md" "$dst/"
cp -- "$src/REVIEW-PROOF-004.json" "$dst/"

(
cd "$dst"
sha256sum REVIEW-PROOF-004.md REVIEW-PROOF-004.json > REVIEW_PROOF004_SHA256SUMS
sha256sum -c REVIEW_PROOF004_SHA256SUMS
)

git add -- \
  "$dst/REVIEW-PROOF-004.md" "$dst/REVIEW-PROOF-004.json" \
  "$dst/REVIEW_PROOF004_SHA256SUMS"
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Record independent CLN-001 conditional mathematical proof review"
git push origin experiment/toy1-pipe-cleaner-001
)
```

Do not fabricate a verdict or replace an unfavorable review.
Do not stage unrelated untracked FR-002 files or overwrite the
original proof attempt. After remote push the delegated coordinator
inspects the actual theorem-by-theorem verdict and determines the
next bounded diagnostic stage.

An `ACCEPT` can accept only T1/T2 **under their exact
mathematical assumptions**. It cannot establish implementation
readiness, resource fit, proof of the full indexed interface, or
permit automatic AP/CON/DE/C implementation. The independent
reviewer cannot change D001, accepted F or AS.

**No formal cleanroom, old Toy 1 proof imports or original legacy
VO discharge follows from this stage.**
