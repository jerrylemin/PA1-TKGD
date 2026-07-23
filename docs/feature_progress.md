# Feature Progress

## 2026-06-10

Completed:

- Migrated the product pair to FIFA and Chess.com.
- Added Playwright screenshot capture and sharp annotation pipeline.
- Captured 13 raw FIFA screenshots and 13 raw Chess.com screenshots.
- Generated 26 annotated screenshots, 26 crops, and 8 solution sketch figures.
- Refreshed official source log as `pa1_sources_fifa_chess.json`.
- Rebuilt personas, use cases, HCI findings, drawbacks, and solutions with F- and C-prefix IDs.
- Regenerated four final PDF deliverables with GroupID filenames.
- Generated final zip with the four PDFs at top level.
- Generated editable Markdown, Mermaid source files, shared fact base, audit, and artifact manifest.
- Validated PDF readability, old-term removal, source counts, real team names, and zip contents.
- Replaced generic team labels with the four real members in ProductResearch, PeerReview, WeeklyReport, shared JSON, and generated PDF text.
- Added strict ProductResearch use-case labels for Where, When, Posture, Device, Attention level, Environment, Interaction method, Goal, Trigger, Precondition, Normal flow, Alternate flow, Error path, Feedback observed, Figure or source reference, and HCI concepts.
- Expanded WeeklyReport with real roster, planned meeting schedule, sprint planning, two per-member scrum tables, sprint review, workload matrix, and final checklist.
- Regenerated Vietnamese WorkDivision docx with RACI, quality checklist, and signature table.

Remaining manual updates:

- Replace `GroupID` with the real group ID if provided.
- Replace mock/internal rehearsal feedback names with actual peer names if required.

## 2026-07-02

- Enforced two-person ownership per website and four balanced 25% contribution rows.
- Added cross-report ownership and ID traceability.
- Created and rendered six Mermaid diagrams; embedded them in all four reports and WorkDivision.
- Regenerated four PDFs, exact four-PDF zip, and both WorkDivision DOCX copies.
- Added `scripts/validate_pa1_balance_diagrams.py`; validation status is PASS.

## 2026-07-06

- Created `GroupID-PA1-Presentation.pptx` and the matching `output/` copy.
- Expanded the presentation to 21 Vietnamese slides so screenshots and diagrams remain readable without cropping.
- Split dense sections by product, persona, use case, HCI finding, limitation, and solution.
- Added substantive speaker notes to all 21 slides for a 5–10 minute presentation.
- Validated 36 image placements, 21 title objects, no slide overflow, no prohibited visible terms, and identical hashes for both PPTX copies.
- Captured 13 usable fresh screenshots with Playwright and generated 11 verified annotation/crop sets in `assets/presentation/`.
- Rendered and visually reviewed every slide before and after; fixed slides 1, 4, 6, 9, 11, 13, 16, 17, 18, and 20.
- Replaced small/cut or misleading visuals with larger real UI evidence; final visual review is PASS 21/21.

## 2026-07-07

- Added centralized `config/pa1_config.json` and derived report, ZIP, WorkDivision, and output names from `group_id`.
- Rebuilt WeeklyReport into the exact ten-section RUP + Scrum minutes structure and removed product References.
- Corrected all ten PotentialSolutions canonical drawback/finding/solution mappings and added source-only evidence labels where no screenshot visibly proves the claim.
- Separated internal rehearsal feedback from the pending real-classroom feedback table without fabricating names or comments.
- Added strict draft/final submission validation, PDF extraction fallback, image checks, ZIP hash checks, freshness checks, and false-readiness detection.
- Regenerated four PDFs, extracted text, WorkDivision DOCX, output copies, exact four-PDF ZIP, shared JSON, and SHA-256 manifest.
- `npm run build:pa1`: PASS. `npm run validate:pa1:draft`: PASS. Final mode: expected FAIL until real group ID and peer feedback are provided.
- Rendered and inspected all 70 final PDF pages; no text exceeded page bounds. DOCX visual render remains unavailable because LibreOffice/soffice is not installed.
## 2026-07-07 - Potential Solutions visual-report revision

- Created `Group10-PA1-PotentialSolutions_VisualReport_Revised.docx` from the locked original.
- Replaced the ten solution-card evidence panels with fresh FIFA.com, FIFA+/DAZN, Chess.com, or official Chess.com Help captures dated 2026-07-07.
- Removed every illustrative redesign image and replaced each right-hand panel with location-specific UI change bullets tied to F-S1..F-S10 and C-S1..C-S10.
- Added an explicit cross-report contract to `Group10-PA1-ProductResearch_VisualReport.docx`; validated shared persona, figure, source, and HCI IDs.
- Follow-up revision overwrote the requested `(1).docx` after backing it up, removed all date/specification labels, replaced support-site screenshots with live Chess.com UI, and recaptured FIFA pages without modal/privacy overlays.
- LibreOffice 26.2.4.2 was installed through winget. The final document rendered to a 20-page PDF for visual QA.
- References were normalized to a complete `[1]`-`[20]` sequence with clickable hyperlinks. Live Chess.com UI links now cover Play Online, Play Computer, Analysis, Puzzles, and Lessons; behavioral help links remain only where needed to support premove, Focus Mode, Game Review, and Analysis claims.

## 2026-07-13 - Teacher Feedback Response

- Replaced the old PeerReview presentation-preparation content with a standalone Vietnamese Teacher Feedback Response for Group10.
- Added `Group10-PA1-PeerReview-Revised.docx`, matching eight-page A4-landscape PDF, and `Group10-PA1-PeerReview-Review.md`.
- Added `scripts/create_teacher_feedback_response.py` so DOCX and PDF are generated from one structured content source.
- Covered FIFA ticket seating, third-party handoff, confirmation, deeper UI and color; covered Chess.com empty space, color, deeper UI and revised mapping.
- Removed the old question-answer structure, temporary feedback material, placeholder table, old reviewer names, and the placeholder group identifier from the revised artifacts.
- PDF render QA passed on all eight pages; Word opened the DOCX and reported eight pages; text scans passed for required sections and prohibited legacy content.
- Added the fully English eight-page PDF `Group10-PA1-PeerReview-Revised-English.pdf`; automated text scan found no Vietnamese residue and full-page render QA passed.

## 2026-07-13 - Group10 WeeklyReport rebuild

- Replaced the old WeeklyReport source with a natural RUP + Scrum record containing one Sprint Planning, two Weekly Scrum meetings, and one Sprint Review and Retrospective.
- Added `scripts/create_weekly_report.py` and generated the required Group10 DOCX, PDF, and review file from the shared Markdown source.
- Updated the package configuration to Group10 and rebuilt the four Group10 PDFs plus the exact four-PDF ZIP.
- Recorded missing Google Docs, Drive, and optional Zoom links with `[TEAM INPUT REQUIRED]`; no URLs were invented.
- Recorded the existing presentation numbering and wording issue as `Needs correction` without modifying `PA1.pptx`.
- Rendered and inspected all 9 WeeklyReport pages. `npm run validate:pa1:draft` passes with 0 failed checks.
