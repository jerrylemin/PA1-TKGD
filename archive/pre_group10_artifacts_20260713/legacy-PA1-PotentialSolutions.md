# GroupID-PA1 Potential Solutions: FIFA and Chess.com

## Executive summary

The solution set keeps FIFA focused on task-first navigation, continuity across FIFA+, clearer ticket status, and utility entry points. It keeps Chess.com focused on novice onboarding, simpler analysis, expectation-setting around access limits, safer premoves, and clearer Focus Mode discovery.

## Relationship to ProductResearch findings

Every FIFA drawback is owned by Le Minh and Nguyen Vu Bach; every Chess.com drawback is owned by Pham Nguyen Gia Bao and Trang Minh Nhut. Each drawback maps to its ProductResearch finding and evidence figure, affected use case, and exactly two solution IDs in the tables below.

![Diagram PS-D1](assets/diagrams/rendered/pa1_potentialsolutions_traceability.png)

Diagram PS-D1. ProductResearch-to-solution traceability. This rendered diagram shows how an observed finding becomes a drawback, two proposed solutions, and an expected HCI improvement.

## Drawback inventory

| ID | Product | Drawback | Linked finding | Severity |
| --- | --- | --- | --- | --- |
| F-D1 | FIFA | Ecosystem sprawl across sibling FIFA properties | F-HCI6 | High |
| F-D2 | FIFA | FIFA+ handoff breaks continuity | F-HCI7 | High |
| F-D3 | FIFA | FIFA+ scan overload | F-HCI8 | Medium |
| F-D4 | FIFA | Ticket status uncertainty | F-HCI9 | High |
| F-D5 | FIFA | Browse-first friction for quick utilitarian tasks | F-HCI10 | Medium |
| C-D1 | Chess.com | Menu and feature overload for novices | C-HCI7 | High |
| C-D2 | Chess.com | Analysis overload | C-HCI10 | High |
| C-D3 | Chess.com | Premium gating interrupts learning momentum | C-HCI10 | Medium |
| C-D4 | Chess.com | Premove blunder risk | C-HCI8 | High |
| C-D5 | Chess.com | Focus Mode is hard to discover | C-HCI9 | Medium |

## Drawback evidence and visual solution mapping

| Drawback ID | Observed evidence | Problem | Persona | Context | HCI principle | Solutions | Solution description | Proposed solution figure | Expected improvement | Tradeoff | Priority | Effort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-D1 | F-09B + [1][6][9] | Cross-property navigation and top-level task competition span FIFA.com, Inside FIFA, FIFA+, Store, Collect, and Rewards. | F-P1/F-P3 | Short task entry and trust-sensitive planning | context switching; mental-model consistency | F-S1/F-S2 | Task-first navigation and audience intent chips | S-01 | Fewer property jumps and clearer task entry | Commercial links receive less top-level exposure | High | Medium |
| F-D2 | Source-only [6] | The DAZN-branded FIFA+ handoff changes brand and account expectations, creating trust friction and mode-boundary confusion. | F-P3 | Family watch handoff after ticket or news research | continuity; orientation; visibility of system status | F-S3/F-S4 | Handoff explainer and shared visual bridge | S-04 | Clearer destination expectations and return path | Adds a step and needs cross-property coordination | High | Medium |
| F-D3 | F-10B + [6] | Dense FIFA+ watch rails increase the scan load for live, highlight, documentary, competition, and archive content. | F-P3 | Evening highlight search with family waiting | visual attention; choice overload; progressive disclosure | F-S5/F-S6 | Rail filters and compact scan mode | No faithful existing mockup | Faster media discovery with less vertical scanning | Depends on reliable content metadata | Medium | Medium |
| F-D4 | Source-only [5][9] | Sale, resale, waiting-room, and availability uncertainty force repeated manual checks. | F-P3 | Multi-day family travel and ticket planning | visibility of system status; prospective memory | F-S7/F-S8 | Ticket status dashboard and official availability alerts | No faithful existing mockup | Users know whether to act now or wait | Requires governed status data and notification consent | High | Medium |
| F-D5 | F-06 + [1][2][3][7] | Article-to-score, article-to-ticket, and article-to-watch tasks require extra navigation after reading. | F-P1/F-P2/F-P3 | Interrupted story reading followed by a utility task | task continuity; efficiency; information scent | F-S9/F-S10 | Article utility rail and embedded action chips | S-03 | Fewer article-to-task jumps | Utility controls may distract from reading | Medium | Low |
| C-D1 | C-06 + [10][18][19][20] | The broad menu and feature taxonomy overload novices before they know which path fits their goal. | C-P1 | First visit and beginner study | choice overload; progressive disclosure | C-S1/C-S2 | Goal-based onboarding and personal dashboard | S-05 | A clearer first success path | Adds onboarding and personalization state | High | Medium |
| C-D2 | Source-only [15][16][17] | Game Review and Analysis expose dense charts, lines, classifications, toggles, and labels before novices know what matters. | C-P1/C-P3 | Post-loss review on laptop or desktop | cognitive load; external cognition | C-S3/C-S4 | Beginner analysis preset and inline glossary | S-07 | Readable feedback before expert controls | Advanced controls move one level deeper | High | Low |
| C-D3 | Source-only [19] | Lesson, puzzle, and review limits can appear after attention is invested and interrupt learning momentum. | C-P1/C-P3 | Beginner learning path after a loss | expectation setting; continuity; visibility of access state | C-S5/C-S6 | Upfront entitlement labels and a soft landing | S-08 | Fewer surprise access interruptions | Access labels add visual noise | Medium | Low |
| C-D4 | Source-only [12] | A legal queued premove may execute after an unexpected reply and create a blunder. | C-P2 | Blitz or bullet under clock pressure | speed-accuracy tradeoff; error prevention; recoverability | C-S7/C-S8 | Premove queue preview and fast clear shortcut | S-06 | More visible and recoverable queued intent | Risk estimates may be imperfect | High | Medium |
| C-D5 | Source-only [13][14] | Focus Mode is hard to discover because related controls appear on hover near the board boundary. | C-P2/C-P3 | Serious-game setup on desktop | discoverability; hidden controls; contextual help | C-S9/C-S10 | Contextual coachmark and persistent settings shortcut | No faithful existing mockup | Focus Mode becomes findable without hover discovery | Coachmarks can annoy experts | Medium | Low |

## Drawback-to-solution mapping

| Drawback | Solutions |
| --- | --- |
| F-D1 | F-S1, F-S2 |
| F-D2 | F-S3, F-S4 |
| F-D3 | F-S5, F-S6 |
| F-D4 | F-S7, F-S8 |
| F-D5 | F-S9, F-S10 |
| C-D1 | C-S1, C-S2 |
| C-D2 | C-S3, C-S4 |
| C-D3 | C-S5, C-S6 |
| C-D4 | C-S7, C-S8 |
| C-D5 | C-S9, C-S10 |

## Visual solution figures

### Figure S-01. FIFA task-first navigation

![Figure S-01](assets/diagrams/s-01_fifa_solution.png)

A task-first header reduces hidden navigation cost for casual fans and tournament followers.

### Figure S-02. FIFA Match Centre filter bar

![Figure S-02](assets/diagrams/s-02_fifa_solution.png)

Sticky date, live, result, and competition controls reduce scanning in the Match Centre.

### Figure S-03. FIFA article utility rail

![Figure S-03](assets/diagrams/s-03_fifa_solution.png)

Context chips let an article reader jump to scores, tickets, or watch actions without re-searching.

### Figure S-04. FIFA+ handoff explainer

![Figure S-04](assets/diagrams/s-04_fifa_solution.png)

A handoff explainer improves trust and user control before switching context to FIFA+.

### Figure S-05. Chess.com beginner home

![Figure S-05](assets/diagrams/s-05_chess_solution.png)

Goal-based cards reduce beginner feature overload before the user learns product taxonomy.

### Figure S-06. Chess.com mobile board guard

![Figure S-06](assets/diagrams/s-06_chess_solution.png)

Larger controls and a clear premove action reduce mobile mis-tap risk under time pressure.

### Figure S-07. Chess.com beginner analysis preset

![Figure S-07](assets/diagrams/s-07_chess_solution.png)

Beginner, standard, and expert presets progressively reveal game-review complexity.

### Figure S-08. Chess.com learn path

![Figure S-08](assets/diagrams/s-08_chess_solution.png)

A recommended beginner path and visible access labels reduce learning-path uncertainty.

## Solution details

| ID | Drawback | Design concept | Detailed UI behavior | Mockup description in words | HCI principle mapping | Affected personas | Affected contexts | Expected effect | Tradeoff | Priority | Effort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-S1 | F-D1 | Task-first global nav | Keep Match Centre, News, Rankings, Tickets, Watch at top level; move Store, Collect, and Rewards into More FIFA. | Slim header with one primary task row and one tucked ecosystem menu. | Recognition over recall; cognitive load reduction | F-P1/F-P2/F-P3 | Short task entry, office browsing, ticket planning | Fewer property jumps for common tasks. | Store and collectibles receive less top-level exposure. | High | Medium |
| F-S2 | F-D1 | Audience intent switcher | Add five quick-intent chips under the hero: Scores, News, Rankings, Tickets, Watch. | Horizontal chip bar under page title. | Feedforward; efficient entry | F-P1/F-P2/F-P3 | Short sessions with unclear starting point | Users choose by intent before reading navigation labels. | One more row competes for above-fold attention. | High | Low |
| F-S3 | F-D2 | Handoff explainer card | Before leaving FIFA.com, show You are opening FIFA+ powered by DAZN with destination benefits and sign-in expectation. | Centered modal with Continue and Stay on FIFA.com. | Visibility of system status; trust | F-P3 | Family watch handoff | Users understand why branding and login state change. | Adds one step for repeat viewers. | High | Low |
| F-S4 | F-D2 | Shared breadcrumb and visual bridge | Add persistent Back to FIFA.com strip and tournament breadcrumb on FIFA+. | Thin top bar with FIFA icon, destination label, and return link. | Continuity; orientation | F-P3 | FIFA+ watch browsing after ticket/news research | Users retain orientation across the watch boundary. | Needs cross-property coordination. | Medium | Medium |
| F-S5 | F-D3 | Filter-first rail controls | Provide filters for Live, Highlights, Documentaries, Competition, and Duration above rails. | Sticky filter row above content rails. | Visual filtering; reduced scan cost | F-P3 | Evening highlight search | Users narrow a large content surface faster. | Filter accuracy depends on metadata quality. | High | Medium |
| F-S6 | F-D3 | Compact scan mode | Collapse nonmatching rails into section labels until expanded. | Condensed page with one expanded rail and folded sections. | Progressive disclosure; visual economy | F-P3 | Slow browsing with family waiting | Lower vertical scanning burden. | Some content feels less discoverable. | Medium | Medium |
| F-S7 | F-D4 | Ticket status dashboard | Show Official sale, Resale open, Waiting room, Coming soon, and Latest update time by tournament. | Small status cards above ticket links. | Visibility of system status; planning support | F-P3 | Trust-sensitive ticket planning | Users know whether to act now or wait. | Requires reliable status data and governance. | High | Medium |
| F-S8 | F-D4 | Official availability alerts | Offer email and browser alerts by tournament and market, confirmed by receipt. | Alert drawer with checkbox list and next release note. | Memory load reduction; trust | F-P3 | Family travel planning over many days | Users stop manually rechecking availability. | Notification fatigue and opt-in compliance. | Medium | Medium |
| F-S9 | F-D5 | Utility rail on story pages | Add right rail or sticky side sheet for Scores today, Rankings latest, Tickets official source, Watch now. | Compact side module with four task cards. | Task continuity; reduced jumping | F-P1/F-P2/F-P3 | Reading story then switching task | Story readers can branch into utilitarian tasks in context. | May distract from article reading. | Medium | Low |
| F-S10 | F-D5 | Embedded action chips in articles | Add context chips in article header: Open Match Centre, View Tickets, Watch on FIFA+. | Chip row under headline metadata. | Contextual navigation; information scent | F-P1/F-P2/F-P3 | Tournament article with adjacent action need | Users can act from the article without searching navigation again. | Requires article metadata rules. | Medium | Low |
| C-S1 | C-D1 | Goal-based onboarding home | First-run chooser: Play now, Review last game, Learn basics, Solve puzzles, Join tournament. | Large task cards above default homepage feed. | Progressive disclosure; recognition over recall | C-P1/C-P2/C-P3 | First visit after signup | New users see goals before feature taxonomy. | Adds onboarding state management. | High | Medium |
| C-S2 | C-D1 | Personal dashboard mode | User pins top three tasks and hides unused modules for 30 days. | Compact home with pinned cards and Edit layout button. | Personalization; cognitive load reduction | C-P1/C-P2/C-P3 | Repeated use with stable goals | Homepage better matches user intent. | May hide growth paths if poorly explained. | Medium | Medium |
| C-S3 | C-D2 | Beginner analysis preset | One-click preset keeps evaluation bar, best move, and plain-language coach notes. | Preset chips at top of analysis panel: Beginner, Standard, Expert. | Progressive disclosure; low-friction defaults | C-P1 | Post-loss beginner review | Novices get a readable analysis surface. | Advanced controls become one step deeper. | High | Low |
| C-S4 | C-D2 | Inline analysis glossary | Hover or tap chart and toggle labels for plain-language explanations. | Right-side info drawer with What this means text. | Learnability; reduced memory load | C-P1/C-P3 | Analysis and Game Review study sessions | Users learn the meaning of graphs and labels in place. | Adds copy maintenance and localization work. | Medium | Medium |
| C-S5 | C-D3 | Upfront entitlement labels | Mark each lesson, puzzle, and analysis feature with access labels before click. | Small pill tags: Free, 3/day, 1 lesson/day, Diamond. | Expectation setting; error prevention | C-P1/C-P3 | Learning path selection | Users know limits before investing attention. | Access labels may add visual noise. | High | Low |
| C-S6 | C-D3 | Soft-landing after limit reached | After a limit wall, offer free alternative, reset timer, and queue for later. | Modal with Continue learning free, Save for later, Upgrade. | Continuity; frustration reduction | C-P1 | Study session after a daily limit | Users keep learning instead of stopping abruptly. | May reduce upgrade pressure. | Medium | Medium |
| C-S7 | C-D4 | Premove queue preview | Show pending premoves with danger icon when opponent reply tree makes risk high. | Tiny queue strip above board, first item tinted warning color. | Error prevention; system status | C-P2 | Blitz and bullet time trouble | Users see what will execute before it happens. | Risk estimate can be imperfect. | High | Medium |
| C-S8 | C-D4 | Fast clear shortcut | One-click Clear or Esc clears queued premove chain. | Small Clear premoves pill next to clocks or settings. | Recoverability; user control | C-P2 | Fast play after unexpected opponent move | Users recover from risky queued intent quickly. | Adds one more in-game control. | Medium | Low |
| C-S9 | C-D5 | First-time coachmark | After two full games, show Need fewer distractions? Try Focus Mode. | Tooltip near board corner. | Discoverability; contextual help | C-P2 | Post-game moment before next serious game | Users learn the hidden control when it is relevant. | Coachmarks can annoy expert users. | Medium | Low |
| C-S10 | C-D5 | Persistent settings shortcut | Add Focus Mode toggle into board settings and keyboard shortcut help. | Settings panel item with live preview thumbnail. | Consistency; discoverability | C-P2/C-P3 | Board settings and serious-game setup | Focus Mode becomes findable without hover discovery. | Settings panel grows slightly. | Medium | Low |

## Prioritized impact-effort matrix

| Solution | Concept | Priority | Effort | Rollout bucket |
| --- | --- | --- | --- | --- |
| F-S1 | Task-first global nav | High | Medium | Deeper redesign |
| F-S2 | Audience intent switcher | High | Low | Quick win |
| F-S3 | Handoff explainer card | High | Low | Quick win |
| F-S4 | Shared breadcrumb and visual bridge | Medium | Medium | Deeper redesign |
| F-S5 | Filter-first rail controls | High | Medium | Deeper redesign |
| F-S6 | Compact scan mode | Medium | Medium | Deeper redesign |
| F-S7 | Ticket status dashboard | High | Medium | Deeper redesign |
| F-S8 | Official availability alerts | Medium | Medium | Deeper redesign |
| F-S9 | Utility rail on story pages | Medium | Low | Quick win |
| F-S10 | Embedded action chips in articles | Medium | Low | Quick win |
| C-S1 | Goal-based onboarding home | High | Medium | Deeper redesign |
| C-S2 | Personal dashboard mode | Medium | Medium | Deeper redesign |
| C-S3 | Beginner analysis preset | High | Low | Quick win |
| C-S4 | Inline analysis glossary | Medium | Medium | Deeper redesign |
| C-S5 | Upfront entitlement labels | High | Low | Quick win |
| C-S6 | Soft-landing after limit reached | Medium | Medium | Deeper redesign |
| C-S7 | Premove queue preview | High | Medium | Deeper redesign |
| C-S8 | Fast clear shortcut | Medium | Low | Quick win |
| C-S9 | First-time coachmark | Medium | Low | Quick win |
| C-S10 | Persistent settings shortcut | Medium | Low | Quick win |

## Quick wins

| ID | Concept | Why first |
| --- | --- | --- |
| F-S2 | Audience intent switcher | High priority with Low effort; concrete UI can be tested without changing core architecture. |
| F-S3 | Handoff explainer card | High priority with Low effort; concrete UI can be tested without changing core architecture. |
| F-S9 | Utility rail on story pages | Medium priority with Low effort; concrete UI can be tested without changing core architecture. |
| F-S10 | Embedded action chips in articles | Medium priority with Low effort; concrete UI can be tested without changing core architecture. |
| C-S3 | Beginner analysis preset | High priority with Low effort; concrete UI can be tested without changing core architecture. |
| C-S5 | Upfront entitlement labels | High priority with Low effort; concrete UI can be tested without changing core architecture. |
| C-S8 | Fast clear shortcut | Medium priority with Low effort; concrete UI can be tested without changing core architecture. |
| C-S9 | First-time coachmark | Medium priority with Low effort; concrete UI can be tested without changing core architecture. |
| C-S10 | Persistent settings shortcut | Medium priority with Low effort; concrete UI can be tested without changing core architecture. |

## Deeper redesigns

| ID | Concept | Why deeper |
| --- | --- | --- |
| F-S1 | Task-first global nav | Requires cross-page, data, personalization, or cross-property coordination. |
| F-S4 | Shared breadcrumb and visual bridge | Requires cross-page, data, personalization, or cross-property coordination. |
| F-S5 | Filter-first rail controls | Requires cross-page, data, personalization, or cross-property coordination. |
| F-S6 | Compact scan mode | Requires cross-page, data, personalization, or cross-property coordination. |
| F-S7 | Ticket status dashboard | Requires cross-page, data, personalization, or cross-property coordination. |
| F-S8 | Official availability alerts | Requires cross-page, data, personalization, or cross-property coordination. |
| C-S1 | Goal-based onboarding home | Requires cross-page, data, personalization, or cross-property coordination. |
| C-S2 | Personal dashboard mode | Requires cross-page, data, personalization, or cross-property coordination. |
| C-S4 | Inline analysis glossary | Requires cross-page, data, personalization, or cross-property coordination. |
| C-S6 | Soft-landing after limit reached | Requires cross-page, data, personalization, or cross-property coordination. |
| C-S7 | Premove queue preview | Requires cross-page, data, personalization, or cross-property coordination. |

## Rollout plan

Sprint 1 implements quick wins, tests wording and UI placement, and validates with the personas most affected by each drawback. Sprint 2 handles task-first navigation, ticket status, FIFA+ filters, personalized Chess.com home, glossary behavior, and premove queue preview. QA checks that every drawback from ProductResearch still maps to exactly two solutions.

## References
[1] Inside FIFA. Official FIFA news and navigation. https://inside.fifa.com/. Accessed 2026-06-10. Supports: Inside FIFA exposes Latest FIFA News and the global navigation labels Match Centre, News, Rankings, Tickets & Hospitality, Play, Inside FIFA, plus sibling destinations such as FIFA+, Store, Collect, and Rewards.
[2] All stories & topics. Official FIFA topic index. https://inside.fifa.com/all-stories. Accessed 2026-06-10. Supports: The all stories page supports exploratory browsing through categories, content types, articles, blogs, media releases, videos, and albums.
[4] FIFA World Cup 26 Ticketing Programme launches this September. Official FIFA media release. https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september. Accessed 2026-06-10. Supports: FIFA directs fans to FIFA.com/tickets to register interest, create a FIFA ID, and follow phased ticket releases.
[5] FIFA World Cup 2026 Last-Minute Sales Phase. Official FIFA media release. https://inside.fifa.com/media-releases/last-minute-ticket-sales-phase-fifa-world-cup-2026. Accessed 2026-06-10. Supports: FIFA.com/tickets is identified as the official and preferred ticket source; fans are asked to check it regularly; the official Resale/Exchange Marketplace is available for eligible ticket holders.
[6] Watch FIFA+ Live Stream Online. Official FIFA+ watch destination. https://www.plus.fifa.com/. Accessed 2026-06-10. Supports: FIFA+ presents a watch surface with sign-in or get-started controls, live or upcoming content, highlights, replays, documentaries, and archive content. The FIFA+ destination is presented through a DAZN-branded page.
[9] Tickets & Hospitality. Official FIFA tickets page. https://www.fifa.com/en/tickets. Accessed 2026-06-10. Supports: The tickets URL is the official entry point for first-hand FIFA tournament ticket and hospitality information; the page is client-side rendered in crawled text.
[10] Chess.com homepage. Official Chess.com homepage. https://www.chess.com/. Accessed 2026-06-10. Supports: The homepage foregrounds Play, Puzzles, Learn, Train, Watch, Community, Get Started, lessons, bots, puzzles, and watching events.
[11] How do I start a game on Chess.com?. Official Chess.com help. https://support.chess.com/en/articles/8609779-how-do-i-start-a-game-on-chess-com. Accessed 2026-06-10. Supports: Users can start games from the homescreen or site-wide Play menu, using recent time control, custom settings, random opponent, bots, or friends.
[12] What are pre-moves and how do they work?. Official Chess.com help. https://support.chess.com/en/articles/8562432-what-are-pre-moves-and-how-do-they-work. Accessed 2026-06-10. Supports: Premoves can be enabled and then entered while it is the opponent's turn; the feature saves time but executes automatically if legal.
[13] What is focus mode? How do I turn it on?. Official Chess.com help. https://support.chess.com/en/articles/8588088-what-is-focus-mode-how-do-i-turn-it-on. Accessed 2026-06-10. Supports: Focus Mode minimizes distractions by expanding the board and showing only the board, clocks, draw, and resign controls.
[14] How do I change my board size?. Official Chess.com help. https://support.chess.com/en/articles/8609533-how-do-i-change-my-board-size. Accessed 2026-06-10. Supports: Board settings, Focus Mode, Theatre Mode, and Flip Board appear when hovering near the board/sidebar boundary, creating a discoverability issue for hidden controls.
[15] How does Game Review work?. Official Chess.com help. https://support.chess.com/en/articles/8584089-how-does-game-review-work. Accessed 2026-06-10. Supports: Game Review appears after a game and provides a detailed review flow with accuracy, move classifications, key moves, coach guidance, graphs, and retry learning.
[17] How do I use the analysis board?. Official Chess.com help. https://support.chess.com/en/articles/8583825-how-do-i-use-the-analysis-board. Accessed 2026-06-10. Supports: The Analysis Board supports direct manipulation, setup position, FEN/PGN loading, game history, collections, engine settings, evaluation bar, lines, arrows, and move feedback.
[19] How do Lessons work on Chess.com?. Official Chess.com help. https://support.chess.com/en/articles/8609703-how-do-lessons-work-on-chess-com. Accessed 2026-06-10. Supports: Lessons are reached from Learn, use interactive practice challenges, and include access limits by membership level.
[20] Chess Study Plans for All Levels. Official Chess.com article. https://www.chess.com/article/view/study-plan-directory. Accessed 2026-06-10. Supports: Study plans guide players by skill level and help organize training time through curated lessons and videos.
