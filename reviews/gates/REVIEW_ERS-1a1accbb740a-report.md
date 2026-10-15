# Independent ERS review — REVIEW_ERS-1a1accbb740a

## Scope and integrity

Reviewed submission `reviews/verification/TOY1-VERIFY-ERS002/receipt.json` for author task `TOY1-VERIFY-ERS002` at checkout revision `0383a46413c099df0782a21a87d090db660f2a29`. The submission points to `reviews/verification/TOY1-VERIFY-ERS002/artifact.json`; its SHA-256 matches the receipt (`2f0cf28f4c85ac60d53f899798cb964fe0ce427eb6e93488c947e4cfb9b6d860`). All 31 pinned source files match their recorded hashes. The artifact content digest matches its payload.

The inventory has 21 requirements and 21 claims, with one unique claim mapping to each requirement. It preserves the original eight projections and adds the arithmetic and resource facets called out by F-ERS-001 and F-ERS-002. The active VO ledger still lists VO-002 through VO-006 as open; the submission discharges none.

## Coverage review

F-ERS-001 is addressed. Separate projections cover mathematical bounds, concrete C expression types/evaluation order, multiplication promotion, legal-domain correspondence, and the initialized rolling transition. The only candidate rung targets `ERS-CON-ARITH-BOUNDS`; its `MODEL_ONLY` scope expressly excludes concrete C, promotion, domain enforcement, and target-memory correspondence. These facets remain implementation obligations under VO-006.

F-ERS-002 is addressed. The inventory includes each of the seven conditional category ceilings, allocated ceiling and reserve, byte/owner/category/lifetime and nonoverlap inventory, stack/context nesting, shared attribution, bounded dynamic allocation if used, documented exclusions, infeasibility handling, and the proposed DE subceilings. It distinguishes the contract-stage conditional budget from concrete inventory and target evidence still due under VO-002. DE subceilings are accurately described as accounting assignments, not measured capacities.

The projected statements are grounded in the pinned AS, CON, DE, active baseline, and active ledger sources. The scope does not add a throughput deadline, heap prohibition, out-of-domain response, target topology, or physical publisher guarantee. No source states that the absent target/compiler and integration evidence is available, and none is needed to accept this ERS projection.

## Clarifications and limits

- `ERS-CON-SRAM-CATEGORIES` records a contract-stage commitment, while concrete feasibility and fit remain open. This review does not establish that the ceilings are feasible on a target.
- `ERS-DE-SRAM-PARTITIONS` projects proposed accounting ownership only. Any subceiling mismatch or infeasible selected integration still requires design review.
- The ERS is a candidate inventory accepted for the next scoped activity. This is not product acceptance, proof of C correspondence, target qualification, or VO discharge.

## Deterministic checks

- Submission and artifact references resolve; artifact hash matches the submission receipt.
- All 31 source pins and the artifact content digest match.
- Requirement/claim counts are both 21; every claim refers to one unique declared requirement.
- Active VO states and the submission's `vo_discharged` list were checked; no VO was discharged.

These checks establish integrity and structural consistency only. Semantic coverage conclusions above are this independent review, not an automatic kernel verdict.

## Disposition

**ACCEPT_WITH_CLARIFICATIONS.** The prior blocking findings F-ERS-001 and F-ERS-002 are resolved for this ERS stage. No new blocking inventory gap was found against the declared accepted source obligations. All implementation evidence and VO-002 through VO-006 remain open. Next eligible action: design the verification ladder for independent review, preserving the MODEL_ONLY limit and all open VOs.
