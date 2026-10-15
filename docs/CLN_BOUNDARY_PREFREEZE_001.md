# CLN-BOUNDARY-PREFREEZE-001: Toy 1 cleanroom isolation contract (candidate)

**Status:** PROPOSED / NOT IMPLEMENTED / NOT INDEPENDENTLY QUALIFIED.  
**Authority:** Analysis from `GENERICITY_PREFREEZE_001` and independent review
`REVIEW_GENERICITY_PREFREEZE_001` (`ACCEPT_WITH_CLARIFICATIONS`), reviewed at
`500271becada7924fed665aa62e9d1e55f3df11a`. Neither receipt
authorizes framework repair, freeze, or a cleanroom execution.

## Objective and adversary boundary

The first cleanroom Toy 1 must test whether the **generic** Progressive
Concretization process can derive a new solution to an authorized unsolved
problem. It must not be able to read previous Toy 1 answers from a checkout,
revision history, application/search connector, contextual prompt, tool transcript,
environment mount, run log, project spine, test fixture, or evaluation rubric.

**Threat model:** inadvertent cross-project retrieval, inherited authority,
tool default selection, leakage through task prompts/filenames/hashes/metadata,
and deliberate attempts to read an accessible disallowed source. This contract
addresses controllable repository/workspace/tool disclosure, not knowledge
that may already exist in a model's training. A cleanroom run is *not*
authorized by this document.

## Trust domains

| Domain | Agent visibility | Allowed materials | Boundary |
|---|---|---|---|
| Generic engine | Cleanroom author, read/execute only as approved | Frozen, reviewed generic roles, playbooks, task contract, controller, selectors, schemas and declared domain-adapter interface | Must contain no Toy 1 solution constants or selected architecture |
| Fresh project input | Cleanroom author, versioned read | Engineering-authority-provided problem/BKP, constraints, acceptance obligations needed for design, initial unsolved spine and empty VO/AD structures | Cannot import existing AS-001/CON/DE/AP/PR/implementation |
| Task runtime | Cleanroom author, controlled write | Project-local scratch workspace, generated draft/evidence, whitelisted utilities and only explicitly mounted dependencies | No host repository .git history, GitHub connector to original repo, previous ChatGPT/Codex thread, artifact library, parent directory, generic shell escape to old repo |
| Evaluator vault | **Not** cleanroom author-visible | Independent test oracle, acceptance rubric, previous Toy 1 result/evidence for comparison, leakage/sentinel fixtures and review criteria | Access only after submission via separate evaluator identity/process |
| Archive | Auditor-only | Historical source snapshots, prior Toy 1 accepted reviews, reproducibility logs | Preserve unmodified; make inaccessible to cleanroom actor |

**Role separation:** An agent who assembles the approved input package cannot
independently certify that the package is uncontaminated. The evaluator may
inspect both the candidate and forbidden archive; the cleanroom author must
not have that privilege.

## Positive allowlist contract (future packaged input, NOT created here)

A candidate cleanroom package must carry a machine-readable manifest with:
`schema`, unique `project_id`, `framework_revision`,
`problem_revision`, `input_files[{path, sha256, classification, owner}]`,
`task_manifest`, `agent_visible_tools`, `inherited_context_policy`,
`evaluator_vault_ref` (auditor-only), `forbidden_classes`, and
`source_authority_receipts`. References may be listed as **opaque**
identifiers only if their metadata cannot disclose the previous solution.
The packer must reject undeclared files, aliases/symlinks escaping the pack,
path traversal, automatic glob expansion, unpinned remote URLs, and a nested
repository's `.git` that exposes prior history.

Approved classes, subject to independent input review:

- A *new* problem/BKP document supplied by engineering authority, not the
  prior solution or a rephrasing of a previous accepted implementation.
- A reviewed **problem-neutral** generic engine with explicit runtime
  dependencies and task/role/playbook interfaces.
- A *new* minimal project-local `PROJECT_SPINE.md` or equivalent bootstrap,
  initially no selected AP, proof, CON, DE or implementation.
- Project-local policy data needed to interpret the new problem, authored
  independently and explicitly, with no previous Toy 1 solution.
- The cleanroom author's task and its necessary source inputs.

Explicitly excluded from cleanroom author reachability:
`knowledge/architecture/AS-001/`, `implementation/toy1/`, previous
`PROJECT_SPINE.md`, `process/verification/toy1-input-*`, accepted
Toy 1 review receipts, run reports/telemetry, history, prior chat,
numbered pilot prompts that hint at solution architecture, previous agent
scratchpad, and evaluator-only test answers/acceptance decisions.

**Nuance:** The fresh problem may legitimately repeat the user-approved
12-bit domain and newest-32 requirement, because these are *problem inputs*.
The old ring-buffer implementation, PR-002 worked derivation, solution
proposals and downstream decisions are forbidden. Domain constraints alone
are not evidence of solution leakage.

## Verification gates for the boundary

1. **Static allowlist:** independently review the package manifest, file
   hashes, archives, symlinks, Git history, environment mounts, prompted
   task, tool permissions and accessible connectors. Fail closed on undeclared
   inputs. Include a fresh unsolved-project bootstrap.
2. **Two-project canary:** with distinct fake project identifiers and
   disjoint context graphs, assert that context extraction, telemetry,
   stage-gate defaults, and review resolution cannot select AS-001 evidence
   unless the authorized manifest explicitly names that project. The current
   `tools/telemetry.py` and `tools/stage_gate.py` do **not** yet meet this.
3. **Forbidden sentinel:** put a distinctive synthetic token only in an
   auditor-only prior-solution artifact; test that no cleanroom-visible
   file, prompt, connector search, repo history, or tool call can surface it.
   Absence from output **alone** is insufficient; test retrieval visibility.
4. **Reviewer execution identity:** qualify the actual supported launch mode
   with a distinct independent reviewer turn, valid exit status and actual
   artifact receipt. Preserve a failed launch separately. No expectation that
   *both* modes work unless both are explicitly promised.
5. **Freeze only after independent review:** validate unchanged accepted Toy 1
   negative gate tests, archive integrity, scope of remaining VOs, and version
   lock of engine and supplied project inputs.
6. **Cleanroom replay:** *only* after authority to launch. The independent
   evaluator compares against the hidden rubric and archives all measured
   intervention/friction metrics. No such replay has happened.

## Sequencing and non-claims

**Design this boundary early, implement it late.** First parameterize
project/role/spine telemetry and generic gate selection; retain C-002 as a
Toy 1 opt-in domain validator. Separately repair historical verification
identity versus current applicability. Define and qualify the supported
reviewer launch route. Only then construct and test the physical package,
sentinel and cleanroom run.

This document is a proposed boundary and test oracle, **not** evidence
of isolation, package creation, launch success, a frozen framework,
product verification, final F-001 comparison, target selection, VO discharge,
or human approval.
