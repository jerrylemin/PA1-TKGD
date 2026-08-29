# PA4 final-submission acceptance

Audit date: 2026-08-24

Overall status: `BLOCKED_EXTERNALLY`

`SUBMISSION_READY` is not asserted. The local prototype/readiness state remains `READY_FOR_REAL_PARTICIPANTS`; the official package builder refused to create `PA4/final/Group10-PA4.zip` because required external evidence is absent.

| ID | Criterion | Status | Evidence |
|---|---|---|---|
| FAC01 | 5+ real participants validated | `BLOCKED_EXTERNALLY` | `participants.csv` is header-only with 0 rows. |
| FAC02 | Participant schema complete | `BLOCKED_EXTERNALLY` | Required headers exist, but no real participant records are present to validate. |
| FAC03 | Recordings verified as real video | `BLOCKED_EXTERNALLY` | Recordings directory contains only `README.md`; 0 media files are present. |
| FAC04 | Mandatory task evidence complete | `BLOCKED_EXTERNALLY` | `task-results.csv` is header-only with 0 rows. |
| FAC05 | Questionnaire complete | `BLOCKED_EXTERNALLY` | `questionnaire.csv` is header-only with 0 rows. |
| FAC06 | Interview evidence complete | `BLOCKED_EXTERNALLY` | `interview-coding.csv` is header-only with 0 rows. |
| FAC07 | `condition_order` valid | `BLOCKED_EXTERNALLY` | No participant records exist with `A_FIFA_FIRST` or `B_CHESS_FIRST`. |
| FAC08 | Analysis pipeline passes tests | `PASS` | `python PA4/study/analysis/test_analyze_study.py`: 15/15 passed; report-model tests: 3/3 passed. |
| FAC09 | Real analysis generated | `BLOCKED_EXTERNALLY` | Canonical analyzer result is `BLOCKED_PARTICIPANT_COUNT`; no real evidence exists. |
| FAC10 | Quantitative results trace to source data | `BLOCKED_EXTERNALLY` | There are no real task, timing, score, error, recovery, hesitation, or questionnaire rows. |
| FAC11 | Qualitative findings trace to source data | `BLOCKED_EXTERNALLY` | There are no interview-coding rows. |
| FAC12 | No synthetic evidence in final analysis | `PASS` | Real evidence tables remain empty; synthetic fixtures are confined to tests and no fixture rows enter PA4 evidence. |
| FAC13 | Summative report uses real results | `BLOCKED_EXTERNALLY` | Report correctly retains `BLOCKED_PARTICIPANT_COUNT` and does not claim participant findings. |
| FAC14 | Hi-fi report contains genuine demo URL | `BLOCKED_EXTERNALLY` | No genuine YouTube URL is present; page 1 retains the explicit external-evidence gate. |
| FAC15 | Weekly Report satisfies official template requirement | `BLOCKED_EXTERNALLY` | Official lecturer-provided template is not present; current report explicitly does not claim compliance. |
| FAC16 | DOCX/PDF substantive content synchronized | `PASS` | Shared report model tests pass 3/3; extracted DOCX/PDF states and required wording agree. |
| FAC17 | Hi-fi PDF QA passes | `PASS` | 5-page PDF rendered and visually/content validated. |
| FAC18 | Summative PDF QA passes | `PASS` | 4-page blocked-state PDF rendered and visually/content validated. |
| FAC19 | Weekly PDF QA passes | `PASS` | 1-page local-snapshot PDF rendered and visually/content validated. |
| FAC20 | Participant privacy review passes | `PASS` | No participant identities, contact details, consent details, recording paths, or participant media are present in final PDFs. |
| FAC21 | Official package gate passes | `BLOCKED_EXTERNALLY` | `python PA4/scripts/package_pa4.py` refused official package generation. |
| FAC22 | `Group10-PA4.zip` contains exact current deliverables | `BLOCKED_EXTERNALLY` | Official ZIP was not generated because FAC01-FAC07, FAC09-FAC11, FAC14-FAC15, and FAC21 remain blocked. |
| FAC23 | No fabricated evidence | `PASS` | Audit, analyzer, reports, and package gate preserve the missing-evidence blockers and add no participant findings. |
| FAC24 | Final state is `SUBMISSION_READY` | `BLOCKED_EXTERNALLY` | Required participant, recording, study-response, YouTube, and official-template evidence is missing. |

## Exact remaining blockers

1. At least five real anonymized participant records with complete metadata, consent, recording filename, and `condition_order`.
2. One verified positive-duration video recording for every participant.
3. Complete FIFA and Chess task evidence, questionnaire responses, and timestamped interview feedback.
4. Genuine YouTube hi-fi demo URL.
5. Official lecturer-provided Weekly Report template.

The working-evidence archive may be used for continuity, but it is not the official submission package.
