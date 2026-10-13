# Independent contract review: TOY1-CON001

**Reviewer:** Independent Verification Agent, current invocation  
**Independence:** Independent of the contract-authoring invocation; the submission receipt identifies its authoring run.  
**Disposition:** `REVISE`  
**Next-stage recommendation:** `CON_REVISION_REQUIRED`

## Revision and authority

Reviewed checkout `16507a3d8bbd9ddbb3e24df72669d32fa9492aef`. The manifest trigger revision `5013f9af7030a0963a63bcc2836693e2361a8adb` exists in history and is an ancestor of this checkout; this review evaluates the submitted artifacts at current HEAD. The approved AP-002 authority record authorizes CON-first decomposition. AD-003 is accepted and remains due before final acceptance. VO-002 through VO-006 remain open; VO-001 is discharged only within its synthetic-domain scope. No authority, obligation, or design-element status is changed here.

The submission receipt's `input_revision` is `3d71ba9b4536ccb9070dee00b4d2281a56cebd9d`, the synchronization-boundary commit immediately preceding the contract submission. The contract files match the submitted revision in history. The differing receipt revision is recorded as provenance, not treated as an input mismatch.

## Findings

### CON-AP2-001 — REVISE: continuity detection boundary

The contract requires the producer to deliver every sample once and in order, and says detected gaps, duplicates, or handoff overruns invalidate the window. It also describes timestamp/order as part of the logical input, but gives no sequence token, timestamp granularity/monotonicity rule, or source guarantee for detecting a missing sample. A producer that silently omits one sample and then resumes with the next value is a minimal case where the detector cannot distinguish a discontinuity from a valid consecutive input if no sequence metadata or reliable overrun signal is provided. Specify either the integration guarantee and its independently checkable evidence, or the sequence/overrun information and detection behavior required at this boundary. Keep physical ADC loss outside the synthetic model unless supported by source evidence.

Target queue capacity, ISR assignment, scheduler choice, and fault channel may be selected during DE refinement: the draft assigns responsible DEs and requires recording and verification before implementation approval. This deferral is acceptable only while the no-loss/order and fault-invalidity semantics above remain explicit and enforceable.

### CON-AP2-002 — REVISE: account for all state under the 72-byte cap

The stated representation consumes 68 bytes for the ring (64), accumulator (4), and at least one byte for the index, leaving at most three bytes below the 72-byte cap. The contract additionally specifies initialization/control state, valid-result state, and continuity-fault state. The AP-002 envelope gives four bytes for “index/control allowance,” but neither artifact maps every specified field to that allowance or says whether any publication/result/fault state is charged instead to the shared-allocation cap. Define the complete persistent field inventory and byte allocation, including ownership/accounting of publication state; show that it fits 72 bytes under the declared allocation model. This is a budget completeness issue, not a demand for measured object layout at CON stage.

PR-002's abstract theorem assumptions are carried correctly: legal 0..4095 inputs, zero initialization, oldest-slot convention, replace-then-advance transition, widened multiplication, and the bounded one-update transient. The contract does not claim C or firmware correctness. VO-005 and VO-006 remain appropriately open.

### CON-AP2-003 — ACCEPT WITH THE ABOVE REVISIONS

The 2048-byte charged-SRAM boundary, category caps (72+64+384+128+128+0+128 = 904 bytes), separate 1024-byte reserve, shared-byte attribution, simultaneous-peak accounting, and no-heap/single-instance/non-nested-ISR assumptions are consistent with the approved C-002 scope and AP-002 envelope. These are allocation commitments, not measured usage. Queue/ISR/scheduler and synchronization choices are named as unresolved integration inputs with owners and a before-implementation evidence checkpoint. No target timing or memory claim is established.

## Coverage and gate result

The coverage matrix maps C-001/C-002/C-003 and R-001/R-002/R-003 to contracts, DE responsibilities, owners, methods, and due stages. It preserves open VO-002 through VO-006 and accepted AD-003. Its mappings do not cure the two contract ambiguities above. The proposed state cap is not yet demonstrably complete for all named state/control fields, and the ingress contract does not make discontinuity detection independently implementable under all allowed integrations.

After correcting these items, the contract set may return for independent review. Platform-specific mechanisms can remain DE integration choices under the conditions stated above. No VO is discharged and no DE is approved by this review.

## Deterministic checks and limits

- `python tools/task.py inspect --manifest process/tasks/TOY1-CON001-REVIEW.yaml` — PASS; manifest/role/playbook/spine/gate controls resolve.
- `python tools/pc.py check --fast` — PASS; 44 concepts, 163 typed links, zero warnings/errors; raw bytes/hash skipped. This is structural validation only.
- No unit tests were run; they do not resolve these contract semantics. No firmware, target configuration, queue implementation, compiler output, linker map, stack report, or target measurements were inspected.

## Reviewed input hashes

See `TOY1-CON001-independent-review-v1.json` for SHA-256 hashes of the manifest, role/playbook, spine, contracts, coverage/submission receipt, authority, ledgers, proof, candidate, verification plan, and resource envelope.
