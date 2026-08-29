import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { chromium } from "../../PA2/capture-work/automation/node_modules/playwright/index.mjs";

const baseUrl = "http://127.0.0.1:4173/index.html";
const screenshotDir = path.resolve("PA4/evidence/prototype-screenshots");
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

async function fifaCalendarState(page) {
  return page.locator('[data-action="fifa-calendar"]').evaluate((button) => ({
    disabled: button.disabled,
    ariaDisabled: button.getAttribute("aria-disabled"),
    title: button.querySelector("#calendarActionTitle")?.textContent.trim() || "",
    copy: button.querySelector("#calendarActionCopy")?.textContent.trim() || "",
  }));
}

async function click(page, selector) {
  const locator = page.locator(selector).first();
  await locator.waitFor({ state: "visible" });
  await locator.click();
}

async function assertNoHorizontalOverflow(page, label) {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
  check(`${label} has no horizontal overflow`, !overflow, overflow ? "document scrollWidth exceeds viewport" : "");
}

async function countVisibleButtonsWithoutRoutes(page, label) {
  const missing = await page.evaluate(() => [...document.querySelectorAll("button")]
    .filter((button) => {
      const style = getComputedStyle(button);
      return style.display !== "none" && style.visibility !== "hidden" && !button.closest("[hidden]")
        && !button.dataset.action && !button.dataset.route;
    })
    .map((button) => button.textContent.trim()));
  check(`${label} visible buttons have routed actions`, missing.length === 0, missing.join(" | "));
}

async function assertLockedChessBoard(page, label) {
  const boardState = await page.evaluate(() => ({
    buttons: document.querySelectorAll('[data-action="chess-square"]').length,
    semanticSquares: document.querySelectorAll('.chess-board [role="img"]').length,
    queen: document.querySelector('.chess-board [data-coord="d1"]')?.getAttribute("aria-label") || "",
  }));
  check(`${label} board is locked`, boardState.buttons === 0 && boardState.semanticSquares === 64, JSON.stringify(boardState));
  check(`${label} shows the white queen in the source position`, boardState.queen === "d1 white piece", boardState.queen);
}

async function assertStudyChromeHidden(page, label, productText) {
  const text = await visibleText(page);
  const domCounts = await page.evaluate(() => ({
    shell: document.querySelectorAll(".lab-header, .home-view").length,
    researcher: document.querySelectorAll(".study-researcher-chrome").length,
    reset: document.querySelectorAll('[data-action="fifa-reset"]').length,
    unavailable: document.querySelectorAll('[data-action="fifa-preview-error"]').length,
    focusableRemoved: [...document.querySelectorAll("button, a, [tabindex]")].filter((node) => node.textContent.includes("Reset demo state") || node.textContent.includes("Preview unavailable state")).length,
  }));
  check(`${label} study route is active`, await page.locator("body").evaluate((body) => body.classList.contains("study-mode")));
  check(`${label} product view is visible`, await page.locator(`#${productText}View`).isVisible());
  check(`${label} presenter shell is removed`, domCounts.shell === 0, JSON.stringify(domCounts));
  check(`${label} researcher chrome is removed from the DOM`, domCounts.researcher === 0 && domCounts.reset === 0 && domCounts.unavailable === 0 && domCounts.focusableRemoved === 0, JSON.stringify(domCounts));
  check(`${label} participant text excludes researcher labels`, !/PA4|HI-FI LAB|Offline demo data|DEMO DATA|DEMO GAME|Exit demo|Local demo analysis|Preview Full Analysis|Reset demo state|Preview unavailable state|review glossary/i.test(text), text);
}

async function assertRedesignStructure(page, label) {
  const structure = await page.evaluate(() => ({
    fifa: {
      eventMasterList: document.querySelectorAll(".event-master-list").length,
      selectedWorkspace: document.querySelectorAll(".selected-event-workspace").length,
      statusHero: document.querySelectorAll(".status-hero").length,
      progressTimeline: document.querySelectorAll(".fifa-progress-section").length,
      actionDock: document.querySelectorAll(".action-dock").length,
      oldStatGrid: document.querySelectorAll(".fifa-stat-grid").length,
      oldRail: document.querySelectorAll(".fifa-rail").length,
    },
    chess: {
      sideNav: document.querySelectorAll(".product-side-nav").length,
      boardWorkspace: document.querySelectorAll(".chess-board-workspace").length,
      reviewPanel: document.querySelectorAll(".review-panel").length,
      oldRail: document.querySelectorAll(".chess-rail").length,
    },
  }));
  check(`${label} FIFA master-detail structure is present`, Object.values(structure.fifa).slice(0, 5).every((count) => count === 1), JSON.stringify(structure.fifa));
  check(`${label} old FIFA structures are absent`, structure.fifa.oldStatGrid === 0 && structure.fifa.oldRail === 0, JSON.stringify(structure.fifa));
  check(`${label} Chess analysis structure is present`, structure.chess.sideNav === 1 && structure.chess.boardWorkspace === 1 && structure.chess.reviewPanel === 1, JSON.stringify(structure.chess));
  check(`${label} old Chess rail is absent`, structure.chess.oldRail === 0, JSON.stringify(structure.chess));
}

try {
  const presenter = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  presenter.on("console", (message) => { if (message.type() === "error") errors.push(`presenter console: ${message.text()}`); });
  presenter.on("pageerror", (error) => errors.push(`presenter pageerror: ${error.message}`));
  await presenter.goto(`${baseUrl}?mode=presenter#home`);
  await presenter.waitForLoadState("networkidle");
  check("Presenter mode loads overview", await presenter.locator("body").evaluate((body) => body.classList.contains("presenter-mode")) && await presenter.locator("#homeView").isVisible());
  check("Presenter shell is visible", await presenter.locator(".lab-header").isVisible() && await presenter.locator(".home-view").isVisible());
  await countVisibleButtonsWithoutRoutes(presenter, "Presenter overview");
  await screenshot(presenter, "home-desktop-redesign.png");
  await presenter.close();

  const fifa = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  fifa.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA console: ${message.text()}`); });
  fifa.on("pageerror", (error) => errors.push(`FIFA pageerror: ${error.message}`));
  await fifa.goto(`${baseUrl}?mode=presenter#fifa`);
  await fifa.waitForLoadState("networkidle");
  check("F01 FIFA overview loads", await fifa.locator("#fifaStatusHeading").isVisible());
  check("F02 FIFA status is visible", (await fifa.locator("#fifaStatusHeading").textContent())?.trim() === "Pending" && (await fifa.locator("#fifaActionCopy").textContent())?.includes("No action needed"));
  check("F11 FIFA identity is consistent", (await visibleText(fifa)).includes("FIFA.com") && (await visibleText(fifa)).includes("Tickets") && !(await visibleText(fifa)).includes("FIFA+"));
  let calendarState = await fifaCalendarState(fifa);
  check("CAL01 Initial Pending", (await fifa.locator('[data-action="fifa-select-event"][data-event="pending"]').getAttribute("aria-pressed")) === "true" && (await fifa.locator("#fifaStatusHeading").textContent())?.trim() === "Pending" && calendarState.disabled && calendarState.ariaDisabled === "true" && calendarState.title === "Add to Calendar" && calendarState.copy === "Available after confirmation", JSON.stringify(calendarState));
  await click(fifa, '[data-action="fifa-select-event"][data-event="confirmed"]');
  calendarState = await fifaCalendarState(fifa);
  check("CAL02 Confirmed", (await fifa.locator("#fifaStatusHeading").textContent())?.trim() === "Confirmed" && !calendarState.disabled && calendarState.ariaDisabled === "false" && calendarState.title === "Add to Calendar" && calendarState.copy === "Save this confirmed event", JSON.stringify(calendarState));
  await click(fifa, '[data-action="fifa-calendar"]');
  calendarState = await fifaCalendarState(fifa);
  const calendarToast = fifa.locator(".toast").filter({ hasText: "Calendar event saved" }).last();
  const calendarToastDetail = await calendarToast.locator("div > span").textContent().catch(() => "");
  check("CAL03 Valid save", !calendarState.disabled && calendarState.title === "Calendar saved" && calendarState.copy === "Toronto event saved" && await calendarToast.count() === 1 && (await calendarToast.locator("strong").textContent())?.trim() === "Calendar event saved" && calendarToastDetail?.trim() === "Toronto \u00b7 21 Jun 2026 is ready for your calendar.", JSON.stringify({ calendarState, toastDetail: calendarToastDetail }));
  await click(fifa, '[data-action="fifa-select-event"][data-event="pending"]');
  calendarState = await fifaCalendarState(fifa);
  check("CAL04 Switch back to Pending", (await fifa.locator("#fifaStatusHeading").textContent())?.trim() === "Pending" && calendarState.disabled && calendarState.ariaDisabled === "true" && calendarState.title === "Add to Calendar" && calendarState.copy === "Available after confirmation", JSON.stringify(calendarState));
  await fifa.locator(".toast").evaluateAll((toasts) => toasts.forEach((toast) => toast.remove()));
  await fifa.locator('[data-action="fifa-calendar"]').evaluate((button) => button.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, view: window })));
  calendarState = await fifaCalendarState(fifa);
  check("CAL06 Defensive handler", calendarState.disabled && calendarState.title === "Add to Calendar" && calendarState.copy === "Available after confirmation" && await fifa.locator(".toast").filter({ hasText: "Calendar event saved" }).count() === 0, JSON.stringify(calendarState));
  await click(fifa, '[data-action="fifa-select-event"][data-event="confirmed"]');
  calendarState = await fifaCalendarState(fifa);
  check("CAL05 Persistence", !calendarState.disabled && calendarState.title === "Calendar saved" && calendarState.copy === "Toronto event saved", JSON.stringify(calendarState));
  await click(fifa, '[data-action="fifa-select-event"][data-event="pending"]');
  await assertRedesignStructure(fifa, "FIFA desktop");
  await screenshot(fifa, "fifa-desktop-overview.png");
  await screenshot(fifa, "fifa-desktop-redesign.png");
  await assertNoHorizontalOverflow(fifa, "FIFA desktop overview");
  await countVisibleButtonsWithoutRoutes(fifa, "FIFA overview");
  check("Presenter reset and unavailable preview remain available", await fifa.locator('[data-action="fifa-reset"]').count() === 1 && await fifa.locator('[data-action="fifa-preview-error"]').count() === 1);

  await click(fifa, '[data-action="fifa-view-order"]');
  check("F03 View Order opens detail", await fifa.locator("#modalTitle").textContent() === "Order FIFA-26-88421");
  await screenshot(fifa, "fifa-desktop-order-detail.png");
  await screenshot(fifa, "fifa-order-drawer.png");
  await fifa.keyboard.press("Escape");
  check("F04 Escape closes modal", await fifa.locator("#modalRoot").isHidden());
  await click(fifa, '[data-action="fifa-view-tickets"]');
  check("F04 Ticket detail opens", await fifa.locator(".ticket-detail-card").isVisible() && (await visibleText(fifa)).includes("Ticket not issued yet"));
  await screenshot(fifa, "fifa-desktop-ticket-detail.png");
  await click(fifa, '.modal-card [data-action="fifa-return-overview"]');
  await click(fifa, '[data-action="fifa-open-handoff"]');
  check("F05 handoff warning opens", await fifa.locator(".partner-destination").isVisible() && (await fifa.locator(".modal-warning").textContent())?.includes("leave FIFA.com"));
  await screenshot(fifa, "fifa-desktop-handoff.png");
  await screenshot(fifa, "fifa-handoff-redesign.png");
  await click(fifa, '[data-action="fifa-stay"]');
  check("F06 Stay keeps FIFA context", await fifa.locator("#modalRoot").isHidden() && await fifa.locator("#fifaView").isVisible());
  await click(fifa, '[data-action="fifa-open-handoff"]');
  await click(fifa, '[data-action="fifa-continue-handoff"]');
  check("F07 Continue enters partner boundary state", (await fifa.locator("#modalTitle").textContent())?.includes("Partner boundary"));
  await screenshot(fifa, "fifa-desktop-partner.png");
  await click(fifa, '[data-action="fifa-return"]');
  check("F08 Return preserves FIFA orientation", await fifa.locator("#fifaReturnNotice").isVisible() && await fifa.locator("#fifaStatusHeading").isVisible());
  await click(fifa, '[data-action="fifa-select-event"][data-event="confirmed"]');
  await click(fifa, "button.refresh-control");
  await fifa.waitForTimeout(800);
  check("FIFA refresh resolves", (await fifa.locator("#fifaLastUpdated").textContent())?.trim() === "just now");
  await click(fifa, '[data-action="fifa-preview-error"]');
  check("FIFA recoverable error is visible", await fifa.locator("#fifaAlert").isVisible());
  await click(fifa, '#fifaAlert button[data-action="fifa-refresh"]');
  await fifa.waitForTimeout(800);
  check("FIFA error retry clears state", !(await fifa.locator("#fifaAlert").isVisible()));

  const fifaStudy = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  fifaStudy.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA study console: ${message.text()}`); });
  await fifaStudy.goto(`${baseUrl}?mode=study&product=fifa#fifa`);
  await fifaStudy.waitForLoadState("networkidle");
  await assertStudyChromeHidden(fifaStudy, "F10 FIFA", "fifa");
  check("F10 FIFA study starts directly in product flow", (await visibleText(fifaStudy)).includes("Your FIFA tickets"));
  await screenshot(fifaStudy, "fifa-study-overview.png");
  await fifaStudy.close();

  const fifaMobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  fifaMobile.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA mobile console: ${message.text()}`); });
  await fifaMobile.goto(`${baseUrl}?mode=presenter#fifa`);
  await fifaMobile.waitForLoadState("networkidle");
  await assertNoHorizontalOverflow(fifaMobile, "F09 FIFA mobile overview");
  await screenshot(fifaMobile, "fifa-mobile-overview.png");
  await screenshot(fifaMobile, "fifa-mobile-redesign.png");
  await click(fifaMobile, '[data-action="fifa-open-handoff"]');
  await assertNoHorizontalOverflow(fifaMobile, "F09 FIFA mobile handoff");
  await screenshot(fifaMobile, "fifa-mobile-handoff.png");
  await fifaMobile.close();

  for (const viewport of [{ width: 1024, height: 768 }, { width: 768, height: 1024 }]) {
    const fifaResponsive = await browser.newPage({ viewport });
    fifaResponsive.on("console", (message) => { if (message.type() === "error") errors.push(`FIFA ${viewport.width} console: ${message.text()}`); });
    await fifaResponsive.goto(`${baseUrl}?mode=presenter#fifa`);
    await fifaResponsive.waitForLoadState("networkidle");
    await assertNoHorizontalOverflow(fifaResponsive, `FIFA ${viewport.width} responsive`);
    check(`FIFA ${viewport.width} primary status visible`, await fifaResponsive.locator("#fifaStatusHeading").isVisible());
    await fifaResponsive.close();

    const chessResponsive = await browser.newPage({ viewport });
    chessResponsive.on("console", (message) => { if (message.type() === "error") errors.push(`Chess ${viewport.width} console: ${message.text()}`); });
    await chessResponsive.goto(`${baseUrl}?mode=presenter#chess`);
    await chessResponsive.waitForLoadState("networkidle");
    await assertNoHorizontalOverflow(chessResponsive, `Chess ${viewport.width} responsive`);
    check(`Chess ${viewport.width} board visible`, await chessResponsive.locator(".chess-board").isVisible());
    await chessResponsive.close();
  }

  const chess = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  chess.on("console", (message) => { if (message.type() === "error") errors.push(`Chess console: ${message.text()}`); });
  chess.on("pageerror", (error) => errors.push(`Chess pageerror: ${error.message}`));
  await chess.goto(`${baseUrl}?mode=presenter#chess`);
  await chess.waitForLoadState("networkidle");
  await assertRedesignStructure(chess, "Chess desktop");
  let chessText = await visibleText(chess);
  check("C01 Chess intro loads", chessText.includes("Start with the most important learning moment"));
  check("C02 Chess intro hides answer", !/Qh5|Nxh5|Qe2|h5/.test(chessText));
  await assertLockedChessBoard(chess, "C02 Chess intro");
  check("C03 intro does not expose a move highlight", await chess.locator(".board-square.is-highlight, .board-square.is-better").count() === 0);
  await screenshot(chess, "chess-desktop-review-intro.png");
  await screenshot(chess, "chess-intro-redesign.png");

  await click(chess, '[data-action="chess-start-review"]');
  chessText = await visibleText(chess);
  check("C04 mistake state reveals move and consequence", chessText.includes("Qh5") && chessText.includes("Nxh5") && !chessText.includes("Qe2"));
  await assertLockedChessBoard(chess, "C04 Chess mistake");
  await screenshot(chess, "chess-desktop-mistake.png");
  await screenshot(chess, "chess-mistake-redesign.png");
  await click(chess, '[data-action="chess-reveal-better"]');
  chessText = await visibleText(chess);
  check("C05 better move is revealed at the right stage", chessText.includes("Qe2") && chessText.includes("safe destination"));
  await assertLockedChessBoard(chess, "C05 Chess better move");
  await screenshot(chess, "chess-desktop-better-move.png");

  await click(chess, '[data-action="chess-try-move"]');
  check("C06 trial requires a real board", await chess.locator('[data-action="chess-square"]').count() === 64 && await chess.locator('[data-action="chess-try-correct"]').count() === 0 && await chess.locator('[data-action="chess-try-wrong"]').count() === 0);
  chessText = await visibleText(chess);
  check("C07 trial hides exact destination before input", !chessText.includes("Qe2") && !chessText.includes("e2"));
  await screenshot(chess, "chess-desktop-trial.png");
  await screenshot(chess, "chess-trial-redesign.png");

  await click(chess, '[data-square="e2"]');
  chessText = await visibleText(chess);
  check("C08 destination-only click does not solve", chessText.includes("Start with the queen") && !chessText.includes("That move keeps the queen safe"));
  check("C09 destination-only click does not select a source", await chess.locator(".board-square.is-source-selected").count() === 0);
  await click(chess, '[data-action="chess-retry"]');
  await click(chess, '[data-square="d1"]');
  check("C10 source selection is visibly indicated", await chess.locator('.board-square[data-square="d1"].is-source-selected').count() === 1);
  await click(chess, '[data-square="e3"]');
  check("C11 wrong destination gives informative feedback", (await visibleText(chess)).includes("does not solve the problem"));
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="e2"]');
  chessText = await visibleText(chess);
  check("C12 correct source-to-destination move advances", chessText.includes("That move keeps the queen safe") && await chess.locator('.board-square[data-square="e2"] .piece').count() === 1 && await chess.locator('.board-square[data-square="d1"] .piece').count() === 0);
  await click(chess, '[data-action="chess-practice"]');
  check("C13 practice is interactive", await chess.locator('[data-action="chess-square"]').count() === 64 && await chess.locator('[data-action="chess-complete-practice"]').count() === 0 && !(await visibleText(chess)).includes("Qd3"));
  await click(chess, '[data-square="d3"]');
  check("C14 practice destination-only click does not solve", (await visibleText(chess)).includes("Select the queen first"));
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="e3"]');
  check("C15 practice wrong move supports retry", (await visibleText(chess)).includes("still unsafe"));
  await click(chess, '[data-square="d1"]');
  await click(chess, '[data-square="d3"]');
  check("C16 practice correct move enables completion", (await visibleText(chess)).includes("Good safety check") && await chess.locator('[data-action="chess-complete-practice"]').count() === 1);
  await chess.waitForTimeout(3600);
  await screenshot(chess, "chess-desktop-practice.png");
  await screenshot(chess, "chess-practice-redesign.png");
  await click(chess, '[data-action="chess-complete-practice"]');
  await click(chess, '[data-action="chess-complete-review"]');
  check("C17 completion state works", (await visibleText(chess)).includes("One mistake, one useful idea"));
  await screenshot(chess, "chess-desktop-completion.png");
  await countVisibleButtonsWithoutRoutes(chess, "Chess completion");
  await assertNoHorizontalOverflow(chess, "C18 Chess desktop");

  const chessStudy = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  chessStudy.on("console", (message) => { if (message.type() === "error") errors.push(`Chess study console: ${message.text()}`); });
  await chessStudy.goto(`${baseUrl}?mode=study&product=chess#chess`);
  await chessStudy.waitForLoadState("networkidle");
  await assertStudyChromeHidden(chessStudy, "C19 Chess", "chess");
  chessText = await visibleText(chessStudy);
  check("C20 Chess study intro hides answer", !/Qh5|Nxh5|Qe2|h5/.test(chessText));
  await assertLockedChessBoard(chessStudy, "C20 Chess study intro");
  await screenshot(chessStudy, "chess-study-intro.png");
  await chessStudy.close();

  const chessMobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  chessMobile.on("console", (message) => { if (message.type() === "error") errors.push(`Chess mobile console: ${message.text()}`); });
  await chessMobile.goto(`${baseUrl}?mode=presenter#chess`);
  await chessMobile.waitForLoadState("networkidle");
  await click(chessMobile, '[data-action="chess-start-review"]');
  await assertNoHorizontalOverflow(chessMobile, "C21 Chess mobile review");
  await screenshot(chessMobile, "chess-mobile-review.png");
  await screenshot(chessMobile, "chess-mobile-redesign.png");
  await click(chessMobile, '[data-action="chess-reveal-better"]');
  await click(chessMobile, '[data-action="chess-practice"]');
  await assertNoHorizontalOverflow(chessMobile, "C21 Chess mobile practice");
  await screenshot(chessMobile, "chess-mobile-practice.png");
  await chessMobile.close();
  await chess.close();
  await fifa.close();

  check("No browser console errors", errors.length === 0, errors.join(" | "));
} catch (error) {
  checks.push({ name: "QA execution", passed: false, detail: error.message });
} finally {
  await browser.close();
}

const result = { generated_at: new Date().toISOString(), checks, errors, status: checks.every((item) => item.passed) && errors.length === 0 ? "PASS" : "FAIL" };
await writeFile(path.join(qaDir, "prototype-browser-qa.json"), `${JSON.stringify(result, null, 2)}\n`, "utf8");
console.log(JSON.stringify(result, null, 2));
if (result.status !== "PASS") process.exitCode = 1;
