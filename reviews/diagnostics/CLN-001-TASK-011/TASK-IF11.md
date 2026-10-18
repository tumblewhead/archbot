# CLN-001 IF11: acquire concrete consumer/lifecycle feasibility evidence

**Stage:** Evidence acquisition, NOT another review of unchanged UNKNOWNs.
**Role:** independent interface-feasibility engineer (not AP selector,
reviewer, sponsor or delegate). Synthetic pre-freeze diagnostic.

The separately reviewed and delegated accepted AS is original
AS-REV-002 plus AS-ADDENDUM-008-R1. Do not rewrite either.
D002, F, conditional T1/T2 and the Stage-10 evidence disposition
remain controlling. All realized H1-H6 are UNKNOWN, APs A/B/C
UNSELECTED, target qualification absent.

Use ONLY AGENTS.md, TASK.md, inputs/SHA256SUMS and supplied
allowlisted inputs. Do not consult solved old Toy1 AP/CON/DE/C,
other workspaces, Git history, external tools/apps, web or hidden
reference. No accepted RN/C-HIST/RI service exists.

## Required NEW engineering work, not literature review

1. **Specify observable boundaries.** Define explicit mathematical
   traces of publisher attempts, valid acceptance, numerical commit,
   publication, consumer receipt, reset start/completion and consumer
   restart. Identify EXACTLY what each hypothetical component can
   observe/retain and which resources it owns. Distinguish authority
   already supplied by D001/R1 from proposed new operating assumptions.
2. **Construct at least two genuinely different candidate physical
   refinement contracts** for consumer association: e.g. a synchronous
   response with proof obligations on accepted-rank context and
   lifetime, versus an explicit ordinal/sequence-tagged interface
   with storage/transport commitments. They are candidates, not
   accepted implementations. Analyze their ability to support
   arbitrary accepted sequence rank without silently finite wrapping,
   forced resets or external infinite memory.
3. **Implement an executable bounded trace witness suite**
   `out/IF11_TRACE_MODEL.py` (stdlib only), with an independent
   specification oracle and explicit hypothetical assumptions.
   Include negative and positive controls covering:
   - invalid attempts between accepted events;
   - zero-energy ambiguity after consumer restart;
   - reset with old owed result then new same index/energy;
   - finite tag reuse while old response remains live;
   - Q+1 accepted, unpublished results with Q-only retained slots;
   - retry as new acceptance vs retry bound to original event;
   - optional acknowledgment versus demonstrated ordering/association;
   - provider snapshot availability on A/B/C only when explicitly
     assumed; never imply a real C-HIST provider.
   Record commands, seed if any, total cases, exit codes and exact
   expected/observed outputs.
4. **Prove or falsify named boundary claims conditionally.**
   A trace where a consumer has identical information but must
   decode different n refutes THAT interface, not all possible
   interfaces. A finite backlog counterexample must state its
   assumptions on unbounded acceptance, queues, storage, replay,
   timing and flow coordination. Separate a full-AS realizability
   blocker from an open supplier/authority contract.
5. **Produce a decision-focused dependency ledger.** For A/B/C,
   list precise missing input capabilities, owner and due-stage;
   give an evidence-producing next action with cheapest distinguishing
   test and how it would affect provisional AP eligibility. Explain
   whether satisfying the accepted AS requires new external services,
   material AS amendment, or can be supported by concrete bounded
   mechanisms under existing authority. **Do not invent the answer.**
6. **Carry resource/lifetime and F scopes.** Include exact retained
   rank, pending debt, reset labels, retries and staging in symbolic
   detector-owned/shared/upstream memory. Keep compute and device
   electrical energy UNKNOWN until compatible measurements exist.
   Distinguish a source-language / finite test from a proof.

## Output ONLY

- `out/IF11_TRACE_MODEL.py`: runnable bounded original trace model
  that prints a deterministic JSON summary and exits nonzero on
  discrepancy. Must not write files, use network, subprocesses,
  other workspace or hidden solution.
- `out/IF11_FEASIBILITY.md`: source-linked alternative contracts,
  assumptions, conditional proofs/counterexamples and evidence ledger.
- `out/IF11_RECEIPT.json`: `study_id=CLN-001-IF11`;
  source hashes, executed commands/seeds/exits/counts, hypothesis
  class per finding, active AS/F/proof boundaries, blocker owners
  and next concrete actions. Set `AP_selected:false`,
  `AS_changed:false`, `RI_RN_C_HIST_approved:false`,
  `full_H1_H6_PASS:false`, `target_verified:false`,
  `product_verified:false`, `formal_cleanroom_qualified:false`,
  `vo_discharged:[]`.
- `out/IF11_BRIEFING.md`: human engineering briefing focused on
  what newly became feasible, impossible *under named assumptions*,
  newly uncovered dependencies and the smallest follow-up decision.

Stop after four raw outputs. No binding AP/CON/DE/C, accepted
service, AS revision, automatic AP selection or review self-approval.
A distinct independent review of this NEW evidence follows.
