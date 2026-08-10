import type { Page } from "@playwright/test";

const candidateNames = [
  /accept all/i,
  /accept all cookies/i,
  /accept cookies/i,
  /^accept$/i,
  /^agree$/i,
  /allow all/i,
  /^continue$/i,
  /^close$/i,
  /^dismiss$/i,
  /no thanks/i,
  /not now/i,
  /maybe later/i,
  /got it/i,
  /i understand/i,
  /reject all/i,
  /only necessary/i
];

export async function detectPopup(page: Page): Promise<string> {
  for (const name of candidateNames) {
    const button = page.getByRole("button", { name }).first();
    if (await button.isVisible().catch(() => false)) {
      return name.source;
    }
  }
  const dialog = page.getByRole("dialog").first();
  return await dialog.isVisible().catch(() => false) ? "visible dialog" : "";
}

export async function handlePopups(page: Page): Promise<string> {
  const actions: string[] = [];
  for (const name of candidateNames) {
    const button = page.getByRole("button", { name }).first();
    if (
      await button.isVisible().catch(() => false) &&
      await button.isEnabled().catch(() => false)
    ) {
      const label = (await button.innerText().catch(() => "")) || name.source;
      const clicked = await button.click({ timeout: 5000 })
        .then(() => true)
        .catch(() => false);
      if (clicked) {
        actions.push(label.replace(/\s+/g, " ").slice(0, 80));
        await page.waitForTimeout(750);
      }
    }
  }
  return actions.length ? actions.join(" | ") : "None";
}
