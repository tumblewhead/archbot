# CLN-001 TASK-FOM-003: fresh Figure of Merit scoping

**Role:** Figure-of-Merit specification analyst, not project decision
maker, reviewer or architecture selector.
**Status:** AUTHORIZED FOM DRAFT ONLY. Not acceptance of F.
**Project:** synthetic CLN-001 diagnostic.
**Authoritative inputs:** `inputs/` only. No old solved Toy 1 F,
candidate AP, resource calculations, measured results or reviewer
oracle. Do not browse source repositories.

## Task

1. Construct a **fresh proposed F** grounded in `AS-REV-002.md`,
   `DECISION-001.yaml`, original BKP, and trace obligations.
   Separate feasibility gates from optimization metrics and
   unquantified interests:
   - hard observable exactness/reset/invalid sample correctness;
   - hypothetical 2048-byte detector-attributable RAM ceiling,
     counting persistent state, scratch and owned stack;
   - no hardware FPU dependency;
   - one output per valid accepted sample; nominal 1 ms is **not**
     a declared hard WCET deadline;
   - compute effort and energy/resource minimization as qualitative
     aims until justified measurable objectives or target chosen;
   - deferred full sustained-energy detection R4 excluded from
     primitive completion but tracked as unresolved integration.
2. For each proposed axis state unit, optimization direction,
   allowed model, source requirement, admissible evidence type,
   current value or `UNKNOWN`, and due stage for real target claims.
   Do not assert numerical flash, cycles, stack, RAM or power
   measurements.
3. Define how symbolic resource/performance expressions (conditional
   estimates) and later target-specific measurements would be
   compared *without changing the underlying objectives*. Unknowns
   stay UNKNOWN, never PASS or zero. If weights/trade-off coefficients
   are absent, use a constraint-first Pareto/partial-order proposal,
   not invented weights or a fabricated ranking.
4. Explain how the eventual architectural-proposal candidates may be
   compared reversibly using F, and what information is not yet
   available. Do **not** choose or sketch a favored implementation
   or pre-supply the older Toy 1 solution.
5. Maintain an explicit obligation crosswalk to trace T002-2..T002-8
   and separate numeric-primitive claims from whole-detector claims.
6. Call out every *new proposal* distinct from the user-delegated
   D001 authority; never silently elevate your proposed thresholds
   to accepted requirements.

## Output files (ONLY these)

- `out/F-DRAFT-003.md`: candidate F with objective-axis table,
  hard constraints, symbolic/final evidence maturity distinction,
  uncertainty policy, comparison/selection decision rules,
  non-prescriptive examples if necessary, traceability.
- `out/F-TRACE-003.md`: source provenance/hashes, unresolved choices,
  explicit proposed-vs-authorized boundary, open evidence obligations,
  reviewer/authority gate needed before F acceptance.

**Forbidden:** making F binding, changing D001/AS, selecting AP,
asserting implementation/hardware feasibility, using older Toy 1 F
or AP values, proof acceptance, code generation or writing outside
`out/`.

**Stop** after both files. No subsequent role.
