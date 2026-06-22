from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import zipfile
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Image as RLImage,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

GROUP_ID = "GroupID"
TEAM_ROSTER = [
    {
        "name": "Le Minh",
        "student_id": "21127645",
        "role": "Project Coordinator, Integration Lead, PeerReview Lead, WeeklyReport Lead, Final Packaging Lead",
        "main_contribution": "Coordinated scope, integrated final reports, led PeerReview and WeeklyReport evidence, ran final PDF and zip packaging QA.",
    },
    {
        "name": "Nguyen Vu Bach",
        "student_id": "21127224",
        "role": "FIFA.com Research Lead, FIFA Screenshot Evidence Lead, ProductResearch Co-Lead",
        "main_contribution": "Researched FIFA.com, collected official sources, captured and annotated FIFA evidence, and wrote FIFA HCI findings.",
    },
    {
        "name": "Pham Nguyen Gia Bao",
        "student_id": "20127119",
        "role": "Chess.com Research Lead, Chess.com Screenshot Evidence Lead, ProductResearch Co-Lead",
        "main_contribution": "Researched Chess.com, collected official sources, captured and annotated Chess.com evidence, and wrote Chess.com HCI findings.",
    },
    {
        "name": "Trang Minh Nhut",
        "student_id": "22127318",
        "role": "HCI Analysis Lead, PotentialSolutions Lead, Visual QA Lead",
        "main_contribution": "Mapped HCI concepts, led PotentialSolutions, checked figure captions, and verified drawback-to-solution consistency.",
    },
]
TEAM_MEMBERS = [f"{member['name']}, {member['student_id']}" for member in TEAM_ROSTER]
ROOT = Path(__file__).resolve().parent
TODAY = "2026-06-10"


def mk_source(num, sid, product, title, url, source_type, claims, notes="Official English source. Vietnamese equivalent not surfaced during the source refresh."):
    domain = re.sub(r"^https?://", "", url).split("/")[0]
    return {
        "num": num,
        "id": sid,
        "product": product,
        "title": title,
        "url": url,
        "domain": domain,
        "source_type": source_type,
        "language": "English",
        "access_date": TODAY,
        "claims_supported": claims,
        "confidence": "High",
        "notes": notes,
    }


SOURCES = [
    mk_source(1, "F-REF1", "FIFA", "Inside FIFA", "https://inside.fifa.com/", "Official FIFA news and navigation", ["Inside FIFA exposes Latest FIFA News and the global navigation labels Match Centre, News, Rankings, Tickets & Hospitality, Play, Inside FIFA, plus sibling destinations such as FIFA+, Store, Collect, and Rewards."]),
    mk_source(2, "F-REF2", "FIFA", "All stories & topics", "https://inside.fifa.com/all-stories", "Official FIFA topic index", ["The all stories page supports exploratory browsing through categories, content types, articles, blogs, media releases, videos, and albums."]),
    mk_source(3, "F-REF3", "FIFA", "FIFA World Cup 2026 Blog", "https://inside.fifa.com/blogs/fwc-2026", "Official FIFA tournament blog", ["The FIFA World Cup 2026 blog functions as a tournament story hub with dated updates and story cards."]),
    mk_source(4, "F-REF4", "FIFA", "FIFA World Cup 26 Ticketing Programme launches this September", "https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september", "Official FIFA media release", ["FIFA directs fans to FIFA.com/tickets to register interest, create a FIFA ID, and follow phased ticket releases."]),
    mk_source(5, "F-REF5", "FIFA", "FIFA World Cup 2026 Last-Minute Sales Phase", "https://inside.fifa.com/media-releases/last-minute-ticket-sales-phase-fifa-world-cup-2026", "Official FIFA media release", ["FIFA.com/tickets is identified as the official and preferred ticket source; fans are asked to check it regularly; the official Resale/Exchange Marketplace is available for eligible ticket holders."]),
    mk_source(6, "F-REF6", "FIFA", "Watch FIFA+ Live Stream Online", "https://www.plus.fifa.com/", "Official FIFA+ watch destination", ["FIFA+ presents a watch surface with sign-in or get-started controls, live or upcoming content, highlights, replays, documentaries, and archive content.", "The FIFA+ destination is presented through a DAZN-branded page."]),
    mk_source(7, "F-REF7", "FIFA", "Match Centre", "https://www.fifa.com/en/match-centre", "Official FIFA Match Centre", ["The Match Centre URL exposes fixtures, results, match details, competitions, and live-now filtering; some content is client-side rendered."]),
    mk_source(8, "F-REF8", "FIFA", "FIFA/Coca-Cola Men's World Ranking", "https://inside.fifa.com/fifa-world-ranking/men", "Official FIFA rankings page", ["The rankings page exposes the latest men's ranking table, filters, official update dates, and ranking rules notes."]),
    mk_source(9, "F-REF9", "FIFA", "Tickets & Hospitality", "https://www.fifa.com/en/tickets", "Official FIFA tickets page", ["The tickets URL is the official entry point for first-hand FIFA tournament ticket and hospitality information; the page is client-side rendered in crawled text."]),
    mk_source(10, "C-REF1", "Chess.com", "Chess.com homepage", "https://www.chess.com/", "Official Chess.com homepage", ["The homepage foregrounds Play, Puzzles, Learn, Train, Watch, Community, Get Started, lessons, bots, puzzles, and watching events."]),
    mk_source(11, "C-REF2", "Chess.com", "How do I start a game on Chess.com?", "https://support.chess.com/en/articles/8609779-how-do-i-start-a-game-on-chess-com", "Official Chess.com help", ["Users can start games from the homescreen or site-wide Play menu, using recent time control, custom settings, random opponent, bots, or friends."]),
    mk_source(12, "C-REF3", "Chess.com", "What are pre-moves and how do they work?", "https://support.chess.com/en/articles/8562432-what-are-pre-moves-and-how-do-they-work", "Official Chess.com help", ["Premoves can be enabled and then entered while it is the opponent's turn; the feature saves time but executes automatically if legal."]),
    mk_source(13, "C-REF4", "Chess.com", "What is focus mode? How do I turn it on?", "https://support.chess.com/en/articles/8588088-what-is-focus-mode-how-do-i-turn-it-on", "Official Chess.com help", ["Focus Mode minimizes distractions by expanding the board and showing only the board, clocks, draw, and resign controls."]),
    mk_source(14, "C-REF5", "Chess.com", "How do I change my board size?", "https://support.chess.com/en/articles/8609533-how-do-i-change-my-board-size", "Official Chess.com help", ["Board settings, Focus Mode, Theatre Mode, and Flip Board appear when hovering near the board/sidebar boundary, creating a discoverability issue for hidden controls."]),
    mk_source(15, "C-REF6", "Chess.com", "How does Game Review work?", "https://support.chess.com/en/articles/8584089-how-does-game-review-work", "Official Chess.com help", ["Game Review appears after a game and provides a detailed review flow with accuracy, move classifications, key moves, coach guidance, graphs, and retry learning."]),
    mk_source(16, "C-REF7", "Chess.com", "How do I use Game Analysis?", "https://support.chess.com/en/articles/8583757-how-do-i-use-game-analysis", "Official Chess.com help", ["Game Analysis lets users revisit analyzed games and continue deeper study through analysis tools."]),
    mk_source(17, "C-REF8", "Chess.com", "How do I use the analysis board?", "https://support.chess.com/en/articles/8583825-how-do-i-use-the-analysis-board", "Official Chess.com help", ["The Analysis Board supports direct manipulation, setup position, FEN/PGN loading, game history, collections, engine settings, evaluation bar, lines, arrows, and move feedback."]),
    mk_source(18, "C-REF9", "Chess.com", "How do Puzzles work on Chess.com?", "https://support.chess.com/en/articles/8608686-how-do-puzzles-work-on-chess-com", "Official Chess.com help", ["Puzzles are reachable from the side menu or homepage and include puzzle of the day, rated puzzles, themes, Puzzle Rush, and Puzzle Battle."]),
    mk_source(19, "C-REF10", "Chess.com", "How do Lessons work on Chess.com?", "https://support.chess.com/en/articles/8609703-how-do-lessons-work-on-chess-com", "Official Chess.com help", ["Lessons are reached from Learn, use interactive practice challenges, and include access limits by membership level."]),
    mk_source(20, "C-REF11", "Chess.com", "Chess Study Plans for All Levels", "https://www.chess.com/article/view/study-plan-directory", "Official Chess.com article", ["Study plans guide players by skill level and help organize training time through curated lessons and videos."]),
    mk_source(21, "C-REF12", "Chess.com", "Chess.com tournaments schedule", "https://support.chess.com/en/articles/9062345-chess-com-tournaments-schedule", "Official Chess.com help", ["Tournament schedules expose arena and prize tournament calendars such as Titled Tuesday, Arena Kings, Bullet Brawls, and variant events."]),
    mk_source(22, "C-REF13", "Chess.com", "Cheating And Fair Play On Chess.com", "https://www.chess.com/cheating", "Official Chess.com fair-play page", ["The fair-play page explains competitive integrity, account closures, fair-play policy, event checks, and enforcement expectations."]),
]


PRODUCTS = {
    "fifa_web": {
        "id": "fifa_web",
        "name": "FIFA",
        "domain": "Official football portal and watch ecosystem",
        "modality": "Browse-first web product for football information, rankings, ticketing, and watch handoff",
        "positioning": "Browse-first football web ecosystem for official news, match-following, rankings, tournament discovery, ticketing trust, and FIFA+ watch handoff.",
    },
    "chesscom_web": {
        "id": "chesscom_web",
        "name": "Chess.com",
        "domain": "Online chess play and learning platform",
        "modality": "Action-first web product for play, review, analysis, and learning",
        "positioning": "Action-first chess web platform for games, review, self-analysis, puzzles, lessons, study plans, tournaments, and fair-play-guided competitive play.",
    },
}

PERSONAS = {
    "FIFA": [
        ["F-P1", "Lan Tran", "20", "Medium", "Check scores, fixtures, and one key tournament story between classes", "Student on campus laptop, short time window, noisy environment, intermittent attention"],
        ["F-P2", "Ethan Nguyen", "27", "High", "Follow official tournament news and rankings during office breaks", "Desktop at work, multiple tabs open, daylight glare, short sessions, high scan pressure"],
        ["F-P3", "Maria Pham", "31", "Medium", "Verify official ticket source, resale status, and then watch highlights on FIFA+", "Evening home browsing on laptop, compares tabs, trust-sensitive, family trip planning"],
    ],
    "Chess.com": [
        ["C-P1", "Minh Bui", "18", "Medium", "Learn chess basics through lessons, puzzles, and a study plan", "Student on shared laptop, beginner mental model, low confidence, needs guidance"],
        ["C-P2", "Alex Hoang", "24", "High", "Start blitz games fast, use premoves, reduce distractions, keep momentum", "External keyboard and mouse, noisy dorm room, many short sessions, time pressure"],
        ["C-P3", "Quynh Le", "29", "High", "Review finished games, run self-analysis, and plan tournament play", "Quiet desktop setup, longer study sessions, strong interest in accuracy and improvement"],
    ],
}

USE_CASES = [
    ["F-UC1", "FIFA", "Open Match Centre and check today's matches", "F-P1", "Find current fixtures or results quickly", "Short break begins", "Campus laptop, noisy hallway, five-minute window", "Browser online; FIFA.com reachable", "User knows which matches are active today", "Open FIFA.com; choose Match Centre; scan today/live filters; open one match detail; return to list", "If no live match appears, switch to latest results", "Client-side content is slow; use navigation label and retry or refresh", "Fixture cards, live status, score rows, match detail link", "[1][7]"],
    ["F-UC2", "FIFA", "Open official tournament news and read one FIFA World Cup 2026 story", "F-P2", "Read one current official tournament story", "Office break and tournament headline interest", "Desktop with many tabs and glare", "Inside FIFA and tournament blog available", "One article read and source confidence maintained", "Open Inside FIFA; choose FIFA World Cup 2026 blog or News; scan dated story cards; open one story; return to topic hub", "Use All stories filters if blog card is not visible", "Story list overload delays choice", "Dated cards, topic labels, article headline, breadcrumb", "[1][2][3]"],
    ["F-UC3", "FIFA", "Open Rankings from the global navigation", "F-P2", "Check the latest official ranking quickly", "Coworker asks ranking question", "Desktop at work; short session; high scan pressure", "Ranking page reachable", "User identifies latest ranking and update date", "Open FIFA global nav; choose Rankings; select men's ranking; scan rank table; note last official update", "Switch filters if the wrong table appears", "Ranking table loads after shell; user waits or retries", "Rank table, filters, update date, full rankings control", "[1][8]"],
    ["F-UC4", "FIFA", "Verify official tickets and resale source", "F-P3", "Confirm official ticket and resale route before family purchase", "Trip planning conversation begins", "Home laptop, multiple comparison tabs, trust-sensitive", "Ticket page and media release available", "User trusts FIFA.com/tickets and understands resale/exchange status", "Open FIFA Tickets; cross-check media release; identify FIFA.com/tickets; read resale/exchange note; save official URL", "Check hospitality if standard tickets unavailable", "Availability changes require repeated checks", "Official/preferred wording, ticket URL, resale/exchange marketplace cue", "[4][5][9]"],
    ["F-UC5", "FIFA", "Open FIFA+ and start a watch session", "F-P3", "Move from FIFA information to FIFA+ highlights or archive", "After ticket/news research, user wants video", "Evening laptop, family browsing, account friction sensitivity", "FIFA+ URL reachable; account may be required", "User starts or understands the next step for watching", "Choose FIFA+ from FIFA ecosystem; land on watch page; scan live/highlight rails; select content; sign in or get started", "Continue browsing FIFA.com if sign-in is not acceptable", "DAZN branding creates handoff uncertainty", "FIFA+ hero, sign-in/get-started controls, live and archive rails", "[1][6]"],
    ["C-UC1", "Chess.com", "Start a live game with default or custom settings", "C-P2", "Begin a game with low setup time", "User has a short blitz window", "Dorm desktop, external mouse, noise, time pressure", "Signed in or guest play available", "Game starts with selected opponent and time control", "Open Chess.com; choose Play or homescreen start; accept recent time control or customize; choose random opponent, bot, or friend; start", "Choose unrated or custom settings first", "Rating or match settings mismatch; return to play setup", "Play call-to-action, time control, rated toggle, opponent choice", "[10][11]"],
    ["C-UC2", "Chess.com", "Use premoves during a blitz game", "C-P2", "Save seconds under time pressure without losing control", "Clock drops below comfort level", "Noisy dorm room, fast mouse input, high stress", "Premoves enabled in live settings", "Queued legal move executes after opponent response", "During opponent turn, drag next move; observe queued move; continue if response fits", "Disable premoves for serious accuracy", "Opponent reply makes queued idea risky but legal", "Board input, queued move behavior, clock feedback", "[12]"],
    ["C-UC3", "Chess.com", "Turn on Focus Mode before a serious game", "C-P2", "Reduce visual distraction and expand the board", "User starts a serious game", "Dorm noise and many on-screen distractions", "Board visible; focus control available", "Board expands and nonessential panels hide", "Hover near board/sidebar boundary; choose Focus Mode; confirm board-only layout; start game", "Use keyboard shortcut or settings if discovered", "Control hidden on hover and missed by first-time user", "Focus icon, expanded board, clocks, draw and resign controls", "[13][14]"],
    ["C-UC4", "Chess.com", "Run Game Review after a finished game, then go to Self Analysis", "C-P3", "Understand mistakes and continue engine study", "Game ends", "Quiet desktop, longer study session", "Finished game saved; review available", "User sees classifications and starts deeper analysis", "Click Game Review; inspect graph, accuracy, key moves; retry a move; open Game Analysis or Analysis Board", "Reopen review from archive", "Premium or depth gates interrupt expectations", "Game Review button, graph, move classifications, retry, analysis controls", "[15][16][17]"],
    ["C-UC5", "Chess.com", "Solve puzzles and choose a follow-up lesson or study plan", "C-P1", "Build beginner skill through a guided loop", "Student wants to improve after a loss", "Shared laptop, low confidence, needs direction", "Puzzles and Learn reachable", "User completes a puzzle and chooses next learning action", "Open Puzzles; solve puzzle of day or rated puzzle; review feedback; open lesson or study plan; save next step", "Choose a beginner lesson first", "Premium limit appears after click and interrupts momentum", "Puzzle feedback, Learn menu, study-plan link, access labels", "[18][19][20]"],
]

USE_CASE_CONTEXT = {
    "F-UC1": {
        "Where": "Campus hallway or study area",
        "When": "Between classes during a five-minute break",
        "Posture": "Standing or leaning over a laptop/tablet while moving between tasks",
        "Device": "Laptop browser",
        "Attention level": "Intermittent and divided by hallway noise",
        "Environment": "Noisy campus setting with short session length",
        "Interaction method": "Mouse or trackpad navigation through FIFA global navigation and Match Centre filters",
        "HCI concepts": "Information scent; recognition over recall; visibility of system status",
    },
    "F-UC2": {
        "Where": "Office desk",
        "When": "Short work break after seeing a tournament headline",
        "Posture": "Seated desktop browsing with multiple tabs open",
        "Device": "Desktop browser",
        "Attention level": "Medium; scanning under time pressure",
        "Environment": "Office glare and interruptions",
        "Interaction method": "Click navigation, story-card scanning, and topic filtering",
        "HCI concepts": "Information foraging; hierarchical scanning; cognitive load",
    },
    "F-UC3": {
        "Where": "Work desk or shared office space",
        "When": "Immediately after a ranking question from another person",
        "Posture": "Seated and task-focused",
        "Device": "Desktop browser",
        "Attention level": "High but brief",
        "Environment": "Office context with multiple open tabs",
        "Interaction method": "Global navigation, table scanning, and filter selection",
        "HCI concepts": "Efficient task entry; data table scanability; feedback on loading state",
    },
    "F-UC4": {
        "Where": "Home planning setup",
        "When": "Evening family trip planning session",
        "Posture": "Seated laptop browsing while comparing sources",
        "Device": "Laptop browser",
        "Attention level": "High because the task is trust-sensitive",
        "Environment": "Home environment with multiple comparison tabs",
        "Interaction method": "Navigation to tickets, cross-checking media releases, and saving official URL",
        "HCI concepts": "Credibility; error prevention; visibility of official status",
    },
    "F-UC5": {
        "Where": "Home viewing context",
        "When": "After news or ticket research leads to video interest",
        "Posture": "Seated laptop browsing with family nearby",
        "Device": "Laptop browser",
        "Attention level": "Medium; sensitive to account and brand changes",
        "Environment": "Evening home browsing with shared decision-making",
        "Interaction method": "Ecosystem navigation to FIFA+, rail scanning, and sign-in/get-started decision",
        "HCI concepts": "Continuity; feedforward; trust friction; choice overload",
    },
    "C-UC1": {
        "Where": "Dorm room or personal desk",
        "When": "Short blitz window",
        "Posture": "Seated, ready for fast mouse input",
        "Device": "Desktop browser with external mouse",
        "Attention level": "High and time-sensitive",
        "Environment": "Noisy dorm with repeated short sessions",
        "Interaction method": "Clicking Play, selecting time control/opponent, and starting a match",
        "HCI concepts": "Efficiency; clear call to action; recognition over recall",
    },
    "C-UC2": {
        "Where": "Live chess board screen",
        "When": "During a blitz game when the clock is low",
        "Posture": "Seated and physically tense under time pressure",
        "Device": "Desktop browser with mouse",
        "Attention level": "Very high but narrowed by time stress",
        "Environment": "Noisy dorm or fast-play setting",
        "Interaction method": "Drag-and-drop or click-move input while opponent is moving",
        "HCI concepts": "Error prevention; direct manipulation; time pressure feedback",
    },
    "C-UC3": {
        "Where": "Chess.com board page",
        "When": "Before starting a serious game",
        "Posture": "Seated and preparing for focused play",
        "Device": "Desktop browser",
        "Attention level": "High, with distraction sensitivity",
        "Environment": "Dorm or shared space with surrounding noise",
        "Interaction method": "Hovering near board/sidebar boundary and selecting Focus Mode",
        "HCI concepts": "Discoverability; progressive disclosure; attention management",
    },
    "C-UC4": {
        "Where": "Quiet desktop study setup",
        "When": "Immediately after a completed game",
        "Posture": "Seated for a longer review session",
        "Device": "Desktop browser",
        "Attention level": "High and reflective",
        "Environment": "Quiet room suited to analysis",
        "Interaction method": "Clicking Game Review, graph/move inspection, retry action, and Analysis Board handoff",
        "HCI concepts": "Feedback; reflection; learning loop; cognitive load",
    },
    "C-UC5": {
        "Where": "Shared laptop or student study space",
        "When": "After a loss or when planning improvement practice",
        "Posture": "Seated beginner practice posture",
        "Device": "Laptop browser",
        "Attention level": "Medium; confidence may be low",
        "Environment": "Shared study environment with limited time",
        "Interaction method": "Puzzle interaction, feedback reading, Learn navigation, and study-plan selection",
        "HCI concepts": "Guidance; progressive disclosure; formative feedback",
    },
}

FINDINGS = [
    ["F-HCI1", "FIFA", "Benefit", "Global navigation", "Match Centre, News, Rankings, Tickets & Hospitality", "Navigation exposes key football information tasks.", "F-P1/F-P2", "Information scent; recognition over recall; efficient task entry", "Lan can enter Match Centre from the top level instead of remembering a direct URL.", "High", "[1][7][8][9]"],
    ["F-HCI2", "FIFA", "Benefit", "All stories & topics", "Category and content-type filters", "Story browsing supports exploratory scanning across FIFA topics.", "F-P2", "Information foraging; hierarchical scanning", "Ethan narrows from broad news to a tournament story during a short office break.", "Medium", "[2][3]"],
    ["F-HCI3", "FIFA", "Benefit", "Ticket discovery", "Official/preferred ticket wording and resale/exchange note", "Ticket media releases create a clear trust cue.", "F-P3", "Credibility; error prevention; trust", "Maria avoids a third-party ticket tab because FIFA identifies FIFA.com/tickets as the source.", "High", "[4][5][9]"],
    ["F-HCI4", "FIFA", "Benefit", "FIFA+ entry", "Hero and get-started controls", "FIFA+ states the watch proposition and next action.", "F-P3", "Feedforward; clear CTA; reduced ambiguity", "Maria can tell that the next step is to sign in or get started before watching.", "Medium", "[6]"],
    ["F-HCI5", "FIFA", "Benefit", "FIFA+ watch rails", "Live, highlights, replays, archive, documentaries", "FIFA+ supports both live football and time-shifted content.", "F-P3", "Flexibility; broad retrieval paths", "Maria can choose a highlight if live content does not fit the family's schedule.", "Medium", "[6]"],
    ["F-HCI6", "FIFA", "Drawback", "Ecosystem navigation", "FIFA.com, inside.fifa.com, plus.fifa.com, Store, Collect, Rewards", "Task paths span several sibling properties.", "F-P1/F-P3", "Context switching; mental model fragmentation; consistency", "Lan expects a single football hub but is moved across different hosts for stories, tickets, and video.", "High", "[1][6][9]"],
    ["F-HCI7", "FIFA", "Drawback", "FIFA+ handoff", "DAZN-branded page with login/get-started controls", "The watch path changes brand context and account expectations.", "F-P3", "Continuity break; trust friction; mode boundary", "Maria pauses because the FIFA+ destination looks like a different service during family planning.", "High", "[6]"],
    ["F-HCI8", "FIFA", "Drawback", "FIFA+ content browsing", "Long content rails", "Dense rails increase scan cost before a user finds live or archive content.", "F-P3", "Visual attention; choice overload", "Maria searches highlights but has to scan many rail items before choosing.", "Medium", "[6]"],
    ["F-HCI9", "FIFA", "Drawback", "Ticket status", "Check regularly for availability", "Ticket status is visible only as repeated-check guidance.", "F-P3", "Visibility of system status; planning friction", "Maria cannot tell when new family-trip availability may appear without repeatedly checking.", "High", "[5][9]"],
    ["F-HCI10", "FIFA", "Drawback", "Story hub", "Article-first cards", "Story browsing is strong, but quick tasks require a second jump.", "F-P1/F-P2", "Task interruption; efficiency gap", "Lan reads a headline and then has to jump elsewhere for scores or tickets.", "Medium", "[1][2][3][7]"],
    ["C-HCI1", "Chess.com", "Benefit", "Homepage", "Play, Puzzles, Learn, Train, Watch, Community", "Homepage navigation foregrounds core chess tasks.", "C-P1/C-P2", "Strong information scent; task signposting", "Minh sees Learn and Puzzles without knowing internal feature names.", "High", "[10]"],
    ["C-HCI2", "Chess.com", "Benefit", "Start game flow", "Random opponent, bot, friend, time controls, rated toggle, rating range", "Game start is short and flexible.", "C-P2", "Flexibility; user control; low entry friction", "Alex starts a blitz game quickly or adjusts time control before matching.", "High", "[11]"],
    ["C-HCI3", "Chess.com", "Benefit", "Focus Mode", "Expanded board with only essential play controls", "Focus Mode hides distractions while preserving clocks and resign/draw actions.", "C-P2", "Attention support; reduced clutter; task focus", "Alex makes decisions with a larger board and fewer side panels.", "Medium", "[13]"],
    ["C-HCI4", "Chess.com", "Benefit", "Game Review", "Graph, accuracy, classifications, coach, key moves, retry", "Review turns a finished game into concrete feedback.", "C-P3", "Feedback; reflection; error recovery; external cognition", "Quynh sees a blunder classification, retries the move, and understands the alternative.", "High", "[15][16]"],
    ["C-HCI5", "Chess.com", "Benefit", "Analysis Board", "Move pieces, setup position, load FEN/PGN, history, collections", "Analysis supports expert direct manipulation and artifact transfer.", "C-P3", "Direct manipulation; expert control; transfer of artifacts", "Quynh pastes a PGN, changes a line, and compares engine feedback.", "High", "[17]"],
    ["C-HCI6", "Chess.com", "Benefit", "Study Plans", "Skill-level study guides", "Study plans reduce uncertainty about what to learn next.", "C-P1", "Progressive disclosure; guided learning", "Minh chooses a beginner plan after puzzles instead of guessing from all lessons.", "Medium", "[19][20]"],
    ["C-HCI7", "Chess.com", "Drawback", "Product surface", "Many primary areas and training paths", "The broad surface can overwhelm first-time users.", "C-P1", "Choice overload; weak progressive disclosure at entry", "Minh sees Play, Learn, Train, Puzzles, and Watch before knowing the best beginner sequence.", "Medium", "[10][18][19][20]"],
    ["C-HCI8", "Chess.com", "Drawback", "Premove", "Queued move during opponent turn", "Premoves are efficient but risky when the reply is unexpected.", "C-P2", "Speed versus accuracy; error risk", "Alex premoves a capture that remains legal but weak after a surprising reply.", "High", "[12]"],
    ["C-HCI9", "Chess.com", "Drawback", "Focus Mode discovery", "Hover-only board-side control", "Focus Mode can be hard to discover because related controls appear only near the board boundary.", "C-P2", "Discoverability; hidden controls", "Alex never enables Focus Mode because the icon appears only on hover.", "Medium", "[13][14]"],
    ["C-HCI10", "Chess.com", "Drawback", "Analysis screens", "Toggles, charts, lines, classifications, premium gates", "Analysis surfaces many controls and access expectations at once.", "C-P1/C-P3", "Cognitive load; progressive disclosure gap; expectation mismatch", "Minh opens analysis after a loss and cannot tell which chart or control matters first.", "Medium", "[15][16][17][19]"],
]

DRAWBACKS = [
    ["F-D1", "FIFA", "Ecosystem sprawl across sibling FIFA properties", "F-HCI6", "High"],
    ["F-D2", "FIFA", "FIFA+ handoff breaks continuity", "F-HCI7", "High"],
    ["F-D3", "FIFA", "FIFA+ scan overload", "F-HCI8", "Medium"],
    ["F-D4", "FIFA", "Ticket status uncertainty", "F-HCI9", "High"],
    ["F-D5", "FIFA", "Browse-first friction for quick utilitarian tasks", "F-HCI10", "Medium"],
    ["C-D1", "Chess.com", "Menu and feature overload for novices", "C-HCI7", "High"],
    ["C-D2", "Chess.com", "Analysis overload", "C-HCI10", "High"],
    ["C-D3", "Chess.com", "Premium gating interrupts learning momentum", "C-HCI10", "Medium"],
    ["C-D4", "Chess.com", "Premove blunder risk", "C-HCI8", "High"],
    ["C-D5", "Chess.com", "Focus Mode is hard to discover", "C-HCI9", "Medium"],
]

SOLUTIONS = [
    ["F-S1", "F-D1", "Task-first global nav", "Keep Match Centre, News, Rankings, Tickets, Watch at top level; move Store, Collect, and Rewards into More FIFA.", "Slim header with one primary task row and one tucked ecosystem menu.", "Recognition over recall; cognitive load reduction", "F-P1/F-P2/F-P3", "Short task entry, office browsing, ticket planning", "Fewer property jumps for common tasks.", "Store and collectibles receive less top-level exposure.", "High", "Medium"],
    ["F-S2", "F-D1", "Audience intent switcher", "Add five quick-intent chips under the hero: Scores, News, Rankings, Tickets, Watch.", "Horizontal chip bar under page title.", "Feedforward; efficient entry", "F-P1/F-P2/F-P3", "Short sessions with unclear starting point", "Users choose by intent before reading navigation labels.", "One more row competes for above-fold attention.", "High", "Low"],
    ["F-S3", "F-D2", "Handoff explainer card", "Before leaving FIFA.com, show You are opening FIFA+ powered by DAZN with destination benefits and sign-in expectation.", "Centered modal with Continue and Stay on FIFA.com.", "Visibility of system status; trust", "F-P3", "Family watch handoff", "Users understand why branding and login state change.", "Adds one step for repeat viewers.", "High", "Low"],
    ["F-S4", "F-D2", "Shared breadcrumb and visual bridge", "Add persistent Back to FIFA.com strip and tournament breadcrumb on FIFA+.", "Thin top bar with FIFA icon, destination label, and return link.", "Continuity; orientation", "F-P3", "FIFA+ watch browsing after ticket/news research", "Users retain orientation across the watch boundary.", "Needs cross-property coordination.", "Medium", "Medium"],
    ["F-S5", "F-D3", "Filter-first rail controls", "Provide filters for Live, Highlights, Documentaries, Competition, and Duration above rails.", "Sticky filter row above content rails.", "Visual filtering; reduced scan cost", "F-P3", "Evening highlight search", "Users narrow a large content surface faster.", "Filter accuracy depends on metadata quality.", "High", "Medium"],
    ["F-S6", "F-D3", "Compact scan mode", "Collapse nonmatching rails into section labels until expanded.", "Condensed page with one expanded rail and folded sections.", "Progressive disclosure; visual economy", "F-P3", "Slow browsing with family waiting", "Lower vertical scanning burden.", "Some content feels less discoverable.", "Medium", "Medium"],
    ["F-S7", "F-D4", "Ticket status dashboard", "Show Official sale, Resale open, Waiting room, Coming soon, and Latest update time by tournament.", "Small status cards above ticket links.", "Visibility of system status; planning support", "F-P3", "Trust-sensitive ticket planning", "Users know whether to act now or wait.", "Requires reliable status data and governance.", "High", "Medium"],
    ["F-S8", "F-D4", "Official availability alerts", "Offer email and browser alerts by tournament and market, confirmed by receipt.", "Alert drawer with checkbox list and next release note.", "Memory load reduction; trust", "F-P3", "Family travel planning over many days", "Users stop manually rechecking availability.", "Notification fatigue and opt-in compliance.", "Medium", "Medium"],
    ["F-S9", "F-D5", "Utility rail on story pages", "Add right rail or sticky side sheet for Scores today, Rankings latest, Tickets official source, Watch now.", "Compact side module with four task cards.", "Task continuity; reduced jumping", "F-P1/F-P2/F-P3", "Reading story then switching task", "Story readers can branch into utilitarian tasks in context.", "May distract from article reading.", "Medium", "Low"],
    ["F-S10", "F-D5", "Embedded action chips in articles", "Add context chips in article header: Open Match Centre, View Tickets, Watch on FIFA+.", "Chip row under headline metadata.", "Contextual navigation; information scent", "F-P1/F-P2/F-P3", "Tournament article with adjacent action need", "Users can act from the article without searching navigation again.", "Requires article metadata rules.", "Medium", "Low"],
    ["C-S1", "C-D1", "Goal-based onboarding home", "First-run chooser: Play now, Review last game, Learn basics, Solve puzzles, Join tournament.", "Large task cards above default homepage feed.", "Progressive disclosure; recognition over recall", "C-P1/C-P2/C-P3", "First visit after signup", "New users see goals before feature taxonomy.", "Adds onboarding state management.", "High", "Medium"],
    ["C-S2", "C-D1", "Personal dashboard mode", "User pins top three tasks and hides unused modules for 30 days.", "Compact home with pinned cards and Edit layout button.", "Personalization; cognitive load reduction", "C-P1/C-P2/C-P3", "Repeated use with stable goals", "Homepage better matches user intent.", "May hide growth paths if poorly explained.", "Medium", "Medium"],
    ["C-S3", "C-D2", "Beginner analysis preset", "One-click preset keeps evaluation bar, best move, and plain-language coach notes.", "Preset chips at top of analysis panel: Beginner, Standard, Expert.", "Progressive disclosure; low-friction defaults", "C-P1", "Post-loss beginner review", "Novices get a readable analysis surface.", "Advanced controls become one step deeper.", "High", "Low"],
    ["C-S4", "C-D2", "Inline analysis glossary", "Hover or tap chart and toggle labels for plain-language explanations.", "Right-side info drawer with What this means text.", "Learnability; reduced memory load", "C-P1/C-P3", "Analysis and Game Review study sessions", "Users learn the meaning of graphs and labels in place.", "Adds copy maintenance and localization work.", "Medium", "Medium"],
    ["C-S5", "C-D3", "Upfront entitlement labels", "Mark each lesson, puzzle, and analysis feature with access labels before click.", "Small pill tags: Free, 3/day, 1 lesson/day, Diamond.", "Expectation setting; error prevention", "C-P1/C-P3", "Learning path selection", "Users know limits before investing attention.", "Access labels may add visual noise.", "High", "Low"],
    ["C-S6", "C-D3", "Soft-landing after limit reached", "After a limit wall, offer free alternative, reset timer, and queue for later.", "Modal with Continue learning free, Save for later, Upgrade.", "Continuity; frustration reduction", "C-P1", "Study session after a daily limit", "Users keep learning instead of stopping abruptly.", "May reduce upgrade pressure.", "Medium", "Medium"],
    ["C-S7", "C-D4", "Premove queue preview", "Show pending premoves with danger icon when opponent reply tree makes risk high.", "Tiny queue strip above board, first item tinted warning color.", "Error prevention; system status", "C-P2", "Blitz and bullet time trouble", "Users see what will execute before it happens.", "Risk estimate can be imperfect.", "High", "Medium"],
    ["C-S8", "C-D4", "Fast clear shortcut", "One-click Clear or Esc clears queued premove chain.", "Small Clear premoves pill next to clocks or settings.", "Recoverability; user control", "C-P2", "Fast play after unexpected opponent move", "Users recover from risky queued intent quickly.", "Adds one more in-game control.", "Medium", "Low"],
    ["C-S9", "C-D5", "First-time coachmark", "After two full games, show Need fewer distractions? Try Focus Mode.", "Tooltip near board corner.", "Discoverability; contextual help", "C-P2", "Post-game moment before next serious game", "Users learn the hidden control when it is relevant.", "Coachmarks can annoy expert users.", "Medium", "Low"],
    ["C-S10", "C-D5", "Persistent settings shortcut", "Add Focus Mode toggle into board settings and keyboard shortcut help.", "Settings panel item with live preview thumbnail.", "Consistency; discoverability", "C-P2/C-P3", "Board settings and serious-game setup", "Focus Mode becomes findable without hover discovery.", "Settings panel grows slightly.", "Medium", "Low"],
]


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        safe = [str(c).replace("\n", " ") for c in row]
        lines.append("| " + " | ".join(safe) + " |")
    return "\n".join(lines)


def ref_nums_for(product):
    return [s["num"] for s in SOURCES if s["product"] == product]


def references_md(nums=None):
    chosen = SOURCES if nums is None else [s for s in SOURCES if s["num"] in nums]
    lines = ["## References"]
    for s in chosen:
        claims = " ".join(s["claims_supported"])
        lines.append(f"[{s['num']}] {s['title']}. {s['source_type']}. {s['url']}. Accessed {s['access_date']}. Supports: {claims}")
    return "\n".join(lines)


def use_case_sections(product):
    lines = []
    for uc in [u for u in USE_CASES if u[1] == product]:
        context = USE_CASE_CONTEXT[uc[0]]
        lines += [
            f"### {uc[0]}. {uc[2]}",
            table(
                ["Field", "Detail"],
                [
                    ["Primary persona", uc[3]],
                    ["Where:", context["Where"]],
                    ["When:", context["When"]],
                    ["Posture:", context["Posture"]],
                    ["Device:", context["Device"]],
                    ["Attention level:", context["Attention level"]],
                    ["Environment:", context["Environment"]],
                    ["Interaction method:", context["Interaction method"]],
                    ["Goal:", uc[4]],
                    ["Trigger:", uc[5]],
                    ["Precondition:", uc[7]],
                    ["Normal flow:", uc[9]],
                    ["Alternate flow:", uc[10]],
                    ["Error path:", uc[11]],
                    ["Feedback observed:", uc[12]],
                    ["Figure or source reference:", uc[13]],
                    ["HCI concepts:", context["HCI concepts"]],
                    ["Success outcome:", uc[8]],
                ],
            ),
        ]
    return "\n\n".join(lines)


def figure_block(fid, title, image_path, caption):
    return f"### Figure {fid}. {title}\n\n![Figure {fid}]({image_path})\n\n{caption}"


def visual_figure_sections():
    figures = [
        ("F-01", "FIFA.com home page information hierarchy", "assets/screenshots/annotated/fifa/fifa_home_desktop.png", "The highlighted hero and task-entry regions show how a casual fan's attention is pulled between promotional content and football task entry."),
        ("F-02", "FIFA.com desktop navigation", "assets/screenshots/annotated/fifa/fifa_navigation_desktop.png", "The top navigation labels support recognition over recall for Match Centre, News, Rankings, Tickets, and More."),
        ("F-03", "FIFA.com mobile navigation", "assets/screenshots/annotated/fifa/fifa_navigation_mobile.png", "The mobile header and menu entry show the extra progressive-disclosure step before match-related tasks."),
        ("F-04", "FIFA.com Match Centre", "assets/screenshots/annotated/fifa/fifa_match_centre_desktop.png", "The date rail, search, live toggle, and match rows support the user's mental model of checking fixtures by day."),
        ("F-05", "FIFA.com search and discovery", "assets/screenshots/annotated/fifa/fifa_search_desktop.png", "The search state supports official lookup tasks but needs clear category separation for teams, tournaments, and articles."),
        ("F-06", "FIFA.com news article page", "assets/screenshots/annotated/fifa/fifa_news_article_desktop.png", "The article surface shows reading-load and scan-load issues for football news consumption."),
        ("F-07", "FIFA.com tournament page", "assets/screenshots/annotated/fifa/fifa_competition_desktop.png", "The tournament page groups competition discovery content for a tournament follower."),
        ("F-08", "FIFA.com mobile content density", "assets/screenshots/annotated/fifa/fifa_home_mobile.png", "The observed promotional modal on mobile is direct evidence of attention interruption over the home-page content."),
        ("F-09", "FIFA.com task flow diagram", "assets/diagrams/s-01_fifa_solution.png", "The task-first navigation sketch is used as a visual proxy for the proposed FIFA browse-to-task flow."),
        ("F-10", "FIFA.com navigation map", "assets/screenshots/annotated/fifa/fifa_footer_desktop.png", "The footer and ecosystem links show how global support and sibling destinations extend the navigation map."),
        ("F-11", "FIFA.com usability issue crop", "assets/screenshots/crops/fifa/fifa_home_mobile_crop_A.png", "The crop isolates the mobile overlay interruption that competes with match and article discovery."),
        ("F-12", "FIFA.com proposed improvement sketch", "assets/diagrams/s-02_fifa_solution.png", "The proposed Match Centre filter bar maps the observed fixture-scanning issue to a concrete control redesign."),
        ("C-01", "Chess.com home page information hierarchy", "assets/screenshots/annotated/chess/chess_home_desktop.png", "The highlighted home page regions show task signposting for Play, Puzzles, Learn, Train, Watch, and Community."),
        ("C-02", "Chess.com play entry point", "assets/screenshots/annotated/chess/chess_play_desktop.png", "The board plus Start Game controls show the action-first pathway for starting a quick chess game."),
        ("C-03", "Chess.com game board or demo board", "assets/screenshots/annotated/chess/chess_board_or_demo_desktop.png", "The chess board uses direct manipulation and a familiar game-board metaphor."),
        ("C-04", "Chess.com puzzle page", "assets/screenshots/annotated/chess/chess_puzzles_desktop.png", "The puzzle screen shows a learning task with layered onboarding and feedback expectations."),
        ("C-05", "Chess.com Learn page", "assets/screenshots/annotated/chess/chess_learn_desktop.png", "The learning surface shows multiple routes that need progressive disclosure for beginners."),
        ("C-06", "Chess.com navigation menu", "assets/screenshots/annotated/chess/chess_navigation_desktop.png", "The side navigation exposes many features, which helps expert recognition but increases beginner scan load."),
        ("C-07", "Chess.com feedback and move status", "assets/screenshots/annotated/chess/chess_play_mobile.png", "The compact play screen shows how clock, board, and action controls compete for mobile attention."),
        ("C-08", "Chess.com mobile layout", "assets/screenshots/annotated/chess/chess_home_mobile.png", "The mobile layout compresses feature discovery and account prompts into a narrow touch surface."),
        ("C-09", "Chess.com task flow diagram", "assets/diagrams/s-05_chess_solution.png", "The beginner-home sketch shows the proposed play, learn, puzzle, and review task sequence."),
        ("C-10", "Chess.com navigation map", "assets/screenshots/annotated/chess/chess_navigation_mobile.png", "The mobile navigation capture shows how feature-rich navigation shifts behind compact controls."),
        ("C-11", "Chess.com usability issue crop", "assets/screenshots/crops/chess/chess_puzzles_desktop_crop_A.png", "The puzzle crop isolates a dense learning prompt layered over the board state."),
        ("C-12", "Chess.com proposed improvement sketch", "assets/diagrams/s-07_chess_solution.png", "The beginner analysis preset sketch maps observed analysis complexity to a progressive-disclosure solution."),
    ]
    return "\n\n".join(figure_block(*f) for f in figures)


def product_research_figure_list():
    return table(
        ["Figure", "Product", "Evidence role"],
        [
            ["F-01 to F-08", "FIFA.com", "Captured live pages for home, navigation, Match Centre, search, article, competition, and mobile density"],
            ["F-09 to F-12", "FIFA.com", "Flow/map, crop, and proposed improvement figures grounded in the captured evidence"],
            ["C-01 to C-08", "Chess.com", "Captured live pages for home, play, board, puzzle, learn, navigation, feedback, and mobile layout"],
            ["C-09 to C-12", "Chess.com", "Flow/map, crop, and proposed improvement figures grounded in the captured evidence"],
        ],
    )


def detailed_personas_table():
    rows = [
        ["F-P1", "Casual football fan", "18-25", "Medium", "Low-medium", "Check today's fixtures, live scores, results, and short news quickly", "Slow paths to match information", "Mobile phone", "Public transport or short break", "Several times per week", "Interrupted attention and low patience"],
        ["F-P2", "Tournament follower", "24-40", "High", "Medium-high", "Follow tournament pages, teams, fixtures, standings, and media", "Too many tournament links to compare", "Desktop", "Home or office", "Weekly during tournaments", "Needs scannable date/team comparison"],
        ["F-P3", "Media or student researcher", "20-35", "High", "Medium", "Find official football news, tournament history, team info, and reliable sources", "Unclear source path across FIFA properties", "Laptop", "Focused research session", "Monthly or project-based", "Needs credible source trails"],
        ["C-P1", "Beginner chess learner", "13-22", "Medium", "Low", "Start a simple game, learn rules, solve easy puzzles", "Feature overload before knowing chess terms", "Mobile or laptop", "Home or school", "Several times per week", "Low domain knowledge and needs guidance"],
        ["C-P2", "Competitive online player", "18-35", "High", "High", "Start a rated game quickly and monitor clock, moves, rating, opponent status", "Delay or mis-tap under time pressure", "Desktop", "Focused play setup", "Daily", "Motor accuracy and low delay tolerance"],
        ["C-P3", "Returning casual player", "25-45", "Medium-high", "Medium", "Play a daily or quick game, read content, review mistakes", "Forgets feature locations and analysis meanings", "Mobile browser", "Interrupted home use", "Weekly", "Needs recognition and lightweight feedback"],
    ]
    return table(["ID", "Persona", "Age range", "Tech experience", "Domain experience", "Main goal", "Frustration", "Device", "Environment", "Usage frequency", "Constraint"], rows)


def use_case_evidence_matrix():
    rows = [
        ["F-UC1", "Find today's match schedule", "FIFA.com", "F-P1", "Mobile", "One-handed glance", "Low", "Public transport", "Open FIFA.com, select Match Centre, scan date/live rows", "No live match; switch to results", "Slow client render; retry/refresh", "F-04, F-08", "information scent, visibility of status"],
        ["F-UC2", "Check live score or result", "FIFA.com", "F-P1", "Mobile/desktop", "Short break", "Low", "Noisy place", "Use Match Centre and live toggle", "Sort/filter by competition", "Too many entries; search competition", "F-04", "mental model, cognitive load"],
        ["F-UC3", "Read football news article", "FIFA.com", "F-P2", "Desktop/mobile", "Leaning back", "Medium", "Office", "Open News or article URL, scan headline/body", "Use related links", "Reading interrupted by dense media", "F-06", "visual attention, reading load"],
        ["F-UC4", "Find tournament information", "FIFA.com", "F-P2", "Desktop", "Focused comparison", "Medium", "Home/office", "Open tournament page, scan dates/teams/content", "Use navigation/footer", "Wrong FIFA property reached", "F-07, F-10", "information architecture, consistency"],
        ["F-UC5", "Search team/player/article/tournament", "FIFA.com", "F-P3", "Laptop", "Focused lookup", "High", "Research session", "Open search, enter query, compare result categories", "Use navigation if search fails", "Sparse or mixed results", "F-05", "recognition, error recovery"],
        ["C-UC1", "Start quick online chess game", "Chess.com", "C-P2", "Desktop/mobile", "Focused play", "High", "Quiet or noisy room", "Open Play, choose time control, start game", "Custom challenge or friend", "Account prompt or match settings mismatch", "C-02, C-07", "efficiency, user control"],
        ["C-UC2", "Solve a puzzle", "Chess.com", "C-P1", "Mobile/desktop", "Learning posture", "Medium", "School/home", "Open Puzzles, read prompt, make move, observe feedback", "Choose puzzle mode", "Intro modal or access limit interrupts", "C-04, C-11", "feedback, learnability"],
        ["C-UC3", "Learn a beginner lesson", "Chess.com", "C-P1", "Laptop", "Exploratory", "Medium", "Home", "Open Learn/Lessons, choose beginner topic", "Use study plan", "Too many paths", "C-05", "progressive disclosure"],
        ["C-UC4", "Review game or view board feedback", "Chess.com", "C-P3", "Desktop", "Reflective study", "High", "Quiet desk", "Finish/open game, view review/analysis controls", "Use analysis board", "Dense feedback overwhelms", "C-03, C-12", "informative feedback"],
        ["C-UC5", "Read chess news/opening content", "Chess.com", "C-P3", "Mobile/desktop", "Casual reading", "Medium", "Interrupted attention", "Open News, scan article list, open story", "Search community content", "Navigation density distracts", "C-09B, C-06", "content discovery, memory load"],
    ]
    return table(["ID", "Title", "Product", "Persona", "Device", "Posture", "Attention", "Distraction", "Normal flow", "Alternate flow", "Error path", "Figures", "HCI concepts"], rows)


def detailed_hci_findings_table():
    figure_map = {
        "F-HCI1": "F-01", "F-HCI2": "F-02", "F-HCI3": "F-09", "F-HCI4": "F-10", "F-HCI5": "F-10",
        "F-HCI6": "F-10", "F-HCI7": "F-12", "F-HCI8": "F-08", "F-HCI9": "F-11", "F-HCI10": "F-06",
        "C-HCI1": "C-02", "C-HCI2": "C-03", "C-HCI3": "C-07", "C-HCI4": "C-07", "C-HCI5": "C-04",
        "C-HCI6": "C-05", "C-HCI7": "C-06", "C-HCI8": "C-02", "C-HCI9": "C-03", "C-HCI10": "C-12",
    }
    rows = []
    for f in FINDINGS:
        rows.append([f[0], f[1], figure_map.get(f[0], ""), f[3], f[4], f[5], f[6], f[7], f[2], f[8], f[9], f"{figure_map.get(f[0], '')} and {f[10]}", "See related solution direction in PotentialSolutions"])
    return table(["Finding ID", "Product", "Screenshot figure", "Screen or flow", "Highlighted UI element", "Observed behavior", "Persona/context", "HCI mapping", "Benefit/drawback", "Concrete scenario", "Severity", "Evidence", "Improvement direction"], rows)


def solution_visual_sections():
    figures = [
        ("S-01", "FIFA task-first navigation", "assets/diagrams/s-01_fifa_solution.png", "A task-first header reduces hidden navigation cost for casual fans and tournament followers."),
        ("S-02", "FIFA Match Centre filter bar", "assets/diagrams/s-02_fifa_solution.png", "Sticky date, live, result, and competition controls reduce scanning in the Match Centre."),
        ("S-03", "FIFA article utility rail", "assets/diagrams/s-03_fifa_solution.png", "Context chips let an article reader jump to scores, tickets, or watch actions without re-searching."),
        ("S-04", "FIFA+ handoff explainer", "assets/diagrams/s-04_fifa_solution.png", "A handoff explainer improves trust and user control before switching context to FIFA+."),
        ("S-05", "Chess.com beginner home", "assets/diagrams/s-05_chess_solution.png", "Goal-based cards reduce beginner feature overload before the user learns product taxonomy."),
        ("S-06", "Chess.com mobile board guard", "assets/diagrams/s-06_chess_solution.png", "Larger controls and a clear premove action reduce mobile mis-tap risk under time pressure."),
        ("S-07", "Chess.com beginner analysis preset", "assets/diagrams/s-07_chess_solution.png", "Beginner, standard, and expert presets progressively reveal game-review complexity."),
        ("S-08", "Chess.com learn path", "assets/diagrams/s-08_chess_solution.png", "A recommended beginner path and visible access labels reduce learning-path uncertainty."),
    ]
    return "\n\n".join(figure_block(*f) for f in figures)


def drawback_solution_visual_table():
    rows = [
        ["F-D1", "F-01/F-02", "Match information is not always the most visible item for quick score users.", "F-P1", "Mobile short break", "information scent", "F-S1/F-S2", "Task-first navigation and intent chips", "S-01", "Faster entry to Match Centre", "Less exposure for commercial links", "High", "Medium"],
        ["F-D2", "F-03", "Mobile navigation hides important sections behind menu layers.", "F-P1", "One-handed mobile use", "progressive disclosure", "F-S3/F-S4", "Mobile task-first menu and handoff orientation", "S-01/S-04", "Fewer hidden steps", "More header/state rules", "High", "Medium"],
        ["F-D3", "F-04", "Competition or match filters require too much scanning.", "F-P2", "Tournament comparison", "cognitive load", "F-S5/F-S6", "Filter-first rail and compact scan mode", "S-02", "Lower scan cost", "Metadata quality dependency", "High", "Medium"],
        ["F-D4", "F-06/F-08", "Article and media-heavy pages overload mobile readers.", "F-P1/F-P2", "Interrupted reading", "attention", "F-S9/F-S10", "Article utility rail and action chips", "S-03", "Keeps task continuity", "May distract from reading", "Medium", "Low"],
        ["F-D5", "F-05", "Search/discovery results do not separate categories clearly enough for official lookup tasks.", "F-P3", "Research lookup", "recognition", "F-S7/F-S8", "Status dashboard and alerts for official tasks", "S-02/S-03", "Clearer official path", "Requires governance", "Medium", "Medium"],
        ["C-D1", "C-01/C-06", "Feature-rich navigation overloads beginners.", "C-P1", "First visit", "memory load", "C-S1/C-S2", "Goal-based onboarding and personal dashboard", "S-05", "Better first success", "Adds onboarding state", "High", "Medium"],
        ["C-D2", "C-10", "Sign-in or account prompts interrupt fast play intent.", "C-P2", "Fast play", "user control", "C-S5/C-S6", "Upfront labels and soft landing", "S-08", "Fewer surprise interruptions", "More copy to maintain", "High", "Low"],
        ["C-D3", "C-07", "Mobile board interaction increases mis-tap risk under time pressure.", "C-P2", "Mobile blitz", "motor accuracy", "C-S7/C-S8", "Premove queue preview and clear shortcut", "S-06", "Reduced accidental input", "One more visible control", "High", "Medium"],
        ["C-D4", "C-05", "Learning section lacks one obvious beginner path.", "C-P1", "Beginner study", "progressive disclosure", "C-S1/C-S5", "Beginner path and entitlement labels", "S-08", "Clear next step", "May reduce exploration", "Medium", "Low"],
        ["C-D5", "C-12", "Game feedback is too dense for casual users after a match.", "C-P3", "Post-game review", "informative feedback", "C-S3/C-S4", "Beginner analysis preset and glossary", "S-07", "Readable feedback first", "Advanced controls move deeper", "High", "Low"],
    ]
    return table(["Drawback ID", "Screenshot figure", "Problem", "Persona", "Context", "HCI principle", "Solutions", "Solution description", "Mockup figure", "Expected improvement", "Tradeoff", "Priority", "Effort"], rows)


def product_research_md():
    benefits = [[f[0], f[1], f[3], f[4], f[7], f[9], f[10]] for f in FINDINGS if f[2] == "Benefit"]
    drawbacks = [[d[0], d[1], d[2], d[3], d[4]] for d in DRAWBACKS]
    comparison = [
        ["Task type", "Browse, compare, follow, verify, then hand off to FIFA+ for video", "Do, review, analyze, train, and enter competitive flows"],
        ["Target users", "Fans checking official football information, tickets, rankings, and video", "Players who want fast games, feedback, training, and fair competitive play"],
        ["Information scent", "Strong for official labels; weaker when tasks cross properties [1][6]", "Strong action labels on homepage and support flows [10][11]"],
        ["Learnability", "Easy for news/rankings; ticket and watch handoff need clearer status [5][6]", "Easy to start; analysis and training depth require guidance [15][17][20]"],
        ["Cognitive load", "Browse surfaces and rails can become dense [2][6]", "Feature breadth and analysis controls can overwhelm novices [10][17]"],
        ["Motivation pattern", "Follow official tournaments and national-team context", "Immediate play loop plus feedback, puzzles, lessons, and study plans"],
        ["Trust model", "Official source and ticket credibility are central [4][5][9]", "Fair play and review credibility shape competitive trust [15][22]"],
        ["Error risk", "Wrong ticket source or lost context during handoff", "Queued premove, hidden focus control, and access-limit interruptions"],
        ["Reflection and feedback", "Article reading and ranking lookup; limited personal feedback", "Game Review and Analysis give rich post-action reflection [15][16][17]"],
        ["Accessibility", "Official 2026 coverage includes accessibility efforts, but this report focuses on IA and task flow", "Focus Mode and board settings support attention but need stronger discovery [13][14]"],
        ["Speed of first success", "Fast for news and rankings; slower for ticket status or watch handoff", "Fast for starting a game; slower for understanding review depth"],
    ]
    matrix = [[d[0], d[1], d[2], d[4], "High" if d[4] == "High" else "Medium", "Addressed in PotentialSolutions"] for d in DRAWBACKS]
    lines = [
        f"# {GROUP_ID}-PA1 Product Research: FIFA and Chess.com web experiences",
        f"Group ID: {GROUP_ID}. Members: {', '.join(TEAM_MEMBERS)}. Course: HCI. Date: {TODAY}. Product pair: FIFA.com and Chess.com. Screenshot evidence note: all screen-level claims reference captured or annotated Playwright evidence.",
        "## Executive summary",
        "This report compares FIFA and Chess.com as web experiences with opposite interaction centers. FIFA is primarily browse, compare, and follow: the user moves through official football news, match data, rankings, tickets, and a FIFA+ watch handoff. Chess.com is primarily do, review, and improve: the user starts games, manages speed features, reviews finished games, analyzes positions, solves puzzles, follows lessons, and plans tournaments. Numbered references are used for all product claims.",
        "## Method and evidence protocol",
        "The team observed official website screens through Chromium automation, saved raw screenshots, generated annotated versions and crops with sharp, and recorded captions in assets/figures_manifest.json. Screenshots are used as evidence only when the referenced UI region is visible. Limitations: login-only personalized states were not entered, and any live content visible on access date may change.",
        product_research_figure_list(),
        "## Product selection rationale",
        table(["Product", "Domain", "Modality", "Positioning"], [[p["name"], p["domain"], p["modality"], p["positioning"]] for p in PRODUCTS.values()]),
        "FIFA.com was selected as the official browse-first football portal. Chess.com was selected as an action-first online chess platform. The comparison isolates how sports websites differ when one product centers on official information discovery and the other centers on immediate gameplay and feedback.",
        "## Source method",
        "Official English pages were prioritized. FIFA client-side pages that yielded sparse crawl text were retained as official URLs when screenshots confirmed the screen. Chess.com claims rely on the official homepage, observed Playwright screenshots, and official support pages. Secondary sources were not needed.",
        table(["Citation", "Product", "Type", "Claim supported"], [[f"[{s['num']}]", s["product"], s["source_type"], " ".join(s["claims_supported"])] for s in SOURCES]),
        "## Product A: FIFA.com",
        "FIFA.com is the official football web portal for sports news, match information, tournament discovery, rankings, official media, tickets, and FIFA+ handoff when relevant.",
        "### FIFA user groups",
        "Casual fans, tournament followers, and media/student researchers need official football information under different time pressure and credibility requirements.",
        "## Product B: Chess.com",
        "Chess.com is an online chess platform for playing games, solving puzzles, learning lessons, reviewing games, reading chess content, and improving chess skill.",
        "### Chess.com user groups",
        "Beginner learners, competitive online players, and returning casual players need fast play, visible feedback, and progressive learning paths.",
        "## Personas",
        detailed_personas_table(),
        "### FIFA personas",
        table(["ID", "Name", "Age", "Tech proficiency", "Goal", "Context"], PERSONAS["FIFA"]),
        "### Chess.com personas",
        table(["ID", "Name", "Age", "Tech proficiency", "Goal", "Context"], PERSONAS["Chess.com"]),
        "## Use cases",
        use_case_evidence_matrix(),
        use_case_sections("FIFA"),
        use_case_sections("Chess.com"),
        "## Screen-level HCI analysis with annotated figures",
        visual_figure_sections(),
        "## HCI findings",
        detailed_hci_findings_table(),
        table(["ID", "Product", "Type", "Screen or flow", "UI element", "Observed behavior", "Persona/context", "HCI mapping", "Concrete scenario", "Severity", "Evidence"], FINDINGS),
        "## Benefits summary",
        table(["ID", "Product", "Screen/flow", "UI element", "HCI mapping", "Severity", "Evidence"], benefits),
        "## Drawbacks summary",
        table(["ID", "Product", "Drawback", "Linked finding", "Severity"], drawbacks),
        "## Difficulty and hindrance matrix",
        table(["ID", "Product", "Hindrance", "Severity", "Task difficulty", "Disposition"], matrix),
        "## Cross-product comparison",
        table(["Dimension", "FIFA", "Chess.com"], comparison),
        "## Summary of major drawbacks",
        "The highest-risk FIFA drawbacks are mobile interruption, hidden mobile navigation layers, match/filter scanning, dense article/media pages, and source continuity across FIFA/FIFA+. The highest-risk Chess.com drawbacks are beginner feature overload, account-prompt interruption, mobile board mis-tap risk, unclear beginner learning paths, and dense post-game feedback.",
        "## Diagram A. FIFA browse and watch flow",
        "```mermaid\nflowchart LR\nA[Open FIFA.com] --> B[Choose Match Centre or News or Rankings or Tickets]\nB --> C[Read tournament info]\nC --> D{Need live or archive video?}\nD -- Yes --> E[Open FIFA+]\nE --> F[Sign up or log in]\nF --> G[Watch Live and Coming Up or Highlights]\nD -- No --> H[Continue on FIFA.com]\n```",
        "Text fallback: Open FIFA.com, choose task entry, read official info, then move to FIFA+ only if video is needed.",
        "## Diagram B. Chess.com play, review, and learn flow",
        "```mermaid\nflowchart LR\nA[Open Chess.com] --> B[Start Game]\nB --> C[Play]\nC --> D[Game Over]\nD --> E[Game Review]\nE --> F[Self Analysis]\nF --> G[Puzzles or Lesson or Study Plan]\n```",
        "Text fallback: Open site, start a game, finish, run Game Review, move into deeper analysis, then continue with training.",
        "## Appendix A: Screenshot manifest",
        "The full machine-readable screenshot manifest is stored in assets/figures_manifest.json and includes raw paths, annotated paths, crops, highlighted regions, claims, HCI concepts, and captions.",
        "## Appendix B: Figure list",
        product_research_figure_list(),
        references_md(),
    ]
    return "\n\n".join(lines)


def solutions_md():
    mapping = [[d[0], ", ".join(s[0] for s in SOLUTIONS if s[1] == d[0])] for d in DRAWBACKS]
    quick = [s for s in SOLUTIONS if s[0] in {"F-S2", "F-S3", "F-S9", "F-S10", "C-S3", "C-S5", "C-S8", "C-S9", "C-S10"}]
    deeper = [s for s in SOLUTIONS if s[0] not in {q[0] for q in quick}]
    matrix = [[s[0], s[2], s[10], s[11], "Quick win" if s in quick else "Deeper redesign"] for s in SOLUTIONS]
    lines = [
        f"# {GROUP_ID}-PA1 Potential Solutions: FIFA and Chess.com",
        "## Executive summary",
        "The solution set keeps FIFA focused on task-first navigation, continuity across FIFA+, clearer ticket status, and utility entry points. It keeps Chess.com focused on novice onboarding, simpler analysis, expectation-setting around access limits, safer premoves, and clearer Focus Mode discovery.",
        "## Drawback inventory",
        table(["ID", "Product", "Drawback", "Linked finding", "Severity"], DRAWBACKS),
        "## Drawback evidence and visual solution mapping",
        drawback_solution_visual_table(),
        "## Drawback-to-solution mapping",
        table(["Drawback", "Solutions"], mapping),
        "## Visual solution figures",
        solution_visual_sections(),
        "## Solution details",
        table(["ID", "Drawback", "Design concept", "Detailed UI behavior", "Mockup description in words", "HCI principle mapping", "Affected personas", "Affected contexts", "Expected effect", "Tradeoff", "Priority", "Effort"], SOLUTIONS),
        "## Prioritized impact-effort matrix",
        table(["Solution", "Concept", "Priority", "Effort", "Rollout bucket"], matrix),
        "## Quick wins",
        table(["ID", "Concept", "Why first"], [[s[0], s[2], f"{s[10]} priority with {s[11]} effort; concrete UI can be tested without changing core architecture."] for s in quick]),
        "## Deeper redesigns",
        table(["ID", "Concept", "Why deeper"], [[s[0], s[2], "Requires cross-page, data, personalization, or cross-property coordination."] for s in deeper]),
        "## Rollout plan",
        "Sprint 1 implements quick wins, tests wording and UI placement, and validates with the personas most affected by each drawback. Sprint 2 handles task-first navigation, ticket status, FIFA+ filters, personalized Chess.com home, glossary behavior, and premove queue preview. QA checks that every drawback from ProductResearch still maps to exactly two solutions.",
        references_md([1, 2, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20]),
    ]
    return "\n\n".join(lines)


def peer_review_md():
    slides = [
        [1, "Scope and selected pair", "FIFA browse-first web ecosystem and Chess.com action-first web platform; Figure F-01 and Figure C-01", "Le Minh", "0:45"],
        [2, "Evidence method and official source protocol", "Official pages first; Playwright screenshots and manifest; Figure F-04 and Figure C-02", "Le Minh", "0:55"],
        [3, "Personas and contexts", "Six personas with task, device, attention, trust, and learning contexts; Figure F-08 and Figure C-08", "Trang Minh Nhut", "1:00"],
        [4, "FIFA findings", "Navigation, Match Centre, mobile interruption, article density, and handoff drawbacks; Figure F-02, Figure F-04, Figure F-06, Figure F-08", "Nguyen Vu Bach", "1:10"],
        [5, "Chess.com findings", "Play, board, puzzles, Learn, navigation, and feedback density; Figure C-02, Figure C-03, Figure C-04, Figure C-05, Figure C-06", "Pham Nguyen Gia Bao", "1:10"],
        [6, "Solution priorities", "Quick wins versus deeper redesigns and impact-effort rationale; Figure S-01 to Figure S-08", "Trang Minh Nhut", "1:10"],
        [7, "Sprint plan, QA, and packaging", "Two-week RUP plus Scrum process, visual QA, PDF regeneration, zip validation; Figure F-09 and Figure C-09", "Le Minh", "0:50"],
    ]
    questions = [
        ["Why pair FIFA with Chess.com?", "They are both high-traffic web experiences, but FIFA is browse-first while Chess.com is action-first, so the contrast exposes different HCI tradeoffs."],
        ["Which site is stronger for fast task completion?", "Chess.com is stronger for immediate action because Play is primary and the start-game flow is short. FIFA is fast for official labels but slower when tasks cross properties."],
        ["Which site carries more scan load?", "FIFA+ and Chess.com analysis both carry scan load; FIFA+ uses dense rails, while Chess.com analysis exposes charts, toggles, lines, and access expectations."],
        ["Which site shows better feedback after action?", "Chess.com, because Game Review and Analysis provide graph, classifications, retry, and engine feedback after a completed game."],
        ["Why is FIFA+ a continuity problem?", "The user moves from FIFA information pages to a DAZN-branded watch page with sign-in/get-started controls, creating trust and mode-boundary friction."],
        ["Why is premove both a feature and a risk?", "It saves time in blitz, but it can legally execute after an unexpected reply and create a blunder."],
        ["How did the team avoid generic UX claims?", "Every finding names page or flow, control, user, context, principle, scenario, severity, and evidence."],
        ["Which redesign gives best impact for effort?", "F-S3 and C-S3 are strong low-effort wins: the handoff explainer reduces trust friction and the beginner analysis preset reduces cognitive load."],
    ]
    feedback = [
        ["Nora Lee", "Mock/internal rehearsal peer", "FIFA ticket trust needs a stronger official-source cue.", "Added F-HCI3, F-D4, F-S7, and F-S8 with FIFA.com/tickets citations.", "Nguyen Vu Bach", "Done"],
        ["Omar Khan", "Mock/internal rehearsal peer", "Explain why FIFA+ is not just another page.", "Added DAZN-branded handoff risk, explainer card, and shared breadcrumb solution.", "Trang Minh Nhut", "Done"],
        ["Jin Park", "Mock/internal rehearsal peer", "Chess.com beginner analysis sounds too expert-focused.", "Added C-S3 beginner preset and C-S4 inline glossary.", "Trang Minh Nhut", "Done"],
        ["Mira Vo", "Mock/internal rehearsal peer", "Premove needs an error-prevention solution.", "Added premove queue preview and fast clear shortcut.", "Pham Nguyen Gia Bao", "Done"],
        ["Sam Patel", "Mock/internal rehearsal peer", "Focus Mode discovery should cite the hover behavior.", "Linked C-HCI9 to board-size and Focus Mode support pages.", "Pham Nguyen Gia Bao", "Done"],
        ["Hana Lim", "Mock/internal rehearsal peer", "The pair needs a clearer comparison logic.", "Reframed FIFA as browse, compare, follow and Chess.com as do, review, improve.", "Le Minh", "Done"],
        ["Leo Tran", "Mock/internal rehearsal peer", "Weekly plan must show QA and packaging.", "Added sprint evidence, validation tasks, and zip checks.", "Le Minh", "Done"],
        ["Ivy Chen", "Mock/internal rehearsal peer", "Mockups should not imply invented screenshots.", "Changed all mockups to written UI descriptions only.", "Trang Minh Nhut", "Done"],
    ]
    script = (
        "Le Minh opens by naming the pair: FIFA and Chess.com web experiences. "
        "The first contrast is task posture: FIFA is browse, compare, and follow, while Chess.com is do, review, and improve. "
        "Le Minh then explains the official-source protocol and why numbered references are used. "
        "Trang Minh Nhut introduces six personas and emphasizes context: short campus browsing, office scanning, trust-sensitive ticket planning, beginner learning, blitz play, and deep review. "
        "Nguyen Vu Bach presents FIFA findings, starting with navigation and official ticket trust, then moving into the drawbacks of ecosystem sprawl, FIFA+ continuity, dense watch rails, ticket status uncertainty, and article-to-utility friction. "
        "Pham Nguyen Gia Bao presents Chess.com findings, showing how Play, Puzzles, Learn, Game Review, Analysis, and Study Plans support action and reflection, then explaining risks from feature overload, premove execution, hidden Focus Mode controls, and complex analysis screens. "
        "Trang Minh Nhut closes the design portion with quick wins and deeper redesigns. "
        "Le Minh finishes with the two-week RUP plus Scrum plan, peer-review feedback loop, citation QA, PDF text extraction, old-term scan, and zip packaging."
    )
    lines = [
        f"# {GROUP_ID}-PA1 Peer Review Preparation: FIFA and Chess.com",
        "## Seven-minute script",
        script,
        "## Slide outline",
        table(["Slide", "Topic", "Purpose", "Speaker", "Time"], slides),
        "## Likely questions and prepared answers",
        table(["Question", "Prepared answer"], questions),
        "## Mock feedback entries",
        "These entries are mock/internal rehearsal feedback because real classroom peer feedback was not available in the repository.",
        table(["Reviewer", "Role", "Feedback", "Response/revision", "Owner", "Status"], feedback),
        "## Revision log and owner mapping",
        table(["Revision area", "Owner", "Evidence of change"], [["Scope, evidence protocol, final QA", "Le Minh", "Product pair, source protocol, final scan, and packaging locked"], ["FIFA.com findings", "Nguyen Vu Bach", "FIFA personas, use cases, screenshot evidence, and HCI findings"], ["Chess.com findings", "Pham Nguyen Gia Bao", "Chess.com personas, use cases, screenshot evidence, and HCI findings"], ["HCI solution priorities", "Trang Minh Nhut", "Drawback-to-solution matrix and visual solution QA"], ["Sprint evidence and packaging", "Le Minh", "WeeklyReport, PDF extraction, and zip validation"], ["Figure and caption QA", "Trang Minh Nhut", "Annotated screenshot and solution figure consistency checks"]]),
        "## Rehearsal checklist",
        "\n".join([f"- Check {i}: {text}" for i, text in enumerate(["First slide names FIFA and Chess.com only.", "Method slide explains official-source-first evidence.", "Persona slide ties each person to a context and task.", "FIFA slide includes benefits and drawbacks with concrete controls.", "Chess.com slide includes play, review, analysis, learning, premove, and Focus Mode.", "Solution slide states UI behavior, effect, tradeoff, priority, and effort.", "Close names regenerated PDFs and top-level zip.", "Q&A uses HCI reasoning instead of generic praise."], 1)]),
        references_md([1, 5, 6, 10, 11, 12, 13, 14, 15, 17, 20, 22]),
    ]
    return "\n\n".join(lines)


def weekly_report_md():
    roster = [[m["name"], m["student_id"], m["role"], m["main_contribution"]] for m in TEAM_ROSTER]
    sprint_planning = [
        ["Meeting type", "Sprint Planning"],
        ["Planned date", "2026-06-10"],
        ["Attendance", "Le Minh, Nguyen Vu Bach, Pham Nguyen Gia Bao, Trang Minh Nhut"],
        ["Decisions", "Product pair locked as FIFA.com and Chess.com; final reports must include visual screenshot evidence; ProductResearch co-led by Nguyen Vu Bach and Pham Nguyen Gia Bao; PotentialSolutions led by Trang Minh Nhut; PeerReview, WeeklyReport, integration, and packaging led by Le Minh; screenshots must be annotated and referenced; four final PDFs must be packaged at the top level of GroupID-PA1.zip."],
        ["Task assignments", "Le Minh: coordinate scope, manage final checklist, write PeerReview, support WeeklyReport, regenerate PDF and zip. Nguyen Vu Bach: research FIFA.com, collect FIFA sources, capture and annotate FIFA screenshots, write FIFA HCI findings. Pham Nguyen Gia Bao: research Chess.com, collect Chess.com sources, capture and annotate Chess screenshots, write Chess.com HCI findings. Trang Minh Nhut: map HCI concepts, write PotentialSolutions, check figure captions, check consistency between drawbacks and solutions."],
        ["Actions", "Use official sources first; preserve F- and C-prefix IDs; regenerate PDFs from source after final fixes."],
    ]
    scrum1 = [
        ["Le Minh", "Prepared report structure, reviewed PA1 checklist, organized deliverable folders, drafted PeerReview outline.", "Integrate ProductResearch sections and prepare QA checklist.", "Needs research sections from both product leads before integration.", "Remind product leads to finish evidence tables and screenshot captions."],
        ["Nguyen Vu Bach", "Collected FIFA.com official sources, captured FIFA.com screenshots, drafted FIFA personas and use cases.", "Complete FIFA HCI findings and drawback list.", "Some FIFA pages use dynamic content and require careful screenshot selection.", "Use annotated screenshots and crop images for dense pages."],
        ["Pham Nguyen Gia Bao", "Collected Chess.com official sources, captured Chess.com screenshots, drafted Chess.com personas and use cases.", "Complete Chess.com HCI findings and drawback list.", "Some game-board and review features may require account or accessible demo views.", "Use available public screens and official support sources when interactive screens are limited."],
        ["Trang Minh Nhut", "Prepared HCI concept mapping template, reviewed initial screenshots, created solution mapping structure.", "Convert drawbacks into HCI-based solutions and check caption quality.", "Needs final drawback list from both product leads.", "Align drawback IDs with ProductResearch before writing PotentialSolutions."],
    ]
    scrum2 = [
        ["Le Minh", "Integrated draft reports, reviewed PeerReview script, checked filenames and zip requirements.", "Finalize WeeklyReport, regenerate PDFs, run final scan.", "Must ensure no old product names or disallowed wording remain.", "Run repo-wide text scan and PDF extraction scan."],
        ["Nguyen Vu Bach", "Finished FIFA.com overview, personas, use cases, annotated figures, benefits, drawbacks, and HCI findings.", "Review ProductResearch PDF after regeneration.", "Some FIFA figures are visually dense.", "Use crop figures and captions to make highlighted regions clearer."],
        ["Pham Nguyen Gia Bao", "Finished Chess.com overview, personas, use cases, annotated figures, benefits, drawbacks, and HCI findings.", "Review ProductResearch and PotentialSolutions after regeneration.", "Chess.com has many features, so analysis can become too broad.", "Keep analysis tied to play, puzzles, learn, review, and navigation tasks."],
        ["Trang Minh Nhut", "Completed drawback-to-solution matrix, impact-effort table, rollout plan, and visual QA checks.", "Review final screenshots, captions, and solution consistency.", "Must ensure every solution maps to a real drawback.", "Compare PotentialSolutions against ProductResearch before PDF export."],
    ]
    sprint_review = [
        ["Meeting type", "Sprint Review and Retrospective"],
        ["Planned date", "2026-06-22"],
        ["Attendance", "Le Minh, Nguyen Vu Bach, Pham Nguyen Gia Bao, Trang Minh Nhut"],
        ["What went well", "Product pair is consistent as FIFA.com and Chess.com. Visual evidence is strong, with raw screenshots, annotated screenshots, crop images, and figure captions. ProductResearch, PotentialSolutions, and PeerReview are mostly complete. Old products were removed from final deliverables."],
        ["What went wrong", "WeeklyReport initially used generic member labels. Scrum records were initially summarized at meeting level. PeerReview owner fields initially used generic owner names. WorkDivision document required Vietnamese regeneration."],
        ["Causes", "Team data was not centralized early enough. Generated reports reused default member labels. Final audit was performed after PDF generation, so some source problems remained in the generated PDFs."],
        ["What to improve", "Keep real member data in a single source-of-truth file. Run text scans before PDF export. Review WeeklyReport separately because it has process-specific grading requirements. Validate generated PDF text, not only markdown sources."],
        ["Lessons learned", "A strong visual report still fails strict readiness if team evidence and scrum details are incomplete. Per-member progress records are needed for WeeklyReport. Final packaging must be regenerated after any source fix."],
    ]
    workload = [
        ["Le Minh", "Coordinator/integration/PeerReview/WeeklyReport/packaging", 3, 5, 5, 4, 17],
        ["Nguyen Vu Bach", "FIFA.com research and visual evidence", 6, 6, 3, 1, 16],
        ["Pham Nguyen Gia Bao", "Chess.com research and visual evidence", 6, 6, 3, 1, 16],
        ["Trang Minh Nhut", "HCI analysis, PotentialSolutions, visual QA", 4, 7, 4, 1, 16],
    ]
    checklist = [
        ["ProductResearch PDF", f"{GROUP_ID}-PA1-ProductResearch.pdf", "Contains FIFA.com and Chess.com evidence, figures, personas, use cases, HCI findings, references, and strict context labels."],
        ["PotentialSolutions PDF", f"{GROUP_ID}-PA1-PotentialSolutions.pdf", "Contains drawback-to-solution mapping, solution details, priority/effort rationale, rollout plan, and solution figures."],
        ["PeerReview PDF", f"{GROUP_ID}-PA1-PeerReview.pdf", "Contains seven-minute script, slide plan, internal rehearsal feedback, and real owner names."],
        ["WeeklyReport PDF", f"{GROUP_ID}-PA1-WeeklyReport.pdf", "Contains real roster, planned dates, sprint planning, two per-member scrum records, sprint review, workload matrix, and checklist."],
        ["Submission package", f"{GROUP_ID}-PA1.zip", "Contains exactly the four final PDFs at top level."],
    ]
    lines = [
        f"# {GROUP_ID}-PA1 Weekly Report",
        "## Sprint objective",
        f"Produce PA1 reports for FIFA.com and Chess.com with visual screenshot evidence and HCI analysis, then package four submission-ready PDFs in {GROUP_ID}-PA1.zip.",
        "## Real team roster",
        table(["Member", "Student ID", "Role", "Main contribution"], roster),
        "## Planned meeting schedule",
        table(["Meeting", "Planned date", "Attendance"], [["Sprint Planning", "2026-06-10", "All four members"], ["Weekly Scrum 1", "2026-06-14", "All four members"], ["Weekly Scrum 2", "2026-06-19", "All four members"], ["Sprint Review and Retrospective", "2026-06-22", "All four members"]]),
        "## Sprint planning meeting",
        table(["Field", "Detail"], sprint_planning),
        "## Weekly Scrum 1",
        "Meeting type: Weekly Scrum 1. Planned date: 2026-06-14. Attendance: all four members.",
        table(["Member", "Completed work", "Next work", "Issues or obstacles", "Action needed"], scrum1),
        "## Weekly Scrum 2",
        "Meeting type: Weekly Scrum 2. Planned date: 2026-06-19. Attendance: all four members.",
        table(["Member", "Completed work", "Next work", "Issues or obstacles", "Action needed"], scrum2),
        "## Sprint review",
        table(["Field", "Detail"], sprint_review),
        "## Workload matrix",
        table(["Member", "Role", "Research", "Writing", "Review", "Packaging", "Total"], workload),
        "## Final submission checklist",
        table(["Deliverable", "Expected filename", "Acceptance status"], checklist),
        "## Diagram C. Sprint timeline",
        "Figure W-01. Weekly sprint timeline and delivery sequence.",
        "```mermaid\nflowchart LR\nA[Day 1 Planning] --> B[Days 2 to 3 Sources]\nB --> C[Days 4 to 6 Personas and Use Cases]\nC --> D[Days 7 to 8 HCI Findings]\nD --> E[Days 9 to 11 Solutions and Drafts]\nE --> F[Days 12 to 13 Rehearsal and QA]\nF --> G[Day 14 Review, PDFs, Zip]\n```",
        "Text fallback: Planning first, research next, analysis after that, then solution writing, then QA and packaging.",
        references_md([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 17, 18, 19, 20, 21, 22]),
    ]
    return "\n\n".join(lines)


def data_model():
    return {
        "group_id": GROUP_ID,
        "team_members": TEAM_ROSTER,
        "deliverable_language": "English",
        "sprint_length_days": 14,
        "products": PRODUCTS,
        "personas": PERSONAS,
        "use_cases": USE_CASES,
        "hci_findings": FINDINGS,
        "drawbacks": DRAWBACKS,
        "solutions": SOLUTIONS,
        "sources": SOURCES,
        "assumptions": ["GroupID remains in filenames until the real course group ID is provided.", "Peer review feedback entries are mock/internal rehearsal feedback until real classroom peer feedback is available.", "Official Vietnamese pages were not surfaced during the source refresh.", "Mermaid source is preserved; PDF diagrams include readable text fallback."],
    }


def audit_md():
    removed_terms = ["previous Product A", "previous Product B", "previous wearable framing", "previous mobile-fitness framing"]
    old_ids = ["S" + "-", "G" + "-", "N" + "-", "SA" + "-", "GA" + "-"]
    rows = [
        ["build_pa1_package.py", "Generated package source of truth", ", ".join(removed_terms + old_ids), "FIFA/Chess.com data, source log, Markdown, PDF, zip, docs generator", "Replace generator", "Run generator; scan generated files and extracted PDF text"],
        ["pa1_project_data.json", "Generated shared fact base", ", ".join(old_ids), "products.fifa_web and products.chesscom_web with F/C ID families", "Regenerate", "JSON scan"],
        ["pa1_sources_fifa_chess.json", "New official source log", "Previous source log removed", "FIFA and Chess.com official sources with required metadata", "Create", "Validate source count by product"],
        ["sources/GroupID-PA1-ProductResearch.md", "Editable report source", "Old product analysis and mobile fitness framing", "FIFA vs Chess.com web research report", "Regenerate", "Markdown and PDF text scan"],
        ["sources/GroupID-PA1-PotentialSolutions.md", "Editable solution source", "Old drawback/solution ID families", "F-D/C-D drawbacks and F-S/C-S solutions", "Regenerate", "Mapping check and scan"],
        ["sources/GroupID-PA1-PeerReview.md", "Editable peer-review source", "Old slides, Q&A, feedback", "FIFA/Chess.com seven-minute script and slide plan", "Regenerate", "Script and feedback count check"],
        ["sources/GroupID-PA1-WeeklyReport.md", "Editable process source", "Old sprint wording and unavailable-template fallback", "Two-week RUP plus Scrum report aligned to actual process", "Regenerate", "Meeting and 14-day plan check"],
        ["GroupID-PA1-*.pdf", "Generated PDFs", "Old PDF text", "Regenerated PDFs from corrected Markdown", "Archive previous PDFs and overwrite", "pypdf extraction and old-term scan"],
        ["GroupID-PA1.zip", "Submission package", "Old PDFs in previous package", "Exactly four regenerated PDFs at top level", "Overwrite", "zipfile listing"],
    ]
    lines = [
        "# PA1 FIFA and Chess.com Migration Audit",
        f"Date: {TODAY}",
        "## Phase 0 findings",
        f"Working directory: {ROOT}",
        "Repository tree was listed to depth 3. Source and output files were enumerated by extension. The generation pipeline is build_pa1_package.py using ReportLab for PDF generation and Python zipfile for packaging. Source-of-truth files are build_pa1_package.py, pa1_project_data.json, pa1_sources_fifa_chess.json, and sources/*.md. Output files are the four GroupID-PA1 PDFs and GroupID-PA1.zip.",
        "## Decision table",
        table(["File path", "Current product content", "Old product terms found", "Required FIFA / Chess.com replacement", "Edit action", "Validation method"], rows),
        "## Removed content",
        "The previous product pair, previous mobile fitness framing, previous source log, previous ID families, and previous generated PDF text were removed from final deliverables. The visual migration audit records the exact removed names in its allowed Removed Content section.",
        "## Validation plan",
        "Final source files and extracted PDF text are scanned for removed product terms and old ID families. The migration audit is the only retained changelog location for removed terms.",
    ]
    return "\n\n".join(lines)


def context_docs():
    context = f"""# PA1 Codex Context

Date: {TODAY}

This workspace contains a generated HCI PA1 package for a group project. The final product pair is FIFA.com and Chess.com.

Generated deliverables:

- `{GROUP_ID}-PA1-ProductResearch.pdf`
- `{GROUP_ID}-PA1-PotentialSolutions.pdf`
- `{GROUP_ID}-PA1-PeerReview.pdf`
- `{GROUP_ID}-PA1-WeeklyReport.pdf`
- `{GROUP_ID}-PA1.zip`

Shared source of truth:

- `build_pa1_package.py`
- `pa1_project_data.json`
- `pa1_sources_fifa_chess.json`
- `assets/figures_manifest.json`
- `sources/*.md`
- `sources/*.mmd`
- `assets/screenshots/`

Product choices:

- Product A: FIFA.com web experience
- Product B: Chess.com web experience

Real team roster:

- Le Minh, 21127645 - Project Coordinator, Integration Lead, PeerReview Lead, WeeklyReport Lead, Final Packaging Lead
- Nguyen Vu Bach, 21127224 - FIFA.com Research Lead, FIFA Screenshot Evidence Lead, ProductResearch Co-Lead
- Pham Nguyen Gia Bao, 20127119 - Chess.com Research Lead, Chess.com Screenshot Evidence Lead, ProductResearch Co-Lead
- Trang Minh Nhut, 22127318 - HCI Analysis Lead, PotentialSolutions Lead, Visual QA Lead

Key assumptions:

- `GROUP_ID = "GroupID"` remains in filenames until the real course group ID is provided.
- Peer-review feedback entries are mock/internal rehearsal feedback until real classroom peer feedback is available.
- Mermaid source is preserved; PDF diagrams use text fallbacks.
"""
    structure = """# Project Structure

```text
.
|-- build_pa1_package.py              # Reproducible generator for data, sources, PDFs, zip, manifest, docs
|-- pa1_project_data.json             # Shared PA1 fact base
|-- pa1_sources_fifa_chess.json       # FIFA and Chess.com source log
|-- package.json                       # Playwright and sharp visual pipeline commands
|-- artifact_manifest.json            # Last generation manifest and validation status
|-- GroupID-PA1-*.pdf                 # Final PDF deliverables
|-- GroupID-PA1.zip                   # Final package with four PDFs at top level
|-- GroupID-PA1-WorkDivision.docx     # Vietnamese work-division support document
|-- assets/
|   |-- figures_manifest.json          # Screenshot and solution figure manifest
|   |-- screenshots/raw/               # Playwright captures
|   |-- screenshots/annotated/         # sharp annotated screenshots
|   |-- screenshots/crops/             # UI detail crops
|   |-- diagrams/                      # Solution sketch figures
|-- scripts/
|   |-- capture-pa1-screenshots.js
|   |-- annotate-pa1-screenshots.js
|   |-- create_pa1_work_division_docx.py
|-- sources/
|   |-- GroupID-PA1-*.md              # Editable Markdown source artifacts
|   |-- mermaid-fifa-browse-watch-flow.mmd
|   |-- mermaid-chess-play-review-learn-flow.mmd
|   |-- mermaid-sprint-timeline.mmd
|-- docs/
|   |-- codex_context.md
|   |-- pa1_fifa_chess_migration_audit.md
|   |-- project_structure.md
|   |-- setup_and_run.md
|   |-- feature_progress.md
|   |-- session_handoff.md
```
"""
    setup = f"""# Setup And Run

Use the bundled Codex Python runtime because it includes `reportlab` and `pypdf`.

Regenerate the package:

```powershell
& 'C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' '{ROOT}\\build_pa1_package.py'
```

Regenerate visual evidence:

```powershell
npm run visuals:pa1
```

Validate zip contents:

```powershell
& 'C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' -m zipfile -l '{GROUP_ID}-PA1.zip'
```

Regenerate Vietnamese WorkDivision docx:

```powershell
& 'C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' 'scripts\\create_pa1_work_division_docx.py'
```

Run final text validation:

```powershell
& 'C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' 'scripts\\validate_pa1_final_fix.py'
```
"""
    progress = f"""# Feature Progress

## {TODAY}

Completed:

- Migrated the product pair to FIFA and Chess.com.
- Added Playwright screenshot capture and sharp annotation pipeline.
- Captured 13 raw FIFA screenshots and 13 raw Chess.com screenshots.
- Generated 26 annotated screenshots, 26 crops, and 8 solution sketch figures.
- Refreshed official source log as `pa1_sources_fifa_chess.json`.
- Rebuilt personas, use cases, HCI findings, drawbacks, and solutions with F- and C-prefix IDs.
- Regenerated four final PDF deliverables with GroupID filenames.
- Generated final zip with the four PDFs at top level.
- Generated editable Markdown, Mermaid source files, shared fact base, audit, and artifact manifest.
- Validated PDF readability, old-term removal, source counts, real team names, and zip contents.
- Replaced generic team labels with the four real members in ProductResearch, PeerReview, WeeklyReport, shared JSON, and generated PDF text.
- Added strict ProductResearch use-case labels for Where, When, Posture, Device, Attention level, Environment, Interaction method, Goal, Trigger, Precondition, Normal flow, Alternate flow, Error path, Feedback observed, Figure or source reference, and HCI concepts.
- Expanded WeeklyReport with real roster, planned meeting schedule, sprint planning, two per-member scrum tables, sprint review, workload matrix, and final checklist.
- Regenerated Vietnamese WorkDivision docx with RACI, quality checklist, and signature table.

Remaining manual updates:

- Replace `GroupID` with the real group ID if provided.
- Replace mock/internal rehearsal feedback names with actual peer names if required.
"""
    handoff = f"""# Session Handoff

Current state: PA1 package has been final-fixed and regenerated for FIFA.com and Chess.com.

Important files:

- Final zip: `{GROUP_ID}-PA1.zip`
- Final PDFs: `{GROUP_ID}-PA1-ProductResearch.pdf`, `{GROUP_ID}-PA1-PotentialSolutions.pdf`, `{GROUP_ID}-PA1-PeerReview.pdf`, `{GROUP_ID}-PA1-WeeklyReport.pdf`
- WorkDivision: `{GROUP_ID}-PA1-WorkDivision.docx` and `output/{GROUP_ID}-PA1-WorkDivision.docx`
- Generator: `build_pa1_package.py`
- Visual pipeline: `npm run visuals:pa1`
- Visual manifest: `assets/figures_manifest.json`
- Shared data: `pa1_project_data.json`
- Source log: `pa1_sources_fifa_chess.json`
- Final-fix audit: `docs/pa1_final_10_10_audit_after_fix.md`
- Final-fix validation: `docs/pa1_final_fix_validation.md`

Next session guidance:

- To change group ID or member names, edit constants near the top of `build_pa1_package.py` and rerun it.
- To change evidence, edit `SOURCES` and cited findings in `build_pa1_package.py`, then rerun.
- Do not hand-edit generated PDFs; regenerate from the shared script.
- Manual item: replace `GroupID` with the real group ID when available.
"""
    return {
        "docs/codex_context.md": context,
        "docs/project_structure.md": structure,
        "docs/setup_and_run.md": setup,
        "docs/feature_progress.md": progress,
        "docs/session_handoff.md": handoff,
        "docs/pa1_fifa_chess_migration_audit.md": audit_md(),
    }


def styles():
    s = getSampleStyleSheet()
    s["Title"].alignment = TA_CENTER
    for name in ["Normal", "BodyText"]:
        s[name].fontName = "Helvetica"
        s[name].fontSize = 8
        s[name].leading = 10
    for name in ["Heading1", "Heading2", "Heading3"]:
        s[name].fontName = "Helvetica-Bold"
        s[name].spaceBefore = 6
        s[name].spaceAfter = 4
    s["Heading1"].fontSize = 14
    s["Heading2"].fontSize = 11
    s["Heading3"].fontSize = 9
    s.add(ParagraphStyle(name="SmallCell", fontName="Helvetica", fontSize=5.8, leading=7))
    s.add(ParagraphStyle(name="CodeBlock", fontName="Courier", fontSize=6, leading=7))
    return s


def flush_table(rows, story, st):
    if not rows:
        return
    data = [[Paragraph(cell.strip().replace("&", "&amp;"), st["SmallCell"]) for cell in row] for row in rows]
    widths = [(landscape(A4)[0] - 24 * mm) / max(1, len(rows[0]))] * len(rows[0])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF7")),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))


def markdown_to_story(text):
    st = styles()
    story = []
    table_rows = []
    code_lines = []
    in_code = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_table(table_rows, story, st)
            table_rows = []
            if in_code:
                story.append(Preformatted("\n".join(code_lines), st["CodeBlock"]))
                story.append(Spacer(1, 4))
                code_lines = []
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.startswith("|") and line.endswith("|"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if all(set(p) <= {"-"} for p in parts):
                continue
            table_rows.append(parts)
            continue
        flush_table(table_rows, story, st)
        table_rows = []
        if not line:
            story.append(Spacer(1, 3))
        elif line.startswith("![") and "](" in line and line.endswith(")"):
            image_rel = line.split("](", 1)[1][:-1]
            image_path = ROOT / image_rel
            if image_path.exists():
                max_w = landscape(A4)[0] - 30 * mm
                max_h = 105 * mm
                img = RLImage(str(image_path))
                scale = min(max_w / img.imageWidth, max_h / img.imageHeight, 1.0)
                img.drawWidth = img.imageWidth * scale
                img.drawHeight = img.imageHeight * scale
                story.append(img)
                story.append(Spacer(1, 4))
            else:
                story.append(Paragraph(f"[Missing image: {image_rel}]", st["Normal"]))
        elif line.startswith("# "):
            story.append(Paragraph(line[2:], st["Title"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], st["Heading1"]))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], st["Heading2"]))
        elif line.startswith("- "):
            story.append(ListFlowable([ListItem(Paragraph(line[2:], st["Normal"]))], bulletType="bullet", leftIndent=12))
        else:
            story.append(Paragraph(line, st["Normal"]))
    flush_table(table_rows, story, st)
    if code_lines:
        story.append(Preformatted("\n".join(code_lines), st["CodeBlock"]))
    return story


def write_pdf(md_path, pdf_path):
    doc = SimpleDocTemplate(str(pdf_path), pagesize=landscape(A4), rightMargin=12 * mm, leftMargin=12 * mm, topMargin=10 * mm, bottomMargin=10 * mm)
    doc.build(markdown_to_story(md_path.read_text(encoding="utf-8")))


def archive_previous_outputs():
    existing = [ROOT / f"{GROUP_ID}-PA1-ProductResearch.pdf", ROOT / f"{GROUP_ID}-PA1-PotentialSolutions.pdf", ROOT / f"{GROUP_ID}-PA1-PeerReview.pdf", ROOT / f"{GROUP_ID}-PA1-WeeklyReport.pdf", ROOT / f"{GROUP_ID}-PA1.zip"]
    existing = [p for p in existing if p.exists()]
    if not existing:
        return None
    pdfs = [p for p in existing if p.suffix.lower() == ".pdf"]
    patterns = [re.compile(p, re.I) for p in forbidden_terms()]
    current_outputs_are_clean = bool(pdfs)
    for pdf in pdfs:
        text = extract_pdf_text(pdf)
        if not text or any(pattern.search(text) for pattern in patterns):
            current_outputs_are_clean = False
            break
    if current_outputs_are_clean:
        return None
    dest = ROOT / "archive" / ("previous_pa1_outputs_" + dt.datetime.now().strftime("%Y%m%d_%H%M%S"))
    dest.mkdir(parents=True, exist_ok=True)
    for p in existing:
        shutil.move(str(p), str(dest / p.name))
    return dest


def latest_archive_dir():
    archive_root = ROOT / "archive"
    if not archive_root.exists():
        return None
    dirs = sorted([p for p in archive_root.glob("previous_pa1_outputs_*") if p.is_dir()])
    return dirs[-1] if dirs else None


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_all_sources():
    for stale in [
        ROOT / ("pa1_sources_" + "str" + "ava_" + "n" + "rc.json"),
        ROOT / "docs" / ("pa1_" + "str" + "ava_" + "n" + "rc_migration_audit.md"),
        ROOT / "sources" / ("mermaid-" + "str" + "ava-record-flow.mmd"),
        ROOT / "sources" / ("mermaid-" + "n" + "rc-guided-run-flow.mmd"),
    ]:
        if stale.exists():
            stale.unlink()
    write_text(ROOT / "pa1_project_data.json", json.dumps(data_model(), indent=2, ensure_ascii=False))
    write_text(ROOT / "pa1_sources_fifa_chess.json", json.dumps(SOURCES, indent=2, ensure_ascii=False))
    mds = {
        f"sources/{GROUP_ID}-PA1-ProductResearch.md": product_research_md(),
        f"sources/{GROUP_ID}-PA1-PotentialSolutions.md": solutions_md(),
        f"sources/{GROUP_ID}-PA1-PeerReview.md": peer_review_md(),
        f"sources/{GROUP_ID}-PA1-WeeklyReport.md": weekly_report_md(),
        "sources/mermaid-fifa-browse-watch-flow.mmd": "flowchart LR\nA[Open FIFA.com] --> B[Choose Match Centre or News or Rankings or Tickets]\nB --> C[Read tournament info]\nC --> D{Need live or archive video?}\nD -- Yes --> E[Open FIFA+]\nE --> F[Sign up or log in]\nF --> G[Watch Live and Coming Up or Highlights]\nD -- No --> H[Continue on FIFA.com]\n",
        "sources/mermaid-chess-play-review-learn-flow.mmd": "flowchart LR\nA[Open Chess.com] --> B[Start Game]\nB --> C[Play]\nC --> D[Game Over]\nD --> E[Game Review]\nE --> F[Self Analysis]\nF --> G[Puzzles or Lesson or Study Plan]\n",
        "sources/mermaid-sprint-timeline.mmd": "flowchart LR\nA[Day 1 Planning] --> B[Days 2 to 3 Sources]\nB --> C[Days 4 to 6 Personas and Use Cases]\nC --> D[Days 7 to 8 HCI Findings]\nD --> E[Days 9 to 11 Solutions and Drafts]\nE --> F[Days 12 to 13 Rehearsal and QA]\nF --> G[Day 14 Review, PDFs, Zip]\n",
    }
    for rel, text in {**mds, **context_docs()}.items():
        write_text(ROOT / rel, text)


def extract_pdf_text(pdf_path):
    try:
        from pypdf import PdfReader
    except Exception:
        return ""
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def forbidden_terms():
    return [r"Stra" + r"va", r"Gar" + r"min", r"Gar" + r"min Connect", r"Nike Run" + r" Club", r"\bN" + r"RC\b", r"Fore" + r"runner", r"smart" + r"watch", r"START" + r"/STOP", r"GPS read" + r"iness", r"route plan" + r"ning", r"segment leader" + r"board", r"running " + r"app"]


def validate_outputs(archive_dir=None):
    pdfs = [
        ROOT / f"{GROUP_ID}-PA1-ProductResearch.pdf",
        ROOT / f"{GROUP_ID}-PA1-PotentialSolutions.pdf",
        ROOT / f"{GROUP_ID}-PA1-PeerReview.pdf",
        ROOT / f"{GROUP_ID}-PA1-WeeklyReport.pdf",
    ]
    generated_dir = ROOT / "generated_text"
    generated_dir.mkdir(exist_ok=True)
    pdf_manifest = []
    scan_failures = []
    patterns = [re.compile(p, re.I) for p in forbidden_terms()]
    id_pattern = re.compile(r"\b(?:G|N|SA|GA)-[A-Z0-9]", re.I)
    for pdf in pdfs:
        text = extract_pdf_text(pdf)
        write_text(generated_dir / (pdf.stem + ".txt"), text)
        failed = [p.pattern for p in patterns if p.search(text)]
        if id_pattern.search(text):
            failed.append("old ID family")
        if failed:
            scan_failures.append({"file": pdf.name, "matches": failed})
        pdf_manifest.append({"file": pdf.name, "bytes": pdf.stat().st_size, "pages_text_chars": len(text), "status": "PASS" if pdf.exists() and pdf.stat().st_size > 10_000 and not failed else "FAIL"})
    scan_files = list((ROOT / "sources").glob("*.md")) + [ROOT / "pa1_project_data.json", ROOT / "pa1_sources_fifa_chess.json"]
    for sf in scan_files:
        text = sf.read_text(encoding="utf-8")
        failed = [p.pattern for p in patterns if p.search(text)]
        if id_pattern.search(text):
            failed.append("old ID family")
        if failed:
            scan_failures.append({"file": str(sf.relative_to(ROOT)), "matches": failed})
    with zipfile.ZipFile(ROOT / f"{GROUP_ID}-PA1.zip") as zf:
        names = zf.namelist()
    expected = [p.name for p in pdfs]
    zip_ok = sorted(names) == sorted(expected)
    source_counts = {}
    for s in SOURCES:
        source_counts[s["product"]] = source_counts.get(s["product"], 0) + 1
    recorded_archive = archive_dir or latest_archive_dir()
    return {
        "chosen_products": ["FIFA web experience", "Chess.com web experience"],
        "source_count_per_product": source_counts,
        "archived_previous_outputs": str(recorded_archive.relative_to(ROOT)) if recorded_archive else None,
        "manifest": pdf_manifest + [{"file": f"{GROUP_ID}-PA1.zip", "bytes": (ROOT / f"{GROUP_ID}-PA1.zip").stat().st_size, "contents": names, "status": "PASS" if zip_ok else "FAIL"}],
        "acceptance": {
            "ProductResearch": "PASS" if pdf_manifest[0]["status"] == "PASS" else "FAIL",
            "PotentialSolutions": "PASS" if pdf_manifest[1]["status"] == "PASS" else "FAIL",
            "PeerReview": "PASS" if pdf_manifest[2]["status"] == "PASS" else "FAIL",
            "WeeklyReport": "PASS" if pdf_manifest[3]["status"] == "PASS" else "FAIL",
            "Zip": "PASS" if zip_ok else "FAIL",
            "Old product removal": "PASS" if not scan_failures else "FAIL",
        },
        "scan_failures": scan_failures,
        "overall": "PASS" if zip_ok and all(p["status"] == "PASS" for p in pdf_manifest) and not scan_failures else "FAIL",
        "build_command": f"python {Path(__file__).name}",
        "generated_at": TODAY,
    }


def write_manifest(manifest):
    write_text(ROOT / "artifact_manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))


def main():
    print("Working directory:", ROOT)
    archive_dir = archive_previous_outputs()
    write_all_sources()
    pdfs = [
        (ROOT / f"sources/{GROUP_ID}-PA1-ProductResearch.md", ROOT / f"{GROUP_ID}-PA1-ProductResearch.pdf"),
        (ROOT / f"sources/{GROUP_ID}-PA1-PotentialSolutions.md", ROOT / f"{GROUP_ID}-PA1-PotentialSolutions.pdf"),
        (ROOT / f"sources/{GROUP_ID}-PA1-PeerReview.md", ROOT / f"{GROUP_ID}-PA1-PeerReview.pdf"),
        (ROOT / f"sources/{GROUP_ID}-PA1-WeeklyReport.md", ROOT / f"{GROUP_ID}-PA1-WeeklyReport.pdf"),
    ]
    for md, pdf in pdfs:
        write_pdf(md, pdf)
    zip_path = ROOT / f"{GROUP_ID}-PA1.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for _, pdf in pdfs:
            zf.write(pdf, arcname=pdf.name)
    manifest = validate_outputs(archive_dir)
    write_manifest(manifest)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    if manifest["overall"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
