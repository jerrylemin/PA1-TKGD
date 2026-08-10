import fs from "node:fs/promises";
import { Workbook } from "@oai/artifact-tool";

const ROOT = String.raw`C:\Users\Administrator\Documents\MEGA\tkgd\PA2`;
// Report-facing evidence paths are deliberately relative to the PA2 root.
const CAP = "capture-work";
const TMP = `${ROOT}\\tmp\\evidence-previews`;

const headers = [
  "figure_id",
  "product",
  "local_path",
  "visible_page_or_state",
  "supported_claims",
  "unsupported_claims",
  "related_persona",
  "related_task",
  "related_drawback",
  "report_usage",
  "caption",
];

const rows = [
  ["F2-E01","FIFA",`${CAP}\\fifa\\desktop\\fifa-01-homepage-desktop.png`,"Full homepage with global header, tournament circles, stacked sections, footer, and a promotional modal over first-view content.","Promotional interruption; broad hierarchy; task-entry competition.","Clean default homepage; cookie banner; distinct navigation-open state.","F-P1; F-P2","FR-T1; FR-T2","F-D1; F-D5","UserResearch; UserAnalysis","FIFA.com homepage showing a promotional modal over the first-view content and a long hierarchy of tournament, match, story, ranking, and ecosystem sections."],
  ["F2-E02","FIFA",`${CAP}\\fifa\\mobile\\fifa-04-homepage-mobile.png`,"Long mobile homepage with compact header, stacked content, ranking content, and footer.","Mobile density; long vertical scanning; compact navigation.","Open mobile menu.","F-P1","FR-T1; FR-T2","F-D1; F-D5","Mobile FIFA.com homepage showing compact navigation and a long vertically stacked information surface."],
  ["F2-E03","FIFA",`${CAP}\\fifa\\desktop\\fifa-06-match-centre.png`,"Match Centre with gender control, date rail, search, live toggle, date, sort and filter controls, match rows, tables, and latest results.","Date-based mental model; visible match status; multiple narrowing controls; long scanning surface.","A measured completion time or participant difficulty.","F-P1; F-P2","FR-T1","F-D5","Match Centre showing date-based navigation, filtering controls, grouped match rows, standings, and latest results."],
  ["F2-E04","FIFA",`${CAP}\\fifa\\desktop\\fifa-10-match-centre-filters.png`,"Match Centre dimmed behind an open A-to-Z Competitions filter drawer.","Filter structure; added scan and selection work; panel-to-results relationship.","A selected competition result.","F-P1; F-P2","FR-T1","F-D5","Match Centre with the A-to-Z Competitions filter drawer open over the results surface."],
  ["F2-E05","FIFA",`${CAP}\\fifa\\desktop\\fifa-11-search-page.png`,"Search results for world cup with content-type and date filters, mixed article cards, sorting, and pagination.","Mixed-content search; comparison among result types; filtering and pagination.","User success rate or search relevance quality.","F-P3","FR-T2","F-D5","FIFA search page showing a world cup query, result filters, mixed article cards, sorting, and pagination."],
  ["F2-E06","FIFA",`${CAP}\\fifa\\desktop\\fifa-13-news-article-full.png`,"Ticketing media-release page with header, hero, article content, a large sparse body interval, related content, and footer.","Article structure; utility action is not persistently visible; captured body includes a long sparse interval.","Universal production loading defect; full body-content assessment.","F-P2; F-P3","FR-T2; FR-T3","F-D5","Ticketing media-release page showing its article structure and a long sparse interval before later content and related links."],
  ["F2-E07","FIFA",`${CAP}\\fifa\\desktop\\fifa-16-tournament-landing.png`,"Tournament landing page covered by a registration-interest modal.","Modal interruption; obscured browsing context.","Dismissed modal.","F-P2","FR-T2","F-D5","Tournament landing page showing a registration-interest modal obscuring the underlying page."],
  ["F2-E08","FIFA",`${CAP}\\fifa\\desktop\\fifa-19-rankings.png`,"Men's World Ranking page with ranking cards, table, explanation, media, related articles, and footer.","Dedicated official ranking content; separation of reading and utility navigation.","Participant comprehension or ranking accuracy.","F-P2; F-P3","FR-T2","F-D5","FIFA men's ranking page showing ranking status, table, explanatory content, media, and related articles."],
  ["F2-E09","FIFA",`${CAP}\\fifa\\desktop\\fifa-20-tickets-hospitality-landing.png`,"Tickets and Hospitality landing page with tournament logos, ticket and hospitality cards, mixed register-interest and buy-now labels, other tournaments, news, and footer.","Tournament-based ticket entry; card destinations; no consolidated cross-tournament status dashboard.","Seat map; waiting room; resale dashboard; verified partner redirect.","F-P3","FR-T3","F-D4","Tickets and Hospitality landing page showing tournament-based entry cards; the captured state has no consolidated sale phase, seat availability, resale, waiting-room, or last-updated dashboard."],
  ["F2-E10","FIFA",`${CAP}\\fifa\\desktop\\fifa-34-fifa-plus-entry.png`,"FIFA-branded page with assistant-referee flag image and an error or unavailable-state message.","Captured entry route does not expose watch content; possible continuity loss in this state.","Every FIFA+ session fails.","F-P3","FR-T4","F-D2","FIFA-branded entry route showing an assistant-referee flag and a message that normal watch content is unavailable in the captured state."],
  ["F2-E11","FIFA",`${CAP}\\fifa\\desktop\\fifa-35-fifa-plus-dazn-landing.png`,"Dark DAZN-hosted FIFA+ page with FIFA+ hero, sign-in controls, navigation, event cards, and media rails.","Brand and account boundary; different IA; dense watch rails; need for handoff feedforward.","A tested trust failure or universal confusion.","F-P3","FR-T4","F-D2; F-D3","DAZN-hosted FIFA+ landing page showing a distinct brand, account controls, task navigation, and multiple media rails."],
  ["F2-E12","FIFA",`${CAP}\\fifa\\desktop\\fifa-36-fifa-plus-cookie-before-dismiss.png`,"DAZN-hosted FIFA+ landing page darkened by a cookie-preferences panel.","Consent handling adds a step before content access.","A distinct rail state.","F-P3","FR-T4","F-D2; F-D3","FIFA+ landing page shown in a consent-obstructed state before cookie preference handling."],
  ["F2-E13","FIFA",`${CAP}\\fifa\\desktop\\fifa-37-fifa-plus-after-cookie-dismiss.png`,"Unobstructed upper portion of the FIFA+ landing page with hero, category controls, and event cards.","Normal landing layout; hero, categories, and media entry.","Seven distinct rail states.","F-P3","FR-T4","F-D2; F-D3","Unobstructed FIFA+ landing page showing the hero, task categories, and event-card entry surface."],
  ["F2-E14","FIFA",`${CAP}\\fifa\\desktop\\fifa-46-store-page.png`,"Bright retail page with store-specific header, merchandising hero, product grids, category tiles, and retail footer.","Cross-property visual and task-model change; retail navigation differs from information navigation.","Ticket availability or FIFA.com navigation continuity.","F-P1; F-P3","FR-T4","F-D1","FIFA Store page showing a retail-specific header, merchandising hierarchy, product grids, and footer."],
  ["F2-E15","FIFA",`${CAP}\\fifa\\desktop\\fifa-47-collect-page.png`,"Dark FIFA Collect marketplace with subscription prompt, collectibles, clubs, prices, filters, and marketplace language.","Cross-property mental-model change; separate transaction vocabulary and structure.","Conventional merchandise shopping flow.","F-P3","FR-T4","F-D1","FIFA Collect page showing subscription, digital-collectible, club, marketplace, price, and challenge structures."],
  ["F2-E16","FIFA",`${CAP}\\fifa\\desktop\\fifa-48-rewards-page.png`,"Black FIFA Rewards page with Join Now, tier cards, FAQs, and FIFA footer.","Distinct sibling-property identity; account-oriented reward task.","A completed sign-up or reward redemption.","F-P3","FR-T4","F-D1","FIFA Rewards page showing account entry, tier cards, FAQs, and a distinct black-and-gold visual identity."],
  ["F2-E17","FIFA",`${CAP}\\fifa\\mobile\\fifa-49-match-centre-mobile.png`,"Mobile Match Centre with compact header, gender control, match groups, latest results, load-more control, and long footer.","Mobile fixture checking; long vertical task surface.","Open filter menu or measured scroll effort.","F-P1","FR-T1","F-D5","Mobile Match Centre showing grouped matches, latest results, and a long vertical continuation."],
  ["F2-E18","FIFA",`${CAP}\\fifa\\mobile\\fifa-51-tickets-mobile.png`,"Mobile Tickets and Hospitality page with stacked cards, horizontal carousels, news, and footer.","Narrow-screen ticket discovery; card-based selection and long continuation.","Unified status dashboard; waiting room; partner redirect.","F-P3","FR-T3","F-D4","Mobile Tickets and Hospitality page showing stacked ticket cards, tournament carousels, ticket news, and long vertical continuation."],
  ["F2-E19","FIFA",`${CAP}\\fifa\\mobile\\fifa-50-article-mobile.png`,"Mobile ticketing article with header, hero, body content separated by a long sparse interval, related topics, and footer.","Little persistent task continuation; long mobile reading surface.","Full article comprehension or universal loading defect.","F-P2; F-P3","FR-T2; FR-T3","F-D5","UserResearch appendix; UserAnalysis secondary","Mobile ticketing article showing a long reading surface with a sparse interval and no persistent task-utility control in the captured state."],
  ["F2-E20","FIFA",`${CAP}\\fifa\\mobile\\fifa-52-fifa-plus-entry-mobile.png`,"Mobile FIFA+ entry route with assistant-referee flag and error or unavailable-state message.","Mobile entry failure in the captured state.","Normal FIFA+ mobile landing page.","F-P3","FR-T4","F-D2","Mobile FIFA+ entry route showing an assistant-referee flag and an unavailable-state message."],
  ["C2-E01","Chess.com",`${CAP}\\chess\\desktop\\chess-01-homepage-desktop.png`,"Long homepage with persistent left navigation, Play hero, Lessons, Bots, Puzzles, Watch, app promotion, and footer.","Feature-rich entry; recognition of categories; many first-level routes; long scan.","A user preference for the whitespace.","C-P1; C-P3","CR-T1; CR-T2; CR-T3","C-D1","Chess.com homepage showing persistent navigation and repeated task-entry sections across a long page."],
  ["C2-E02","Chess.com",`${CAP}\\chess\\desktop\\chess-05-play-entry.png`,"Play entry with board, clocks, time control, Start Game, Custom Challenge, Play a Friend, Tournaments, navigation, and advertisement.","Direct board mental model; fast-play options; competing controls and advertising.","Active game in progress.","C-P1; C-P2; C-P3","CR-T1","C-D1","Chess.com Play entry showing a board, clocks, time control, game-start options, navigation, and advertising."],
  ["C2-E03","Chess.com",`${CAP}\\chess\\desktop\\chess-07-custom-game-settings.png`,"Skill-level modal over the Play page with Sign Up, Log In, and Play as a Guest.","Account/onboarding interruption; skill-level setup decision.","A completed custom-game configuration.","C-P1","CR-T1","C-D1","Play entry showing a skill-level onboarding modal with account and guest continuation choices."],
  ["C2-E04","Chess.com",`${CAP}\\chess\\desktop\\chess-10-bot-game.png`,"Bot-selection page with board preview, bot categories and levels, options, Play button, navigation, and advertisement.","Many choices before bot play; category and difficulty structure.","Active game; move feedback; premove; Focus Mode.","C-P1; C-P3","CR-T1","C-D1","Chess.com bot-selection page showing category lists, bot choices, board preview, options, and Play control."],
  ["C2-E05","Chess.com",`${CAP}\\chess\\desktop\\chess-19-puzzle-landing.png`,"Puzzle board with move context, progression map, Solve Puzzles control, navigation, and advertisement.","Direct manipulation; board/progression split; ad attention competition.","Correct or incorrect result state.","C-P1; C-P3","CR-T2","C-D1","Chess.com puzzle entry showing a board, progression path, Solve Puzzles control, navigation, and advertising."],
  ["C2-E06","Chess.com",`${CAP}\\chess\\desktop\\chess-20-puzzle-before-move.png`,"Puzzle board with highlighted move context and progression map.","Move affordance and immediate action state.","Correct or incorrect result.","C-P1","CR-T2","C-D1","Puzzle entry showing a candidate action state beside the progression path before a verified result."],
  ["C2-E07","Chess.com",`${CAP}\\chess\\desktop\\chess-24-lessons-landing-loaded.png`,"Lessons page with category tabs, upgrade messaging, learning rank, ads, app promotion, long course list, pagination, and footer.","Multiple learning categories; paid messaging and ads near learning content; long course list.","A specific lesson completed or premium entitlement interruption.","C-P1; C-P3","CR-T3","C-D1","Lessons landing page showing categories, upgrade messaging, ads, a long course list, and pagination."],
  ["C2-E08","Chess.com",`${CAP}\\chess\\desktop\\chess-26-learn-page.png`,"Learn-to-Play board with progressive lesson path, prompt, and Next Lesson control.","Progressive guided-learning pattern; clear next action.","Measured learning improvement.","C-P1","CR-T3","C-D1","Learn-to-Play page showing a board, progressive lesson path, explanatory prompt, and clear Next Lesson action."],
  ["C2-E09","Chess.com",`${CAP}\\chess\\desktop\\chess-27-study-plan.png`,"Long article titled Chess Study Plans for All Levels with navigation, article content, comments, and related content.","Study guidance exists as content rather than a unified personalized dashboard.","A verified personalized learning path.","C-P1; C-P3","CR-T3","C-D1","Chess Study Plans article showing level-based guidance, related content, and a long comments section."],
  ["C2-E10","Chess.com",`${CAP}\\chess\\desktop\\chess-29-analysis-board.png`,"Analysis entry board with Set Up Position, Explore, Game Search, Game Collections, import/upload options, and Start Analysis.","Advanced entry exposes several paths and controls.","Completed review; engine lines; chart; classifications; beginner explanation.","C-P1; C-P3","CR-T4","C-D2","Chess.com Analysis entry showing multiple setup and import paths beside a board and Start Analysis control."],
  ["C2-E11","Chess.com",`${CAP}\\chess\\desktop\\chess-53-ad-panel-natural.png`,"Homepage-like content; no unambiguous high-salience advertisement is visible in the inspected pixels.","Homepage task hierarchy only.","Advertising competition unless an ad is visibly identifiable.","C-P1","CR-T1; CR-T3","C-D1","Restricted evidence: this inspected capture does not provide unambiguous proof of an advertising panel."],
  ["C2-E12","Chess.com",`${CAP}\\chess\\mobile\\chess-03-homepage-mobile.png`,"Mobile homepage with hamburger icon, Sign Up and Log In, stacked Play, Lessons, Bots, Puzzles, Watch, app content, and footer.","Mobile content stacking and long vertical scanning.","Open mobile menu.","C-P1; C-P3","CR-T1; CR-T2; CR-T3","C-D1","Mobile Chess.com homepage showing compact account controls and a long stack of task-entry sections."],
  ["C2-E13","Chess.com",`${CAP}\\chess\\mobile\\chess-47-play-mobile.png`,"Mobile Play entry with board, clocks, bottom task navigation, time control, Start Game, and alternative play options.","Mobile play entry and vertical continuation.","Active game.","C-P1; C-P2; C-P3","CR-T1","C-D1","Mobile Play entry showing a compact board, clocks, game-start controls, and alternative play routes."],
  ["C2-E14","Chess.com",`${CAP}\\chess\\mobile\\chess-48-puzzle-mobile.png`,"Mobile puzzle progression map with coach prompt and Solve Puzzles control.","Mobile puzzle entry and progression.","Puzzle result or board interaction.","C-P1","CR-T2","C-D1","Mobile puzzle entry showing a progression map, prompt, and Solve Puzzles control."],
  ["C2-E15","Chess.com",`${CAP}\\chess\\mobile\\chess-49-lessons-mobile.png`,"Very long mobile Lessons page with categories, course cards, promotion, ranking, and footer.","Extended vertical scanning on mobile learning content.","A completed lesson or measured difficulty.","C-P1; C-P3","CR-T3","C-D1","Mobile Lessons page showing categories, many course cards, promotional content, and extensive vertical continuation."],
  ["C2-E16","Chess.com",`${CAP}\\chess\\mobile\\chess-50-active-game-mobile.png`,"Mobile bot-selection/setup page with bot identity, board preview, categories, options, and Play.","Mobile bot selection and setup.","Active game.","C-P1; C-P3","CR-T1","C-D1","Mobile bot-selection page showing a board preview, bot categories, options, and Play control."],
];

const normalizedRows = rows.map((row) => {
  if (row.length === 10) {
    return [...row.slice(0, 9), "UserResearch evidence appendix; traceability source", row[9]];
  }
  if (row.length !== headers.length) {
    throw new Error(`Evidence row ${row[0] ?? "<unknown>"} has ${row.length} fields; expected ${headers.length}.`);
  }
  return row;
});

function csvCell(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function toCsv(columns, data) {
  return [columns, ...data].map((row) => row.map(csvCell).join(",")).join("\r\n") + "\r\n";
}

const traceHeaders = [
  "research_question","persona","task","screenshot_evidence","pa1_finding",
  "affinity_cluster","tough_problem","concept_alternative","use_case","report_section"
];
const traceRows = [
  ["RQ-F1: How is a quick fixture/result check performed?","F-P1; F-P2","FR-T1","F2-E03; F2-E04; F2-E17","F-D5","FIFA-A1; FIFA-A2; FIFA-A5","Secondary","F-A1","F-UC01","UserResearch §6; UserAnalysis §4"],
  ["RQ-F2: How is official World Cup information found?","F-P2; F-P3","FR-T2","F2-E05; F2-E06; F2-E07; F2-E08","F-D5","FIFA-A1; FIFA-A2","Secondary","F-A1","F-UC01","UserResearch §6; UserAnalysis §4"],
  ["RQ-F3: What status is visible before ticket action?","F-P3","FR-T3","F2-E09; F2-E18","F-D4","FIFA-A3","TP-FIFA","F-A1","F-UC01; F-UC02; F-UC03; F-UC04","UserResearch §6/§10; UserAnalysis §6/§9; ProjectProposal §2/§4; UseCaseDocument §4-§5"],
  ["RQ-F4: What happens at a partner/property boundary?","F-P3","FR-T4","F2-E10; F2-E11; F2-E12; F2-E13","F-D2; F-D3","FIFA-A4","TP-FIFA","F-A2","F-UC05; F-UC06","UserResearch §6/§10; UserAnalysis §6/§9; ProjectProposal §2/§4; UseCaseDocument §4-§5"],
  ["RQ-F5: How can future action replace repeated checking?","F-P3","FR-T3","F2-E09; F2-E18","F-D4","FIFA-A3","TP-FIFA","F-A3","F-UC04; F-UC06","ProjectProposal §4/§6; UseCaseDocument §5/§8"],
  ["RQ-C1: What choices precede game or bot play?","C-P1; C-P2; C-P3","CR-T1","C2-E02; C2-E03; C2-E04; C2-E13; C2-E16","C-D1","CHESS-A1; CHESS-A2","Secondary","C-A1","C-UC01","UserResearch §6; UserAnalysis §4"],
  ["RQ-C2: How is puzzle action signposted?","C-P1","CR-T2","C2-E05; C2-E06; C2-E14","C-D1","CHESS-A3","Secondary","C-A1","C-UC04; C-UC06","UserResearch §6; UseCaseDocument §7"],
  ["RQ-C3: How is a beginner learning path continued?","C-P1; C-P3","CR-T3","C2-E07; C2-E08; C2-E09; C2-E12; C2-E15","C-D1","CHESS-A4; CHESS-A6","TP-CHESS","C-A1; C-A2","C-UC02; C-UC06","UserResearch §6/§10; UserAnalysis §6/§9; ProjectProposal §2/§5; UseCaseDocument §6-§7"],
  ["RQ-C4: What is the next action at analysis entry?","C-P1; C-P3","CR-T4","C2-E10","C-D2","CHESS-A5","TP-CHESS","C-A1","C-UC01; C-UC02; C-UC03; C-UC04; C-UC05","UserResearch §6/§10; UserAnalysis §6/§9; ProjectProposal §2/§5; UseCaseDocument §6-§7"],
  ["RQ-C5: Can review be organized as a comprehensible narrative?","C-P1; C-P3","CR-T4","C2-E08; C2-E10","C-D2","CHESS-A5","TP-CHESS","C-A3","C-UC03; C-UC04; C-UC06","ProjectProposal §5/§6; UseCaseDocument §7/§8"],
];

await fs.mkdir(TMP, { recursive: true });
await fs.writeFile(`${ROOT}\\evidence-index.csv`, "\uFEFF" + toCsv(headers, normalizedRows), "utf8");
await fs.writeFile(`${ROOT}\\traceability-matrix.csv`, "\uFEFF" + toCsv(traceHeaders, traceRows), "utf8");

for (const [name, csv] of [
  ["evidence-index", toCsv(headers, normalizedRows)],
  ["traceability-matrix", toCsv(traceHeaders, traceRows)],
]) {
  const workbook = await Workbook.fromCSV(csv, { sheetName: name });
  const sheet = workbook.worksheets.getItem(name);
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  const used = sheet.getUsedRange();
  used.format.wrapText = true;
  used.format.font = { name: "Arial", size: 9, color: "#1F2937" };
  used.format.autofitColumns();
  used.format.autofitRows();
  sheet.getRangeByIndexes(0, 0, 1, used.columnCount).format = {
    fill: "#123B65",
    font: { name: "Arial", size: 9, bold: true, color: "#FFFFFF" },
    wrapText: true,
  };
  const preview = await workbook.render({
    sheetName: name,
    range: name === "evidence-index" ? "A1:K12" : "A1:J11",
    scale: 1,
    format: "png",
  });
  await fs.writeFile(`${TMP}\\${name}.png`, new Uint8Array(await preview.arrayBuffer()));
  const inspected = await workbook.inspect({
    kind: "table",
    sheetId: name,
    range: name === "evidence-index" ? "A1:K37" : "A1:J11",
    include: "values",
    tableMaxRows: 40,
    tableMaxCols: 12,
    maxChars: 2000,
  });
  await fs.writeFile(`${TMP}\\${name}-inspect.ndjson`, inspected.ndjson, "utf8");
}

console.log(JSON.stringify({ evidence_rows: normalizedRows.length, traceability_rows: traceRows.length }, null, 2));
