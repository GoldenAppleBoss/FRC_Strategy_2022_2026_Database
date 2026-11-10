# BEAN Design Workbench

The workbench uses a local, authenticated Codex CLI because the investigation needs the whole repository available as external memory, actual image inspection, shell-based calculations, a writable research notebook and a controllable execution environment. It does not put the complete corpus in one prompt or ask for an API key in the browser. The user receives one index.html, containing the research reader, branded interface, downloadable launcher and an embedded research workspace.

## Start

Open index.html and choose Local runner setup. Download workbench.py beside the HTML. Use Python 3.10+; install the official Codex CLI and sign in with `codex login`. If using the npm distribution, Node.js LTS is needed. Install `pymupdf` for complete PDF extraction and page rendering. Run `python workbench.py` (or `python3` / `py` as appropriate). The launcher opens the loopback workbench. Keep its terminal open.

Inside an existing corpus, `python workbench/workbench.py` uses its current original research assets. A launcher beside the standalone index restores the embedded research workspace, source text, full robot packets, compressed display images and lexical retrieval. The restored workspace records DELIVERY_PROVENANCE.json. It is a research distribution, with no Git history, original-resolution figure guarantee or required worksheet. The task explicitly waives workbook deliverables.

The default model is the user's configured Codex model; reasoning defaults to high. Users can specify a model they have access to. Unsupported model/settings or sign-in/quota errors are shown as failed passes with saved research; the application does not silently substitute a model or simulated output. Use is subject to the account's available Codex access/usage.

## Investigation

1. Read every manual page, inspect consequential figures and identify the actual game/revision.
2. Compare complete elite-primary architectures with common assumptions.
3. Retrieve full relevant packets, exact versions and images; preserve typed evidence and the strongest rival.
4. Develop one coherent concept, including complete possession paths and physical packaging.
5. Challenge strategy, reach, interference, transfer assumptions, power, CG, service and unsupported claims.
6. Resolve the critique and write recommendation.md.

Each pass starts fresh with the user brief, persistent notebook, source map and access to complete prior results and raw sources. This limits long-chat context loss without discarding access to detail. The runner checks manual page coverage, corpus identifiers, image observation structure and blocking final findings. It automatically asks the agent to repair a failed contract once. Consequential questions pause the pipeline and rerun the affected pass with owner answers. Stop/resume preserves completed passes; no percentage is fabricated.

Source inspection and mechanical understanding are agent-reported. Automated checks do not independently verify that an image was understood, establish causality or validate physical performance. The final recommendation still requires human engineering review and the identified decision-changing checks.

## Local boundary and storage

The server binds to 127.0.0.1, restricts Host/Origin and requires a per-process CSRF token for writes. It does not enable CORS, collect API keys, execute arbitrary browser-supplied commands or expose general filesystem browsing. The runner invokes an argument-array Codex command in an isolated `.bean-workbench/RUN_ID` folder with workspace-write sandboxing; it never uses a dangerous sandbox bypass. The corpus is a read-only task input. Manuals, structured outputs, prompts, notebooks and logs stay in the local run store and are excluded from Git.

The existing Codex authentication is used by the CLI; selected manual/research content is processed by the configured Codex provider as part of the user's run. This is not an offline model. The workbench itself adds no separate analytics or external application backend.

## Verification

Run `python workbench/test_workbench.py` for the deterministic CLI-double integration suite, covering a six-pass lifecycle, questions/resume, cancellation, reference/coverage gates, automatic contract repair, snapshot mismatch and actual loopback HTTP/CSRF paths. Run `node scripts/check_reader.js` for research and workbench render checks. The standalone installation and actual PDF extraction/rendering are also checked.

A live CLI smoke test in the authoring environment was blocked by its read-only Codex runtime state directory; sign-in detection succeeded. The mock runner tests are not a live six-pass model run or a benchmark of design quality. Browser QA covers the branded interface, brief inputs, missing-manual feedback and setup flow. Current limitations are recorded in VALIDATION.json.

## References and assets

Execution follows the official Codex non-interactive interface documented at https://learn.chatgpt.com/docs/non-interactive-mode and confirmed against the installed CLI help. Branding is based on https://www.team1833.org: teal #237f8f, deep teal #1a6573, coral #f34732, tint #eaf5f7; Chewy headings and Manrope body type. The team logo and Clover photograph are credited to Team BEAN. Historical research figures retain their own source attribution.

The launcher checks research and runtime-support fingerprints against the embedded snapshot. An older existing repository is preserved and a matching workspace is restored instead. Each run records its snapshot and blocks resume or a new pass if those sources changed.
