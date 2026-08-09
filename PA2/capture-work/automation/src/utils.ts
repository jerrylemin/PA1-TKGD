import fs from "node:fs";
import path from "node:path";
import type { Page } from "@playwright/test";

export const captureWorkRoot = path.resolve(process.cwd(), "..");
export const manifestPath = path.join(captureWorkRoot, "capture-manifest.csv");
export const logPath = path.join(captureWorkRoot, "capture-log.md");
export const summaryPath = path.join(captureWorkRoot, "capture-summary.json");
export const urlsPath = path.join(captureWorkRoot, "urls-discovered.txt");

export function localTimestamp(): string {
  const parts = new Intl.DateTimeFormat("sv-SE", {
    timeZone: "Asia/Ho_Chi_Minh",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false
  }).formatToParts(new Date());
  const value = (type: string) => parts.find((part) => part.type === type)?.value ?? "";
  return `${value("year")}-${value("month")}-${value("day")} ${value("hour")}:${value("minute")}:${value("second")} +07:00`;
}

export function compactError(error: unknown): { errorClass: string; message: string } {
  if (error instanceof Error) {
    return {
      errorClass: error.name || "Error",
      message: error.message.replace(/\s+/g, " ").slice(0, 500)
    };
  }
  return {
    errorClass: "UnknownError",
    message: String(error).replace(/\s+/g, " ").slice(0, 500)
  };
}

export function safeFilename(value: string): string {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9-]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 150);
}

export function nextAvailablePng(directory: string, basename: string): string {
  fs.mkdirSync(directory, { recursive: true });
  const initial = path.join(directory, `${safeFilename(basename)}.png`);
  if (!fs.existsSync(initial)) {
    return initial;
  }
  for (let revision = 2; revision < 1000; revision += 1) {
    const candidate = path.join(
      directory,
      `${safeFilename(basename)}-r${String(revision).padStart(2, "0")}.png`
    );
    if (!fs.existsSync(candidate)) {
      return candidate;
    }
  }
  throw new Error(`No available revision filename for ${basename}`);
}

export async function disableAnimations(page: Page): Promise<void> {
  await page.addStyleTag({
    content: `
      *,
      *::before,
      *::after {
        animation-duration: 0s !important;
        animation-delay: 0s !important;
        transition-duration: 0s !important;
        transition-delay: 0s !important;
        scroll-behavior: auto !important;
        caret-color: transparent !important;
      }
    `
  }).catch(() => {});
}

export async function autoScroll(page: Page): Promise<{
  reachedBottom: boolean;
  iterations: number;
  finalHeight: number;
}> {
  let previousHeight = 0;
  let stableCount = 0;
  const startedAt = Date.now();
  let completedIterations = 0;

  for (let iteration = 1; iteration <= 100; iteration += 1) {
    completedIterations = iteration;
    if (Date.now() - startedAt > 60000) {
      break;
    }

    const metrics = await page.evaluate(() => {
      const root = document.documentElement;
      const body = document.body;
      const scrollHeight = Math.max(root?.scrollHeight ?? 0, body?.scrollHeight ?? 0);
      const nextY = Math.min(
        window.scrollY + 900,
        Math.max(0, scrollHeight - window.innerHeight)
      );
      window.scrollTo(0, nextY);
      return {
        scrollHeight,
        scrollY: window.scrollY,
        viewportHeight: window.innerHeight,
        reachedBottom:
          Math.ceil(window.scrollY + window.innerHeight) >= scrollHeight - 2
      };
    });

    await page.waitForTimeout(350);
    stableCount = metrics.scrollHeight === previousHeight ? stableCount + 1 : 0;
    previousHeight = metrics.scrollHeight;

    if (metrics.reachedBottom && stableCount >= 3) {
      await page.waitForTimeout(2000);
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(1000);
      return {
        reachedBottom: true,
        iterations: iteration,
        finalHeight: metrics.scrollHeight
      };
    }
  }

  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(1000);
  return {
    reachedBottom: false,
    iterations: completedIterations,
    finalHeight: previousHeight
  };
}

export async function documentMetrics(page: Page): Promise<{
  width: number;
  height: number;
}> {
  return page.evaluate(() => {
    const root = document.documentElement;
    const body = document.body;
    return {
      width: Math.max(root?.scrollWidth ?? 0, body?.scrollWidth ?? 0),
      height: Math.max(root?.scrollHeight ?? 0, body?.scrollHeight ?? 0)
    };
  });
}

export function ensureOutputDirectories(): void {
  for (const relative of [
    "fifa/desktop",
    "fifa/mobile",
    "fifa/states",
    "chess/desktop",
    "chess/mobile",
    "chess/states",
    "failed"
  ]) {
    fs.mkdirSync(path.join(captureWorkRoot, relative), { recursive: true });
  }
}
