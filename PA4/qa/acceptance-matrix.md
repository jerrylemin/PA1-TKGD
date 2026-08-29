# PA4 acceptance matrix

Status meanings: `PASS` means the local artifact or reproducible QA check is complete. `BLOCKED EXTERNALLY` means the remaining acceptance condition requires real study activity or a genuine external upload that is not present in this workspace. No blocked condition is represented by invented evidence.

| ID | Acceptance condition | Status | Evidence / blocker |
|---|---|---|---|
| AC01 | FIFA selected concept is carried forward as Alt 1 Status Dashboard | PASS | `work/pa3-continuity.md`; prototype dashboard shell |
| AC02 | Chess selected concept is carried forward as Alt 1 Beginner Review Flow | PASS | `work/pa3-continuity.md`; prototype review flow |
| AC03 | FIFA prototype has hi-fi visual fidelity and realistic content | PASS | `prototype/`; browser screenshots; hi-fi PDF |
| AC04 | Chess prototype has hi-fi visual fidelity and realistic content | PASS | `prototype/`; browser screenshots; hi-fi PDF |
| AC05 | FIFA supports the core status, action, refresh, error, and partner-boundary interactions | PASS | `qa/prototype-browser-qa.json` |
| AC06 | Chess supports review entry, explanation, better move, trial feedback, practice, and completion | PASS | `qa/prototype-browser-qa.json` |
| AC07 | Prototype states use coherent product-specific content and feedback | PASS | Browser QA screenshots and source prototype |
| AC08 | Desktop layouts are usable without horizontal overflow | PASS | Browser QA at 1440 x 900 |
| AC09 | Mobile layouts are usable without horizontal overflow | PASS | Browser QA at 390 x 844 |
| AC10 | PA1 -> PA2 -> PA3 -> PA4 traceability is documented | PASS | `evidence/pa3-pa4-traceability.csv` |
| AC11 | Summative study plan defines participants, tasks, measures, timing, and procedure | PASS | `study/study-plan.md` |
| AC12 | Facilitator script and interview guide are ready for execution | PASS | `study/facilitator-script.md`; `study/post-test-interview.md` |
| AC13 | Post-test questionnaire and structured data schemas are ready | PASS | `study/study-plan.md`; `study/data/*.csv` |
| AC14 | Group roles and evidence responsibilities are defined without claiming completion | PASS | `study/study-plan.md`; weekly report |
| AC15 | Deterministic analysis script and evidence gate are implemented | PASS | `study/analysis/analyze_study.py`; unit tests |
| AC16 | At least five real participants completed the study | BLOCKED EXTERNALLY | No real sessions or participant rows supplied |
| AC17 | Each completed session has a readable video recording | BLOCKED EXTERNALLY | `evidence/recordings/README.md`; no recordings supplied |
| AC18 | Real participant feedback and interview observations are collected | BLOCKED EXTERNALLY | Interview CSV is header-only |
| AC19 | Real task timings, outcomes, errors, and questionnaire responses are collected | BLOCKED EXTERNALLY | Task/questionnaire CSVs are header-only |
| AC20 | Summative analysis is populated from verified study evidence | BLOCKED EXTERNALLY | Current analysis status is evidence-gated as blocked |
| AC21 | Hi-fi PDF page 1 contains a genuine YouTube demo URL | BLOCKED EXTERNALLY | Page 1 contains an explicit upload gate, not a fabricated link |
| AC22 | Weekly report is prepared with scope, continuity, roles, and blockers | PASS | Weekly report PDF/DOCX |
| AC23 | Final reports are rendered and visually inspected | PASS | `qa/pdf-renders/`; selectable-text checks; report visual QA |
| AC24 | Final package contains exact deliverables and excludes QA caches/synthetic evidence | PASS | `scripts/package_pa4.py`; `final/Group10-PA4.zip` |

## Verification record

- Browser QA: 64 checks passed; no console errors.
- PDF rendering: all three PDFs rendered with the bundled Playwright browser and PDF.js renderer; every page was visually inspected for clipping and overflow.
- DOCX rendering: blocked because the required LibreOffice `soffice` executable is not installed; all three DOCX files passed structural open/paragraph/table checks.
- External gates are intentionally left visible in the reports and package rather than being filled with placeholder participant data, recordings, or links.
