# 2023-4414: Low service burden can require careful construction

Version: Tsunami interview plus June 29 elevator construction write-up; not one certified event configuration

## Evidence premises

- **team_construction_paraphrase**: Team packages motors inline with the mast base, uses a continuous belt with few redirects and bearing-supported idlers, and adds constant-force return springs. Locator: https://www.chiefdelphi.com/t/team-4414-hightide-2023-robot-tsunami/428584?page=8#post_155
- **team_report_not_independent_test**: Team explicitly describes precision-intensive upfront assembly and reports essentially no maintenance after completion. Locator: https://www.chiefdelphi.com/t/team-4414-hightide-2023-robot-tsunami/428584?page=8#post_155
- **retained_interview_study**: Existing source study records a shared claw, later wide cube collector, elevator and virtual four-bar, plus automated alignment. Locator: Technical note study6-2023-4414

## Piece flow

Shared-claw path: piece enters the claw and stays with it for placement. Later cube-collector path: cube enters wide collector → crosses an additional transfer through the elevator opening → reaches the scoring claw. Keep those paths distinct; the later robot is not a universal zero-handoff example.

## Physical arrangement and swept space

Elevator rails and moving stages establish the lift corridor; the end-effector linkage occupies additional swept space near the carriage. The through-opening used by the later cube path is a functional packaging feature. Inline base drive placement preserves mast overlap/travel. Belt redirects, tensioning access and return assistance must fit within the same package. Exact battery extraction and collector-to-claw contact geometry remain unresolved.

## Independent motions and powered functions

Lift extension plus end-effector linkage position are distinct functional coordinates; additional acquisition deployment may belong to the later collector. Link count and virtual-link geometry do not establish the number of independent axes. The drivetrain and automation are part of the complete system cost.

## Burdens avoided

Compact rigging can avoid consuming mast travel with bulky base gearing. Careful belt routing can avoid friction that would otherwise demand repeated adjustment. The original shared-claw path avoids a handoff; the later path deliberately spends complexity on acquisition.

## Burdens retained

Belt stiffness, alignment, bearing wear, tension setting, return consistency and precise assembly remain burdens. The team report separates low operating maintenance from manufacturing simplicity. Twelve-motor swerve and advanced alignment controls in the retained source study prevent using Tsunami as proof that every subsystem was minimal.

## Engineering hypothesis

Spend fabrication effort where it produces repeatable motion and reduces event service, while evaluating the full robot on acquisition and scoring. A later wide collector is justified only by a complete-cycle benefit that outweighs its transfer and space costs.

## Rival explanation

The maintenance report may reflect excellent execution, spares or operating conditions rather than a universally forgiving transmission. Fast placement may depend heavily on drivetrain control and driver workflow.

## When the preference reverses

A simpler rigging method may be better if assembly capability, belt quality or alignment control cannot reproduce this construction. A wide collector can be worse if transfer jams dominate the time it saves at acquisition.

## Unknowns

Measured service hours, comparable elevator failure rates, exact collector handoff and verified installation chronology. No CAD release was reviewed. Do not copy nonstandard pulley bend radii from informal feel tests as validated practice.

## Proposed check; not performed

Use a full-stroke clearance and return-force calculation first. If rigging choice remains consequential, test one representative loaded stage path and return consistency, including tolerances and service access; measure complete pickup cycles before adding a collector.

## Outcome evidence

No controlled architecture comparison or individual cycle-time measurement performed.

## Sources

- https://www.chiefdelphi.com/t/team-4414-hightide-2023-robot-tsunami/428584?page=8
- https://youtu.be/URZEkOANGHQ
