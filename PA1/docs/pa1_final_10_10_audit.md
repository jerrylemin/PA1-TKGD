# PA1 Final 10/10 Completion Audit

Audit date: 2026-06-22
Workspace: `C:\Users\Administrator\Documents\MEGA\tkgd\PA1`

## 1. Executive verdict

Status: NOT READY

Score: 92.5/100

One-sentence reason: Core PA1 deliverables, zip packaging, product migration, citations, and visual evidence are strong, but the final WeeklyReport PDF still contains placeholder team-member language and does not include the required four real member names, so the package is not a strict 10/10 submission.

## 2. Required deliverables check

Repository inspection:

- Current working directory: `C:\Users\Administrator\Documents\MEGA\tkgd\PA1`
- Report source files: `sources/GroupID-PA1-ProductResearch.md`, `sources/GroupID-PA1-PotentialSolutions.md`, `sources/GroupID-PA1-PeerReview.md`, `sources/GroupID-PA1-WeeklyReport.md`
- PDF generation pipeline: `build_pa1_package.py`
- Screenshot capture pipeline: `scripts/capture-pa1-screenshots.js`
- Screenshot annotation pipeline: `scripts/annotate-pa1-screenshots.js`
- Visual npm command: `npm run visuals:pa1`
- Depth-4 tree was inspected excluding vendor/archive noise; relevant roots found: `assets/`, `assets/screenshots/`, `assets/diagrams/`, `docs/`, `generated_text/`, `scripts/`, `sources/`, four final PDFs, `GroupID-PA1.zip`, `GroupID-PA1-WorkDivision.docx`, `pa1_sources_fifa_chess.json`, `assets/figures_manifest.json`, `artifact_manifest.json`, and `package.json`.

| File | Exists | Size | Pass/Fail | Notes |
| --- | --- | ---: | --- | --- |
| `GroupID-PA1-ProductResearch.pdf` | Yes | 9,231,554 bytes | Pass | 37 pages; largest report as expected. |
| `GroupID-PA1-PotentialSolutions.pdf` | Yes | 561,323 bytes | Pass | 14 pages; larger than 10 KB. |
| `GroupID-PA1-PeerReview.pdf` | Yes | 10,515 bytes | Pass | 3 pages; larger than 10 KB but only narrowly. |
| `GroupID-PA1-WeeklyReport.pdf` | Yes | 11,305 bytes | Pass with issue | 3 pages; larger than 10 KB but contains placeholder text. |
| `GroupID-PA1.zip` | Yes | 7,846,942 bytes | Pass | Contains exactly four top-level PDFs. |
| `assets/figures_manifest.json` | Yes | 49,666 bytes | Pass | 26 screenshots and 8 solution figures recorded. |
| `pa1_sources_fifa_chess.json` | Yes | 14,605 bytes | Pass | 22 official sources. |
| `docs/pa1_fifa_chess_visual_migration_audit.md` | Yes | 3,772 bytes | Pass | Supporting visual migration audit exists. |
| `docs/visual_pipeline_validation.md` | Yes | 1,220 bytes | Pass | Supporting visual validation exists. |

Generated PDFs found: final four PDFs at repo root, `PA1-LKDuy-2026-Public.pdf`, and archived previous PA1 PDFs under `archive/previous_pa1_outputs_20260610_233509/`.

## 3. Zip check

Contents:

- `GroupID-PA1-ProductResearch.pdf` - 9,231,554 bytes
- `GroupID-PA1-PotentialSolutions.pdf` - 561,323 bytes
- `GroupID-PA1-PeerReview.pdf` - 10,515 bytes
- `GroupID-PA1-WeeklyReport.pdf` - 11,305 bytes

Missing: None

Extra: None

Pass/Fail: Pass

## 4. Product consistency check

Old product scan:

- Scanned final PDF extracted text and final source markdown for: Strava, Nike Run Club, NRC, Garmin, Garmin Connect, Forerunner, smartwatch, running app, cycling app, GPS watch, START/STOP, segment leaderboard.
- Matches found: 0.
- Pass/Fail: Pass

New product scan:

| File | FIFA.com coverage | Chess.com coverage | Pass/Fail |
| --- | --- | --- | --- |
| ProductResearch PDF | FIFA.com 55; FIFA 207; Match Centre 20 | Chess.com 132; chess 152; Game Review 12; Analysis 42 | Pass |
| PotentialSolutions PDF | FIFA.com 11; FIFA 54; Match Centre 5 | Chess.com 33; chess 36; Game Review 3; Analysis 17 | Pass |
| PeerReview PDF | FIFA.com 5; FIFA 37; Match Centre 2 | Chess.com 37; chess 39; Game Review 4; Analysis 11 | Pass |
| WeeklyReport PDF | FIFA.com 15; FIFA 54; Match Centre 4 | Chess.com 36; chess 44; Game Review 2; Analysis 7 | Pass |

Pass/Fail: Pass for product pair and old-product removal.

## 5. ProductResearch score

Score: 57/60

Missing:

- Use cases include device, posture, attention, distraction, flows, alternates, error paths, and feedback, but the detailed use-case tables do not split every context field into the exact labels `where`, `when`, `environment`, and `interaction method`.

Strengths:

- Title, executive summary, method, product rationale, FIFA.com overview, Chess.com overview, user groups, and references exist.
- 12 persona rows found, exceeding the required 6.
- 10 use cases found, meeting the required 10.
- 20 unique HCI findings found, meeting the required 20.
- Each main HCI row names finding ID, product, figure/screen, UI element, observed behavior, persona/context, HCI concept, benefit/drawback, scenario, severity, evidence, and improvement direction.
- 24 ProductResearch figure headings found.
- 22 numbered references appear in the references section.

Fixes needed:

- For strict rubric polish, rewrite each detailed use-case context table to include explicit fields for where, when, posture, device, attention level, environment, and interaction method.

## 6. PotentialSolutions score

Score: 24.5/25

Missing:

- No major content gap found. Half-point reserved because solution figures are lightweight sketch/mockup images rather than high-fidelity interface mockups.

Strengths:

- Executive summary, drawback inventory, drawback-to-solution mapping, visual solution figures, solution details, prioritization, quick wins, deeper redesigns, rollout plan, and references exist.
- 10 drawbacks cover both FIFA.com and Chess.com.
- 20 unique solution IDs found: 10 FIFA and 10 Chess.com.
- Every drawback maps to at least 2 solutions.
- Solution rows include product linkage, persona/context, HCI principle, UI behavior detail, expected improvement, tradeoff, priority, and effort.
- 8 visual solution figures exist.

Fixes needed:

- Optional polish only: make solution mockups more visually detailed if the course grader expects richer UI mockups.

## 7. PeerReview score

Score: 9/10

Missing:

- Owner fields still use `Member1` to `Member5` placeholders.

Strengths:

- Seven-minute script exists.
- Slide outline includes product pair, method/evidence, FIFA findings, Chess.com findings, solution priorities, sprint/QA, and closing.
- Likely questions and prepared answers exist.
- 8 mock feedback entries exist with reviewer name, role, feedback, response/revision, owner, and status.
- Revision log and rehearsal checklist exist.
- Product pair is consistently FIFA.com and Chess.com.

Fixes needed:

- Replace placeholder owners with real member names or initials before final submission.

## 8. WeeklyReport score

Score: 2/5

Missing:

- Required real members are absent from the final PDF/source: Le Minh 21127645, Nguyen Vu Bach 21127224, Pham Nguyen Gia Bao 20127119, Trang Minh Nhut 22127318.
- WeeklyReport explicitly says there are `five placeholder team members`.
- WeeklyReport explicitly says `Manual placeholders remain for GroupID, member names, and peer reviewer names`.
- Sprint planning and scrum rows exist, but the rubric asks each member to answer completed work, next work, and issues/obstacles; the current version summarizes at meeting level only.
- Meeting dates or date placeholders are absent.

Strengths:

- Sprint objective exists.
- Role assignment exists, but it is placeholder-based.
- Sprint planning, weekly scrum 1, weekly scrum 2, and sprint review rows exist.
- Workload matrix and submission checklist exist.
- Diagram C sprint timeline exists.

Fixes needed:

- Replace placeholder team model with the four required real members.
- Add per-member scrum details for completed work, next work, and issues/obstacles.
- Add dates or accepted date placeholders for planning, scrum 1, scrum 2, and sprint review.
- Remove all final-report `placeholder` wording.

## 9. Visual evidence audit

Screenshot counts:

- Raw FIFA screenshots: 13
- Raw Chess.com screenshots: 13
- Annotated FIFA screenshots: 13
- Annotated Chess.com screenshots: 13
- FIFA crops: 13
- Chess.com crops: 13

Figure counts:

- Manifest screenshot items: 26
- Manifest screenshots by product: 13 FIFA, 13 Chess.com
- ProductResearch figure headings: 24
- PotentialSolutions solution figures: 8
- Solution diagram files: 8

Missing images:

- None found from manifest paths.

Caption issues:

- No missing manifest captions found.
- Pixel comparison confirmed all 26 annotated screenshots differ from their raw counterparts, which supports that highlights were added.

Pass/Fail: Pass

## 10. Citation audit

FIFA sources: 9

Chess.com sources: 13

Missing citations:

- No major citation gap found for the core product claims.
- ProductResearch and PotentialSolutions both include references.
- Source log contains 22 official FIFA/Chess.com sources.
- No old-product sources found in final deliverables.

Pass/Fail: Pass

## 11. Formatting audit

Issues:

- `GroupID-PA1-WeeklyReport.pdf` contains `placeholder` text.
- `sources/GroupID-PA1-WeeklyReport.md` contains the same placeholder text.
- `GroupID-PA1-WeeklyReport.pdf` uses `Member1` to `Member5`, conflicting with the required four-member roster.
- `sources/GroupID-PA1-PeerReview.md` uses `Member1` to `Member5` owner placeholders.
- `GroupID-PA1-WorkDivision.docx` exists, but extracted text does not appear Vietnamese and does not include the four required real member names.

Pass/Fail: Fail

## 12. Critical blockers

1. WeeklyReport final PDF/source does not include the required four real members: Le Minh 21127645, Nguyen Vu Bach 21127224, Pham Nguyen Gia Bao 20127119, Trang Minh Nhut 22127318.
2. WeeklyReport final PDF/source contains explicit placeholder language, including `five placeholder team members` and `Manual placeholders remain`.
3. WeeklyReport scrum evidence is meeting-level only and does not provide each member's completed work, next work, and issues/obstacles.
4. Supporting WorkDivision docx fails its optional audit checks: not Vietnamese by extracted text signals and missing the required four real members.

## 13. Exact fix plan

| Priority | File | Issue | Required fix | Estimated effort |
| --- | --- | --- | --- | --- |
| P0 | `build_pa1_package.py`, `pa1_project_data.json` if used | Team/member placeholders drive generated reports. | Replace `Member1` to `Member5` with the four required real members and adjust role model to four people. | 30-45 min |
| P0 | `sources/GroupID-PA1-WeeklyReport.md` via generator source | WeeklyReport missing real roster and contains placeholder text. | Add the four required members, remove all placeholder wording, and rebalance workload for four members. | 30-45 min |
| P0 | `sources/GroupID-PA1-WeeklyReport.md` via generator source | Scrums do not answer per member completed/next/issues. | Add planning date, scrum dates, sprint review date, and per-member scrum rows with completed work, next work, and blockers. | 45-60 min |
| P1 | `sources/GroupID-PA1-PeerReview.md` via generator source | Owner placeholders remain. | Replace `Member1` to `Member5` owner labels with real names or agreed initials. | 15-20 min |
| P1 | `GroupID-PA1-WorkDivision.docx` generation source/script | Supporting docx is not Vietnamese and lacks required real names. | Regenerate Vietnamese work-division docx with four real members, RACI, checklist, deliverable ownership, and signature table. | 45-60 min |
| P1 | `build_pa1_package.py` | Final deliverables must match source after fixes. | Regenerate four PDFs and zip, then rerun old-product scan and zip validation. | 15-30 min |
| P2 | `sources/GroupID-PA1-ProductResearch.md` via generator source | Use-case context is good but not label-perfect. | Split context fields into where, when, posture, device, attention level, environment, and interaction method for all 10 use cases. | 30-45 min |

## 14. Final checklist

- [x] Product pair correct
- [x] Old products removed
- [x] 4 PDFs present
- [x] Zip correct
- [x] ProductResearch complete
- [x] PotentialSolutions complete
- [x] PeerReview complete
- [ ] WeeklyReport complete
- [x] Visual evidence complete
- [x] Citations complete
- [ ] Ready to submit
