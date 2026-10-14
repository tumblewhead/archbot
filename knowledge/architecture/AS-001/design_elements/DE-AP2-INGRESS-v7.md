---
type: Design Element
id: DE-AP2-INGRESS-v7
title: Accepted-sample ingress and operation boundary
status: draft
version: 7
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
---
# DE-AP2-INGRESS-v7

**Purpose and boundary.** Admit one legal unsigned integer sample as one
accepted-sample operation and preserve its acceptance order through the
update boundary. This boundary makes the contract's one-to-one operation
count auditable. The upstream publisher owns uninterrupted ordered delivery;
that remains an external, unverified assumption. This element adds no loss
detection, sequence counter, rate, overload behavior, transport, or hardware
mechanism.

**Interface.** `accept(sample)` has precondition `sample ∈ [0,4095]` and
that the acceptance lifecycle is enabled. It invokes the update exactly
once and returns the result associated with that completed update. Its
postcondition is exactly one operation in the accepted order and a returned
value equal to the newest-32 sum after that operation. Behavior outside the
legal domain is unspecified by contract; this element does not invent a
rejection or recovery response. Any implementation range protection needed
for VO-006 must preserve the domain assumption and be reviewed there.

**Ownership and lifecycle.** It owns no persistent detector history. It
owns only any bounded transient needed to convey the sample and return value;
the concrete call/queue mechanism is left to integration. It accepts no
operation while reset quiescence is in force. Integration must preserve the
contract's ordering and one-to-one publisher boundary without claiming
physical continuity evidence here.

**Composition and verification hooks.** Calls `DE-AP2-UPDATE-v7` once and
returns its corresponding result from `DE-AP2-RESULT-v7`. Correspondence
checks should enumerate accepted calls and show exactly one ordered update
and associated completion value per call. Integration evidence for
publisher continuity, if required, stays external and does not discharge a
detector VO by assumption.
