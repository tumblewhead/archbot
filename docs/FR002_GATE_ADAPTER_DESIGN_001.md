# FR-002 Gate Adapter: bounded genericity repair design candidate

**Status:** PROPOSED, NOT IMPLEMENTED, NOT AUTHORIZED FOR ENGINE CHANGES.  
**Project:** Progressive Concretization (`tumblewhead/archbot`).  
**Predecessor:** Independent FR-001 R1 review, `REVIEW_FR001_PROJECT_CONTEXT_R1-001`, source receipt committed at `6718424a4880ac6bba22c279d0a00483f5a8de98`: `ACCEPT_WITH_CLARIFICATIONS` for **telemetry role-projected context** only. This is not cleanroom qualification.

## A. Existing source-backed coupling

The shared-looking `tools/stage_gate.py` is still a Toy 1-specific AP provisional selection gate:

| Current location | Coupling | Sustainable disposition |
|---|---|---|
| `DEFAULTS` | Hardcoded `process/policies/AP_SELECTION_v2.yaml`, `process/decisions/C-002-scope.yaml`, historical `process/ledgers/vo_ledger.yaml` | Generic entry requires explicit project-specific inputs. Historical Toy 1 invocation may remain behind an **explicit legacy mode**, never a silent default when evaluating another project |
| `MEMORY_CATEGORIES` and `check_memory_envelope` | Seven detector SRAM attribution buckets, reserve, 2048-byte ceiling and C-002 messages | Move without relaxing checks to opt-in Toy 1 C-002 validator/policy |
| `evaluate` scope preamble and `req == 'C-002'` branch | Universal gate assumes protected scope C-002 | Dispatch project-selected domain validators at their declared requirements. Missing required validator must BLOCK, not skip |
| F-mode notes | Hardcoded final F-001 wording | Take protected final F identity from explicit project policy; preserve semantics and no-final-Pareto claim |
| VO/AD and evidence logic | Stage admissibility, authoritative VO carry-forward, deferral completeness, protected selection and review eligibility | Keep common mechanics, with active ledger references from project manifest/baseline rather than Toy 1 historical filenames |

These are **static source observations**, not a new product defect or an executed cross-project attack. `tests/test_stage_gate.py` currently exercises a Toy 1 simulation and negative controls; it is not a project-agnostic integration qualification.

## B. Proposed minimum interface

A future FR-002 implementation should separate:

- **Common gate**: no embedded C-002/AS-001 constants. Input consists of an explicit project identity/spine, a selected stage, the assessment, the active reviewed baseline/VO/AD ledgers, policy and a resolved list of required validators. Output preserves gate decision, errors, unresolved obligations, citation identities, and a distinct note that eligibility is not engineering approval.
- **Domain policy**: under a project-owned namespace, declares `validator_id`, pinned reviewed source/policy revision, applicable requirement IDs and authority receipts; Toy 1 explicitly requires a C-002 resource-envelope check.
- **Validator implementation**: applies the existing seven-category envelope bounds, accounting boundary, margin and decision authority checks to Toy 1, unchanged in meaning. Its error messages may remain C-002-specific because that is a domain policy, not a universal truth.
- **Dispatch boundary**: deterministic explicit registry of approved validators only; unknown validator, missing configuration, unexpected project, unsupported stage, stale source pin, or a required validator that did not run produces `UNRESOLVED` or `NO_DOWNSELECTION`, not `PASS`.
- **Compatibility**: existing Toy 1 tests should call an explicit Toy 1 adapter where possible; retain a narrowly documented CLI compatibility mode only if it cannot silently infer AS-001 on a fresh project. Never reinterpret historical Toy 1 receipts.

A candidate declarative mapping (design sketch, **not** an approved or installed schema):

```yaml
project_id: AS-001
spine: /architecture/AS-001/spine.md
active_baseline: process/baselines/AS-001-v2-active.yaml
vo_ledger: process/ledgers/vo_ledger-AS-001-v2-active.yaml
ad_ledger: process/ledgers/ad_ledger.yaml
stage_policy: process/policies/AP_SELECTION_v2.yaml
required_validators:
  - id: TOY1_C002_CHARGED_SRAM
    requirement: C-002
    approved_scope: process/decisions/C-002-scope.yaml
    policy_source: reviewed_project_authority
```

**Important:** this is a design illustration. It must not become a new active project policy without source pinning, independent review, and the authorized scope decision. The generic gate must not substitute missing keys with `DEFAULTS` from Toy 1.

## C. Acceptance canaries for FR-002

| Canaries | Required behavior |
|---|---|
| Toy 1 positive and all historical negative checks | Preserve existing gate decisions, evidence requirements and C-002 accounting, including overflow, no margin, missing charged category, missing authority and AP-due requirement errors |
| Toy 1 missing validator / wrong validator / altered policy pin | Fail closed; C-002 requirements cannot be bypassed by omitting a plugin or claiming success without its report |
| Fresh Toy 2 numerical root solver | Can reach a **structural** AP gate with a new project and its own policy, with no forced C-002 buckets, ADC size, 2048-byte limit, F-001 text or AS-001 ledger |
| Cross-project references | Wrong source spine, VO ledger, scope receipt or reviewer identity must not confer authority |
| Accepted-review separation | Deterministic gate can report only *eligibility*; it cannot approve AP, discharge VO, accept AD, or assert target evidence |
| Review and history | Historical Toy 1 receipts remain byte-for-byte intact and retrievable at their original commits |
| No implicit defaults | Missing active policy, authority, project or required validator returns a reasoned blocker |

**Test ownership:** the human runs builds, tests and simulations; an independent reviewer examines actual pushed evidence and reproduces negative canaries. We will not fabricate test counts or claim these tests exist until implemented.

## D. Minimal work and preserved constraints

Potential new source locations: `tools/gates/common.py` and `tools/gates/toy1_c002.py`, an explicit project gate manifest, modified `tools/stage_gate.py`, and bounded tests in `tests/test_stage_gate.py` / `tests/test_gate_adapter.py`. The names are provisional design choices, not registered paths.

Do **not** refactor `task_legacy.py`, rewrite `verification_kernel.py`, change proof authority, or alter accepted AS/AP/F/CON/DE just to achieve genericity. Do not switch to a permissive no-validator configuration. Preserve FR-001 context behavior. The shared `tools/pc.py check` hardcoded manifest requires a separate scoped decision rather than being silently included.

## E. Gate sequence and explicit non-claims

1. Human engineering authority authorizes only the bounded FR-002 gate-adapter change described here.
2. Assistant authors source, policy wiring and negative tests, commits a candidate to GitHub with versioned scope.
3. Human pulls, runs the exact tests and checks, pushes bounded evidence including failures if any.
4. A **different independent invocation** reviews the implementation, source pins, domain scope and the test evidence.
5. Accept or revise FR-002 within its reviewed scope; only then continue to the next separately authorized framework repair.

FR-001's scoped acceptance remains valid; the previous `REVISE` remains historical. No framework freeze, cleanroom launch, final F-001 comparison, target configuration, product verification, VO discharge or AD change is conferred by this proposal.
