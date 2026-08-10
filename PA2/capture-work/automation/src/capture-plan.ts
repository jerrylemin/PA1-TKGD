import type { CaptureAction, CaptureTarget } from "./types.js";

const waitForText = (text: string): CaptureAction[] => [{ type: "waitForText", text }];
const clickButton = (name: string): CaptureAction[] => [
  { type: "clickRole", role: "button", name }
];
const clickLink = (name: string): CaptureAction[] => [
  { type: "clickRole", role: "link", name }
];

const fifaHome = "https://www.fifa.com/en";
const fifaMatchCentre = "https://www.fifa.com/en/match-centre";
const fifaSearch = "https://www.fifa.com/en/search?q=world%20cup";
const fifaArticle =
  "https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september";
const fifaTournament =
  "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026";
const fifaRankings = "https://inside.fifa.com/fifa-world-ranking/men";
const fifaTickets = "https://www.fifa.com/en/tickets";
const fifaPlusEntry = "https://www.fifa.com/en/fifa-plus";
const fifaPlus = "https://www.plus.fifa.com/";

export const fifaTargets: CaptureTarget[] = [
  {
    captureId: "fifa-01-homepage-desktop",
    product: "fifa",
    viewport: "desktop",
    pageArea: "homepage",
    state: "homepage",
    url: fifaHome,
    relatedPa1Figure: "F-01",
    relatedPa1UseCase: "F-UC1"
  },
  {
    captureId: "fifa-02-global-navigation-desktop",
    product: "fifa",
    viewport: "desktop",
    pageArea: "global navigation",
    state: "default",
    url: fifaHome,
    relatedPa1Figure: "F-02"
  },
  {
    captureId: "fifa-03-homepage-hero-desktop",
    product: "fifa",
    viewport: "desktop",
    pageArea: "homepage hero",
    state: "default",
    url: fifaHome,
    relatedPa1Figure: "F-01"
  },
  {
    captureId: "fifa-04-homepage-mobile",
    product: "fifa",
    viewport: "mobile",
    pageArea: "homepage",
    state: "default",
    url: fifaHome,
    relatedPa1Figure: "F-03"
  },
  {
    captureId: "fifa-05-mobile-navigation-open",
    product: "fifa",
    viewport: "mobile",
    pageArea: "global navigation",
    state: "menu open",
    url: fifaHome,
    relatedPa1Figure: "F-03",
    actions: clickButton("Menu")
  },
  {
    captureId: "fifa-06-match-centre",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Match Centre",
    state: "default",
    url: fifaMatchCentre,
    relatedPa1Figure: "F-04",
    relatedPa1UseCase: "F-UC1"
  },
  {
    captureId: "fifa-07-match-centre-today",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Match Centre",
    state: "Today",
    url: fifaMatchCentre,
    relatedPa1UseCase: "F-UC1",
    actions: clickButton("Today")
  },
  {
    captureId: "fifa-08-match-centre-live",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Match Centre",
    state: "Live",
    url: fifaMatchCentre,
    relatedPa1UseCase: "F-UC2",
    actions: clickButton("Live")
  },
  {
    captureId: "fifa-09-match-centre-results",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Match Centre",
    state: "Results",
    url: fifaMatchCentre,
    relatedPa1UseCase: "F-UC2",
    actions: clickButton("Results")
  },
  {
    captureId: "fifa-10-match-centre-filters",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Match Centre",
    state: "filters open",
    url: fifaMatchCentre,
    relatedPa1Figure: "F-04",
    actions: clickButton("Filter")
  },
  {
    captureId: "fifa-11-search-page",
    product: "fifa",
    viewport: "desktop",
    pageArea: "search",
    state: "query loaded",
    url: fifaSearch,
    relatedPa1Figure: "F-05",
    relatedPa1UseCase: "F-UC5"
  },
  {
    captureId: "fifa-12-search-results-mixed-content",
    product: "fifa",
    viewport: "desktop",
    pageArea: "search results",
    state: "multiple content types",
    url: fifaSearch,
    relatedPa1Figure: "F-05",
    relatedPa1UseCase: "F-UC5",
    actions: waitForText("World Cup")
  },
  {
    captureId: "fifa-13-news-article-full",
    product: "fifa",
    viewport: "desktop",
    pageArea: "news article",
    state: "full article",
    url: fifaArticle,
    relatedPa1Figure: "F-06",
    relatedPa1UseCase: "F-UC3"
  },
  {
    captureId: "fifa-14-article-header",
    product: "fifa",
    viewport: "desktop",
    pageArea: "article header",
    state: "default",
    url: fifaArticle,
    relatedPa1Figure: "F-06",
    relatedPa1UseCase: "F-UC3"
  },
  {
    captureId: "fifa-15-article-body",
    product: "fifa",
    viewport: "desktop",
    pageArea: "article body",
    state: "loaded",
    url: fifaArticle,
    relatedPa1Figure: "F-06",
    relatedPa1UseCase: "F-UC3",
    actions: waitForText("FIFA World Cup 26")
  },
  {
    captureId: "fifa-16-tournament-landing",
    product: "fifa",
    viewport: "desktop",
    pageArea: "tournament",
    state: "landing",
    url: fifaTournament,
    relatedPa1Figure: "F-07",
    relatedPa1UseCase: "F-UC4"
  },
  {
    captureId: "fifa-17-tournament-after-modal-dismiss",
    product: "fifa",
    viewport: "desktop",
    pageArea: "tournament",
    state: "after modal dismissed",
    url: fifaTournament,
    relatedPa1Figure: "F-07",
    relatedPa1UseCase: "F-UC4"
  },
  {
    captureId: "fifa-18-tournament-subnavigation",
    product: "fifa",
    viewport: "desktop",
    pageArea: "tournament subnavigation",
    state: "default",
    url: fifaTournament,
    relatedPa1Figure: "F-07"
  },
  {
    captureId: "fifa-19-rankings",
    product: "fifa",
    viewport: "desktop",
    pageArea: "rankings",
    state: "men ranking",
    url: fifaRankings
  },
  {
    captureId: "fifa-20-tickets-hospitality-landing",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Tickets and Hospitality",
    state: "landing",
    url: fifaTickets,
    relatedPa1UseCase: "F-UC4"
  },
  {
    captureId: "fifa-21-tournament-logo-row",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Tickets and Hospitality",
    state: "tournament logo row",
    url: fifaTickets,
    actions: waitForText("Tickets")
  },
  {
    captureId: "fifa-22-ticket-card",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket card",
    state: "current",
    url: fifaTickets,
    actions: waitForText("Tickets")
  },
  {
    captureId: "fifa-23-hospitality-card",
    product: "fifa",
    viewport: "desktop",
    pageArea: "hospitality card",
    state: "current",
    url: fifaTickets,
    actions: waitForText("Hospitality")
  },
  {
    captureId: "fifa-24-explore-details-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket CTA",
    state: "Explore details",
    url: fifaTickets,
    actions: waitForText("Explore details")
  },
  {
    captureId: "fifa-25-buy-now-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket CTA",
    state: "Buy now",
    url: fifaTickets,
    actions: waitForText("Buy now")
  },
  {
    captureId: "fifa-26-buy-packages-now-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "hospitality CTA",
    state: "Buy Packages Now",
    url: fifaTickets,
    actions: waitForText("Buy Packages Now")
  },
  {
    captureId: "fifa-27-register-interest-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket CTA",
    state: "Register your interest",
    url: fifaTickets,
    actions: waitForText("Register your interest")
  },
  {
    captureId: "fifa-28-coming-soon-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket availability",
    state: "Coming soon",
    url: fifaTickets,
    actions: waitForText("Coming soon")
  },
  {
    captureId: "fifa-29-sold-out-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket availability",
    state: "Sold out",
    url: fifaTickets,
    actions: waitForText("Sold out")
  },
  {
    captureId: "fifa-30-waiting-room-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket availability",
    state: "Waiting room",
    url: fifaTickets,
    actions: waitForText("Waiting room")
  },
  {
    captureId: "fifa-31-resale-state",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket availability",
    state: "Resale",
    url: fifaTickets,
    actions: waitForText("Resale")
  },
  {
    captureId: "fifa-32-before-partner-handoff",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket handoff",
    state: "before partner handoff",
    url: fifaTickets,
    actions: waitForText("Buy")
  },
  {
    captureId: "fifa-33-partner-after-public-redirect",
    product: "fifa",
    viewport: "desktop",
    pageArea: "ticket partner",
    state: "after redirect",
    url: fifaTickets,
    actions: [...clickLink("Buy now"), { type: "wait", milliseconds: 3000 }]
  },
  {
    captureId: "fifa-34-fifa-plus-entry",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ entry",
    state: "FIFA.com entry",
    url: fifaPlusEntry,
    relatedPa1Figure: "F-10B"
  },
  {
    captureId: "fifa-35-fifa-plus-dazn-landing",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+",
    state: "landing",
    url: fifaPlus,
    relatedPa1Figure: "F-10B"
  },
  {
    captureId: "fifa-36-fifa-plus-cookie-before-dismiss",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ cookie banner",
    state: "before dismiss",
    url: fifaPlus,
    relatedPa1Figure: "F-10B",
    captureBeforePopupDismiss: true
  },
  {
    captureId: "fifa-37-fifa-plus-after-cookie-dismiss",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+",
    state: "after cookie dismiss",
    url: fifaPlus,
    relatedPa1Figure: "F-10B"
  },
  {
    captureId: "fifa-38-fifa-plus-hero",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ hero",
    state: "loaded",
    url: fifaPlus,
    relatedPa1Figure: "F-10B"
  },
  {
    captureId: "fifa-39-fifa-plus-live-rail",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ rail",
    state: "Live",
    url: fifaPlus,
    actions: waitForText("Live")
  },
  {
    captureId: "fifa-40-fifa-plus-highlights-rail",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ rail",
    state: "Highlights",
    url: fifaPlus,
    actions: waitForText("Highlights")
  },
  {
    captureId: "fifa-41-fifa-plus-documentary-rail",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ rail",
    state: "Documentary",
    url: fifaPlus,
    actions: waitForText("Documentary")
  },
  {
    captureId: "fifa-42-fifa-plus-competition-rail",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ rail",
    state: "Competition",
    url: fifaPlus,
    actions: waitForText("Competition")
  },
  {
    captureId: "fifa-43-fifa-plus-archive-rail",
    product: "fifa",
    viewport: "desktop",
    pageArea: "FIFA+ rail",
    state: "Archive",
    url: fifaPlus,
    actions: waitForText("Archive")
  },
  {
    captureId: "fifa-44-footer",
    product: "fifa",
    viewport: "desktop",
    pageArea: "footer",
    state: "default",
    url: fifaHome,
    relatedPa1Figure: "F-09B"
  },
  {
    captureId: "fifa-45-footer-ecosystem-navigation",
    product: "fifa",
    viewport: "desktop",
    pageArea: "footer ecosystem navigation",
    state: "default",
    url: fifaHome,
    relatedPa1Figure: "F-09B",
    actions: waitForText("FIFA")
  },
  {
    captureId: "fifa-46-store-page",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Store",
    state: "public landing",
    url: "https://store.fifa.com/",
    relatedPa1Figure: "F-09B"
  },
  {
    captureId: "fifa-47-collect-page",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Collect",
    state: "public landing",
    url: "https://collect.fifa.com/",
    relatedPa1Figure: "F-09B"
  },
  {
    captureId: "fifa-48-rewards-page",
    product: "fifa",
    viewport: "desktop",
    pageArea: "Rewards",
    state: "public landing",
    url: "https://www.fifa.com/en/rewards",
    relatedPa1Figure: "F-09B"
  },
  {
    captureId: "fifa-49-match-centre-mobile",
    product: "fifa",
    viewport: "mobile",
    pageArea: "Match Centre",
    state: "mobile",
    url: fifaMatchCentre,
    relatedPa1Figure: "F-04",
    relatedPa1UseCase: "F-UC1"
  },
  {
    captureId: "fifa-50-article-mobile",
    product: "fifa",
    viewport: "mobile",
    pageArea: "news article",
    state: "mobile",
    url: fifaArticle,
    relatedPa1Figure: "F-06",
    relatedPa1UseCase: "F-UC3"
  },
  {
    captureId: "fifa-51-tickets-mobile",
    product: "fifa",
    viewport: "mobile",
    pageArea: "Tickets and Hospitality",
    state: "mobile",
    url: fifaTickets
  },
  {
    captureId: "fifa-52-fifa-plus-entry-mobile",
    product: "fifa",
    viewport: "mobile",
    pageArea: "FIFA+ entry",
    state: "mobile",
    url: fifaPlusEntry,
    relatedPa1Figure: "F-10B"
  },
  {
    captureId: "fifa-53-promotional-popup",
    product: "fifa",
    viewport: "desktop",
    pageArea: "promotional popup",
    state: "naturally appeared",
    url: fifaTournament,
    captureBeforePopupDismiss: true,
    relatedPa1Figure: "F-07"
  },
  {
    captureId: "fifa-54-cookie-banner",
    product: "fifa",
    viewport: "desktop",
    pageArea: "cookie banner",
    state: "naturally appeared",
    url: fifaHome,
    captureBeforePopupDismiss: true
  }
];

const chessHome = "https://www.chess.com/";
const chessPlay = "https://www.chess.com/play/online";
const chessBot = "https://www.chess.com/play/computer";
const chessPuzzles = "https://www.chess.com/puzzles";
const chessLessons = "https://www.chess.com/lessons";
const chessLearn = "https://www.chess.com/learn";
const chessStudyPlan = "https://www.chess.com/article/view/study-plan-directory";
const chessReview = "https://www.chess.com/analysis";
const chessAnalysis = "https://www.chess.com/analysis";

export const chessTargets: CaptureTarget[] = [
  {
    captureId: "chess-01-homepage-desktop",
    product: "chess",
    viewport: "desktop",
    pageArea: "homepage",
    state: "default",
    url: chessHome,
    relatedPa1Figure: "C-01"
  },
  {
    captureId: "chess-02-side-navigation-desktop",
    product: "chess",
    viewport: "desktop",
    pageArea: "side navigation",
    state: "default",
    url: chessHome,
    relatedPa1Figure: "C-06"
  },
  {
    captureId: "chess-03-homepage-mobile",
    product: "chess",
    viewport: "mobile",
    pageArea: "homepage",
    state: "default",
    url: chessHome,
    relatedPa1Figure: "C-08"
  },
  {
    captureId: "chess-04-mobile-navigation-open",
    product: "chess",
    viewport: "mobile",
    pageArea: "navigation",
    state: "menu open",
    url: chessHome,
    relatedPa1Figure: "C-06M",
    actions: clickButton("Menu")
  },
  {
    captureId: "chess-05-play-entry",
    product: "chess",
    viewport: "desktop",
    pageArea: "Play",
    state: "entry",
    url: chessPlay,
    relatedPa1Figure: "C-02",
    relatedPa1UseCase: "C-UC1"
  },
  {
    captureId: "chess-06-time-control-selector",
    product: "chess",
    viewport: "desktop",
    pageArea: "Play",
    state: "time-control selector open",
    url: chessPlay,
    relatedPa1UseCase: "C-UC1",
    actions: clickButton("Time")
  },
  {
    captureId: "chess-07-custom-game-settings",
    product: "chess",
    viewport: "desktop",
    pageArea: "Play",
    state: "custom game settings",
    url: chessPlay,
    actions: clickButton("Custom")
  },
  {
    captureId: "chess-08-start-game-state",
    product: "chess",
    viewport: "desktop",
    pageArea: "Play",
    state: "Start Game",
    url: chessPlay,
    actions: waitForText("Play")
  },
  {
    captureId: "chess-09-guest-game",
    product: "chess",
    viewport: "desktop",
    pageArea: "game",
    state: "guest",
    url: chessPlay,
    relatedPa1UseCase: "C-UC1",
    actions: waitForText("Guest")
  },
  {
    captureId: "chess-10-bot-game",
    product: "chess",
    viewport: "desktop",
    pageArea: "Play Computer",
    state: "bot selection",
    url: chessBot,
    relatedPa1Figure: "C-03"
  },
  {
    captureId: "chess-11-active-board",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "active",
    url: chessBot,
    relatedPa1Figure: "C-07",
    actions: [...clickButton("Play"), { type: "wait", milliseconds: 2000 }]
  },
  {
    captureId: "chess-12-active-board-clock",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "clock visible",
    url: chessBot,
    relatedPa1Figure: "C-07",
    actions: waitForText("10:00")
  },
  {
    captureId: "chess-13-last-move-indicator",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "last move indicator",
    url: chessBot,
    relatedPa1Figure: "C-07",
    actions: waitForText("Move")
  },
  {
    captureId: "chess-14-legal-move-feedback",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "legal move feedback",
    url: chessBot,
    relatedPa1Figure: "C-07",
    actions: waitForText("Move")
  },
  {
    captureId: "chess-15-draw-control",
    product: "chess",
    viewport: "desktop",
    pageArea: "game controls",
    state: "Draw control",
    url: chessBot,
    actions: waitForText("Draw")
  },
  {
    captureId: "chess-16-resign-control",
    product: "chess",
    viewport: "desktop",
    pageArea: "game controls",
    state: "Resign control",
    url: chessBot,
    actions: waitForText("Resign")
  },
  {
    captureId: "chess-17-settings-control",
    product: "chess",
    viewport: "desktop",
    pageArea: "game controls",
    state: "Settings control",
    url: chessBot,
    actions: waitForText("Settings")
  },
  {
    captureId: "chess-18-board-side-panel",
    product: "chess",
    viewport: "desktop",
    pageArea: "board and side panel",
    state: "default",
    url: chessBot,
    relatedPa1Figure: "C-03"
  },
  {
    captureId: "chess-19-puzzle-landing",
    product: "chess",
    viewport: "desktop",
    pageArea: "Puzzles",
    state: "landing",
    url: chessPuzzles,
    relatedPa1Figure: "C-04",
    relatedPa1UseCase: "C-UC2"
  },
  {
    captureId: "chess-20-puzzle-before-move",
    product: "chess",
    viewport: "desktop",
    pageArea: "Puzzle",
    state: "before move",
    url: chessPuzzles,
    relatedPa1Figure: "C-04A",
    relatedPa1UseCase: "C-UC2"
  },
  {
    captureId: "chess-21-puzzle-after-correct",
    product: "chess",
    viewport: "desktop",
    pageArea: "Puzzle",
    state: "after correct move",
    url: chessPuzzles,
    actions: waitForText("Correct")
  },
  {
    captureId: "chess-22-puzzle-after-wrong",
    product: "chess",
    viewport: "desktop",
    pageArea: "Puzzle",
    state: "after wrong move",
    url: chessPuzzles,
    actions: waitForText("Incorrect")
  },
  {
    captureId: "chess-23-puzzle-feedback",
    product: "chess",
    viewport: "desktop",
    pageArea: "Puzzle",
    state: "feedback",
    url: chessPuzzles,
    actions: waitForText("Puzzle")
  },
  {
    captureId: "chess-24-lessons-landing-loaded",
    product: "chess",
    viewport: "desktop",
    pageArea: "Lessons",
    state: "cards loaded",
    url: chessLessons,
    relatedPa1Figure: "C-05",
    relatedPa1UseCase: "C-UC3",
    actions: waitForText("Lessons")
  },
  {
    captureId: "chess-25-beginner-lesson",
    product: "chess",
    viewport: "desktop",
    pageArea: "Lesson",
    state: "beginner lesson",
    url: chessLessons,
    relatedPa1UseCase: "C-UC3",
    actions: waitForText("Beginner")
  },
  {
    captureId: "chess-26-learn-page",
    product: "chess",
    viewport: "desktop",
    pageArea: "Learn",
    state: "landing",
    url: chessLearn,
    relatedPa1Figure: "C-05"
  },
  {
    captureId: "chess-27-study-plan",
    product: "chess",
    viewport: "desktop",
    pageArea: "Study plan",
    state: "article",
    url: chessStudyPlan,
    relatedPa1UseCase: "C-UC5"
  },
  {
    captureId: "chess-28-game-review",
    product: "chess",
    viewport: "desktop",
    pageArea: "Game Review",
    state: "entry",
    url: chessReview,
    relatedPa1UseCase: "C-UC4",
    actions: waitForText("Analysis")
  },
  {
    captureId: "chess-29-analysis-board",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "default",
    url: chessAnalysis,
    relatedPa1UseCase: "C-UC4"
  },
  {
    captureId: "chess-30-evaluation-bar",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "evaluation bar",
    url: chessAnalysis,
    actions: waitForText("Evaluation")
  },
  {
    captureId: "chess-31-move-list",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "move list",
    url: chessAnalysis,
    actions: waitForText("Moves")
  },
  {
    captureId: "chess-32-engine-lines",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "engine lines",
    url: chessAnalysis,
    actions: waitForText("Lines")
  },
  {
    captureId: "chess-33-analysis-chart",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "chart",
    url: chessAnalysis,
    actions: waitForText("Analysis")
  },
  {
    captureId: "chess-34-analysis-toolbar",
    product: "chess",
    viewport: "desktop",
    pageArea: "Analysis Board",
    state: "toolbar",
    url: chessAnalysis,
    actions: waitForText("Analysis")
  },
  {
    captureId: "chess-35-premium-limit-natural",
    product: "chess",
    viewport: "desktop",
    pageArea: "access prompt",
    state: "premium limit naturally appeared",
    url: chessLessons,
    actions: waitForText("Premium")
  },
  {
    captureId: "chess-36-entitlement-message-natural",
    product: "chess",
    viewport: "desktop",
    pageArea: "access prompt",
    state: "entitlement message naturally appeared",
    url: chessLessons,
    actions: waitForText("Upgrade")
  },
  {
    captureId: "chess-37-premove-setting",
    product: "chess",
    viewport: "desktop",
    pageArea: "board settings",
    state: "premove setting",
    url: chessBot,
    actions: waitForText("Premove")
  },
  {
    captureId: "chess-38-board-queued-premove",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "queued premove",
    url: chessBot,
    actions: waitForText("Premove")
  },
  {
    captureId: "chess-39-premove-clear-state",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "premove cleared",
    url: chessBot,
    actions: waitForText("Premove")
  },
  {
    captureId: "chess-40-focus-mode-control",
    product: "chess",
    viewport: "desktop",
    pageArea: "board controls",
    state: "Focus Mode control",
    url: chessBot,
    actions: waitForText("Focus")
  },
  {
    captureId: "chess-41-focus-mode-hover",
    product: "chess",
    viewport: "desktop",
    pageArea: "board controls",
    state: "Focus Mode hover",
    url: chessBot,
    actions: [{ type: "hover", selector: "[aria-label*='Focus' i], [title*='Focus' i]" }]
  },
  {
    captureId: "chess-42-focus-mode-tooltip",
    product: "chess",
    viewport: "desktop",
    pageArea: "board controls",
    state: "Focus Mode tooltip",
    url: chessBot,
    actions: [
      { type: "hover", selector: "[aria-label*='Focus' i], [title*='Focus' i]" },
      { type: "waitForText", text: "Focus Mode" }
    ]
  },
  {
    captureId: "chess-43-focus-mode-enabled",
    product: "chess",
    viewport: "desktop",
    pageArea: "board",
    state: "Focus Mode enabled",
    url: chessBot,
    actions: clickButton("Focus Mode")
  },
  {
    captureId: "chess-44-focus-mode-settings-shortcut",
    product: "chess",
    viewport: "desktop",
    pageArea: "board settings",
    state: "Focus Mode shortcut",
    url: chessBot,
    actions: waitForText("Focus Mode")
  },
  {
    captureId: "chess-45-returning-user-home",
    product: "chess",
    viewport: "desktop",
    pageArea: "homepage",
    state: "returning user if session exists",
    url: chessHome,
    requiresAuth: true
  },
  {
    captureId: "chess-46-recent-task-shortcuts",
    product: "chess",
    viewport: "desktop",
    pageArea: "homepage",
    state: "recent-task shortcuts if session exists",
    url: chessHome,
    requiresAuth: true
  },
  {
    captureId: "chess-47-play-mobile",
    product: "chess",
    viewport: "mobile",
    pageArea: "Play",
    state: "mobile",
    url: chessPlay,
    relatedPa1UseCase: "C-UC1"
  },
  {
    captureId: "chess-48-puzzle-mobile",
    product: "chess",
    viewport: "mobile",
    pageArea: "Puzzle",
    state: "mobile",
    url: chessPuzzles,
    relatedPa1UseCase: "C-UC2"
  },
  {
    captureId: "chess-49-lessons-mobile",
    product: "chess",
    viewport: "mobile",
    pageArea: "Lessons",
    state: "mobile",
    url: chessLessons,
    relatedPa1UseCase: "C-UC3"
  },
  {
    captureId: "chess-50-active-game-mobile",
    product: "chess",
    viewport: "mobile",
    pageArea: "board",
    state: "active game mobile",
    url: chessBot,
    relatedPa1Figure: "C-07"
  },
  {
    captureId: "chess-51-account-prompt-natural",
    product: "chess",
    viewport: "desktop",
    pageArea: "account prompt",
    state: "naturally appeared",
    url: chessPlay,
    actions: waitForText("Sign Up")
  },
  {
    captureId: "chess-52-cookie-banner-natural",
    product: "chess",
    viewport: "desktop",
    pageArea: "cookie banner",
    state: "naturally appeared",
    url: chessHome,
    captureBeforePopupDismiss: true
  },
  {
    captureId: "chess-53-ad-panel-natural",
    product: "chess",
    viewport: "desktop",
    pageArea: "ad panel",
    state: "naturally appeared",
    url: chessHome,
    actions: waitForText("Advertisement")
  }
];

export const allCaptureTargets = [...fifaTargets, ...chessTargets];

export function targetsFor(
  product: "fifa" | "chess",
  viewport: "desktop" | "mobile"
): CaptureTarget[] {
  return allCaptureTargets.filter(
    (target) => target.product === product && target.viewport === viewport
  );
}
