# 2023-6328: What an articulated arm and a handoff actually cost

Version: February controls write-up, May wiring report and pinned repository snapshot; event binary unverified

## Evidence premises

- **team_controls_paraphrase**: Shoulder, elbow and wrist provide multiple positioning coordinates. Team describes coupled dynamics, optimized collision-constrained paths and intake avoidance. Locator: https://www.chiefdelphi.com/t/frc-6328-mechanical-advantage-2023-build-thread/420691/58
- **pinned_code_inspection**: IntakeCubeHandoff runs intake and gripper while moving the arm to CUBE_HANDOFF, then requests HOMED on termination. This verifies coordination logic, not successful physical transfer. Locator: https://github.com/Mechanical-Advantage/RobotCode2023/blob/1759ecc7ab5d76fcca157d8b76ead233ecb1454f/src/main/java/org/littletonrobotics/frc2023/commands/IntakeCubeHandoff.java
- **team_service_paraphrase**: Team moved wiring outside the arm to ease tube replacement, accepting exposure with protective wrapping; it reports a short repair list despite electrical complexity. Locator: https://www.chiefdelphi.com/t/frc-6328-mechanical-advantage-2023-build-thread/420691/209

## Piece flow

For the inspected cube-handoff command: ground cube → dedicated cube intake → overlap with gripper at an arm handoff pose → arm-carried cube → scoring release. The command coordinates intake, arm and gripper; it does not by itself prove compression, transfer sensor coverage, success rate or the full cone route.

## Physical arrangement and swept space

The arm base must carry shoulder reactions; the elbow and wrist sweep through a large changing workspace. The separate intake consumes a ground-access region that can conflict with the arm trajectory. Wiring must survive joint motion and remain replaceable. Exact package coordinates, loaded inertias, pickup mouth width and battery removal route are not established by this selected review.

## Independent motions and powered functions

Shoulder, elbow and wrist are three positioning coordinates. The cube intake and gripper add powered functions; their deployment and transport must be audited before giving a whole-robot DOF or motor total. High moment of inertia is an owner concern; actual loaded inertia is not measured here.

## Burdens avoided

An articulated arm can reach multiple positions without forcing the chassis to follow one fixed mast line. A dedicated collector can decouple a generous ground-capture mouth from the smaller placing hand. These are potential advantages that a fixed-lift alternative must explicitly match.

## Burdens retained

Multiple joint states require calibration, safe transit paths, dynamic control and recovery from interrupted motion. A handoff adds possession transfer, support and timing requirements. The wiring tradeoff shows service access and impact protection can conflict. More complexity is not proof of poor reliability; retain the team repair report as counterevidence.

## Engineering hypothesis

An arm is worthwhile when its workspace and acquisition advantages save more complete-cycle time or failures than its coordination costs create. For a team whose required poses fit a fixed mast, that flexibility may be unnecessary expense. Compare reachable task sets before comparing mechanism prestige.

## Rival explanation

Better control software can make extra coordinates fast and consistent, and a well-developed handoff may outperform direct narrow-mouth pickup. Alliance outcomes cannot isolate architecture from execution or partners.

## When the preference reverses

Prefer articulation if the fixed mast cannot legally reach essential poses, requires slow repositioning, or loses acquisition reliability. Prefer the fixed lift when it meets the same task envelope and measured cycle targets with lower development/service burden.

## Unknowns

Actual inertia, comparable complete-cycle distributions, full cone route, failure recovery behavior, exact event-installed code and final mechanical configuration. Code execution was not simulated or hardware tested.

## Proposed check; not performed

Map identical task poses, legal extensions and intake clearances. Estimate masses and arm inertias from real geometry instead of adjectives. Compare acquisition, handoff and scoring times separately, then combine them with failures; inspect interruption recovery in code before any physical trial.

## Outcome evidence

No controlled architecture comparison or individual cycle-time measurement performed.

## Sources

- https://www.chiefdelphi.com/t/frc-6328-mechanical-advantage-2023-build-thread/420691/58
- https://www.chiefdelphi.com/t/frc-6328-mechanical-advantage-2023-build-thread/420691/209
- https://github.com/Mechanical-Advantage/RobotCode2023/blob/1759ecc7ab5d76fcca157d8b76ead233ecb1454f/src/main/java/org/littletonrobotics/frc2023/commands/IntakeCubeHandoff.java
