import fs from "node:fs";
import type { AttemptLog } from "./types.js";
import { logPath } from "./utils.js";

export function ensureLog(): void {
  if (!fs.existsSync(logPath) || fs.statSync(logPath).size === 0) {
    fs.writeFileSync(logPath, "# Capture log\n\n", "utf8");
  }
}

function factual(value: string): string {
  return value.replace(/\r?\n/g, " ").replace(/\s+/g, " ").trim();
}

export function appendLog(entry: AttemptLog): void {
  ensureLog();
  const lines = [
    `## ${factual(entry.timestamp)} - ${factual(entry.captureId)}`,
    "",
    `- Timestamp: ${factual(entry.timestamp)}`,
    `- Capture ID: ${factual(entry.captureId)}`,
    `- Playwright project: ${factual(entry.project)}`,
    `- Attempt number: ${entry.attempt}`,
    `- Viewport: ${factual(entry.viewport)}`,
    `- Source URL: ${factual(entry.sourceUrl)}`,
    `- Final URL: ${factual(entry.finalUrl)}`,
    `- Navigation result: ${factual(entry.navigationResult)}`,
    `- Popup action: ${factual(entry.popupAction)}`,
    `- Action result: ${factual(entry.actionResult)}`,
    `- Auto-scroll result: ${factual(entry.autoScrollResult)}`,
    `- Screenshot result: ${factual(entry.screenshotResult)}`,
    `- Output path: ${factual(entry.outputPath)}`,
    `- Error class: ${factual(entry.errorClass)}`,
    `- Error message: ${factual(entry.errorMessage)}`,
    `- Status: ${entry.status}`,
    ""
  ];
  fs.appendFileSync(logPath, `${lines.join("\n")}\n`, "utf8");
}
