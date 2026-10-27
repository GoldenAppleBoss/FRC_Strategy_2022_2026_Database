> Owner constraints: no pneumatics; no turrets; no support-only architecture. Historical scope and future 2018/2019 roadmap: `docs/1833_ACTUATION_AND_HISTORY_SCOPE.md` from corpus root.

> Owner correction: prioritize independently achievable RP and essential scoring independence. Physical iteration is extremely expensive; use proportionate analytical checks and targeted tests. Read `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` from corpus root.

# Architecture decision review and task quality protocol

This protocol addresses the DunkTank output reviewed on 2026-10-26. The historical artifact earned 68/100 under the recorded rubric; that is a reviewer assessment, not a model benchmark. The new 1833 constraints also make its support-only baseline unacceptable as a current recommendation. Do not change its original score retroactively or present an untested replacement design as a demonstrated improvement.

## 1. Establish functional priorities before choosing a role or mechanism

Start with rule-derived actions and constraints, including autonomous, primary scoring, enabling resource flow, endgame and denial. Record phase and game-state effects before specializing an architecture. Identify what would make 1833 the strongest primary contributor. Map the objective into measurable useful outcomes; do not fill the task sheet with priorities that merely restate a preselected specialist role. Keep outcome tasks, implementation concepts, compliance constraints and alliance-wide results distinct. Extra rows are not evidence of comprehensive understanding. Retain one sheet; use labeled rows or a hierarchy inside that sheet rather than group tabs.

Record initial neutral functional priorities and the reasons for any changes after architecture comparison. A team's assignment alongside exceptional partners is a scenario, not proof that the robot should depend on those partners for fundamental scoring. Follow the binding no-support and no-turret constraints in `docs/1833_DESIGN_DOCTRINE.md`.

## 2. Model the game as state and flow

Identify inventories, locations, capacity/weight thresholds, scoring eligibility, occupied goals, possession, reload/discharge behavior, deadlines and final evaluation conditions. Model autonomous, transition and endgame separately where the rules differ. Opening a return chute can change feasible sustained flow, but does not establish that returned pieces are accessible or instantly reusable. Include return delay, collection success, route interference and control latency. Check rule-specific settling/scoring cutoffs rather than applying an invented universal end timestamp.

For each candidate, construct a timed match/resource model under at least three named scenarios: ordinary or weak partners; strong partners; and elite defended play. The same partner capabilities, field rules, opponent assumptions and external supply must apply to every candidate within a scenario. Show acquisition, travel, alignment, release, recovery and waiting separately, and document which operations overlap. Use measured or sourced values when available; otherwise use explicitly labeled plausible ranges and sensitivity analysis. Unknown inputs cannot silently become optimistic constants. Do not add overlapping time costs twice or count the same enabled alliance points as multiple robots' individual output.

Calculate whole-alliance output and compare the counterfactual replacement: same partners, different 1833 architecture. Report direct contribution, enabled contribution, denied contribution and opportunity cost separately, with interactions explained. A shared multiplier can help the opponent. A hostile reset may enable them to score again. Evaluate per-goal final-state recovery instead of a binary full-refill test. A maximum possible score or denial is not an expected match result.

## 3. Compare capacity and deployment choices explicitly

A field threshold is not automatically an onboard capacity requirement. Compare at least three plausible capacities or storage arrangements spanning the proposed choice. For a 100-piece cumulative threshold, 50/75/100/150 are illustrative candidates, not prescribed targets. Consider existing target inventory, multiple deliveries, collection delay, cross-field distance, throughput, spill, usable packing and loaded maneuverability. Compare fixed versus expanding storage before adding expansion. Record what packing fraction means and reserve volume for conveyors, structure, supports, electronics, moving swept volume and trapped pieces.

Use deliverable capacity under stated motion and wear conditions. If delivery efficiency is eta, capacity C and residual r, account for losses without double-counting them; a simplified effective delivery estimate C*eta-r must state its assumptions. A 100-count load with 98% retention cannot guarantee 100 delivered. If the field threshold is measured by weight, piece counts are a proxy requiring tolerance and calibration rather than a certified exact trigger. Inventory sensing and target-state sensing are distinct problems.

## 4. Select between credible complete candidates

Compare at least two viable non-turret primary-contributor architectures. Do not use an intentionally weak alternative to justify a preferred concept. Compare mission output, controllability, defended performance, autonomous, loaded dynamics, resources, complexity and development time using common assumptions. A high-level sketch or bounded layout is sufficient at this stage; exact fabrication drawings and invented motor ratios are not required.

Establish the physical envelope: legal start/deployed dimensions, ground transition, storage volume, lift to outlet, entry aperture, collision/swept volumes, electrical access and loaded CG. Label dimensions measured from governing CAD separately from provisional allocations. Resolve cheap geometry questions before a large prototype. Identify which values could reverse the choice, show those sensitivities, and define fallback milestones.

An original mechanism is allowed without a famous reference. Its essential interfaces still need a causal explanation and a test. For borrowed mechanisms verify year/team/version, game-piece diameter/material/deformability and competition hardware legality. The 2022 Rapid React cargo diameter is 9.5 inches, not 7 inches. Never transfer compression, traction or roller speed merely because both objects are called balls. Keep representative source images and locators available to the next reviewer; claim visual review only when actually performed.

## 5. Make the task workbook substantive

Every occupied row must carry a task-specific dependency and rationale. Identify actual predecessor tasks or external conditions, relevant mechanism interfaces, and effects of failure. Repeated generic statements about coordination or unverified CAD do not satisfy this requirement. Explain difficulty using a consistent basis such as interfaces, maturity, tolerance, manufacturing and commissioning. Do not pretend the Fibonacci scale is a calibrated numeric effort estimate. Distinguish no relevant task (N/A) from a real task excluded from the robot.

Column K contains an authoritative acceptance requirement or a clearly unresolved target. Column M identifies the unknown, the test that resolves it, and the decision it changes; merely copying K after an introductory sentence is insufficient. Distinguish screening targets from release criteria explicitly. Preserve row/requirement IDs in the design record so cross-row conflicts can be reconciled. If one row allows two residual balls and another requires a guaranteed 100-ball delivery from a 100-ball load, label the former as intermediate screening and prevent release until the system target is met.

Keep agent recommendations and human decisions separate. Check summary formulas, caches, validations and occupied-row coverage. Run `python scripts/audit_task_workbook.py PATH.xlsx`; its duplicate-field warnings require human review, not automatic deletion of legitimately shared dependencies. It cannot validate physics or infer the semantic consistency of every target.

## 6. Test only where the value justifies the iteration cost

First verify rules and field apertures, then use inexpensive envelope and analytical checks. Only where consequential uncertainty remains, test the cheapest capacity/transition or one-lane geometry that can change the choice. Then prototype representative loaded flow, sensing and reversal; integrate at full capacity when the smaller tests support it. Complete defended/dynamic trials and practice validation before calling the system competition-ready. State hypothesis, conditions, sample size, measured quantities, screening/release target, and decision consequence for each test. A proposed 20/20 result is an acceptance target, not measured evidence or a statistical reliability guarantee.

## 7. Deliver and preserve the decision

Deliver the populated single-sheet workbook; one selected architecture and the complete alternatives comparison; quantitative scenario/capacity results with input provenance; physical envelope; exact reference locators/images; and prioritized open tests. Maintain assumptions, decisions, rejected alternatives, user corrections and test results in a dated design record. Fill `examples/design_review_skeleton.json` as a machine-readable summary and run `python scripts/validate_design_review.py FILE.json`. Apply `agent/design_rubric.json` with evidence for each score. The no-support and no-turret gates take precedence over a high numeric score. Validation is structural; a human must judge whether inputs and conclusions are credible.


## Solo ranking capability and proportional evidence

For a new architecture, explicitly map each ranking objective to independent capability or external prerequisites and quantify the individually achievable route with margin. Include a passive-partner stress case in addition to ordinary/elite alliance comparisons. Complete the solo RP record and validation economics; the latter must identify decision consequences, expected costs, cheapest evidence and stopping rules. A bounded improvement can use a short comparison and update only affected task rows, rather than repeating full CAD or model development. See `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` for the owner's actual four-lane decision and the proportionate process.
