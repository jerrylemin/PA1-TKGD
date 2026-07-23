# Visual Reconnaissance: FIFA.com and Chess.com

Date: 2026-06-11

Method: real Chromium sessions were run through Playwright with desktop `1440x1000`, tablet `768x1024`, and mobile `390x844` viewports. The interactive `js_repl` runtime required by the Playwright Interactive skill was not exposed in this Codex session, so the reconnaissance followed the skill workflow with persistent real-browser visual checks, local screenshots, and sampled image inspection.

## FIFA.com Screenshot Plan

| Figure | URL | Viewport | Screen state | Important UI regions | Possible HCI finding | Screenshot filename | Login required | Popup/banner | Manual capture |
|---|---|---:|---|---|---|---|---|---|---|
| F-01 | https://www.fifa.com/en | desktop | Home page above the fold | hero, countdown, top navigation, account/search icons | visual hierarchy and attention compete with quick match tasks | fifa_home_desktop.png | No | Dismissible privacy banner handled | No |
| F-02 | https://www.fifa.com/en | desktop | Navigation visible | tournaments, match centre, news, rankings, tickets, more | recognition over recall for official sections | fifa_navigation_desktop.png | No | Dismissible privacy banner handled | No |
| F-03 | https://www.fifa.com/en | mobile | Mobile navigation/header area | logo, search, account, menu, hero cards | progressive disclosure and hidden navigation cost | fifa_navigation_mobile.png | No | concert modal observed on mobile | No |
| F-04 | https://www.fifa.com/en/match-centre | desktop | Match Centre | search, date rail, live toggle, fixture rows, sort/filter | date and fixture model supports today's match task | fifa_match_centre_desktop.png | No | Dismissible privacy banner handled | No |
| F-04M | https://www.fifa.com/en/match-centre | mobile | Mobile Match Centre | date row, match cards, filter/sort | mobile scan cost for fixtures | fifa_match_centre_mobile.png | No | Dismissible privacy banner handled | No |
| F-05 | https://www.fifa.com/en/search?q=world%20cup | desktop | Search/discovery URL | search page shell and query results area | official lookup needs clear category separation | fifa_search_desktop.png | No | Dismissible privacy banner handled | No |
| F-06 | FIFA media release URL | desktop | News article | headline/article body and metadata | article density and reading load | fifa_news_article_desktop.png | No | Dismissible privacy banner handled | No |
| F-06M | FIFA media release URL | mobile | News article mobile | headline, body, stacked content | mobile reading load in interrupted contexts | fifa_news_article_mobile.png | No | Dismissible privacy banner handled | No |
| F-07 | FIFA World Cup 2026 tournament URL | desktop | Competition page | tournament hero and content modules | tournament discovery and information architecture | fifa_competition_desktop.png | No | Dismissible privacy banner handled | No |
| F-08 | https://www.fifa.com/en | mobile | Mobile home with observed concert modal | modal, countdown, hero content behind overlay | interruption and attention capture on mobile | fifa_home_mobile.png | No | concert modal remained visible | No |
| F-09B | https://www.fifa.com/en | desktop | Footer | footer links, language/ecosystem area | international support and utility links | fifa_footer_desktop.png | No | Dismissible privacy banner handled | No |
| F-10B | https://www.plus.fifa.com/ | desktop | FIFA+ media destination | sign-in/get-started, content rails, media handoff | watch handoff and brand/context continuity | fifa_video_or_media_desktop.png | Account may be needed for playback | handled where possible | No |

## Chess.com Screenshot Plan

| Figure | URL | Viewport | Screen state | Important UI regions | Possible HCI finding | Screenshot filename | Login required | Popup/banner | Manual capture |
|---|---|---:|---|---|---|---|---|---|---|
| C-01 | https://www.chess.com/ | desktop | Home page | side navigation, play/get-started, learning content | strong task signposting | chess_home_desktop.png | No | none blocking | No |
| C-02 | https://www.chess.com/play/online | desktop | Online play | board, clock, time control, start game, challenge buttons | fast play entry and status visibility | chess_play_desktop.png | No for visible setup | ads visible | No |
| C-02M | https://www.chess.com/play/online | mobile | Online play mobile | compact board and start controls | motor accuracy and touch constraints | chess_play_mobile.png | No for visible setup | none blocking | No |
| C-03 | https://www.chess.com/play/computer | desktop | Demo/computer board | board, controls, opponent area | direct manipulation and board metaphor | chess_board_or_demo_desktop.png | No for visible setup | none blocking | No |
| C-04 | https://www.chess.com/puzzles | desktop | Puzzle page | puzzle modal/board, solve path | feedback and onboarding in puzzle flow | chess_puzzles_desktop.png | No for visible setup | puzzle intro modal observed | No |
| C-04M | https://www.chess.com/puzzles | mobile | Puzzle page mobile | compact puzzle prompt and board area | touch target and visual density | chess_puzzles_mobile.png | No for visible setup | puzzle intro modal observed | No |
| C-05 | https://www.chess.com/lessons | desktop | Learn page | lesson categories and entry points | beginner path and progressive disclosure | chess_learn_desktop.png | No for visible setup | none blocking | No |
| C-06 | https://www.chess.com/ | desktop | Navigation | Play, Puzzles, Learn, Train, Watch, Community, Other | navigation density and memory load | chess_navigation_desktop.png | No | none blocking | No |
| C-06M | https://www.chess.com/ | mobile | Mobile navigation | collapsed/stacked mobile header and menu access | hidden navigation cost | chess_navigation_mobile.png | No | none blocking | No |
| C-08 | https://www.chess.com/ | mobile | Mobile home | mobile task entry and sign-up prompts | touch target and attention constraints | chess_home_mobile.png | No | none blocking | No |
| C-09B | https://www.chess.com/news | desktop | News page | article list and content categories | shift from action to reading mode | chess_news_desktop.png | No | none blocking | No |
| C-10B | https://www.chess.com/login | desktop | Account prompt | login fields, sign-in entry, account route | interruption and user control before personalized play | chess_account_or_prompt_desktop.png | Login page itself | none blocking | No |

## Reconnaissance Notes

- FIFA.com supports a browse-first model with high-level official navigation, Match Centre, tournament pages, news/media pages, tickets, and FIFA+ handoff.
- FIFA.com Match Centre evidence shows date navigation, search, live toggle, sorting/filtering, and fixture rows.
- FIFA.com mobile home showed an on-site promotional modal; this is retained as evidence for attention interruption because it was a real observed screen state.
- Chess.com supports an action-first model with persistent task navigation, online play setup, visible board metaphors, puzzles, lessons, news, and account entry.
- Chess.com play evidence shows board, clocks, game-start controls, custom challenge, friend play, and tournament entry.
- Chess.com puzzle evidence shows onboarding/intro modal over a puzzle board, supporting the claim that learning feedback appears in layered task states.

Decision gate: both products have a complete screenshot plan and automated captures for the required screens.
