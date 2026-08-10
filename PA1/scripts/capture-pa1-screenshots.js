const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const ACCESS_DATE = "2026-06-11";
const ROOT = path.resolve(__dirname, "..");
const MANIFEST_PATH = path.join(ROOT, "assets", "figures_manifest.json");
const MANUAL_PATH = path.join(ROOT, "assets", "screenshots", "MANUAL_SCREENSHOT_REQUIRED.md");

const viewports = {
  desktop: { width: 1440, height: 1000, isMobile: false, hasTouch: false },
  tablet: { width: 768, height: 1024, isMobile: true, hasTouch: true },
  mobile: { width: 390, height: 844, isMobile: true, hasTouch: true },
};

const fifaArticle =
  "https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september";

const tasks = [
  ["F-01", "fifa", "Home page information hierarchy", "https://www.fifa.com/en", "desktop", "fifa_home_desktop.png", "home"],
  ["F-08", "fifa", "Mobile scrolling and content density", "https://www.fifa.com/en", "mobile", "fifa_home_mobile.png", "home"],
  ["F-T01", "fifa", "Tablet home layout", "https://www.fifa.com/en", "tablet", "fifa_home_tablet.png", "home"],
  ["F-02", "fifa", "Desktop navigation", "https://www.fifa.com/en", "desktop", "fifa_navigation_desktop.png", "navigation"],
  ["F-03", "fifa", "Mobile navigation", "https://www.fifa.com/en", "mobile", "fifa_navigation_mobile.png", "mobile-menu"],
  ["F-05", "fifa", "Search or discovery flow", "https://www.fifa.com/en/search?q=world%20cup", "desktop", "fifa_search_desktop.png", "search"],
  ["F-04", "fifa", "Match Centre fixtures page", "https://www.fifa.com/en/match-centre", "desktop", "fifa_match_centre_desktop.png", "match"],
  ["F-04M", "fifa", "Match Centre mobile fixtures page", "https://www.fifa.com/en/match-centre", "mobile", "fifa_match_centre_mobile.png", "match"],
  ["F-06", "fifa", "News article page", fifaArticle, "desktop", "fifa_news_article_desktop.png", "article"],
  ["F-06M", "fifa", "News article mobile page", fifaArticle, "mobile", "fifa_news_article_mobile.png", "article"],
  ["F-07", "fifa", "Tournament or competition page", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026", "desktop", "fifa_competition_desktop.png", "competition"],
  ["F-09B", "fifa", "Footer language and ecosystem area", "https://www.fifa.com/en", "desktop", "fifa_footer_desktop.png", "footer"],
  ["F-10B", "fifa", "FIFA+ video or media area", "https://www.plus.fifa.com/", "desktop", "fifa_video_or_media_desktop.png", "media"],

  ["C-01", "chess", "Home page information hierarchy", "https://www.chess.com/", "desktop", "chess_home_desktop.png", "home"],
  ["C-08", "chess", "Mobile home layout", "https://www.chess.com/", "mobile", "chess_home_mobile.png", "home"],
  ["C-T01", "chess", "Tablet home layout", "https://www.chess.com/", "tablet", "chess_home_tablet.png", "home"],
  ["C-06", "chess", "Desktop navigation", "https://www.chess.com/", "desktop", "chess_navigation_desktop.png", "navigation"],
  ["C-06M", "chess", "Mobile navigation", "https://www.chess.com/", "mobile", "chess_navigation_mobile.png", "mobile-menu"],
  ["C-02", "chess", "Play entry point", "https://www.chess.com/play/online", "desktop", "chess_play_desktop.png", "play"],
  ["C-02M", "chess", "Mobile play entry point", "https://www.chess.com/play/online", "mobile", "chess_play_mobile.png", "play"],
  ["C-03", "chess", "Game board or demo board", "https://www.chess.com/play/computer", "desktop", "chess_board_or_demo_desktop.png", "board"],
  ["C-04", "chess", "Puzzle page", "https://www.chess.com/puzzles", "desktop", "chess_puzzles_desktop.png", "puzzles"],
  ["C-04M", "chess", "Puzzle page mobile", "https://www.chess.com/puzzles", "mobile", "chess_puzzles_mobile.png", "puzzles"],
  ["C-05", "chess", "Learn page", "https://www.chess.com/lessons", "desktop", "chess_learn_desktop.png", "learn"],
  ["C-09B", "chess", "News page", "https://www.chess.com/news", "desktop", "chess_news_desktop.png", "news"],
  ["C-10B", "chess", "Account prompt or sign-in entry", "https://www.chess.com/login", "desktop", "chess_account_or_prompt_desktop.png", "account"],
];

function ensureDirs() {
  for (const dir of [
    "assets/screenshots/raw/fifa",
    "assets/screenshots/raw/chess",
    "assets/screenshots/annotated/fifa",
    "assets/screenshots/annotated/chess",
    "assets/screenshots/crops/fifa",
    "assets/screenshots/crops/chess",
    "assets/diagrams",
  ]) {
    fs.mkdirSync(path.join(ROOT, dir), { recursive: true });
  }
}

async function acceptBanners(page) {
  const candidates = [
    "Accept All Cookies",
    "Accept all cookies",
    "Accept Cookies",
    "Accept",
    "I Accept",
    "I'm OK with that",
    "OK with that",
    "Agree",
    "Got it",
    "Continue",
  ];
  for (const text of candidates) {
    const locator = page.getByRole("button", { name: new RegExp(text, "i") }).first();
    if (await locator.isVisible({ timeout: 700 }).catch(() => false)) {
      await locator.click({ timeout: 1500 }).catch(() => {});
      await page.waitForTimeout(500);
      break;
    }
  }
}

async function dismissOverlays(page, viewport) {
  const closeButtons = [
    page.getByRole("button", { name: /close|dismiss/i }).first(),
    page.locator("button[aria-label*='close' i]").first(),
    page.getByRole("button", { name: /^ok$/i }).first(),
  ];
  for (const locator of closeButtons) {
    if (await locator.isVisible({ timeout: 700 }).catch(() => false)) {
      await locator.click({ timeout: 1500 }).catch(() => {});
      await page.waitForTimeout(500);
      return;
    }
  }
  const bodyText = await page.locator("body").innerText({ timeout: 1000 }).catch(() => "");
  if (/Don't miss the FIFA Countdown Concert|FIFA Countdown Concert/i.test(bodyText)) {
    await page.mouse.click(Math.max(40, viewport.width - 72), Math.min(viewport.height - 80, Math.round(viewport.height * 0.34))).catch(() => {});
    await page.waitForTimeout(700);
  }
}

async function openPossibleMenu(page) {
  const locators = [
    page.getByRole("button", { name: /menu|navigation|open/i }).first(),
    page.locator("button[aria-label*='menu' i]").first(),
    page.locator("button:has(svg)").first(),
  ];
  for (const locator of locators) {
    if (await locator.isVisible({ timeout: 1000 }).catch(() => false)) {
      await locator.click({ timeout: 2000 }).catch(() => {});
      await page.waitForTimeout(1200);
      return;
    }
  }
}

async function prepareState(page, kind) {
  await acceptBanners(page);
  await dismissOverlays(page, page.viewportSize() || { width: 1440, height: 1000 });
  if (kind === "mobile-menu") {
    await openPossibleMenu(page);
  }
  if (kind === "footer") {
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await page.waitForTimeout(1500);
  }
  if (kind === "article") {
    await page.mouse.wheel(0, 350).catch(() => {});
    await page.waitForTimeout(700);
  }
}

async function captureTask(browser, task) {
  const [figureId, product, screen, url, viewportName, filename, kind] = task;
  const viewport = viewports[viewportName];
  const context = await browser.newContext({
    viewport: { width: viewport.width, height: viewport.height },
    isMobile: viewport.isMobile,
    hasTouch: viewport.hasTouch,
    userAgent:
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148 Safari/537.36",
  });
  const page = await context.newPage();
  const rawRel = `assets/screenshots/raw/${product}/${filename}`;
  const rawPath = path.join(ROOT, rawRel);
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60000 });
    await page.waitForTimeout(4500);
    await prepareState(page, kind);
    await page.screenshot({ path: rawPath, fullPage: false, animations: "disabled" });
    const textStart = await page.locator("body").innerText({ timeout: 3000 }).catch(() => "");
    return {
      figure_id: figureId,
      product,
      screen,
      url: page.url(),
      viewport: viewportName,
      viewport_size: { width: viewport.width, height: viewport.height },
      raw_path: rawRel,
      capture_status: "success",
      access_date: ACCESS_DATE,
      notes: `Captured ${kind} state. Visible text sample: ${textStart.replace(/\s+/g, " ").slice(0, 180)}`,
    };
  } catch (error) {
    return {
      figure_id: figureId,
      product,
      screen,
      url,
      viewport: viewportName,
      viewport_size: { width: viewport.width, height: viewport.height },
      raw_path: rawRel,
      capture_status: "failed",
      access_date: ACCESS_DATE,
      notes: error.message,
    };
  } finally {
    await context.close();
  }
}

function writeManualFailures(items) {
  const failed = items.filter((item) => item.capture_status !== "success");
  const lines = ["# Manual Screenshot Required", ""];
  if (!failed.length) {
    lines.push("No manual screenshots are required. All automated captures succeeded.");
  }
  for (const item of failed) {
    lines.push(`## ${item.figure_id} ${item.screen}`);
    lines.push(`Product: ${item.product}`);
    lines.push(`URL: ${item.url}`);
    lines.push(`Viewport: ${item.viewport} ${item.viewport_size.width}x${item.viewport_size.height}`);
    lines.push(`Required screen state: ${item.screen}`);
    lines.push(`Exact filename: ${path.basename(item.raw_path)}`);
    lines.push(`Save folder: ${path.dirname(item.raw_path)}`);
    lines.push(`Why automation failed: ${item.notes}`);
    lines.push("Manual steps: Open the URL, set the viewport, dismiss popups, reach the named screen state, and save a PNG with the exact filename.");
    lines.push(`Expected UI region to capture: ${item.screen}`);
    lines.push("");
  }
  fs.writeFileSync(MANUAL_PATH, `${lines.join("\n")}\n`, "utf8");
}

(async () => {
  ensureDirs();
  const browser = await chromium.launch({ headless: true });
  const manifest = [];
  for (const task of tasks) {
    const result = await captureTask(browser, task);
    manifest.push(result);
    console.log(`${result.capture_status.toUpperCase()} ${result.figure_id} ${result.raw_path}`);
  }
  await browser.close();
  fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2), "utf8");
  writeManualFailures(manifest);
  const ok = manifest.filter((item) => item.capture_status === "success").length;
  const failed = manifest.length - ok;
  console.log(`Capture complete: ${ok} succeeded, ${failed} failed.`);
  if (failed) process.exitCode = 1;
})();
