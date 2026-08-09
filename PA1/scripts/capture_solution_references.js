const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const output = path.join(root, "assets", "screenshots", "solution-references");
const targets = [
  { file: "fifa_footer_clean.png", url: "https://www.fifa.com/en", action: "footer" },
  { file: "fifa_plus_boundary_clean.png", url: "https://www.plus.fifa.com/" },
  { file: "fifa_tickets_clean.png", url: "https://www.fifa.com/en/tickets" },
  { file: "fifa_article_clean.png", url: "https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september", action: "article" },
  { file: "chess_navigation_ui.png", url: "https://www.chess.com/" },
  { file: "chess_analysis_ui.png", url: "https://www.chess.com/analysis" },
  { file: "chess_lessons_ui.png", url: "https://www.chess.com/lessons" },
  { file: "chess_puzzles_ui.png", url: "https://www.chess.com/puzzles" },
  { file: "chess_board_ui.png", url: "https://www.chess.com/play/computer" },
];

async function clickIfVisible(locator) {
  if (await locator.isVisible({ timeout: 500 }).catch(() => false)) {
    await locator.click({ force: true, timeout: 2000 }).catch(() => {});
    await locator.page().waitForTimeout(500);
    return true;
  }
  return false;
}

async function clearObstructions(page) {
  for (let pass = 0; pass < 4; pass += 1) {
    const cookieLabels = [
      /i'?m ok with that/i,
      /accept all/i,
      /accept cookies/i,
      /allow all/i,
      /^accept$/i,
      /got it/i,
      /continue without accepting/i,
    ];
    for (const label of cookieLabels) {
      if (await clickIfVisible(page.getByRole("button", { name: label }).first())) break;
    }

    const closeLocators = [
      page.locator("button[aria-label*='close' i]").first(),
      page.locator("[role='dialog'] button").filter({ hasText: /^(x|×|close)$/i }).first(),
      page.locator("button").filter({ hasText: /^(x|×)$/ }).first(),
      page.locator("[data-testid*='close' i], [class*='modal'] [class*='close' i], [class*='popup'] [class*='close' i]").first(),
    ];
    for (const locator of closeLocators) {
      if (await clickIfVisible(locator)) break;
    }
    await page.keyboard.press("Escape").catch(() => {});
    await page.waitForTimeout(400);
  }

  // Remove only residual consent/modal layers after attempting their real controls.
  await page.evaluate(() => {
    const phrases = /your privacy|official app|cookie|consent|sign up to continue/i;
    for (const node of document.querySelectorAll("[role='dialog'], [aria-modal='true']")) {
      if (phrases.test(node.textContent || "")) node.remove();
    }
    document.documentElement.style.overflow = "auto";
    document.body.style.overflow = "auto";
  }).catch(() => {});
}

(async () => {
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({
    headless: true,
    executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  });
  for (const target of targets) {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    await page.goto(target.url, { waitUntil: "domcontentloaded", timeout: 60000 });
    await page.waitForTimeout(6000);
    await clearObstructions(page);
    if (target.action === "footer") {
      await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await page.waitForTimeout(1800);
      await clearObstructions(page);
    } else if (target.action === "article") {
      await page.mouse.wheel(0, 400).catch(() => {});
      await page.waitForTimeout(800);
    }
    await page.screenshot({ path: path.join(output, target.file), animations: "disabled" });
    console.log(`Captured ${target.file}: ${page.url()}`);
    await page.close();
  }
  await browser.close();
})();
