# VO-001 reconciliation and independent authority record

Read AGENTS.md, theory_of_operation.md and agents/verification-agent.md.
Start at the AS spine and inspect the exact sources for C-001, AS-001,
VP-001 and VO-001, including any prior independent AS-review receipts.

Determine whether the C-001 input-domain obligation is already discharged by
independently accepted evidence or still needs acceptance. Do not infer PASS
from a narrative statement, an agent's confidence, or a structural-check PASS.

If accepted evidence exists, prepare a versioned, source-revision-bound receipt
identifying the reviewer, claim, checked evidence and precise scope. If no such
review exists, create an independent review request with an explicit pending
status. Do not forge approval and do not close VO-001 on your own authority.

Propose, but do not silently perform, the resulting
`process/ledgers/vo_ledger.yaml` update. Preserve prior VO definitions and
other review history. Record unresolved obligations and next gate.
