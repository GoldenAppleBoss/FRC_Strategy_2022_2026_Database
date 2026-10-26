# Scouting analysis with Tableau

Authored expansion from selected timestamped passages, with the retained prior full-caption review. This is not a new full visual audit or a claim that the enrichment covers every spoken point.

[Original video](https://www.youtube.com/watch?v=R11PUq_m8Fk)

## Retained full-caption account

This tutorial builds averages, phase breakdowns, scatterplots, box plots and shared selection filters. It emphasizes match-level context: the same average autonomous score can represent different capability and reliability distributions, and an outlier deserves match review. This is a 2024 tutorial using historical example data, not current Tableau documentation.

## 1. Identifiers are dimensions, not quantities

[Navigation 225–290 s](https://www.youtube.com/watch?v=R11PUq_m8Fk&t=225)

**Source account / attributed commentary:** The tutorial distinguishes team and match labels from values to aggregate, and notes that Boolean observations can be represented separately.

**Conditional interpretation — analyst reasoning:** A data model that averages team numbers or counts rows when it intends to average performance can look polished while answering the wrong question. Define the unit of observation—robot-match, alliance-match or event—before building plots.

## 2. Show phase context without hiding units

[Navigation 675–740 s](https://www.youtube.com/watch?v=R11PUq_m8Fk&t=675)

**Source account / attributed commentary:** The source organizes tooltips to separate auto, teleop, endgame and overall output, reducing clutter in a bubble/scatter view.

**Conditional interpretation — analyst reasoning:** A clean display should retain metric definitions. Dock points are not a count of docks; alliance points are not individual contributions. Cross-game phase labels can conceal different scoring actions, especially 2026 endgame fuel versus tower points.

## 3. Outliers are match-review leads

[Navigation 1125–1190 s](https://www.youtube.com/watch?v=R11PUq_m8Fk&t=1125)

**Source account / attributed commentary:** The commentator recommends inspecting the match behind a peak or failure, asking whether the performance is repeatable and fits the intended alliance.

**Conditional interpretation — analyst reasoning:** A peak is useful evidence of capability only after identifying the enabling conditions. A mean depressed by a breakdown may hide upside, but removing failures without judging repairability overstates expected output. Evaluate reliability and ceiling separately.

## Quiz prompts

- What is the unit of observation in this plot?
- When should a high outlier affect alliance selection?
- How could averaging disguise a breakdown or autonomous incompatibility?

## Remaining uncertainties

- Historical Tableau tutorial, not current software documentation.
- No causal validation of example outliers.

No new visual match audit. Timestamp spans are navigation aids; the selected-passages manifest distinguishes the new recheck from the inherited full-caption review.
