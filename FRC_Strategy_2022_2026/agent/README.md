> Owner correction 2026-10-27: explain the actual robot in plain language, with concrete mechanism construction, historical feature transfer, physical packaging and decision-relevant engineering support. Read `docs/1833_PLAIN_LANGUAGE_AND_PHYSICAL_DESIGN.md` before drafting or grading a recommendation. Jargon, citations and equations do not substitute for these explanations.

> Current edition 2026-10-27: 141 provisional robot-year studies. Original125 (25/year2022–2026) plus three604 supplements and thirteen curated2018/2019 primary-source studies. Historical expansion adds 52 technical notes, 15 parameter records and 61 credited image references. It is not an EPA-ranked top25-per-year expansion, exhaustive mechanism/version history, new PCH benchmark study or additional video/match audit.

> Current 604 expansion: 128 dossiers = original 125 plus supplemental 2022/2023/2026 604 entries; existing 2024/2025 entries expanded. Original 25/year selections are preserved. Read docs/context/1833-design-workflow.md and data/604_research_audit.jsonl. Visual match audits are no longer required by the user; commentary attribution remains mandatory.

# Agent access and interpretation

The entry point is `../AGENTS.md`. Machine-readable routing and semantics are in `manifest.json`. Paths **inside JSON records** are relative to the corpus root, not this directory. `robot_packets/2026-2910.json`, for example, uses image paths beginning `images/`, resolved from the folder containing `index.html`.

## Two levels of reading

The searchable `retrieval_units.jsonl` contains complete paragraphs or technical fields with stable IDs and exact local locators. Technical fields are separated by evidence type so an agent cannot accidentally cite an analyst explanation as a team statement. Each hit points to a complete robot packet and required game chapter. Long paragraphs are preserved even when they exceed the target chunk size. Retrieval is a navigation operation; a single matching sentence is rarely sufficient for an architectural recommendation.

The `robot_packets/` directory contains one self-contained record for every selected robot-year. It preserves the nested dossier, all available technical notes, selected parameter records, complete robot-specific context documents, publication labels, image metadata, primary source links and binder-discovery audit. The full game chapter remains a required separate read. “Complete packet” means the complete **included record**, not an exhaustive history of the real robot. Coverage gaps remain inside the packet.

## Run local queries

From the corpus root:

```sh
python scripts/query_agent.py search slapdown --year 2026 --kind technical_claim
python scripts/query_agent.py search floor --robot 2026-254 --evidence analyst_inference
python scripts/query_agent.py search L1 algae --year 2025
python scripts/query_agent.py packet 2026-2910
python scripts/query_agent.py images --robot 2026-2910
python scripts/query_agent.py game 2025
```

Search matches all literal word tokens by default; `--any` switches to any-token matching. Use `--robot`, `--year`, `--kind`, `--evidence` and `--subsystem` to constrain the result. Multiword questions are not semantically rewritten: start with a few concrete mechanism or task terms, inspect the vocabulary, and widen explicitly if necessary. FTS5's BM25 ordering measures lexical relevance, not confidence or mechanical quality. `--limit` limits returned records but the response also gives the full match count. The CLI returns the entire selected unit rather than an ellipsized snippet. `read UNIT_ID` retrieves an exact unit by ID.

No API key, embedding model, network request, external package or vector service is required. A future agent can embed the retrieval units, but it should preserve the stable IDs, metadata filters and complete-packet expansion. Do not use a vector similarity score to overrule year/version boundaries.

## Evidence record meanings

| Evidence type | What it permits | What it does not establish |
| --- | --- | --- |
| `team_publication_paraphrase` | Attribute the described construction to the reviewed publication | Exact quotation, every event installation, independent validation |
| `team_reason_or_boundary_paraphrase` | Report the stated rationale or the explicit absence/boundary of one | Assume every record is a positive statement of team intent |
| `team_reported_parameter` | Preserve the selected value with source units and ratio order | Normalize transmission direction, extrapolate duty cycle or certify fabrication |
| `analyst_inference` | Explain a conditional causal hypothesis | Say the team gave that reason or that a test proved it |
| `proposed_test_not_performed` | Recommend a decision-changing experiment | Describe it as completed |
| `evidence_boundary` | Identify source and interpretation limits | Treat a lack of information as hardware absence |
| `mixed_synopsis_coarse_source_mapping` | Locate a useful dossier and its source bundle | Claim precise sentence-level source attribution |
| `analyst_synthesis_with_attributed_evidence` / `mixed_context_read_attribution` | Retrieve contextual reasoning and read its internal attributions | Treat an entire chapter as one uniform primary-source assertion |
| `source_associated_visual_reference` | Locate actual bytes and their publication/crop context | Infer hidden geometry or claim visual understanding from the caption alone |
| `full_transcript_review` / `unreviewed` | Distinguish available caption review from pending video research | Claim visual match watching or full channel coverage |
| `derived_event_benchmark` | Retrieve event/week-specific historical alliance summaries and separately labeled EPA estimates | A guaranteed winning requirement or individual observed scoring total |
| `mixed_match_record_read_note_attribution` | Retrieve scores and explicitly typed reported/inferred Einstein notes | A completed visual audit or permission to narrate unseen action |
| `derived_component_sample` | Retrieve tower-only aggregates with valid/missing denominators | An all-season census or a decomposition of model endgame EPA |

The labels are attribution categories, not calibrated probabilities. All five fields of each technical note remain in the packet. `claims.jsonl` is an explicit field-level view over those notes and selected parameters, not a new independent evidence source.

The search index also includes all 58 event benchmarks, all 80 Einstein records and each 2026 tower-sample summary. Their full record text is retained with denominator and review boundaries. Use `--kind event_benchmark`, `--kind einstein_record` or `--kind tower_sample` to retrieve them separately; exact match or event keys can be searched as literal tokens. The original 7,995 match rows remain available in the main SQL database rather than being duplicated into the agent's small navigation index.

## Images and source citations

`image_catalog.jsonl` provides stable IDs, original local paths, dimensions, MIME types, byte counts, hashes, original URLs, page references where available, crop bounds where recorded, visual-review scope and rights notes. The standalone reader embeds every image and offers an in-page full-size view plus a download of the unchanged original bytes. `index.html#image=IMAGE_ID` opens a particular figure. Original publication links still require internet access and may become unavailable; embedded figure availability is independent of the remote source's availability.

A text-only model must delegate visual inspection to an available image-capable tool or state that it has not inspected the pixels. Source captions and editorial labels should not be passed to a reasoning step as if they were measured geometry. For a proposed combination of mechanisms, inspect feed direction, swept volume, support structure, alignment and packing before claiming compatibility.

## Version grouping

`publication_versions.jsonl` groups existing technical-note version labels without inventing date ranges. Its null event/date fields are intentional. Read the note and dossier for known changes; do not assume label ordering proves chronology. Broad labels can encompass a publication that discusses more than one revision. This directory does not close the exhaustive-version acceptance gate.

## Evaluate an agent before trusting its architecture suggestions

Use `evaluation_cases.jsonl` as held-out prompts when possible. Score year/version correctness, evidence attribution, parameter conditions, unknown handling, source navigation, visual-grounding honesty and interface reasoning separately. Reject an answer that invents team intent or installed geometry even if its recommendation sounds plausible. Successful local index tests establish that navigation works; they do not measure the quality of an arbitrary model's FRC reasoning.


## Integrated research pass and video studies

The prior 64-study checkpoint is now merged with 34 additional studies: all 98 previously uncovered robot-years have focused technical studies integrated into the reader, SQL exports and agent packets. The corpus has 227 technical notes across all 125 robot-years. Keep the distinction: only 27 robot-years have the earlier reviewed technical-publication coverage; the other 98 are focused interview/source-bundle studies, not newly discovered binders, CAD certifications or exhaustive version histories.

The current checkpoint recovers all eleven previously pending transcripts through the normal YouTube transcript interface. No CAPTCHA appeared in this session. The 44-video ledger now has 35 complete available-caption reviews: 33 inherited reviews with selected-passage enrichment, plus two new complete caption reads. Those two studies add 27 sections and about 6,900 written words covering six 2026 Einstein matches. Nine recovered transcripts still await full content review. Across all 35 studies there are 132 sections and 114 quiz prompts. Full channel enumeration remains unverified. Tested match players stayed black and buffering, so zero visual Einstein audits are complete. Read `docs/EINSTEIN_VISUAL_AUDIT.md` and `data/einstein_visual_audit.jsonl` before using a match account as observation.

Read `docs/roboreplay/README.md`, `data/roboreplay_review_ledger.jsonl`, `data/video_access_audit.json` and `data/roboreplay_quiz_prompts.jsonl`. Original raw captions are not redistributed. Use `python scripts/query_agent.py search algae --year 2025 --kind video_analysis` and expand to the complete written study before answering. A quiz failure should become an identified evidence gap, not an invented answer.


## Required 1833 task sheet

For each new game/manual analysis, material rules revision or new/revised robot design brief, fill a fresh copy of [the one-sheet template](../team1833/1833_Task_List_Template.xlsx). Follow `docs/TASK_LIST_PROTOCOL.md` and `team1833/task_template_schema.json`, with all paths resolved from the corpus root. The template includes task outcome, phase, points/enabling value, priority, difficulty, recommendation, rationale, alliance dependencies, acceptance target, exact rule/source, uncertainty/test and separate human decision. No group tabs; no inherited season-specific decisions. Four previously blocked 604 image originals are now recovered and embedded (2023 robot; 2026 serializer, intake and hopper).


## 1833 elite architecture and decision-quality edition

The owner requires an Einstein-level primary contributor, never a support-only design, and no turret. Relatively simple mechanisms should be optimized for elite output. Historical research remains available, including turret robots and complementary match assignments; those are not permission to violate this design brief. Read `docs/1833_DESIGN_DOCTRINE.md`, `docs/DESIGN_REVIEW_PROTOCOL.md`, `docs/1833_OPTIMIZATION_REFERENCES.md` and `docs/evaluations/DUNKTANK_REVIEW_2026-10-26.md`. Use `team1833/design_profile.json`, `team1833/design_review_schema.json`, `agent/design_rubric.json` and `examples/design_review_skeleton.json`. Structural validators audit the one-sheet workbook and review package; they do not establish engineering correctness or improved model performance. All paths in this paragraph are relative to the corpus root.


## Solo RP and decision economics correction

Owner priorities now explicitly require independently achievable ranking bonuses, scoring independence and ambitious seeding. Physical iteration is extremely expensive. Read `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` from corpus root; inexpensive spatial and analytical decisions may precede hardware validation, and tests must justify their decision value and cost. The actual four-lane switch occurred before two-lane CAD was complete.
