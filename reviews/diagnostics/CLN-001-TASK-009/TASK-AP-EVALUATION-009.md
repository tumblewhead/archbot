# CLN-001 TASK-AP-EVALUATION-009: independent evidence-aware AP feasibility

**Role:** independent AP feasibility evaluator. Not the Stage-6 proposal
author, Stage-6 candidate reviewer, CLN-001 sponsor/delegate, or AP selector.

**Scope:** three unselected AP-006-A/B/C under the accepted original
synthetic AS plus the separately activated `AS-ADDENDUM-008-R1` and
the accepted scoped F, D002 and T1/conditional T2. This task is not
CON/DE/C or hardware qualification. Use ONLY AGENTS.md, TASK.md,
inputs/SHA256SUMS and supplied allowlisted inputs. Do not access old
solved Toy1 AP/CON/DE/C, Git history, other workspaces, connected apps,
network or hidden reference/evaluator.

First read `inputs/AP-EVALUATION-SCOPE-009.yaml` and all supplied
acceptance dispositions. Source hashes establish bytes, not approval;
approval comes from explicitly supplied decision/activation records.

## What to evaluate

1. **Authority and eligibility.** Reconstruct active AS as
   AS-REV-002 + accepted R1 addendum, not a rewritten original.
   H1 exact latest-32 `E_n`, H2 initialization/reset, H3 correct
   consumer-decodable logical `(n,E_n)` with no silent loss, H4
   invalid rejection and observable faults, H5 complete detector
   attributable RAM <=2048, H6 no hardware-FPU dependency.
   No hard 1ms deadline; R4 complete detection remains deferred.
   Distinguish clauses actually established from source-only claims.

2. **Independent numeric feasibility and falsification.** If useful,
   create an inline or ephemeral Python exact-integer oracle using
   ALL accepted valid samples and latest 32 squares. Independently
   model A (ordered raw 31), B (ordered square 31 plus aggregate S,
   correct oldest-first cursor) and C (snapshot service ASSUMED to
   supply exactly the event-bound pre-tail, explicitly hypothetical).
   Challenge A expiry, B stale/wrong-age cursor/reset/coupled update,
   C mixed or wrong-event snapshot; invalid attempts cannot enter
   accepted sequence. Test 1/31/32/33, max, resets, long streams,
   negative/4096/65536 rejections and consumer/result races where
   a concrete model is appropriate. Record seeds/counts/commands and
   sample-size limits. This is *not* a physical system realization.

3. **Index and acceptance feasibility.** For A/B's RI, specify
   what actual consumer knows and a candidate decoder's required
   information; *do not manufacture* one. For C's RN, list exact
   provider/ordinal/transport and lifetime dependencies. Trace
   event acceptance, numeric commitment, resulting owed output,
   reset linearization, delayed output, consumer restart, queue
   saturation and retry identity. Distinguish conditional impossibility
   under an explicit narrow boundary from unknown service feasibility.
   Do not invent a finite epoch or mandatory acknowledgment.

4. **Full resource accounting.** Use AP-COMPARISON's symbolic model,
   e.g. `RAM_peak = max_t [P+S+K+G]`. Include all owned persistent,
   scratch, stack/callees, buffer/queue, index association and
   attributable shared costs, and keep external-only costs separately
   scoped. Report 31 raw slots versus 31 square slots + S versus
   no detector-owned history ONLY as conditional representations.
   Identify nonlinear or length-dependent state. No 47-byte SRAM
   claim from conditional T2 and no phantom-free upstream service.

5. **Figure-of-Merit.** Evaluate three active axes
   `RAM_peak`, `compute_effort`, `device_energy_consumption`.
   Use consistent workload/target and attribution scopes for every
   proposed comparison. Identify typed arithmetic and memory traffic,
   reset, rejection, faults, C snapshot/index costs, pending work.
   Illustrative assumptions MUST be tagged sensitivity models.
   Realized H gates and F remain UNKNOWN where not supported.
   No synthetic numeric target costs or Pareto downselection.

6. **Evidence and decision map.** Per AP and per H gate, distinguish
   CONDITIONAL_SYMBOLIC, FINITE_MODEL, HOST_SPECIFIC, TARGET_SPECIFIC.
   Give falsifiers and an economical sequence of independent next
   experiments to resolve missing decision-relevant evidence.
   Distinguish numerical kernel feasibility from complete observable
   interface feasibility. Carry every T002-2..8 and deferred R4
   obligation forward. Do not select a candidate or accept AD.

## Outputs: write ONLY these 3 files

- `out/AP-EVALUATION-009.md`: separate A/B/C dossiers,
  H1–H6 and obligations table, executable checks actually conducted,
  symbolic F and explicit unknowns, interesting failures/surprises,
  interface/service dependency matrix and decision-relevant next tests.
- `out/AP-EVALUATION-009.json`: structured evidence receipt with
  `evaluation_id: CLN-001-AP-EVALUATION-009`,
  per candidate/gate findings, exact source-hash coverage, independent
  test counts/seeds, evidence levels, F uncertainty, barriers and
  next gate. Include `AP_selected:false`,
  `all_full_interface_gate_PASS:false`,
  `target_verified:false`, `product_verified:false`,
  `formal_cleanroom_qualified:false`, `vo_discharged:[]`.
  Do not claim a compatibility-grade gate PASS from finite models.
- `out/AP-EVALUATION-BRIEFING-009.md`: human-facing,
  source-linked engineering briefing: what changed, relationships
  between information, interface and ownership, surprises,
  unknowns/falsifiers and the next independently reviewable step.

No changes to supplied authority, candidate drafts, code, implementation
or historic evidence. **STOP after all three outputs exist.**
An independent Stage-10 review of evaluation evidence is required
before any separately authorized AP commitment.
