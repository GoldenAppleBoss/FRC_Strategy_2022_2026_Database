> Current edition 2026-10-27: 141 provisional robot-year studies. Original125 (25/year2022–2026) plus three604 supplements and thirteen curated2018/2019 primary-source studies. Historical expansion adds 52 technical notes, 15 parameter records and 61 credited image references. It is not an EPA-ranked top25-per-year expansion, exhaustive mechanism/version history, new PCH benchmark study or additional video/match audit.

> Owner constraints: no pneumatics; no turrets; no support-only architecture. Historical scope and completed curated 2018/2019 expansion: `docs/1833_ACTUATION_AND_HISTORY_SCOPE.md` from corpus root.

> Owner correction: prioritize independently achievable RP and essential scoring independence. Physical iteration is extremely expensive; use proportionate analytical checks and targeted tests. Read `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` from corpus root.

> Binding 1833 mandate (2026-10-26): design the best primary-contributor robot on the field; never a support-only architecture; no turrets. Favor simple mechanisms with elite optimization. Read docs/1833_DESIGN_DOCTRINE.md and docs/DESIGN_REVIEW_PROTOCOL.md before setting priorities.

> Earlier 604 expansion checkpoint: 128 dossiers = original 125 plus supplemental 2022/2023/2026 604 entries; existing 2024/2025 entries expanded. Original 25/year selections are preserved. Read docs/context/1833-design-workflow.md and data/604_research_audit.jsonl. Visual match audits are no longer required by the user; commentary attribution remains mandatory.

# Start here: FRC architecture research corpus

This file is the reading contract for an agent using this directory. The corpus is a dated research snapshot, not a collection of complete engineering drawings or an autonomous design authority. Preserve the long explanations and their qualifications. Use the small search records to locate the full material, not to replace it.

## First reads

For 2018/2019 read `docs/HISTORICAL_2018_2019_TRANSFER.md` and the historical coverage audit. Query actual historical years; the thirteen entries carry null EPA/ranks rather than fabricated estimates. The later edition supersedes earlier checkpoint counts below.

1. Read `agent/manifest.json` for canonical paths, schema, evidence meanings and current coverage.
2. Identify the exact organizer/game/year first: WCP CADathon and FRC games in the same year are different. Read the **entire** `docs/game_YEAR.md` for the target season. Scoring values alone do not establish strategic priority. Read `docs/AGENT_GUIDE.md` and `docs/TECHNICAL_EVIDENCE_GUIDE.md` before recommending hardware.
3. Read `team1833/design_profile.json`, `docs/1833_DESIGN_DOCTRINE.md`, `docs/DESIGN_REVIEW_PROTOCOL.md` and `docs/1833_OPTIMIZATION_REFERENCES.md`. Aim for elite primary contribution under the no-support/no-turret constraints. Establish event stage, partners, resources, development time and maintenance capacity without lowering the objective to a third-robot niche. Historical match assignments and robot capability remain distinct.
4. **Required task-sheet deliverable:** read `docs/TASK_LIST_PROTOCOL.md` and fill a fresh `team1833/1833_Task_List_Template.xlsx` for every new game/manual analysis, material rules revision or new/revised robot design brief. Produce exactly one worksheet; no group tabs. Use `team1833/task_template_schema.json` for machine-readable fields. Complete functional priorities before final architecture recommendations. Never invent 1833 human decisions.
5. Search with `python scripts/query_agent.py search ... --year YEAR`, then load `python scripts/query_agent.py packet YEAR-TEAM` for each serious candidate. Read all sibling fields of a technical note, especially its limits. The packet contains the full explanations, publication version groups, selected parameters, images and discovery audit.
6. Open the image files using an image-capable tool when a recommendation depends on geometry. Text-only ingestion of an image caption does not mean the agent saw the mechanism. All image `path` fields are relative to the **corpus root**, even inside a nested packet. The reader also embeds the bytes and can be opened on its own.

## Facts that must travel with an answer

- Reference **year, team and publication/version label**. Never silently merge 2910's original 2026 four-bars with its rebuild slapdown. Publication groups are not certified event/date intervals; null dates mean unknown.
- Keep published construction, team-stated reason or boundary, analyst inference, proposed validation and limitations separate. A reason field may explicitly report that the team's reason is unknown. An engineering explanation is not evidence of the team's intent.
- Keep source/page links, parameter notation, fuel/piece condition, timing, accuracy and battery assumptions when available. Do not turn a published peak rate into a sustained match average. The selected parameter strings are not complete CAD specifications.
- A photograph or extracted crop establishes only what its scope and source allow. Hidden geometry, exact dimensions and event installation need other evidence. An editorial component label is a retrieval aid, not a publisher certification.
- A source-post locator, CAD discovery link or search result is **not a reviewed source**. A missing binder is **not an absent mechanism**. All141 dossiers remain provisional; 2018/2019 scope is in data/historical_2018_2019_audit.json. Zero have exhaustive version certification.
- EPA is a model estimate, not an observed individual scoring ledger. Alliance scores and alliance medians are not per-robot design targets. Do not infer match strategy from scores alone. None of the 80 Einstein rows has a completed visual audit.
- RoboReplay coverage is 35 available full-caption reviews among the prior 44-video inventory. All eleven previously pending exports were recovered; nine still await full review. Full channel enumeration is unverified. No visual watching is claimed.

## Strategic corrections to preserve

For 2026, retrieve the tower-only evidence before discussing endgame. Fuel scoring continues in an endgame period; “endgame EPA” is not “climb EPA.” The reviewed PCH/Worlds sample supports a fuel-first default and very low climb priority. It does not constitute a census of every match or a universal rule that no hypothetical climb could ever be useful.

For 2025, do not reduce task priority to coral height or assume L1 begins only after branch saturation. The elite-alliance example uses 1323 on L1/algae in parallel with 2910 and 4272 filling branches, followed by additional L1 help. Separate the user's observed role account, primary team mechanism reasoning, official scores and any unreviewed match timing. “Best robot” is an opinion that depends on the role and metric.

## Produce a design recommendation, not a collection of famous names

Give the intended role and measurable outcome first. Describe at least two coherent architectures under the same game, partner and resource assumptions. For each borrowed mechanism identify its function, exact reference, source-backed construction, stated rationale, your causal hypothesis and the conditions that would invalidate the transfer. Evaluate acquisition → storage → transfer → release as a coupled system, including chassis motion, electrical load, loaded CG, service access and recovery after jams or impacts.

State what remains unknown and propose the smallest test that could change the choice. Never present a proposed test as performed. If evidence is insufficient to recommend exact geometry, recommend the function and test instead of inventing a dimension. `agent/evaluation_cases.jsonl` provides questions and expected distinctions for checking an agent's behavior; it is not a claim of measured model accuracy.

## Reproducibility and maintenance

`scripts/build_agent_and_reader.py` rebuilds the embedded-image reader and agent exports from the included JSONL, Markdown and original images. `scripts/query_agent.py` runs locally with the Python standard library. `scripts/rebuild_database.py` independently rebuilds the original normalized research database from `schema.sql` and `tables/`. The agent search database is a derived lexical index, not an additional scientific source. The current edition adds focused technical studies and selected-passage video enrichment; exact scope is below.


## Integrated research pass and video studies

The prior 64-study checkpoint is now merged with 34 additional studies: all 98 previously uncovered robot-years have focused technical studies integrated into the reader, SQL exports and agent packets. The corpus has 227 technical notes across all 125 robot-years. Keep the distinction: only 27 robot-years have the earlier reviewed technical-publication coverage; the other 98 are focused interview/source-bundle studies, not newly discovered binders, CAD certifications or exhaustive version histories.

The current checkpoint recovers all eleven previously pending transcripts through the normal YouTube transcript interface. No CAPTCHA appeared in this session. The 44-video ledger now has 35 complete available-caption reviews: 33 inherited reviews with selected-passage enrichment, plus two new complete caption reads. Those two studies add 27 sections and about 6,900 written words covering six 2026 Einstein matches. Nine recovered transcripts still await full content review. Across all 35 studies there are 132 sections and 114 quiz prompts. Full channel enumeration remains unverified. Tested match players stayed black and buffering, so zero visual Einstein audits are complete. Read `docs/EINSTEIN_VISUAL_AUDIT.md` and `data/einstein_visual_audit.jsonl` before using a match account as observation.

Read `docs/roboreplay/README.md`, `data/roboreplay_review_ledger.jsonl`, `data/video_access_audit.json` and `data/roboreplay_quiz_prompts.jsonl`. Original raw captions are not redistributed. Use `python scripts/query_agent.py search algae --year 2025 --kind video_analysis` and expand to the complete written study before answering. A quiz failure should become an identified evidence gap, not an invented answer.
