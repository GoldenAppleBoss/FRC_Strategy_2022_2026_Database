import sys,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from robot_studies_v5 import STUDIES,add
add('2023-1323','Buffered cube supply and separate reach axes create an alliance tool',107,435,
 'A wide overhead cube collector funnels through an internal tunnel to a claw. Separate vertical and horizontal elevator axes plus an articulated arm provide reach. The interview distinguishes normal cone pickup from a slower tipped-cone uprighting maneuver.',
 'The team explicitly describes designing for high-level play and wanting a differentiated capability. The physical room for multiple pieces is not permission to possess them outside the applicable protected zones.',
 'Buffering can decouple human-player delivery from the next placement, but only within the game’s legal possession constraints. Extra reach axes also create collision and maintenance demands. The slower cone fallback is capability, not evidence it is the preferred cycle.',
 'Test legal buffered operation, tunnel recovery, both-axis settling and cone fallback cycle cost.')
add('2023-2468','A narrower claw purchases access to contested low geometry',107,250,
 'A narrow gripper handles both pieces, with a wide tilted cascading elevator and wrist. Cross-bracing resists parallelogram deformation; shimmed gearing and a chain wrist reduce play under the collector load.',
 'The retained account ties claw width to fitting between hybrid dividers for retrieval/re-scoring. The team says a chain held the wrist load better than its belt trial.',
 'Maximum acquisition width is not always optimal. A smaller receiver can access a task a wider collector cannot, provided pickup tolerance remains acceptable. Elevator tilt can improve approach geometry while changing tip margin and wrist loads.',
 'Measure pickup tolerance, low-node retrieval clearance, wrist hysteresis and full-extension stability.')
add('2023-2767','A familiar carbon elevator reduces development uncertainty, not every failure mode',78,365,
 'A wide cube collector feeds the upper gripper while cones use direct acquisition. A carbon elevator tilts on a sector mechanism; an escape region avoids trapping a second piece.',
 'The team explicitly cites prior carbon-elevator experience, limited build time and a desire for reliable fast scoring. Low mass addresses concern about crossing the charge station with a tall structure.',
 'Mechanism familiarity is a legitimate resource constraint. Tilting extends effective reach but couples scoring geometry to support-polygon and drivetrain pitch. An extra-piece escape path must preserve control of the intended piece and the season’s possession rules.',
 'Test charge-station pitch with the mechanism safely stowed, tilt stiffness and rejection of an unintended extra piece.')
add('2023-2910','A compact telescoping package still needs piece-specific poses',118,270,
 'A two-stage telescoping arm, shoulder and wrist provide grid reach while stowing low. The source demonstrates distinct floor-cube, tipped-cone, upright-cone and shelf-acquisition poses using dead-axis roller contacts.',
 'The stated objectives are speed, compactness, all-level reach and low center of gravity.',
 'One gripper does not imply one acquisition state. The arm and wrist jointly create the contact conditions for each piece, while extension changes torque and clearance. A copied roller layout without those poses and transitions is incomplete.',
 'Validate every acquisition pose and the connecting paths, then measure loaded settle time at maximum reach.')
add('2023-3005','Separate contact development can outperform one compromised gripper',110,510,
 'A telescoping arm on a braced A-frame uses a highly articulated wrist and distinct cone/cube contact arrangements. The interview reports eleven cone-intake iterations versus four cube-intake generations.',
 'The team’s stated goal is a light, fast robot that acquires cones in different orientations and scores high/mid; the different contact systems emerged through tests.',
 'The separate iteration counts show that the two pieces presented different problems. Avoid inferring that a more complex-looking gripper was unnecessary without comparing acquisition and release reliability. Bracing saves upper structural mass only if its tension and anchors remain repeatable.',
 'Test both pieces, cable-brace tension and wrist motion limits; include calibration and replacement time.')
add('2023-3467','A week-zero prototype must not be treated as the final competition configuration',78,480,
 'The early double-jointed arm uses low gearboxes and MAXSpline transmission; the interview states roughly 100:1 at each joint. Pneumatic opening changes cone/cube grip. A proposed collector/four-bar was not yet installed in this snapshot.',
 'The team emphasizes getting a simple arm running early for software/setpoint work and describes profiled control for smooth repeatable movement.',
 'A working early mechanism is valuable development infrastructure, but a proposed collector cannot become a fielded capability merely because it appears in the interview. Piece-dependent jaw opening also requires possession-state handling.',
 'Verify later installed versions separately and test grip retention throughout profiled motion.',
 'Early snapshot only. Automatic captions are not sufficient to certify detailed motor/transmission part numbers.')
add('2023-3538','A virtual linkage must preserve useful contact at every task pose',109,400,
 'A curved roller gripper directly acquires both pieces on a virtual-four-bar/extension architecture. Linkage/sprocket geometry serves floor, station and scoring positions; holding rollers idle at lower speed in the last useful direction.',
 'The team identifies fast cycles and a wide acquisition aperture as priorities, and describes testing drivetrain/contact choices for charge-station traction.',
 'A virtual linkage can coordinate joints mechanically, but its coupled path still needs field/robot clearance. Idle roller direction must match possession state or it can eject the wrong piece.',
 'Test every acquisition/release pose, interrupted transitions and low-speed holding under chassis acceleration.')
add('2023-4414','A wide elevator enables a later collector, with a real packaging cost',146,335,
 'A belted elevator and chained virtual four-bar place a shared claw. A later cube collector passes through the elevator opening. The source describes a custom second drive motor on each module and a nominal ratio/speed claim.',
 'The team explicitly says the wide opening made the late cube handoff possible. Additional drive power is a configuration-specific choice, not a requirement for every copied elevator.',
 'Future expansion space can create strategic flexibility, but extra width and power hardware consume mass and electrical margin from the beginning. Separate the original direct claw from the later cube-assisted acquisition.',
 'Measure handoff tolerance, frame torsion and loaded drivetrain current before copying the full package.')
add('2023-5940','Passive cone reorientation removes an axis only if the handoff remains tolerant',76,300,
 'A two-stage elevator has an overextending carriage and internally routed Dyneema. The rear collector vectors cubes and uses a compliant cone handoff to correct orientation before the scoring gripper receives it.',
 'The source links internal line routing to avoiding snags. The retained account describes passive cone reorientation in place of another controlled axis.',
 'Moving orientation work into compliance reduces actuator/control count while making friction, piece pose and guide geometry decisive. Internal rigging protects lines but complicates inspection and replacement.',
 'Test extreme cone approaches, worn pieces and line service access; distinguish smooth demo transfer from statistical handoff reliability.')
add('2023-6036','Deliberately omitted floor cones preserve a reliable preferred cycle',75,330,
 'A double-jointed arm keeps both joint transmissions low. A wide cube collector uses compliant guides; cones are acquired at the double station rather than through a floor-cone mechanism. Collector material iterations address trapped or damaged cubes.',
 'The team chooses arm freedom to permit software iteration and targets rapid pickup-to-setpoint motion. The retained account explicitly omits floor cones in favor of reliable station work.',
 'Missing a task can be a deliberate architectural trade. That trade depends on station access under defense and the cost of a failed floor recovery, not a blanket claim that floor cones lack value.',
 'Measure defended station cycles, cube handoff damage and arm settle time; provide a recovery plan when station access is blocked.')
add('2023-6329','Two piece modes coordinate a tilted elevator and motorized wrist',108,250,
 'An Everybot-inspired gripper changes wheel orientation and adds retaining netting for cubes. A tilted elevator and wrist acquire and place directly; software coordinates mode-specific heights, wrist angles and roller directions.',
 'The source identifies containment and shared piece handling as the gripper’s purpose. Color cues indicate the selected mode; they are not themselves a vision classification result.',
 'A shared effector needs different states for different pieces. Confusing selected cone/cube mode with sensed possession can produce the wrong approach or release even if every motor reaches its setpoint.',
 'Test mode disagreement, partial pickup and retention during tilt/wrist movement.')
add('2022-111','Removing contact points can improve cargo flow',79,370,
 'The collector was repeatedly revised to remove dead zones and pinch points. A pneumatic gate separates stored cargo from the launcher, with a kicker and two capacity sensors. The retained source distinguishes main/back-wheel choices and a sequential traversal climb.',
 'The team explicitly ties collector iteration to reliable acquisition rather than simply higher roller speed.',
 'A gate decouples possession from launch readiness. More grip can create an unwanted stable pinch, so the test must include side-by-side cargo and partial entry, not only single clean pickups.',
 'Measure jam/recovery frequency and feed latency with worn cargo; test gate timing during wheel recovery.')
add('2022-118','Acceleration, protected acquisition and climb CG were iterated separately',79,735,
 'The retained technical account describes a compliant dead-axis intake, isolated kicker, turret and adjustable hood. A coarser hood rack addressed skipping. The interview describes changing drivetrain gearing for acceleration under defense and shifting climb CG by rotating the arm.',
 'The team explicitly reports insufficient acceleration after States and a one-to-two-second climb improvement from the CG change.',
 'Maximum free speed is not defended cycle performance. Climb timing also depends on gravitational motion and hook approach, not merely winch speed. Separate the filmed later configuration from earlier competitions.',
 'Measure loaded acceleration, hood backlash and repeatable climb completion, preserving the reported timing conditions.')
add('2022-125','Impact-resistant acquisition and reduced spin require coordinated contacts',80,410,
 'A wide dead-axis collector feeds a curved S-path and hooded launcher with powered upper contacts to reduce backspin. The interview discusses planned bouncing-cargo improvements and future climb automation, while the filmed climb remains manually sequenced.',
 'The source explicitly identifies fast acquisition and impact resistance as collector priorities.',
 'A controlled transfer can prepare incoming speed/spin, but each curve introduces another compression interface. Planned Velcro and planned automation must remain unfielded at this snapshot; neither can be used to explain its existing results.',
 'Test side impacts, bouncing entry, full-path current and manual climb timing before attributing later automation benefits.')
add('2022-148','Low hardware placement and staged turret feeding share scarce volume',76,475,
 'An inverted swerve arrangement moves motors low, while a protected collector and printed guide feed staged cargo to the turret. A limit switch and color sensor support possession/rejection. The climb uses retained hooks and a rotating arm.',
 'The team identifies top-side packaging space as a reason for the inverted modules. More exact collector optimization intent remains in the retained source bundle rather than the selected excerpt.',
 'Lower motors can free the turret/feed envelope without eliminating service and cable constraints. Color detection and staged possession need separate states so a delayed classification cannot feed the wrong cargo.',
 'Test sensor latency, partial entry and turret-angle transfer clearance; verify climb hard-stop and disabled retention.')
add('2022-176','A productive scorer may rationally skip the climb in some playoff roles',75,660,
 'A compliant four-bar collector and belt centering feed a turret/hood launcher. Capacity indicators and operator rejection coordinate cargo state. The automated climb is contrasted with continuing to shoot.',
 'The team explicitly says two partners capable of traversal can make continued scoring preferable in playoffs, while qualification bonus needs may require its climb.',
 'Climb value is marginal and alliance-specific even in a season where climbing is generally important. This is not evidence that the 2022 climb was universally irrelevant, nor justification for projecting its value into 2026.',
 'Compare expected scored cargo during the whole climb interval with climb reliability, partner capability and qualification RP needs.')
add('2022-179','Break symmetric jams and choose a reliable climb pace',79,550,
 'Foam collector contacts replace earlier rubber/mecanum choices; agitation addresses two-cargo jams. The retained account describes staged wrong-color ejection, a powered upper roller added after South Florida and a hooded turret. The team reports a roughly ten-second traversal with faster but less reliable trials.',
 'The source explicitly prefers the slightly slower climb because faster operation sometimes behaves unpredictably.',
 'A peak mechanism time should not replace a completion-probability model. In transport, a symmetric two-ball load can remain jammed unless agitation changes relative contact, even when a single ball flows easily.',
 'Measure full-cycle jam rate, rejection interactions and climb success versus timing, not only best-case speed.')
add('2022-624','Independent rejection avoids disturbing the entire transport path',75,660,
 'An over-bumper vectored collector narrows into a ball-width throat. The retained technical account describes independently driven compliant contacts, a larger lower roller to remove a dead region and a fixed-heading two-position hood launcher.',
 'The source links collector geometry to centering and the independent rejection stage to removing wrong-color cargo without reversing the whole feeder.',
 'Local rejection can preserve a correctly staged ball and reduce recovery time. The narrow throat must still handle simultaneous arrival and worn cargo; a nominal ball-width gap alone does not guarantee reliable singulation.',
 'Test two-ball arrival, wrong-color position permutations and aim/readiness delay at both hood positions.')
add('2022-694','Sensor latency and passive hood compliance are deliberate constraints',80,730,
 'A tall conveyor and rejection fork pause cargo for delayed color sensing. Printed collector contacts and biased flaps address two-ball jams. The retained launcher uses added flywheel inertia and a compliant passive hood; an additional powered back roller was unfinished.',
 'The team explicitly prioritizes simpler scoring after pandemic-related experience gaps.',
 'A deliberate staging pause can improve correct classification even when it lowers nominal feed speed. A passive hood saves actuation but must hold repeatable compression as material wears. Unfinished hardware cannot be credited as an explanation of observed shooting.',
 'Measure classification latency, false rejection, two-ball recovery and trajectory drift as the hood material ages.')
add('2022-987','An intake rebuild and hood change solve different range/flow limits',78,405,
 'After Orange County, a compliant four-bar replaces collector behavior that kicked cargo away. A three-finger popper presents cargo; the retained record distinguishes an early two-position hood from a later adjustable rack.',
 'The team explicitly reports the initial pickup failure and credits a historical in-team popper concept.',
 'A mechanism lineage is useful because it carries operating experience, not because old geometry is automatically optimal. Keep the collector and hood revisions separate; improved range cannot be assigned to the collector alone.',
 'Test moving cargo acquisition and popper timing, then compare hood-range performance at controlled incoming velocity.')
add('2022-1577','Broad pickup and controlled low-spin release require local jam relief',81,695,
 'A broad flat-belt/polycord collector feeds color-based rear rejection and a conveyor. Early edge-vectoring features were removed after simultaneous-ball jams. Adjustable hood arcs and powered back contacts manage release spin; climb sequencing uses contact/current cues.',
 'The retained source ties collector simplification to two-ball reliability rather than minimum part count for its own sake.',
 'A wide acquisition face can deliver multiple pieces into a narrower region, so pair tests are more informative than isolated pickup speed. Current-based climb transition detection needs a threshold robust to friction and battery state.',
 'Test adjacent cargo, wrong-color ordering and climb sensor false positives; do not assume lower spin is always optimal without trajectory data.')
add('2022-1619','An offset path changes both cargo control and partner climb clearance',109,545,
 'Separate front/rear elevator belts oppose to retain cargo and run together to feed an offset fixed-heading launcher. Color/IR staging supports rear rejection. A driver alignment flap helps place the robot for a shared hangar climb.',
 'The source explicitly connects the alignment cue to preventing a climb motor from hitting the hangar wall during a triple climb.',
 'Transport modes must preserve possession while another action waits on readiness. The offset scorer and climb envelope also affect alliance geometry; a theoretically fast independent climb may collide in a three-robot arrangement.',
 'Test retention during belt reversals and verify shared-climb clearance with representative partners, not only an isolated fixture.')
add('2022-1678','Late winglets improve edge acquisition without changing the core scorer',146,185,
 'An unequal four-bar with compliant plates receives later deployable winglets/belts to address edge jams. Sensor-tracked slots and an independent ejector select retained versus wrong-color cargo; the hood lineage credits 2910.',
 'The interview explicitly ties most intake optimization to side-entry jamming and describes winglets stowing inside the starting envelope.',
 'Acquisition width is only useful if edge contacts direct cargo into a controlled state. Adding a winglet changes impact and stow geometry, so its success cannot be inferred from center pickups. Lineage should retain year and implementation differences.',
 'Measure edge pickup/rejection recovery and stow clearance under deformed plates and realistic impacts.')
add('2022-1690','Moving shots require a state model beyond distance alone',81,625,
 'A compliant-link collector feeds horizontal/vertical conveyors and a low-driven turret. The source describes a shot model using distance and chassis velocity components to select hood angle and wheel speed.',
 'The retained construction uses linkage compliance for impact survival; the interview explains compensating radial and tangential motion in the aiming solution.',
 'A distance-only lookup cannot describe the same shot from a stationary robot and one moving sideways. The compensation still depends on measured release behavior and pose latency. A sophisticated model does not excuse uncontrolled incoming cargo state.',
 'Test moving-shot error by direction/speed, camera latency and worn cargo; compare predicted and measured flight time.')
add('2022-1771','Long-lived turret experience does not remove staging and rejection requirements',78,755,
 'A floating broad collector and mecanum centering feed two-stage transport with color sensing and rejection recovery. The turret/launcher family has several historical iterations, including earlier-season examples, with controlled backspin in this version.',
 'The team explicitly describes iteration of a familiar turret family rather than a wholly new 2022 mechanism.',
 'Existing know-how can reduce development risk, but the new game’s piece state, rejection legality and contact path still require testing. A rejected ball may disturb the next staged piece, so recovery is part of useful cycle time.',
 'Test rejection followed immediately by scoring and verify turret range/cable limits with the actual 2022 configuration.')
add('2022-2046','A bounded shooting envelope can be an intentional simplification',80,475,
 'The collector moves from early flap/Velcro contacts through rubber to a later griptape tube. Breakaway members protect the core. A fixed-heading, fixed-elevation launcher uses a powered back roller and accepts a bounded shooting region; the climb uses swing to reach traversal.',
 'The source explicitly reports early contacts repelling cargo and later material experiments. The retained account treats the limited shooting area as an accepted design constraint.',
 'Range is not free capability. A simpler scorer can be effective if its reachable positions, acquisition routes and defended access remain adequate. Offseason material changes must not be back-projected onto Worlds.',
 'Test access to the preferred scoring area under defense and compare collector materials with consistent cargo and approach speed.')
add('2022-2056','Climb-or-shoot is a partner-dependent allocation decision',78,440,
 'A wide collector centers moving cargo and was reinforced after impact damage. A vertical conveyor/color stage feeds a roughly ±175-degree turret with two hood states. The interview reports a roughly ten-to-fifteen-second best climb range.',
 'The team explicitly says reliable traversal partners can make continued shooting the preferable assignment.',
 'The comparison must include travel, capture, retries and available cargo, not only mechanism lift time. This demonstrates marginal task value in 2022 without making any claim that its climb incentive matches 2026.',
 'Measure scored output during the entire climb interval and validate shared-climb reliability before fixing the alliance’s endgame allocation.')
add('2022-2481','Frame and climb objectives can justify an unusual drivetrain',79,520,
 'The source describes an octagonal five-module chassis, asymmetric collector contact for adjacent cargo and a turreted launcher. At the filmed event, alignment for its special climb remains manual; floor-line sensors are planned.',
 'The team links frame length to its truss-climb approach and the fifth module to stability while driving.',
 'An unusual module count cannot be evaluated independently of the task geometry that produced it. Added contact and mass may help stability while increasing power, scrub and service burden. Planned alignment sensors cannot be credited to the filmed result.',
 'Measure traction/current, alignment success and shared-climb clearance with the actual event configuration.')
add('2022-2910','Stored launcher energy and explicit hook confirmation reduce different risks',81,515,
 'The retained account describes a large flywheel/long contact wrap, powered upper contacts, an adjustable hood and a top-driven path over the battery. Climb control confirms both mid-bar hooks before starting the automatic sequence.',
 'The team connects low swerve motor placement to CG and packaging, and explains hook confirmation as preventing a one-hook climb that could break hardware.',
 'A fast automated sequence should begin from a verified mechanical state. Similarly, high flywheel energy helps paired shots only if the feed preserves contact and motor power restores speed between volleys.',
 'Test partial hook capture, full two-ball release and recovery at realistic battery conditions.')
add('2022-4414','Repeated intake iterations must remain attached to the correct shooter snapshot',223,955,
 'The team reports several whole-robot iterations. The retained account distinguishes early pneumatic flex-wheel collection from later motorized rollers, sensor-tracked cargo chambers, a wide-range turret and a high-mounted targeting camera.',
 'The interview emphasizes rapid fabrication/iteration and material testing. More exact performance attribution requires the dated release/configuration, not the number of iterations alone.',
 'A camera mounted to preserve near-goal visibility changes the available aiming envelope. Color/rejection and staged possession must still coordinate with turret direction. Do not combine every photographed intake into one version.',
 'Validate close-range sight lines, rejection trajectory and intake/feed readiness after a mechanism swap.')
add('2022-4499','Collapsible acquisition and lowered transport preserve packaging',79,445,
 'A wide compliant four-bar feeds a lowered second stage and a fixed-heading adjustable-hood launcher. The compact climb replaces an earlier size-constrained concept. A central transport feature remains from a dual-intake idea that was not built.',
 'The team explicitly wants the collector to collapse in wall contact, especially behind the hub where visibility is poor; climb packaging motivated the alternate arrangement.',
 'A visible legacy feature is not proof of a fielded subsystem. Collector compliance must work with the pneumatic state and hard stops, while a lower transport path can alter compression and dead zones.',
 'Test blind-side contact, full-path flow and climb/shooter clearance; retain the unbuilt dual-intake status.')
add('2022-5172','A fast rejected climb is not the same as a useful fielded climb',79,475,
 'A nonparallel four-bar and passive bumper-gap flap feed a ramp and turreted launcher with added brass inertia. The team says a faster two-arm climb had mechanical problems, so it reverted and widened hooks to clear the turret/reduce swing.',
 'The source explicitly prioritizes the revised reliable climb over the failed fast alternative.',
 'Useful timing includes completion probability and physical interference. A turret that scores well can still block the climb’s swept envelope. Continuous wheel idling also has an electrical/thermal cost that should be measured.',
 'Test hook clearance over turret range, climb swing and repeated-volley wheel recovery.')
add('2022-5940','Dual acquisition improves route flexibility without proving every component optimal',109,400,
 'A second opposed collector was added after the single-intake early robot to support drive-by autonomous pickup. The source reports wide mecanum collectors, a controlled upward/passthrough belt path and a later moving-shot solution. The onseason climb differs from an offseason traversal upgrade.',
 'The team explicitly ties dual pickup to easier drive-by autonomous, while cautioning that its mecanum implementation required many iterations and was not a blanket recommendation.',
 'A successful robot can contain a mechanism the team would not copy again. Preserve that negative experience. Additional pickup directions buy route freedom, but require two transport-entry cases and greater repair exposure.',
 'Compare complete auto routes, feed/rejection recovery and the exact onseason climb; do not back-project the offseason improvement.')
add('2022-4911','A six-bar collector and configurable CAD need version-aware interpretation',0,0,
 'The reveal describes a six-bar pickup with knockdown rollers for bouncing cargo, adjustable launcher rails/top roller and traversal climb. The later CAD release explicitly includes a configuration for the original Glacier Peak climb.',
 'The stated roller purpose is controlling bouncing balls and the rail/top-contact purpose includes a broad shooting envelope with reduced unwanted spin. Exact design-choice causation beyond that is not established.',
 'A configurable assembly can preserve genuine history, but the default displayed CAD is not automatically the configuration used at every event. Knockdown and acquisition contacts should be tested together; a roller that stops bounce may also create a pinch.',
 'Inspect both CAD configurations and validate bouncing-entry behavior plus disabled climb retention.',
 'First-party release topics 404720 and 412974; no technical-video rewatch claimed. Reveal text and topic title use differing names, so source naming is preserved rather than silently harmonized.')
