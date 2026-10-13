# EP-002: Stage-Appropriate Architecture Selection

Read AGENTS.md and theory_of_operation.md.

Act as the Evidence Planning Agent.

Start at AS-001's architecture spine.

Read AS-001, F-001, AP-001, AP-002, PR-002, AE-001, AE-002, EP-001, the verification plan, and applicable VOs.

## Objective

Determine the minimum sufficient evidence to select an architectural proposal for subsequent contract-first decomposition.

Do not require completed firmware or final target measurements before architectural commitment.

## Required analysis

1. Distinguish provisional AP selection from final implementation acceptance.

2. Identify which obligations must be assessed at AP selection and which may be explicitly deferred to CON, DE, implementation, or validation.

3. Resolve or explicitly flag the C-002 scope ambiguity. Do not expand "detector state" to include unrelated resources without an authorized interpretation.

4. Construct candidate-level resource envelopes using analytical bounds and conservative assumptions.

5. Identify which architectural differences matter to F-001 and which measurements can be postponed.

6. Determine whether F-001 needs an approved stage-specific interpretation or versioned revision. Do not silently change its requirements or ranking policy.

7. Carry every deferred requirement forward as a Verification Obligation.

8. Propose the smallest evidence package needed for a defensible AP selection.

9. Retain EP-001's target-level evidence campaign for final verification.

## Outputs

Create EP-002 as a new OKF artifact.

Include:
- AP-stage evidence requirements
- A candidate feasibility matrix
- Outstanding verification obligations
- Resource assumptions and uncertainty
- A proposed staged selection policy
- Decision blockers, if any
- Recommended next gate

Do not overwrite EP-001.
Do not select an AP.
Do not change AS-001 or F-001.
Do not treat a projected resource estimate as a measured result.

Update the architecture spine.
Run the structural checks.
Create a review receipt.