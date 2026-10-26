"""Original analysis. Factual clauses refer to PDF pages; inference is separate."""
RECORDS=[]
def add(bid,subsystem,title,pages,facts,reason,analysis,test,limits='The binder is a published configuration snapshot, not an independent durability or match-rate test.'):
 RECORDS.append(dict(binder_id=bid,subsystem=subsystem,title=title,pdf_pages=pages,construction=facts,team_stated_reason=reason,engineering_analysis=analysis,recommended_validation=test,limitations=limits))

# 2026: design history must accompany the successful configuration.
add('75601cba410631181a','intake','Original BLITZ: two mirrored four-bar collectors',[5,8],
 'Dual four-bars; X44 deployment at 79.37:1; separate X60 roller drives.',
 'Collect sideways while passing; collapse under impacts.',
 'This is a coupled routing decision. Collecting on either side allows the chassis to translate across a fuel pile while its fixed shooter points toward the destination. That can recover some of the directional independence normally purchased with a turret. A four-bar can also move backward under a frontal impact, but only if the linkage, motor controller, chain and hard stops permit that motion. More joints create more wear locations, and both collectors consume the space that another architecture could use for a hopper. The second intake should therefore be evaluated by additional useful fuel delivered, rather than the visual symmetry of the mechanism.',
 'Compare opposite-side sweep paths against turning a single-intake robot, including one damaged linkage and time to replace it.')
add('75601cba410631181a','transfer','Original BLITZ: serpentine inventory and passing',[5,9],
 'Serpentine conveyor, two X60 feeder motors, three X60 shooter motors; variable hood.',
 'Use the alliance zone as storage for a passing-centered role.',
 'The low-storage concept treats the field as an external buffer. Its success requires the alliance to recover that buffered fuel at the right time and place. Passing capacity and scoring capacity are different services even when the same launcher performs both. A continuous serpentine can constrain fuel well but adds contact length, curved transitions and friction; a well-controlled ball path may still be unable to supply enough mass flow. This original brief must be read alongside the later rebuild account: a design rationale is evidence of a hypothesis, not evidence that the hypothesis met the team’s competitive targets.',
 'Measure fuel moved to a recoverable location, residual path inventory, and scoring available after the passer returns; vary partner collection quality.',
 'The brief describes a 25-fuel/s feed capability; the later account reports inadequate overall performance. Do not treat that number as an independently demonstrated match average.')
add('6d8168bcbb62d71a38','intake','RE-BLITZ: strengthened slapdown',[7,9],
 'Four-bar replaced by slapdown; 0.6-inch plates; #35 deployment chain; powered bottom roller.',
 'Strength, service access and reliable full-speed acquisition.',
 'A single pivot simplifies the force path: an exposed roller loads its arms, pivot and hard stop without several moving links sharing the impact. That does not make it automatically more impact tolerant. The stronger arm and larger deployment chain need a corresponding chassis attachment and a stop that can react a collision without loading the gearbox teeth. Powering the lower contact also matters at the bumper transition: fuel can otherwise be caught between a moving upper roller and a stationary surface while the robot continues advancing. Plate stiffness and ball transport are separate improvements and should be tested separately.',
 'Test a wall hit and an oblique corner hit, then remeasure roller alignment and deployment current; test full-speed pickup of worn fuel.')
add('6d8168bcbb62d71a38','transfer','RE-BLITZ: preserve width through the floor and tower',[7,10],
 'Ten inclined floor rollers; four-X60 feeder; Teflon backing; enlarged four-wide path.',
 'Remove restrictions between hopper and launcher.',
 'Adding a fourth release lane helps only if four lanes remain supplied. A floor feeding a narrow or irregular throat produces alternating bursts and starvation even when the drum has ample power. Inclination and backing determine the normal force and the direction in which fuel escapes when multiple balls arrive together. Low-friction backing reduces the energy lost to sliding while powered rollers maintain forward contact. An open path also needs a controlled final approach: a ball entering the launch contact at a variable velocity or height changes compression and the exit state. Diagnose the last few balls separately from the first dense volley.',
 'Log feeder current, wheel speed and scored output through a full hopper; repeat with 5, 15 and 30 fuel and with deliberate asymmetric loading.')
add('6d8168bcbb62d71a38','scoring','RE-BLITZ: drum, hood rollers and flywheel recovery',[10],
 'Four-inch drum, 1.5-inch hood rollers, overdriven flywheel; team reports >30 fuel/s and a 34 maximum.',
 'High discharge rate with manageable shooter recovery.',
 'A drum’s useful contact surface is a distributed launch interface. If fuel encounters different compression along its width, the nominally identical lanes can launch at different speeds. Flywheel energy can cover short impulses while the motors replace average energy, but a dense volley still requires sufficient sustained electrical power. Surface condition, ball wear and hood contact determine how much of the wheel’s speed becomes translation versus spin. The reported rate is valuable as a team result; it does not establish accuracy, defended performance, battery condition or an all-match average. Copy the geometry only with a plan to characterize those conditions.',
 'Measure per-lane velocity and accuracy before and after a long volley; log loaded battery voltage and recovery between successive shots.')
add('6d8168bcbb62d71a38','storage','RE-BLITZ: expansion actuated by the intake',[7,11],
 'Intake-driven hopper expansion; smooth internal sheet-metal joints; deployed one-way catchers.',
 'Store useful inventory and feed it back toward the shooter.',
 'The expanding walls and intake form one mechanism state machine. A wall that expands independently without managing its overlap can create a ledge, trap fuel, or fight the intake during retraction. Smooth fasteners reduce snagging, while the deployed catches react loads that should not be carried continuously by the intake motor. A large hopper helps separate acquisition from discharge, giving the driver freedom to reposition. That freedom disappears if the final fuel cannot leave without a specific intake movement. The recommendation should therefore specify both the retained capacity and the emptying sequence.',
 'Interrupt deployment halfway with a full hopper; test reverse motion, ball trapping at panel overlaps, trench travel and final-fuel evacuation.')
add('6d8168bcbb62d71a38','controls','RE-BLITZ: mechanism readiness and fallback operation',[12,13],
 'Shot gates, vision-based targeting, CANrange preload sensing and fixed-position manual fallbacks.',
 'Coordinate feeding with the actual launch state.',
 'A high mechanical ceiling can be lost to premature feed. The feeder must distinguish an intentional firing pause from a jam, an empty hopper and a shooter that has not recovered. Readiness should use measured values with hysteresis rather than one noisy threshold. Manual known-position shots preserve a useful degraded mode when localization fails, but require practiced driver cues and a stable mechanical zero. A mechanism database needs this control contract because an intake, indexer and drum borrowed from different robots may otherwise disagree about who owns the next ball.',
 'Disable one camera, introduce an empty-hopper sensor error and force a heading correction mid-volley; check the operator can recover predictably.')

add('9edf90221b2e646336','intake','BEARRICADE: collector evolution and impact reinforcement',[22,23],
 'Three rollers; dead-axle polycarbonate tubes; later metal stub-axle reinforcement.',
 'Remove pickup dead zones and improve impact survival.',
 'A compliant tube may survive bending while its end attachment fails. That makes the stub axle, bearing retention and local side-plate load path as important as the roller material. A lower transition roller closes the region where a single upper roller can push fuel rather than capture it. More contact points can improve acquisition, but they also add belt drag and opportunities for a ball to be over-compressed. The relevant question is whether the ball experiences a continuous forward velocity through the bumper transition, including when the robot is moving and the hopper is already full.',
 'Film pickup from the side at maximum approach speed; inspect stub-axle displacement after repeated oblique hits.')
add('9edf90221b2e646336','storage','BEARRICADE: linked hopper and capacity states',[24,25],
 'Collector-linked sliding walls; net; reported 60 fuel under trench and 75–80 over bump.',
 'Increase useful storage without losing the travel state.',
 'These capacity figures describe different operating envelopes, not one universally available volume. A net can retain the top layer while allowing a changing envelope, but it adds elastic forces and can push fuel into the throat or against a wall. Sliding walls need enough overlap to remain guided under a side load without creating an inward shelf. Coupling deployment to the collector saves an actuator and synchronizes the opening, but also couples hopper faults to pickup. A good borrowed implementation preserves service access and allows the robot to recover when only one side deploys correctly.',
 'Measure retained and feedable capacity after loaded bump travel, then test deployment with a damaged slide or displaced net.')
add('9edf90221b2e646336','transfer','BEARRICADE: why the belt bed became rollers',[17,18,26,27],
 'Belt bed abandoned; ten 1.25-inch rollers, successive 21:20 speed steps, two X44s.',
 'Belt tension and ball motion were limiting the early design.',
 'A belt bed pulls continuously on its support shafts; the tension required to transmit power can bend those shafts even before fuel loading is considered. A roller floor moves that challenge into shaft spacing, surface grip and transmission design. Incrementally faster rollers can stretch spacing between balls, but only if the fuel actually follows the surface and does not simply slip. Agitation is not automatically helpful: repeated upward kicks can keep a ball from settling into the receiving contact. This is why a rate test must observe the inlet to the superstructure, not only the speed of the floor.',
 'Measure time to empty under several fill levels, compare stepped speeds against equal speeds, and count time balls spend recirculating at the inlet.')
add('9edf90221b2e646336','scoring','BEARRICADE: integrated S-path and two-lane drum',[28,29,30,31],
 'Four-inch drum; printed backing; hood range −10° to 60°; triple-lane prototype became dual.',
 'Match launch capacity to indexing and preserve packaging.',
 'Reducing lane count can improve the robot if the extra lane forces a worse feeder, more current or a larger structure. The S-shaped path is an integration choice, not a universal superiority claim over a J-shaped route. Negative launch angles create a specific close-to-hub shot envelope; they need geometric clearance and empirical tuning, especially where the robot is braced against a field element. Integrating shooter and tower plates can remove redundant material and align contact surfaces, while increasing the consequence of damage to that shared structure. The same binder also shows a turret concept; that image alone does not prove it competed.',
 'Test near-hub reverse shots and far shots at depleted battery; inspect integrated plate deflection while the feeder is fully loaded.')
add('9edf90221b2e646336','endgame','BEARRICADE: delete the low-value climb',[6,32],
 'The team rejected a six-pound, ten-point climbing package that occupied hopper space.',
 'Fuel contribution outweighed the mechanism’s opportunity cost.',
 'This is direct team evidence for treating climb as a low-priority 2026 architecture choice. Its cost is larger than its actuator and hook: it can remove storage, require alignment practice, complicate wiring and consume testing that could improve fuel flow. A calculation that includes only seconds spent climbing misses those development and packaging costs. Conversely, a near-free existing device could have a different marginal cost. The agent should begin with the observed fuel-dominant game, then require a specific positive marginal case before adding climb. It should not recommend one merely because the manual awards points for it.',
 'Compare scored-fuel loss from displaced volume and lost testing time against the expected climb contribution in the intended event role.')

add('86ae539d8a57982e4c','intake','DESPERATE MEASURES: linear collector as a controllable spring',[8,9],
 'Double-layer polycarbonate rack; two 2-inch rollers; low-stator-current deployment.',
 'Large acquisition area with passive impact retraction.',
 'A backdrivable, current-limited rack can yield during a collision rather than make the gearbox a rigid stop. That behavior depends on friction, reduction, acceleration limits and the controller remaining enabled; it is not supplied by polycarbonate alone. Stacking a structural plate beside the rack allows the designer to distribute load without relying only on gear teeth. A paired-roller collector should preserve positive contact as fuel crosses the bumper. The matching chassis and slide must react lateral hits, because a low-current motor primarily helps the axial direction.',
 'Measure peak rack load during frontal and sideways impacts; check tooth engagement and deployment after the test.')
add('86ae539d8a57982e4c','storage','DESPERATE MEASURES: active floor and inventory policy',[10,20],
 '1.5-inch powered floor rollers; net; CANrange minimum-inventory control while passing.',
 'Keep fuel available for the next scoring shift.',
 'Inventory sensing changes the job of a passer. Passing every available ball can improve the alliance pile but leave this robot empty when the shift turns. A minimum reserve is a control policy tied to how quickly the robot can refill, return and shoot. A distance sensor sees a local surface, not a perfect total count; a sloped or bridged pile can produce the same reading at very different usable inventories. The threshold needs validation under different pile shapes and while accelerating. Reserve logic should have an operator override when alliance strategy intentionally assigns all fuel elsewhere.',
 'Compare sensor reading with deliverable inventory for uneven fills and motion; measure reserve adequacy at the start of each shift.')
add('86ae539d8a57982e4c','transfer','DESPERATE MEASURES: constrained belts and collision sorting',[12,13],
 'Two rubber-coated conveyors, printed carryways, vertical kicker, quarter-pipe feed.',
 'Turn bulk fuel into a reliable stream.',
 'The carryway controls the support beneath the belt so compression does not change with belt sag. The vertical kicker addresses a different failure: two balls arriving at the quarter-pipe entrance can lock each other before either is captured. That distinction matters when diagnosing a singulator. Increasing belt speed does not necessarily release an arch; changing relative contact directions or reversing one element can. The quarter-pipe must preserve contact through the bend and deliver fuel at an appropriate velocity to the turret. A compact throat earns hopper space only if it remains serviceable and can clear a hard jam.',
 'Feed deliberately paired balls and partially collapsed fuel; log current signatures before and after reversal and inspect carryway wear.')
add('86ae539d8a57982e4c','scoring','DESPERATE MEASURES: compact turret and continuous hood',[14,15],
 'Eight-inch bearing; ±185° turret; 4-inch Fairlane wheel; separate backspin kicker; variable hood.',
 'Score and pass across a broad envelope.',
 'The bearing and base plate must keep the launch contact aligned while the chassis accelerates and balls enter the shooter. Independent back contact permits spin tuning without changing the main wheel, but also introduces another speed and recovery condition. A range slightly greater than one turn reduces the frequency of an unwind; it does not create unlimited rotation. The cable chain must survive the worst combined hood and turret state. For a recommendation, the compact swept envelope and the singulator’s feed location are as important as the shooter’s wheel diameter.',
 'Map accuracy over turret angle and hood angle, including near both cable limits and under representative chassis acceleration.')
add('86ae539d8a57982e4c','versions','DESPERATE TIMES to DESPERATE MEASURES',[2,24],
 'Original hopperless four-to-two-to-one path replaced; turret reused; Orbit 1690 explicitly credited.',
 'Original throughput did not justify minimal storage.',
 'This is a valuable negative result because it separates the concept from its execution. A narrowing conveyor can spread fuel longitudinally as it accelerates, yet still fail to maintain sufficient launch supply. Without a hopper, every interruption in acquisition becomes an interruption in scoring. Reusing the turret preserved calibrated software and known interfaces while the rest of the architecture changed. The proper historical record includes both machines and the transition; the later successful package should not be projected backward onto the initial competitions or treated as a season-long fixed architecture.',
 'For a rebuild, identify which calibrated interfaces can survive unchanged and which performance assumptions require new integrated testing.')

add('df1392177a72d1aa1e','intake','CYCLONE: collector and frame share the impact path',[8,9],
 'Full-width linear collector; 1.125-inch rollers; load-spreading hubs and washers.',
 'Acquire five columns and survive contact.',
 'An exposed roller’s compliance must be paired with a force path into the chassis. A small washer can concentrate force and start a crack even if the main plate is otherwise flexible. Distributing that load across a hub or a larger washer reduces local pressure, but the joint must still allow the intended movement. The collector width also has an autonomous geometry consequence: it changes which fuel columns can be reached without the chassis crossing a contested route. A width figure should be linked to the effective acquisition envelope rather than merely the distance between arms.',
 'Map acquisition success across the entire mouth with off-center hits, then repeat after controlled impact loading.')
add('df1392177a72d1aa1e','transfer','CYCLONE: DYE-inspired rotor with independent feed',[10],
 '22-inch rotor; eight-fuel ring; separate rotation/feed drives; reported 18-fuel/s feed.',
 'Maintain bulk-to-single-stream flow in a compact package.',
 'A rotor is not just a rotating bucket. Its moving boundary, internal feed contact and exit geometry jointly determine whether fuel circulates, enters the ring, or jams. Independent feed drive lets the team tune the launch supply without requiring the whole bulk pile to turn at that speed. A lower-profile center obstruction improves the area through which fuel can enter; reversing must not turn a hook or seam into a trap. A theoretical ring count multiplied by rotation rate is only an upper bound: pockets must actually fill and discharge.',
 'Measure pocket occupancy and output variability at full, half and nearly empty loads; test reversing a deliberately bridged inlet.')
add('df1392177a72d1aa1e','scoring','CYCLONE: floating hood, preload and turret support',[11],
 'Compact turret; floating hood; constant-force spring; through-bore sensing; powered hood rollers.',
 'Reduce backlash and preserve storage volume.',
 'Spring preload can keep a reduction loaded against one tooth flank, reducing reversal uncertainty, but adds a torque that the motor must overcome in the opposite direction. Measuring the output rather than only the motor helps detect residual compliance between gearbox and hood. The feed path and turret bearing need common structural alignment; a compact height is valuable only if it does not permit the hood to deflect enough to change the exit angle. Powered hood rollers alter the spin/contact state, so their ratio belongs in the shot calibration rather than being treated as passive guidance.',
 'Measure hood angle repeatability from both approach directions and at several turret headings; compare loaded and unloaded structure.')
add('df1392177a72d1aa1e','controls','CYCLONE: moving-shot compensation and variable feed',[13],
 'Gyro latency compensation, empirical flight time and variable rotor speed are documented.',
 'Maintain accurate mobile firing and stable throughput.',
 'A turret can cancel chassis heading only if the controller uses the correct observation time and the actual release state. A latency error grows with angular velocity and can look like a mechanical aiming bias. Rotor speed also changes shot timing and inlet loading; a firing command is not the same as a ball leaving the hood. The mechanical and control record should include this delay and its variation. Slowing the feed may improve delivered score if it reduces wheel droop or keeps the exit state within tolerance.',
 'Time-stamp vision, gyro, turret position, feeder transitions and ball release; compare miss direction against angular and translational velocity.')

add('1e35160c2e3b44126d','intake','3467: redundant rack support and expanding walls',[9,10],
 'Double polycarbonate rack plates; powered and idler pinions; walls move with intake.',
 'Impact tolerance, tooth engagement and more storage.',
 'Supporting a rack at more than one point reduces its tendency to peel away from the drive pinion under load. Two rack plates can distribute stress, but only if their tooth timing and guidance are aligned; otherwise they can fight each other. Moving the walls with the collector creates agitation as well as extra volume. Agitation may improve flow near the floor but can also throw a top layer out unless the lid and wall overlap control it. A side load remains a separate case from a frontal collapse.',
 'Test rack deflection, skipping and skew with a side hit; observe fuel near moving wall seams during repeated deploy/retract cycles.')
add('1e35160c2e3b44126d','transfer','3467: active centering into two launch streams',[11,12],
 'Ten floor rollers; powered stacked-belt side wedges; central divider; live-axle tower roller.',
 'Center fuel while limiting tower oscillation.',
 'Active side contact can rotate or translate fuel away from a bottleneck rather than relying on gravity against a fixed wall. Its surface direction has to agree with the desired stream; excessive inward force can create an arch at the divider. The live-axle tower roller is a structural answer to rapidly changing multi-ball loads, reducing a source of compression variation. The useful comparison is not simply belts versus rollers: it is whether the particular contact geometry establishes two repeatable, supplied paths through the entire range of hopper fill.',
 'Feed off-center piles, log each stream separately, and compare tower deflection under single-ball and paired-ball arrivals.')
add('1e35160c2e3b44126d','scoring','3467: two independent launchers and stored energy',[13,14],
 'Two launchers; four 3-inch 45A wheels per launcher with inertia kits; adjustable hood.',
 'High rate with controllable exit conditions.',
 'Independent launch drives can compensate for asymmetric supply, but increase the number of conditions that must be measured. Added inertia can reduce transient speed droop while consuming mass and spin-up time. A soft wheel increases compliance and contact duration, but changes compression as it wears or heats. Hood range should be translated into a validated scoring and passing envelope, rather than assuming every geometric angle produces a useful trajectory. The desired test is a full stream of representative fuel, not a single ideal ball launched repeatedly.',
 'Compare both streams’ exit speed distributions and accuracy through a long volley, at fresh and worn surface conditions.')
add('1e35160c2e3b44126d','controls','3467: camera structure and predictive trench ducking',[15,19,20],
 'Braced camera towers; measured shot gates; future-pose hood retraction for trench entry.',
 'Preserve localization and avoid hood collisions.',
 'Camera vibration produces an apparent pose error even if the vision algorithm is otherwise correct. Bracing the mount to the shooter can stiffen it, but also transmits shooter vibration; the net effect should be measured. Trench protection is a dynamic clearance problem: retracting at the boundary is too late when the mechanism takes time to move. The lookahead should include speed, control delay, deceleration and an uncertainty margin, with a safe fallback if localization becomes invalid. This is a control requirement created by the mechanism’s envelope.',
 'Run approach tests at several speeds and headings with degraded pose data; verify the hood clears before the physical entry plane.')

add('7a7e0a4611c12ba4f1','intake','DOWNPOUR original: linear collection and linked hopper',[11,12],
 'Rack deployment, multiple powered rollers, pin-slot hopper extension.',
 'Compact stow and broad acquisition.',
 'The intake and expanding wall are physically linked, so their travel, friction and alignment cannot be optimized independently. A pin-slot joint can accommodate different trajectories but may create a high local pressure at the end of travel. A multirotor pickup needs enough overlap to avoid an uncontrolled interval as fuel crosses the bumper. If the linkage binds, commanding more motor torque can damage the rack before solving the wall alignment. The architecture should retain a way to inspect and replace the joint without disassembling the whole fuel path.',
 'Cycle the linkage under hopper side loading and inspect slot wear; test an interrupted deployment and recovery.')
add('7a7e0a4611c12ba4f1','transfer','DOWNPOUR original: serpentine and turret feed',[13,14,15],
 'Belt serpentine; curved backing replaces interfering upper wheels; 400° turret.',
 'Compact routing with controlled feed and independent aim.',
 'Removing a wheel can improve a mechanism when the wheel occupies the same space needed by another moving assembly. Curved backing trades active contact for sliding contact and must keep fuel captured through the bend. The turret’s rotation range is a cable-management specification as much as an aiming specification. The original design and its later replacement are separate records: a successful collection system does not prove the single-stream scorer met the team’s later competitive needs. Prototype targets must remain labeled targets even when the surrounding prose sounds confident.',
 'Sweep the full turret range while feeding deliberately varied fuel, and compare useful output with the original target under realistic voltage.')
add('bae3039bd0aeeccdcb','intake','DOWNPOUR DCMP: repair the collision path',[4],
 'Single-pivot intake; higher round bash bar; extra motor-plate bracing; passive lower bar.',
 'Stop bar deflection from stalling rollers; save power and weight.',
 'A bash bar can become the failure if it bends into the very roller it protects. Moving the reaction member above the rotating contact changes that failure geometry. Reverting a powered element to a passive surface is an important counterexample to the rule that more powered contacts always help: the added drive may cost current without improving capture in the tested geometry. This result should not be transferred blindly to another bumper gap or approach speed. It supports testing the actual bottleneck and force path before adding a motor.',
 'Measure bar-to-roller clearance after impact; compare capture probability and current with powered and passive lower contact.')
add('bae3039bd0aeeccdcb','storage','DOWNPOUR DCMP: net, trench access and electrical relocation',[3,5],
 'Net-topped storage; bumper-mounted panels; electrical panel flipped upward.',
 'Retain fuel, use trench routes and protect electronics.',
 'A bumper-mounted wall can simplify robot mass allocation but introduces a service interface: removing or shifting the bumper can change hopper alignment and expose a gap. The net adds a travel envelope that depends on fuel loading and deformation. Flipping the electrical panel exchanges one exposure for another, so the skid plate, drainage and access plan must be considered with the new layout. The correct capacity test measures fuel retained after the actual route and then delivered to the shooter, rather than the empty CAD volume.',
 'Remove and reinstall bumpers repeatedly, inspect wall alignment, then run full-load trench and bump routes followed by complete discharge.')
add('bae3039bd0aeeccdcb','scoring','DOWNPOUR DCMP: single-stream turret to four-wide drum',[2,6,7],
 'Four-wide transfer; mixed-diameter rollers; three X60 shooter drives and two feeder drives.',
 'Original single stream was too slow for the intended competition level.',
 'The rebuild changes both the launcher and the supply path. Wider discharge without wider feeding would preserve the original restriction. Gradually accelerating fuel can reduce crowding before launch, but it must preserve contact and avoid forcing balls against a stationary roof. The strategic claim is specific to this team’s execution and operating conditions; it does not invalidate compact turrets that achieve a different combination of capacity, sustained firing and maneuverability. Preserve the original development and the district-to-DCMP transition so a recommendation can learn from the pivot rather than only its final appearance.',
 'Compare complete cycle score against the original under the same fuel supply, defense and active-window timing.')
add('bae3039bd0aeeccdcb','endgame','DOWNPOUR: proposed telescope and later compact hooks',[8],
 'Original telescope did not compete at districts; later pivoting hooks replaced it.',
 'Weight, space and scoring priorities displaced the initial climb.',
 'The presence of a climber CAD image in an early binder is not proof it was installed or used. The later brief supplies a useful version boundary by explicitly saying the earlier mechanism did not compete. The new hook package should be recorded as a compact capability, not evidence that climbing became strategically central. In a fuel-dominant game, retain the opportunity cost in storage, mechanism power, alignment and testing. A low-mass hook can still be a poor choice if it blocks a valuable fuel route.',
 'Audit actual installation and match use separately from prototype drawings; calculate lost usable fuel volume before selecting a climbing package.')

# REEFSCAPE: scoring height is not a robot-quality ordering.
add('786e3d5aabeae7d675','drivetrain','971 2022: a deliberate West Coast drive simplicity choice',[3,5],
 'Six Colson-wheel West Coast drive; two dual-Falcon gearboxes; 8:70 gearbox tooth ratio.',
 'Robustness, low maintenance and short-distance acceleration.',
 'A differential drive sacrifices direct sideways motion while reducing the number of independent drive and steering mechanisms. That trade can fit a robot whose turret provides aiming independence and whose collectors support acquisition from opposite sides. Wheel choice affects maintenance and turning losses as well as traction. The team’s post-COVID experience constraint is part of this architecture decision: the most sophisticated available module is not automatically the strongest choice when integration and practice capacity differ. Preserve the resource assumption rather than presenting a universal drivetrain ranking.',
 'Measure short-cycle path time, turning current and defended maneuverability using the actual collector and turret operating policy.')
add('786e3d5aabeae7d675','intake','971 2022: center and guide cargo rather than only gripping harder',[6],
 'Flex-wheel prototype became mecanum-centered pickup with compliant chain/arm geometry and extra upper guides.',
 'Use known intake behavior and improve transfer support.',
 'The pickup must establish both ownership and a useful lateral position for the catapult transfer. Mecanum contact supplies centering while the compliant arm accommodates shape and pressure variation. Additional upper rollers address the transition after the initial capture, where a ball can lose support or arrive at the receiver at an uncontrolled height. The lesson is to diagnose the entire handoff path: improving the first roller’s grip cannot solve a downstream gap that lets cargo escape.',
 'Track the ball center through acquisition and transfer with several inflation states; test off-center pickup at realistic driving speed.')
add('786e3d5aabeae7d675','transfer','971 2022: flippy arms combine retention and release',[8],
 'Spring-loaded paired transfer arms; one-way-bearing action opens them when rollers reverse.',
 'Hold cargo in the catapult, then release it for firing.',
 'The transfer mechanism serves as a timed constraint on the projectile. It must hold the cargo through turret alignment but stop exerting an unwanted force at release. Coupling reversal to opening reduces an actuator but creates a mechanical timing relationship that software must understand. Spring force and ball compression affect both retention and release delay. If the catapult controller assumes the ball is free before the arms actually clear, a perfectly tracked motor trajectory can still produce a poor shot.',
 'Measure arm clearance and ball release timing relative to motor command, over cargo pressure and spring-wear variation.')
add('786e3d5aabeae7d675','scoring','971 2022: a controlled catapult instead of a flywheel',[9,13],
 'Light carbon catapult, two Falcons, 7:99 tooth ratio and model-predictive launch control.',
 'Team prototypes favored tolerance to cargo pressure and surface-friction variation.',
 'A motor-driven catapult sets the projectile’s velocity through the motion of a supporting arm rather than relying primarily on slip against a high-speed wheel. That can reduce one source of friction sensitivity while introducing trajectory tracking, release timing and structural stiffness requirements. A lighter arm spends less energy accelerating itself and leaves more actuator authority for the cargo. The controller needs the correct state at release, not merely a final position, because angle and velocity together determine the shot. This is a specific tested alternative, not a claim that catapults universally beat flywheels.',
 'Measure release angle and velocity across inflation and surface variation, compare with the flywheel prototype under equal conditions, and test mis-timed retention release.')
add('786e3d5aabeae7d675','endgame','971 2022: turret structure must also react climbing loads',[7,10],
 'Turret carries catapult and climber; paired bearing support; climber revisions progress toward a spring-extended high-bar package.',
 'Support firing and hanging loads with compact packaging.',
 'A bearing sized only for smooth aiming may be inadequate once the suspended robot applies an overturning moment through the turret. Two support locations can define a load path for that moment while maintaining axis alignment. Shared structure saves space but couples the climber’s strength requirements to the shooter’s pointing stiffness. The documented objective changed from a mid-rung solution toward higher reach, so do not infer traversal capability from a general “climber” label. Each pictured prototype also needs its own competition-use evidence.',
 'Check bearing and mount loads through firing and hanging, verify output-axis alignment afterward, and establish the dated competed climb configuration.')

add('6054858ce2266dbdc2','drivetrain','AURELIA: package the base around two different clearances',[4,5],
 '28-inch square chassis; X2i elevator-side modules and X2t intake-side modules; custom lowering spacers.',
 'Motor protection, low chassis and intake gearbox clearance.',
 'Choosing different module orientations within one drivebase is a packaging solution rather than a reason to recommend mixed modules universally. A motor placed inside can protect the elevator-side envelope while an outward placement can free an intake drive path. The lowering hardware must preserve module stiffness and ground clearance under a loaded, accelerating robot. Low mass is helpful, but the more relevant quantity for fast reef approach is the loaded center of mass and its motion as the shoulder and elevator change state. Include bumper and battery interfaces in the same model.',
 'Sweep the complete intake/elevator envelope against each module; measure clearance and wheel unloading through aggressive scoring transitions.')
add('6054858ce2266dbdc2','intake','AURELIA: separate coral and algae contacts on a shared axis',[7,8,9],
 'Coaxial intake pivots; separate deployment reductions; shared roller drive; bilateral transfer tubes.',
 'Synchronize both arms and combine the intakes for L1.',
 'Sharing an axis does not make these one generic intake. Each piece needs a different contact geometry, and the dedicated L1 action depends on their relative positions. Driving both sides helps prevent an arm from twisting out of phase during asymmetric contact. A common roller drive saves a motor and packaging but couples the desired surface speeds of the two pickup functions. The useful retrieval target is the entire relative geometry and state sequence: which surface acquires, which guides, and which constrains the coral during release. A lone roller photo cannot explain the L1 performance.',
 'Film the complete L1 cycle from first floor contact through release; vary coral orientation, reef occupancy and approach angle.')
add('6054858ce2266dbdc2','transfer','AURELIA: center coral before a direct handoff',[9],
 'Flex upper rollers, grippy lower rollers, about 0.125-inch coral compression and proximity detection.',
 'Center coral and hand directly into the end effector.',
 'A low-compression pickup can reduce the force required to accept an awkwardly oriented tube, but it leaves less traction margin when the surfaces are dirty or the coral is wedged against another piece. Centering before transfer reduces the number of states the end effector must solve. A direct handoff avoids an intermediate tray, while demanding that the receiving geometry arrive at the right position before the piece loses its previous constraint. Sensor placement should identify the handoff state, rather than simply report that some portion of a long tube is nearby.',
 'Test slow, diagonal and multi-piece approaches; observe whether detection occurs before, during or after reliable ownership transfers.')
add('6054858ce2266dbdc2','positioning','AURELIA: four-stage lift on a rotating shoulder',[6,10,11],
 'Shoulder-supported four-stage continuous elevator; internal HTD belts; interlocking extended-stage stops.',
 'Compact packaging with stiffness at scoring height.',
 'The shoulder changes both the lift’s direction and its center-of-mass path. A multi-stage lift can reach high while stowing short, but introduces more interfaces that can deflect or develop play. Hard stops that engage at extension can add stiffness where the mechanism otherwise has the least overlap; they must not produce damaging impacts at operating speed. The carriage’s integrated gearbox reduces redundant structure while making belt access and service sequencing important. In the alliance role described by the user, much of the robot’s value comes from low scoring and algae, yet its high reach still supplies capability and tactical flexibility.',
 'Measure tip error and settling after shoulder/elevator transitions, including side acceleration and partial rather than only full extension.')
add('6054858ce2266dbdc2','scoring','AURELIA: differential wrist and independently driven rollers',[12,13],
 'Printed bevel differential; paired 61.6:1 drives; independent coral rollers; front algae pinch wheels.',
 'Reorient coral while keeping the moving end effector compact.',
 'A differential combines two motor coordinates into two output motions. That can package orientation control densely, but means a joint motion may require both motors and leave less authority for the other axis at the same instant. Printed bevel gears need controlled bearing alignment and a stiffness model; backlash at a small output stage becomes placement error at the coral tip. Independent roller contacts can change tube orientation before release, which is particularly valuable for intentional L1 placement and stacking. The same hardware can support very different alliance jobs, so high-level capability must be separated from the task actually assigned in a match.',
 'Command combined wrist motions under realistic piece load; measure output backlash and horizontal-coral placement consistency across L1 pile heights.')
add('6054858ce2266dbdc2','endgame','AURELIA: reuse the shoulder and reposition the cage',[8,14],
 'Powered cage capture, passive latches, sliding support and shoulder-driven lifting; algae intake supplies support.',
 'Reuse primary joints while controlling the hanging geometry.',
 'A shared-joint climb saves dedicated structure only if the primary system can react the new loads. Capturing one cage tube is different from supporting the robot after the cage rotates; the lower reaction point and position of the chain relative to the robot’s center of mass determine the motion. The sliding support permits that geometry to change rather than requiring a single fixed pivot to solve every phase. Reuse also couples faults: a damaged shoulder, end effector or intake latch can affect climb. Record the support contact explicitly instead of reducing the design to “uses its arm to climb.”',
 'Test cage swing and off-center capture, inspect every reaction contact, and verify retention after power is removed.')

add('c8be42e3972c8859d8','drivetrain','SPECTRE: base and module revision at Championship',[5],
 'District Mk4i modules changed to prototype Mk5 at Worlds; ballast placement also changed.',
 'Low center of gravity and short-cycle maneuverability.',
 'A module swap is a robot version, even if the scoring architecture looks unchanged. Saving module weight can be reinvested as low ballast rather than removed from the robot, changing traction and stability differently from a simple weight reduction. A wide tread and different enclosure can alter friction, debris protection and maintenance. Retuning drive and autonomous behavior is part of the mechanical change: old acceleration and feedforward assumptions should not be carried over without measurements. The database should name the competition stage associated with each configuration.',
 'Compare module slip, current and stopping repeatability before and after the change with the actual ballast and bumper package.')
add('c8be42e3972c8859d8','positioning','SPECTRE: remote power at an integrated pivot',[6,9],
 'Separate three-X60 shoulder and extension gearboxes; dead-axle pivot; two-stage cascade arm.',
 'Fast motion with a low stowed center of gravity and serviceable arm.',
 'Keeping heavy actuators near the base reduces distal inertia and lets the arm respond without carrying all its drive mass at the tip. The price is a more complicated transmission across the pivot and through the telescope. A coaxial extension drive must preserve tension and alignment over the shoulder’s range. A large shared pivot can support stiffness and removal, but its clamps and end plugs become critical load interfaces. Motor count alone does not explain speed: the arm’s inertia, reduction, current limits and acceleration profile determine whether it can move quickly without rocking the chassis.',
 'Measure end-point settling after simultaneous pivot and extension; test removal/reinstallation repeatability and chain tension over the full range.')
add('c8be42e3972c8859d8','intake','SPECTRE: acquire, orient and score with one end mechanism',[8],
 'Vertical and horizontal roller sets; four CANrange sensors; reversible front/back handoff and scoring.',
 'Serve coral and algae tasks with the same manipulator.',
 'Combining acquisition and scoring avoids a separate transfer interface, but makes the moving assembly larger and creates competing contact requirements. Coral has to be oriented differently for branches and L1; algae needs enough compliant pinch to stay captured during rapid motion. Multiple sensors can distinguish piece position and direction, provided their views remain reliable for both geometries. Front/back scoring reduces chassis rotation when the software chooses a sensible approach. The architecture should be assessed by complete cycle time and reach under defense, not by the number of available poses.',
 'Test front/back coral scoring, intentional horizontal L1 placement and algae capture with the same rollers after wear.')
add('c8be42e3972c8859d8','endgame','SPECTRE: moving climb carriage manages the hanging center',[7,9],
 'Powered one-bar cage capture; carriage slides along arm; shoulder lifts; extension locks to bumper structure.',
 'Balance under the chain while reusing the main arm.',
 'The carriage is not just a convenient mount. Its translation changes where the cage pulls relative to the robot’s mass, allowing a controlled transition into suspension. The shoulder then supplies the lifting work and the arm lock supplies a post-match retention path. Those are separate functions and should be recorded separately. Reusing the arm reduces dedicated hardware but raises its required load and reliability. Any recommendation needs the actual cage contact, latch, shoulder and lock sequence rather than assuming that a strong scoring arm can safely substitute for a complete climber.',
 'Capture at several swing angles, verify carriage travel under load, and test power-off retention through the intended bumper lock.')
add('c8be42e3972c8859d8','controls','SPECTRE: automate approach choice and L1 placement',[10],
 'Automatic front/back reef choice; level/side selected by driver; distinct base/top L1 states.',
 'Remove repeated alignment work from the driver.',
 'Choosing the nearest face or easiest orientation can save time, but the shortest geometric route is not always the least congested or the most valuable remaining target. L1 stacking creates an occupancy problem as well as a pose problem: a fixed placement height is insufficient once previous coral changes the landing surface. The driver still needs strategic control over task and side, with software handling repeatable motion. A mechanism recommendation should include the sensors, pose references and operator choices required to realize its cycle advantage.',
 'Test automatic choices near boundaries between faces and with populated L1; verify deliberate driver override and recovery after a failed release.')

add('ffe1c28c7bdb167b96','drivetrain','UNDERTOW: short-cycle gearing and low mass placement',[12],
 '29.5-inch square base; low 3×1 frame; X2i modules geared about 13.2 ft/s free speed.',
 'Favor acceleration and grip over long-run top speed.',
 'For a short reef cycle, acceleration, braking and repeatable final alignment can matter more than a higher unloaded top speed. Lower gearing increases available wheel torque but does not guarantee traction; wheel compound, normal load and current limits still bound acceleration. A broad low base helps resist tipping while the elevator changes height, but occupies more traffic space. The useful comparison uses the actual route and raised mechanism state rather than a module specification on its own.',
 'Measure complete reef-to-supply cycle time, stopping error and wheel unloading with the elevator at representative positions.')
add('ffe1c28c7bdb167b96','intake','UNDERTOW: floating continuous rollers and four-bar deployment',[13],
 'Foam/silicone continuous rollers, floating front plate, rubber-band dead-zone belts and four-bar deployment.',
 'Admit longways coral and yield during collisions.',
 'A continuous compliant surface can avoid the discrete kicks caused by spaced wheels, while a floating roller accommodates the changing cross-section presented by a tube approaching diagonally. Rubber bands bridge regions where neither main roller can maintain ownership. They also introduce wear, tracking and tension variables, so their role should be tested rather than treated as decorative assistance. The four-bar positions the deployed pickup without requiring its pivot at the very front of the chassis. Copy the contact geometry and trajectory together: substituting a single pivot can change both bumper clearance and handoff.',
 'Approach coral at a grid of angles, measure uninterrupted contact, and repeat after a wall impact and belt replacement.')
add('ffe1c28c7bdb167b96','transfer','UNDERTOW: flatten and index before handing off',[14,15],
 'Eight compliant/star wheels; guide wedges, flattening yoke and beam breaks; separate steep station funnel.',
 'Create a repeatable handoff from either source.',
 'Ground and station pickup arrive with different velocities and orientations. A common indexer lets the end effector see a smaller set of input states, but the funnel and pickup must not feed incompatible positions. Wedges and a flattening wheel create deliberate constraints; if they constrain too many dimensions at once, the tube can wedge rather than align. Sensors should identify the indexed state before the receiver moves. The station funnel adds redundancy and autonomous options, so its value depends on how much extra envelope and mass it costs alongside floor acquisition.',
 'Compare handoff time and jam rate from both sources with skewed and bouncing arrivals; test the full state sequence after a missed detection.')
add('ffe1c28c7bdb167b96','positioning','UNDERTOW: fast continuous elevator',[16],
 'Two-stage internal-belt lift; two X60s; welded support frame; team reports roughly 0.3-second full travel.',
 'Reach scoring heights rapidly and maintain stiffness.',
 'A fast travel number does not include settling, alignment or release. Internal belts protect the drive path but make access, tensioning and inspection more important. The support frame must react lateral inertia from the raised wrist as well as the elevator’s own acceleration. If the system reaches height quickly but sways outside the coral-placement tolerance, the useful cycle has not improved. A matched recommendation needs carriage mass, output stiffness, profile constraints and a maintenance plan rather than only belt width and motor count.',
 'Measure time until the coral tip enters and stays within scoring tolerance, not merely until the encoder reaches its height setpoint.')
add('ffe1c28c7bdb167b96','scoring','UNDERTOW: Flying V compliance and an L1 pass-through',[18,19],
 'Wrist-mounted compliant coral roller, pipe-aligning Flying V, cam-controlled rear hoop and shared algae drive.',
 'Fast branch placement with controlled piece handoff.',
 'Mechanical alignment can absorb residual chassis error by guiding the end effector relative to the actual pipe. It must do so without pushing the tube into a trapped configuration or transmitting a large side load into the wrist. The movable hoop illustrates why the handoff and L1 scoring states differ: a stop that is necessary to receive coral can obstruct the intended exit. Sharing a motor between piece contacts reduces moving mass but couples their speed and torque requirements. The complete mechanism includes the cam state and sensing, not just the front roller.',
 'Map tolerated lateral and angular pipe error, test handoff against L1 pass-through, and repeat with a worn wheel and occupied nearby branches.')
add('ffe1c28c7bdb167b96','endgame','UNDERTOW: capture first, then winch the robot under the cage',[17],
 'Powered roller claw, passive latch, gas-spring deployment and low-mounted ratcheting winch.',
 'Acquire a cage quickly and retain suspension after disable.',
 'Separating capture from lifting allows the capture wheels to optimize entry while the winch carries the robot load. The latch and cage reaction surfaces must take over reliably before the wheels stop providing traction. Remoting the winch lowers mass but lengthens the tension path and adds rope-routing concerns. A deep-climb recommendation should identify acquisition tolerance, how the cage rotates, where the chain ends relative to the robot’s center of mass, and the load path after power is removed.',
 'Test swinging-cage acquisition, transition from powered rollers to latch, and power-off retention with the actual rope routing.')

add('b99a49d2db2fb68f4f','intake','MISS DAISY: orient on the floor and preserve collision compliance',[19,20,21,22,23],
 'Sprung OTB rollers with ramps; later stronger front tube and round shafts.',
 'Broad-orientation acquisition and impact survival.',
 'Orienting the tube before lifting reduces the number of uncontrolled handoff states. A wide compliant roller captures early while ramps and passive contacts bias the tube toward the desired orientation. That can fail if a ramp starts lifting one end too soon. Structural damage also changes the ball path: a bent mounting tube can turn a nominally symmetric intake into a one-sided jam. Preserve the sequence of revisions, because a successful final contact geometry may rely on the preceding stiffness fix.',
 'Film diagonal approaches from both sides before and after impacts; measure ramp and roller alignment rather than judging symmetry by eye.')
add('b99a49d2db2fb68f4f','transfer','MISS DAISY: diagnose jams from observed contact',[24],
 'Reduced compression, relocated support shaft, changed hard stops and redesigned ramp bends.',
 'Slow-motion review identified different jams at successive events.',
 'A jam is a geometric event, not merely insufficient motor power. A tube can press a belt into a support, climb at one end while the other end remains constrained, or stop a roller whose structure is bent. Each mode requires a different change. Moving the wheels forward changes both normal force and where the tube begins to rise. A useful agent should first ask which contacts stop moving and where the tube becomes over-constrained; recommending more torque without this observation can destroy the part that reveals the fault.',
 'Create a repeatable failed orientation, isolate the first contact that arrests motion, change one dimension and compare the failure frequency.')
add('b99a49d2db2fb68f4f','scoring','MISS DAISY: grip algae while allowing coral release',[27,28,29,30],
 'Coral compression reduced to 0.375 inch; drive ratio revised; harder wheels and algae shields added.',
 'Improve coral release, pulley durability and algae retention.',
 'The two pieces demand conflicting grip behavior. Increasing compression can improve retention but make a tube difficult to release without disturbing the target. A harder wheel can resist wear yet reduce conformity and change normal force. A larger drive pulley may reduce tooth loading and skipping while changing speed and torque. Shields can prevent a soft ball from folding around the side plates, addressing a failure that motor current alone cannot solve. These are linked empirical tradeoffs, so the record should preserve both piece types and the tested release geometry.',
 'Measure coral release force and algae retention after representative wheel wear; inspect pulley teeth during repeated high-torque captures.')
add('b99a49d2db2fb68f4f','positioning','MISS DAISY: rope geometry and structural stiffness evolved together',[31,32,33,34,35,36,37],
 'Horizontal Dyneema spool inspired by 1678; continuous lift; later U-crossplate and rigid side support.',
 'Solve rope slip, poor tension and elevator lateral play.',
 'A lift can have accurate motor position while its carriage moves laterally because the structure and rope system are different error sources. Rope routing should keep each run aligned as winding radius changes; overlapping wraps change effective motion per motor turn. A stiff top crosspiece limits upright splay, while a triangulated or rigid support reacts side loading without relying only on adjustable rods. These revisions show why copying the final spool alone is insufficient. The recommendation needs the complete routing, tension system and support geometry.',
 'Track carriage height versus motor position and lateral tip error independently; inspect winding over repeated full strokes under load.')
add('b99a49d2db2fb68f4f','positioning','MISS DAISY: shoulder and wrist serve different coordinates',[38,39,40],
 '45:1 shoulder with lantern gear; 21.4:1 wrist with about ±100° motion.',
 'Move between robot sides and reorient coral without collisions.',
 'The shoulder changes the end effector’s position and reach, while the wrist changes the piece orientation. Those motions need not be performed serially, but simultaneous movement requires a collision-aware path. A lantern gear can place the reduction close to the output and control backlash; its performance still depends on bearing alignment and tooth/pin wear. A dead-axle wrist offers a clear reaction path, but the cantilevered mass and cable routing contribute torque and deflection. The useful model is the coral’s swept volume, not only each joint’s independent limit.',
 'Generate and physically check the coral envelope during side swaps; measure output angle repeatability under reversing load.')
add('b99a49d2db2fb68f4f','endgame','MISS DAISY: passive harpoon over a wheeled grabber',[44,45,46,47],
 'Levering climber; passive sprung harpoon; 675:1 reduction; steel gears replaced inadequate aluminum gears.',
 'Similar capture performance with fewer vulnerable parts.',
 'A high reduction can provide lifting torque, but it does not reduce the load carried by the final gear and support shaft. Material changes at that interface can therefore matter more than adding motor power. A passive hook can outperform powered acquisition when the robot’s approach already supplies sufficient engagement force and the cage geometry naturally directs the bar into the latch. That simplifies the controller while placing more importance on the approach envelope and retention geometry. Capture reliability should be assessed with swing and imperfect alignment, not only a stationary cage.',
 'Measure engagement tolerance and inspect final-stage stress after repeated climbs; test retention with the cage rotated and the robot disabled.')
add('b99a49d2db2fb68f4f','versions','MISS DAISY: remove a dedicated algae intake that adds no useful capability',[41,42],
 'A separate floor-algae collector was removed after prototype comparisons.',
 'It did not outperform the end effector enough to justify complexity.',
 'A subsystem can satisfy its own requirements and still be a poor robot-level choice. A dedicated collector may save a little positioning time while costing envelope, sensors, wiring, maintenance and driver decisions. If the primary end effector already serves the intended algae role, the marginal gain must exceed those costs. This is the right level for an architecture agent to reason: compare complete task contribution and reliability rather than rewarding more mechanisms. Keep the removed design in the history as an evaluated alternative, not as an installed feature of the final robot.',
 'Compare complete algae cycles and failure recovery with and without the auxiliary system, including time spent switching modes.')

add('cb12c402d721aad7df','intake','OPR 2025: floating capture and protected pivot drive',[7,8],
 '20-inch OTB intake; coaxial roller drive; synchronized pivot sides; floating upper roller.',
 'Tolerant coral pickup with motors protected in the frame.',
 'Coaxial power transmission lets a roller remain driven as the intake pivots without a long changing-center belt run. The floating contact accommodates an awkward tube orientation while the lower contact keeps it moving into the robot. Synchronizing both sides resists twist, but an impact can still concentrate load at the polycarbonate-to-aluminum joint. Large clamps distribute this force and retain the bearing as the plate flexes. Automatic retraction protects the collector only after the sensor has confirmed that the tube is safely inside.',
 'Test diagonal pickup, asymmetric loading and capture-triggered retraction; inspect bearing retention following a side impact.')
add('cb12c402d721aad7df','transfer','OPR 2025: independent straightening drives and staged cradle sensing',[9,10,11,12],
 'Independently driven straightener sides; current-triggered reversal; two-sensor cradle with anti-bounce step.',
 'Align coral and recover jams before handoff.',
 'Independent sides permit relative slip or reversal instead of forcing both ends of a tube forward at the same speed. Current sensing can identify resistance, but must distinguish a normal capture transient from a persistent jam. The cradle then changes the problem from continuous alignment to a discrete known handoff position. A stop lip and anti-bounce feature control longitudinal motion, while cutouts provide room for the receiving gripper. Excessively constraining the tube at the same time as the gripper closes can create a new jam, so the handoff sequence matters as much as the tray shape.',
 'Feed tubes at skewed angles, tune jam detection against false triggers, and test receiver clearance during an interrupted handoff.')
add('cb12c402d721aad7df','scoring','OPR 2025: reduce moving inertia without losing algae grip',[13,14],
 'Formed-sheet arm replaced tubing; lighter geared gripper drive; remoted motor; velocity-matched coral ejection.',
 'Reduce mass and pivot moment while keeping functional grip.',
 'Removing mass far from the pivot reduces inertia more effectively than removing the same mass near the axis. A remoted motor achieves that while adding a transmission whose backlash and compliance must be controlled. Formed sheet can provide a stiff section with low mass if the flanges and joints react the actual loads. Matching ejection to chassis motion can reduce unwanted relative velocity at release, but requires consistent roller surface speed and piece position. It is a coordinated robot motion, not a passive property of the gripper.',
 'Measure tip settling and grip under acceleration; test scoring while approaching and backing away at several speeds.')
add('cb12c402d721aad7df','positioning','OPR 2025: stiff internally belted elevator',[15,16],
 'Two-stage continuous lift, internal 18-mm HTD belt, two X60s; reported about 0.6-second travel.',
 'Fast motion with lateral stiffness and camera visibility.',
 'The upright supports, top bridge and bearing guidance determine how much commanded height becomes actual end-effector position. Internal belts protect the tension path but demand a practical inspection and replacement route. Integrating a wrist gearbox into the carriage removes interfaces while increasing the consequences of a carriage service problem. Cameras on both uprights can preserve tag visibility as the robot approaches different branch sides, but their structural reference must remain stable as the lift moves.',
 'Measure tip error at full and intermediate height during chassis braking; verify camera visibility and calibration on both scoring sides.')
add('cb12c402d721aad7df','endgame','OPR 2025: lightweight winch and guided cage capture',[17,18],
 '4.5-pound climbing package; rope winch, ratchet, sprung deployment and printed cage guides.',
 'Easy alignment, legal cage clearance and power-off retention.',
 'A guide can enlarge the capture envelope without adding an actuator, but its shape must not let the cage rotate into the elevator or chain contact an illegal surface. Rope lifting places high local loads at the spool, attachment and pivot; these should be checked independently of motor torque. A ratchet provides a mechanical holding path after disable, while the magnet and collars manage capture and slippage. The architecture record should identify which elements guide, which retain and which actually carry the robot.',
 'Test rotating and swinging cages, inspect the rope at attachment bends, and verify chain clearance through the full lift.')

add('dd729524010212768b','intake','BREAD 2025: floating intake plus dedicated L1 restraint',[5],
 'Floating front roller, centering wedges and deployable L1 bar with anti-bounce hooks.',
 'Broad pickup and controlled L1 release.',
 'A tube entering lengthwise needs space to rotate; a fixed narrow contact can eject it before alignment finishes. The floating front roller accommodates that transition. The L1 bar serves a different task: it changes the release boundary and prevents the intake from lifting or letting coral bounce away. This is a useful example for an agent because L1 capability is not merely “run the intake backward.” The intended orientation, release contact and state of the front roller determine whether coral stays where the alliance needs it.',
 'Test L1 placement at several existing pile heights and compare bounce-out with and without the restraint engaged.')
add('dd729524010212768b','transfer','BREAD 2025: asymmetric star-wheel orientation',[6],
 'Asymmetric star-wheel indexer, beam-break extra-piece rejection and repeatable handoff tray.',
 'Reduce alignment jams and reject an unwanted second tube.',
 'Symmetry can preserve a bad equilibrium: both ends of a skewed tube may be driven equally without ever rotating into the desired orientation. A deliberate asymmetry can break that state, but may also introduce a preferred direction and different behavior for mirror-image approaches. The extra-piece logic must distinguish a second tube from a long first tube passing multiple sensors. A tray then provides a controlled receiving state. Test these as one chain rather than optimizing the indexer’s standalone speed.',
 'Feed mirror-image diagonal tubes and closely spaced pairs; record orientation time, rejection errors and handoff repeatability.')
add('dd729524010212768b','positioning','BREAD 2025: cascade lift with counterbalance and chain control',[7,8],
 'Two-stage cascade; two X60s at 7:1; constant-force springs; cantilevered pivot and chain tensioner.',
 'Rapid lift with lower current and controlled transmission.',
 'Counterbalance reduces the gravitational load the motors must supply during part of the stroke, but its force and mounting geometry affect upward and downward behavior differently. A cascade lift magnifies travel and velocity while changing the force seen by each stage. A rolling chain tensioner can manage slack during acceleration, but does not cure a misaligned sprocket or insufficient tooth engagement. The cantilevered wrist support must react both bending and overturning moments. A fast reported stroke needs a settling and placement test to establish its useful cycle value.',
 'Log lift current and tracking in both directions, inspect tension during reversals, and measure tip displacement under sideways load.')
add('dd729524010212768b','scoring','BREAD 2025: shared drive for coral and algae contacts',[9],
 'One X60 drives distinct coral/algae contacts through different ratios and printed gear-pulley combinations.',
 'Handle both pieces while reducing moving mass.',
 'A shared motor saves wiring and mass but ties the contact speeds to fixed ratios. The design must provide enough algae holding torque without making coral release too abrupt. Combining a gear and pulley can shorten the assembly and remove redundant hubs, while concentrating loads into the printed part and its bearing interface. Material choice, print orientation and temperature therefore belong in the durability review. A successful borrowed geometry requires matching compression and piece position, not only duplicating the nominal ratio.',
 'Measure algae retention and coral release after repeated cycles and heating; inspect printed tooth roots and bearing fits.')
add('dd729524010212768b','endgame','BREAD 2025: centered single-tube cage support',[10],
 'Six-pound spear/flyswatter collector; spring deploy; string winch; reported 1.5-second lift.',
 'Center the cage and use a compact lifting package.',
 'A passive centering shape can simplify acquisition while making the load path highly dependent on where the cage settles. If retention relies partly on robot weight and friction, the transition into suspension needs careful testing before full load is applied. Spring deployment saves an actively driven extension but requires a reliable latch and stow sequence. The winch reduction determines available force, while rope radius and cage lever arm determine actual robot lift. A lift-time claim should remain distinct from total acquisition-plus-settling time.',
 'Test swinging-cage entry and interrupted lifts, including a case where only one contact is initially engaged.')
add('dd729524010212768b','drivetrain','BREAD 2025: low chassis and direct reef ranging',[4],
 'Dropped X2 modules, low frame and CANrange reef-distance sensing.',
 'Low center of gravity and repeatable approach.',
 'Lowering the frame can improve stability while reducing ground clearance and access. A direct range measurement near the reef can refine the final approach, but only if the sensor sees the intended surface rather than a tube, branch or oblique panel. It should complement a known geometric model and a validated scoring tolerance. Treat a sensor as an observation with failure modes rather than proof of alignment.',
 'Map distance error over reef approach angle, piece occupancy and elevator position; check collision and service clearances.')

add('3dfd18a3f5f1ef7749','intake','Alpha Dogs: retention, compliance and source fallback',[7,8],
 'Single roller became dual; long compliance linkage became compact sprung arm; first event used station funnel.',
 'Solve escaping coral, collision vulnerability and packaging.',
 'Capturing a tube is not the same as retaining it after the first contact. The second roller can close an escape path while increasing the need to control compression. An impact-yielding linkage can protect the pickup, but a long arm consumes chassis volume and increases bending moment. The report’s station-funnel fallback is evidence of a competition configuration, while its ground-intake drawings include developmental versions. Keep those distinct when recommending inspiration: a promising prototype is not automatically a demonstrated event mechanism.',
 'Test retention during braking and reverse motion; verify the exact event configuration before using a version as a performance example.')
add('3dfd18a3f5f1ef7749','transfer','Alpha Dogs: conveyor and tray progressively consolidated',[8,9],
 'Opposed star-wheel conveyors evolved into a lighter polycarbonate assembly and integrated receiving cup.',
 'Straighten coral and simplify the transfer structure.',
 'A conveyor that both straightens and transports a tube can avoid a separate orientation stage, but its downstream tray must stop the tube without sending it back into the drive contacts. Removing redundant support material can improve access and mass while changing alignment under load. A receiving cup reduces uncertainty in the arm’s pickup position, provided it has no lip that prevents release into the gripper. The best architecture depends on the handoff’s repeatability and recovery after a partial acquisition, not only its nominal travel time.',
 'Test varied tube orientation and arrival speed, then interrupt the handoff to verify that the mechanism can recover without driver intervention.')
add('3dfd18a3f5f1ef7749','scoring','Alpha Dogs: gripper envelope changed the architecture',[10],
 'Combined piece gripper revised after reach/envelope problems; elevator-mounted arrangement developed.',
 'Keep the placing assembly within the intended geometry.',
 'Adding a second piece function changes more than roller spacing: the swept volume, center of mass and necessary approach path may all grow. A gripper that works on a bench can violate the robot’s usable envelope when attached to an arm. Moving it onto an elevator changes the kinematic problem but does not by itself prove accurate release. The report leaves some final geometry and transmission details unresolved, so an agent should retrieve CAD or later event evidence rather than invent an elevator ratio or a final mechanism sequence.',
 'Check the full loaded piece envelope and actual event revision; measure pickup, hold and release separately for each piece.',
 'This engineering report documents development. It does not establish every final CAD dimension, elevator reduction or competition use of every pictured prototype.')
add('3dfd18a3f5f1ef7749','endgame','Alpha Dogs: reduce the cage mechanism to its useful load path',[6],
 'Complex capture concepts led to a simpler pivoting jack; chain endpoint targeted the robot’s mass center.',
 'Reduce weight and improve hanging geometry.',
 'A cage mechanism must transfer the robot’s weight through a secure contact while allowing the robot to settle into a stable orientation. A design can capture well yet demand excessive torque because its chain line remains far from the center of mass. Simplifying to a lever reduces parts but can concentrate load at the main pivot and rope attachment. The analysis should identify the actual hanging geometry and load path, with an explicit boundary between proposed and competed revisions.',
 'Test off-center acquisition and load transition; confirm the final revision with dated match or pit evidence.')
add('3dfd18a3f5f1ef7749','controls','Alpha Dogs: camera view and reef occupancy are architecture inputs',[12,17,18,19,20],
 'Camera angle revised for close tags; field-region alignment and operator-entered reef occupancy are described.',
 'Reduce blind spots and repeated target-selection work.',
 'A camera can see an AprilTag far away yet lose it at the exact distance where precision is needed. Mount angle and obstruction therefore belong in the early CAD review. Keeping reef occupancy in software changes the operator’s task from repeatedly aiming to maintaining a reliable shared state. Incorrect occupancy can send the robot toward a filled branch, so the system needs a quick correction and manual override. The mechanism recommendation should include what target information it assumes the controls will supply.',
 'Test tag visibility at every final scoring pose and recovery from deliberately incorrect occupancy entries.')

add('f93f8ab32955ff8090','intake','SIDEWAYS: compliant dual four-bar collection',[10,14],
 'Dual pneumatic four-bars; quarter-inch polycarbonate arms; large front and smaller transfer rollers.',
 'Acquire from either side and yield in collisions.',
 'Two intake directions reduce the turn needed to collect the next cargo while keeping the shooter in a useful field orientation. The four-bar defines the roller’s approach and stowed position; the arm material supplies lateral compliance that the linkage alone cannot. Different roller diameters and reductions establish surface velocities through the transition. An apparent increase in grip is unhelpful if it arrests the ball between contacts. This architecture should be understood as two collectors feeding one shared storage and shooter system, not as two independent scoring paths.',
 'Measure acquisition at speed and across approach angles, then verify both directions still transfer correctly after impact.')
add('f93f8ab32955ff8090','transfer','SIDEWAYS: serialize two wide inputs and reject wrong-color cargo',[15,21,22],
 'Centering wheels and rollers; beam-break position tracking; color sensing; deliberate opponent-cargo ejection.',
 'Maintain two-cargo ownership and consistent shooter feeding.',
 'The serializer converts a broad acquisition front into an ordered narrow output under a possession limit. Storing the first accepted ball away from the active intake leaves room for the second; that is a spatial control policy, not merely a conveyor. Color rejection adds an adversarial constraint: an unwanted ball must leave without corrupting the state estimate or helping the opponent more than necessary. A sensor detects contact or color at one location, so software must preserve identity as balls move and occasionally slip. A jam can be a state-estimation failure even when all rollers turn.',
 'Run correct/wrong-color pairs from both sides, interrupt the feed, and verify the estimated inventory against video.')
add('f93f8ab32955ff8090','scoring','SIDEWAYS: wrap, surface matching and a moving target',[16,17,22],
 'Nine-inch main wheel, driven back rollers, adjustable hood and ±120° turret.',
 'Long contact and controlled spin for accurate mobile shots.',
 'A long wrap increases the time available to accelerate the cargo and can reduce the impulse required at any single contact. Driving the backing rollers changes both friction loss and the ball’s angular velocity. Surface-speed matching is a kinematic idea; the actual ball may slip or deform, so launch spin must be measured. The turret reduces chassis-heading dependence, while the hood and speed map determine range. None of these removes the need to account for robot velocity and shot timing. The relevant comparison is the repeatability of the exit state under a sequence of shots.',
 'Measure ball translation and spin with high-speed video, compare first and second shots, and test motion compensation across turret headings.')
add('f93f8ab32955ff8090','endgame','SIDEWAYS: react against the truss before reaching traversal',[18,19],
 'Chain elevator, reaction arm, passive telescoping stinger and retention latches.',
 'Reorient the robot to reach traversal within the envelope.',
 'This climb is a sequence of changing load paths. The elevator first loads a rung; the reaction arm then changes the robot angle by pushing against the truss; the stinger finally reaches a farther rung. Large internal forces can occur while the robot barely moves because opposing contacts create a short lever arm. A tensile strap can carry a known directional load efficiently, but cannot resist compression or uncontrolled reverse motion. The passive stinger can be light because it need not retract under robot load. Copying only its telescoping tubes would omit the reaction geometry that makes the reach possible.',
 'Instrument reaction loads and verify every intermediate retention state; test misalignment and incomplete hook engagement before increasing speed.')
add('f93f8ab32955ff8090','drivetrain','SIDEWAYS: first swerve and deliberately low mass placement',[13],
 'Mk4i L3 modules, added motor-shaft support bearings, low solid bellypan and central battery.',
 'Maneuver around defense and maintain stability.',
 'The drive choice supports the collector and turret by allowing travel direction to change without the chassis continuously pointing toward the next ball. Lowering mass helps resist wheel unloading during fast transitions, while the chosen ground clearance still has to survive real field debris and cargo. Extra bearing support changes how module loads reach the motor shaft. A reusable design record should retain these integration details because a module family name alone cannot explain collision survival or handling.',
 'Compare stopping and lateral acceleration with representative cargo and bumper loads; inspect motor-shaft support alignment after impacts.')

add('1b0b189d42a421199e','positioning','BREAKDOWN: independent vertical and lateral extension',[12,13],
 'Vertical elevator plus 15° inclined three-stage carbon-fiber laterator; PEEK guidance rollers.',
 'Fast reach with low moving mass.',
 'Separating vertical and outward motion turns scoring poses into two mostly independent coordinates. That can simplify the end-effector geometry and let the chassis remain farther from the grid, but adds another flexible stage and a collision envelope between stages. Low-mass carbon structures reduce inertia; guidance roller preload and tube alignment determine whether they move freely without excessive play. The laterator’s angle contributes vertical motion as it extends, so the control system still needs a coupled pose model. A reported travel time describes one axis, not a complete pickup-to-placement transition.',
 'Measure coral-equivalent tool-tip error under simultaneous axis motion and chassis acceleration; inspect guidance play and cable drag across the entire stroke.',
 'The PDF required OCR. Page 12 elevator construction was checked visually; other numerical OCR details should be checked in the original before fabrication.')
add('1b0b189d42a421199e','scoring','BREAKDOWN: articulate contacts for cones and cubes',[8,15],
 'Articulating roller claw with distinct cube and cone contacts; over-center cone grip.',
 'Serve upright cones and cubes without pursuing every floor orientation.',
 'A cone and a cube present different contact and centering problems. An articulated claw can open enough for a cube while using a different smaller contact to constrain a cone. Over-center geometry can supply retention without continuous high motor force, provided the piece is located in the intended three-point contact. Choosing not to solve sideways floor cones is an explicit scope decision linked to expected high-level supply; it must not become a universal claim that such pickup has no value. A local event or a disrupted supply plan can change that assumption.',
 'Test each intended piece orientation and define a safe fallback for excluded orientations; measure grip after approach collisions.')
add('1b0b189d42a421199e','intake','BREAKDOWN: rack-deployed cube floor pickup',[16],
 'Rack-and-pinion polycarbonate extension and a small grippy roller feed the main claw.',
 'Lightweight, robust access to floor cubes.',
 'Linear extension preserves roller height while changing its distance from the chassis, which is useful when a simple pivot would change the pickup geometry too much. A rack cut directly into the side plate reduces part count but concentrates wear and impact load in that plate. The floor mechanism does not solve every piece task; it supplies a known cube path to the articulating claw. That specialization can be efficient when the human-player and game-piece plan makes it sufficient.',
 'Test cube acquisition near walls and with oblique contact; inspect rack alignment and tooth wear after repeated forced retractions.')
add('1b0b189d42a421199e','endgame','BREAKDOWN: forks change the robot’s balance interface',[17],
 'Carbon-fiber forks and a sliding carriage react against bumper structure; rope lift.',
 'Lift alongside partners and balance quickly.',
 'The forks are an alliance interaction mechanism. Their usefulness depends on the partner’s underside, bumper placement and where the combined load settles on the platform. Reacting through bumper wood can counter sag but creates a load path that needs appropriate mounting and repeatability. A mechanism that works under one partner may interfere with another, so compatibility belongs in the selection criteria. This differs fundamentally from a cage or rung climb despite sharing motors, rope and lifting motion.',
 'Test with representative partner geometries, unequal loading and platform tilt; verify the load path through the bumper attachment.')
add('1b0b189d42a421199e','controls','BREAKDOWN: collision avoidance and compliant station intake',[20,21],
 'Intermediate superstructure states, reduced-precision transitions and a compliant laterator intake mode.',
 'Move quickly while avoiding collisions and station impact loads.',
 'A Cartesian-looking mechanism still needs a safe sequence through its intermediate states. Requiring every joint to settle precisely at every waypoint wastes time, while removing all intermediate conditions can create a collision. A compliant acquisition mode trades position stiffness for reduced impact, so its transition back to scoring control must be deliberate. Vision and odometry should supply a confidence-aware pose; the mechanical compliance is a complement to that estimate rather than evidence that accurate sensing is unnecessary.',
 'Start transitions from unexpected interrupted states, test a station impact, and verify that the mechanism returns to a known scoring reference.')

add('6aaa544e036a9d5234','positioning','OPR 2023: low-backlash articulated arm',[9,11,13],
 'Two driven joints, dead axles, bronze bushings and gas-shock shoulder counterbalance.',
 'Fast repeatable motion with motor-side position sensing.',
 'An articulated arm can reach floor, station and grid positions without a tall lift, but the endpoint error combines both joint errors. A small shoulder angle error becomes a larger tip error as the arm extends. Reducing backlash at shafts, gears and chains supports motor-side sensing only if elastic deformation remains acceptable. Gas shocks reduce gravitational torque over part of the motion but produce a changing torque with angle. A bronze bushing can be appropriate for high load and limited rotation, while friction and wear must be included in control tuning.',
 'Measure tip repeatability approaching the same pose from both directions, under load and after chain wear.')
add('6aaa544e036a9d5234','intake','OPR 2023: piece-specific active contacts',[15,16],
 'Pneumatic top roller for cubes, synchronized side rollers for cones and piece-specific sensors.',
 'Center and hold both pieces while limiting damage.',
 'The top roller and side pinch solve different shapes rather than forcing both through one fixed gap. Timing the side mechanism prevents one arm closing first and pushing the cone away. A sensor that reliably detects a cube may not see a cone in the same position, which explains why sensing belongs in the physical design. The control should stop or change the roller command after capture to avoid damaging the soft piece. Compliance reduces impact severity but must not let the frame spread enough to lose the intended contact geometry.',
 'Test skewed cone entry, cube retention during traversal and sensor-triggered transitions with worn or deformed pieces.')
add('6aaa544e036a9d5234','drivetrain','OPR 2023: base mass supports arm motion',[5,7],
 'Low Mk4i base; rear steel ballast and solid bellypan; rigid tower and dead-axle shoulder support.',
 'Stable traversal and a stiff arm reference.',
 'A lightweight arm does not eliminate its overturning moment. Low ballast and a broad support polygon can permit more aggressive joint motion, while adding driving load and stopping energy. Tower deflection appears as arm error even when both joint encoders are exact. The base, tower and arm should therefore be tested as one structure. The appropriate ballast location depends on the arm’s range and battery placement rather than a generic preference for more robot weight.',
 'Measure wheel unloading and tool-tip motion during combined driving and arm transitions over cable track and platform edges.')

add('ba2298a5d1686ccd7a','intake','ECHO: compliant vector pickup and cone centering',[8],
 'Sponge/noodle roller, dustpan, powered centering flappers and bent-polycarbonate structure.',
 'The binder lists construction; detailed comparative selection reasoning is not supplied.',
 'A broad soft contact can accommodate variation in approach and distribute pressure on a deformable piece. The dustpan supplies support underneath, while the flappers create a separate centering action. That is a different mechanism from merely adding compliant wheels to an arm. The soft material’s wear and compression set can alter intake behavior over an event; the structure must remain aligned while yielding to impacts. Because the binder does not give a complete rejected-alternatives account, these are engineering implications rather than a claim about the team’s exact selection process.',
 'Measure centering success across cone orientations and roller wear, and inspect whether the dustpan or flappers create an escape path.')
add('ba2298a5d1686ccd7a','positioning','ECHO: lightweight telescoping arm and roller end effector',[7,10],
 'Sheet-metal pivot structure, carbon telescope, shimmed hex interfaces and light dead-axle end rollers.',
 'Weight and backlash reduction are explicitly documented.',
 'Reducing distal mass improves both arm acceleration and the chassis stability needed to exploit it. A light telescoping tube still needs sufficient overlap and guidance to resist bending and torsion at full extension. Shimmed interfaces target lost motion, while structure and belt elasticity remain separate error sources. Dead-axle rollers can remove rotating shaft mass and simplify the wheel assembly, but their supports must retain alignment. A recommendation should compare endpoint settling and piece ownership under load rather than claiming a material alone makes the arm fast.',
 'Measure endpoint deflection at full reach and after reversing both axes; inspect telescoping guidance and roller support wear.')
add('ba2298a5d1686ccd7a','endgame','ECHO: nonparallel balance-fork linkage',[9],
 'Carbon-rod forks, nonparallel four-bar lift and over-center deployment with ratchet release.',
 'Lift and tilt relative to a partner and the floor.',
 'A nonparallel four-bar controls orientation as well as translation. That can lift a robot while changing its attitude without another actuator, but the force and mechanical advantage vary through the stroke. Over-center deployment can hold a state mechanically, while the ratchet provides a separate release/retention function. Partner geometry and platform angle determine the contact loads. The design should be retrieved as an alliance-specific balance solution rather than grouped indiscriminately with climbers from other seasons.',
 'Model linkage force through the entire stroke and test with multiple partner undersides and off-axis loading.')
add('ba2298a5d1686ccd7a','special','ECHO: preload catapult and vacuum swiper are distinct tactical tools',[11,12],
 'Spring-released one-shot cube catapult; dual vacuum cups added in a three-day development period.',
 'Preload launch and opponent loading-zone cube acquisition.',
 'A one-shot mechanism can be mechanically simpler than forcing the main manipulator to execute the same autonomous action, but it spends mass on a narrow use. Its value depends on repeatability and the time it frees for the rest of the routine. Vacuum acquisition relies on seal area, surface condition and resistance to peeling; it is poorly described by a generic grip-force number. The swiper is a dated tactical addition, not proof every earlier robot revision carried it. Keep the development date and task boundary attached to the feature.',
 'Test preload release over the allowed setup variation and vacuum retention under peeling loads and imperfect cube surfaces.')

add('a2221ee1dc5a83c0f2','intake','VORTEX: centered under-bumper acquisition',[11],
 'Mecanum front contact, kicker rollers and angled powered funneling wheels.',
 'Accept side approaches and center notes without jamming.',
 'A note arriving sideways or off-center should be translated toward the feeder before the shooter demands a repeatable entry state. Mecanum and angled contacts can supply that transverse velocity, but excess lateral force can fold or wedge the note. A stiff bumper and intake mount preserve the intended compression under defense. The correct performance measure includes successful ownership from the edge of the mouth, not only straight-on pickup at the center.',
 'Map pickup across the mouth with deformed notes, oblique approaches and bumper impacts; observe the first region where motion stops.')
add('a2221ee1dc5a83c0f2','transfer','VORTEX: annular feed removes the intake-indexing heading constraint',[12,13],
 'Two-direction annular feeder supplies a turret without returning it to the intake; 720° cable system.',
 'Maintain goal tracking during acquisition and feeding.',
 'The architectural benefit is not merely a large turret angle. Many turreted designs must rotate to an intake alignment before receiving a note, losing continuous tracking. An annular feed trades that delay for a larger guided path whose friction, seams and direction switching must be managed. Choosing the shorter route can reduce feed time, while a reversal must preserve piece state. The cable system makes the aiming envelope physically usable; without reliable wire guidance, the extra angular range is only a CAD possibility.',
 'Feed at multiple turret headings including through a direction change; test note wear, guide friction and cable-chain operation near both limits.')
add('a2221ee1dc5a83c0f2','scoring','VORTEX: revised shooter separates feed and launch contacts',[14],
 'Second-revision quad-wheel shooter; staged feed rollers; asymmetrical wheels; sector-gear hood.',
 'Controlled note entry and spin for a flatter useful trajectory.',
 'The note’s flexible ring makes its entry orientation and deformation important to launch repeatability. A dedicated first stage can establish the approach before the high-speed wheels impart the final velocity and spin. Asymmetric contact can bias spin, but the resulting flight still needs empirical validation over wear and range. Hood backlash is an angular error that becomes more consequential at some distances than others. The revision label matters: a final shooter image must not silently stand in for an earlier competition version.',
 'Measure entry deformation and shot dispersion with several note conditions; compare hood approaches from both directions and both feed routes.')
add('a2221ee1dc5a83c0f2','scoring','VORTEX: amplifier is a second routing destination',[15],
 'Roller carriage on an elevator routes notes to amp/trap and accepts human-player feed.',
 'Support multiple scoring and shuttling roles.',
 'The amplifier is not just a final scoring roller. It adds a branch to the note-routing state machine and a distinct human-player acquisition path. Shared use can justify the mechanism’s mass if those roles are valuable in the alliance plan, but creates more transitions and collision states. Passive trap-reaction wheels supply a structural contact during climbing, tying its geometry to the endgame sequence. The agent should explain those dependencies before recommending the package to a team that only needs one of its functions.',
 'Test every routing transition and interrupted sequence; verify that the trap reaction contact does not dislodge the stored note.')
add('a2221ee1dc5a83c0f2','endgame','VORTEX: rapid rope climb establishes trap height',[16],
 'Sprung hook arms and a low-mounted rope winch pull the robot to trap height.',
 'Lift quickly while enabling the amplifier to reach the trap.',
 'The climb’s lift distance is determined by the scorer’s required geometry, not just the minimum suspension score. Gas springs can deploy the hooks while the winch retracts them under load. A rope path needs secure anchors, consistent winding and sufficient clearance as the robot swings. If retention relies on drivetrain or motor braking behavior, that exact power-off state should be validated rather than assumed. The trap sequence must preserve the reaction contact and note orientation throughout the lift.',
 'Test acquisition, lift, trap alignment and disable as one sequence with several chain heights and swing angles.')

add('fd6ffec203a0f28f66','intake','OPR 2024: chassis and module geometry create the intake path',[4,6,8],
 'Modified front module clearance; under-bumper conveyor; post-Newmarket aluminum side plates and added bracing.',
 'Wide pickup, consistent centering and impact rigidity.',
 'An under-bumper path consumes the same volume as frame rails and module motors, so module orientation and mounting plates are part of the intake design. Increasing plate rigidity preserves compression but can transmit more collision load elsewhere. The documented event boundary should be retained: the stronger side plates and bracing were a precautionary update rather than necessarily the initial robot. Intake width is useful only if the full path can move off-center notes without trapping them at a module or frame corner.',
 'Test side pickup and corner impacts, then compare roller alignment and chassis squareness before and after the update.')
add('fd6ffec203a0f28f66','scoring','OPR 2024: pre-compression, differential spin and revised release angle',[11,13,14],
 'Pre-compression contacts, independent left/right drives, low-backlash pivot; flywheels later tipped down 6°.',
 'Consistent feed and greater useful shot range.',
 'A flexible note can enter the same nominal wheel gap in different shapes. Pre-compression aims to control that shape before final acceleration. Independent side speeds then create spin, while mechanically linked upper/lower contacts preserve another aspect of consistency. A six-degree structural change alters the reachable trajectory envelope even if the control software is unchanged. Distinguish output speed, compression and release geometry when diagnosing misses: increasing RPM cannot necessarily compensate for a deformed or inconsistently presented note.',
 'Compare shot distributions before and after the geometric revision with the same notes, recording entry deformation and wheel recovery.')
add('fd6ffec203a0f28f66','endgame','OPR 2024: pneumatic lift and an explicitly different disable behavior',[16],
 'Dual pneumatic cylinders and revised double hook; single-acting valve retracts on loss of power.',
 'Fast hanging and compatibility with a partner-loaded chain.',
 'A pneumatic climber stores energy before the lift, reducing the need for a large electric winch during the final action. Available force depends on regulated pressure, piston area and the retracting-side rod area, while repeated actions consume finite stored air. The hook geometry must accommodate a chain already displaced by a partner. The described valve behavior is specific to this plumbing and control configuration; it should not become a generic assumption about all solenoids or an instruction to rely on an untested after-buzzer action.',
 'Test force and timing at the lowest expected pressure, including partner chain displacement and the actual disabled valve state.')
add('fd6ffec203a0f28f66','controls','OPR 2024: adapt autonomous to whether a note is actually present',[20],
 'Game-piece camera, drive-to-point correction, missing-note diversion and velocity-compensated aiming.',
 'Avoid wasting autonomous time on absent or displaced notes.',
 'An intake with a large acquisition envelope becomes more useful when the path can correct toward the observed note. The controller must decide early enough that a failed attempt does not consume the rest of autonomous. A missing-note branch is a strategy choice tied to contested supply and partner routes, not simply a vision feature. The shot system also depends on current robot velocity and a stable angle reference. Database recommendations should include these feedback assumptions alongside the mechanical pickup.',
 'Displace or remove expected notes and test diversion timing, partner-route safety and the resulting end pose.')

add('3b948aa1f27320cf6d','intake','ROTI: under-bumper pickup feeds a movable shooter',[7],
 'Full-width intake with pickup rollers and centering wheels.',
 'Center notes before they enter the shooter.',
 'The collector has to supply a consistent location and shape to a scorer whose height and angle can change. Centering at the floor reduces the uncertainty the moving receiver must handle. A shallow pickup can preserve chassis protection but needs clearance around module and frame structure. Surface speed should capture a note without throwing it past the receiving contact. The effective system includes the handoff state that determines when the elevator may move away.',
 'Test off-center acquisition and interrupted handoff while varying the receiver’s initial height and angle.')
add('3b948aa1f27320cf6d','positioning','ROTI: one lift creates scoring height and endgame capability',[5,8,9],
 'Continuous rope lift with overextending carriage; passive lower hooks retain the chain after initial lift.',
 'Use one shooter for speaker, amp and trap.',
 'Moving the shooter upward changes its release geometry and can improve defended shot access, while stowing preserves travel routes under the stage. That broad capability costs raised mass and a multi-state handoff. The passive lower hooks are central to the climb: they take over the suspension load so the elevator can extend again for trap scoring. Without that load transfer, the same actuator cannot independently hold the robot and reposition the scorer. This is an architectural sequence rather than an elevator plus an unrelated climber.',
 'Verify passive-hook engagement before re-extension; test full-height stability and stowed route clearance with the actual scorer mass.')
add('3b948aa1f27320cf6d','scoring','ROTI: counterbalanced pivot and shaped note feed',[10,11],
 'Gas-spring counterbalance; output-angle sensing; asymmetric launch speeds; conical/mecanum feeder contacts.',
 'One shooter serves several release geometries.',
 'A counterbalance reduces gravitational torque but changes the motor’s required effort across the angular range. Sensing the output helps distinguish gearbox motion from actual scorer angle. Conical and mecanum feed contacts can shape and spread the note before launch; their useful effect depends on how the flexible ring deforms. The front roller angle also affects trap delivery, so optimizing only speaker shots may degrade another required mode. A recommendation needs the complete scoring envelope and mode transition tests.',
 'Measure output-angle hysteresis and shot dispersion in every scoring mode, with both new and damaged notes.')

add('53aa4619f3f5cdb626','scoring','Team Kika Mana: technical sheet supports construction, not a complete design history',[1],
 'Asymmetric 3-inch Colson shooter; side-compression feed; rack hood; elevator-mounted scoring package.',
 'The sheet attributes spin to shot accuracy; broader selection reasoning is not documented.',
 'This source is useful for geometry and component identification but should not be promoted to a full engineering binder. Different wheel count or speed across the note can create spin; compression controls the contact state and must remain consistent through the feed. A moving scorer adds position and angle errors that require joint calibration. The exact tolerance, rejected alternatives and event-by-event revision history are not established by one illustrated sheet. The agent should use it to locate a mechanism family and then seek CAD, interviews or team replies before claiming why every dimension was selected.',
 'Validate wheel arrangement and compression in CAD, then test dispersion and elevator deflection across the intended scoring range.',
 'One-page technical sheet only. Complete trade studies, final reductions and season revision history remain unverified.')

add('web-9470','scoring','9470: triple-channel scorer to an open drum path',[],
 'Triple shooter at early events; DCMP drum uses a full-width roller, pivoting hood rollers and three feeder rollers.',
 'Higher ceiling without a channel-settling step.',
 'The significant change is the removal of restrictive channel interfaces, not simply a larger launch wheel. Dividers can stabilize a piece path while creating an arch or an extra alignment delay; an open drum path can accept a broader front but needs consistent compression across its width. The early triple shooter remains an intentional schedule choice rather than a failed idea in every context. A team with an early event can rationally choose a lower ceiling that preserves practice time, then rebuild once the feed and current demands are understood.',
 'Compare first-shot delay, sustained output and nearly-empty-hopper output across both configurations under the same supply conditions.')
add('web-9470','intake','9470: reinforce the proven failure while preserving geometry',[],
 'Worlds intake uses stacked quarter-inch SRP side plates with leaf-spring mounting and reinforced motor plates.',
 'DCMP damage made intake survival the next priority.',
 'Changing material without changing the mounting boundary may fail to create the intended compliance. A leaf-spring arrangement needs room to bend, a predictable load path and fasteners that do not clamp the compliant region into an unintended rigid joint. Reinforcing the motor plate addresses a concentrated load while preserving the pickup geometry that the drivers already know. This is a useful rebuild principle: once the collection and shot behavior work, the largest improvement may be a structural interface that prevents losing the entire match rather than another nominal-rate optimization.',
 'Measure deflection and residual alignment after repeatable corner hits, and time a side-plate replacement without disturbing the roller assembly.')
add('web-9470','transfer','9470: floor redesign follows the scorer and service needs',[],
 'Final floor has eight mixed-compliance rollers, one X60 and a two-screw pivot for access.',
 'Simpler feeding and fast electronics service.',
 'A floor that works for one shooter architecture may create unnecessary volume and transfer stages for another. Mixing hard tubes and compliant contacts can maintain support while encouraging fuel through a problematic region. The service pivot adds a deliberate state outside gameplay: technicians must be able to open the floor, reach electronics and restore alignment quickly. That can improve event reliability more than reducing a small amount of mass. Include cable routing, fastener retention and the post-service check in the architecture record.',
 'Time an actual electrical repair through the pivot, then verify floor alignment and feeding after repeated open/close cycles.')
add('web-9470','controls','9470: empirical calibration and practice deadline',[],
 'Interpolated shot map, measured first-shot correction and time-of-flight lookahead; fixed pre-event ship deadline.',
 'Preserve practice and tuning time.',
 'An empirical map can be a technically rigorous choice when it captures the dominant real-world exit behavior within the available build window. It still needs enough sampling, a stable mechanical reference and a policy for replacing worn surfaces or changing fuel. The deadline is part of the architecture’s feasibility: every additional mechanism competes with the time needed to calibrate and drive it. A borrowed model should include its data-collection procedure and failure fallback rather than promising accuracy from a published algorithm name.',
 'Repeat calibration after surface replacement and at low battery, then validate moving shots outside the original tuning trajectories.',
 'The process page is a team account. Dynamic homepage counters rendered as zero in static retrieval and were not imported as historical records; one L1 valuation on the page is not accepted as a rules authority.')

add('web-4414','drivetrain','RIPCURRENT: shape the chassis and bumpers around the feed system',[],
 'Chamfered 25×32-inch base; offset battery rail; structural bumper/hopper walls and low electronics.',
 'Preserve low rotor diameter and storage area within the perimeter.',
 'A singulator occupies a swept area, not just a rectangular bounding box. Changing chassis corners can preserve the parts of that area that most improve ring diameter while removing less useful perimeter. Moving the battery to an edge creates a new structural problem because the rail still has to carry drive and impact loads. Using the bumper backing as a hopper boundary can reclaim interior width, while tying scorer alignment to a removable impact structure. The package needs a repeatable bumper interface, and the stored-fuel center of mass must be evaluated alongside the empty robot.',
 'Reinstall bumpers and measure scorer alignment; test loaded lateral acceleration and rotor clearance after representative impacts.')
add('web-4414','transfer','RIPCURRENT: independently driven rotor, packing relief and passive contact',[],
 'Separate rotor/feed drives; shaped fin and wrap guides; passive rollers and omni contacts.',
 'Reduce packing pressure, friction and belt slip.',
 'A bulk pile can load the singulator even when the exit path is clear. Agitating the pile and supplying the launch stream are different motions, so separating drives gives useful tuning freedom. A shaped fin can alter where that pile pressure is released; passive rollers reduce sliding resistance where balls push against each other. These details explain why a DYE-inspired design cannot be generalized as a generic circular indexer. The critical behavior is the changing network of contacts at full, partial and nearly empty loads, including a controlled reverse to clear a bridge.',
 'Measure stream continuity and current at several load states; observe whether agitation increases entry occupancy or merely recirculates fuel.')
add('web-4414','intake','RIPCURRENT: compliant racks and a separately latched lower contact',[],
 'Stacked polycarbonate racks; primary and lower powered rollers; strengthened hubs and shear interfaces.',
 'Impact compliance and reliable pickup with retained storage.',
 'Stacking plates can create controlled flex only if the plates and fasteners permit the intended relative motion. A low roller that remains deployed adds another ownership contact near the bumper, while its latch removes continuous holding load from an actuator. Stronger hubs and distributed shear interfaces address local failure modes that a thicker arm alone may not fix. The collector also moves storage boundaries, so its success must be measured while the hopper is loaded and the side walls are being pushed by fuel.',
 'Test diagonal wall contact, rack synchronization and lower-latch retention; inspect roller-end alignment and capacity after impact.')
add('web-4414','scoring','RIPCURRENT: compact shooter swept volume and stored energy',[],
 'Four-X44 3-inch flywheel; added dense inertia; powered hood roller; vertically stacked motor package.',
 'Reduce protrusions while preserving the desired launch contact.',
 'A compact turret can improve the whole robot by leaving more feed and storage volume around its swept envelope. That benefit must be weighed against launch-contact repeatability, motor cooling, wire access and flywheel recovery. Dense inertia stores energy in limited space, but increases spin-up energy and bearing loads. A powered hood contact changes the spin state and must remain geometrically consistent as the hood moves. The key comparison with a drum is delivered scored fuel during usable windows, including time moving and acquiring, rather than a single instantaneous output rate.',
 'Map exit velocity and spin versus hood angle, turret heading and volley length; inspect belt tracking under acceleration.')
add('web-4414','controls','RIPCURRENT: calibration and uncertainty remain empirical',[],
 'Team reply describes robust-shot selection followed by measured angle and velocity calibration.',
 'Choose trajectories tolerant of exit-state errors.',
 'A nominal ballistic solution is not enough when fuel compression, wear and launch contact change the actual exit velocity. Searching for a region of successful trajectories can improve tolerance, but the model must be anchored to measurements of the real mechanism. Separate localization, hood-reference and exit-speed errors before retuning: otherwise one correction can conceal another. This is a transferable technical procedure, not evidence that every team should adopt the same equation set or that the robot can score under every motion and defense condition.',
 'Use stationary known-pose tests to isolate launch error, then add translation, rotation and tilt one at a time.',
 'Construction is from the previously reviewed binder and current indexed binder text; calibration explanation is from team reply /519602/116. Current direct binder download returned 403. Existing source images were retained; no new visual watching is claimed.')

add('fea3938f462d86d32d','drivetrain','FIREFLY: wheel stiffness is part of end-effector accuracy',[10,11],
 'Custom Grip Lock hubs, lowered Mk4-C base and later lower drive gearing.',
 'Reduce tire flex and preserve a stiff floor-to-tool reference.',
 'Wheel compliance permits the chassis to rotate relative to the carpet even when the frame and elevator are stiff. The resulting angular error becomes a larger displacement at an elevated tool, so a tire-hub change can improve L4 placement without changing the wrist. A low frame and ballast distribution address another component of the same stability problem. The gearing revision also changes acceleration and braking behavior; it needs drive retuning with the real mechanism load. Do not treat a module model or a free speed as a complete explanation of placement repeatability.',
 'Measure tool-tip displacement under known lateral load and during stopping, separating tire deflection from lift deflection.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/502317/5']
add('fea3938f462d86d32d','positioning','FIREFLY: short lift and low-mounted carriage actuators',[8,12],
 'Single-stage counterbalanced lift; thin-wall tube; algae, coral and arm drives mounted low on carriage.',
 'Low moving center of gravity and direct piece delivery.',
 'Remoting the roller drives removes mass from the far end of the arm while keeping it on the lift carriage. That reduces one component of arm inertia without eliminating the carriage mass that the lift must accelerate. A single-stage lift can simplify guidance but requires the arm to supply the remaining reach and orientation. Counterbalance reduces gravity demand, while belt tension and routing still determine tracking and friction. The integration goal is a useful task sequence with no wait for piece delivery, rather than a collection of independently fast axes.',
 'Measure lift current and tool settling during combined motion; verify belt tension and direct-handoff clearance at every relevant pose.')
add('fea3938f462d86d32d','intake','FIREFLY: sideways orientation while maintaining coral ownership',[14],
 'Sideways reorienting belt, compliant tube rollers, independent roller drives and twisted-belt transmission.',
 'Direct handoff or controlled L1 without staging the coral.',
 'A sideways belt gives the tube a deliberate transverse velocity rather than relying only on passive wedges. The remaining contacts must keep ownership while that reorientation happens; an unconstrained gap can erase the advantage. Separate roller drives permit holding a tube for L1 or continuing into the end effector, but create more state choices and sensor requirements. Twisted and bent belts solve an off-axis power-routing problem, while adding tracking, wear and alignment concerns. Their tension cannot be chosen solely for torque transmission if the belt also participates in piece contact.',
 'Film diagonal and lengthwise entries through both L1 and handoff branches, then repeat after belt wear and an intake impact.')
add('fea3938f462d86d32d','intake','FIREFLY: dedicated floor-algae route integrates with climb',[13],
 'Counter-rotating floor-algae rollers; reinforced printed bevel gears; three-piece jackshaft around climb packaging.',
 'Acquire algae and deliver it to the arm without subsystem interference.',
 'A dedicated floor pickup lets the main end effector specialize in retention and scoring rather than reaching a difficult carpet pose. That value must exceed the added mass and handoff complexity. Segmenting the jackshaft can make assembly possible around another subsystem, but every joint adds an alignment and torque-transfer interface. Printed bevel gears need stable bearing support and an appropriate tooth load; a successful material in another mechanism does not certify this one. The pathway should remain useful if the climb is damaged, consistent with the robot’s stated degraded-operation objective.',
 'Test floor acquisition and handoff while climb is stowed, partially deployed and disabled; inspect bevel alignment under peak capture load.')
add('fea3938f462d86d32d','scoring','FIREFLY: internal coral grip and algae torque selected by test',[15],
 'Internal coral gripping; compliant placement geometry; shared tool also acquires and scores algae.',
 'Control both pieces while keeping moving structure light.',
 'Gripping inside a tube changes the reference surface and can leave the outside clearer for placement. It still needs a controlled release and enough compliance to tolerate the branch without wedging the tool. Algae retention is a different torque problem: the wheel must deform and hold a soft sphere rather than simply spin at the desired acquisition speed. A practical way to choose the ratio is to measure the required final-shaft torque, then check speed and motor current under that load. This is more informative than selecting a reduction from a famous robot without matching its compression and geometry.',
 'Measure algae pull-in torque and holding current, then test coral release with intentional branch misalignment and the same worn contacts.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/502317/11']
add('fea3938f462d86d32d','endgame','FIREFLY: powered magnetic cage acquisition and sensed latching',[10,16],
 'Magnetic TPU intake wheels pull cage into two one-way latches; winch/rotation share a drive.',
 'Capture before automatically lifting.',
 'Magnetic attraction can improve the first contact with a steel cage, but the final robot load should pass through the designed latch and structure. Two capture switches give the controller a stronger condition than assuming engagement after a fixed time. Shared winch and rotation power saves hardware while tying the phase sequence to transmission geometry. The dated timeline records later additions to the cage collector and automation, so the final system should not be projected back to the robot’s first event. Total climb time includes acquisition and settling, not just the powered lift.',
 'Test one-sided and swinging-cage contact, sensor disagreement and disable retention; confirm the latch carries the suspended load.')
add('fea3938f462d86d32d','transmission','FIREFLY: custom cycloidal reduction is an iterative capability',[17],
 '23:1 dual-disc cycloidal; hardened steel discs; rolling pins; team reports about 0.3° backlash.',
 'Compact, lightweight low-backlash joint drive.',
 'A cycloidal gearbox trades ordinary spur stages for a shaped eccentric load path with multiple contacts. Opposed discs can reduce dynamic imbalance, but machining accuracy, pin support and eccentric bearings still control vibration, efficiency and backlash. The reported backlash is a team result for its design and measurement conditions. It should not be assumed for a copied outline made with a different process. This is a mature, revised manufacturing capability, so its adoption cost includes inspection, heat treatment and assembly knowledge rather than just CAD availability.',
 'Characterize output backlash, temperature and efficiency under the intended reversing load, and inspect contact wear after repeated shock cycles.')

add('c3e9d55e9042421508','intake','NOCTURNE: passive centering trades motor count for geometry',[10],
 'Fast under-bumper rollers with passive wedges replacing an active-centering beta design.',
 'Reduce current while retaining useful acquisition.',
 'A passive wedge can convert forward motion into centering without another motor, but requires the right approach velocity, contact friction and space for the note to move laterally. If a note is pinched against the wedge before it is captured, a faster roller can make the jam worse. The source represents the Granite State configuration, and a later team account describes impact failures and difficult repairs. The observed update is therefore part of the technical recommendation: a pickup can satisfy its contact objective while losing event value through poor service access.',
 'Test wide and oblique capture, then time a damaged roller replacement and verify alignment after repair.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/445350/82','https://www.chiefdelphi.com/t/445350/95']
add('c3e9d55e9042421508','positioning','NOCTURNE: reuse a familiar joint and simplify the architecture',[3,6,7],
 'Single-joint arm, paired planetary drives, chain final reduction and output-angle sensing.',
 'Reuse 2023 experience and preserve time before week 1.',
 'A familiar joint can reduce the number of new mechanical and software problems, which matters when experienced students have graduated. It still needs a force-path and backlash review for its new payload. Multiple chain runs can distribute load but require matched tension so one does not carry nearly everything. A hard-stop shot gives a mechanically referenced fallback when vision or arm control fails, but repeated impact into the stop can change alignment. Schedule feasibility is a legitimate architecture criterion alongside reach and nominal speed.',
 'Measure output repeatability under reversing load and after repeated hard-stop approaches; test the documented fallback with vision disabled.')
add('c3e9d55e9042421508','scoring','NOCTURNE: stage the note before launch while minimizing distal mass',[8,9],
 'Eight launch wheels; lightweight staging rollers and low-friction guides integrated with the scorer.',
 'Hold and preaccelerate without another storage mechanism.',
 'A staging section can establish a repeatable note entry and prevent an uncontrolled piece from touching the flywheels prematurely. Using a smaller motor reduces moving mass only if it still supplies enough capture and feed force. The structure must resist both wheel vibration and arm acceleration; a flexible mount changes the launch angle even with correct encoder readings. A grippy stage and low-friction guides serve different purposes: one supplies drive while the other avoids wasting that effort. Test the full transfer at operating speed rather than assuming more grip everywhere is better.',
 'Measure note-entry timing, launch dispersion and structure vibration with new and worn notes while the arm is moving.')
add('c3e9d55e9042421508','controls','NOCTURNE: the real field exposed calibration and fallback needs',[12,13],
 'Pose-based shot map, motion lookahead and automatic intake stop after note detection.',
 'Aim through brief vision loss and avoid accidental extra possession.',
 'A consistent pose estimate can still be systematically wrong if the practice target or camera geometry is wrong. Calibrating a lookup table against an inaccurate practice field can make reliable local shots fail at an event. A safe fallback should use a mechanically repeatable pose with a validated close shot, rather than trusting the same mistaken distance model. The fixed under-bumper intake also creates a possession-control requirement because it cannot simply retract away from a second piece. Mechanical geometry and sensor timing must be verified together.',
 'Validate against measured field geometry, remove expected vision input, and test closely spaced notes for unintended second-piece capture.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/445350/82','https://www.chiefdelphi.com/t/445350/95']

# First-party replies supplement, rather than masquerade as, a formal binder.
add('discussion-2542026','transfer','OVERLOAD: floor versions change what should be copied',[],
 'Alpha floor, SVDE split-axle floor, CVDE continuous axle and Worlds captured fixed-center floor are distinguished.',
 'Eliminate binding, belt escape, shaft failure and fuel trapped beneath the floor.',
 'An adjustable joint can make prototyping easier while becoming a weak structural interface under a full hopper. A split axle is especially sensitive because bending, thread retention and tension adjustment meet at the same small connection. Capturing a cam follower must account for lateral deflection as well as the nominal two-dimensional motion; otherwise the follower can escape around a track that looks constrained in a sketch. Fixed centers can improve reliability once the correct tension is known, but require accurate geometry and assembly. The correct inspiration for a rebuild is a dated floor version with its failure history, not simply “254 belts.”',
 'Load the floor unevenly, push the intake backward, test lateral racking and inspect whether fuel can get underneath before copying the travel geometry.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/516252/105']
add('discussion-2542026','transfer','OVERLOAD: shared feeder power is a different optimization from floor tilt',[],
 'Team says final floor tilt helped modestly; compares its output with 2910’s mechanically shared feeder/floor drives.',
 'Recognize the changing load distribution during discharge.',
 'A hopper floor initially accelerates under a large pile load, while the downstream feeder can dominate later in the same discharge. Mechanically sharing motors can let the available power serve those changing demands instead of leaving some motors lightly loaded while another stage struggles. That benefit trades away independent control and can transmit a jam farther through the system. Extra floor tilt is a separate variable: it may improve the entry geometry without justifying a complicated cam and narrow packaging. Compare the complete energy and service cost rather than assuming every feature of the reference robot is worth retaining.',
 'Log floor and feeder torque over a full discharge; compare independently powered and shared-power layouts under identical contact geometry.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/516252/113']
add('discussion-2542026','development','OVERLOAD: a kitbot and prototypes test the architectural premise',[],
 'Early plywood shooter and modified kitbot tested wide launch; belt and roller floors were compared before alpha integration.',
 'Establish piece contact and multi-ball behavior quickly.',
 'A low-fidelity test should answer the uncertainty that changes the architecture. Before modeling a sophisticated drum, demonstrate that the available goal, piece and launch geometry can accept simultaneous streams without destructive interaction. The prototype then needs adjustable compression and a representative feed, not a beautifully finished chassis. If a simple kitbot already tests the relevant contact, reusing it can preserve time for the harder integration questions. Later failures in floor structure show the boundary of that early evidence: successful launch physics does not certify tensioning, impact survival or service access.',
 'Write the decision the prototype will change, test representative piece conditions, and reserve a second integrated test for load and flow.')
RECORDS[-1]['additional_sources']=['https://www.chiefdelphi.com/t/516252/116']

# Preserve a key team-stated L1 motivation and the corresponding acquisition limit.
for _n in RECORDS:
 if _n['binder_id']=='6054858ce2266dbdc2' and _n['title'].startswith('AURELIA: separate coral'):
  _n['team_stated_reason']='The team explicitly ties this intake choice to horizontal L1 placement, alongside concerns about a separate centering/indexing system.'
  _n['additional_sources']=['https://www.chiefdelphi.com/t/500435/131']
  _n['limitations']='Team reply reports difficult horizontal approaches beyond about 45 degrees, extensive practice and late-season durability work. Successful match execution is not proof of effortless any-orientation pickup.'
