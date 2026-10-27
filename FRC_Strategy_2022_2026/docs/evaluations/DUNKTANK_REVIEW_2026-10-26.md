# DunkTank agent output review and regression case

The corrected assignment is 2024 WCP CADathon DunkTank. The earlier Hero Heist prompt attribution was corrected by the user, so it incurs no deduction. Reviewed artifacts: the user's supplied one-sheet task workbook and detailed design recommendation. Preserve their original state; this review is not a revised design or evidence of an implemented prototype.

The recorded review score is 68/100: assignment/context 9/10; rules/math 10/12; strategic model 8/14; task decomposition 7/10; workbook substance 7/10; reference quality 7/10; architecture 8/12; alternatives 2/8; tests 4/6; usefulness 6/8. This is an evidence-anchored reviewer judgment with ordinal partial credit, not a calibrated accuracy measurement. The subsequently supplied 1833 doctrine rejects a support-only architecture independently of that historical score.

Verified strengths: 58 tasks on one sheet; 43 Must do, 7 Might do, 8 Won't do; summary caches and priority-times-difficulty calculations match; no cached Excel error cells; final human decisions pending. Core stack math gives 48 ordinary basketball points, 60 possible final stack bonuses, a 31-point successful preload-plus-exit routine and 33 1/3 points for 100 successful endgame electrolyte scores. The packing calculation gives about 6.31 cubic feet at an assumed 60% fraction before mechanism intrusion. Those batch ceilings are not a match model. The output recognizes useful versus harmful clears, shared bonuses, ball return delay and intake-to-outlet integration.

Failure 1 — specialist selected before marginal comparison: two capable basketball partners are assumed, but no same-partner timed comparison establishes whether an electrolyte-only robot beats a mixed or basketball-capable candidate. Repair: model direct, enabled and denied output and a counterfactual replacement, including weak/ordinary and elite defended scenarios. For 1833, a support-only candidate is disallowed by the new owner instruction.

Failure 2 — threshold converted into capacity: row 25 makes 100 delivered onboard balls essential because the tank clears at a cumulative 100. Multiple smaller deliveries and existing tank inventory are not compared. Repair: evaluate capacities and fixed/expanding storage with travel, collection, mass/volume, losses and actual useful resets. Do not assert that a smaller design is necessarily better either.

Failure 3 — full refill used as denial proxy: final bonuses are evaluated per stack. An opponent that cannot refill all three can still restore one or two. Repair: model per-stack recovery, prerequisite dependencies, time left, and the attacker's lost scoring. Maximum 60 denied points is a conditional upper bound, not expected contribution.

Failure 4 — boilerplate dependencies: 50 of 58 J cells repeat the same coordination/route/timing sentence; the other eight repeat an exclusion sentence. Difficulty explanations similarly repeat that a number is provisional. Repair: require task-specific predecessor/interface/failure conditions and difficulty drivers. Task count and nonblank cells alone earn no substantive-quality credit.

Failure 5 — contradictory acceptance targets: row 25 requires at least 100 delivered; row 28 initially permits two residuals; row 56 requires 98% retention. Row 13 specifies 20/20 combined auto exits/discharges whereas rows 21/39 specify 18/20. Repair: define authoritative system release targets, screening stages, loss margins and test conditions, with traceable requirement IDs. Do not quietly label inconsistent targets equivalent.

Failure 6 — historical piece-size error: the recommendation describes 254's 2022 reference as 7-inch cargo. The official 2022 manual section 5.7 specifies 9.5-inch fuzzy inflated cargo. Repair: verify year-specific diameter, material and compliance before importing intake compression or contact speeds. The primary/secondary roller arrangement is supported by 254's binder; preserve the valid principle while correcting the dimensional statement.

Failure 7 — deferred physical feasibility and optimization: routes, field opening, packaging and resources are acknowledged unknown, but the output still selects capacity and expansion. Endgame/auto open-chute flow deserves investigation without assuming a physically accessible instant recycling loop. Repair: cheap aperture and envelope checks, state/flow model, capacity trade study, then integrated loaded tests. No complete new DunkTank recommendation is certified by adding this protocol.

Evidence locators: original workbook rows 13,21,25,28,32,39,56 and column J; detailed recommendation sections on hopper, compared alternative and first tests. Original uploaded attachments remain with the user and are not silently rewritten. Scoring criteria are in `agent/design_rubric.json`.

Sources: supplied DunkTank Game Update 01 manual, physical pp 3,10–14,17–19; https://www.chiefdelphi.com/t/wcp-cadathon-2024-dunktank/472262?page=4 ; https://firstfrc.blob.core.windows.net/frc2022/Manual/HTML/2022FRCGameManual.htm section 5.7; https://media.team254.com/2022/10/8f2407a5-Team_254_Tech_Binder_2022.pdf physical p14. Later update parity remains unverified. This case does not claim visual match watching or measured hardware results.


## Reproduction

Unchanged source artifacts are preserved in `evaluations/evidence/dunktank-2026-10-26/` from corpus root, with hashes in `data/dunktank_evidence_manifest.json`. Run `python scripts/audit_task_workbook.py evaluations/evidence/dunktank-2026-10-26/original_agent_task_list.xlsx`. The structural audit confirms 58 tasks and flags the 50 repeated dependency cells; it does not claim semantic correctness.
