# Installed engineering projects

This folder is the **project boundary**, not part of Archbot's permanent
engine. Each child `projects/<project_id>/` contains an independent
`project.yaml`, project spine, decisions, implementation and evidence.

A project may be:
- an ordinary copied directory with a valid project manifest;
- an independently maintained Git repository checked out as a submodule;
- a standalone Git checkout copied under `projects/`.

Archbot discovery does **not** require a submodule, and a Git submodule
does **not** confer accepted engineering authority. No project is active by
default. Explicitly select a project for every project-scoped operation.

## Stage-one CLI (source candidate)

From the Archbot repository root:

```bash
python framework/core/project_registry.py list
python framework/core/project_registry.py init ROOT-002
python framework/core/project_registry.py inspect ROOT-002
```

`init` creates only an unsolved scaffold. It does **not** initialize Git,
create a remote repository, register a submodule or approve any baseline,
AP, CON, DE, implementation, VO or independent review.

The existing legacy task/gate/telemetry tools still use legacy paths.
**Do not delete legacy `knowledge/`, `process/`, `reviews/`, or
`implementation/` directories.** The portable project resolver has
not yet been integrated with these programs.

## Using independent Git repositories

When a separate project repository exists, add it from the parent Archbot
checkout using:

```bash
git submodule add <real-project-git-url> projects/AS-001
git add -- .gitmodules projects/AS-001
git diff --cached --stat
git diff --cached
git commit -m "Install AS-001 engineering project as submodule"
```

Use `git submodule update --init --recursive` after cloning Archbot.
Inside the submodule, commit and push project changes first. Then update
and commit the parent repo's submodule Gitlink. Do not invent a remote URL.

The authoritative Toy 1 identifier today is `AS-001`, including the
hyphen. Keep that identity unless a separately reviewed project-ID
migration is approved.

`git submodule deinit` removes the local checkout but leaves the
registration in the parent repository. Removal from `.gitmodules`
and the parent's tracked Gitlink is a separate deliberate action.
Deleting the working directory never erases Git history.

An **actual cleanroom** must omit the old framework repository's Git
history and prior Toy 1 answers, even if the active Toy 1 folder is gone.
