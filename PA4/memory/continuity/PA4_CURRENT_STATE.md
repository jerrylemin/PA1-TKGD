# PA4 current state

Last validated: 2026-08-23, HEAD `b6f6bde` plus current working-tree changes. Source and current QA are authoritative; Graphify is the navigation layer.

## Prototype architecture

The prototype is an offline, dependency-free vanilla HTML/CSS/JavaScript application. Presenter/default mode exposes the PA4 lab shell and researcher tools. Direct `?mode=study&product=...` routes remove the lab shell, launcher, demo labels, reset/unavailable preview controls, and researcher-only help from the participant DOM and focus order.

Browser QA is driven by the existing Playwright runtime and writes screenshots plus `qa/prototype-browser-qa.json`.

## FIFA Status Dashboard

The status-first flow exposes Pending and Confirmed states, owner/timing, official source, freshness, order/ticket actions, calendar action, partner preview, preserved context, and recoverable refresh behavior. Presenter mode retains reset and unavailable-state preview for demonstration; study mode removes those controls.

## Chess Beginner Review Flow

The current authoritative scenario is `queen-safety-before-activity`:

- Move 12, White to move, validated position.
- Mistake `Qh5`; immediate legal consequence `Nxh5` captures the queen.
- Better move `Qe2`, which moves outside the black knight attack.
- Practice uses a new bishop-attack micro-position with `Qd3` as the validated move.

The disclosure progression is intro → mistake/consequence → better move → trial → practice → completion. Trial and practice both require source selection followed by destination selection, track `selectedSquare`, show selection state, reject destination-only clicks, provide retry feedback, and render the resulting board after a correct move. The validator reads the scenario object from `prototype/app.js` and verifies board legality, attack/consequence, better move, explanation alignment, and practice concept without creating a second authoritative fixture.

## Study methodology and evidence state

The study package specifies moderated concurrent think-aloud, descriptive task time, consented recording, task markers, questionnaires, interviews, named Group10 responsibilities, counterbalanced `A_FIFA_FIRST`/`B_CHESS_FIRST` order, and a minimum of five real participants. `success_score` is 2/1/0 for independent, neutral-prompt/recoverable, or failed/directly assisted completion. `hesitation_count` is tracked separately using the documented five-second observable-pause rule.

The analyzer requires an existing MP4, positive duration, and a `codec_type=video` stream when `ffprobe` is available. Audio-only media is `RECORDING_INVALID_NO_VIDEO_STREAM`; corrupt/text media is `RECORDING_INVALID_MEDIA`; a present file without a probe is `RECORDING_PRESENT_UNVERIFIED` and never counts as verified.

The four study input CSVs remain header-only and the recordings directory has no participant media. The canonical analysis result is therefore `BLOCKED_PARTICIPANT_COUNT`, with independent participant, recording, task, questionnaire, interview, quantitative, and report gates. No participant finding is asserted.

## Report and package pipeline

`build_pa4_reports.py` loads the canonical `study/analysis/analysis-result.json` through `build_summative_report_data`. The DOCX and PDF Summative User Study renderers consume the same substantive model for counts, gate state, order-neutral procedure, task wording, scoring, hesitation, and recording rules. ReportLab escapes raw URLs at the markup boundary, preserving `?mode=study&product=fifa` and `?mode=study&product=chess` in extracted PDF text. The current Summative PDF is populated without the former near-empty continuation page.

`package_pa4.py` builds the working-evidence archive while evidence is incomplete. It reports `READY_FOR_REAL_PARTICIPANTS` for local readiness, refuses official ZIP generation while submission blockers remain, and preserves any pre-existing official ZIP.

## Readiness and blockers

Final local state: `READY_FOR_REAL_PARTICIPANTS`.

`SUBMISSION_READY` is not asserted. Confirmed external blockers are: a genuine YouTube demo URL, at least five real participant sessions, consented verified video recordings, task results, questionnaire responses, interview evidence, final evidence-backed analysis, and the official Weekly Report template if it remains unavailable.

Source:

- `PA4/prototype/app.js`
- `PA4/prototype/index.html`
- `PA4/prototype/styles.css`
- `PA4/scripts/capture-prototype-qa.mjs`
- `PA4/qa/validate_chess_scenario.py`
- `PA4/qa/remediation-round2-acceptance-matrix.md`
- `PA4/study/analysis/analyze_study.py`
- `PA4/study/analysis/analysis-result.json`
- `PA4/scripts/build_pa4_reports.py`
- `PA4/scripts/package_pa4.py`
- `PA4/work/remediation-round2-decision-log.md`
- `PA4/memory/PA4_REMEDIATION_HISTORY.md`
