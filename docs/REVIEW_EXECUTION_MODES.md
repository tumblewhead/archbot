# Registered review execution modes and launch-failure recovery

**Status:** Operating clarification after VC-001 and VR-001. This document
does not retroactively turn failed reviewer launches into successful runs.

## Observed evidence

- `reviews/gates/REVIEW_COMPILER_EVIDENCE-TOY1-VC001-receipt.json`
  records `python tools/task.py run` failed before a reviewer turn. The
  separately recorded independent report directly examined and reproduced
  host C evidence, but there was no successful registered launcher session.
- `reviews/gates/REVIEW_RESOURCE_EVIDENCE-TOY1-VR001-receipt.json`
  independently records a failed reviewer launch with zero completed turns;
  stderr reports read-only filesystem during in-process app-server
  initialization. Its separately recorded direct review inspected (but did
  not reproduce) host resource evidence.

Both are *review orchestration* failures, not evidence that the detector C
or host memory layout is wrong. The precise Codex-internal failure origin
is not proven by these records; a nested-session / read-only sandbox
constraint is an architectural hypothesis, not a confirmed root cause.

## Two explicit modes

| Mode | Where initiated | Operation | Evidence |
|---|---|---|---|
| OUTER_SHELL_LAUNCH | A host shell outside any Codex agent session | `python tools/task.py inspect --manifest ...`, then `python tools/task.py run --manifest ...` | Codex telemetry run ID, exit status, completed turns, actual authored report/receipt |
| CURRENT_AGENT_DIRECT | Already inside a Codex agent invocation | `python tools/task.py inspect --manifest ...`, then `python tools/task.py render --manifest ...`; follow the rendered task in the **existing agent invocation** | Explicit direct invocation identity, inspected sources, actual operations, independent report/receipt; no claim that `task.py run` passed |

**Do not invoke `task.py run` from inside an already running Codex agent
as a reflexive way to execute the current agent's own assigned task.**
That command launches an additional Codex instance, and the current
environment may prohibit such nesting. Render the task, read it, and
carry it out within the current authorized agent invocation instead.

`render` is **validation and prompt output only**; it does not execute
the task, accept its conclusions, or produce a review. The agent must
actually follow the rendered task and author the evidence report.
No mode is an automatic approval or independent review.

## Reviewer independence and failure semantics

- Independent review requires a *different invocation from the author*.
  CURRENT_AGENT_DIRECT qualifies as a candidate independent invocation
  only if it is genuinely separate and its output identifies that fact.
  Renaming the same author or invoking a script does not make it independent.
- The reviewer must explicitly distinguish checks performed, checks read
  from producer logs, and checks not performed.
- A launch that returns nonzero with zero reviewer turns has no
  valid automatic gate output. Mark the launcher run
  `FAILED_BEFORE_REVIEWER_TURN`, retain evidence, and stop that
  automatic route. A separately authored direct review remains a
  distinct auditable event.
- A successful `task.py render` validates the task but does not
  establish that the direct review happened.
- Do not evade read-only sandbox constraints by relaxing security,
  changing home-directory permissions indiscriminately, or forcing
  `--danger-full-access`. Any different authorized runtime must be
  deliberately selected and tested.
- Do not create reviews that claim to be emitted by the registered
  runner if their actual execution was CURRENT_AGENT_DIRECT.

## Safe commands: diagnosis and dispatch

From a host shell:

```bash
set +e
python tools/task.py inspect --manifest process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml
inspect_rc=$?
printf 'inspect exit=%s\n' "$inspect_rc"
```

If inspected inside a running Codex agent, render the actual task
instead of recursively launching another Codex process:

```bash
python tools/task.py render --manifest process/tasks/AUDIT_GENERICITY-PREFREEZE-001.yaml
```

The **existing agent** follows that task and its playbook,
then writes the explicitly authorized versioned output artifacts.
If the human is using an outer host shell with a working Codex CLI,
`task.py run` remains a supported entrypoint; validate results from
`runs/` telemetry and actual review files, not solely its exit code.

The prefreeze audit must measure and distinguish these modes, establish
a reproducible launch strategy for cleanroom agents, and identify any
remaining Codex environment/configuration blocker. This document is
a dispatch clarification, not evidence that either mode has been
qualified for future cleanroom operation.
