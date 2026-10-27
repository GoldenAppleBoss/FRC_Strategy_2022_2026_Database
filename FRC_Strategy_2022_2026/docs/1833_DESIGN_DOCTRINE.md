> Owner constraints: no pneumatics; no turrets; no support-only architecture. Historical scope and future 2018/2019 roadmap: `docs/1833_ACTUATION_AND_HISTORY_SCOPE.md` from corpus root.

> Owner correction: prioritize independently achievable RP and essential scoring independence. Physical iteration is extremely expensive; use proportionate analytical checks and targeted tests. Read `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` from corpus root.

# 1833 design mandate — owner instruction, 2026-10-26

## Binding design brief

Design to be the best robot on the field: an Einstein-level primary contributor, alliance-captain or elite first-round caliber. Never propose a support-role robot as 1833's architecture. Never propose a turret. Favor relatively simple mechanisms that achieve elite effectiveness through execution, acquisition, sustained throughput, autonomous, driving, controls, reliability, serviceability and extensive optimization. These are explicit user constraints, not conclusions inferred from EPA or a generic small-team stereotype. Only a later explicit user instruction can change them. Do not repeatedly ask to relax them.

Primary contribution is an objective to substantiate, not a guarantee of a future result or an instruction to do every available task. Rank functions by contribution to winning and eliminate low-value complexity. A dominant scorer can play defense or a complementary assignment in a particular match; that does not turn its architecture into a deliberately limited third robot. Preserve historical specialist examples, including 2025 parallel L1/algae assignments, as knowledge about alliance optimization. They are not authorization to cap 1833's own architecture at a support role.

For this profile, turret means a dedicated azimuth/yaw aiming assembly for the scoring mechanism. A chassis-aimed launcher can still have an adjustable hood, elevation pivot or other game-required motion if justified. Explain the cost of chassis aiming, angular acceleration, shot readiness, defender interaction and positioning. Do not disguise a turret under a different name, or delete useful historical turret research: its intake, feed, sensors and failure histories may still be transferable.

The 2027 game is unknown in this analysis. Do not prescribe a 2026 drum, a 2024 low chassis or any historical geometry before reading its rules and strategic constraints. Transfer the optimization approach, not an unexamined shape. A game requiring vertical reach may justify an elevator even though a short chassis worked in another game.

## Ambition grounded in the team's stated history

The owner reports that 1833 peaked at eighth worldwide EPA in 2026, was around 35th at this instruction, and was top 75 worldwide during 2025. Treat these as owner-reported dated context; peak date, ranking cohort and model version were not supplied. The included older mirror snapshot instead contains 2026 rank 36 / EPA 233.53 and 2025 rank 130 / EPA 73.05. Do not silently overwrite either record, mistake an end/snapshot rank for a historical peak, or infer a permanent capability limit from a different snapshot. Live ranking pages/API were not successfully available in this research pass. Official 2026 records confirm Newton Division Finalist; the alliance record identifies 1833 as captain of alliance 5 with 930, 180 and 3966. This supports treating 1833 as an established high-performing team, while actual current shop/time constraints remain inputs to obtain.

## Alliance selection and design ceiling

The owner's warning is that an excellent narrow specialist may survive the first selection round and become the first available second-round pick of alliance 8, instead of joining a leading alliance. The 2026 official manual section 10.6.1 confirms first-round order 1→8 and second-round order 8→1; section 13.2 adds Worlds' third round 1→8 and four-team rosters with three starters. This is an incentive to build an independently valuable leading robot, not a deterministic theorem about draft outcomes. Captains, first picks, scouting judgments, availability, declines, autonomous compatibility and game-specific marginal value affect actual choices; a first-round pick list is not necessarily EPA order. Check the next season's rules rather than assuming the format persists.

Do not optimize 1833 merely to be the best remaining specialist. Analyze qualification ranking power, individual offensive production, autonomous ownership of contested resources, contribution with ordinary partners, and ceiling alongside elite partners. Report why the design would plausibly be attractive as a captain or first-round partner. Do not invent a numerical probability of an Einstein appearance or draft position.

## Simplicity means removing costs while retaining output

Compare mechanisms by actuators, coupled states, interfaces, tolerance sensitivity, manufacturing burden, software commissioning, driver demands, service operations and development time—not silhouette or motor count alone. A simple-looking elevator can hide elaborate alignment, handoff, vacuum or trajectory control. Reduced moving inertia, reliable acquisition and short dead time can produce elite output without decorative complexity. Conversely, a necessary capability must not be omitted merely to make the robot look simple.

The specific exemplars and their limits are researched in `docs/1833_OPTIMIZATION_REFERENCES.md`. 7769's jam remedy is evidence that stronger feed is not automatically better; its rack failures prohibit treating its entire mechanism as perfected. Orbit's compact 2024 robot combined low packaging with substantial controls and refinement. OP 2025 used familiar high-level functions but considerable integration. Orbit 2025 used a differential transmission and vacuum system with real maintenance and control costs. The owner's comparison of 1261 with Orbit is an attributed diagnostic lead, not a verified causal account of another team's failures.

## Required decision outputs

Read `docs/DESIGN_REVIEW_PROTOCOL.md`, complete the one-sheet task workbook, and supply the evidence package specified by `team1833/design_review_schema.json`. Compare credible non-turret primary-contributor architectures with common assumptions before recommending one. If decisive information is missing, recommend a provisional candidate and the next test, rather than declaring superiority without analysis. Run the structural checks, apply the 100-point rubric, and disclose unperformed experiments and unverified claims. Passing a file validator does not establish robot quality or model intelligence.

## Sources

- Owner instruction in this conversation, 2026-10-26: authoritative for preferences and ambition; reported performance claims retain attribution.
- https://firstfrc.blob.core.windows.net/frc2026/Manual/HTML/2026GameManual.htm — sections 10.6.1 and 13.2.
- https://frc-events.firstinspires.org/2026/team/1833 — division finalist record.
- https://www.thebluealliance.com/event/2026new — alliance membership.
- `tables/season_epa.jsonl` — retained historical mirror snapshot; not a newly verified live rank.
