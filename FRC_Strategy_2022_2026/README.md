> Current 604 expansion: 128 dossiers = original 125 plus supplemental 2022/2023/2026 604 entries; existing 2024/2025 entries expanded. Original 25/year selections are preserved. Read docs/context/1833-design-workflow.md and data/604_research_audit.jsonl. Visual match audits are no longer required by the user; commentary attribution remains mandatory.

# FRC Strategy Research Database · 2022–2026

Open **index.html** in a browser. Text, data and all 508 images are embedded. The reader works even when index.html is moved on its own. The original images/ folder remains for agent tools and Markdown documents. No server or account is required. Primary source links require internet access.

This research edition contains **125 robot-year reference dossiers (25/year), five game/meta chapters, 58 event benchmarks and all 80 Einstein match records**. It also includes 7,995 completed match rows and the full five-year EPA ranking snapshot. **Important: these are provisional dossiers, not 125 certified exhaustive histories.** Unresolved subsystems and intermediate versions are marked. Fifty-four Einstein records have reviewed reported tactics; none has a completed visual audit. The user's strict exhaustive acceptance gate remains open.

The supplied Statbotics mirror made all five ranking years available. Rankings use its total-points EPA snapshot dated 2026-10-25, with original rank preserved when a lower-ranked documented robot was substituted. Read `data/selection_audit.csv` and `docs/METHODOLOGY.md` before treating the sample as a top-25 census or the mechanism descriptions as complete CAD specifications.

## Files

- `index.html` — searchable offline reader: robots, game chapters, PCH/Worlds benchmarks, Einstein ledger, source library and coverage audit.
- `frc_strategy.sqlite` — normalized SQL database, JSON score components and FTS5 robot search.
- `data/robot_dossiers.jsonl` — nested agent-friendly robot records; `robot_index.csv` for a flat index.
- `robots/` — one readable Markdown dossier per robot-year.
- `docs/game_2022.md` through `game_2026.md` — functional game models, evolution, tradeoffs and mechanism inspiration.
- `docs/BENCHMARKS.md` — PCH week 3/week 5/DCMP and Worlds comparison tables.
- `data/benchmarks.csv`, `einstein.csv`, `coverage_audit.csv`, `selection_audit.csv`, `epa_rankings_2022_2026.csv` — inspection/export files.
- `docs/AGENT_GUIDE.md` — retrieval workflow, mechanism interfaces, uncertainty handling and evaluation cases.
- `schema.sql`, `example_queries.sql`, `tables/`, `scripts/rebuild_database.py` — reproducible database rebuild from included exports.
- `data/audit.json`, `VALIDATION.json`, `SHA256SUMS.txt` — scope, data validation and file integrity.

## Start with three checks

Search `2026 4414` and compare the documented 85+/100+ capacity claims with the unverified 110 claim. Search `2022 5940` to see why the onseason and offseason climbs differ. Open 2026 Einstein final 3 to see why large endgame points must not be called climb points.

The purpose is useful, falsifiable architecture reasoning. A team/year/version identifies a source-supported package; a high EPA does not make every one of its mechanisms optimal for your team. Unknowns stay unknown, reported measurements keep their conditions and analyst interpretation is labeled separately.

## Rebuild

Run `python scripts/rebuild_database.py` from this directory (Python standard library with SQLite FTS5). To avoid replacing the included database, pass a different output path as the first argument. The script reads only the included schema and exact table exports. It does not re-download sources or refresh the EPA snapshot.

## Expanded context edition

Added 14,264 words across 12 contextual documents, including five longer game supplements, three robot-specific deep notes, architecture reasoning and a durable agent context entry point. Added 258 curated technical images across 70 robot-years, 3,499 dated post locators and 375 CAD/code/shared-document discovery links. Discovery links are not content-review certifications.

RoboReplay: **35 full available transcript reviews** among the prior 44-video inventory; all eleven previously pending transcripts recovered, nine of those awaiting full content review. **The entire channel inventory is unverified, and no visual watching is claimed.** The included review ledger records source summaries, conditional interpretation and timestamp navigation. Full captions and entire forum discussions are not redistributed.

Start a new agent session with `docs/context/AGENT_CONTEXT.md`, then retrieve the long game chapters and source-specific records. This is saved project context, not a claim of permanent internal model memory. The original 125 dossiers remain provisional; these additions do not close the exhaustive mechanism/version or all-match visual-review gates.

New SQL tables: `context_documents`, `mechanism_images`, `source_posts`, `cad_code_links`, `video_reviews`, and `context_search`. Nested data exports retain the richer metadata. The reader adds Context and RoboReplay views.


## Technical binder and corrected game-model edition

Added 129 technical mechanism/architecture notes across 27 robot-years, based on 26 PDF technical publications, two web binders and first-party technical replies. One PDF is a one-page technical sheet; original/rebuild briefs remain separate publications. Added 246 credited figures and 121 selected parameter records. All 125 received an initial discovery search; 101 unresolved entries received a second search-engine pass. The audit distinguishes reviewed sources, inaccessible candidates and unresolved discovery. This is not a claim that all 125 binders or all competition versions have been found.

The 2026 chapter now makes fuel contribution primary and climb a low-priority exception, with tower-only event evidence. The 2025 chapter makes parallel L1/algae and branch roles central, using the user's 1323/2910/4272 example with an explicit visual-review boundary. 2910's 2026 original four-bars and rebuild slapdown are separated.

Open the **Binders & mechanics** reader tab. Agent exports: `data/binder_audit.jsonl`, `binder_sources.jsonl`, `technical_mechanisms.jsonl`, `technical_parameters.jsonl`, `mechanism_images.jsonl`, and `tower_summary_2026.jsonl`. Long technical reviews are in `docs/technical/`; use `docs/TECHNICAL_EVIDENCE_GUIDE.md` for the reasoning standard. Source PDFs, full transcripts and private transfer files are not redistributed.

## Image portability and agent navigation edition

All 508 figures are embedded in the reader, share one rendering path across galleries, and open in an in-page full-size viewer with original-byte downloads and credited publication links. Markdown image syntax and document-relative links are supported. The image folder is still included for image-capable agents and external Markdown viewers; extract the whole archive to preserve those paths.

Start an agent at `AGENTS.md`, then `agent/manifest.json`. This edition adds 125 complete included-record packets, 766 typed technical claim/parameter records, a lexical retrieval index, an image catalog with dimensions/hashes, publication-version groupings and evaluation cases. Long explanations are preserved. Run `python scripts/query_agent.py search slapdown --year 2026`, then load the suggested robot packet and full game chapter. The reader adds an **Agent entry point** tab. This is navigation and evidence-structure work; technical research coverage remains 27/125 robot-years.

Rebuild the reader and agent layer with `python scripts/build_agent_and_reader.py` (Pillow required to verify/read image formats; the query CLI itself uses only Python's standard library). The canonical agent inputs are the included JSONL and Markdown files. `data/reader_payload.json` retains the prior reader snapshot for reproducible template assembly; it is not a second, independently sourced dataset. Update that snapshot if changing the underlying human-reader content.


## Integrated research pass and video studies

The prior 64-study checkpoint is now merged with 34 additional studies: all 98 previously uncovered robot-years have focused technical studies integrated into the reader, SQL exports and agent packets. The corpus has 227 technical notes across all 125 robot-years. Keep the distinction: only 27 robot-years have the earlier reviewed technical-publication coverage; the other 98 are focused interview/source-bundle studies, not newly discovered binders, CAD certifications or exhaustive version histories.

The current checkpoint recovers all eleven previously pending transcripts through the normal YouTube transcript interface. No CAPTCHA appeared in this session. The 44-video ledger now has 35 complete available-caption reviews: 33 inherited reviews with selected-passage enrichment, plus two new complete caption reads. Those two studies add 27 sections and about 6,900 written words covering six 2026 Einstein matches. Nine recovered transcripts still await full content review. Across all 35 studies there are 132 sections and 114 quiz prompts. Full channel enumeration remains unverified. Tested match players stayed black and buffering, so zero visual Einstein audits are complete. Read `docs/EINSTEIN_VISUAL_AUDIT.md` and `data/einstein_visual_audit.jsonl` before using a match account as observation.

Read `docs/roboreplay/README.md`, `data/roboreplay_review_ledger.jsonl`, `data/video_access_audit.json` and `data/roboreplay_quiz_prompts.jsonl`. Original raw captions are not redistributed. Use `python scripts/query_agent.py search algae --year 2025 --kind video_analysis` and expand to the complete written study before answering. A quiz failure should become an identified evidence gap, not an invented answer.


## Required 1833 task sheet

For each new game/manual analysis, material rules revision or new/revised robot design brief, fill a fresh copy of [the one-sheet template](team1833/1833_Task_List_Template.xlsx). Follow `docs/TASK_LIST_PROTOCOL.md` and `team1833/task_template_schema.json`, with all paths resolved from the corpus root. The template includes task outcome, phase, points/enabling value, priority, difficulty, recommendation, rationale, alliance dependencies, acceptance target, exact rule/source, uncertainty/test and separate human decision. No group tabs; no inherited season-specific decisions. Four previously blocked 604 image originals are now recovered and embedded (2023 robot; 2026 serializer, intake and hopper).
