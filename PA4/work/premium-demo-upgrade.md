# Premium demo upgrade audit

## Current FIFA layout

- Presenter shell with FIFA wordmark, breadcrumb, status summary, status card, event rows, quick actions, and a three-card support rail.
- Order and ticket detail currently render through the shared modal system; transfer uses a two-step handoff modal and offline partner boundary state.
- Pending is the default selected event; confirmed Toronto is available through the existing event selector.

## Current Chess layout

- Distinct dark review shell with a two-column stage, Unicode chess board, review copy, and route/context rail.
- Validated phases are intro, mistake, better move, trial, practice, and complete.
- Trial and practice already require source then destination, preserve answer disclosure, and provide retry/correct feedback.

## Current shared shell

- Single static HTML/CSS/JS prototype with hash routes for home, FIFA, and Chess.
- Presenter chrome is removed from the DOM in study mode; product views remain available directly on the study route.
- Shared modal, toast, focus-visible, escape-close, and modal focus-loop behavior already exists.

## Current interaction states

- FIFA: event selection, status explanation, refresh/error recovery, order detail, ticket detail, calendar confirmation, handoff cancel/continue/return, presenter reset/unavailable preview.
- Chess: locked intro/mistake/better boards, alternate explanation, source-to-destination trial, wrong move retry, practice, and completion.

## Files to modify

- `PA4/prototype/index.html`
- `PA4/prototype/app.js`
- `PA4/prototype/styles.css`
- `PA4/scripts/capture-prototype-qa.mjs`
- Generated `PA4/qa/prototype-browser-qa.json` and `PA4/evidence/prototype-screenshots/`

## Validation plan

- Run `node --check PA4/prototype/app.js`.
- Run the existing Playwright QA with added detail/partner screenshots and 1440, 1024, 768, and 390 viewport checks.
- Inspect the regenerated FIFA and Chess state screenshots, including study routes, for hierarchy, overflow, focus, and answer disclosure.
- Review `git diff` and confirm no study, evidence, package, or non-UI files changed beyond the allowed generated QA/evidence outputs.
