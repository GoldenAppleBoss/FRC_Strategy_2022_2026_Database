# 2026-2910: Compare paths and iteration costs, not intake names

Version: BLITZ original versus RE-BLITZ rebuild; inherited physical studies

## Evidence premises

- **inherited_source_bounded_study**: Two collectors approach the chassis from opposite sides. They feed a constrained serpentine path and a fixed-yaw launcher rather than a deep open bulk hopper. The launcher structure occupies one end of the base, while the four-bar links occupy side deployment space. The binder base image shows four corner drive modules and a lightened pan. Electronics under the pan require turning the robot over and removing its protective belly sheet according to the team release; do not draw those electronics as accessible through the ball path. Battery removal direction is not established. A fixed launcher can aim with the chassis while the side collectors sweep laterally, but that is a control and route advantage, not unrestricted acquisition in every heading. Locator: data/physical_studies.jsonl#physical-2026-2910-original
- **inherited_source_bounded_study**: The rebuild uses a single front slapdown collector, an expanding storage enclosure over an inclined roller floor, and a full-width raised shooter at the opposite end. Corner swerve modules sit below this path; the launcher side structure carries the drum and hood and attaches down toward the drive rails. Source dimensions give a 27.5 by 27-inch frame. The hopper panels and their joints surround the ball path, so screw heads on the hood can rub a sliding wall. A source reply specifically explains using flathead screws there. Some electronics moved above the brainpan, but under-pan equipment still needs underside access. Preserve that service split. Do not infer battery removal without its source view. Locator: data/physical_studies.jsonl#physical-2026-2910-rebuild

## Piece flow

Original: two collectors → constrained serpentine transport → fixed launcher. Rebuild: slapdown acquisition → bulk hopper/roller-floor path → launcher. Read both full physical studies; the original inlet merge and several rebuilt interfaces remain unknown.

## Physical arrangement and swept space

The original places deployment links beside a constrained transport path. The rebuild allocates inventory volume and an active floor beneath it. Mouth deployment, stored inventory, launcher support and electronics access must be evaluated as one package; a compact intake alone says little about sustained feed.

## Independent motions and powered functions

Count collector deployment coordinates separately from roller motors, floor drive and hood motion. Two collectors do not automatically double throughput, and a single slapdown does not make the hopper feed problem disappear.

## Burdens avoided

A less constrained bulk path can avoid repeated direction changes and dedicated conveyor transitions, if pieces can still reach the feeder consistently. Fewer deployment linkages may simplify impact recovery and replacement.

## Burdens retained

Bulk inventory introduces bridging, starvation, compression and center-of-mass effects. An active floor adds contact and power demands. Rebuild development time is itself a cost; no numerical time saving or causal season improvement is established by the reviewed construction.

## Engineering hypothesis

Evaluate pickup rate, usable stored capacity and sustained release together. A simple mechanism that starves the launcher cannot meet an elite throughput target. Conversely, a more elaborate collector that feeds no faster may spend space and iteration budget without useful benefit.

## Rival explanation

The apparent improvement may depend on launcher changes, code, field strategy or testing maturity, rather than collector topology alone. Treat the before/after history as a source of hypotheses, not a controlled experiment.

## When the preference reverses

A constrained path may win when orientation/order matters or bulk feed is unreliable. A bulk path may win when high inventory and simultaneous feed dominate. Select using the new game piece and geometry, not the historical team name.

## Unknowns

Common-condition rates, exact interface geometry, actual jam frequency and isolated effects of each redesign. Do not infer hidden plumbing or installed pairings from different binder snapshots.

## Proposed check; not performed

Before replacing an architecture, calculate capacity, clearances and bottleneck rates. Test the single most uncertain transfer or hopper-floor section only if its outcome can change the decision.

## Outcome evidence

No controlled architecture comparison or individual cycle-time measurement performed.

## Sources

- https://drive.google.com/file/d/1jPf-aOGhz0dntoAgahFBgRhJiJv9rGpj/view?usp=sharing
- https://drive.google.com/file/d/1r-6zR4afbr_BpeZfWwcM5XL1N74FjScI/view?usp=sharing
- https://www.chiefdelphi.com/t/2910-cad-and-tech-binder-release-2026/521705
- https://www.chiefdelphi.com/t/2910-cad-and-tech-binder-release-2026/521705?page=2
