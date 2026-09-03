# Group10 PA4 summative user study plan

Status: study materials prepared; participant evidence is `BLOCKED EXTERNALLY` until real sessions are run.

## 1. Research questions

1. Can target users determine a FIFA ticket’s current state, ownership, and next action without coaching?
2. Can target users recognize an external partner boundary and return to the FIFA context without losing orientation?
3. Can beginner or returning Chess.com users scan the available key moments, choose what to review first, and explain that moment in their own words?
4. Can users optionally move from a selected Chess card into a safer-move trial or related practice activity and return to the dashboard?
5. What errors, pauses, wording problems, and recovery behaviors remain in the hi-fi flows?

## 2. Evaluation expectations

These are evaluation expectations, not results:

- The status-first FIFA hierarchy should make current state and next-step ownership easier to identify than a distributed ticket-entry surface.
- The FIFA handoff preview should reduce mistaken assumptions about the external destination and make return orientation explicit.
- The user-controlled Chess card dashboard should make key moments easy to scan while preserving meaningful choice over what to review first.
- The optional Chess trial and practice bridges should make the next learning action feel related to the selected explanation rather than a forced sequence or separate destination.

## 3. Participant criteria

Recruit at least five real participants, anonymized as `P01` through `P05` or more. Participants should be adults or students who use a web browser regularly and can understand the task instructions in the study language.

Target profile coverage:

- FIFA: low-to-medium familiarity with tournament ticket planning; no requirement to have used a real FIFA ticket account.
- Chess: beginner or returning player; no requirement to use engine analysis regularly.
- Digital ability: medium or above, with any accessibility needs recorded without storing unnecessary personal data.

The preferred design is a within-subject session in which each participant tests both flows. If recruitment produces two materially different target groups, recruit the smallest evidence-supported split and report the split instead of pooling incompatible results.

## 4. Recruitment plan

Recruit through the team’s course network. Provide a plain-language invitation that states the session length, screen/video recording, fictional prototype content, voluntary participation, anonymized reporting, and the right to stop. Do not recruit the Group10 members as study participants. Do not promise a grade benefit.

## 5. Study environment

- Quiet room or video-call setup with minimal interruption.
- One laptop or desktop browser for the primary run; one mobile browser run may be added if the participant normally uses mobile.
- Browser window at 1440 x 900 for desktop or 390 x 844 for mobile where practical.
- Fresh prototype state before every task.
- Facilitator screen recording plus participant interaction audio/video only after consent.
- Observer records timestamps, first action, wrong paths, assistance, and notable hesitation without interpreting during the task.
- Method: `MODERATED CONCURRENT THINK-ALOUD WITH DESCRIPTIVE TASK TIME`. Participants verbalize while completing tasks; task duration is still captured, but verbalization and neutral prompts can affect it.

## 6. Roles

All four members have assigned PA4 work. These assignments describe ownership, not completed participant evidence.

| member | primary_role | secondary_role | study_session_responsibility | artifact_responsibility | evidence_responsibility |
|---|---|---|---|---|---|
| Le Minh | Facilitator | Analysis owner | Read the neutral script, confirm consent, assign the recorded condition order, keep prompts neutral, and control resets. | Integrate PA4 continuity, final reports, and package checklist. | Run the independent analysis gates after evidence ingestion and report blockers without inferring results. |
| Nguyen Vu Bach | Recording operator | FIFA observer | Set up and verify the consented recording, operate the filename check, and observe FIFA status/handoff behavior without coaching. | Maintain FIFA status-dashboard copy and handoff traceability. | Confirm each session file is readable/verified and that FIFA observations retain timestamps. |
| Pham Nguyen Gia Bao | Prototype operator | Chess observer | Reset and operate the assigned prototype flow, observe card choice, explanation, and recovery behavior, and record no-answer coaching. | Maintain Chess scenario/task wording and Card Review continuity. | Check Chess task rows, choice behavior, and recovery outcomes against the session record. |
| Trang Minh Nhut | Data recorder | QA reviewer | Record task start/end, success score, errors, wrong paths, assistance, recovery outcome, questionnaire answers, and interview timestamps. | Maintain CSV schemas, browser QA, and report consistency review. | Validate row completeness, duplicate detection, and acceptance-matrix status. |

Required ownership is explicit: Le Minh owns facilitation and analysis; Nguyen Vu Bach owns recording integrity; Trang Minh Nhut owns data integrity; and Pham Nguyen Gia Bao owns the Chess prototype/task surface. Work remains `Assigned` or `In Progress` until the team confirms completion.

## 7. Recording setup and consent

Before the first task, explain what is recorded, where it is stored, who can access it, how long it is retained for the assignment, and that the participant can stop. Obtain explicit consent before recording. Use anonymized IDs in filenames and CSVs. Do not store full names, account passwords, or unrelated personal data. A session is not verified until the corresponding recording exists, has a positive duration, and contains a video stream.

## 8. Procedure

1. Greeting and consent (3 minutes).
2. Confirm recording and ask background questions (2 minutes).
3. Brief think-aloud practice unrelated to the prototype (1 minute).
4. Run the assigned first product tasks one at a time (6–8 minutes). The participant thinks aloud concurrently; the facilitator records descriptive task time from task marker to the defined endpoint.
5. Run the questionnaire for the first assigned product (1 minute).
6. Reset, then run the assigned second product tasks one at a time (7–9 minutes), using the same concurrent think-aloud and descriptive timing protocol.
7. Run the questionnaire for the second assigned product (1 minute).
8. Ask neutral post-test interview questions (5–7 minutes).
9. Close, confirm the recording filename, and thank the participant (1 minute).

Target session length: 25–35 minutes. Stop if the participant requests it, recording fails and cannot be restored, the participant becomes uncomfortable, or the facilitator would need to coach completion.

## 9. Counterbalancing and order

Use two orders when at least five participants are available:

- `A_FIFA_FIRST`: FIFA then Chess.
- `B_CHESS_FIRST`: Chess then FIFA.

Assign alternating orders by participant ID and store the value structurally in `participants.csv` under `condition_order`. Do not rely on free-text notes for the assignment. Keep task wording and starting state identical. Within each product, keep the required task order because later tasks depend on the earlier context.

## 10. Tasks and success criteria

### FIFA tasks

| ID | Instruction | Independent success |
|---|---|---|
| FIFA-T1 | Determine the overall ticket situation, then explain what needs to happen next for one event. | Participant uses the account counts, identifies Pending/Confirmed, explains the chosen event state, names the owner, and states whether action is required. |
| FIFA-T2 | Find the relevant order or ticket detail from the dashboard. | Participant opens View Order or View Tickets and identifies the event and status. |
| FIFA-T3 | Start the transfer action and identify the destination before leaving FIFA. | Participant opens the handoff preview and names the partner/destination before choosing Continue or Stay. |
| FIFA-T4 | Return to the FIFA prototype and re-establish the current status context. | Participant returns and identifies that context is preserved and partner completion is not inferred. |

### Chess tasks

| ID | Instruction | Independent success |
|---|---|---|
| CHESS-T1 | Scan the available key moments and choose what you want to review first. | Participant notices the summary and four cards, names a reason for the choice, and selects any card without facilitator direction. |
| CHESS-T2 | Open the chosen moment and explain what happened and why it matters in your own words. | Participant uses the selected-card explanation and identifies the relevant idea or consequence. |
| CHESS-T3 | From a relevant selected moment, find or try a safer move. | Participant reveals the optional alternative, performs a source-to-destination move, and understands the feedback; an incorrect attempt is recorded as recovery behavior, not hidden. |
| CHESS-T4 | Find the related optional practice activity, enter or complete it, and return to the card dashboard. | Participant recognizes that practice is optional, selects a source and destination, retries after an error if needed, and returns without losing the selected review context. |

## 11. Measures and scoring

Record one row per participant × product × task in `study/data/task-results.csv`.

- Success score: `2` = independent success without facilitator assistance; `1` = success after one neutral prompt or a defined recoverable wrong path; `0` = failure, abandonment, or solution-revealing/direct assistance.
- Duration: seconds from the facilitator’s task-start marker to the first stable success/failure endpoint. Because this is moderated concurrent think-aloud, duration is descriptive for within-study comparison only; it is not natural unmoderated performance and must not be compared with an unrelated current-practice timing baseline.
- Errors: observable incorrect actions or statements relevant to the task.
- Wrong paths: detours that do not directly support the task.
- Assistance count: number of neutral prompts; coaching is not permitted.
- Recovery outcome: one of `NOT_NEEDED`, `RECOVERED_INDEPENDENTLY`, `RECOVERED_WITH_ASSISTANCE`, or `NOT_RECOVERED` describing whether the user returns to the intended task path.
- Hesitation is separate from success score. Record `hesitation_count` for observable events only: no task-progress action for at least 5 consecutive seconds while the participant is visibly attending to the task, excluding expected reading of substantial explanatory content. Add a timestamp and observable behavior in `notes`; do not infer personality or reduce the score for hesitation alone.

Do not change the scoring scale after data collection without recording the protocol version and reason.

## 12. Questionnaire

Use the custom five-item Likert questionnaire, not SUS. Ask after each product flow. Scale: `1 Strongly disagree`, `2 Disagree`, `3 Neither agree nor disagree`, `4 Agree`, `5 Strongly agree`.

1. I could find the first useful action without help.
2. The status or explanation was clear.
3. I felt confident about what to do next.
4. The feedback after my action was useful.
5. I was satisfied with this flow.

Store raw answers in `study/data/questionnaire.csv`. Do not replace missing answers with a neutral score.

## 13. Interview questions

Use `post-test-interview.md` after both flows. Ask in neutral language and record the participant’s words or an accurate paraphrase with a timestamp.

## 14. Data schema

- `participants.csv`: anonymized profile, device, consent, verified recording filename, and structural `condition_order` (`A_FIFA_FIRST` or `B_CHESS_FIRST`).
- `task-results.csv`: task timing, success, errors, wrong paths, assistance, `recovery_outcome`, notes, and recording timestamp.
- `questionnaire.csv`: raw 1–5 answers and optional notes.
- `interview-coding.csv`: post-test theme coding with timestamp and design implication.

Raw recordings remain immutable. Do not copy participant names into report text. Do not place synthetic rows in the real evidence folders.

## 15. Analysis method

Run `python PA4/study/analysis/analyze_study.py` after evidence ingestion. The script reports independent gates for participant count, participant metadata, recording validity, task completeness, questionnaire completeness, interview/feedback completeness, quantitative readiness, and report readiness. It verifies positive-duration media with `ffprobe` and requires a `codec_type=video` stream when the probe is available, classifies present-but-unverified media as not verified, requires every assigned task/questionnaire item/feedback record for each verified participant, and keeps all missing data visible.

With five participants, report individual rows plus descriptive aggregates only. Do not claim statistical significance. If no baseline uses comparable task start/end criteria, state: `No controlled current-practice timing baseline was collected.`

## 16. Stop criteria and privacy

Stop a session if consent is withdrawn, the participant is distressed, recording is not functioning, or the facilitator would need to coach. Delete a participant’s data only through the team’s agreed retention process; keep the audit trail of deletion without the personal content. Store files in the assignment workspace with access limited to the team and teaching staff as required.

## 17. Evidence checklist

- [ ] P01–P05 or more are real and anonymized.
- [ ] Every participant has a consent confirmation.
- [ ] Every participant has a verified recording file named by convention.
- [ ] Every task has start/end markers or a documented missing-time reason.
- [ ] Every questionnaire answer is raw and traceable.
- [ ] Every interview code has a supporting timestamp or is marked missing.
- [ ] No synthetic rows are mixed with real evidence.
- [ ] Analysis output was generated after the final evidence audit.
- [ ] Report results remain `BLOCKED EXTERNALLY` until all minimum evidence is verified.
