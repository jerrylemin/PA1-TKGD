# Session Handoff

Date: 2026-07-13

## 2026-07-13 Group10 WeeklyReport rebuild

- Final files: `Group10-PA1-WeeklyReport.docx`, `Group10-PA1-WeeklyReport.pdf`, and `Group10-PA1-WeeklyReport-Review.md`.
- Rebuild WeeklyReport only with bundled Python: `python scripts/create_weekly_report.py`; rebuild the four-PDF package with `python build_pa1_package.py`.
- WeeklyReport is 9 A4 portrait pages. All pages were rendered and visually inspected; content, meeting-format, prohibited-term, table, header/footer, and ZIP checks passed.
- `Group10-PA1.zip` contains exactly the four Group10 PDFs. `npm run validate:pa1:draft` passes.
- Current team inputs: three Google Docs links, Google Drive README link, optional Zoom link, presentation correction, and real classroom peer feedback.
- Previous current artifacts with the old prefix were moved to `archive/pre_group10_artifacts_20260713/` with `legacy-` filenames.

## 2026-07-13 Teacher Feedback Response

- Current requested deliverables are complete at repo root: `Group10-PA1-PeerReview-Revised.docx`, `Group10-PA1-PeerReview-Revised.pdf`, and `Group10-PA1-PeerReview-Review.md`.
- Rebuild them with bundled Python: `python scripts/create_teacher_feedback_response.py`.
- The revised document is Vietnamese, A4 landscape, eight pages, and uses navy report headers/title bars.
- `PA1.pptx` is the content baseline. The document keeps the deck's three user groups, four use cases, benefits, drawbacks, and solutions for each website.
- Final checks passed: DOCX opens in Word, PDF renders at A4 landscape, all eight pages were visually inspected, required sections/markers are present, and legacy PeerReview preparation content is absent.
- Do not regenerate this deliverable through `build_pa1_package.py`; it is intentionally separate from the draft package and uses Group10 directly.
- English-only companion PDF: `Group10-PA1-PeerReview-Revised-English.pdf`; rebuild with `python scripts/create_teacher_feedback_response_english.py`.

## Latest document revision

- `Group10-PA1-PotentialSolutions_VisualReport (1).docx` is now the revised Potential Solutions report; the pre-revision file is backed up under `archive/potential_solutions_before_live_ui_revision_20260707/`.
- Mark-of-the-Web was removed from the two Group10 input DOCX files, so Word no longer opens them in Protected View. Protected View was not disabled globally.
- Ten live/reference captures are stored under `assets/screenshots/raw/` and `assets/screenshots/solution-references/`; reproducible capture and DOCX revision scripts are under `scripts/`.
- All illustrative redesign sketches were removed and replaced with explicit UI-location bullets linked to ProductResearch IDs. Chess evidence images now come only from live `chess.com` UI.
- LibreOffice 26.2.4.2 is installed; final QA render contains 20 pages under `output/potential_solutions_final_render/`.

Current state: READY DRAFT. The build and strict draft validator pass. Do not submit as final yet.

## Current artifacts

- Final draft ZIP: `GroupID-PA1.zip`.
- Root PDFs: ProductResearch, PotentialSolutions, PeerReview, and WeeklyReport.
- WorkDivision: root and `output/` copies.
- Root/output PDF and ZIP copies are regenerated; ZIP contains exactly four top-level PDFs.
- Current validation evidence: `docs/pa1_final_validation_report.md`.

## Remaining blockers

1. Replace `config/pa1_config.json` `group_id` with the real course group ID.
2. After the lecture presentation, replace the pending PeerReview table with real commenter name, feedback/question, group response, revision action, owner, and status. Remove internal/mock wording from the final PeerReview only after real data is used.
3. Replace TODO Google Docs/Drive/Zoom links when the real URLs are available.

## Required next-session sequence

1. Update config and real peer data in the generator/source of truth; do not hand-edit binary files.
2. Run `npm run build:pa1`.
3. Run `npm run validate:pa1:draft`.
4. Run `npm run validate:pa1:final`; it must exit 0 before Moodle submission.
5. Confirm the renamed ZIP contains exactly the four renamed PDFs and no WorkDivision DOCX.
6. If LibreOffice becomes available, render and visually inspect the final WorkDivision DOCX.

Do not restore historical `READY 10/10` claims. They are marked superseded because they predate the strict authenticity gates.
