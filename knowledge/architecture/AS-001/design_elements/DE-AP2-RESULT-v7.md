---
type: Design Element
id: DE-AP2-RESULT-v7
title: Completed-operation result handoff
status: draft
version: 7
relations:
  - kind: constrained_by
    target: /architecture/AS-001/contracts/CON-AP2-001-v6.md
---
# DE-AP2-RESULT-v7

**Purpose and boundary.** Associate a coherent post-update sum with the
accepted-sample operation whose completion produced it. Keeping the handoff
separate from the rolling state clarifies which result the caller receives
without implying a separately concurrent reader.

**Interface.** The completion path carries an unsigned integer capable of
the full inclusive range `[0,536608800]` (at least 29 value bits). On return
from the accepted-sample operation, the value equals the accumulator after
that operation's update. The result is an operation return/handoff in the
abstract design; no persistent duplicate result field is required by this
element. A concrete implementation may choose a representation that meets
the full-range requirement.

**Ownership and lifecycle.** The update owns the value's mathematical
meaning; this element owns the completion association and transfer to the
caller. Initialization and reset yield zero result before any later sample
can be accepted, as required by CON-AP2-001-v6. Any implementation storage
needed during a call is transient and charged once to its responsible
category. No atomic, publication, separate-reader, or synchronization
guarantee is introduced.

**Verification hooks.** For each accepted operation, compare the returned
value to the reference model's post-update value and the STATE accumulator;
include zero, maximum, startup and wrap cases. A separately concurrent
reader remains outside scope absent new authority.
