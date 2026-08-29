# PA4 decision chains

These chains preserve verified continuity without turning inference into history. Each link points to a source path.

## FIFA-STATUS-CHAIN

Problem: PA1 ticket discovery was distributed and did not provide a consolidated, trusted status view.

Original evidence: PA2 F2-E09 shows tournament-based ticket entry without a consolidated status dashboard.

PA2 interpretation: Ticket status clarity and safe next action are represented by UR-F01, use cases F-UC02/F-UC03, and selected concept F-A1 Status Dashboard.

PA3 concept: FIFA Alt 1 Status Dashboard was selected.

PA3 test result: The selected flow showed strong status-first scanning but left Pending meaning, direct actions, and handoff recognition under-specified in formative review.

PA3 improvement: F-IMP-01, F-IMP-02, F-IMP-03, F-IMP-04, F-IMP-08.

PA4 implementation: Status card, event actions, freshness/source cues, and handoff guardrail in PA4/prototype/app.js and PA4/prototype/index.html.

PA4 QA: FIFA browser checks and traceability status in PA4/qa/prototype-browser-qa.json, PA4/qa/acceptance-matrix.md, and PA4/evidence/pa3-pa4-traceability.csv.

PA4 study task: FIFA-T1 and FIFA-T2 in PA4/evidence/pa3-pa4-traceability.csv; study procedure in PA4/study/study-plan.md.

Current status: Local implementation is validated for real-participant handoff; summative evidence is not present.

Source:

- PA1/sources/Group10-PA1-ProductResearch.md
- PA2/evidence-index.csv
- PA2/traceability-matrix.csv
- PA3/submission-final/source-evidence/formative-testing-results.md
- PA4/evidence/pa3-pa4-traceability.csv
- PA4/prototype/app.js
- PA4/qa/prototype-browser-qa.json

## FIFA-HANDOFF-CHAIN

Problem: Leaving FIFA context without partner identity, destination, or return context weakens trust.

Original evidence: PA2 F2-E09, F2-E10, and F2-E11; evidence descriptions in PA2/evidence-index.csv.

PA2 interpretation: Handoff trust is UR-F02 with use cases F-UC04/F-UC05/F-UC06.

PA3 concept: FIFA Alt 1 Status Dashboard.

PA3 test result: Formative review found no visible pre-leave message explaining the external service or return path.

PA3 improvement: F-IMP-04.

PA4 implementation: Before-you-leave modal and partner boundary in PA4/prototype/app.js; traceability row in PA4/evidence/pa3-pa4-traceability.csv.

PA4 QA: Handoff and return behavior in PA4/qa/prototype-browser-qa.json and PA4/qa/remediation-acceptance-matrix.md.

PA4 study task: FIFA-T3/FIFA-T4.

Current status: Browser QA is marked implemented; no participant result is claimed.

Source:

- PA2/evidence-index.csv
- PA2/traceability-matrix.csv
- PA3/submission-final/source-evidence/formative-testing-results.md
- PA4/prototype/app.js
- PA4/qa/prototype-browser-qa.json

## CHESS-BEGINNER-CHAIN

Problem: Chess analysis entry exposes too many paths and vocabulary before a beginner can identify a useful first step.

Original evidence: PA2 C2-E10 and related evidence in PA2/evidence-index.csv.

PA2 interpretation: Entry-choice overload is UR-C01, use cases C-UC01/C-UC02, selected concept C-A1 Beginner Review Preset.

PA3 concept: Chess Alt 1 Beginner Review Flow.

PA3 test result: The guided sequence was strongest, but the start cue, notation load, try result, and help route needed improvement.

PA3 improvement: C-IMP-01, C-IMP-02, C-IMP-04, C-IMP-08.

PA4 implementation: Start state, one-mistake rail, explanation, better move, trial feedback, and glossary in PA4/prototype/app.js and PA4/prototype/index.html.

PA4 QA: Deterministic scenario and browser QA in PA4/qa/validate_chess_scenario.py, PA4/qa/chess-scenario-validation.md, and PA4/qa/prototype-browser-qa.json.

PA4 study task: CHESS-T1, CHESS-T2, and CHESS-T3 in PA4/evidence/pa3-pa4-traceability.csv.

Current status: Local interaction is marked implemented; no human learning outcome is claimed.

Source:

- PA2/evidence-index.csv
- PA2/traceability-matrix.csv
- PA3/submission-final/source-evidence/formative-testing-results.md
- PA4/evidence/pa3-pa4-traceability.csv
- PA4/prototype/app.js
- PA4/qa/validate_chess_scenario.py

## CHESS-PRACTICE-CHAIN

Problem: Practice existed as a related capability but was not reliably connected to review.

Original evidence: PA2 C2-E05, C2-E07, and C2-E10.

PA2 interpretation: Practice continuation is UR-C03 and use case C-UC06.

PA3 concept: Chess Alt 1 Beginner Review Flow.

PA3 test result: The mistake-to-explanation-to-practice chain was a strength but needed persistent continuity and visible recovery.

PA3 improvement: C-IMP-03 and C-IMP-04.

PA4 implementation: Practice card, trial/retry state, and return route in PA4/prototype/app.js; traceability in PA4/evidence/pa3-pa4-traceability.csv.

PA4 QA: Practice and recovery checks in PA4/qa/prototype-browser-qa.json, PA4/qa/chess-scenario-validation.md, and PA4/qa/remediation-acceptance-matrix.md.

PA4 study task: CHESS-T3 and CHESS-T4.

Current status: Local flow is ready for real participant testing; participant evidence is absent.

Source:

- PA2/evidence-index.csv
- PA3/submission-final/source-evidence/formative-testing-results.md
- PA4/evidence/pa3-pa4-traceability.csv
- PA4/prototype/app.js
- PA4/qa/prototype-browser-qa.json

## STUDY-VALIDITY-CHAIN

Problem: The study requires real participants and recorded sessions, while the current workspace contains only empty schemas.

Original evidence: PA4 brief requirements and current data folders.

PA2 interpretation: Not applicable; this is a PA4 execution/evidence gate.

PA3 concept: Not applicable; formative evidence is explicitly separate from summative evidence.

PA3 test result: Not applicable.

PA3 improvement: Not applicable.

PA4 implementation: Study plan, facilitator script, schemas, conservative analyzer, and recording policy in PA4/study, PA4/evidence/recordings, and PA4/study/analysis.

PA4 QA: Independent gates and fake-media rejection are documented in PA4/study/analysis/test_analyze_study.py and PA4/qa/remediation-acceptance-matrix.md.

PA4 study task: All required participant tasks are defined in PA4/study/study-plan.md.

Current status: READY_FOR_REAL_PARTICIPANTS; real sessions, recordings, and outcomes remain BLOCKED_EXTERNALLY.

Source:

- PA4/PA4-LKDuy-2026-Public.pdf
- PA4/study/study-plan.md
- PA4/study/analysis/analyze_study.py
- PA4/study/analysis/analysis-report.md
- PA4/work/external-blockers.md

## REPORTING-CHAIN

Problem: Reports and packages must stay synchronized with the current implementation and must not present blocked evidence as completed.

Original evidence: Official PA4 brief in PA4/PA4-LKDuy-2026-Public.pdf.

PA2 interpretation: Prior report continuity is represented through PA2 selected concepts and use cases in PA2/traceability-matrix.csv.

PA3 concept: Selected directions and formative improvements are carried into PA4.

PA3 test result: The report must distinguish formative AI-agent evidence from summative human evidence.

PA3 improvement: Preserve explicit traceability and external blockers.

PA4 implementation: PA4/scripts/build_pa4_reports.py generates editable DOCX and PDF outputs.

PA4 QA: Report/package checks in PA4/qa/remediation-acceptance-matrix.md, PA4/qa/pdf-renders/render-manifest.json, and PA4/scripts/package_pa4.py.

PA4 study task: Summative methodology and evidence gate in PA4/study/study-plan.md.

Current status: Local report artifacts exist; official template, YouTube URL, and real participant evidence remain external blockers.

Source:

- PA4/PA4-LKDuy-2026-Public.pdf
- PA4/scripts/build_pa4_reports.py
- PA4/scripts/package_pa4.py
- PA4/qa/remediation-acceptance-matrix.md
- PA4/work/external-blockers.md
