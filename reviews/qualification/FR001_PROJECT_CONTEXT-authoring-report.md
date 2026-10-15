# FR-001-PROJECT-CONTEXT: authored repair candidate

**Authority:** FR-001-PROJECT-CONTEXT-AUTHORIZATION-001.
**Status:** Source candidate. Remote author has NOT run local Python tests, Codex, builds or cleanroom. Independent review pending.

## Changes

- tools/task.py forwards the task manifest's validated project spine to telemetry.
- tools/telemetry.py requires a declared project spine for manual and registered task runs. It rejects unsafe, missing and adjacent-project context before starting the run.
- Run state includes the spine; role-specific eligible context reporting and review ZIP exports use the recorded spine, not AS-001.
- Old run records without a spine cannot silently export AS-001 role context; use --no-context for those old packets.
- tests/test_telemetry.py covers two disjoint projects, exported-context separation, missing/unsafe spines and sibling-project traversal.
- tests/test_task.py verifies manifest-to-runner spine forwarding.

## Limits

Role-projected context eligibility remains an estimate, not proof of Codex reads. The repository-level snapshot and generic OKF catalog remain broader than project-only input visibility; physical cleanroom isolation requires a future allowlisted workspace. This change does not revise tools/stage_gate.py, tools/pc.py, accepted AS/AP/F/CON/DE, product firmware, historical evidence, VO/AD ledgers or target qualification.

## Locally executable checks, not yet performed

    python -m unittest discover -s tests -p 'test_telemetry.py' -v
    python -m unittest discover -s tests -p 'test_task.py' -v
    python -m unittest discover -s tests -p 'test_genericity_review_route.py' -v
    python -m unittest discover -s tests -p 'test_genericity_audit_route.py' -v
    python -m unittest discover -s tests -p 'test_stage_gate.py' -v
    python tools/task.py inspect --manifest process/tasks/REVIEW_GENERICITY_PREFREEZE-001.yaml

Stop if any test fails; do not manufacture a favorable result. After actual local test evidence is pushed, route a separate independent implementation review before treating FR-001 as qualified. Framework freeze and cleanroom remain unauthorized.
