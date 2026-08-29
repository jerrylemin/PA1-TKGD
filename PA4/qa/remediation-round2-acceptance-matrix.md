# PA4 remediation round 2 acceptance matrix

Status vocabulary is limited to `PASS`, `FAIL`, `BLOCKED_EXTERNALLY`, and `NOT_APPLICABLE`.

## Prototype

| ID | Criterion | Status | Evidence |
|---|---|---|---|
| R2AC01 | Chess intro hides the mistake answer | PASS | Browser QA C02/C20; intro text and board have no Qh5/Nxh5/Qe2 answer. |
| R2AC02 | Mistake state hides the better move until the appropriate stage | PASS | Browser QA C04; Qe2 appears only after the reveal action. |
| R2AC03 | Trial does not reveal the destination answer before input | PASS | Browser QA C07; trial copy contains no Qe2/e2 destination. |
| R2AC04 | Chess position legality verified | PASS | `python PA4/qa/validate_chess_scenario.py`; legal boards and king-safety checks pass. |
| R2AC05 | Mistake consequence verified | PASS | Validator proves legal Qh5 followed by knight Nxh5 capturing the queen. |
| R2AC06 | Better move addresses the documented consequence | PASS | Validator proves Qe2 is legal and outside the knight attack. |
| R2AC07 | Explanation matches ground truth | PASS | Authoritative scenario fields, renderer, and validator use the same attack/consequence model. |
| R2AC08 | Trial requires source-to-destination interaction | PASS | Browser QA C06/C08/C09/C10/C12; 64-square board and selectedSquare state. |
| R2AC09 | Wrong trial move gives feedback | PASS | Browser QA C11; wrong destination returns informative feedback. |
| R2AC10 | Correct trial move advances | PASS | Browser QA C12; source and destination produce the resulting board. |
| R2AC11 | Practice requires Chess input | PASS | Browser QA C13/C14; no completion control before a move. |
| R2AC12 | Practice supports retry | PASS | Browser QA C15; wrong practice move can be retried. |
| R2AC13 | Practice tests the same concept | PASS | Validator proves new Qd3 micro-position moves the queen away from a bishop attack. |
| R2AC14 | FIFA study mode hides researcher/demo chrome | PASS | Browser QA F10/C19; controls are removed from the participant DOM and text. |
| R2AC15 | Presenter mode retains required tools | PASS | Browser QA presenter checks and FIFA reset/preview availability check. |
| R2AC16 | Desktop layout passes | PASS | Browser QA desktop overflow and interaction checks. |
| R2AC17 | Mobile layout passes | PASS | Browser QA F09/C21 at 390×844 with no horizontal overflow. |

## Study methodology

| ID | Criterion | Status | Evidence |
|---|---|---|---|
| R2AC18 | Recording verification requires a video stream | PASS | `verify_recording` parses ffprobe JSON and requires `codec_type=video`. |
| R2AC19 | Audio-only MP4 is rejected | PASS | Analysis test T13 → `RECORDING_INVALID_NO_VIDEO_STREAM`. |
| R2AC20 | Text fake MP4 is rejected | PASS | Analysis test T06 → `RECORDING_INVALID_MEDIA`. |
| R2AC21 | `condition_order` is enforced | PASS | Existing analyzer tests and `ALLOWED_CONDITION_ORDERS` validation. |
| R2AC22 | Procedure is order-neutral | PASS | Study plan, facilitator script, and report model use first/second assigned product with both orders defined. |
| R2AC23 | `success_score` is operationally defined | PASS | Study plan, facilitator script, analyzer validation, and report model define 2/1/0. |
| R2AC24 | Hesitation is separate from success score | PASS | `hesitation_count` schema, 5-second operational definition, analyzer metric, and tests/docs. |
| R2AC25 | Weekly Report template does not block participant readiness | PASS | Package readiness separates local readiness from official template blocker. |
| R2AC26 | YouTube does not block participant readiness | PASS | YouTube is an official-package blocker only; local state remains participant-readiness scoped. |
| R2AC27 | Local study defects prevent false READY state | PASS | Package readiness checks browser QA, Chess validation, and canonical analysis artifact. |

## Reporting

| ID | Criterion | Status | Evidence |
|---|---|---|---|
| R2AC28 | DOCX/PDF share a substantive content model | PASS | `build_summative_report_data` is passed to both renderers; model tests pass. |
| R2AC29 | Study URLs render correctly | PASS | PDF extraction contains both raw `?mode=study&product=...` URLs; no `product;=`. |
| R2AC30 | Participant count is dynamic | PASS | Shared model test changes real empty state to isolated five-participant fixture. |
| R2AC31 | Recording state is dynamic | PASS | Shared model derives recording state from canonical G03/verified count. |
| R2AC32 | Task-data state is dynamic | PASS | Shared model test reflects 0 versus 40 task rows. |
| R2AC33 | Questionnaire state is dynamic | PASS | Shared model test reflects 0 versus 50 questionnaire rows. |
| R2AC34 | Interview state is dynamic | PASS | Shared model test reflects 0 versus 5 interview rows. |
| R2AC35 | Counterbalancing wording is aligned | PASS | Shared procedure model and both study renderers use assigned first/second product wording. |
| R2AC36 | Accidental near-empty page is fixed | PASS | Current Summative PDF has 4 populated pages; no page has three or fewer extracted lines. |
| R2AC37 | No stale answer-leaking screenshot | PASS | Regenerated screenshots use Qh5/Qe2/Qd3 ground truth and intro/trial checks show no leakage. |

## Packaging and external gates

| ID | Criterion | Status | Evidence |
|---|---|---|---|
| R2AC38 | Working evidence ZIP builds | PASS | `python PA4/scripts/package_pa4.py` builds the working archive before the official refusal. |
| R2AC39 | Official ZIP refuses while evidence is blocked | PASS | Same command returns `REFUSED` and preserves the prior official ZIP. |
| R2AC40 | Real YouTube link | BLOCKED_EXTERNALLY | No genuine YouTube URL is present locally. |
| R2AC41 | Minimum participant count | BLOCKED_EXTERNALLY | Current canonical analysis has zero participant rows and zero verified sessions. |
| R2AC42 | Real recordings | BLOCKED_EXTERNALLY | No consented session recordings are present. |
| R2AC43 | Task results | BLOCKED_EXTERNALLY | Task-results CSV is header-only. |
| R2AC44 | Questionnaire | BLOCKED_EXTERNALLY | Questionnaire CSV is header-only. |
| R2AC45 | Interviews | BLOCKED_EXTERNALLY | Interview-coding CSV is header-only. |
| R2AC46 | Official Weekly Report template | BLOCKED_EXTERNALLY | The referenced official template is not present in the workspace. |

## Participant-readiness hard gate

`READY_FOR_REAL_PARTICIPANTS` is the final local readiness state. R2AC01–R2AC27 are PASS. External study evidence is intentionally not required for this state and remains blocked for `SUBMISSION_READY` only.
