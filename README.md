# FRC Strategy Research Database

Project imported from `FRC_Strategy_2022_2026 (7).zip`.

Open [the offline reader](FRC_Strategy_2022_2026/index.html) in a browser. No server or account is required. Source links need an internet connection.

The [project README](FRC_Strategy_2022_2026/README.md) describes the research, data, scripts, and evidence limits. The ZIP's folder structure is preserved under `FRC_Strategy_2022_2026/`.

## Push to GitHub

This repository uses `main` and is connected to [GoldenAppleBoss/FRC_Strategy_2022_2026_Database](https://github.com/GoldenAppleBoss/FRC_Strategy_2022_2026_Database).

Run these commands from this repository's root:

```powershell
git add .
git commit -m "Import updated FRC strategy project"
git push origin main
```

Keep the included databases, images, and offline reader in the repository. The root `.gitignore` excludes local environments, caches, secrets, and ZIP downloads.

## Local tools

The reader works on its own. To use the data query CLI, install Python 3 and run:

```powershell
cd FRC_Strategy_2022_2026
python scripts/query_agent.py search slapdown --year 2026
```

With Node.js installed, check the reader logic from the repository root:

```powershell
node FRC_Strategy_2022_2026/scripts/check_reader.js
```
