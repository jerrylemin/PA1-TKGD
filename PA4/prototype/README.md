# Group10 PA4 hi-fi prototype

This dependency-free offline demonstrator implements the task-authoritative PA3 continuity directions:

- FIFA Alt 1: Status Dashboard.
- Chess Alt 2: Card Review Mode.

PA3 historical artifacts are preserved unchanged. The Chess Alt 2 direction here is the explicit continuity correction for PA4.

## Start

From the repository root:

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory PA4/prototype
```

Open `http://127.0.0.1:4173/index.html`.

The prototype does not call a live FIFA, ticketing, or Chess.com service. All records are fictional demo content and are labeled accordingly.

## Demo paths

- FIFA: scan the four account-level status counts, compare the Pending and Confirmed event cards, open the relevant order or tickets, save the eligible event to the calendar, inspect the partner boundary, continue to the offline handoff state, and return to the dashboard.
- Chess: scan four key-moment cards, choose any card to review, inspect the `Qh5` mistake and `Nxh5` consequence, reveal the optional `Qe2` safer move, try it by selecting source and destination, optionally complete the separate `Qd3` practice position, and return to the card dashboard.

## Study and presenter modes

- Presenter/default: `http://127.0.0.1:4173/index.html?mode=presenter#home`
- FIFA participant flow: `http://127.0.0.1:4173/index.html?mode=study&product=fifa#fifa`
- Chess participant flow: `http://127.0.0.1:4173/index.html?mode=study&product=chess#chess`

Study mode opens directly into one product flow and hides the PA4 lab shell, launcher, offline-demo labels, and researcher-only help controls. Presenter mode retains the overview and demo navigation.

## QA

The deterministic Playwright checks use an available local Playwright runtime:

```powershell
node PA4/scripts/capture-prototype-qa.mjs
```

By default, screenshots are written to `PA4/evidence/prototype-screenshots/`; set `PA4_QA_SCREENSHOT_DIR` to use a temporary evidence location. The machine-readable result is `PA4/qa/prototype-browser-qa.json`.
