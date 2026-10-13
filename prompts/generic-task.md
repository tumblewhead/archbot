# Generic Progressive Concretization task

Read `AGENTS.md` and `PROJECT_SPINE.md`.

Read the **assigned task manifest** at the path provided with this run.
If the manifest is missing, stop with `TASK_MANIFEST_REQUIRED` and request
one; do not guess the architecture or the next gate from chat history.

Read your role definition from `agents/` and the operation's approved
playbook from `process/playbooks/`. Follow the architecture spine identified
by the manifest. Use selective relationship traversal plus mandatory
dependency closure; do not bulk-load raw experiments.

Use the current repository state, accepted proof and authority receipts,
and applicable AS/F/VO/AD records. Preserve immutable historical artifacts.
Only make writes explicitly allowed by the task manifest. If an expected
playbook, policy, receipt, or authoritative input is missing, report the
missing dependency and halt that gate; never fabricate approval.

Run the applicable deterministic structural and gate checks, distinguish
their results from mathematical/engineering acceptance, and emit a bounded
review receipt with input revisions, changed artifacts, unresolved obligations,
and the next eligible action.

Do not create a new architecture-specific prompt merely to advance a gate.
