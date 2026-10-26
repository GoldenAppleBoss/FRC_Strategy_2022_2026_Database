# How to reason about a robot assembled from several historical references

A compound proposal is meaningful because experienced FRC people compress years of context into a few team names. The agent should expand that shorthand into functions, interfaces and conditional advantages. It should then check whether the resulting machine can work as a whole. This chapter uses the user’s proposed 2026 dumper as an example; it does not provide manufacturing dimensions or certify legality of a new design.

## Expand the phrase before judging it

“Dumper” identifies an intended pattern of high-rate batch discharge. It leaves unresolved how the robot acquires, stores, transfers, aims and recovers, and how often it can reach a useful batch. “Four-wide” proposes parallel delivery but does not establish that four lanes will remain fed or that their trajectories are consistent. “254 geometry” should be resolved to the particular year and source that explain contact, acceleration and spin; it should not be treated as a magic wheel ratio.

“2910-style slapdown” proposes a deployed ground-acquisition package. The database should return the documented linkage and protection arrangement for the intended version, while warning that the broad name does not specify kinematics. “Citrus-style expanding hopper” proposes using changing volume and possibly linked motion to store more fuel while meeting an envelope. It says nothing yet about whether the collector’s path and the floor’s path agree.

The first useful response is a precise restatement: a fixed, parallel-stream launcher fed by a controlled floor/tunnel, with a deploying collector and a storage envelope that changes between travel and scoring states. Then name the unresolved degrees of freedom. Is the robot intended to fit the trench full, empty or in a reduced-capacity state? Can it collect and fire simultaneously? Does deployment alter the floor? Is the shooter expected to change range while loaded? Those answers change which historical package is a useful starting point.

## Check the intake-to-storage interface

The collector must deliver fuel into a space that remains open through the deployment motion. A wide roller can move fuel faster than a narrow throat accepts it. A moving hopper wall can improve volume but pinch fuel at the handoff. A robust crash bar can protect the roller while preventing recovery of fuel near a wall. These are not reasons to reject the concept; they are the first places to test whether the chosen mechanisms agree.

Build a representative section with the actual bumper opening, roller position, floor, wall and transfer entry. Test scattered fuel, a dense pile, oblique approach and reversal. Include the deformed states that can plausibly occur in a match. Record retained, feedable fuel rather than only how many entered the robot. If the first test uses an open box with no bumper or moving wall, it has not tested the proposed interface.

## Check the storage-to-feed interface

Large storage creates multiple pressure and contact conditions. A full load can produce bridging or uneven lane fill; a nearly empty load can leave fuel stranded where agitation no longer reaches it. Turning can move the whole pile, and flexible boundaries can change the effective floor area. A feed path should be evaluated over the entire depletion curve.

The 254, 1678, 2910 and 1768 notes offer different ways of accelerating, staging and retaining fuel. Some eliminate a velocity reversal; others retain a geometry that worked in their own comparison. The existence of both is useful evidence against a universal S-path or J-path rule. The agent should state the desired contact history and compression, then explain which source demonstrates a similar condition. It should not choose a path shape solely because the label appears in a champion’s interview.

An important question is where excess fuel goes when one lane slows. If the only response is to compact the pile harder, a brief disturbance can become a full jam. An independently controlled entry, reverse policy, bypass or compliant surface may help, but each adds its own cost. The design recommendation should identify the recovery behavior before treating nominal flow as a solved problem.

## Check the feed-to-launcher interface

Wheel speed is not fuel exit speed. The entry condition, friction, compression, contact duration and interaction with a powered hood affect what leaves the robot. A four-wide drum can have uneven delivery across its width even if the drum itself is uniform. Shaft deflection, support placement, feeder geometry and occupied width all matter.

Measure trajectories from each portion of the effective width under realistic delivery. Include the first few fuel, a dense volley, a partly depleted hopper and worn fuel. Record misses and energy use along with release rate. A higher rate that increases misses can reduce score; a faster burst that leaves more residual fuel can increase the time before the next useful batch. The question is not whether the mechanism can eject quickly, but whether it can deliver controlled scoring quickly under its expected conditions.

The compact-turret alternative should be subjected to the same accounting. Continuous aiming can increase the useful shooting fraction, but the singulator, cable range and calibration can impose interruptions. Compare architectures with the same fuel distribution, battery condition and defense assumptions. A bench BPS comparison between one and four streams is not that experiment.

## Check the robot-to-field interface

Envelope, route graph and contact recovery are strategic properties. A taller hopper may gain capacity or a higher release point while losing a route and exposing another transit delay. A smaller chassis may escape more easily while reducing storage. A rounded or chamfered footprint can change how opponents apply rotational leverage, but it also changes available interior volume, bumper construction and service access.

Build a route model with states. For each route, specify the required configuration, expected travel time, likely queue and what happens if fuel is under the chassis. Include the transition time between states. If a hopper must retract before a passage, the robot needs somewhere for the fuel to go and a reliable way to recognize completion. “It fits in CAD” is insufficient without the loaded and interrupted cases.

## Check the robot-to-alliance interface

Two individually strong robots can fight over the same pile, occupy each other’s shooting region or collide during autonomous. A third supplier can improve output or increase congestion. A defender can help one scorer while forcing another to take a longer route. The architecture brief should state the intended alliance role and a plausible alternative when the expected partner is absent.

For a 2026 PCH rebuild, write several scenarios: a strong supplier, a weak supplier, contested midfield, denied return route and one disabled partner. Estimate useful output in each with uncertainty bounds. These estimates are model inputs, not source facts. Test the scenario that most threatens the architecture’s advantage. If a design only works when two exceptional suppliers maintain a perfect floor pattern, the team should know that before it builds the dependency into the machine.

## Use quantitative goals without false precision

A useful requirement has a metric, condition, target, confidence and deadline. “Score more than last year’s winner” lacks a role and condition. “Empty a useful full load at the chosen defended location before the active interval ends, with a known residual count and a recovery policy” can guide an experiment. Historical benchmarks can calibrate ambition, but the individual contribution still depends on partners and rules.

Use a simple model to identify the dominant term, then improve it with observations. If the robot is starved for half its active time, improving peak release rate is unlikely to be the first priority. If it has full hoppers but cannot empty before the window closes, the feed/launcher becomes more valuable. If transit failures dominate, loaded ground interaction and route access matter more. If it repeatedly misses after contact, distinguish aim recovery from inconsistent exit conditions.

## Make the recommendation reviewable

For each candidate architecture, include a short source map and a long causal explanation. State which principles are retained and which interfaces must be designed anew. Preserve the failed experiments that set the design boundaries. Give a minimum integrated prototype, the observations that would reject the candidate, the fallback architecture and a calendar gate that leaves real practice time.

The database supports that process; it does not replace engineering judgment or validation. A recommendation is strongest when it tells the team exactly what new evidence would change it. That is how historical robot knowledge becomes useful design reasoning instead of a collage of successful-looking mechanisms.
