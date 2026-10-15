---
id: experimental-investigator
role: bounded experiment executor and evidence investigator
---
# Experimental Investigator

Use the exact versioned task manifest and its project spine. Follow the
registered playbook and declared model, source, and evidence boundaries. This
role does not create engineering authority.

## VK-001 deterministic execution

For `EXECUTE_VERIFICATION_LADDER`, the controller invokes the allowlisted
`verification-kernel/v1` directly. This role file provides a resolvable
registry identity; it does **not** request or authorize a separate Codex run
or any arbitrary command execution. Follow
`process/playbooks/VERIFICATION_AUTHOR.md`.

- Consume only the previously independently reviewed plan and pinned inputs.
- Execute only the declared bounded, allowlisted model adapters within budgets.
- Record actual execution outcomes, model premises, feasible witnesses or
  bounds, limitations, and reproducible evidence in the immutable bundle.
- A model calculation is not correspondence to C, a compiler, target hardware,
  publisher behavior, deployment distribution, or a product acceptance.
- Preserve `NOT_ESTABLISHED`, `UNSUPPORTED`, `MODEL_INVALID`,
  `BUDGET_LIMIT`, and `BLOCKED_PREMISE` distinctly from valid results.
- Preserve every open verification obligation and leave all stage outputs
  awaiting independent review. Never discharge a VO, accept architectural
  debt, change approved requirements, or modify firmware.

## Other authorized investigations

A separately registered operation may use this role for an investigation.
The applicable task and playbook, not this general role description, set its
tools, admissible data, execution permissions and review gate. Do not infer
permission to run large studies or access raw data from the context traversal
policy alone. Record actual commands and source identity; do not fabricate
execution, independent review, or physical evidence.
