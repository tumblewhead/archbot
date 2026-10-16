# Submodule-first project migration: execution and safety contract

**State:** planned, NOT yet performed. Stage-one project discovery is
a source candidate; the existing Toy 1 authority, working tree and Git
history have not been moved. See
`process/layout/PC_PROJECT_BOUNDARY_001.yaml` and
`process/decisions/PC-PROJECT-SUBMODULE-FOUNDATION-AUTHORIZATION-001.yaml`.

## Why a submodule, not merely a directory

A project should own its **Git history**, its engineering source, and its
approval/review trail. The parent Archbot repo should pin a specific
project commit without needing to contain that project's source history
or accept its engineering decisions. Submodules provide a Gitlink,
not a second status authority. The Archbot engine continues to accept
ordinary project directories, and does not infer acceptance from either
installation form.

```mermaid
flowchart TD
  A[Permanent Archbot framework repo] --> G[Gitlink: exact project commit]
  G --> P[Independent project repository]
  P --> S[Project manifest and spine]
  P --> E[Project decisions, reviews, implementation]
  A --> F[Framework qualification, versioned interfaces]
  S --> X{Explicit project-compatible interface?}
  X -->|yes| F
  X -->|no| B[Fail visibly, no inherited authority]
```

## Phase A: working project installation, no Toy 1 move

The first code slice `framework/core/project_registry.py` supports
`list`, `inspect`, and `init` on `projects/<project_id>/`.
It checks `project.yaml`, relative in-bundle roots, ID equality,
symlinks, declared adapter *paths* (never imports them), and optionally
an existing Gitlink. It can list an empty installation, accept copied
folders, or recognize a checked-out submodule. It does **not** change
`tools/task.py`, `tools/pc.py`, `tools/gates/binding.py`, or the
old Toy 1 evidence paths.

Acceptance: local synthetic tests for an empty project installation,
drop-in project, independent second project, deletion/unregistration by
visible folder disappearance, manifest mismatch, alias rejection,
unreviewed unsolved initializer, and staged local Gitlink identification.
All source/test executions are performed by the human and require a
separate review before acceptance claims.

## Phase B: make a real independent Toy 1 repository

Requires a **real new repository** and an explicit authority/migration
record preserving original source identities. The connected GitHub
tooling here does not currently expose repository creation. The human
may create that repository, then provide the real clone URL.

Do not manually manufacture a fake `.gitmodules` URL or silently
rewrite the accepted Toy 1 review receipts. Before first extraction,
create a file-level ownership mapping for mixed
`process/decisions/`, `process/tasks/`, `reviews/`,
`tools/gates/`, `tests/`, `prompts/` and `docs/`.

The old source identity of a reviewed file stays:
`(archbot repository, old commit, old path, digest)`.
After extraction a newly submitted project file gains a new identity:
`(Toy 1 repository, new commit, new path, digest)`. An explicit
migration mapping links them; equivalence must be checked, not assumed.
This protects FR-003's source-time evidence semantics.

Recommended staged sequence, each with a local test/review gate:
1. Create a separate Toy 1 repository with project-local
   `project.yaml`, `PROJECT_SPINE.md`, all owned BKP/AS/P/AP/CON/DE
   sources, project decisions/VO/AD and reviews, implementation,
   domain validators and tests. Keep legacy originals unchanged.
2. Commit/verify the project-owned source snapshot and its migration
   map. No source approval or VO discharge is implied by copying.
3. Add the real repository as a Git submodule at
   `projects/AS-001`. The parent pins the project commit.
4. Update generic task/context/gate/verification routes to accept
   an explicit selected project root, while preserving legacy historical
   review lookups at their original commit and paths.
5. Run the old Toy 1 accepted canaries, new second-project isolation
   canaries, and portable drop/unload/reload tests.
6. Independently review the migration before removing the old *active*
   paths. Never rewrite archived original receipts or acceptance records.

## Phase C: usability acceptance, not file-renaming theater

The measurable finish line is:
- Fresh Archbot clone with **no projects** has no active project.
- Add a new ordinary folder or existing submodule, then inspect its
  manifest with no engine source edit or global project registry edit.
- Install two distinct projects, select either explicitly, and observe
  no cross-project context or accepted-authority leakage.
- Unload the first project without affecting the second.
- Create a genuinely unsolved third project with empty accepted-state
  fields and no prior solution history.

For a managed submodule, `git submodule deinit` removes its
checkout but retains parent registration; deleting folder contents
is **not** the same as deregistering the Gitlink. For a plain folder,
removing it removes the visible active project but not remote/backed-up
copies. Document both lifecycle behaviors honestly.

## Relation to FR-004, FR-005 and FR-006

FR-004 qualifies only the reviewer execution mode the process needs.
FR-005 produces an independently evaluated allowlisted package that
cannot access earlier Toy 1 answers, Git history, or evaluator material.
FR-006 decides whether the integrated framework is ready to freeze.
A plain project installation or submodule is a **distribution choice**,
not a cleanroom boundary.

Source migration and integration steps beyond Phase A need their own
local evidence and explicit review/authorization before destructive moves.
