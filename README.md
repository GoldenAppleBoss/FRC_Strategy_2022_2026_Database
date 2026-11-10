# FRC Strategy Research Database

Open [the standalone reader](FRC_Strategy_2022_2026/index.html) in your browser. For an agent, open the `FRC_Strategy_2022_2026` folder as the working directory and start with `AGENTS.md` and `agent/manifest.json`.

This source export combines the tracked project files with the final reader's expanded corpus. It includes 143 robot dossiers, 292 event benchmark distributions, 21 labeled 2026 Team 4414 revisions, the image audit, both SQLite databases, and the local workbench source. The export omits Git history and local settings.

From inside `FRC_Strategy_2022_2026`:

```text
python scripts/query_agent.py search Lockdown --kind dossier_review
python workbench/research.py packet 2018-254 --section source_review
python workbench/workbench.py
```

The reader opens offline. The workbench starts a local server and uses your authenticated Codex CLI for recommendation runs. Source links need internet access.

The expanded SQLite tables are `dossier_source_reviews`, `event_benchmark_distributions`, `design_comparisons` and `image_visual_audit`. The legacy `benchmarks` table retains the original sample for compatibility. Run `python scripts/rebuild_database.py` to rebuild the SQL database from the included exports. Older checkpoint and validation files document earlier editions. The final reader and retrieval data already match. The older corpus generators recreate earlier reader layouts.

The latest update was imported from `FRC_Strategy_2022_2026_Database.zip` on November 9, 2026. The image audit records the 20 excluded images removed by this update. The extracted import folder and local workbench runs are excluded from Git.

Check the current reader and workbench from the repository root:

```text
node FRC_Strategy_2022_2026/scripts/check_reader.js
python -X utf8 FRC_Strategy_2022_2026/workbench/test_workbench.py
```

The reader check uses the final interface and compressed data format. The workbench suite uses a deterministic CLI double; it does not run a live recommendation. The older `validate_architectures.py` currently fails its inherited note-preservation hash assertion for `tech-86ae539d8a57982e4c-17` in the supplied export.
