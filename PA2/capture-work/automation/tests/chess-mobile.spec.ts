import { test } from "@playwright/test";
import { captureTarget } from "../src/capture-page.js";
import { targetsFor } from "../src/capture-plan.js";

for (const target of targetsFor("chess", "mobile")) {
  test(target.captureId, async ({ browser }, testInfo) => {
    await captureTarget(browser, target, testInfo.project.name);
  });
}
