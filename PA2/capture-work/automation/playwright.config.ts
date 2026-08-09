import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  fullyParallel: false,
  workers: 1,
  retries: 2,
  timeout: 120000,
  expect: {
    timeout: 15000
  },
  reporter: [
    ["list"],
    ["html", {
      outputFolder: "playwright-report",
      open: "never"
    }]
  ],
  use: {
    browserName: "chromium",
    headless: true,
    locale: "en-US",
    timezoneId: "Asia/Ho_Chi_Minh",
    navigationTimeout: 45000,
    actionTimeout: 15000,
    screenshot: "off",
    trace: "retain-on-failure",
    video: "off"
  },
  projects: [
    {
      name: "desktop",
      use: {
        viewport: {
          width: 1440,
          height: 1000
        },
        deviceScaleFactor: 1,
        isMobile: false,
        hasTouch: false
      }
    },
    {
      name: "mobile",
      use: {
        ...devices["iPhone 13"],
        viewport: {
          width: 390,
          height: 844
        },
        deviceScaleFactor: 1
      }
    }
  ]
});
