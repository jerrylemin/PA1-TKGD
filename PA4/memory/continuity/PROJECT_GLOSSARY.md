# PA4 project glossary

Definitions below use the terms as they appear in PA4 artifacts, not generic dictionary meanings.

| Term | PA4 meaning | Source |
|---|---|---|
| Status Dashboard | FIFA PA2 concept F-A1, refined as the PA4 status-first ticket flow. | PA2/traceability-matrix.csv; PA4/prototype/app.js |
| Pending | Current FIFA state meaning that FIFA confirmation is still awaited; the owner and expected next update are shown. | PA4/prototype/app.js; PA4/evidence/pa3-pa4-traceability.csv |
| owner | The party responsible for the next status transition, shown beside the current status. | PA4/prototype/app.js |
| freshness | Source/update information used to communicate how current the displayed FIFA status is. | PA4/prototype/app.js; PA4/qa/acceptance-matrix.md |
| handoff | A transition from FIFA.com to an external partner that must show destination, context, and a return path first. | PA4/prototype/app.js; PA4/work/decision-log.md |
| Beginner Review | The PA4 Chess guided review route derived from PA2 C-A1 and PA3 Alt 1. | PA2/traceability-matrix.csv; PA4/prototype/app.js |
| mistake | The current single learning moment in the guided Chess review. | PA4/prototype/app.js; PA4/qa/chess-scenario-validation.md |
| better move | The suggested Chess move shown after the plain-language explanation. | PA4/prototype/app.js; PA4/evidence/pa3-pa4-traceability.csv |
| practice | The short follow-on activity that reinforces the current Chess idea and can return to review. | PA4/prototype/app.js; PA4/study/study-plan.md |
| trial | The recoverable Chess interaction where the participant tries the suggested idea and sees wrong/correct feedback. | PA4/prototype/app.js; PA4/qa/validate_chess_scenario.py |
| study mode | A direct participant route that hides the presenter/lab shell and researcher-only controls. | PA4/prototype/README.md; PA4/README.md |
| presenter mode | The demo route that retains the overview, lab shell, and navigation for the 15-20 minute presentation. | PA4/prototype/README.md; PA4/demo/DEMO-SCRIPT.md |
| success_score | The task-results field intended to record task outcome for a real participant; it is empty in the current template. | PA4/study/data/task-results.csv; PA4/study/analysis/analyze_study.py |
| hesitation_count | Separate task-results count for an observable pause of at least five seconds without task-progress action while the participant is attending; it does not lower success_score by itself and is empty in the current template. | PA4/study/study-plan.md; PA4/study/facilitator-script.md; PA4/study/analysis/analyze_study.py |
| condition_order | Required participant counterbalancing field: A_FIFA_FIRST or B_CHESS_FIRST. | PA4/study/data/participants.csv; PA4/study/analysis/analyze_study.py |
| recovery_outcome | Required task-results field describing whether the participant recovered after an error. | PA4/study/data/task-results.csv; PA4/study/analysis/analyze_study.py |
| VERIFIED_RECORDING | A consented recording that is an existing MP4 with positive duration and at least one `codec_type=video` stream from the available media probe. | PA4/evidence/recordings/README.md; PA4/study/analysis/analyze_study.py |
| RECORDING_INVALID_NO_VIDEO_STREAM | A present media file rejected because the probe found no video stream, including audio-only MP4. | PA4/evidence/recordings/README.md; PA4/study/analysis/analyze_study.py |
| RECORDING_PRESENT_UNVERIFIED | A present file that cannot be verified because no media probe is available or the probe could not run; it never counts as verified. | PA4/evidence/recordings/README.md; PA4/study/analysis/analyze_study.py |
| READY_FOR_REAL_PARTICIPANTS | Local prototype, study protocol, schemas, and QA gates are ready for genuine sessions; participant evidence is not yet present. | PA4/qa/remediation-acceptance-matrix.md |
| READY_FOR_FINAL_ANALYSIS | A future gate requiring the participant, recording, task, questionnaire, and interview evidence gates to pass. | PA4/study/analysis/analyze_study.py; PA4/study/analysis/analysis-report.md |
| SUBMISSION_READY | A final state that additionally requires external demo/template/evidence blockers to be resolved and package validation to pass. | PA4/work/external-blockers.md; PA4/scripts/package_pa4.py |
| BLOCKED_EXTERNALLY | A condition requiring genuine evidence or an external file not present in the authorized workspace. | PA4/work/external-blockers.md; PA4/qa/remediation-acceptance-matrix.md |

The terms success_score, condition_order, and recovery_outcome describe schemas and gates. They must not be populated with invented values.
