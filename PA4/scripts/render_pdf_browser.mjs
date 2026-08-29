import { createServer } from "node:http";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "../../PA2/capture-work/automation/node_modules/playwright/index.mjs";

const PA4 = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const FINAL = path.join(PA4, "final");
const OUT = path.join(PA4, "qa", "pdf-renders");
const runtimeNodeModules = path.resolve(path.dirname(process.execPath), "..", "node_modules");
const pdfjsRoot = path.join(runtimeNodeModules, "pdfjs-dist");

const html = `<!doctype html>
<html><body style="margin:0;background:#fff">
<script type="module">
import * as pdfjsLib from "/pdfjs/build/pdf.mjs";
pdfjsLib.GlobalWorkerOptions.workerSrc = "/pdfjs/build/pdf.worker.mjs";
const pdfName = new URLSearchParams(location.search).get("pdf");
const documentProxy = await pdfjsLib.getDocument({ url: "/pdf/" + encodeURIComponent(pdfName), disableWorker: true }).promise;
for (let pageNumber = 1; pageNumber <= documentProxy.numPages; pageNumber += 1) {
  const page = await documentProxy.getPage(pageNumber);
  const viewport = page.getViewport({ scale: 1.35 });
  const canvas = document.createElement("canvas");
  canvas.dataset.page = String(pageNumber);
  canvas.width = viewport.width;
  canvas.height = viewport.height;
  canvas.style.display = "block";
  canvas.style.margin = "0 auto 12px";
  document.body.appendChild(canvas);
  await page.render({ canvasContext: canvas.getContext("2d"), viewport }).promise;
}
document.body.dataset.pageCount = String(documentProxy.numPages);
window.__renderReady = true;
</script></body></html>`;

function contentType(filePath) {
  if (filePath.endsWith(".mjs")) return "text/javascript; charset=utf-8";
  if (filePath.endsWith(".pdf")) return "application/pdf";
  return "application/octet-stream";
}

async function serveFile(response, filePath) {
  response.writeHead(200, { "Content-Type": contentType(filePath) });
  response.end(await readFile(filePath));
}

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url, "http://127.0.0.1");
    if (url.pathname === "/") {
      response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      response.end(html);
      return;
    }
    if (url.pathname.startsWith("/pdf/")) {
      const name = decodeURIComponent(url.pathname.slice("/pdf/".length));
      const filePath = path.resolve(FINAL, name);
      if (path.dirname(filePath) !== FINAL || !filePath.endsWith(".pdf")) throw new Error("invalid PDF path");
      await serveFile(response, filePath);
      return;
    }
    if (url.pathname.startsWith("/pdfjs/")) {
      const relative = url.pathname.slice("/pdfjs/".length);
      const filePath = path.resolve(pdfjsRoot, relative);
      if (!filePath.startsWith(pdfjsRoot) || !filePath.endsWith(".mjs")) throw new Error("invalid PDF.js path");
      await serveFile(response, filePath);
      return;
    }
    response.writeHead(404);
    response.end("Not found");
  } catch (error) {
    response.writeHead(404);
    response.end(String(error.message));
  }
});

await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const address = server.address();
const baseUrl = `http://127.0.0.1:${address.port}`;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 900, height: 1200 } });
const pageErrors = [];
page.on("pageerror", (error) => pageErrors.push(error.message));
page.on("console", (message) => { if (message.type() === "error") pageErrors.push(message.text()); });
const manifest = [];
await mkdir(OUT, { recursive: true });

try {
  const pdfNames = (await readFile(path.join(FINAL, "Group10-PA4-HifiProtype.pdf"))).length ? [
    "Group10-PA4-HifiProtype.pdf",
    "Group10-PA4-SummativeUserStudy.pdf",
    "Group10-PA4-WeeklyReport.pdf",
  ] : [];
  for (const pdfName of pdfNames) {
    await page.goto(`${baseUrl}/?pdf=${encodeURIComponent(pdfName)}`);
    try {
      await page.waitForFunction(() => window.__renderReady === true, { timeout: 10000 });
    } catch (error) {
      throw new Error(`PDF.js render failed for ${pdfName}: ${pageErrors.join(" | ") || error.message}`);
    }
    const target = path.join(OUT, path.basename(pdfName, ".pdf"));
    await mkdir(target, { recursive: true });
    const pageCount = await page.locator("canvas").count();
    const pages = [];
    for (let pageNumber = 1; pageNumber <= pageCount; pageNumber += 1) {
      const imagePath = path.join(target, `page-${String(pageNumber).padStart(2, "0")}.png`);
      await page.locator(`canvas[data-page="${pageNumber}"]`).screenshot({ path: imagePath });
      pages.push({ page: pageNumber, image: imagePath });
    }
    manifest.push({ file: path.join(FINAL, pdfName), page_count: pageCount, pages });
  }
} finally {
  await browser.close();
  await new Promise((resolve) => server.close(resolve));
}

await writeFile(path.join(OUT, "render-manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
console.log(JSON.stringify(manifest, null, 2));
