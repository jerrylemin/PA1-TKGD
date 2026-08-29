# PA4 remediation acceptance matrix — historical round 1

> This file preserves the prior remediation snapshot and its then-current Qa4/Qc2 scenario. It is not the current acceptance source. Use `remediation-round2-acceptance-matrix.md` for the validated round-2 scenario and readiness state.

Status meanings: `PASS` means the local implementation or deterministic validation is complete. `BLOCKED_EXTERNALLY` means the remaining condition requires genuine participant activity, an external upload, or the official course template that is not present in this workspace. No blocked condition is represented by invented evidence.

Current local handoff status: `READY_FOR_REAL_PARTICIPANTS`.

| ID | Acceptance condition | Status | Evidence / notes |
|---|---|---|---|
| RAC01 | Chess board shows a coherent legal scenario | PASS | `qa/chess-scenario-validation.md`; deterministic replay and final-position check |
| RAC02 | Mistake move is valid for the scenario | PASS | Authoritative `Qa4` mistake is legal from the validated position |
| RAC03 | Better move is valid and coherent | PASS | Authoritative `Qc2` better move is legal and protects c3 |
| RAC04 | Explanation matches the displayed board | PASS | c3 pawn, loose-pawn explanation, and Qa4/Qc2 states are aligned |
| RAC05 | Practice reinforces the same concept | PASS | Practice keeps the loose-c3-pawn concept and explanatory task |
| RAC06 | Old contradictory chess scenario is removed | PASS | Current prototype/reports use Qa4/Qc2; stale-literal validation is recorded |
| RAC07 | `chess-explain` works or is removed | PASS | Visible alternate explanation is repeatable and covered by browser QA |
| RAC08 | Read-only chess phases ignore board clicks | PASS | Intro, mistake, better, and practice boards use semantic non-button squares |
| RAC09 | Trial/practice input behavior matches the intended task | PASS | Trial accepts a wrong Qa4 path and a correct Qc2 path; practice is explanatory/read-only |
| RAC10 | FIFA primary interactions work | PASS | FIFA F01–F10 browser checks cover status, action, refresh, error, handoff, and return |
| RAC11 | FIFA branding and product boundary are consistent | PASS | FIFA.com ticket context and partner handoff are checked in presenter and study modes |
| RAC12 | Presenter mode is explicit and usable | PASS | `?mode=presenter#home` route and presenter shell pass browser QA |
| RAC13 | Study mode hides presenter/researcher shell | PASS | Direct FIFA and Chess study routes hide lab, launcher, offline/demo, and researcher chrome |
| RAC14 | Desktop layout is responsive | PASS | Browser QA at 1440 x 900; no horizontal overflow |
| RAC15 | Mobile layout is responsive | PASS | Browser QA at 390 x 844 for FIFA and Chess; no horizontal overflow |
| RAC16 | Keyboard and modal behavior work | PASS | Q01–Q06: reachability, focus, Escape, focus return, visible focus, and non-color status |
| RAC17 | `condition_order` is captured | PASS | `participants.csv` schema and study plan define `A_FIFA_FIRST`/`B_CHESS_FIRST` |
| RAC18 | `recovery_outcome` is captured | PASS | `task-results.csv` schema and study plan define the four permitted values |
| RAC19 | Named team responsibilities are documented | PASS | Study plan and report name Le Minh, Nguyen Vu Bach, Pham Nguyen Gia Bao, and Trang Minh Nhut |
| RAC20 | Timing limitation is stated | PASS | Moderated concurrent think-aloud uses descriptive task time; timing is not a controlled baseline |
| RAC21 | Participant count is independently gated | PASS | Analysis G01 blocks the current zero-row template at the real-participant threshold |
| RAC22 | Recording validity is independently gated | PASS | Analysis G03 validates media extension/size and ffprobe when available; no recording is claimed |
| RAC23 | Task data is independently gated | PASS | Analysis G04 checks required tasks, scores, durations, duplicates, and recovery fields |
| RAC24 | Questionnaire data is independently gated | PASS | Analysis G05 requires five Likert responses for each product per verified participant |
| RAC25 | Interview data is independently gated | PASS | Analysis G06 requires a timestamped non-empty feedback row per verified participant |
| RAC26 | Five metadata rows alone cannot produce PASS | PASS | Empty-template analysis has separate evidence gates and returns `BLOCKED_PARTICIPANT_COUNT` |
| RAC27 | Fake text `.mp4` cannot masquerade as valid recording | PASS | Recording validator checks media semantics; text fixture is rejected/unverified in tests |
| RAC28 | Fewer than five real participants remains blocked | PASS | Current analysis reports zero verified participants and blocks external evidence gates |
| RAC29 | Hi-fi report is synchronized | PASS | DOCX/PDF updated with legal chess scenario, study routes, evidence gate, and current screenshots |
| RAC30 | Summative report is synchronized | PASS | DOCX/PDF updated with roles, schemas, timing limitation, independent gates, and blockers |
| RAC31 | Weekly report uses official template or states external block | BLOCKED_EXTERNALLY | Official template is referenced by the brief but is not present locally; local snapshot is labeled as such |
| RAC32 | Screenshots are regenerated from the running prototype | PASS | 64-check browser run generated presenter/study desktop/mobile screenshots |
| RAC33 | Final PDFs render cleanly | PASS | Browser PDF.js render manifest covers HiFi 7 pages, Summative 6, Weekly 2; all visually inspected |
| RAC34 | Working evidence ZIP is separated from submission ZIP | PASS | `Group10-PA4-WorkingEvidence.zip` contains working artifacts and QA evidence; no nested ZIP |
| RAC35 | `Group10-PA4.zip` contains only official submission artifacts | PASS | Package validator requires exactly the three official PDF base names |
| RAC36 | YouTube demo URL is available | BLOCKED_EXTERNALLY | No genuine upload exists; reports retain an explicit external-evidence gate |
| RAC37 | Real participant sessions are complete | BLOCKED_EXTERNALLY | No real participant sessions were performed or claimed |
| RAC38 | Real recordings are complete and verified | BLOCKED_EXTERNALLY | No genuine recordings are present |
| RAC39 | Real questionnaire, task, and interview evidence is complete | BLOCKED_EXTERNALLY | CSVs remain schemas/header-only; no participant-dependent results are fabricated |

## Hard-stop conditions

Before real participant testing, RAC01/02/03/04/05/07/08/09/11/13/17/18/19/20/21/22/23/24/25/26/27/31 are reviewed. The implementation gates pass locally; RAC31 remains an explicit external blocker until the official Weekly Report template is supplied.

## Evidence integrity

No participant identities, recordings, quotes, task outcomes, questionnaire responses, timing results, or YouTube URL were invented. The local status is `READY_FOR_REAL_PARTICIPANTS`, not submission completion.
