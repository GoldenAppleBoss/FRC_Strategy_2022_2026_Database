## Corrected architecture priority: fuel, not climbing

The central 2026 design question is how the alliance acquires, controls, retains and scores fuel. Climbing should not appear as a co-equal primary objective merely because the rules contain tower points. The user's correction is consistent with the stored event sample throughout the season, including PCH events before Worlds. The default architecture recommendation is to allocate mass, volume, power, practice and engineering time to useful fuel contribution. A climb needs a specific positive marginal case before it earns those resources.

This distinction matters at kickoff as well as in hindsight. A task inventory says what is legal; it does not say what deserves development effort. A point-value table cannot account for the hopper volume displaced by a climber, the day spent fixing its deployment, or the time the drivers lose practicing it. A calculator that compares only final seconds of scoring with final seconds of climbing is still incomplete. A robot can pay a climb's opportunity cost for the entire season without ever choosing to climb during an important match.

The numerical audit uses actual tower component fields from the stored match payloads, rather than EPA endgame estimates. It excludes missing components instead of converting them to zero. In 2,237 valid Worlds-division alliance performances, 95.4% record zero teleop tower points; the mean is about 0.60. All 32 Einstein alliance performances record zero autonomous and teleop tower points. In the sampled PCH week-3 event, 91.8% of 146 alliance performances record zero teleop tower points; week 5 has 93.3% of 150; DCMP has 89.0% of 210. Week-1, week-2 and week-4 samples likewise show tower scoring as a minor exception. The detailed denominators and missing-field counts are in `data/tower_summary_2026.jsonl`.

These are selected historical event records, not an exhaustive census of every 2026 match. A few nonzero tower scores establish that climbing happened; they do not make it a central architecture priority. Nor does a large value in a field named endgame establish a climb: 2026 endgame also contains substantial fuel scoring. Component EPA can be negative because it is a model estimate, so it cannot serve as a physical climb count. The agent must use the actual tower fields for this distinction.

There is direct technical evidence for the opportunity-cost interpretation. [2046's binder, PDF page 32](https://drive.google.com/file/d/1YBlY312kMTiV29boVv6xRt87foDIU9lk/view?usp=sharing#page=32) says the team dropped a six-pound, ten-point climber that occupied hopper volume. [6800's DCMP binder, PDF page 8](https://drive.google.com/file/d/11rQrMwCIseY18JbKFytGLXSd__x1JP1S/view?usp=sharing#page=8) says its earlier telescope did not compete at districts because of weight constraints and higher-priority scoring work. These are accounts of particular teams' decisions, not an assertion that every robot had the same development path.

## Resource control does not excuse a fuel path that cannot meet its job

Passing, denying supply and preparation for the next shift remain central. The failure mode is to use a plausible alliance strategy as a substitute for integrated performance. [2910's original brief](https://drive.google.com/file/d/1jPf-aOGhz0dntoAgahFBgRhJiJv9rGpj/view?usp=sharing) explains the minimal-hopper, dual-intake passing hypothesis. [The rebuild brief](https://drive.google.com/file/d/1r-6zR4afbr_BpeZfWwcM5XL1N74FjScI/view?usp=sharing) explains why its actual throughput, scoring and partner dependence did not justify that package. The replacement changes storage, pickup kinematics and the entire feeder/scorer interface. It is not simply the same robot with one more lane.

That history should remain available to the agent as a falsified local hypothesis. The original strategy had a coherent resource argument: move fuel to an area where partners can score it. Its weakness was the conjunction of assumptions needed to make that role valuable under real competition conditions. Recommending a similar architecture requires tests of useful delivered fuel, recoverability of the resulting pile, autonomous compatibility, self-scoring when partners fail and performance under denial. It cannot rely on a future partner solving every missing function.

Likewise, the observed spread of drums should not turn into an instruction to maximize lane count. A third or fourth lane can increase the nominal launch ceiling while making indexing, current or structure worse. The mechanism notes document changes to floors, backing, transitions, rigidity and service access because those interfaces determine whether the ceiling is realized. A compact turret can remain strong if it is supplied and accurately firing for more of the usable time. Compare complete operating policies under the same fuel distribution and defense, including the final few balls and depleted battery.

For a PCH rebuild, the resulting goal hierarchy begins with reliable acquisition, retained and deliverable capacity, repeatable useful output, route access, jam recovery and survival. Autonomous and shift-transition preparation belong in that same fuel model. Tower capability is a separate, low-priority exception. This hierarchy is now the default for the agent rather than an optional caution buried after a rules summary.


# REBUILT: high throughput must survive the inventory cycle

The base chapter provides the rules and stage benchmarks. This supplement connects the reviewed early-season RoboReplay predictions with later team explanations and reported match context. The available RoboReplay caption review reaches the week-2 viewer analysis; later 2026 video announcements are inventoried but their transcripts were blocked. Therefore this is not a RoboReplay-backed account of every late-season match. The existing Einstein ledger remains explicit about reported tactics and absent visual audits.

## A hopper stores time only under specific conditions

A starting inventory can let a robot keep firing while it searches for the next useful pile. That is the intuition behind calling capacity a time buffer. But the conversion depends on the firing rate, the collection rate, whether collection and firing can overlap, and how much of the nominal inventory is actually feedable. A hopper whose last fuel bridges above the entry does not deliver its photographed capacity. A hopper that must be emptied before the robot can use a route also stores a more constrained resource.

For a simplified interval with firing rate `s` and simultaneous intake rate `a`, the depletion time of a useful starting inventory `H` is `H / (s - a)` while `s > a` and those rates remain valid. With no simultaneous acquisition it is `H / s`. These are explanatory bounds, not predictions of a real robot: misses, jams, alignment pauses, acceleration and changing fuel density all change the rates. The useful design question is which assumption dominates the team’s intended play.

This model also explains why “more BPS” can make a supply problem worse. A faster scorer empties the same buffer sooner. If replenishment or access is the limiting process, a new drum may increase bench output while leaving active-window score almost unchanged. The team should measure full acquisition-to-discharge cycles and time spent starved before committing to the higher-rate architecture.

## Fixed shooters and turrets expose different dependencies

A fixed multi-lane shooter can put many fuel through at once, but needs a useful chassis orientation and a reliable way to preserve or recover that orientation under contact. A turret can allow more acquisition directions while aiming, but needs continuous singulation, usable angular range and calibration that survives motion. Neither description establishes the winner. The comparison depends on the achievable rate multiplied by the time that rate remains accurate and supplied.

The reviewed early videos discuss bracing a fixed shooter against field geometry, using blind areas, self-passing and mobile firing. These are observations and forecasts tied to particular configurations. Bracing can reduce rotational disturbance while constraining escape; a turret can compensate for heading changes while still being starved or prevented from reaching fuel. A defender can attack transit or inventory instead of directly defeating the aiming mechanism.

The 4414 deep note provides a complementary later team account: small turret swept volume, large low rotor and storage integration, with empirical calibration and a deliberately chosen autonomous. The 254, 1678, 2910 and 1768 dossiers expose different floor, preacceleration and rebuild choices. A recommendation should compare those complete packages rather than pretend a turret is an accessory to any hopper or a wide drum can replace any shooter without changing the floor.

## Storage and mobility are a state machine

Trench access is not just an overall height specification. The robot may have a compact travel state and an expanded scoring state; flexible walls, retained fuel, intake position and moving floor geometry affect whether the transition is safe. The loaded state can change the center of mass, ground interaction and the ability to slide off fuel. A mechanism that fits when empty can fail when the hopper is packed or when a wall deflects during contact.

The 1768 note shows how a lower four-bar link carried hopper geometry while satisfying several constraints. The 1678 dossier explains why its expansion and path had to be developed together. Those are examples of coupled design, not interchangeable parts. Before borrowing the collector from one team and storage from another, define the physical handoff between them in both directions and through every intermediate state.

Useful tests include partial fill, full fill, final-fuel evacuation, a forced reverse, a sideways hit and loaded travel over representative terrain. Also test a deployment that is interrupted halfway through. The question is not whether the mechanism eventually reaches both endpoints; it is whether the robot stays useful when the match prevents the ideal sequence.

## Scoring windows make return timing a mechanism requirement

An inactive period can be spent acquiring, passing, stealing, defending, repairing the field’s supply pattern or returning to the next scoring position. The last choice can be easy to undervalue because it adds no immediate points. A full hopper that arrives late can miss the interval that made the capacity valuable. A robot that empties quickly can tolerate a later arrival only if its approach and aim are reliable.

The reviewed kickoff and build-season videos forecast advantages from shift order and transition preparation. Later early-season reviews discuss actual delays, beaching and matched opportunities to assess the score. Preserve that chronology: a prediction that winning auto always determines the match is too strong, while an observed difference in preparation time can still be important. Current score before equal opportunities can mislead a coach; the remaining inventory and route access matter as well.

4414’s team explanation of rejecting double-swipe auto variants is a useful counterweight to a simple “collect more in auto” rule. The stated constraints include available firing time, transition endpoint and partner compatibility. That is a full-system optimization. It should be re-evaluated if the opponent does not create the expected fuel distribution or if a local partner occupies a different route.

## Resource control changes the value of a third robot

A supplier can add score indirectly by keeping a strong scorer’s useful area replenished. A defender can add value by denying replenishment, a route or the ability to return before the shift. A third scorer can instead reduce congestion by working a different region, or can create more traffic than output if all three need the same pile. The right role depends on measured supply and partner capability.

The early 2910 analysis is especially valuable because it forecasts that better future suppliers could make the hopperless concept work. The later team account reports unmet targets and a complete rebuild. Preserve both. The original argument was not nonsensical; it depended on assumptions that did not satisfy the team’s actual schedule and operating targets. An agent should identify that dependency and offer a test, rather than present the final successful architecture as the only idea anyone could reasonably have chosen.

The later 7415 discussion adds a distinct, out-of-sample example of a swappable hopper and opponent preparation. It belongs as a strategic case with attributed team claims, not as an extra top-25 dossier or proof that every alliance should swap its envelope. Modular capability has value only if it remains legal, reliable, practiced and compatible with the rest of the robot when changed.

## Converting high-end examples into PCH goals

Set goals for usable capacity, collection from realistic fuel distributions, delivered fuel per active window, defended-shot accuracy, route access, jam recovery, current draw and repair time. Associate each number with the configuration and fuel condition that produced it. Fresh-fuel bench rate, worn-fuel event rate and full-match average are different records. The 1768 October feeder improvements and 254’s reported firing range should never be collapsed into one universal drum rate.

Use the historical week-3, week-5 and DCMP references as observed alliance outcomes. They do not tell an individual robot how much it must score alone. Choose the contribution your likely partners need and keep a path to the later stage. For a rebuild, preserve enough time to validate the whole chain. A smaller, tested change to an intake, floor or feed interface can be more valuable than adding another lane that the robot cannot supply. At Worlds and Einstein, return to the actual lineups and match-specific evidence; the final score by itself cannot identify why one architecture prevailed.
