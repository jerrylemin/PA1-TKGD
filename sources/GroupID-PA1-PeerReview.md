# GroupID-PA1 Peer Review Preparation: FIFA and Chess.com

## Seven-minute script

Member1 opens by naming the pair: FIFA and Chess.com web experiences. The first contrast is task posture: FIFA is browse, compare, and follow, while Chess.com is do, review, and improve. Member1 then explains the official-source protocol and why numbered references are used. Member2 introduces six personas and emphasizes context: short campus browsing, office scanning, trust-sensitive ticket planning, beginner learning, blitz play, and deep review. Member3 presents FIFA findings, starting with navigation and official ticket trust, then moving into the drawbacks of ecosystem sprawl, FIFA+ continuity, dense watch rails, ticket status uncertainty, and article-to-utility friction. Member4 presents Chess.com findings, showing how Play, Puzzles, Learn, Game Review, Analysis, and Study Plans support action and reflection, then explaining risks from feature overload, premove execution, hidden Focus Mode controls, and complex analysis screens. Member4 closes the design portion with quick wins and deeper redesigns. Member5 finishes with the two-week RUP plus Scrum plan, peer-review feedback loop, citation QA, PDF text extraction, old-term scan, and zip packaging.

## Slide outline

| Slide | Topic | Purpose | Speaker | Time |
| --- | --- | --- | --- | --- |
| 1 | Scope and selected pair | FIFA browse-first web ecosystem and Chess.com action-first web platform; Figure F-01 and Figure C-01 | Member1 | 0:45 |
| 2 | Evidence method and official source protocol | Official pages first; Playwright screenshots and manifest; Figure F-04 and Figure C-02 | Member1 | 0:55 |
| 3 | Personas and contexts | Six personas with task, device, attention, trust, and learning contexts; Figure F-08 and Figure C-08 | Member2 | 1:00 |
| 4 | FIFA findings | Navigation, Match Centre, mobile interruption, article density, and handoff drawbacks; Figure F-02, Figure F-04, Figure F-06, Figure F-08 | Member3 | 1:10 |
| 5 | Chess.com findings | Play, board, puzzles, Learn, navigation, and feedback density; Figure C-02, Figure C-03, Figure C-04, Figure C-05, Figure C-06 | Member4 | 1:10 |
| 6 | Solution priorities | Quick wins versus deeper redesigns and impact-effort rationale; Figure S-01 to Figure S-08 | Member4 | 1:10 |
| 7 | Sprint plan, QA, and packaging | Two-week RUP plus Scrum process, visual QA, PDF regeneration, zip validation; Figure F-09 and Figure C-09 | Member5 | 0:50 |

## Likely questions and prepared answers

| Question | Prepared answer |
| --- | --- |
| Why pair FIFA with Chess.com? | They are both high-traffic web experiences, but FIFA is browse-first while Chess.com is action-first, so the contrast exposes different HCI tradeoffs. |
| Which site is stronger for fast task completion? | Chess.com is stronger for immediate action because Play is primary and the start-game flow is short. FIFA is fast for official labels but slower when tasks cross properties. |
| Which site carries more scan load? | FIFA+ and Chess.com analysis both carry scan load; FIFA+ uses dense rails, while Chess.com analysis exposes charts, toggles, lines, and access expectations. |
| Which site shows better feedback after action? | Chess.com, because Game Review and Analysis provide graph, classifications, retry, and engine feedback after a completed game. |
| Why is FIFA+ a continuity problem? | The user moves from FIFA information pages to a DAZN-branded watch page with sign-in/get-started controls, creating trust and mode-boundary friction. |
| Why is premove both a feature and a risk? | It saves time in blitz, but it can legally execute after an unexpected reply and create a blunder. |
| How did the team avoid generic UX claims? | Every finding names page or flow, control, user, context, principle, scenario, severity, and evidence. |
| Which redesign gives best impact for effort? | F-S3 and C-S3 are strong low-effort wins: the handoff explainer reduces trust friction and the beginner analysis preset reduces cognitive load. |

## Mock feedback entries

| Reviewer | Role | Feedback | Response/revision | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| Nora Lee | Peer | FIFA ticket trust needs a stronger official-source cue. | Added F-HCI3, F-D4, F-S7, and F-S8 with FIFA.com/tickets citations. | Member3 | Done |
| Omar Khan | Peer | Explain why FIFA+ is not just another page. | Added DAZN-branded handoff risk, explainer card, and shared breadcrumb solution. | Member4 | Done |
| Jin Park | Peer | Chess.com beginner analysis sounds too expert-focused. | Added C-S3 beginner preset and C-S4 inline glossary. | Member4 | Done |
| Mira Vo | Peer | Premove needs an error-prevention solution. | Added premove queue preview and fast clear shortcut. | Member4 | Done |
| Sam Patel | Peer | Focus Mode discovery should cite the hover behavior. | Linked C-HCI9 to board-size and Focus Mode support pages. | Member3 | Done |
| Hana Lim | Peer | The pair needs a clearer comparison logic. | Reframed FIFA as browse, compare, follow and Chess.com as do, review, improve. | Member1 | Done |
| Leo Tran | Peer | Weekly plan must show QA and packaging. | Added Day 13 and Day 14 validation tasks and zip checks. | Member5 | Done |
| Ivy Chen | Peer | Mockups should not imply invented screenshots. | Changed all mockups to written UI descriptions only. | Member4 | Done |

## Revision log and owner mapping

| Revision area | Owner | Evidence of change |
| --- | --- | --- |
| Scope | Member1 | Product pair and cross-product framing locked |
| Personas/use cases | Member2 | Six personas and ten detailed use cases |
| HCI findings | Member3 | Twenty findings with scenario and citation |
| Solutions | Member4 | Ten drawbacks and twenty UI-level solutions |
| QA/package | Member5 | PDF extraction, old-term scan, and zip validation |

## Rehearsal checklist

- Check 1: First slide names FIFA and Chess.com only.
- Check 2: Method slide explains official-source-first evidence.
- Check 3: Persona slide ties each person to a context and task.
- Check 4: FIFA slide includes benefits and drawbacks with concrete controls.
- Check 5: Chess.com slide includes play, review, analysis, learning, premove, and Focus Mode.
- Check 6: Solution slide states UI behavior, effect, tradeoff, priority, and effort.
- Check 7: Close names regenerated PDFs and top-level zip.
- Check 8: Q&A uses HCI reasoning instead of generic praise.

## References
[1] Inside FIFA. Official FIFA news and navigation. https://inside.fifa.com/. Accessed 2026-06-10. Supports: Inside FIFA exposes Latest FIFA News and the global navigation labels Match Centre, News, Rankings, Tickets & Hospitality, Play, Inside FIFA, plus sibling destinations such as FIFA+, Store, Collect, and Rewards.
[5] FIFA World Cup 2026 Last-Minute Sales Phase. Official FIFA media release. https://inside.fifa.com/media-releases/last-minute-ticket-sales-phase-fifa-world-cup-2026. Accessed 2026-06-10. Supports: FIFA.com/tickets is identified as the official and preferred ticket source; fans are asked to check it regularly; the official Resale/Exchange Marketplace is available for eligible ticket holders.
[6] Watch FIFA+ Live Stream Online. Official FIFA+ watch destination. https://www.plus.fifa.com/. Accessed 2026-06-10. Supports: FIFA+ presents a watch surface with sign-in or get-started controls, live or upcoming content, highlights, replays, documentaries, and archive content. The FIFA+ destination is presented through a DAZN-branded page.
[10] Chess.com homepage. Official Chess.com homepage. https://www.chess.com/. Accessed 2026-06-10. Supports: The homepage foregrounds Play, Puzzles, Learn, Train, Watch, Community, Get Started, lessons, bots, puzzles, and watching events.
[11] How do I start a game on Chess.com?. Official Chess.com help. https://support.chess.com/en/articles/8609779-how-do-i-start-a-game-on-chess-com. Accessed 2026-06-10. Supports: Users can start games from the homescreen or site-wide Play menu, using recent time control, custom settings, random opponent, bots, or friends.
[12] What are pre-moves and how do they work?. Official Chess.com help. https://support.chess.com/en/articles/8562432-what-are-pre-moves-and-how-do-they-work. Accessed 2026-06-10. Supports: Premoves can be enabled and then entered while it is the opponent's turn; the feature saves time but executes automatically if legal.
[13] What is focus mode? How do I turn it on?. Official Chess.com help. https://support.chess.com/en/articles/8588088-what-is-focus-mode-how-do-i-turn-it-on. Accessed 2026-06-10. Supports: Focus Mode minimizes distractions by expanding the board and showing only the board, clocks, draw, and resign controls.
[14] How do I change my board size?. Official Chess.com help. https://support.chess.com/en/articles/8609533-how-do-i-change-my-board-size. Accessed 2026-06-10. Supports: Board settings, Focus Mode, Theatre Mode, and Flip Board appear when hovering near the board/sidebar boundary, creating a discoverability issue for hidden controls.
[15] How does Game Review work?. Official Chess.com help. https://support.chess.com/en/articles/8584089-how-does-game-review-work. Accessed 2026-06-10. Supports: Game Review appears after a game and provides a detailed review flow with accuracy, move classifications, key moves, coach guidance, graphs, and retry learning.
[17] How do I use the analysis board?. Official Chess.com help. https://support.chess.com/en/articles/8583825-how-do-i-use-the-analysis-board. Accessed 2026-06-10. Supports: The Analysis Board supports direct manipulation, setup position, FEN/PGN loading, game history, collections, engine settings, evaluation bar, lines, arrows, and move feedback.
[20] Chess Study Plans for All Levels. Official Chess.com article. https://www.chess.com/article/view/study-plan-directory. Accessed 2026-06-10. Supports: Study plans guide players by skill level and help organize training time through curated lessons and videos.
[22] Cheating And Fair Play On Chess.com. Official Chess.com fair-play page. https://www.chess.com/cheating. Accessed 2026-06-10. Supports: The fair-play page explains competitive integrity, account closures, fair-play policy, event checks, and enforcement expectations.
