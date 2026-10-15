# VK-001: Independent verification artifact review

Operations: REVIEW_ERS, REVIEW_VERIFICATION_LADDER, REVIEW_VERIFICATION_RUNG.
Read the exact input SUBMISSION receipt named by trigger.reference. Follow its
artifact pointer and briefing; check hashes and all original authority sources.
The operation is an ordinary independent Codex review, not an automatic approval.

ERS: inspect coverage against actual AS, CON, DE, proofs and open ledgers in both
directions. The supplied inventory is a candidate interpretation, not a trusted
extraction of every requirement. Preserve normative statements; identify omitted
requirements, unsupported additions, and implementation annotation limitations.

PLAN: check model applicability, typed units, domain, quantifier, horizon,
nonvacuity, oracle, budgets and the distinction between scheduling and premises.
All VK-001 methods are MODEL_ONLY. No rung in this slice establishes the project
C binary, hardware, publisher behavior, confidence in an unspecified population,
or full coverage of unknown higher-order interactions. Unplanned claims remain
open; they are not silently marked NOT_APPLICABLE.

EVIDENCE: inspect the concrete calculated results, execution outcomes, witnesses
and bounds, source/model identity, limitations, statistical unit identities and
briefing. Distinguish a bound exceeding capacity from an admissible witness.
Reject budget exhaustion, unsupported methods or invalid models as proof of success.
Do not mistake metadata integrity or a hand-authored adapter for a proof certificate.

Write additive report Markdown and one JSON review receipt under reviews/gates/.
Use this exact common protocol (values shown in angle brackets are placeholders):

```json
{
  "schema": "pc-verification/v1",
  "kind": "REVIEW",
  "mode": "PROJECT",
  "operation": "<the current REVIEW_* operation>",
  "task_id": "<this assigned review task ID>",
  "project_id": "<copy from submission>",
  "spine": "<copy from submission>",
  "subject": {"id": "<copy>", "semantics": "<copy>", "scope": "<copy>"},
  "artifact": {"path": "<copy exact pointer>", "sha256": "<copy and verify>"},
  "reviewed_author_task_id": "<submission task_id>",
  "reviewer_invocation_id": "<this invocation/run identifier>",
  "independent_of_authoring_invocation": true,
  "disposition": "ACCEPT_WITH_CLARIFICATIONS",
  "findings": [],
  "vo_discharged": [],
  "report": "reviews/gates/<versioned report>.md"
}
```

Disposition may be ACCEPT, ACCEPT_WITH_CLARIFICATIONS, REVISE or UNRESOLVED.
Findings have id, severity, summary, source, and required_resolution. Never return
ACCEPT with an unresolved blocking finding. Only claim review independence when
this is a separate invocation. The controller can check references and declared
identity, not prove human or model cognitive independence.

Acceptance here is acceptance of this draft stage for the next scoped activity,
not product acceptance or automatic VO discharge. Preserve all existing VOs.
Do not recurse into tools/task.py run; perform this assigned review directly.
A REVIEW_VERIFICATION_RUNG result is the terminal review of this slice; final
product acceptance and controlled ledger updates remain outside VK-001.
