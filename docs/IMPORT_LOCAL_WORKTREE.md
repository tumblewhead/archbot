# One-time import of your existing Codex worktree

The GitHub repository was intentionally initialized without claiming that its bootstrap matches your latest local generated proof/evaluation artifacts.

The authoritative current code and knowledge artifacts are on the developer workstation at:
`/home/easy/proj/archbot/progressive-concretization-codex/`.

After cloning the new `archbot` repo to a **different** folder:

```bash
git clone https://github.com/tumblewhead/archbot.git archbot-repo
cd archbot-repo

# Import your actual latest local tree. Source path must be adjusted if needed.
rsync -av --ignore-existing \
  --exclude='.git/' --exclude='.venv/' --exclude='__pycache__/' \
  --exclude='runs/' --exclude='pc-review-*.zip' \
  --exclude='*.pyc' \
  /home/easy/proj/archbot/progressive-concretization-codex/ ./

# Inspect overlap before committing. `--ignore-existing` deliberately
# preserves repository AGENTS.md, README.md and PROJECT_SPINE.md.
git status --short

# You may want to reconcile AGENTS.md and update PROJECT_SPINE.md.
# Add only reviewed, appropriately scoped files and concise run receipts.
git add -A
git diff --cached --stat
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/pc.py check --fast

# Commit/push only when results and source contents have been reviewed.
git commit -m "Import locally validated Codex prototype and evidence"
git push origin main
```

The supplied `rsync` is additive. It does not replace tracked files in the new repository with an older snapshot, and it excludes raw run logs. It may import a large synthetic CSV fixture. Review whether that belongs in Git or should stay external with a manifest.

If the regression remains, inspect `patches/pc-spine-context-regression.patch` and run `git apply --check` before applying it. The patch is based on a snapshot, not guaranteed to match the live tree.

Do not delete the original local working directory until the imported result is validated and pushed.
