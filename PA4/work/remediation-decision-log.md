# PA4 remediation decision log

Date opened: 2026-08-23
Repository: `C:\Users\Administrator\Documents\MEGA\tkgd\PA`
Branch: `main`
HEAD: `b6f6bde` (`del`)
Working tree at start: `PA4.zip` and the complete `PA4/` working tree were already untracked. These files are preserved.

## Scope and invariants

- Preserve the selected FIFA Status Dashboard and Chess Beginner Review Flow.
- Correct only verified PA4 implementation, study-validity, QA, report, and packaging defects.
- Do not create real participant evidence or external links.
- Do not use destructive Git commands or overwrite unrelated user work.

## Phase 0 evidence

- Official brief: `PA4/PA4-LKDuy-2026-Public.pdf`, three pages, directly read on 2026-08-23.
- PA3 continuity: `PA4/work/pa3-continuity.md` confirms FIFA Alt 1 Status Dashboard and Chess Alt 1 Beginner Review Flow.
- Roster continuity: `PA4/work/pa1-continuity.md` and prior artifacts identify Le Minh, Nguyen Vu Bach, Pham Nguyen Gia Bao, and Trang Minh Nhut.
- Local template search and all reviewed defects remain audit items until Phase 1 reproduction is complete.

## Audit findings

The full Phase 1 table is in `PA4/work/remediation-audit.md`. Confirmed local defects are R1, R2, R3, R4, R5, R7, R8, R9, R10, R11, and R12. R6 is blocked externally because the official Weekly Report template is not available locally.

### Decisions before implementation

- Preserve both PA3 directions and patch the smallest affected surface.
- Replace the invalid Chess example with a legal, internally coherent beginner position and one authoritative scenario object; do not reintroduce the old `Qd3`/`Qe2` content.
- Keep `chess-explain` as useful progressive disclosure with deterministic visible feedback.
- Make review boards semantic and read-only outside trial/practice, with a dispatcher guard as a second defense.
- Treat recording files as verified only after extension/size and media-header/duration validation when a local probe exists; otherwise report an unverified external blocker.
- Split independent study evidence gates so five participant rows alone cannot pass the study.
- Add the structured `condition_order` and `recovery_outcome` fields, then validate required tasks and evidence per participant.
- Assign named Group10 study responsibilities while preserving honest status labels.
- Document moderated concurrent think-aloud with descriptive task time; do not claim natural unmoderated timing.
- Add presenter/study modes and make FIFA.com ticket context the primary identity.
- Expand the existing browser harness and create separate working-evidence and submission packages.
- Preserve the pre-existing root `PA4.zip`; it is not the submission artifact.

## Decisions

To be recorded after each defect is reproduced or shown not to reproduce. The default is the smallest architecture-compatible fix; external evidence remains blocked rather than simulated.

## Validation plan

- deterministic Chess scenario validation;
- targeted analysis unit tests, including fake-recording rejection;
- browser interaction QA for visible controls, locked board phases, keyboard/modal behavior, responsive layouts, branding, and presenter/study modes;
- report/PDF render and text checks;
- ZIP content and schema validation;
- final diff and acceptance-matrix review.

## External blockers confirmed

See `PA4/work/external-blockers.md`: official Weekly Report template, genuine YouTube URL, and all real summative evidence remain unavailable.
