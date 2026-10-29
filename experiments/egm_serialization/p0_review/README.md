# EGM-P0 independent review: one focused gate before the Goldfish pilot

Current available evidence: human reported 10/10 checker tests PASS.
[Local-test observation](../P0_USER_TEST_REPORT_001.json) records only what
the pasted terminal output establishes. No independent review or
`py_compile` output was supplied.

This review tests both the comparator's real behavior and whether
the **author-drafted evaluator-only P1 answer key** is faithful to the
actual proposed harness/skeleton/EGM documents. Neither a perfect
checker nor a perfect reference is assumed in advance.

## Prepare

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
git status -sb
git switch work/cln001-integration-c-kernel-harness
git pull --ff-only origin work/cln001-integration-c-kernel-harness

bash -n experiments/egm_serialization/p0_review/prepare.sh &&
bash -n experiments/egm_serialization/p0_review/archive.sh &&
bash experiments/egm_serialization/p0_review/prepare.sh
```

A previous review workspace is not overwritten. The preparer
verifies exact Git blob identities for the checker, test, provisional
reference and three governing sources. A fresh directory is
NOT verified runtime isolation.

## Fresh independent reviewer

New terminal, new Codex session:

```bash
cd "$HOME/archbot-egm-p0-review-001" || exit 1
codex
```

Give Codex:

> Read AGENTS.md, TASK.md and inputs/SHA256SUMS.
> Independently reproduce the 10 checker tests. Check the comparator's
> fail-closed behavior and its structural-only scope. Audit every
> provisional P1 reference fact and typed edge against the three
> supplied source documents; identify unsupported or ambiguous entries.
> Verify the positive-allowlist P1 preparation and evaluator separation,
> without asserting OS/network/connector isolation from directory
> separation alone. Write ONLY the two requested independent review
> outputs, then STOP. Do not run the Goldfish or activate a process gate.

## Archive exact evidence

After both review outputs exist, return to the normal checkout:

```bash
cd /home/easy/proj/archbot/archbot-repo || exit 1
bash experiments/egm_serialization/p0_review/archive.sh
git show --stat --oneline HEAD
```

On `READY_FOR_SCOPED_EGM_P1_DIAGNOSTIC`, a separately scoped
decision can permit the first source-only pilot described at
[EGM-P1 handoff](../p1/README.md). On `REVISE`, fix only
identified defects and rerun the affected review. Do not
re-execute the full old Toy1 numerical campaign.

Independent review here is of **new checker/source fidelity**,
not another general review of unresolved implementation feasibility.
