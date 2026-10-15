# VK-001 synthetic obligations

These statements are hand-authored framework fixtures, not product requirements.

F-RESET: Initialization establishes the declared zero-history model state.
F-RING: Every transition in the declared finite ring model returns the newest-window squared sum.
F-QUEUE: Queue occupancy fits capacity under the declared arrival, service and initial-state model.
F-RATE: A failure-rate bound applies only to the declared frozen fixed-sample iid-unit model.

The ring fixture deliberately omits a reset observation annotation to test that
an ERS does not drop a normative requirement when implementation annotations omit it.
