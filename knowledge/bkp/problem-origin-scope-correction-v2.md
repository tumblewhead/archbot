---
type: Provenance Annotation
id: BKP-NEED-001-SCOPE-v2
title: Corrected authority and provenance annotation for toy sample timing
status: draft
version: 2
relations:
  - kind: derived_from
    target: /bkp/problem-origin.md
  - kind: addresses
    target: /architecture/AS-001/statement-v2.md
---
# Provenance annotation (candidate)

The source brief `BKP-NEED-001` explicitly labels itself “invented for the
demonstration.” Its phrase “updated every 1 ms” is therefore demonstration
provenance, not independently established stakeholder authority. The
engineering authority's controlled decision
`AS-001-SCOPE-CORRECTION-001` authorizes a versioned AS correction: process
the newest 32 published samples in order and update once per accepted sample,
independent of elapsed time.

The upstream publisher's responsibility for uninterrupted ordered published
samples is an approved interface boundary. This annotation does not establish
physical ADC acquisition continuity, delivery performance, maximum throughput,
or target real-time capability. Existing source files and prior review records
remain unchanged.

