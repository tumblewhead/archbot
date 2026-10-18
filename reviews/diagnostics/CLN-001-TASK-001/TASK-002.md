# CLN-001 TASK-002: revise the draft Architecture Statement

**Status:** authorized diagnostic authoring task, NOT AS acceptance.
**Role:** architecture-agent. **Project:** CLN-001, synthetic diagnostic only.
**Prior gate:** REVIEW-001 = READY_FOR_HUMAN_QUESTIONS.

## Controlled inputs

- projects/CLN-001/knowledge/bkp/problem-origin.md
- projects/CLN-001/knowledge/bkp/adc.md
- projects/CLN-001/knowledge/bkp/target.md
- projects/CLN-001/out/AS-DRAFT-001.md
- projects/CLN-001/out/QUESTIONS-001.md
- projects/CLN-001/out/BRIEFING-001.md
- projects/CLN-001/process/decisions/DECISION-001.yaml
- framework/agents/architecture-agent.md

The independent diagnostic review established that the first AS is
source-faithful enough for questions. New DECISION-001 records the
explicitly delegated synthetic requirements decisions. It is new
project-owned authority: do not treat its contents as intrinsic to the
old BKP, or pretend the prior draft was already accepted.

## Procedure

1. Read the original BKP and previous draft/questions, then the NEW
   delegated decision record. Trace every revised requirement to BOTH
   its originating BKP candidate and the numbered decision.
2. Write `projects/CLN-001/out/AS-REV-002.md` as a new DRAFT AS=(C,R,PS)
   with a coherent requirement register, adopted synthetic model,
   explicit revised timing R3 and separately tracked R4 detection
   scope/deferment.
3. Keep the observable latest-32 exact sum and startup-zero behavior.
   Define accepted logical sample order, init/reset, output relation
   and invalid input behavior without prescribing an algorithm,
   data structure, C API or integer representation.
4. Create `projects/CLN-001/out/DECISION-TRACE-002.md` listing
   Q1-Q7, disposition of R1-R6/A1-A4, rationale, boundary, and any
   remaining verification obligations and due stage. No inherited
   historical VO identifier is conferred on this new project.
5. Create `projects/CLN-001/out/BRIEFING-002.md` with source
   identities, produced artifacts, limitations and next review gate.
6. Stop. The output is a candidate **not yet independently reviewed
   or accepted**. Do not run Proof Scout, select AP, write CON/DE,
   implement C or cite previous Toy 1 solutions.

## Required distinctions

- Source BKP statement != delegated diagnostic engineering decision.
- Nominal 1 ms arrival cadence != proven hard completion deadline.
- Exact window energy core != full sustained-energy detection function.
- RAM ceiling != measured RAM use or target qualification.
- Review-ready prior draft != accepted engineering baseline.

Permitted writes are ONLY:
`projects/CLN-001/out/AS-REV-002.md`,
`projects/CLN-001/out/DECISION-TRACE-002.md`, and
`projects/CLN-001/out/BRIEFING-002.md`.

No project authority changes may be made by the authoring agent.
A distinct later reviewer must assess fidelity against DECISION-001,
the original BKP and the first draft. The human-delegated diagnostic
decision maker may issue an AS disposition only after that review.
