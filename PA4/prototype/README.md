# Group10 PA4 hi-fi prototype

This is a dependency-free offline demonstrator for the two selected PA3 directions:

- FIFA Alt 1: Status Dashboard.
- Chess Alt 1: Beginner Review Flow.

## Start

From the repository root:

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory PA4/prototype
```

Open `http://127.0.0.1:4173/index.html`.

The prototype does not call a live FIFA, ticketing, or Chess.com service. All records are fictional demo content and are labeled accordingly.

## Demo paths

- FIFA: select the Pending event, open `View Order`, open `Transfer Tickets`, inspect the partner boundary, continue in the offline handoff state, and return to the dashboard.
- Chess: start Beginner Review, inspect the `Qh5` mistake and `Nxh5` consequence, reveal `Qe2`, perform a source-to-destination trial, complete the separate `Qd3` practice position, and finish the review.

## Study and presenter modes

- Presenter/default: `http://127.0.0.1:4173/index.html?mode=presenter#home`
- FIFA participant flow: `http://127.0.0.1:4173/index.html?mode=study&product=fifa#fifa`
- Chess participant flow: `http://127.0.0.1:4173/index.html?mode=study&product=chess#chess`

Study mode opens directly into one product flow and hides the PA4 lab shell, launcher, offline-demo labels, and researcher-only help/depth controls. Presenter mode retains the overview and demo navigation.

## QA

The existing PA2 Playwright runtime runs the deterministic browser checks and screenshot capture:

```powershell
node PA4/scripts/capture-prototype-qa.mjs
```

Screenshots are written to `PA4/evidence/prototype-screenshots/`; the machine-readable result is `PA4/qa/prototype-browser-qa.json`.
