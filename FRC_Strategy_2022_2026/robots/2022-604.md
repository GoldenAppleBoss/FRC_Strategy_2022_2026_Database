# 2022-604 — Quixilver: Octopus Prime

Primary source: https://github.com/frc604/2022-public

Reviewed 2026-10-26. This is a source-bounded technical study. Construction, stated intent, interpretation and unresolved evidence are separate.

Code commit: 2cfd645d19ac09681d201481e8eecd10156b2b9d. Read the original FRC-2022 tree. FRC-2022-NEW is a learning rewrite, not certified event code. File locators: Intake.java, BallPath.java, Launcher.java, Climber.java and Calibration.java under FRC-2022/src/com/_604robotics/robot2022/.

## Published FRC-2022 code · drivetrain

### Published construction or code

Calibration defines a 20.5-inch wheelbase and track width, 3.94-inch wheel diameter, 6.75:1 drive reduction and 12.8:1 steering reduction. These are software configuration values, not independent measurements.

### Stated rationale and boundaries

Mechanical selection rationale is not established by the code.

### Engineering interpretation

The swerve and localization must be considered together. A configured maximum speed is not a demonstrated match speed. Wheel calibration affects both the path tracker and the launch-distance estimate, so a copied drive configuration can corrupt scoring even when teleop feels acceptable. Check hardware revision, encoder scales and actual loaded wheel circumference before borrowing constants.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Published FRC-2022 code · intake

### Published construction or code

Intake.java configures distinct Falcon 500 roller and deployment motors, a trapezoidal deployment profile, arm feedforward and a 45A deployment stator limit. Intake, eject, unjam and yeet commands are separate entry points.

### Stated rationale and boundaries

The code does not state why this exact mechanical geometry was selected.

### Engineering interpretation

The published interface treats recovery and reverse flow as designed operating modes. That is useful architectural evidence, but it does not establish roller material, width, compression or impact survival. A profiled pivot can reduce abrupt actuation; whether it does so under contact depends on the real mechanism and controller settings. Preserve these unknowns rather than infer a later 604 polycarbonate intake in 2022.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Published FRC-2022 code · transfer

### Published construction or code

BallPath.java separates upper and lower Falcon-driven transport sections and exposes position/velocity control and sensor-based ball handling.

### Stated rationale and boundaries

Exact transport geometry and team selection rationale remain unresolved.

### Engineering interpretation

Separately controlled transport can stage a second cargo while releasing the first, but introduces coordination between occupancy sensing, launcher readiness and reverse recovery. Code supports the existence of these interfaces, not an independent throughput result or proof of jam-free behavior. A two-cargo game rewards preserving a reliable staged sequence; extra transport complexity should be justified by actual scoring continuity.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Published FRC-2022 code · scoring

### Published construction or code

Launcher.java configures front and rear Falcon flywheel motors with feedforward and feedback. Readiness checks use a five-sample speed buffer and tolerance; distance-related bounds are treated separately.

### Stated rationale and boundaries

The source establishes readiness logic, not a published mechanical reason for wheel geometry.

### Engineering interpretation

Requiring recent samples within tolerance is different from checking one instantaneous RPM. It can reject a momentary speed crossing after spin-up or a previous shot. The trade is delayed release versus launch consistency. The existence of front/rear motors does not establish independent spin control in competition, wheel dimensions, a turret, or exact release angle. Those require geometry and event evidence.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Published FRC-2022 code · endgame

### Published construction or code

Climber.java configures three NEO motors and staged first-rung, lift, handoff, high-rung and traversal transitions. It uses filtered tilt and tilt rate, position/profile completion and an angle-history lockout.

### Stated rationale and boundaries

Comments explicitly describe gyro-controlled transitions and an antenna-touch-angle lockout; broader hardware intent is not fully documented here.

### Engineering interpretation

This is a dynamic climb sequence, not a simple winch toggle. A transition may require both operator approval and a suitable swing/position state. That ties compliance, sensor filtering, angular thresholds and operator timing together. A traversal state in released code proves intended capability, not a successful traversal in every match or that all events ran this revision. Exact hook and support geometry remain open.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Original code versus learning rewrite · controls

### Published construction or code

The repository README identifies FRC-2022 as robot code and FRC-2022-NEW as a work-in-progress reimplementation for learning and cleanup. Quikplan-swerve and the offboard quixpf particle filter are separate directories.

### Stated rationale and boundaries

The rewrite is explicitly described as preparation and learning.

### Engineering interpretation

Do not read the cleaner NEW tree and retroactively claim every behavior was fielded in 2022. The original tree is the stronger starting point for event-era behavior, though its final commit still lacks per-event installation certification. Pin the repository commit and file path when citing code; preserve the distinction between software configuration, mechanical construction and observed performance.

### Validation still required

Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.

## Evidence limits

- Selected primary publications/code reviewed; exact per-event installation and exhaustive intermediate revisions remain unresolved.
- Four previously blocked source originals (2023 robot photo; 2026 serializer, intake and hopper CAD views) were recovered through normal browser downloads on 2026-10-26 and inspected. Whole-robot source views are not exhaustive mechanism or event-version certification.
