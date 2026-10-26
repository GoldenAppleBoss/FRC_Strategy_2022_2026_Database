> Start at `AGENTS.md` and `agent/manifest.json`. Use `scripts/query_agent.py` for literal search, then load the full packet under `agent/robot_packets/` and the entire game chapter. The new typed claim records separate source paraphrase, team reasoning/boundary, analyst inference and unperformed validation. Image paths in JSON are relative to the corpus root.

# Using this corpus for robot architecture decisions

This is a retrieval corpus and an auditable research edition, not a model trained to recognize every FRC robot from an image. Its 125 robot entries contain substantial primary-source summaries, but unresolved subsystem details and unverified intermediate versions remain. Treat those as unknowns; never fill them with a famous team's usual practice. There are 80 Einstein records, of which 54 have reviewed reported tactics; none has a completed visual audit. Score-only records must not be narrated as observed match strategy.

## Retrieval order

1. Load the dated game rules and field geometry. Extract legal actions, possession, timing, finite resources, access constraints and scoring dependencies.
2. Define the role and event stage: PCH week 3, week 5, DCMP, division contender, or Einstein alliance. Include two hypothetical partners.
3. Estimate the bottleneck in a complete match: acquisition, transport, handoff, alignment, release, recovery, energy, supply or lane occupancy.
4. Retrieve mechanisms by function and failure mode, then by team/year/version. A team number without a year is an ambiguous reference.
5. Compare at least two coherent whole-robot architectures. Use the same match assumptions for both.
6. Return a source-backed recommendation, confidence, unresolved interfaces, and the smallest tests that could falsify it.

Use SQLite for structured filtering and full-text retrieval; use the Markdown chapters and source links for context. Embeddings can supplement this, but should not replace exact year, version, event and metric filters. The JSONL exports make provider-neutral ingestion straightforward. No model API credentials or paid service are required to browse the delivered database.

## Mechanism vocabulary and interface contracts

Store four separate ideas: **function** (acquire fuel), **kinematics** (four-bar, pivoting/slapdown, translating rack), **implementation** (materials, rollers, transmission), and **observed performance** (conditions and date). Treat labels as retrieval hints and inspect actual linkage geometry. For 2910 specifically, the 2026 original and rebuild briefs explicitly distinguish dual four-bars from the later slapdown; do not blend versions.

“Dumper” in the reviewed 2026 sources usually refers to multi-stream/batch shooting through a broad fixed-heading drum. It does not imply a literal gravity dump, a fixed hood, absence of aiming software, or a particular lane count. “Four-wide” should specify usable stream width, not merely the number of visible wheels. DYE Rotor is paintball-loader lineage; a rotating-cone spindexer is a related but different singulation family.

For every proposed combination, explicitly check:

- Intake → hopper: deployed/stowed envelopes, full-load capacity, collision collapse and whether a deformed wall can block retraction.
- Hopper → feeder: floor support, packing pressure, dead zones, bridging, agitation, retained residual pieces and service access.
- Feeder → launcher: compression, incoming velocity/spin, lane width, time of flight, rate distribution and current draw.
- Scorer → chassis: aiming motion, swept volume, cable limits, reaction loads, CG throughout travel, and accessible routes while loaded.
- Climber → everything: capture alignment, partner clearance, removed scoring time, held state after disable, mass margin and actual installed version.

## Required evidence language

Use **official score**, **team-reported measurement**, **broadcast report**, **analyst inference**, **proposed/unfielded**, and **unresolved** as distinct labels. A reported BPS number without fuel condition, accuracy, duration and battery state is not a portable design specification. An automatic score decomposition does not establish defensive effectiveness or individual contribution. A part visible in CAD is not proof it was installed at every event.

EPA is a model estimate of contribution, not an individual scoring ledger. Some component estimates are negative or outside physical probability bounds. Do not convert such outputs to observed ball counts, success rates or hardware absence. Do not add three season-final EPAs to claim the score an alliance will produce in a specific match. Partner interference, defense, rule versions and timing can invalidate that approximation.

The numeric snapshot uses the user-supplied Statbotics mirror consistently, retrieved 2026-10-25. It is not asserted to be bit-identical to every official Statbotics historical model revision. Pre-elimination event EPA is supplied for historical event comparison; it is still an estimate, not a prediction made before kickoff.

## Output format for the eventual agent

Start with a robot role and measurable goals. Then give an architecture sentence with **year and version** on each inspiration. Explain what function each reference solves and why the components fit together. Include two rejected alternatives and the conditions under which either would become preferable. State development burden, maintenance requirements and the next decision-changing prototype.

Example query: “Find 2026 batch scorers with expanding storage, compare a 2910 rebuild intake/hopper arrangement to 1678 and a 254-style preaccelerated drum. Explain which motion/linkage details must be rechecked.” A correct answer retrieves those particular dossiers, distinguishes their interview dates, and declines to invent a universal combination from their labels.

## Evaluation cases

- Ask for 5940's 2022 Worlds climb. The answer must distinguish onseason high-bar from offseason traversal.
- Ask whether 4414 held 110 fuel in 2026. The answer must identify the published 85+/100+ configuration claims and leave 110 unverified.
- Ask which 2026 Einstein finalist had 150 climb points. The answer must reject interpreting endgame fuel as tower points.
- Ask for 2025 week-1 coral-RP requirements. The answer must find the early rule version rather than blindly use the latest manual.
- Ask for the strategy of a score-only Einstein row. The answer must expose the pending tactical review, not invent a defender.
- Ask why 1690's 2025 alliance used a station-fed third robot. The answer must discuss partner interference and preserve attribution to the team account.
- Ask for the best 2022 architecture solely from EPA. The answer must explain outcome-selection and documentation bias, then ask which role/resources the architecture must serve.

Hold back some known robot-year questions when evaluating a retrieval agent. Score source correctness, version correctness, unknown handling, interface reasoning and recommendation quality separately. Fluent use of team numbers is not evidence of sound strategic design.


## Technical review edition

Read `data/binder_audit.jsonl` for all 125 search statuses, `data/binder_sources.jsonl` for reviewed publications, and `data/technical_mechanisms.jsonl` for construction, stated intent, inference, proposed tests and limits. Use `data/technical_parameters.jsonl` for selected published values and source notation. `docs/TECHNICAL_EVIDENCE_GUIDE.md` explains the reasoning standard. A first-pass search is not exhaustive absence evidence.

For 2026, begin with fuel contribution and treat climbing as low priority; use actual tower fields rather than endgame EPA. For 2025, retrieve the 1323/2910/4272 parallel L1-algae/branch case before ranking tasks by height.


## Integrated research pass and video studies

The prior 64-study checkpoint is now merged with 34 additional studies: all 98 previously uncovered robot-years have focused technical studies integrated into the reader, SQL exports and agent packets. The corpus has 227 technical notes across all 125 robot-years. Keep the distinction: only 27 robot-years have the earlier reviewed technical-publication coverage; the other 98 are focused interview/source-bundle studies, not newly discovered binders, CAD certifications or exhaustive version histories.

The current checkpoint recovers all eleven previously pending transcripts through the normal YouTube transcript interface. No CAPTCHA appeared in this session. The 44-video ledger now has 35 complete available-caption reviews: 33 inherited reviews with selected-passage enrichment, plus two new complete caption reads. Those two studies add 27 sections and about 6,900 written words covering six 2026 Einstein matches. Nine recovered transcripts still await full content review. Across all 35 studies there are 132 sections and 114 quiz prompts. Full channel enumeration remains unverified. Tested match players stayed black and buffering, so zero visual Einstein audits are complete. Read `docs/EINSTEIN_VISUAL_AUDIT.md` and `data/einstein_visual_audit.jsonl` before using a match account as observation.

Read `docs/roboreplay/README.md`, `data/roboreplay_review_ledger.jsonl`, `data/video_access_audit.json` and `data/roboreplay_quiz_prompts.jsonl`. Original raw captions are not redistributed. Use `python scripts/query_agent.py search algae --year 2025 --kind video_analysis` and expand to the complete written study before answering. A quiz failure should become an identified evidence gap, not an invented answer.


## Required 1833 task sheet

For each new game/manual analysis, material rules revision or new/revised robot design brief, fill a fresh copy of [the one-sheet template](../team1833/1833_Task_List_Template.xlsx). Follow `docs/TASK_LIST_PROTOCOL.md` and `team1833/task_template_schema.json`, with all paths resolved from the corpus root. The template includes task outcome, phase, points/enabling value, priority, difficulty, recommendation, rationale, alliance dependencies, acceptance target, exact rule/source, uncertainty/test and separate human decision. No group tabs; no inherited season-specific decisions. Four previously blocked 604 image originals are now recovered and embedded (2023 robot; 2026 serializer, intake and hopper).
