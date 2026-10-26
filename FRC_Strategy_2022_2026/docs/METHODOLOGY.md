# Methods and limits

This research edition is a substantial starting corpus. It does **not** satisfy a literal claim that every mechanism, every intermediate robot version and every Einstein tactic has been exhaustively verified. The coverage audit is part of the data, not a footnote. All 125 entries are reference dossiers; none is certified as a complete historical record.

## Team selection

The starting lists are the Statbotics mirror's team-year total-points EPA rankings for 2022–2026, ordered descending. Ties are ordered by team number. Selected dossiers preserve original rank and EPA. Higher-ranked candidates that were not selected remain in `selection_audit.csv`, with a retrieval/scope reason. A skip means this review did not obtain sufficient usable coverage; it does not mean the team published nothing or built an inferior robot.

Substitution makes the sample biased toward teams that publish, English-language interviews and documentation accessible to these tools. High EPA is also an outcome-selected sample. This dataset cannot identify the causal effect of a mechanism across all teams, nor prove the highest-ranked architecture was best for a particular team's resources.

Some selected entries still have important gaps, especially endgame installation and complete season chronology. Those are marked provisional. The user's stricter requirement—25 fully documented accepted entries in each season—remains an open acceptance gate. The database does not pad that gate by calling an unresolved feature absent or treating one interview as proof of every version.

## Source hierarchy

Official game manuals define rules; event-specific rules and updates are necessary for historical thresholds. TBA supplies event/match identities, schedules, divisions and score verification. Numeric bulk data came through the user-supplied public Statbotics mirror API. The package keeps both TBA links and numeric-source URLs. Selected direct TBA/FIRST checks corroborate results; it does not claim every one of the 7,995 scorecards was independently re-entered from TBA.

Team-authored binders, CAD/code releases, build journals and technical interviews support robot summaries. Interview captions can mistranscribe dimensions, materials and team numbers; unresolved transcription is not promoted to fact. A third-party dashboard was used to discover links, not as an authority for robot specifications. Additional bibliography links may be discovery-only; those are separate from reviewed source bundles.

Copyrighted source binders, complete transcripts and forum threads are not redistributed. The deliverable contains concise original summaries, derived data and links. Intermediate downloads and frontend assets are excluded. No API keys or authentication material are included.

## Numeric definitions

`epa` is the snapshot team-year estimate, not a raw individual score. `pre_elim_epa` is the event estimate before elimination play. `event_end_epa` is after that event. The eighth-highest EPA is **not** the eighth qualification seed. Qualification rank 1 is recorded separately. Components may be negative or physically implausible because they are model estimates; they are never treated as literal individual counts.

Clean alliance score means score excluding received foul points. Champion playoff clean-score median/min/max summarize matches attributed to the eventual winning alliance, using at least two continuing lineup members to account for an appearing substitute. The full four-team award roster is not reconstructed when a robot never appeared in the sampled lineups. Selection and winning a district event also depend on partners and opponents; there is no guaranteed “EPA needed to win.”

Event participation is derived from actual matches. This avoids a 2026 Einstein payload metadata problem that listed hundreds of teams. There are 75 events, 7,995 completed match rows, 4,021 appearing team-event rows, 58 benchmark rows and 80 Einstein rows in this snapshot. Some completed matches have missing score components, including disqualification/abnormal cases; these remain null, not invented zeros.

## Einstein analysis

All 80 records have phase/component analysis and source links. Fifty-one have reviewed reported tactics from broadcast captions or first-hand team accounts. None has a completed visual frame-by-frame audit. Other rows retain an explicit pending tactical-review state. Captions do not establish failure causes or player intent, and an aggregate teleop advantage does not prove a named defender's effect.

One mirror video association is demonstrably wrong: the video linked to 2022 semifinal match 2 describes match 15 and is embedded on TBA's match-15 page. The association is rejected for match 2 and used only for match 15. The primary ledger preserves the error flag.

For 2026, the two own-active scoring windows occur at different clock times for red and blue. `endgame_points` includes final-window fuel; tower components are kept separately. This distinction prevents the especially misleading inference that a large endgame score means a high climb.

## Reproducibility and updates

The package includes schema, build scripts, exact input/derived exports and checksums. The compact numeric exports are sufficient to rebuild the database without the original downloaded web pages. Rechecking human interpretation still requires following the primary links. The ranking snapshot is dated 2026-10-25; later EPA models, offseason records, corrected matches or link changes can alter a fresh pull.

To add a source or resolve a gap, preserve the original claim, add the new dated evidence, mark whether the conclusion changed and update coverage. To add a robot version, create a distinct version row with its applicable period; do not silently overwrite the season record with a later mechanism. Architecture recommendations should cite the version actually supporting them.
