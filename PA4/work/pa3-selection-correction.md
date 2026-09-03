# PA3 selection continuity correction

Status: continuity correction implemented and validated; the final Graphify result is reported in the task handoff.

## Git baseline

- Remote commit (`origin/main` after `git fetch origin`): `793cfa10d6ef79cc443b31144229c6ffc9e42cdd`.
- Local commit (`HEAD`): `793cfa10d6ef79cc443b31144229c6ffc9e42cdd` on `main`.
- Divergence: `0 0`; local and remote main match.
- Working tree before this task: 915 pre-existing deletions, all under `PA2/capture-work/automation/node_modules/`; no pre-existing PA4 changes.
- Root `README.md`: absent. Applicable root `AGENTS.md`, `PA4/README.md`, and `PA4/prototype/README.md` were read.

## Authoritative concept definitions

Repository definition source: `PA3/submission-final/source-evidence/testing-plan.md`.

- FIFA Alt 1 — Status Dashboard: status cards, confirmed/pending distinction, event list, primary next action, quick actions, support, and current-state summary. Its question is “What is true now?”
- FIFA Alt 2 — Timeline Tracker: completed/current/upcoming stages, current marker, freshness, source, ownership, and next-step guide. Its question is “Where am I in the process?”
- Chess Alt 1 — Beginner Review Flow: guided sequence, progress indicator, explanation, better move, practice bridge, and optional depth. It uses system-selected order.
- Chess Alt 2 — Card Review Mode: visual scan, self-selected moments, mini-board previews, expanded explanation, review/try/puzzle actions, and a practice bridge. It uses user-selected content.

### Historical selection conflict

The PA3 synthesis and existing PA4 continuity artifacts record Chess Alt 1 as the historical winner. The task contract explicitly overrides the implementation target to Chess Alt 2. This is a stale/conflicting winner-label case covered by the supplied decision rule. PA3 history will not be rewritten; the bounded PA4 prototype, QA, demo, and study surfaces will use FIFA Alt 1 + Chess Alt 2.

## Current PA4 mismatch audit

### FIFA

Classification: **B — selected-event lifecycle / timeline tracker**.

- Dominant region: `event-master-list` drives a selected `selected-event-workspace`.
- State summary visibility: no account-level Total/Confirmed/Pending/Action Needed summary appears before detail.
- Simultaneous events: both event names appear in a narrow selector, but their meanings, ownership, next steps, and actions are hidden behind selection.
- Selection dependency: one event is preselected and the main content changes only after event selection.
- Timeline prominence: a large four-step `fifa-progress-section` is a primary dashboard region.
- Quick actions: present, but bound to the currently selected event rather than adjacent to self-contained event states.
- Support/provenance: source and freshness are present; support is only in top navigation.

Conclusion: despite the Status Dashboard label, the composition is progress-first and selected-event-first, so it structurally behaves like FIFA Alt 2.

### Chess

Classification: **A — fixed system-guided Beginner Review Flow**.

- Initial state offers one “Start Beginner Review” action.
- Global state machine is `intro → mistake → better → trial → practice → complete`.
- The system chooses the Qh5 moment and exposes no multi-card dashboard.
- A global “STEP 1 OF 3” rail and mandatory next controls impose order.
- “Review another moment” resets to the same mistake rather than enabling an independent choice.

Conclusion: the current implementation is Chess Alt 1 and is incompatible with user-selected Card Review Mode.

## Root cause

PA4 preserved labels from one direction while later redesign work changed FIFA composition toward timeline/master-detail and retained Chess Alt 1's fixed wizard. The problem is continuity/interaction-model mismatch, not visual polish.

## Decision table

If FIFA is progress-first / selected-event-first
→ replace its primary composition with PA3 Alt 1 Status Dashboard.

If Chess is fixed system-sequenced
→ replace its primary composition with PA3 Alt 2 Card Review Mode.

If local PA3 evidence contains stale/conflicting winner labels
→ do NOT rewrite PA3 history; treat the user-authoritative PA4 selection as FIFA Alt 1 + Chess Alt 2 and record the conflict.

Otherwise
→ stop with SELECTION_CONTRADICTION and report exact evidence.

Decision: the first three conditions apply. Proceed with the bounded correction; there is no third interpretation.

## Planned files

- `PA4/prototype/index.html`
- `PA4/prototype/styles.css`
- `PA4/prototype/app.js`
- `PA4/prototype/README.md`
- `PA4/scripts/capture-prototype-qa.mjs`
- `PA4/qa/prototype-browser-qa.json` (generated only by canonical QA)
- `PA4/study/study-plan.md`
- `PA4/study/facilitator-script.md`
- `PA4/demo/DEMO-SCRIPT.md`
- `PA4/work/pa3-selection-correction.md`

No PA1/PA2/PA3 historical deliverable, participant data, recording, analysis-result evidence, package architecture, dependency, framework, backend, or Chess engine will be changed.

## Implemented correction

### FIFA Alt 1 — Status Dashboard

- The primary page now begins with four internally consistent account counts: 2 All, 1 Confirmed, 1 Pending, and 0 Action needed.
- Mexico City and Toronto are simultaneously visible as self-contained cards with date, venue/match, state, plain-language meaning, owner, next step, source, and contextual action.
- Summary cards filter the same event list; no event selection is required to understand the account state.
- View Order and View Tickets open secondary drawers. The only lifecycle display is a compact history inside order detail, not the dashboard composition.
- Quick actions, official-source/freshness cues, a local notification cue, contextual calendar controls, recoverable refresh state, and the external-partner trust boundary remain available.

### Chess Alt 2 — Card Review Mode

- The initial state now contains four derived summary chips and four simultaneously visible, independently selectable cards. No card is preselected.
- Every card includes a static mini-board preview, move number, category cue, short label, description, and available-action cue.
- Any card opens its own explanation and preserves an explicit return to all key moments; there is no global step rail or mandatory card order.
- The Queen safety card retains the validated `Qh5` → `Nxh5` explanation and optional source-to-destination `Qe2` trial plus separate optional `Qd3` practice.
- Wrong trial/practice moves remain recoverable, correct moves update the board, and both optional paths return to the selected card or dashboard without forcing a global completion flow.

## Study synchronization and evidence boundary

- `FIFA-T1` now begins with the overall account situation before one event's next step; the remaining FIFA handoff tasks and study design are unchanged.
- `CHESS-T1` through `CHESS-T4` now measure dashboard scanning and first-card choice, selected-card comprehension, optional safer-move trial, and optional practice plus dashboard return.
- Participant criteria, five-or-more participant gate, counterbalancing, questionnaire, success scale, consent, privacy, and evidence schemas were preserved.
- No participant CSV, recording, questionnaire response, interview evidence, timing row, or analysis-result evidence changed.

## Validation evidence

- `node --check PA4/prototype/app.js`: PASS.
- `node --check PA4/scripts/capture-prototype-qa.mjs`: PASS.
- `python PA4/qa/validate_chess_scenario.py`: PASS for legal/static `Qh5`, `Nxh5`, `Qe2`, and `Qd3` behavior; its tracked output remained unchanged.
- `node PA4/scripts/capture-prototype-qa.mjs`: PASS, 150/150 assertions, 0 browser console/page errors. Screenshots were directed to a temporary folder so tracked screenshot evidence stayed untouched.
- FIFA `FIFA-A1-01` through `FIFA-A1-10`: PASS, including CAL01–CAL06 and partner preview/cancel/continue/safe-return behavior.
- Chess `CHESS-A2-01` through `CHESS-A2-15`: PASS, including independent card choices, answer-leakage gates, retry paths, optional practice, and return to another card.
- Presenter and both study routes: PASS; study pages contain no PA4/presenter controls, researcher hints, visible internal IDs, or premature `Qe2`/`Qd3` answers.
- Responsive checks at 1440×900, 1024×768, 768×1024, and 390×844: PASS for overflow, overlap, event/card availability, mini-board size, selected-card return, and event/handoff dialog geometry.
- Human inspection of presenter, study-dashboard, desktop, mobile, selected-card, and mobile-handoff captures found no clipping, overlap, or hierarchy regression.
- `git diff --check -- PA4`: PASS (only repository line-ending notices).

## Stale-reference classification

The active corrected surfaces (`prototype`, prototype README, study plan, facilitator script, and demo script) contain no claim that Chess Alt 1 or FIFA Alt 2 is the selected PA4 implementation. Broader `rg PA4` results still include pre-existing out-of-scope historical, traceability, generated-report, build-script, and semantic-memory references to the former Chess Alt 1 implementation. Examples include `PA4/evidence/pa3-pa4-traceability.csv`, `PA4/qa/acceptance-matrix.md`, `PA4/scripts/build_pa4_reports.py`, `PA4/memory/`, and `PA4/graphify-out/`. They were not edited because the task scope explicitly forbids evidence/report/package expansion and requires preservation of PA3 history.

The required AST-only Graphify update cannot refresh those semantic artifacts while semantic workers are forbidden. If those references remain after the one permitted incremental update, the handoff marker is `GRAPHIFY_SEMANTIC_MEMORY_STALE`.
