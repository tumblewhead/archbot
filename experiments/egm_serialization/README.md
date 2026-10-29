# EGM-P0: offline serialization reconstruction checker

**Status:** proposed bounded tool and tests, not a mandatory Archbot
gate, independently verified output or qualifying fresh-agent run.

See [EGM design](../../docs/EGM_GOLDFISH_SERIALIZATION_001.md)
and [research roadmap](../../process/roadmaps/EGM_GOLDFISH_001.yaml).

The `assess.py` program makes a deterministic structural comparison
between an **evaluator-only** source-grounded reference and an
independent Goldfish reconstruction. Both are JSON. This is not an
LLM worker launcher, an architecture validator or an authority engine.

## Run local tests

From the repo root:

```bash
python3 -m unittest discover \
  -s experiments/egm_serialization/tests -p 'test_*.py' -v
python3 -m py_compile experiments/egm_serialization/assess.py
```

The tests exercise missing facts, missing edges, missing proof
conditions, misclassified authority, an invented asserted fact,
explicit unknowns, unallowlisted sources, duplicate IDs, duplicate
JSON properties and the three CLI exit statuses. Unit tests must
be run in the intended environment; writing them does not mean
they have passed. A successful test does not validate the completeness
of a real project's source graph.

## Minimal JSON contracts

Evaluator-only reference:

```json
{
  "schema": "pc-egm-evaluator-reference/v0",
  "project_id": "ROOT-002",
  "allowed_source_ids": ["source-CON-1", "source-DE-1"],
  "required_facts": [
    {"id":"CON-1","kind":"CONTRACT","authority":"ACCEPTED",
     "source_ids":["source-CON-1"],"proof_conditions":[]},
    {"id":"DE-1","kind":"MODULE","authority":"PROPOSED",
     "source_ids":["source-DE-1"],"proof_conditions":[]}
  ],
  "required_relations": [
    {"from":"DE-1","type":"IMPLEMENTS","to":"CON-1"}
  ]
}
```

Goldfish output (not allowed to read the reference):

```json
{
  "schema":"pc-egm-goldfish-reconstruction/v0",
  "project_id":"ROOT-002",
  "traversed_source_ids":["source-CON-1","source-DE-1"],
  "facts":[
    {"id":"CON-1","kind":"CONTRACT","authority":"ACCEPTED",
     "source_ids":["source-CON-1"],"proof_conditions":[]},
    {"id":"DE-1","kind":"MODULE","authority":"PROPOSED",
     "source_ids":["source-DE-1"],"proof_conditions":[]}
  ],
  "relations":[{"from":"DE-1","type":"IMPLEMENTS","to":"CON-1"}],
  "unknowns":[]
}
```

Save these as `/tmp/egm-reference.json` and
`/tmp/egm-goldfish.json` **outside the fresh worker workspace**,
then run:

```bash
python3 experiments/egm_serialization/assess.py \
  --reference /tmp/egm-reference.json \
  --reconstruction /tmp/egm-goldfish.json
```

Exit codes: `0` structural match, `1` structural discrepancy,
`2` malformed/out-of-scope input. The program prints a JSON
finding record. `semantic_review: NOT_PERFORMED`,
`authority_accepted: false`, and
`runtime_isolation_verified: false` remain explicit even at 0.

## Experiment boundary and leaks

The reference is an **evaluator-side oracle**, not a source of truth
for the Goldfish. Build it by independent source-grounded review,
record its source identities, and verify its accuracy before
interpreting discrepancies. Do **not** mount its file or metadata
as part of the Goldfish context projection.

The tool assumes a separate preparer already verifies source hashes,
dependency traversal, and the permitted input manifest. Its
`source_ids` fields are *identifiers*, not cryptographic
authenticators. A match detects omissions only among the facts
and edges that the reference explicitly names. Absence from the
reference is **not** proof of irrelevance; unexpected facts require
semantic review, not automatic rejection of otherwise valid evidence.
The checker does not prove any material outside the reference, nor
does it verify filesystem, network or connector isolation.

Use a fresh Goldfish with independently recorded runtime identity
for the *real* P1 experiment. Do not use a chat-session reset as
a substitute for controlled isolation. The P0 tool can run fully
offline with Python standard library only.
