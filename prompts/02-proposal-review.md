# Codex task 2: New-session proposal and assurance review

Start a NEW Codex session to demonstrate that state is in Git/OKF rather than prior conversation. Read `AGENTS.md`, act as `agents/verification-agent.md`, and use the role's spine view.

1. `python tools/pc.py check`
2. `python tools/pc.py view --role verification-agent --spine /architecture/AS-001/spine.md --emit`
3. Inspect PO created by the scout and the two APs. Do NOT pretend an unverified PO is a theorem.
4. Produce `reviews/AP-REVIEW-001.md` with a table of R/C obligations and candidate status `PASS`, `FAIL`, `UNRESOLVED`, plus what proofs or target tests would discharge each unknown.
5. Discuss whether F can select an AP yet. If not, identify the minimum next evidence needed.
6. Do not write firmware or change accepted upstream assumptions.
7. Run check again and provide a short report.
