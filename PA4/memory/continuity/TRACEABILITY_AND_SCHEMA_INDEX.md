# PA4 traceability and schema index

This adapter exists because Graphify 0.8.18 detects code, Markdown, PDFs, DOCX sidecars, and images but does not classify CSV files as graph inputs. It records the CSV structures and the current empty-data state without copying participant values.

## PA3 to PA4 traceability

Source: PA4/evidence/pa3-pa4-traceability.csv

| Product | PA2 evidence | PA3 improvement | PA4 element | Study task | Local validation |
|---|---|---|---|---|---|
| FIFA | F2-E09; ticket status clarity | F-IMP-01/F-IMP-02 | Current Status card with Pending definition, owner, timing | FIFA-T1 | IMPLEMENTED - browser QA |
| FIFA | F2-E09; direct ticket actions | F-IMP-03 | Common Actions beside event list | FIFA-T2 | IMPLEMENTED - browser QA |
| FIFA | F2-E09/F2-E10/F2-E11; handoff trust | F-IMP-04 | Before you leave FIFA.com guardrail | FIFA-T3/FIFA-T4 | IMPLEMENTED - browser QA |
| FIFA | F2-E02/F2-E03/F2-E04; mobile overview | F-IMP-08 | Responsive status and action layout | FIFA-T1/FIFA-T4 | IMPLEMENTED - browser QA |
| Chess | C2-E10; analysis recall demand | C-IMP-02 | Start Beginner Review intro | CHESS-T1 | IMPLEMENTED - browser QA |
| Chess | C2-E08/C2-E10; beginner bridge | C-IMP-01 | Mistake and Why this matters explanation | CHESS-T2 | IMPLEMENTED - browser QA |
| Chess | C2-E05/C2-E07/C2-E10; practice continuation | C-IMP-03 | Practice this idea card | CHESS-T4 | IMPLEMENTED - browser QA |
| Chess | C2-E10; recoverable experimentation | C-IMP-04 | Trial board with wrong/correct feedback | CHESS-T3 | IMPLEMENTED - browser QA + scenario validation |
| Chess | C2-E10; advanced detail load | C-IMP-08 | Three-step, one-mistake rail | CHESS-T2/CHESS-T4 | IMPLEMENTED - browser QA |

The validation labels above describe local implementation/QA state only. They do not claim participant performance.

## Study input schemas

Source: PA4/study/data/participants.csv

The participant schema fields are: participant_id, date, target_profile_match, device, prior_fifa_experience, prior_chess_experience, recording_file, consent_confirmed, condition_order.

Current data state: header-only; zero participant rows.

Source: PA4/study/data/task-results.csv

The task schema fields are: participant_id, product, task_id, task_start, task_end, duration_seconds, success_score, errors, wrong_paths, assistance_count, hesitation_count, recovery_outcome, notes, recording_timestamp_reference. `hesitation_count` is separate from `success_score` and uses the five-second observable-pause definition in the protocol.

Current data state: header-only; zero task rows.

Source: PA4/study/data/questionnaire.csv

The questionnaire schema fields are: participant_id, product, flow, question_id, question_text, response_1_to_5, notes.

Current data state: header-only; zero questionnaire rows.

Source: PA4/study/data/interview-coding.csv

The interview schema fields are: participant_id, product, theme, observation, severity, supporting_timestamp, design_implication.

Current data state: header-only; zero interview rows.

## Generated analysis schemas

Source: PA4/study/analysis/analyze_study.py

The analyzer writes independent participant, metadata, recording, task, questionnaire, interview, and report gates. Current generated outputs report zero verified participants and BLOCKED statuses rather than fabricating metrics. Recording verification requires a video stream; the report builder consumes the same canonical result through a shared substantive model for DOCX and PDF.

Sources:

- PA4/study/analysis/analysis-result.json
- PA4/study/analysis/analysis-report.md
- PA4/study/analysis/summary.csv
- PA4/study/analysis/task-metrics.csv
- PA4/study/analysis/questionnaire-summary.csv

## Evidence boundary

Synthetic rows used inside PA4/study/analysis/test_analyze_study.py are test fixtures only. They are not present in PA4/study/data and must never be described as real study evidence.

## Graph adapters and generated-artifact links

Graphify 0.8.18 does not auto-classify CSV files. The traceability rows, schema field lists, and zero-row states above are therefore a deterministic memory adapter; they do not copy participant values into the graph.

The graph also contains source-backed navigation aliases for the exact status tokens used by the validation plan: `READY_FOR_REAL_PARTICIPANTS?`, `SUBMISSION_READY?`, `VERIFIED_RECORDING?`, `package?`, and `generated`. Each alias points to a canonical node or source script and is marked `INFERRED`; it is not evidence.

The report pipeline is represented as generated-artifact provenance: `scripts/build_pa4_reports.py` generates the three final report PDFs, and the three source DOCX reports are linked to their final PDFs with `renders_to` edges. These links describe the local build pipeline, not participant findings.
