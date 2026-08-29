<!-- converted from Group10-PA4-SummativeUserStudy.docx -->

Group10 PA4 · Summative User Study
Study design, instruments, evidence gate, and analysis plan

# Study objective and research questions
Measure whether the selected hi-fi flows support effective, efficient, low-error, and satisfactory completion of the core tasks. The study evaluates interface behavior, not the participant.
- Can users identify FIFA status, ownership, and the next action without coaching?
- Can users recognize the partner boundary and return with context?
- Can users identify and explain the Chess mistake before advanced analysis?
- Can users perform a safer Chess move, recover from an incorrect trial, and complete related practice?
- What errors, pauses, wording problems, and recovery behaviors remain?
# Canonical analysis state
The report reflects the canonical analysis result: BLOCKED_PARTICIPANT_COUNT. It changes when evidence is ingested and the analyzer is rerun; no participant findings are inferred from empty or synthetic templates.


# Setup, roles, and order-neutral procedure
- Quiet room or call; desktop reference 1440 × 900 and mobile reference 390 × 844 where appropriate.
- Moderated concurrent think-aloud with descriptive task time; use neutral prompts only.
- Observer records first action, timestamps, errors, wrong paths, assistance, recovery, and hesitation.
- Recording begins after consent and is verified using the media rule below.
- Target session length is 25–35 minutes; stop for withdrawal, discomfort, recording failure, or coaching risk.
- Greeting, purpose, consent, and recording confirmation.
- Background questions and think-aloud practice.
- Run the first assigned product tasks, then that product's questionnaire.
- Reset the prototype.
- Run the second assigned product tasks, then that product's questionnaire.
- Neutral post-test interview, closing, and recording filename confirmation.
## Counterbalancing
- A_FIFA_FIRST: FIFA tasks → FIFA questionnaire → reset → Chess tasks → Chess questionnaire.
- B_CHESS_FIRST: Chess tasks → Chess questionnaire → reset → FIFA tasks → FIFA questionnaire.
# Tasks and measures

2 = independent completion without facilitator assistance; 1 = completion after one neutral prompt or a defined recoverable wrong path; 0 = failure, abandonment, or solution-revealing/direct assistance.
Track hesitation separately: one event is at least 5 consecutive seconds without task-progress action while the participant is visibly attending, excluding expected reading. Store hesitation_count, timestamp, and observable behavior; hesitation alone does not lower success_score.
# Questionnaire and interview
Use the custom five-item Likert questionnaire after each assigned product flow. Store raw 1–5 responses and do not replace missing answers. Ask the neutral interview questions in `PA4/study/post-test-interview.md` and create only timestamped, non-empty evidence-backed feedback rows.

# Recording and analysis rule
A verified recording is an existing MP4 with a positive duration and at least one codec_type=video stream. A present file without a probe is RECORDING_PRESENT_UNVERIFIED and never counts as verified.
# Limitations
- The prototype uses static fictional data and does not measure live service reliability or partner completion.
- Participant-dependent findings remain subject to the canonical analysis gates shown above.
- PA3 formative evidence is continuity evidence and is not substituted for PA4 human sessions.
- Concurrent think-aloud timings are descriptive and are not a natural unmoderated baseline.
# Evidence index


| STUDY STATUS
BLOCKED_PARTICIPANT_COUNT · No verified participant sessions. This report contains no inferred participant findings. |
| --- |
| Evidence item | Current state | Required before PASS |
| --- | --- | --- |
| Verified participants | No verified participant sessions | At least five verified, anonymized participant sessions |
| Recordings | No verified video recordings | One consented MP4 with positive duration and a video stream per session |
| Task results | No task rows (header-only template) | All assigned task rows with timestamps, 2/1/0 score, recovery, and hesitation fields |
| Questionnaire | No questionnaire rows (header-only template) | Five raw items per product and verified participant |
| Interview | No interview/feedback rows (header-only template) | At least one timestamped non-empty feedback row per verified participant |
| Gate | Name | Status |
| --- | --- | --- |
| G01 | participant count | BLOCKED_PARTICIPANT_COUNT |
| G02 | participant metadata completeness | BLOCKED_PARTICIPANT_METADATA |
| G03 | recording presence and validity | BLOCKED_RECORDINGS |
| G04 | task-result completeness | BLOCKED_TASK_DATA |
| G05 | questionnaire completeness | BLOCKED_QUESTIONNAIRE |
| G06 | interview/feedback completeness | BLOCKED_INTERVIEW_DATA |
| G07 | quantitative-analysis readiness | BLOCKED_EXTERNAL_EVIDENCE |
| G08 | final summative-report readiness | BLOCKED_EXTERNAL_EVIDENCE |
| Task | Success endpoint | Measures |
| --- | --- | --- |
| FIFA-T1 | Status, owner, timing, and next action explained | 2/1/0; time; errors; wrong paths; assistance; hesitation |
| FIFA-T2 | Order or ticket detail opened and interpreted | Same task measures |
| FIFA-T3 | Partner destination recognized before leaving | Same measures; boundary recognition |
| FIFA-T4 | Return restores status context | Same measures; orientation |
| CHESS-T1 | Beginner Review started independently | Same task measures |
| CHESS-T2 | Mistake and immediate consequence explained | Same measures; own-words explanation |
| CHESS-T3 | Safer move performed and feedback understood | Same measures; source-to-destination interaction; retry/recovery |
| CHESS-T4 | New practice position completed and context retained | Same measures; practice input and continuation |
| ID | Statement |
| --- | --- |
| Q1 | I could find the first useful action without help. |
| Q2 | The status or explanation was clear. |
| Q3 | I felt confident about what to do next. |
| Q4 | The feedback after my action was useful. |
| Q5 | I was satisfied with this flow. |
| Artifact | Purpose | State |
| --- | --- | --- |
| study-plan.md | Design, criteria, procedure, tasks, measures, privacy | Prepared |
| facilitator-script.md | Neutral moderated session script | Prepared |
| data/*.csv | Raw evidence capture schema | Header-only until real evidence is ingested |
| evidence/recordings/README.md | Recording convention and video verification rule | Prepared; no recordings claimed |
| study/analysis/ | Canonical gates, result, metrics, and synthetic-only tests | Generated from current evidence state |
| NEXT REQUIRED ACTION
Run the prepared study, verify consented video recordings and timestamped feedback, ingest real evidence, rerun the analyzer, and rebuild the reports before any submission package is generated. |
| --- |