# AE-003: Controlled provisional architecture selection

Read AGENTS.md, theory_of_operation.md, agents/evaluation-agent.md, and
`docs/AE003_GATE.md`. Traverse the AS spine selectively. Read the approved
C-002 decision, evidence for VO-001, applicable proof acceptance, VP/VO/AD,
AP-001/AP-002 and candidate resource envelopes, AE-001/002, EP-001/002 as
needed, and the unchanged F-001.

Do not require completed firmware, linker maps, or measured target WCET to
select an AP for decomposition. Require credible AP-stage obligations and carry
later verification forward. Do not relax the 2 KiB detector-charged SRAM limit.

Build candidate assessments using `pc-ap-assessment/v2`, including a categorized
`memory_envelope`, requirement-by-requirement evidence, outstanding VOs,
explicit assumptions, F-001's three projected dimensions, and unresolved
architectural risks. Distinguish allocated memory budgets from proven physical
bounds. Run `python tools/stage_gate.py evaluate --assessment PATH` for each.

If no candidate meets the AP gate, report NO_DOWNSELECTION and the *minimal*
missing evidence. If one is eligible, report ELIGIBLE_FOR_INDEPENDENT_REVIEW,
not PROVISIONALLY_SELECTED. If F projection is incomparable, propose a
stakeholder tradeoff with AD but DO NOT mark that debt accepted or invent
stakeholder approval. A separate authority action must select an AP.

Do not modify AS-001, F-001, historical AE/EP/PR records or accepted theorem
scope. Preserve the authority and debt chain and produce an AE-003 artifact,
spine link, and review receipt. Run structural checks.
