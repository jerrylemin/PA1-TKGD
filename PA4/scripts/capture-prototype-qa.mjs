import { existsSync } from "node:fs";
import { mkdir, writeFile } from "node:fs/promises";
import { homedir, tmpdir } from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const playwrightCandidates = [
  path.resolve("PA2/capture-work/automation/node_modules/playwright/index.mjs"),
  path.join(homedir(), ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs"),
];
const playwrightPath = playwrightCandidates.find((candidate) => existsSync(candidate));
if (!playwrightPath) throw new Error("Playwright runtime not found in the project or bundled Codex runtime.");
const { chromium } = await import(pathToFileURL(playwrightPath).href);

const baseUrl = "http://127.0.0.1:4173/index.html";
const screenshotDir = process.env.PA4_QA_SCREENSHOT_DIR
  ? path.resolve(process.env.PA4_QA_SCREENSHOT_DIR)
  : path.resolve("PA4/evidence/prototype-screenshots");
const qaDir = path.resolve("PA4/qa");

await mkdir(screenshotDir, { recursive: true });
await mkdir(qaDir, { recursive: true });

const errors = [];
const checks = [];
const browser = await chromium.launch({ headless: true });

function check(name, passed, detail = "") {
  checks.push({ name, passed, detail });
  if (!passed) throw new Error(`${name}: ${detail}`);
}

async function screenshot(page, name) {
  await page.screenshot({ path: path.join(screenshotDir, name), fullPage: true });
}

async function visibleText(page) {
  return page.locator("body").innerText();
}

async function click(page, selector) {
  const locator = page.locator(selector).first();
  await locator.waitFor({ state: "visible" });
  await locator.click();
}

async function assertNoHorizontalOverflow(page, label) {
  const dimensions = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  }));
  check(`${label} has no horizontal overflow`, dimensions.scrollWidth <= dimensions.clientWidth + 1, JSON.stringify(dimensions));
}

async function assertCardsDoNotOverlap(page, selector, label) {
  const overlap = await page.locator(selector).evaluateAll((nodes) => {
    const boxes = nodes
      .filter((node) => !node.hidden && getComputedStyle(node).display !== "none")
      .map((node, index) => ({ index, rect: node.getBoundingClientRect().toJSON() }));
    for (let left = 0; left < boxes.length; left += 1) {
      for (let right = left + 1; right < boxes.length; right += 1) {
        const a = boxes[left].rect;
        const b = boxes[right].rect;
        const overlapWidth = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const overlapHeight = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (overlapWidth > 1 && overlapHeight > 1) return { left: boxes[left].index, right: boxes[right].index, overlapWidth, overlapHeight };
      }
    }
    return null;
  });
  check(`${label} cards do not overlap`, overlap === null, JSON.stringify(overlap));
}

async function assertDialogFitsViewport(page, label) {
  const geometry = await page.locator(".modal-card").evaluate((dialog) => {
    const rect = dialog.getBoundingClientRect();
    const root = dialog.closest(".modal-root");
    return {
      left: rect.left,
      right: rect.right,
      width: rect.width,
      viewportWidth: window.innerWidth,
      rootScrollable: Boolean(root && root.scrollHeight >= root.clientHeight),
      closeVisible: Boolean(dialog.querySelector(".modal-close")?.getClientRects().length),
    };
  });
  check(`${label} fits the viewport and remains dismissible`, geometry.left >= -1 && geometry.right <= geometry.viewportWidth + 1 && geometry.width <= geometry.viewportWidth + 1 && geometry.rootScrollable && geometry.closeVisible, JSON.stringify(geometry));
}

async function assertVisibleButtonRouting(page, label) {
  const missing = await page.evaluate(() => [...document.querySelectorAll("button")]
    .filter((button) => {
      const style = getComputedStyle(button);
      return style.display !== "none" && style.visibility !== "hidden" && !button.closest("[hidden]")
        && !button.dataset.action && !button.dataset.route;
    })
    .map((button) => button.textContent.trim()));
  check(`${label} visible buttons have routed actions`, missing.length === 0, missing.join(" | "));
}

async function assertStudyChromeHidden(page, label, product) {
  const text = await visibleText(page);
  const dom = await page.evaluate(() => ({
    shell: document.querySelectorAll(".lab-header, .home-view").length,
    researcher: document.querySelectorAll(".study-researcher-chrome").length,
    internalIds: [...document.querySelectorAll("[data-moment]")].some((node) => node.textContent.includes(node.dataset.moment)),
  }));
  check(`${label} study route is active`, await page.locator("body").evaluate((body) => body.classList.contains("study-mode")));
  check(`${label} product view is visible`, await page.locator(`#${product}View`).isVisible());
  check(`${label} presenter and researcher chrome are removed`, dom.shell === 0 && dom.researcher === 0, JSON.stringify(dom));
  check(`${label} participant surface excludes lab labels and internal IDs`, !/PA4|FINAL HI-FI|DEMO DATA|DEMO GAME|Exit demo|Local demo analysis|Preview unavailable state|Reset demo state|review glossary/i.test(text) && !dom.internalIds, text);
}

async function fifaCalendarState(page, event) {
  return page.locator(`[data-action="fifa-calendar"][data-event="${event}"]`).evaluate((button) => ({
    disabled: button.disabled,
    ariaDisabled: button.getAttribute("aria-disabled"),
    title: button.querySelector("strong")?.textContent.trim() || "",
    copy: button.querySelector("small")?.textContent.trim() || "",
  }));
}

async function assertLockedChessBoard(page, label) {
  const board = await page.evaluate(() => ({
    buttons: document.querySelectorAll('[data-action="chess-square"]').length,
    semanticSquares: document.querySelectorAll('.chess-board [role="img"]').length,
    queen: document.querySelector('.chess-board [data-coord="d1"]')?.getAttribute("aria-label") || "",
  }));
  check(`${label} board is locked`, board.buttons === 0 && board.semanticSquares === 64, JSON.stringify(board));
  check(`${label} board retains the white queen source`, board.queen === "d1 white piece", board.queen);
}

async function assertInitialFifaConcept(page, label) {
  const structure = await page.evaluate(() => ({
    summary: document.querySelectorAll(".fifa-status-summary").length,
    summaryCards: document.querySelectorAll(".status-summary-card").length,
    events: [...document.querySelectorAll("[data-fifa-event-card]")].filter((card) => !card.hidden).map((card) => card.dataset.event),
    quickActions: document.querySelectorAll(".quick-action-row").length,
    sourceCues: document.querySelectorAll(".support-cue").length,
    dominantTimeline: document.querySelectorAll(".fifa-progress-section, .fifa-timeline, .selected-event-workspace, .event-master-list").length,
  }));
  check(`${label} FIFA-A1-01 dashboard opens with state summary`, structure.summary === 1 && structure.summaryCards === 4, JSON.stringify(structure));
  check(`${label} FIFA-A1-02 Mexico and Toronto are simultaneously visible`, structure.events.length === 2 && structure.events.includes("pending") && structure.events.includes("confirmed"), JSON.stringify(structure.events));
  check(`${label} FIFA-A1-05 quick actions are visible`, structure.quickActions >= 3, JSON.stringify(structure));
  check(`${label} FIFA-A1-06 source and freshness are visible`, structure.sourceCues >= 2 && (await visibleText(page)).includes("Official FIFA source") && (await visibleText(page)).includes("Last checked"), JSON.stringify(structure));
  check(`${label} FIFA-A1-07 lifecycle timeline is not the dashboard structure`, structure.dominantTimeline === 0, JSON.stringify(structure));
}

async function assertInitialChessConcept(page, label) {
  const state = await page.evaluate(() => ({
    chips: [...document.querySelectorAll(".review-summary-chip")].map((chip) => chip.textContent.trim()),
    cards: document.querySelectorAll(".moment-card").length,
    selected: document.querySelectorAll('.moment-card[aria-pressed="true"], .moment-card.is-selected').length,
    miniBoards: document.querySelectorAll(".mini-board").length,
    miniSquares: document.querySelectorAll(".mini-board .mini-square").length,
    progressRails: document.querySelectorAll(".review-panel-progress, .review-panel-step").length,
  }));
  const text = await visibleText(page);
  check(`${label} CHESS-A2-01 initial summary chips match card data`, state.chips.length === 4 && state.chips.some((value) => value.includes("4") && value.includes("Key moments")) && state.chips.some((value) => value.includes("2") && value.includes("Mistakes")) && state.chips.some((value) => value.includes("1") && value.includes("Good moves")) && state.chips.some((value) => value.includes("1") && value.includes("Practice available")), JSON.stringify(state.chips));
  check(`${label} CHESS-A2-02 multiple key-moment cards are visible`, state.cards === 4, JSON.stringify(state));
  check(`${label} CHESS-A2-03 cards include recognizable mini-board previews`, state.miniBoards === 4 && state.miniSquares === 256, JSON.stringify(state));
  check(`${label} CHESS-A2-04 no first card is forced`, state.selected === 0 && text.includes("Nothing is selected yet"), JSON.stringify(state));
  check(`${label} CHESS-A2-14 no global wizard rail is present`, state.progressRails === 0 && !/STEP\s+1\s+OF|Start Beginner Review|Beginner Review Flow/i.test(text), text);
  check(`${label} answer leakage gate hides Qe2 and Qd3`, !/Qe2|Qd3/.test(text), text);
}

async function assertResponsiveProduct(product, viewport) {
  const page = await browser.newPage({ viewport });
  page.on("console", (message) => { if (message.type() === "error") errors.push(`${product} ${viewport.width} console: ${message.text()}`); });
  page.on("pageerror", (error) => errors.push(`${product} ${viewport.width} pageerror: ${error.message}`));
  await page.goto(`${baseUrl}?mode=presenter#${product}`);
  await page.waitForLoadState("networkidle");
  await assertNoHorizontalOverflow(page, `${product} ${viewport.width}x${viewport.height}`);
  if (product === "fifa") {
    check(`FIFA ${viewport.width} summary remains visible`, await page.locator(".fifa-summary-grid").isVisible());
    check(`FIFA ${viewport.width} event cards remain available`, await page.locator("[data-fifa-event-card]").count() === 2);
    check(`FIFA ${viewport.width} quick actions remain usable`, await page.locator(".quick-action-row").count() >= 3);
    await assertCardsDoNotOverlap(page, ".status-summary-card", `FIFA ${viewport.width} summary`);
    await assertCardsDoNotOverlap(page, "[data-fifa-event-card], .fifa-actions-panel, .fifa-support-panel", `FIFA ${viewport.width} content`);
    await click(page, '[data-action="fifa-view-tickets"][data-event="pending"]');
    await assertDialogFitsViewport(page, `FIFA ${viewport.width} event drawer`);
    await page.keyboard.press("Escape");
    await click(page, '[data-action="fifa-open-handoff"]');
    await assertDialogFitsViewport(page, `FIFA ${viewport.width} handoff dialog`);
    if (viewport.width === 390) await screenshot(page, "fifa-390x844-handoff-selection-correction.png");
    await click(page, '[data-action="fifa-stay"]');
  } else {
    check(`Chess ${viewport.width} summary chips remain visible`, await page.locator(".review-summary-grid").isVisible());
    check(`Chess ${viewport.width} card grid remains available`, await page.locator(".moment-card").count() === 4);
    const previewBox = await page.locator(".mini-board").first().boundingBox();
    check(`Chess ${viewport.width} mini-board remains recognizable`, Boolean(previewBox && previewBox.width >= 70 && previewBox.height >= 70), JSON.stringify(previewBox));
    await assertCardsDoNotOverlap(page, ".review-summary-chip", `Chess ${viewport.width} summary`);
    await assertCardsDoNotOverlap(page, ".moment-card", `Chess ${viewport.width} moment`);
    if (viewport.width === 390) await screenshot(page, "chess-390x844-card-dashboard-selection-correction.png");
    await click(page, '[data-action="chess-select-card"][data-moment="queen-safety"]');
    check(`Chess ${viewport.width} selected detail and return are usable`, await page.locator(".moment-detail").isVisible() && await page.locator('[data-action="chess-back-dashboard"]').first().isVisible());
    await assertCardsDoNotOverlap(page, ".moment-detail, .board-panel", `Chess ${viewport.width} selected workspace`);
    await assertNoHorizontalOverflow(page, `Chess ${viewport.width} selected detail`);
  }
  if (viewport.width === 1440 || viewport.width === 390) await screenshot(page, `${product}-${viewport.width}x${viewport.height}-selection-correction.png`);
  await page.close();
}

try {
  const presenter = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  presenter.on("console", (message) => { if (message.type() === "error") errors.push(`presenter console: ${message.text()}`); });
  presenter.on("pageerror", (error) => errors.push(`presenter pageerror: ${error.message}`));
  await presenter.goto(`${baseUrl}?mode=presenter#home`);
  await presenter.waitForLoadState("networkidle");
  const presenterText = await visibleText(presenter);
  check("Presenter mode loads overview", await presenter.locator("#homeView").isVisible());
  check("Presenter identifies FIFA Alt 1 Status Dashboard", presenterText.includes("SELECTED \u00b7 PA3 ALT 1") && presenterText.includes("Status Dashboard"));
  check("Presenter identifies Chess Alt 2 Card Review Mode", presenterText.includes("SELECTED \u00b7 PA3 ALT 2") && presenterText.includes("Card Review Mode"));
  await assertVisibleButtonRouting(presenter, "Presenter overview");
  await screenshot(presenter, "home-selection-correction.png");
  await presenter.close();

  const fifa = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  fifa.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA console: ${message.text()}`); });
  fifa.on("pageerror", (error) => errors.push(`FIFA pageerror: ${error.message}`));
  await fifa.goto(`${baseUrl}?mode=presenter#fifa`);
  await fifa.waitForLoadState("networkidle");
  await assertInitialFifaConcept(fifa, "FIFA desktop");
  const fifaText = await visibleText(fifa);
  check("FIFA-A1-03 Pending and Confirmed are distinguishable", fifaText.includes("Pending") && fifaText.includes("Confirmed") && await fifa.locator(".ticket-event-pending").isVisible() && await fifa.locator(".ticket-event-confirmed").isVisible());
  check("FIFA-A1-04 status meaning, owner, and safe next action are on cards", fifaText.includes("No immediate action is required") && fifaText.includes("OWNER") && fifaText.includes("FIFA") && fifaText.includes("You own the next action"));
  await assertVisibleButtonRouting(fifa, "FIFA dashboard");

  let pendingCalendar = await fifaCalendarState(fifa, "pending");
  let confirmedCalendar = await fifaCalendarState(fifa, "confirmed");
  check("CAL01 Initial Pending", pendingCalendar.disabled && pendingCalendar.ariaDisabled === "true" && pendingCalendar.title === "Add to calendar" && pendingCalendar.copy === "Available after confirmation", JSON.stringify(pendingCalendar));
  check("CAL02 Confirmed", !confirmedCalendar.disabled && confirmedCalendar.ariaDisabled === "false" && confirmedCalendar.title === "Add to calendar" && confirmedCalendar.copy === "Save confirmed event", JSON.stringify(confirmedCalendar));
  await click(fifa, '[data-action="fifa-calendar"][data-event="confirmed"]');
  confirmedCalendar = await fifaCalendarState(fifa, "confirmed");
  const calendarToast = fifa.locator(".toast").filter({ hasText: "Calendar event saved" }).last();
  check("CAL03 Valid save", confirmedCalendar.title === "Calendar saved" && confirmedCalendar.copy === "Toronto event saved" && await calendarToast.count() === 1, JSON.stringify(confirmedCalendar));
  pendingCalendar = await fifaCalendarState(fifa, "pending");
  check("CAL04 Pending remains unavailable", pendingCalendar.disabled && pendingCalendar.title === "Add to calendar" && pendingCalendar.copy === "Available after confirmation", JSON.stringify(pendingCalendar));
  await fifa.locator(".toast").evaluateAll((toasts) => toasts.forEach((toast) => toast.remove()));
  await fifa.locator('[data-action="fifa-calendar"][data-event="pending"]').evaluate((button) => button.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, view: window })));
  pendingCalendar = await fifaCalendarState(fifa, "pending");
  check("CAL06 Defensive Pending handler", pendingCalendar.disabled && await fifa.locator(".toast").filter({ hasText: "Calendar event saved" }).count() === 0, JSON.stringify(pendingCalendar));
  confirmedCalendar = await fifaCalendarState(fifa, "confirmed");
  check("CAL05 Confirmed save persists", confirmedCalendar.title === "Calendar saved" && confirmedCalendar.copy === "Toronto event saved", JSON.stringify(confirmedCalendar));

  await click(fifa, '[data-action="fifa-view-tickets"][data-event="pending"]');
  check("FIFA-A1-08 event details open secondarily", await fifa.locator(".ticket-detail-card").isVisible() && (await visibleText(fifa)).includes("Ticket not issued yet"));
  await fifa.keyboard.press("Escape");
  await click(fifa, '[data-action="fifa-open-handoff"]');
  check("FIFA-A1-09 handoff destination preview opens", await fifa.locator(".partner-destination").isVisible() && (await visibleText(fifa)).includes("Cancel") && (await visibleText(fifa)).includes("Continue to partner"));
  await click(fifa, '[data-action="fifa-stay"]');
  check("FIFA-A1-09 cancel keeps FIFA context", await fifa.locator("#modalRoot").isHidden() && await fifa.locator("#fifaView").isVisible());
  await click(fifa, '[data-action="fifa-open-handoff"]');
  await click(fifa, '[data-action="fifa-continue-handoff"]');
  check("FIFA-A1-09 continue makes no completion claim", (await visibleText(fifa)).includes("PARTNER RESULT") && (await visibleText(fifa)).includes("Not claimed by FIFA"));
  await click(fifa, '[data-action="fifa-return"]');
  check("FIFA-A1-09 safe return restores account dashboard", await fifa.locator("#fifaReturnNotice").isVisible() && await fifa.locator(".fifa-status-summary").isVisible());
  check("FIFA-A1-10 CAL01-CAL06 all passed", checks.filter((item) => item.name.startsWith("CAL")).length === 6 && checks.filter((item) => item.name.startsWith("CAL")).every((item) => item.passed));

  await click(fifa, '[data-action="fifa-filter"][data-filter="pending"]');
  check("FIFA summary filters without requiring event selection", await fifa.locator('[data-fifa-event-card][data-event="pending"]').isVisible() && await fifa.locator('[data-fifa-event-card][data-event="confirmed"]').isHidden());
  await click(fifa, '[data-action="fifa-filter"][data-filter="all"]');
  await click(fifa, ".refresh-control");
  await fifa.waitForTimeout(800);
  check("FIFA refresh updates account freshness", (await fifa.locator("#fifaLastUpdated").textContent())?.trim() === "just now" && (await fifa.locator("#fifaFootFreshness").textContent())?.includes("just now"));
  await click(fifa, '[data-action="fifa-preview-error"]');
  check("FIFA unavailable state is recoverable", await fifa.locator("#fifaAlert").isVisible());
  await click(fifa, '#fifaAlert [data-action="fifa-refresh"]');
  await fifa.waitForTimeout(800);
  check("FIFA retry clears unavailable state", await fifa.locator("#fifaAlert").isHidden());
  await fifa.close();

  const chess = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  chess.on("console", (message) => { if (message.type() === "error") errors.push(`Chess console: ${message.text()}`); });
  chess.on("pageerror", (error) => errors.push(`Chess pageerror: ${error.message}`));
  await chess.goto(`${baseUrl}?mode=presenter#chess`);
  await chess.waitForLoadState("networkidle");
  await assertInitialChessConcept(chess, "Chess desktop");
  await assertLockedChessBoard(chess, "Chess dashboard");
  await assertVisibleButtonRouting(chess, "Chess dashboard");

  await click(chess, '[data-action="chess-select-card"][data-moment="development"]');
  check("CHESS-A2-05 user can independently choose Development", (await chess.locator(".moment-detail h2").textContent())?.trim() === "Development with tempo");
  check("CHESS-A2-06 selected card opens an explanation", (await visibleText(chess)).includes("WHAT HAPPENED") && (await visibleText(chess)).includes("WHY IT MATTERS"));
  check("CHESS-A2-08 return to all key moments is visible", await chess.locator('[data-action="chess-back-dashboard"]').first().isVisible());
  await click(chess, '[data-action="chess-back-dashboard"]');
  await click(chess, '[data-action="chess-select-card"][data-moment="queen-safety"]');
  let chessText = await visibleText(chess);
  check("CHESS-A2-05 user can choose Queen safety independently", (await chess.locator(".moment-detail h2").textContent())?.trim() === "Queen safety");
  check("CHESS-A2-07 selected card exposes Review, Try, and Puzzle actions", chessText.includes("Review safer move") && chessText.includes("Try this move") && chessText.includes("Go to puzzle / practice"));
  check("CHESS-A2-09 Qh5 card preserves Qh5 to Nxh5 explanation", chessText.includes("Qh5") && chessText.includes("Nxh5") && chessText.includes("capture the queen"));
  check("Chess selected-detail leakage gate hides Qe2 until reveal", !chessText.includes("Qe2"));
  await click(chess, '[data-action="chess-reveal-solution"]');
  check("Chess local Review reveals Qe2 at the requested point", (await visibleText(chess)).includes("Qe2"));
  await click(chess, '[data-action="chess-back-dashboard"]');
  check("CHESS-A2-15 another card remains selectable after review", await chess.locator('[data-action="chess-select-card"][data-moment="opening-idea"]').isVisible());
  await click(chess, '[data-action="chess-select-card"][data-moment="opening-idea"]');
  check("CHESS-A2-05 card order is not fixed", (await chess.locator(".moment-detail h2").textContent())?.trim() === "Opening idea");
  await click(chess, '[data-action="chess-back-dashboard"]');
  await click(chess, '[data-action="chess-select-card"][data-moment="queen-safety"]');
  await click(chess, '[data-action="chess-try-move"]');
  chessText = await visibleText(chess);
  check("CHESS-A2-10 Qe2 trial preserves source-to-destination input", await chess.locator('[data-action="chess-square"]').count() === 64 && !chessText.includes("Qe2") && !chessText.includes("e2"));
  await click(chess, '[data-square="e2"]');
  check("CHESS-A2-10 destination-only input does not solve", (await visibleText(chess)).includes("Select the queen first"));
  await click(chess, '[data-square="d1"]');
  check("CHESS-A2-10 source selection is visible", await chess.locator('[data-square="d1"].is-source-selected').count() === 1);
  await click(chess, '[data-square="e3"]');
  check("CHESS-A2-11 wrong trial supports retry", (await visibleText(chess)).includes("does not solve the problem") && await chess.locator('[data-action="chess-retry"]').isVisible());
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="e2"]');
  chessText = await visibleText(chess);
  check("CHESS-A2-10 correct Qe2 trial updates the board", chessText.includes("Qe2") && await chess.locator('[data-coord="e2"] .piece').count() === 1 && await chess.locator('[data-coord="d1"] .piece').count() === 0);
  check("CHESS-A2-13 practice remains optional after trial", chessText.includes("Return to selected card") && chessText.includes("Back to all key moments") && chessText.includes("Open related practice"));
  await click(chess, '[data-action="chess-back-dashboard"]');
  check("CHESS-A2-15 dashboard remains available after trial", await chess.locator(".moment-grid").isVisible() && await chess.locator(".moment-card").count() === 4);
  await click(chess, '[data-action="chess-select-card"][data-moment="queen-safety"]');
  await click(chess, '[data-action="chess-practice"]');
  chessText = await visibleText(chess);
  check("CHESS-A2-12 Qd3 practice opens without leaking its answer", await chess.locator('[data-action="chess-square"]').count() === 64 && !chessText.includes("Qd3"));
  await click(chess, '[data-square="d3"]');
  check("CHESS-A2-12 practice destination-only input does not solve", (await visibleText(chess)).includes("Select the queen first"));
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="e3"]');
  check("CHESS-A2-12 practice wrong move supports retry", (await visibleText(chess)).includes("still unsafe"));
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="d3"]');
  check("CHESS-A2-12 correct Qd3 enables completion", (await visibleText(chess)).includes("Qd3") && await chess.locator('[data-action="chess-complete-practice"]').isVisible());
  await click(chess, '[data-action="chess-complete-practice"]');
  check("CHESS-A2-13 completed practice offers card and dashboard returns", (await visibleText(chess)).includes("Practice complete") && await chess.locator('[data-action="chess-back-card"]').count() >= 1 && await chess.locator('[data-action="chess-back-dashboard"]').isVisible());
  await click(chess, '[data-action="chess-back-dashboard"]');
  check("CHESS-A2-15 another card can be selected after practice", await chess.locator('[data-action="chess-select-card"][data-moment="king-safety"]').isVisible());
  await assertNoHorizontalOverflow(chess, "Chess desktop completed path");
  await chess.close();

  const fifaStudy = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  fifaStudy.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA study console: ${message.text()}`); });
  fifaStudy.on("pageerror", (error) => errors.push(`FIFA study pageerror: ${error.message}`));
  await fifaStudy.goto(`${baseUrl}?mode=study&product=fifa#fifa`);
  await fifaStudy.waitForLoadState("networkidle");
  await assertStudyChromeHidden(fifaStudy, "FIFA study", "fifa");
  await assertInitialFifaConcept(fifaStudy, "FIFA study");
  await screenshot(fifaStudy, "fifa-study-status-dashboard.png");
  await fifaStudy.close();

  const chessStudy = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  chessStudy.on("console", (message) => { if (message.type() === "error") errors.push(`Chess study console: ${message.text()}`); });
  chessStudy.on("pageerror", (error) => errors.push(`Chess study pageerror: ${error.message}`));
  await chessStudy.goto(`${baseUrl}?mode=study&product=chess#chess`);
  await chessStudy.waitForLoadState("networkidle");
  await assertStudyChromeHidden(chessStudy, "Chess study", "chess");
  await assertInitialChessConcept(chessStudy, "Chess study");
  check("Chess study has no researcher hint or forced selection", await chessStudy.locator('.moment-card[aria-pressed="true"]').count() === 0 && !(await visibleText(chessStudy)).includes("recommended"));
  await screenshot(chessStudy, "chess-study-card-dashboard.png");
  await chessStudy.close();

  for (const viewport of [
    { width: 1440, height: 900 },
    { width: 1024, height: 768 },
    { width: 768, height: 1024 },
    { width: 390, height: 844 },
  ]) {
    await assertResponsiveProduct("fifa", viewport);
    await assertResponsiveProduct("chess", viewport);
  }

  check("No browser console errors", errors.length === 0, errors.join(" | "));
} catch (error) {
  checks.push({ name: "QA execution", passed: false, detail: error.message });
} finally {
  await browser.close();
}

const result = {
  generated_at: new Date().toISOString(),
  screenshot_dir: screenshotDir.startsWith(tmpdir()) ? "temporary" : screenshotDir,
  checks,
  errors,
  status: checks.every((item) => item.passed) && errors.length === 0 ? "PASS" : "FAIL",
};
await writeFile(path.join(qaDir, "prototype-browser-qa.json"), `${JSON.stringify(result, null, 2)}\n`, "utf8");
console.log(JSON.stringify(result, null, 2));
if (result.status !== "PASS") process.exitCode = 1;
