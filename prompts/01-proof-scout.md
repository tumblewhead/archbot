# Codex task 1: Proof opportunity discovery

Adopt the role in `agents/proof-scout.md`, guided by repository `AGENTS.md`.

1. Run `python tools/pc.py check` and `python tools/pc.py view --role proof-scout --spine /architecture/AS-001/spine.md --emit`.
2. Do **not** open `knowledge/architecture/AS-001/evidence/raw/samples.csv` unless you discover a specific mathematical need. The compact results should be enough.
3. Examine AS, BKP, F, and candidate APs. Identify the 1-3 highest-value **proof opportunities**. Look for universal bounds, inductive invariants, and impossibility results. Distinguish evidence from proof.
4. Create draft OKF PO artifacts in `knowledge/architecture/AS-001/proofs/opportunities/`. Each must have explicit proposition, quantifiers, assumptions, proof strategy, possible counterexample, and architectural value. Cite sources with OKF `sources` and footnotes.
5. Add typed `opportunity` edges from the architecture spine to the new artifacts. Never add `verified` or `proven_by` metadata. Do not modify BKP, AS, F, or proposal content.
6. Write one short task receipt as `reviews/PO-SCOUT-001.md` including exact artifacts inspected and uninspected, what you added, and `UNRESOLVED` items.
7. Run `python tools/pc.py check`, then `python tools/pc.py view --role proof-scout --spine /architecture/AS-001/spine.md` and report the changes.

Output: the best candidate theorem stated mathematically, its assumptions, and what an independent proof engineer would need to establish. Do not claim it is proven.
