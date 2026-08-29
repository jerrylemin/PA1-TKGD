# PA4 remediation round 2 — memory-aware audit

Date: 2026-08-23
Repository root: `C:\Users\Administrator\Documents\MEGA\tkgd\PA`
PA parent: `C:\Users\Administrator\Documents\MEGA\tkgd\PA`
PA4 root: `C:\Users\Administrator\Documents\MEGA\tkgd\PA\PA4`
Branch: `main`
HEAD: `b6f6bde` (`del`)
Working tree: PA4 and supporting Codex/Graphify files are already untracked; preserved unchanged.

## Graphify state

- Version: `graphify 0.8.18`.
- Graph root: `PA4`.
- Graph JSON: `PA4/graphify-out/graph.json`.
- Report: `PA4/graphify-out/GRAPH_REPORT.md`.
- HTML: `PA4/graphify-out/graph.html`.
- Manifest: `PA4/graphify-out/manifest.json`.
- `graphify check-update PA4`: exited 0 with no pending update reported.
- The manifest matches the current pre-round-2 source mtimes for the principal code and document files, but has no entry for `prototype/styles.css`.
- Memory freshness at session start: `MEMORY_STALE_AT_SESSION_START` for the requested round-2 contract. The graph describes the prior remediation state, while current source still contains the round-2 defects.

## Memory-first findings

Scoped queries and explanations identified `prototype/app.js`, `qa/validate_chess_scenario.py`, `study/analysis/analyze_study.py`, `scripts/build_pa4_reports.py`, and `scripts/package_pa4.py` as the primary implementation surfaces. The graph preserved the selected FIFA Status Dashboard and Chess Beginner Review Flow lineage and the non-fabricated evidence boundary.

The following graph/source conflicts are material:

1. Graph/current-state memory presents participant-mode chrome as hidden and the local handoff as ready, but source uses CSS-only hiding and leaves researcher/debug controls in the participant DOM/state.
2. Graph memory describes the existing Qa4/Qc2 trial/practice path as validated, but source validation proves only move-shape/path geometry and the UI still leaks answers and uses destination-only input.
3. Graph memory records recording validation as a current gate, but source verification checks only MP4 extension, size, probe success, and positive duration; it does not require a video stream.
4. Graph memory describes counterbalancing in the study plan, while report source branches still write a fixed FIFA-first procedure and hardcode pre-study evidence values.
5. The current graph manifest does not index `prototype/styles.css`, so CSS coverage must be verified from source and refreshed after implementation.

## Phase 0 source verification

- R2-01: `prototype/app.js` renders the intro with `boardPanel({ phase: "mistake" })`; the mistake state exposes the `BETTER IDEA` move before the reveal action.
- R2-02: `qa/validate_chess_scenario.py` replays piece shapes and checks a path/attack distinction, but does not validate a complete move application, observable consequence, or pedagogical equivalence of the alternative.
- R2-03: trial squares dispatch on a single clicked destination and compare only `target.dataset.square`; direct `Play Qc2`/`Play Qa4` controls also bypass source-to-destination input.
- R2-04: practice renders the review position and a passive `Complete practice` button; no practice source/destination input is required.
- R2-05: `styles.css` hides `.study-researcher-chrome`, but the controls remain in `index.html`; `fifa-preview-error` and `fifa-reset` are not blocked in `handleAction()` when study mode is active.
- R2-06: `verify_recording()` invokes ffprobe for duration only and returns `VERIFIED_RECORDING` for any positive-duration probed media, without checking `codec_type=video`.
- R2-07: `study-plan.md` defines `A_FIFA_FIRST` and `B_CHESS_FIRST`, but report procedure content explicitly places FIFA before Chess.
- R2-08: study/report scoring text includes “meaningful hesitation” without an observable threshold or separate score field.
- R2-09: `pdf_p()` passes raw text to ReportLab `Paragraph`; report URLs contain query strings with `&`.
- R2-10: DOCX and PDF reports are authored in separate builder functions with duplicated substantive prose.
- R2-11: `build_study_docx()`/`build_study_pdf()` hardcode `0 verified`, empty/header-only states, and fixed gate wording instead of reading the canonical analysis result.
- R2-12: `package_pa4.py` always calls `build_submission_zip()` after file checks and has no official-readiness gate.
- R2-13: readiness is represented only in documents/matrices; no executable state model separates participant readiness from submission-template/external evidence blockers.
- R2-14: the current summative PDF uses unconditional page breaks and has not been root-cause-checked for near-empty pagination.

## Candidate affected files

- Prototype: `prototype/app.js`, `prototype/index.html`, `prototype/styles.css`, `prototype/README.md`.
- Chess QA: `qa/validate_chess_scenario.py`, `qa/chess-scenario-validation.md`, `scripts/capture-prototype-qa.mjs`.
- Study protocol/analysis: `study/study-plan.md`, `study/facilitator-script.md`, `study/analysis/analyze_study.py`, `study/analysis/test_analyze_study.py`, generated analysis outputs.
- Reports: `scripts/build_pa4_reports.py`, generated DOCX/PDF outputs, report QA helpers.
- Packaging/readiness: `scripts/package_pa4.py`, `qa/remediation-acceptance-matrix.md`, `work/external-blockers.md`.
- Memory after validation: `memory/continuity/PA4_CURRENT_STATE.md`, `memory/continuity/PROJECT_DECISION_CHAIN.md` only if decisions change, `memory/PA4_REMEDIATION_HISTORY.md`, `memory/MEMORY_ACCEPTANCE.md`, and source manifest only if classification/coverage changes.

Phase 1 reproduction and decisions are recorded separately in `PA4/work/remediation-round2-decision-log.md`.
