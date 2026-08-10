import type { Page } from "@playwright/test";
import type { CaptureAction } from "./types.js";

export async function performActions(
  page: Page,
  actions: CaptureAction[] = []
): Promise<{ result: string; missingState: boolean }> {
  const results: string[] = [];
  let missingState = false;

  for (const action of actions) {
    try {
      switch (action.type) {
        case "wait":
          await page.waitForTimeout(action.milliseconds);
          results.push(`wait ${action.milliseconds}ms`);
          break;
        case "clickRole": {
          const locator = page.getByRole(action.role, {
            name: action.name,
            exact: action.exact
          }).first();
          await locator.waitFor({ state: "visible", timeout: 8000 });
          await locator.click({ timeout: 8000 });
          results.push(`clicked ${action.role} ${action.name}`);
          break;
        }
        case "clickText": {
          const locator = page.getByText(action.text, { exact: action.exact }).first();
          await locator.waitFor({ state: "visible", timeout: 8000 });
          await locator.click({ timeout: 8000 });
          results.push(`clicked text ${action.text}`);
          break;
        }
        case "clickLocator":
          await page.locator(action.selector).first().click({ timeout: 8000 });
          results.push(`clicked locator ${action.selector}`);
          break;
        case "hover":
          await page.locator(action.selector).first().hover({ timeout: 8000 });
          results.push(`hovered ${action.selector}`);
          break;
        case "press":
          await page.keyboard.press(action.key);
          results.push(`pressed ${action.key}`);
          break;
        case "fill":
          await page.locator(action.selector).first().fill(action.value, { timeout: 8000 });
          results.push(`filled ${action.selector}`);
          break;
        case "selectOption":
          await page.locator(action.selector).first().selectOption(action.value, { timeout: 8000 });
          results.push(`selected ${action.value}`);
          break;
        case "waitForText":
          await page.getByText(action.text, { exact: false }).first()
            .waitFor({ state: "visible", timeout: 10000 });
          results.push(`found text ${action.text}`);
          break;
        case "waitForUrl":
          await page.waitForURL(new RegExp(action.urlPattern, "i"), { timeout: 15000 });
          results.push(`matched URL ${action.urlPattern}`);
          break;
        case "screenshotCheckpoint":
          results.push(`checkpoint ${action.state}`);
          break;
      }
      await page.waitForTimeout(500);
    } catch (error) {
      missingState = true;
      const message = error instanceof Error ? error.message.split("\n")[0] : String(error);
      results.push(`${action.type} unavailable: ${message.slice(0, 180)}`);
      break;
    }
  }

  return {
    result: results.length ? results.join("; ") : "No target actions",
    missingState
  };
}
