# Group10 PA3 Final-Submission Audit

Audit date: 2026-08-18  
Authority: `PA3-LKDuy-2026-Public.pdf`, then approved PA3 assets and the independent R1-R5 records.

## Official rubric

The brief defines Requirement 1 Paper Prototype / Storyboarding (45%), Requirement 2 Formative Testing (45%), Requirement 3 Peer Review (5%), and Requirement 4 Weekly Report (5%). It requires two scenarios with three alternatives each, a YouTube demonstration for every paper prototype, a testing plan/results/evaluation/improvement report with an improved-prototype demo link, a 5–10 minute peer presentation with commenter feedback and group responses, member task tracking, four named PDFs, and `Group10-PA3.zip`.

## Current authoritative evidence

- Official brief: `PA3/PA3-LKDuy-2026-Public.pdf`.
- Approved Requirement 1 images: six PNGs in `PA3/paper prototypes/slides-src/assets/prototypes/`.
- Requirement 2 plan/results: `testing-plan.md`, repaired `formative-testing-results.md`, and `ai-testing/R1.md` through `R5.md`.
- Original editable deck: `paper prototypes/Group10-PA3-PaperPrototypes.pptx`, 42 native slides; source `slides-src/export_native.mjs`.
- Improved editable deck: `improved-prototypes/Group10-PA3-ImprovedLoFi.pptx` with two native wireframes and rendered PNGs.
- Rebuilt editable reports: four DOCX files in `PA3/final/`.
- Final-ready local package: `PA3/submission-final/`.

## Requirement 1 status

Local content is complete: six alternatives retain the approved images, problem/motivation/solution, strengths/weaknesses, and explicit storyboards. The Paper Prototype report acknowledges the later R2 selection result without changing the approved design space.

Hard external blocker: no verified YouTube URL for any of the six original prototypes was found. Reports state this truthfully; no fake URL or placeholder is used.

## Requirement 2 status

PASS for the authorized AI-Agent Formative Testing evidence. Five independent AI reviewers evaluated six alternatives using 19 tasks each: 285 outcomes total, comprising 190 Independent Success, 56 Success With Hesitation, and 39 Failure.

Aggregate counts (Independent / Hesitation / Failure):

- FIFA Alt 1 = 31 / 11 / 8; Alt 2 = 26 / 9 / 15; Alt 3 = 37 / 3 / 10.
- Chess Alt 1 = 36 / 8 / 1; Alt 2 = 34 / 11 / 0; Alt 3 = 26 / 14 / 5.

Selected directions: FIFA Alt 1 Status Dashboard and Chess Alt 1 Beginner Review Flow. Selection uses task outcomes, recurring issues, severity/recurrence, comprehension, next-step clarity, trust or practice continuity, preference, and revision effort. Preference alone is not used as a winner rule.

Improved evidence is complete locally. FIFA F-IMP-01…08 and Chess C-IMP-01…08 are documented in the Formative Testing report and rendered in the improved native wireframes.

Hard external blocker: no verified improved-prototype YouTube demo URL was found.

## Peer Review status

HARD EXTERNAL BLOCKER. No verified PA3 lecture/class peer-review record, commenter identity, feedback/question, or group response was found. `Group10-PA3-PeerReview.docx` and its capture PDF are clearly marked as a capture structure and are not substituted for actual evidence. AI reviewer IDs are not peer-review commenter evidence.

## Weekly Report status

PASS locally. The report is titled `Group10-PA3 Weekly Report` and tracks assigned responsibility, current artifact state, verification state, external gates, QA, and handoff. It does not invent meetings, attendance, or feedback.

## Encoding and PPTX consistency

- Repaired the repeated quotation/dash/arrow mojibake in `formative-testing-results.md`; independent R1-R5 source records were preserved.
- Slides 19–42 now disclose AI-Agent Formative Testing and use reviewer terminology consistently.
- Slides 21–23 use reviewer setup/isolation language, reviewer IDs, and reviewer expectations.
- Slide 40 states `Decision matrix · Select the strongest PA4 direction.`
- Slide 42 states the completed five-reviewer, six-prototype, 285-outcome evaluation and selected directions.
- Native deck render/test passed with no overflow; no Python PPTX mutation was used.

## QA results

- Native deck rebuilt with artifact-tool: 42 slides.
- Native deck rendered and inspected; `slides_test.py`: passed, no overflow detected.
- Official PDFs generated with selectable text: Paper Prototype (8 pages), Formative Testing (10 pages), Weekly Report (3 pages), Peer Review capture (1 page).
- PDF pages rasterized with Poppler and contact sheets visually inspected; no visible overflow or placeholder leakage found.
- DOCX files are retained as editable sources. The bundled DOCX renderer could not launch LibreOffice on this Windows image; Microsoft Word export stalled on the dense Formative DOCX, so official PDFs were generated directly from the same report data with ReportLab and independently validated.

## Submission package status

Locally complete except the three external blockers. `submission-final/` contains three official PDFs, four editable DOCX sources including the clearly marked Peer Review capture, the original and improved editable PPTX files, improved PNGs, source evidence, `RUBRIC-CHECK.md`, and this audit.

The final-ready ZIP intentionally excludes `Group10-PA3-PeerReview.pdf` while Requirement 3 evidence is absent. The capture PDF is retained under `PA3/qa/peer-review-capture/`. The package must not be labelled full-score-ready until the external URLs and actual peer-review evidence are added.
