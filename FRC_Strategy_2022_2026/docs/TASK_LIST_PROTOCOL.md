> Owner constraints: no pneumatics; no turrets; no support-only architecture. Historical scope and future 2018/2019 roadmap: `docs/1833_ACTUATION_AND_HISTORY_SCOPE.md` from corpus root.

> Owner correction: prioritize independently achievable RP and essential scoring independence. Physical iteration is extremely expensive; use proportionate analytical checks and targeted tests. Read `docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md` from corpus root.

> 1833 override: elite primary-contributor architecture; no support-only robot; no turret. Apply `docs/1833_DESIGN_DOCTRINE.md` and `docs/DESIGN_REVIEW_PROTOCOL.md` from corpus root.

# 1833 required task-list protocol

## Required deliverable and trigger

For every new-season manual analysis, material rules revision, or new/revised robot design brief, fill a fresh copy of `team1833/1833_Task_List_Template.xlsx` before presenting the final architecture recommendation. The required output is a populated workbook with exactly one worksheet, `Task List`. Do not create group tabs. The blank canonical template must remain blank. Save the populated copy under a dated season-and-brief filename; preserve previous analyses so changed priorities can be explained. For a small revision, revise a copy of the previous sheet and identify the changed assumption or rule and its consequences in the rationale. The template is a work product requirement, not a guarantee that a model will obey without being given this protocol.

## Establish the decision context

Fill the six metadata inputs C2:H7: season/game; exact manual revision and governing source URL; target event, week and competition stage; expected alliance roles and opponent assumptions; 1833's time, people, fabrication, budget, robot packaging, practice and maintenance constraints; and agent/date/human review status. Unknown inputs must be explicitly marked unknown with the assumption used provisionally. Historical EPA, alliance scores and Worlds examples do not substitute for the current manual or team constraints. If these are not available, produce a provisional sheet and identify the missing inputs rather than inventing them.

## Enumerate the work before choosing mechanisms

Use one actionable task or required outcome per row, beginning at row 13. Cover every legal task and enabling capability that could matter: mobility and traversal, acquisition, storage and transfer, resource control, scoring, autonomous, endgame, alignment/sensing, defense/support, and other legal actions. These are starter categories, not mandatory robot subsystems. Add or rename categories when the game requires it. Record an excluded or inapplicable task with the reason instead of silently omitting it. Split the same task into separate rows when autonomous/teleop, event stage, alliance role, field location or game state changes its value materially. Keep a functional task such as collecting floor pieces separate from an architecture proposal such as a slapdown intake; mechanisms are evaluated after the functional priorities are stated.

Columns A–N are defined in `team1833/task_template_schema.json` and in the worksheet header. For each occupied task row, complete A–F and H–M; G is calculated. Use N/A plus a reason where a field truly does not apply, and unknown plus a smallest decision-changing test where evidence is missing. Column N is reserved for an actual human decision/rationale: leave blank or label pending human review until 1833 supplies a decision. Never fabricate human approval. Preserve the user's explicit corrections as attributed context alongside their date and scope.

## Give priorities a defensible meaning

Priority 1 means essential to the rule-derived elite primary-contributor objective, before architecture selection; 2 means valuable; 3 means optional. Difficulty uses the team's relative Fibonacci scale: 1, 2, 3, 5, 8, 13, 21. Explain the basis of both judgments in Why / tradeoff. Do not treat the product P×D as an objective ranking, a points-per-effort model or a decision rule. The supplied original workbook used priority times difficulty; this template retains that discussion aid without claiming it captures strategic value. A difficult must-do can remain a must-do. A high-point action can be unnecessary for this robot when an alliance partner covers it. Enabling tasks and denial can be valuable without directly scoring points.

Use the Agent recommendation dropdown: Must do, Might do, Won’t do, or Needs discussion. State the opportunity cost, partner dependency, game-state conditions and reliability assumptions that could change it. Column D should distinguish rule points from inferred enabling value; include timing, capacity, accuracy or probability conditions when quantified. Do not invent numeric precision when the data supports only a qualitative judgment.

## Make each recommendation testable and traceable

Acceptance target / units must describe a measurable functional outcome under specified conditions, or explicitly say the target is not yet established. Examples include loaded collection success, release accuracy at a stated location, usable capacity with the mechanism swept envelope, sustained throughput including acquisition and readiness interruptions, or recovery time after a jam. These examples are not requirements or performed tests. Record the rule number/section/page and revision, and the exact source or corpus locator behind each factual claim. Clearly distinguish official rules, team-reported performance, attributed commentary, 1833's judgment and agent inference. Unknowns / smallest test should identify what observation or prototype result could change the priority or architecture.

After filling the sheet, compare at least two coherent architectures against the same prioritized tasks and constraints. Cite historical inspiration by year/team/version and inspect the whole acquisition-to-output interface. Feed architecture findings back into the sheet when they change difficulty, dependencies or acceptance criteria. Preserve both the initial reason and the reason for the revision. Do not jump from famous team names to compatibility claims.

## Workbook handling and completion gate

The starter table `RobotTasks` occupies A12:N92, providing 80 task rows. It is a starting capacity, not a task limit. If more rows are needed, insert rows within/at the end of the table and extend the table, G formulas, E/F/H validations and summary ranges in B10/E10/H10/K10 to include every occupied row; move the provenance footer below the table. Do not add another worksheet. Keep frozen headings and task columns. G must remain blank until task, priority and difficulty are supplied. Summary counts count only the named statuses; verify no recommendation is left on an unused row and no placeholder category row is counted as a task.

Before delivering, check exactly one sheet, correct manual revision, all task categories considered, all occupied rows documented, no invented decisions, formulas recalculated, no spreadsheet errors, and source locators preserved. Unresolved items may remain explicitly unresolved; their existence must be reflected in the confidence and proposed tests. Deliver the filled workbook with the design analysis. A prose task list alone does not satisfy the user's requested workflow.

## Provenance

This template adapts the user's supplied `team1833/task_list_2026.xlsx`, particularly its cleaned task list and the group sheets' priority/difficulty fields, without reproducing the group tabs or inheriting the original season's priorities. `team1833/mechanical_research_2026.pdf` remains a separate input to mechanism brainstorming. Historical kickoff choices and later strategic corrections retain their original context; the template does not rewrite them as current universal priorities.


## Substantive completion gate added after the DunkTank review

Task-specific dependencies, justified difficulty, distinct unknown/test/decision consequences, and consistent screening versus release requirements are mandatory. Repeated generic filler does not satisfy a field. A field threshold is not an onboard capacity mandate. Compare capacities and fixed/expanding storage, perform common-assumption match modeling, and apply the owner constraints before final recommendation. Run `scripts/audit_task_workbook.py` and the design-review validator; human review remains necessary. Follow `docs/DESIGN_REVIEW_PROTOCOL.md` for detailed requirements.
