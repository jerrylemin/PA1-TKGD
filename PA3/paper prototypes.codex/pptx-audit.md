# PA3 presentation evidence audit

## Scope and evidence boundary

- Repository root: `C:\Users\Administrator\Documents\MEGA\tkgd\PA`
- Working tree before implementation: existing user changes under `PA3/`; no required presentation outputs existed.
- Source of authority for original interface claims: PA2 evidence index, PA2 traceability matrix, PA2 evidence validation, and the approved local screenshots listed below.
- PA1 and PA2 remain read-only. Prototype PNGs remain unchanged; only presentation-local working copies are used by the HTML source.
- No participant results, timings, preference claims, quotes, or success rates are used as evidence. PA3 formative measures are presented as planned tests or hypotheses only.

## Evidence table

| Scenario | Alternative | Prototype file | Original UI reference | PA1 or PA2 finding | Problem addressed | Interaction model | Primary delta from original | Traceability ID if verified | Source file for traceability | Evidence confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| FIFA.com ticket planning | Alt 1 — Status Dashboard | `paper prototypes/alt1scenario1.png` | `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` | FIFA ticket action lacks consolidated decision confidence; outbound route needs trust context. | Users need an at-a-glance answer to whether tickets are okay and what to do next. | Status-first dashboard with state counts, event cards, quick actions, support. | Adds a persistent account-level status view over tournament-entry cards; makes confirmed/pending/action-needed states explicit. | `F-A1`; `F-UC02/F-UC03/F-UC06` | `PA2/traceability-matrix.csv` | High for baseline; medium for hypothesis |
| FIFA.com ticket planning | Alt 2 — Timeline Tracker | `paper prototypes/alt2scenario1.png` | `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` | FIFA ticket action lacks consolidated decision confidence; PA2 evidence supports clearer state/freshness and next-step hypotheses. | Users need to know where an order is in its lifecycle, whether information is current, and what happens next. | Progress-first timeline with milestone states, update history, official source, next-step guidance. | Adds lifecycle visibility and freshness signals that are not present on the captured landing state. | Descriptive name only; `F-UC02/F-UC04/F-UC06` is verified use-case context | `PA2/traceability-matrix.csv`; `PA2/evidence-index.csv` | High for baseline; medium for hypothesis |
| FIFA.com ticket planning | Alt 3 — Action Hub | `paper prototypes/alt3scenario1.png` | `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png`; `PA2/capture-work/fifa/desktop/fifa-32-before-partner-handoff.png` | Ticket task entry and partner-boundary context are separated across the captured experience. | Users need to find common ticket actions quickly and understand when a task leaves FIFA.com. | Tasks-first action hub with shortcuts, official options, support, and handoff trust. | Reframes the entry surface around high-frequency post-purchase tasks and makes partner boundaries explicit. | Descriptive name only; `F-UC02/F-UC04/F-UC05/F-UC06` is verified use-case context | `PA2/traceability-matrix.csv`; `PA2/evidence-index.csv` | High for baseline; medium for hypothesis |
| Chess.com beginner post-game review | Alt 1 — Beginner Review Flow | `paper prototypes/alt1scenario2.png` | `PA2/capture-work/chess/desktop/chess-29-analysis-board.png`; `PA2/capture-work/chess/desktop/chess-26-learn-page.png` | Chess analysis entry has high recall demand; learning and analysis lack a beginner bridge; practice is disconnected from review. | Beginners need one comprehensible path from a game mistake to a better move and practice. | Fixed guided sequence: one mistake, plain explanation, better move, practice bridge. | Turns a multi-path analysis entry into a constrained beginner mode using the progressive Learn pattern. | `C-A1`; `C-UC02/C-UC03/C-UC04/C-UC05/C-UC06` | `PA2/traceability-matrix.csv` | High for baseline; medium for hypothesis |
| Chess.com beginner post-game review | Alt 2 — Card Review Mode | `paper prototypes/alt2scenario2.png` | `PA2/capture-work/chess/desktop/chess-29-analysis-board.png`; `PA2/capture-work/chess/desktop/chess-26-learn-page.png` | Chess analysis entry has high recall demand; users need a bridge into review and practice. | Beginners need to scan what matters and choose a relevant learning moment without an imposed sequence. | Non-linear visual dashboard of summary chips, key-moment cards, expanded explanation, practice actions. | Replaces blank/setup-heavy analysis entry with recognition-first review cards and self-selected order. | Descriptive name only; `C-UC03/C-UC04/C-UC05/C-UC06` is verified use-case context | `PA2/traceability-matrix.csv`; `PA2/evidence-index.csv` | High for baseline; medium for hypothesis |
| Chess.com beginner post-game review | Alt 3 — Side-by-Side Assistant | `paper prototypes/alt3scenario2.png` | `PA2/capture-work/chess/desktop/chess-29-analysis-board.png`; `PA2/capture-work/chess/desktop/chess-26-learn-page.png` | Analysis entry has high recall demand; beginner explanations need a bridge from the board to plain language. | Beginners need contextual explanations without leaving the board or knowing engine vocabulary. | Conversational assistant beside the board with contextual highlights, key moments, follow-up prompts. | Keeps board context present while adding a question-led explanation layer and visible follow-up paths. | Descriptive name only; `C-UC03/C-UC04/C-UC05/C-UC06` is verified use-case context | `PA2/traceability-matrix.csv`; `PA2/evidence-index.csv` | High for baseline; medium for hypothesis |

## Current-state conclusion

### Scenario 1 baseline

The approved PA2 capture `F2-E09` shows FIFA.com’s Tickets & Hospitality landing page organized around tournament logos and ticket/hospitality cards with actions such as register interest or buy now. The evidence index explicitly limits the claim: the captured state does not show a consolidated cross-tournament status dashboard, seat map, waiting room, resale dashboard, or last-updated dashboard. The PA2 traceability matrix identifies the supported problem as lack of consolidated decision confidence and separately flags outbound-route trust. Therefore the deck compares the six alternatives against ticket-entry and handoff evidence, not against an invented post-purchase FIFA account state.

### Scenario 2 baseline

The approved PA2 capture `C2-E10` shows Chess.com’s Analysis entry with Set Up Position, Explore, Game Search, Game Collections, import/upload controls, and Start Analysis. PA2 evidence validation explicitly limits that screenshot to analysis-entry choices; it does not show completed review output, engine lines, classifications, or a beginner explanation. `C2-E08` shows a separate Learn-to-Play surface with a progressive lesson path, explanatory prompt, and clear Next Lesson action. The deck therefore frames the Chess alternatives as a beginner bridge from the advanced analysis entry toward a clearer review workflow, while keeping the evidence boundary visible.

## Prototype distinction

- **FIFA Alt 1:** Status Dashboard — answers “What is my status now?” with state recognition and confidence.
- **FIFA Alt 2:** Timeline Tracker — answers “Where am I in the process, and what happens next?” with progress and freshness.
- **FIFA Alt 3:** Action Hub — answers “What can I do right now?” with tasks, shortcuts, and handoff trust.
- **Chess Alt 1:** Beginner Review Flow — system-selected order; a fixed guided sequence.
- **Chess Alt 2:** Card Review Mode — user-selected content; a visual dashboard of review cards.
- **Chess Alt 3:** Side-by-Side Assistant — user-selected questions; conversational exploration beside the board.

## Decision

Repository evidence is sufficient. Use repository evidence only. No new public-site screenshot is required or captured.

## Grove reference

The deck adapts the Grove system from the required reference: deep forest `#192b1b`, parchment `#e8e4d6`, warm cream `#d4cfbf`, terracotta `#c8524a`, Playfair Display headlines, Jost body text, JetBrains Mono labels, 1px rules, generous negative space, restrained accent usage, and subtle watermark numerals. Prototype screenshots retain their original approved content and are framed rather than redesigned.
