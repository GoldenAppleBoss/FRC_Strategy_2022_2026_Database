# CHARGED UP: the value of a node depends on the rest of the grid

The base chapter supplies the official score values, grid structure and event records. This supplement examines why ranking tasks by their individual point values misses much of the architecture problem. The key state variables are available piece types, remaining node geometry, link completion, partner capability, autonomous occupancy and the time needed to finish together on the charge station.

## Reach is only useful after the robot controls the piece

A cone or cube can arrive in several orientations and from different sources. An arm that reaches all nodes can be less useful than a more constrained mechanism if its pickup or handoff repeatedly loses time. The intake’s tolerance therefore has value beyond the initial acquisition: it can reduce the operator’s alignment burden, make the transfer repeatable and allow the chassis to leave sooner. On the other hand, adding an intermediate handoff can make a compact scorer possible while introducing another failure state.

Compare complete sequences. Does the robot need to turn after collection? Can it raise while translating? Is a cone’s orientation established before the scoring joint moves? Can it recover a dropped piece without restarting the entire sequence? These questions should sit beside nominal reach and cycle time in the database. They explain why two machines that both “do all levels” can have very different match usefulness.

The 2910, 4414, 1323 and 2056 dossiers offer different packages for reach, mass distribution and transfer. Use their primary bundles for the exact mechanism. A telescoping arm changes bending loads and stow geometry; an elevator changes the moving mass and joint sequence; front/back scoring changes approach options but can demand a more complicated end effector. No one noun settles which package is best for a particular team’s manufacturing, controls and practice capacity.

## Links make independent task lists misleading

The same piece at the same tier can have different immediate value depending on neighboring occupancy. A link completion can change the points gained by a final placement, while filling an easy isolated node can leave difficult work for later. That does not mean “always complete links immediately”: the correct policy also depends on travel, partner plans, piece availability and whether a delayed node can be completed safely later.

An agent should retain the grid state and a record of which robots can service which positions. If only one partner can reliably place a particular piece at a remaining upper node, that capability is an alliance bottleneck. Sending that robot to a task every partner can do may reduce total output even when its personal point rate looks higher. Conversely, a third robot with a modest average can become valuable by filling the constrained gap while the others continue fast cycles.

This suggests a better kickoff task table: list a function, the game state where it matters, the partners assumed available, the opportunity cost and the failure consequence. “Place a top cone” is a task. “Complete the last constrained upper node without disturbing existing pieces while partners collect surplus pieces” is a different architectural requirement, even though both may end with a cone on the same target.

## Saturation changes the job again

Once ordinary grid placement is complete, the next useful action can change from reach to repeatable surplus placement. That is a real regime change: adding another high-level capability to an already saturated alliance does not necessarily add output, while faster acquisition or reliable low placement can. The transition should be forecast from the likely event depth rather than assumed from the eventual Einstein final.

The Einstein ledger contains reported examples of filled grids, supercharging and triple balance. Those examples establish that the late-game regime occurred in particular high-level matches. They do not show that every week-3 PCH alliance could use the same policy. A team deciding whether to specialize needs to know how often its partners leave valuable ordinary nodes unfilled. If that happens frequently, specializing solely for the saturated regime can leave the alliance unable to reach it.

The timing of a final ordinary placement can also affect how a live score looks before all conditions are satisfied. RoboReplay discusses delayed score realization and late point bursts in retrospectives. Do not infer intentional deception just from an incomplete node: the robot may have missed, waited for a piece or followed a route that left the node for later. The agent should label the distinction between the visible sequence and a commentator’s explanation of why it happened.

## Autonomous is a shared schedule

The charge station occupies valuable route and timing space. A robot’s high personal autonomous output can reduce alliance output if it obstructs a partner, changes station angle unexpectedly or ends where another routine needs to pass. The useful autonomous package therefore includes its start pose, timing, destination, swept envelope, recovery conditions and final pose. A simple compatible routine can be a better second-pick offering than a larger routine that cannot coexist with the captain’s.

Do not use a successful solo autonomous demonstration as evidence of a reliable alliance package. Test combinations, including an unusually slow partner and a routine that misses its first piece. Those failures alter occupancy and can invalidate a path that works when every robot follows the nominal schedule. The design-level consequence may be another intake side, a narrower stow state or a simpler endpoint, not necessarily a faster drivetrain.

## Balancing requires partners, not just a control loop

Three robots approaching a shared tilting platform create a coupled system. Width, wheelbase, center of mass, bumper contact and entry order change the transient behavior. A robot that balances beautifully alone may still leave too little room or demand a sequence that partners cannot execute. The architecture should include an accessible approach and a way to hold a useful position while another robot joins.

When deciding when to leave scoring, compare the value of another likely cycle with the risk of losing the entire group’s endgame. That risk is not constant: it changes with the remaining pieces, approach congestion, a partner’s control precision and whether a robot can enter from a different side. A team should practice the common joint sequence and the recovery after a poor entry. The agent should retrieve those operational constraints with the mechanism, instead of treating balance as a yes/no checkbox.

## Defense and degraded operation

The reviewed 2023 RoboReplay retrospective follows 1678 adapting after an intake problem and using defense. Its useful lesson is role recovery, not a universal claim that defense dominated CHARGED UP. A broken scorer can retain meaningful alliance value if its drivetrain, geometry and driver practice support another task. A small amount of reliable interference can be preferable to repeated failed scoring attempts, but a defender that cannot reach useful paths or creates penalties may add little.

For a PCH design brief, ask what contribution survives the loss of each major subsystem. Then compare the observed stage benchmarks and likely partner capability. A robot that reliably handles the district’s scarce grid function and joins a triple balance can be strategically better than an ambitious generalist that only demonstrates those tasks independently. At Worlds, the same team may need a compatible autonomous, faster surplus placement or a defensive role to remain valuable. The database should preserve that progression rather than overwrite the earlier objective with the final-season job.
