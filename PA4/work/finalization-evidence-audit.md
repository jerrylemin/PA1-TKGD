# PA4 finalization evidence audit

Audit date: 2026-08-24

## Source and protocol authority

- `PA4/study/study-plan.md` is the authority for the minimum five-participant design, the two recorded counterbalanced orders, the four FIFA tasks, the four Chess tasks, the custom five-item questionnaire per product, and timestamped post-test feedback.
- `PA4/study/data/*.csv` contains the current evidence tables.
- `PA4/evidence/recordings/README.md` defines the verified-media rule: positive duration and at least one video stream; no placeholder or renamed text files are accepted.
- `PA4/study/analysis/analyze_study.py` is the canonical gate and analysis pipeline.

## Audit results

| Gate | Result | Evidence |
|---|---|---|
| Participants | `BLOCKED_PARTICIPANT_COUNT` | `participants.csv` has headers only: 0 rows and 0 unique participant IDs. No participant schema, duplicate, consent, or `condition_order` record can be validated. |
| Recordings | `BLOCKED_RECORDINGS` | `PA4/evidence/recordings/` contains only `README.md`; there are 0 media files and no participant recordings to pass the media validator. |
| Task evidence | `BLOCKED_TASK_DATA` | `task-results.csv` has headers only: 0 task rows and no mandatory task evidence for any verified participant. |
| Questionnaire | `BLOCKED_QUESTIONNAIRE` | `questionnaire.csv` has headers only: 0 responses and no required five-item product coverage. |
| Interview evidence | `BLOCKED_INTERVIEW_DATA` | `interview-coding.csv` has headers only: 0 timestamped post-test feedback rows. |
| Counterbalancing | `BLOCKED_PARTICIPANT_COUNT` | No participant records contain `A_FIFA_FIRST` or `B_CHESS_FIRST`; no balance or session order is claimed. |
| YouTube demo URL | `YOUTUBE_BLOCKED` | No genuine `youtube.com` or `youtu.be` URL is present in the current PA4 sources; the hi-fi report retains only the explicit external-evidence gate. |
| Weekly Report template | `WEEKLY_TEMPLATE_BLOCKED` | No lecturer-provided official template is present in the workspace. The current Weekly Report is explicitly a local snapshot and does not claim official-template compliance. |

## Analysis readiness

The evidence set is not complete, so real summative analysis, evidence-backed findings, and final evidence-populated report regeneration are not authorized by the task contract. The current canonical analysis state remains `BLOCKED_PARTICIPANT_COUNT`, with G01-G06 blocked by missing study evidence and G07-G08 blocked as external evidence dependencies.

No participant findings, timings, scores, errors, recovery outcomes, questionnaire answers, interview themes, baseline comparison, or YouTube URL are inferred or fabricated. The current readiness state is `READY_FOR_REAL_PARTICIPANTS`; `SUBMISSION_READY` is not asserted.

## Exact external blockers

1. At least five real, anonymized participant records with complete consent, metadata, recording filename, and structural `condition_order`.
2. One verified positive-duration video recording for every real participant.
3. Complete mandatory FIFA and Chess task rows with traceable timing and observation fields.
4. Complete raw questionnaire responses for both product flows.
5. Timestamped post-test interview/feedback evidence for every participant.
6. A genuine supplied YouTube demo URL.
7. The official lecturer-provided Weekly Report template.
