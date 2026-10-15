# VK-001: First runnable ERS, rung planning and model-evidence slice

Status: implementation authored for local regression and independent review.
No tests were run by the authoring assistant. No existing product requirement,
firmware source, accepted review, or VO/AD state is changed by this commit.
Basis: VS-001, VS-002 and the user-approved bounded implementation direction.

## What actually exists

Three deterministic authoring operations and three independent review operations
share `pc-verification/v1`, rather than introducing stage-specific receipt fields:

| Author operation | Output | Independent operation |
|---|---|---|
| DERIVE_ERS | ERS and source-coverage/observation gap map | REVIEW_ERS |
| DESIGN_VERIFICATION_LADDER | Validated hand-authored rung DAG | REVIEW_VERIFICATION_LADDER |
| EXECUTE_VERIFICATION_LADDER | Bounded model evidence and scope-preserving briefing | REVIEW_VERIFICATION_RUNG |

Use the existing `tools/task.py` and `tools/next_task.py` entry points. The new
small task frontend delegates old gates to `tools/task_legacy.py`, which is a
byte-for-byte copy of the previous task.py. This isolates existing policies for
later genericity review; it does not fix every historical project-specific gate.
One shared hook validates the six new operations. Deterministic author operations
do not launch Codex. Independent reviewers still use normal local Codex telemetry.

This is a bounded verification protocol, NOT a completed generic theorem prover.

## Boundaries

The ERS starts from an explicit, hand-authored input inventory. It verifies source
hashes, selectors, one-to-one statement preservation and coverage in both directions
within that inventory. Independent review must check semantic coverage against the
actual AS/CON/DE and ledgers. The kernel cannot detect every omitted English clause.
Implementation observations remain annotations, not normative authority or code proof.

The planner validates candidate rungs and hyperedges supplied in the input. It does
not yet generate models or discover all interactions. Domains, units, states and
statistical assumptions are part of model adapters. There is no arbitrary eval,
shell execution, dynamically loaded plugin, universal SMT backend or C parser.

Execution currently supports only MODEL_ONLY bindings. It never silently treats a
model result as a C-binary, target, deployment or product result. Source identity,
content integrity, sound model semantics, physical correspondence, reviewer
independence and final acceptance are different obligations.

The precise implemented adapters are:
- `window_integer_bound/v1`: conditional exact mathematical integer bound.
- `ring_finite/v1`: complete bounded enumeration of a reduced reference transition,
  including selected mutants and a shifted-queue oracle. Not project C execution.
- `queue_envelope/v1`: exact rational arrival/service-envelope calculation.
- `queue_trace/v1`: discrete admissible witness before modeled service starts.
- `zero_failures/v1`: fixed-sample zero-failure bound with unique sampling units,
  declared iid assumptions, frozen candidate and no adaptive selection.

Unknown methods return UNSUPPORTED. Oversized enumeration returns BUDGET_LIMIT.
Bad units/invalid models yield MODEL_INVALID. None is success. Plans are limited
to 32 rungs and one million total declared case units in this first version.
No-witness-in-prefix is not unbounded safety; an upper bound above capacity is not
itself an actual overflow; independence declarations are not verified by counting IDs.

## Dependencies and result scope

`scheduled_after_result` allows a diagnostic after failure.
`requires_established_claim` currently supports only a fingerprint-bound exact
`FINITE_MODEL_CHECK` result. A different model or nonmatching result blocks the
premise-dependent rung. This is NOT a general logical implication/composition engine.

Every result retains model scope, model hash, concrete diagnostic details and
limitations. `requested_claim_status` stays NOT_DISCHARGED. Artifact review state
stays PENDING. No path in this slice updates product VOs or grants product acceptance.

Each immutable bundle contains artifact.json, briefing.md and receipt.json under
`reviews/verification/<task-id>/`. The briefing is generated from the same typed
record, not an independent status inference. It shows scope, outcome, limitations,
questions and next action. There is no interactive UI yet and no claim that the
briefing improves comprehension. Hypothetical fixture results cannot enter project
gates. This preserves the later without-dialogue/with-dialogue replay experiment.

Output bundles are published under a local directory lock. An interrupted lock
must be inspected before removal. Retrying the same unchanged task returns its
existing artifact; changed inputs require a new task ID. This is local coordination,
not a distributed transaction or security certification.

## Run locally

First run the complete repository regression suite:

```bash
python -m unittest discover -s tests -v
python tools/pc.py check --fast
```

Then exercise the three complete model-only fixture paths. Output directories
must be new; use a different suffix for a deliberate fresh execution.

```bash
python tools/verification_kernel.py demo --fixture process/verification/fixtures/ring.json --out runs/vk001-ring-1
python tools/verification_kernel.py demo --fixture process/verification/fixtures/queue.json --out runs/vk001-queue-1
python tools/verification_kernel.py demo --fixture process/verification/fixtures/statistics.json --out runs/vk001-statistics-1
```

Expected reference outcomes (not a report of execution by the author): ring reset
remains in the ERS despite its omitted observation annotation; reduced correct ring
has 4096 checked transitions and zero mismatches; specified mutants produce model
counterexamples. Cold queue bound is 232 bytes, resumed bound 296, and its replay
requires 260 bytes at 4 ms. Statistics counts ten unique units in one hundred rows,
not one hundred independent trials. Every artifact is FIXTURE and unreviewed.

The fixture demo intentionally uses direct stage calls without synthetic project
approvals. The regression integration test separately exercises the actual registry,
planner and task validation with test-only independent review records in a temporary
directory; it mocks the existing active-baseline verifier only for that synthetic
project. Another test uses the actual Toy 1 entry and real baseline verifier.
No test-created approvals are committed or usable in the real project.

Now draft the real Toy 1 ERS:

```bash
python tools/task.py inspect --manifest process/tasks/TOY1-VERIFY-ERS001.yaml
python tools/task.py run --manifest process/tasks/TOY1-VERIFY-ERS001.yaml
cat reviews/verification/TOY1-VERIFY-ERS001/briefing.md
```

The pinned Toy 1 input is a candidate inventory, not a freshly approved requirements
baseline. It includes C/R clauses plus reset/result contracts, existing source hashes,
open VO-002..VO-006 and a proposed mathematical bound rung. No physical scope is added.
The independent ERS reviewer must identify any omitted source obligations.

Create and run independent ERS review through the existing receipt router:

```bash
manifest="$(python tools/next_task.py emit --receipt reviews/verification/TOY1-VERIFY-ERS001/receipt.json | jq -er '.manifest_path')"
python tools/task.py inspect --manifest "$manifest"
python tools/task.py run --manifest "$manifest"
```

After a favorable review, route its exact review receipt the same way to planning.
Repeat for plan review, execution, and evidence review. No automatic favorable
review is supplied by this commit. The shared review contract and exact example
are in `process/playbooks/VERIFICATION_REVIEW.md`.

REVISE/UNRESOLVED reviews do not advance. For this bounded version, preserve the
review, revise the input candidate as a new file and author a new task ID for the
affected stage. Automatic regeneration/revision routing is not yet implemented.
REVIEW_VERIFICATION_RUNG is terminal here; controlled product evidence synthesis,
new target adapters and VO discharge need their own subsequent work.

## Known limits that remain visible

- Legacy telemetry still has historical context assumptions; deterministic stage
  records are separate from Codex token telemetry, not fabricated token measurements.
- Hashes establish byte identity, not authenticity or correctness of evidence.
- Reviewer invocation fields are traceable declarations, not proof of cognitive
  independence; the checker does not authenticate a person's identity.
- Semantic translation, physical admissibility, true sampling independence and
  human comprehension require independent evidence/review.
- Reference adapters are ordinary reviewed Python calculations, not proof kernels
  with formally checked certificates. Their mathematical scope is explicit.
- The full production C, toolchain, target, stack, integration and F comparison
  are not executed by these model adapters and remain outside their conclusions.

## Changed-file map

`tools/verification_kernel.py`: shared contract and deterministic stages.
`tools/verification_models.py`: isolated domain adapters.
`tools/task.py`: shared dispatcher; old gates preserved in task_legacy.py.
`process/operations.yaml`, `process/loop_transitions.yaml`: registrations/routes.
`process/verification/`: explicit project input and isolated fixtures.
`tests/test_verification_kernel.py`: negative cases and integrated workflow.
`process/playbooks/VERIFICATION_*.md`: author/reviewer operating boundaries.

No new service, distributed broker, frontend, product threshold or firmware feature
is introduced. The next decision should use actual local regression and review
results, not treat this implementation report as an acceptance receipt.
