import fs from "node:fs";
import path from "node:path";
import { devices, type Browser, type BrowserContextOptions, type Page } from "@playwright/test";
import { imageSize } from "image-size";
import { appendLog } from "./logger.js";
import { appendManifest, successfulCaptureIds } from "./manifest.js";
import { detectPopup, handlePopups } from "./popup-handlers.js";
import { performActions } from "./state-actions.js";
import type {
  AuthenticationState,
  CaptureStatus,
  CaptureTarget,
  ManifestRow
} from "./types.js";
import {
  autoScroll,
  captureWorkRoot,
  compactError,
  disableAnimations,
  documentMetrics,
  ensureOutputDirectories,
  localTimestamp,
  nextAvailablePng
} from "./utils.js";

const storageStatePath = path.join(
  process.cwd(),
  "private",
  "storage-state.json"
);

function contextOptions(target: CaptureTarget): BrowserContextOptions {
  const base: BrowserContextOptions = {
    locale: "en-US",
    timezoneId: "Asia/Ho_Chi_Minh",
    serviceWorkers: "block"
  };
  if (target.viewport === "mobile") {
    Object.assign(base, devices["iPhone 13"], {
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 1
    });
  } else {
    Object.assign(base, {
      viewport: { width: 1440, height: 1000 },
      screen: { width: 1440, height: 1000 },
      deviceScaleFactor: 1,
      isMobile: false,
      hasTouch: false
    });
  }
  if (fs.existsSync(storageStatePath)) {
    base.storageState = storageStatePath;
  }
  return base;
}

function authenticationState(target: CaptureTarget): AuthenticationState {
  if (fs.existsSync(storageStatePath)) {
    return "AUTHENTICATED_EXISTING_SESSION";
  }
  if (target.requiresAuth) {
    return "LOGIN_REQUIRED";
  }
  if (target.state.toLowerCase().includes("guest")) {
    return "GUEST";
  }
  return "PUBLIC";
}

async function pageBlockReason(page: Page): Promise<string> {
  const url = page.url();
  const body = await page.locator("body").innerText({ timeout: 5000 }).catch(() => "");
  const sample = `${url}\n${body}`.slice(0, 100000);
  if (/captcha|verify you are human|cloudflare|challenge-platform/i.test(sample)) {
    return "CAPTCHA or anti-bot challenge was displayed.";
  }
  if (/access denied|request blocked|temporarily blocked/i.test(sample)) {
    return "Access-block message was displayed.";
  }
  return "";
}

function outputDirectory(target: CaptureTarget, status: CaptureStatus): string {
  if (status === "FAILED" || status === "BLOCKED") {
    return path.join(captureWorkRoot, "failed");
  }
  return path.join(captureWorkRoot, target.product, target.viewport);
}

function emptyRow(target: CaptureTarget): ManifestRow {
  return {
    capture_id: target.captureId,
    product: target.product,
    viewport: target.viewport,
    page_area: target.pageArea,
    state: target.state,
    source_url: target.url,
    final_url: "",
    page_title: "",
    filename: "",
    absolute_path: "",
    captured_at_local: localTimestamp(),
    width_px: "",
    height_px: "",
    file_size_bytes: "",
    document_scroll_width: "",
    document_scroll_height: "",
    auto_scroll_iterations: "",
    reached_bottom: "",
    popup_action: "None",
    authentication_state: authenticationState(target),
    status: "FAILED",
    attempt_count: "0",
    failure_reason: "",
    related_pa1_figure: target.relatedPa1Figure ?? "",
    related_pa1_use_case: target.relatedPa1UseCase ?? "",
    notes_factual_only: ""
  };
}

export async function captureTarget(
  browser: Browser,
  target: CaptureTarget,
  projectName: string
): Promise<void> {
  ensureOutputDirectories();
  if (successfulCaptureIds().has(target.captureId)) {
    return;
  }

  const row = emptyRow(target);
  if (target.requiresAuth && !fs.existsSync(storageStatePath)) {
    row.status = "BLOCKED";
    row.attempt_count = "1";
    row.failure_reason = "No existing authenticated session was available.";
    row.notes_factual_only = "The target requires an existing authenticated session.";
    appendManifest(row);
    appendLog({
      timestamp: row.captured_at_local,
      captureId: target.captureId,
      project: projectName,
      attempt: 1,
      viewport: target.viewport,
      sourceUrl: target.url,
      finalUrl: "",
      navigationResult: "Not attempted because the target requires an authenticated session.",
      popupAction: "None",
      actionResult: "No target actions",
      autoScrollResult: "Not run",
      screenshotResult: "Not run",
      outputPath: "",
      errorClass: "LoginRequired",
      errorMessage: row.failure_reason,
      status: "BLOCKED"
    });
    return;
  }

  let finalError: unknown;
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    let context;
    let page: Page | undefined;
    let navigationResult = "Not started";
    let popupAction = "None";
    let actionResult = "No target actions";
    let autoScrollResult = "Not run";
    let screenshotResult = "Not run";
    let outputPath = "";
    let status: CaptureStatus = "FAILED";
    let errorClass = "";
    let errorMessage = "";
    let missingState = false;
    let blockReason = "";

    try {
      context = await browser.newContext(contextOptions(target));
      page = await context.newPage();
      const response = await page.goto(target.url, {
        waitUntil: "domcontentloaded",
        timeout: 45000
      });
      navigationResult = response
        ? `HTTP ${response.status()} ${response.statusText()}`
        : "Navigation completed without a main resource response.";

      await page.waitForLoadState("load", { timeout: 15000 }).catch(() => {});
      await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
      await page.waitForTimeout(3000);
      row.final_url = page.url();
      row.page_title = await page.title().catch(() => "");
      blockReason = await pageBlockReason(page);

      const popupDetected = await detectPopup(page);
      if (target.captureBeforePopupDismiss) {
        if (popupDetected) {
          popupAction = `Retained before screenshot: ${popupDetected}`;
        } else {
          popupAction = "None";
          missingState = true;
          actionResult = "The requested popup or cookie banner was not present.";
        }
      } else {
        popupAction = await handlePopups(page);
      }

      if (!blockReason) {
        const actions = await performActions(page, target.actions);
        actionResult = actions.result;
        missingState = missingState || actions.missingState;
      } else {
        status = "BLOCKED";
        actionResult = blockReason;
      }

      await disableAnimations(page);
      const scroll = await autoScroll(page);
      autoScrollResult =
        `reachedBottom=${scroll.reachedBottom}; iterations=${scroll.iterations}; finalHeight=${scroll.finalHeight}`;
      const metrics = await documentMetrics(page);
      row.document_scroll_width = String(metrics.width);
      row.document_scroll_height = String(metrics.height);
      row.auto_scroll_iterations = String(scroll.iterations);
      row.reached_bottom = String(scroll.reachedBottom);

      if (blockReason) {
        status = "BLOCKED";
      } else if (missingState) {
        status = "MISSING_CURRENT_STATE";
      } else if (!scroll.reachedBottom) {
        status = "PARTIAL";
      } else {
        status = "SUCCESS";
      }

      const temporaryDirectory = path.join(process.cwd(), "test-results", "capture-temp");
      fs.mkdirSync(temporaryDirectory, { recursive: true });
      const temporaryPath = path.join(
        temporaryDirectory,
        `${target.captureId}-attempt-${attempt}.png`
      );
      await page.screenshot({
        path: temporaryPath,
        fullPage: true,
        type: "png",
        animations: "disabled",
        caret: "hide",
        timeout: 60000
      });
      const destination = nextAvailablePng(outputDirectory(target, status), target.captureId);
      fs.renameSync(temporaryPath, destination);
      outputPath = destination;
      screenshotResult = "Full-page PNG written.";

      const buffer = fs.readFileSync(destination);
      const dimensions = imageSize(buffer);
      row.filename = path.basename(destination);
      row.absolute_path = destination;
      row.width_px = String(dimensions.width ?? "");
      row.height_px = String(dimensions.height ?? "");
      row.file_size_bytes = String(fs.statSync(destination).size);
      row.final_url = page.url();
      row.page_title = await page.title().catch(() => row.page_title);
      row.captured_at_local = localTimestamp();
      row.popup_action = popupAction;
      row.authentication_state = authenticationState(target);
      row.status = status;
      row.attempt_count = String(attempt);
      row.failure_reason =
        status === "BLOCKED"
          ? blockReason
          : status === "MISSING_CURRENT_STATE"
            ? actionResult
            : "";
      const notes: string[] = [];
      if (popupAction !== "None") {
        notes.push(`Popup action: ${popupAction}.`);
      }
      if (row.final_url && row.final_url !== target.url) {
        notes.push(`Page final URL: ${row.final_url}.`);
      }
      if (status === "PARTIAL") {
        notes.push("Auto-scroll did not report reaching the document bottom.");
      }
      row.notes_factual_only = notes.join(" ");

      appendLog({
        timestamp: row.captured_at_local,
        captureId: target.captureId,
        project: projectName,
        attempt,
        viewport: target.viewport,
        sourceUrl: target.url,
        finalUrl: row.final_url,
        navigationResult,
        popupAction,
        actionResult,
        autoScrollResult,
        screenshotResult,
        outputPath,
        errorClass,
        errorMessage,
        status
      });
      appendManifest(row);
      await page.close().catch(() => {});
      await context.close().catch(() => {});
      return;
    } catch (error) {
      finalError = error;
      const compact = compactError(error);
      errorClass = compact.errorClass;
      errorMessage = compact.message;
      status = /captcha|cloudflare|challenge/i.test(errorMessage) ? "BLOCKED" : "FAILED";
      appendLog({
        timestamp: localTimestamp(),
        captureId: target.captureId,
        project: projectName,
        attempt,
        viewport: target.viewport,
        sourceUrl: target.url,
        finalUrl: page?.url() ?? row.final_url,
        navigationResult,
        popupAction,
        actionResult,
        autoScrollResult,
        screenshotResult,
        outputPath,
        errorClass,
        errorMessage,
        status
      });
      await page?.close().catch(() => {});
      await context?.close().catch(() => {});
    }
  }

  const compact = compactError(finalError);
  row.status = /captcha|cloudflare|challenge/i.test(compact.message)
    ? "BLOCKED"
    : "FAILED";
  row.attempt_count = "3";
  row.failure_reason = compact.message;
  row.captured_at_local = localTimestamp();
  row.notes_factual_only = "All three technical attempts ended without a saved screenshot.";
  appendManifest(row);
}
