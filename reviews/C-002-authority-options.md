# C-002 authority options memorandum

**Disposition:** Decision requested; AP selection remains stopped at the authority gate. This memorandum proposes an interpretation for authority review. It does not amend AS-001, F-001, or approve either candidate.

## 1. Requirement and ambiguity

AS-001 C-002 states: **“Detector state must fit within 2 KiB SRAM.”** The cited BKP-TARGET-001 note instead describes a **“detector subsystem”** 2 KiB SRAM budget. “State” can mean persistent algorithm-owned storage, while “subsystem” can include other SRAM consumed to operate the detector. Neither phrase defines treatment of stack, interrupt context, shared services, or runtime allocations. VP-001 requires a conservative AP-stage complete-memory budget and margin, with the boundary resolved at the AP gate; final accounting is due at implementation. [^as] [^target] [^vp]

## 2–3. Competing interpretations and accounting consequences

| Option | Charged 2 KiB boundary | Accounting consequence | Review obligation |
|---|---|---|---|
| **A. Detector-owned persistent state** | Persistent algorithm-owned detector state: history, accumulator, index/control state, and any other memory explicitly defined as state. Report call stack, interrupt context, shared services, and other runtime allocations separately. | EP-002's modeled figures are 72 B for AP-001 (including modeled update accumulator) and 76 B for AP-002 (including a modeled square temporary). These leave nominal headroom under this narrow model, but do not establish a complete-state total, margin, or pass; exact representations/layout remain unspecified. | Bound all state introduced by the candidate at AP. At implementation verify concrete objects/map and any memory classified as state. Separate reports for excluded memory must still identify it and its owner; do not present the state subtotal as total subsystem SRAM. |
| **B. Detector-charged subsystem SRAM** | Every SRAM byte charged to detector operation, potentially including persistent state, detector call stack, interrupt context, and relevant shared allocations. Authority must define charging, shared-resource attribution, and nonoverlap/double-counting rules. | Begin with the same 72 B / 76 B algorithm models, then add conservative upper bounds for every in-scope stack, context, and shared allocation. These contributors are not currently bounded, so no complete total or residual margin can be calculated. | At AP provide a candidate-specific complete charged-boundary envelope and margin, with named unknowns and ownership/nonoverlap rules. At implementation reconcile static/map use, stack bounds, interrupt/runtime allocations, and shared-resource accounting; keep relevant runtime bounds through final verification. |

The figures above are EP-002 analytical models, not target measurements. The 2 KiB limit is 2048 bytes; nominal subtraction from the modeled subtotals is not evidence of compliance where charged terms are omitted or unbounded. [^ep] [^vp]

## 4. AP selection and downstream Verification Obligations

C-002 is first assessable at AP. Under either interpretation, AP selection needs a credible conservative envelope and margin for the authorized boundary; the implementation map/static accounting and applicable stack/runtime bounds remain due at implementation. Under Option A, AP-001 and AP-002 still lack a complete state layout, so the present models alone do not clear the AP gate. Under Option B, the presently unbounded non-state contributors make the complete envelope unresolved for both candidates.

VO-002 remains pending and is not discharged by this memo. Once authority rules, its method should be read against that scope: candidate complete envelope at AP, then implementation accounting for the same boundary. Owner, assumptions, acceptance criterion, and any shared-memory accounting convention must be explicit. VP-001 does not permit an omitted unbounded contributor to be treated as zero or `DEFERRED`. EP-002 likewise records C-002 as a blocker until scope is authorized and a complete candidate envelope is reviewed. No candidate may proceed to selection on the strength of the small algorithm subtotal alone. [^vo] [^vp] [^ep]

## 5. Recommendation

Recommend **Option B, detector-charged subsystem SRAM**, with authority defining exactly which stack, interrupt context, runtime, and shared allocations are charged and how shared bytes are attributed without overlap. This best matches BKP-TARGET-001's stated “detector subsystem” budget and gives the 2 KiB limit an operationally useful boundary. This recommendation is not approval; if the engineering authority intends only persistent state, Option A remains a valid explicit ruling, and the subsystem resource envelope should continue to be reported separately.

## 6. Decision required from engineering authority

Choose and authorize one boundary:

1. **Option A:** 2 KiB applies to detector-owned persistent state as defined above; non-state SRAM is reported separately; or
2. **Option B:** 2 KiB applies to all SRAM charged to detector operation, with explicit inclusion, attribution, and nonoverlap rules for stack, interrupt context, runtime, and shared allocations.

Record the chosen interpretation, approver, and decision evidence in the designated decision record. Until that explicit ruling is recorded and independently reviewable, C-002 remains unresolved and **AP architecture selection must not proceed**. The requested `process/decisions/C-002-scope.yaml` is absent from the working tree. `pc-process-v2.patch` contains a proposed `pending_authority` record only; this memorandum does not apply that patch or change any authority status.

## Review receipt

**Claims:** This memo preserves C-002's original wording, describes both plausible accounting boundaries, carries VO-002 forward, and recommends Option B for authority consideration. No stakeholder approval, compliance finding, AP selection, or change to AS-001/F-001 is claimed.

**Inspected:** `AGENTS.md`, `theory_of_operation.md`, architecture-agent role instructions, AS-001 spine projection and statement, BKP target note, VP-001, EP-002, and VO-002. The decision YAML named in the task was not present; the proposed record in `pc-process-v2.patch` was inspected only to establish that it is not a live decision file.

**Not inspected:** Raw data, implementation, compiler output, linker/map files, stack report, target SRAM measurements, and an engineering-authority approval. No `pc.py check` was run because no knowledge-bundle files were changed.

**Unresolved:** Authorized C-002 boundary; candidate-complete memory envelopes; VO-002 independent assessment. AP selection remains blocked.

**Suggested next gate:** Engineering authority records Option A or B and its accounting rules in the designated decision artifact; then an independent review assesses candidate envelopes against that boundary before architecture selection resumes.

[^as]: AS-001, `knowledge/architecture/AS-001/statement.md`.
[^target]: BKP-TARGET-001, `knowledge/bkp/target.md`.
[^vp]: VP-001, `knowledge/architecture/AS-001/verification_plan.md`.
[^ep]: EP-002, `knowledge/architecture/AS-001/evidence/EP-002.md`.
[^vo]: VO-002, `knowledge/architecture/AS-001/verification/VO-002.md`.
