# TOY1-BASELINE002: Independent baseline re-review request

**Stage:** BASELINE_REVIEW, pending independent review; no activation.

The first independent baseline review, `reviews/gates/TOY1-BASELINE001-independent-review.json`, reported BR-001: the reviewed AS-v2 document retains a historical `specifies` link to VP-v2 while the reviewed baseline selects VP-v3.

Rather than modify an already-reviewed AS or repeat its proof, this versioned *baseline candidate* explicitly states its effective relation selection:

- Historical AS: `knowledge/architecture/AS-001/statement-v2.md` remains immutable.
- Historical raw relation: `specifies /architecture/AS-001/verification_plan-v2.md`.
- Effective relationship *within this candidate baseline only*: `specifies /architecture/AS-001/verification_plan-v3.md`.
- Grounded authority: favorable `reviews/gates/TOY1-AS002-independent-review-v3.json`, which covers AS-v2 and VP-v3.
- Deterministic proof-of-projection check: `python tools/baseline_relations.py inspect --baseline process/baselines/AS-001-v2-candidate-r2.yaml`.

The resolver must reject an invented source/target, missing source edge, unreviewed replacement, and any attempt to activate an unreviewed candidate. Before controlled activation, the active graph/context projection must use the reviewed relation override; readers must not resolve the obsolete VP-v2 as current authoritative evidence. Historical graph edges remain discoverable.

## Requested review

1. Determine whether the explicit, review-backed effective relation **resolves BR-001** while keeping AS-v2's reviewed hash unchanged. If not, give the smallest precise missing requirement for version selection.
2. Independently check the candidate active AS, VP, VO-004 and open VO-ledger entries against both protected human decisions. No fabricated timing, publisher-loss hardware, source sequence or watchdog features.
3. Verify that proposed VO-004 is still OPEN and due at IMPLEMENTATION, with no unauthorized VO status changes, AD changes, or new target evidence claims.
4. Ensure the selected AP-002 remains *provisional*, C-002 is still 2048 detector-attributable bytes and PR-002 still abstract.
5. Record source hashes, actual checks, any blocking findings, review limitations and exact next eligible step.

**Acceptance does not activate the baseline.** Following a favorable independent receipt, use a separate controlled activation operation to make the reviewed AS/VP/effective relations and open VO ledger authoritative before new minimal CON work.
