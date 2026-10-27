# DunkTank: one recommended design for 1833

October26,2026, revision1. Companion: `1833_DunkTank_Task_List_2026-10-26.xlsx`. Agent recommendation only; human decisions pending.

## Recommendation

Build a low electrolyte specialist: swerve chassis, wide compliant ground intake, horizontally expanding hopper, and a broad powered conveyor delivering through a short chute into either alliance tank. Qualify 100 actually deliverable electrolytes per load. No basketball elevator, turret, or climb in the baseline. Its job is to keep two basketball partners scoring, force strategically timed opponent clears, then score its remaining electrolytes in the final 20 seconds.

This is an alliance-role recommendation under an explicit assumption: partners can score low/middle basketballs, with at least one capable of high. Neither partner capability nor current team resources is established. If the intended goal is to carry weak randomized partners as an independent captain, this specialist is a weaker recommendation; a mixed basketball/electrolyte architecture deserves reconsideration. I recommend the specialist here because it attacks the game's gating resource and a permitted late scoring-denial mechanism while avoiding a 90-in elevator. It is not a claim of universal optimality.

## Governing evidence and limits

All 19 physical pages of the supplied **Game Update 01** manual were read. Field drawings on pp 5,9,11 were visually inspected. Page 1 links the official update discussion, field CAD and score calculator. Organizer answers on thread pages 2-4 were reviewed. Current source parity and a complete later clarification audit are not certified: the linked update 87 and page 5 could not be fetched. Field CAD was identified but not dimensionally inspected. No physical prototypes, CAD assembly, code, or simulation results are claimed.

The user's existing corpus guides, schema, task protocol and template apply to this new game. A fresh one-sheet workbook was produced; no Hero Heist scoring, class restrictions, or cheat-sheet content is carried over. Tasks include excluded basketball and climb actions so the specialist choice is explicit. Numeric acceptance targets are proposed screening requirements, not achieved performance or reliability certification. Current schedule, designers, shop capability, budget, practice, and maintenance capacity remain unknown.

The recommendation uses 2022 Team 254 and 2026 Team 604 as specific engineering references from the supplied collection. **The 2026 examples are retrospective references for this 2026 analysis of a 2024 game, not concepts available at the 2024 kickoff.** Only 2024-legal motors, electrical and pneumatic components may be used under R06. The full relevant 2026 game chapter, selected source packets and their construction/reasoning/limits were consulted; 604 intake and hopper original CAD images were visually inspected. Interviews were not watched. Unverified CAD tolerances and event-version histories remain unknown.

## Why electrolytes control the game

The match lasts 135 seconds:15 autonomous and 120 teleoperated. Basketball rim heights are 36/54/90 in. Auto scores are 3/8/12 per dunk, with 6 for exiting an alliance zone. Auto ignores stack-fill prerequisites. Teleop scores are 2/5/8, doubled during an alliance's activated 10-second Bonus Mode. In teleop, low holds 6 counted balls, middle 4, high 2; additional balls in a full stack do not score. High is locked until low and middle are full. A robot may hold only one basketball, but unlimited electrolytes. [Manual pp 2-3,7-10,G15.]

A complete unboosted stack set therefore earns `6×2+4×5+2×8=48` basketball points. Two high dunks account for16 of those48; the prerequisite low/middle work contributes32. A high-only robot does not create an unrestricted8-point cycle. An alliance tank receiving100 electrolytes automatically clears every allied hoop stack and its own tank. This happens regardless of stack occupancy. Stored basketball points remain, but the alliance can score another set. Ordinary-teleop electrolytes have no direct point value. [pp10-12; organizer post70.]

Only stacks full at the end earn 20 points each: up to 60 plus the all-full qualification RP. Those 60 points are not awarded at every clear. The additional qualification RP comes from three alliance clears OR one alliance clear and one Bonus Mode. Wins/ties/losses are 2/1/0 RP. [pp 3,19; organizer posts 62,69.]

This makes timing more important than maximum dump rate. Clearing your own tank with full stacks and enough time to refill can enable additional score. Clearing with empty stacks can do nothing useful. Clearing near the end can destroy final bonuses and require rebuilding the 6/4 prerequisite before high scores again.

The organizer explicitly permits scoring into the **opponent's** tank and says forcing opposing clears is expected gameplay (posts 62,73). Thus a loaded electrolyte robot can threaten their final occupancy, not merely supply its own scorers. It may erase up to 60 final bonus points and the all-full RP **if the opponent cannot refill**. That is conditional denied value, not guaranteed points scored by this robot. An early hostile clear may benefit the opponent by reopening full stacks.

Clears stop when 20 seconds remain. Attack completion needs margin before that transition. Derive the attack window from measured opponent refill time: if they need T seconds after the clear to refill and C seconds remain at completion, the intended denial needs C<T, while C must still exceed 20 seconds. If they refill faster than the available pre-endgame window, a simple late-clear plan will not deny all final bonuses. Occupancy, travel uncertainty, scores already in flight, and their own electrolyte deliveries alter this calculation.

After the cutoff, our additional own-tank electrolytes earn 1/3 point each and no clears trigger.100 delivered gives 33.33 direct points.50 auto electrolytes gives 25, plus 6 exit for 31. These are successful-action ceilings for those batches, not predicted match totals. [pp 3,12.]

## Supply and routes

There are 500 electrolytes total,250 initially behind each alliance wall, in 50-piece buckets. Preloads come from the available allocation; no extra unlimited supply is assumed. All electrolyte introduction must occur before 60 seconds remain. Once introduced, pieces stay on the field; own-tank clears release them back for reuse. Center-tank deliveries remain trapped for the match. Human buckets do not enter the field. [pp 8,12-14.]

The organizer estimates tank discharge at approximately 10 electrolytes/s (post 66), so recycling 100 balls takes about 10 seconds of discharge alone. Collection and travel still follow; a fast robot outlet cannot make field return instantaneous. Do not design an autonomous infinite scoring loop or assume an immediate second 100-ball supply after a clear.

The center tank gives **both alliances** one independently activatable 10-second Bonus Mode for each 100 electrolytes deposited, capped atthree each. A center delivery can help qualification RP and favor the alliance ready to use it, but it also helps the opponent and permanently consumes shared supply. The baseline policy is no center donation without a positive alliance-level comparison. A full ordinary 48-point basketball set entirely doubled would add 48, but completing 12 individual dunks in a single 10-second window is not demonstrated and is not our target.

The top-down drawing places own loading box and own hoop wall on the opposite side from own tank. Supply-to-tank is therefore not assumed to be a short protected station loop. The opponent tank may be convenient to your original loading side, but contact protection still applies. Ground collection of returned or dispersed supply becomes essential after the introduction deadline. Routes, clear timing and loaded starting position matter as much as the conveyor.

## The physical robot and direct mechanism references

### Intake:604 Toploader robustness, with 254-style controlled over-bumper transfer

**2026 Team604, Toploader release, intake section:** independent deployment on each arm, protected motors, belt-driven dead-axle polycarbonate rollers covered with silicone tubing, compliant polycarbonate arms, and TPU supports retaining belts during arm deflection. The team explains that independent arms addressed a chain-breaking failure in the linked2024 intake; its reported printed-plug material and maintenance history are version-specific. Relevant corpus note: `604-expansion-2026-4`. [Team604 primary release, posts1,6,19-20](https://www.chiefdelphi.com/t/team-604-quixilver-2026-robot-cad-and-code-release/524289).

Implementation: use this contact-and-impact arrangement for a wide pickup of 5-in wiffle balls. Scale the roller gap, bumper rise and supporting kicker for those actual pieces. Make a passive geometric barrier reject 9.39-in basketballs without trapping them. Position motors behind the frame, replace exact later motor models with legal 2024 choices, and preserve belt retention while one side deflects. The source does not prove identical grip on perforated hard balls; test worn electrolytes at speed and against walls before choosing covering/compression.

**2022 Team254, SIDEWAYS technical binder, physical p14:** a pneumatically deployed four-bar carries the primary pickup and smaller transfer roller to move cargo over the bumper. The published reason for dual compliant collectors is acquisition from either direction and yielding in contact. [Original binder](https://media.team254.com/2022/10/8f2407a5-Team_254_Tech_Binder_2022.pdf#page=14). Corpus note `tech-f93f8ab32955ff8090-77`.

Implementation: borrow the explicit primary-contact→secondary-contact→supported-interior transition. Do not install both 254 intakes or copy its 7-in cargo compression merely because they worked historically. One wide front intake is enough for this package; a rear discharge keeps pickup and scoring paths separate. This reference is about continuous capture, not an exact four-bar geometry promise.

### Hopper:604 linked sliding wall, redesigned around 100 delivered balls

**2026 Team604, Toploader linked sliding hopper:** intake deployment extends a sliding hopper, surgical tubing retracts it, walls use laminated corrugated plastic, and slots are locally reinforced with0.090-in polycarbonate. The team cites robustness, low mass and repairability with limited router access. Corpus note `604-expansion-2026-5`; source release Hopper section above. Original intake/hopper CAD views were inspected; hidden clearances and exact dimensions were not measured.

Implementation: a similar outward-sliding front wall adds volume while the intake is deployed. Keep every wall, belt, chute and actuator below 42 in outside the basketball dunk zone, including transient motion. Limit extension to 18 in beyond frame. Use reinforced slots and replaceable panels, but ensure a full load can retract or recover after a lateral hit. Linking the wall to intake saves one actuator but couples faults; test loaded interrupted deployment rather than only empty endpoints.

100 spheres of 5-in diameter occupy 3.79 ft³ of solid sphere volume. At an assumed 60% packing fraction, gross empty storage is about 6.31 ft³ **before** dead zones, wall slopes, conveyor and actuation. A28×28×14-in box is only 6.35 ft³, so it is not credible proof of 100 usable balls after hardware. Expand horizontally or increase legal interior height, and qualify capacity by balls actually delivered.150 is a stretch option, not baseline. No 604 or 1678 reported capacity is imported as a DunkTank measurement.

### Discharge:original broad conveyor and gated chute

I recommend a supported, reversible inclined live floor leading to a short chute above the tank's 24-in opening, while the whole mechanism remains below 42 in. Avoid a narrow single-ball serializer and high-speed launcher: neither long range nor individual shot aim is needed for the nominal 4-ft tank. The 120-degree open sector and closed lid make actual chute-to-tank alignment more restrictive than the nominal diameter suggests.

This conveyor/chute is a proposed design, not a mechanism claimed to exist on 604 or 254. Their transferable principles are continuous piece support, independent feed control and accessible wear parts. Use multiple guided ball streams through a broad throat, a positive stop gate, reversible agitator or floor action, and an output sensor arrangement tested against side-by-side balls. A count inferred from motor revolutions alone does not prove 100 entered the tank.

The important interface is low hopper floor→inclined conveyor→raised chute. Gravity does not move balls uphill over the tank lip. Check lift distance, ball rollback, bridging at the narrowing, re-ingestion after reverse and the final two balls. Count overshoot after stopping the gate; balls already in the chute can trigger a clear after the operator intended to stop at 99. Keep the chute out of field structures and opponent volume.

## Match policy

1. Start in own tank zone with 50 electrolytes. Discharge legally, then take the 6-point exit. Proposed auto target 31 points, with safe partner paths.
2. During early teleop, collect bucket-fed and loose electrolytes. Coordinate own clears with real hoop occupancy and partner refill rate. Deliver 100 from empty only when a clear is useful; fewer if partners already contributed, with reliable state confirmation.
3. Consider one center batch for qualification RP or a favorable multiplier window; never assume it is exclusively ours.
4. Keep a threshold-capable hostile batch available when denial is worthwhile. Complete the opposing clear before 20 seconds remain, with margin and only if the opponent lacks enough refill time. Do not contact a protected opponent or block access.
5. Return/stage toward own tank with useful inventory for direct endgame delivery. A hostile attack that strands the robot across the field can cost its own 33+ endgame points, so compare the complete route and score margin.

No live tank/hoop FMS data interface is promised in this manual. Provide operator confirmation and a conservative timer/state display rather than assume automatic knowledge. G14 protection is phrased differently for dunk-zone partial overlap and tank-zone full containment; review exact geometry. G12 prohibits blocking openings or flow. G21 requires humans to return basketballs within 30 seconds after a clear; withholding them is not our denial method. Ordinary bumper defense is secondary to useful electrolyte delivery; pins have a five-second limit here.

## Compared alternative and decision boundary

The internally compared alternative is a one-basketball elevator/wrist robot with a small electrolyte subsystem, aimed at independent low/middle/high access. It reduces partner dependence and can finish the 20-point-per-stack end bonus itself. However, its 90-in dunk needs the **bottom** of the 9.39-in basketball above the rim before release (organizer post 76), all height extension above 42 in must occur fully in the dunk zone (post 60), and its electrolyte subsystem still needs bulk loading/discharge to reopen high. It is a more demanding integrated package, not a free upgrade to this specialist.

I select the low bulk specialist as the single recommendation under the stated basketball-partner assumption. If two partners cannot reliably complete the 6/4 prerequisites and high finishing, or a full 100-ball route is so slow that clears add little basketball score, the role is invalidated. Forced clears alone do not justify a robot that cannot contribute throughout the match.

## First tests and release gate

- Full-size 100-ball mockup, actual 5-in balls, the proposed conveyor/gate and a 120-degree opening/lid proxy.20 loaded trials: proposed 100 delivered per qualified load, <=10 s emptying, no manual jam clearing, legal 42-in height throughout. Report residual inventory and count uncertainty explicitly.
- Pickup trials with dispersed/wall-adjacent electrolytes and basketball interference. Proposed 90/100 capture success at a declared speed, then impact/reverse tests. Do not transfer foam-ball grip assumptions to hard perforated balls.
- Timed loaded route tests or a geometry-grounded simulation for station/returned pile→own tank→opponent tank→own endgame position. Include approximately 10-s field-tank discharge, not just robot discharge rate.
- Partner refill test from empty 6/4/2. This establishes the own last-clear cutoff and whether an opponent denial window exists before 20 s. No arbitrary universal 25-s attack rule.
- Verify electronics service access, loaded CG/braking, legal 2024 electrical/pneumatic parts and the selected bumper rule set. The manual allows 2023 bumper rules or the specified 2025 alternative if declared. Do not silently import 2026 hardware legality.

No proposed test above has been performed. The fresh task workbook separates functional goals, recommendations, sources, acceptance targets and human decisions. Preserve this revision and update only after actual measurements or explicit user corrections.

## Exact sources for continuation

- Supplied `WCP DunkTank 2024 Game Manual.pdf`, Game Update01,19 pages. Scoring p3; supply pp7-8,13; stacks pp9-10; tanks pp11-12; human station p14; gameplay pp15-18; tournament pp18-19.
- [Organizer page2](https://www.chiefdelphi.com/t/wcp-cadathon-2024-dunktank/472262?page=2): post21 mixed possession;25 height limit.
- [Organizer page3](https://www.chiefdelphi.com/t/wcp-cadathon-2024-dunktank/472262?page=3): post60 full dunk-zone containment for extension.
- [Organizer page4](https://www.chiefdelphi.com/t/wcp-cadathon-2024-dunktank/472262?page=4):62 end-full criterion/opponent scoring;65 stack capacities;66 tank discharge;69 once-only final bonus;70 occupancy-independent clear;73 hostile clear;74 reduced preload;76 basketball bottom above rim;77 contact-side auto rule. Checked2026-10-26. The update87 link was inaccessible.
- [Field CAD](https://cad.onshape.com/documents/ae754cf4aa9650ad668b481f/w/1f51df44abe906e7a324481f/e/e57799ced4669a6a46d8e2c5). Source identified, exact dimensions not verified here.
- Corpus root is `FRC_Strategy_2022_2026_Database-main/FRC_Strategy_2022_2026/` from the supplied archive. Read `agent/robot_packets/2026-604.json`, notes604-expansion-2026-4/5 and originals `images/604_2026_intake.png`, `images/604_2026_hopper.png`; `agent/robot_packets/2022-254.json`, note tech-f93f8ab32955ff8090-77 and binder physical p14. These are reference-specific publication snapshots, not exhaustive installation histories.
