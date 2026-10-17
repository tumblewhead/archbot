# QUESTIONS-001 — Decisions needed for AS-DRAFT-001

Status: OPEN; no answers or approval inferred. Questions refer to the source and requirement IDs in `AS-DRAFT-001.md`. The human must identify the appropriate decision authority; these questions do not assign authority to the agent.

## Q1 — Establish requirement authority (U1)

Who may authorize this project's requirements and assumptions? Does that authority adopt, revise, or reject each explicit brief statement R1–R6 and each synthetic assumption A1–A4? S1 is labeled “Stakeholder Decision,” but also draft and invented for demonstration; S2 and S3 are synthetic drafts. Please record the decision maker, disposition, and scope. Is this to remain solely a hypothetical exercise or describe a particular device?

## Q2 — Decide the timing requirement (U2)

Is “updated every 1 ms” an authorized stakeholder requirement, a demonstration assumption, or a statement to revise? The workspace provides no accepted authority for it. If adopted, what precisely is required: periodic sampling, periodic publication, completion within a deadline from a specified event, or a combination? Specify the reference event, allowed latency and jitter, startup behavior, missed-update policy, and acceptance criterion. Does the synthetic 1 ms arrival model A2 remain valid independently of the output requirement? No hard 1 ms deadline is adopted pending this decision.

## Q3 — Define sustained-energy detection (U3)

Is the deliverable the numeric energy result alone, or must it also produce a detection decision? If a decision is required, specify the threshold or rule, duration, units/scaling, output behavior, and acceptance criteria. No detection threshold or duration is present in S1.

## Q4 — Define initialization and the result interface (U4)

What event initializes or resets the history? When is the first result required, including before a full window exists? How is the exact numeric result exposed, to whom, and with what association to a sample or timestamp? Confirm the sequence interpretation of “latest 32” used in the draft PS. R2 supplies startup zero padding but does not answer these interface and lifecycle questions.

## Q5 — Define resource and target constraints (U5)

Is the assumed MCU envelope sufficient for this exercise, or must a specific device and execution environment be named? Does the 2 KiB limit include history, stack, acquisition buffers, shared data, runtime overhead, and output storage, and who allocates these to the detector subsystem? What measurable compute or power criterion makes “conserving” acceptable? Does the floating-point statement merely remove a hardware dependency, or impose an additional arithmetic restriction? Target cycle counts, WCET, power, and compiler settings are not supplied; no feasibility conclusion is available.

## Q6 — Define sample delivery and exceptional cases (U6)

Who owns acquisition and delivery, and what ordering and availability are guaranteed? What should “latest 32” mean with lost, late, duplicated, or out-of-order samples? What behavior is required for invalid or out-of-range values? S2 supplies neither an analog quality guarantee nor a sample loss guarantee. Startup zero padding must not silently become a policy for losses during operation. Decide whether these cases are outside the adopted model or need specified behavior.

## Q7 — Arrange independent review and human disposition (U7)

Who will perform the separate independent review and who will decide the disposition of this draft and its open questions? Review should examine source fidelity and authority, especially R3. No reviewer outcome or stakeholder approval exists in the supplied inputs. After review and recorded human decisions, the recommended gate is disposition and revision of the Architecture Statement; progression requires explicit authorization beyond this task.
