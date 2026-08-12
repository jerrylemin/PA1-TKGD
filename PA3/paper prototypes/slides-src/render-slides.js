const fs = require('fs');
const path = require('path');
const http = require('http');
const { chromium } = require('playwright');

const sourceDir = __dirname;
const qaDir = path.resolve(sourceDir, '..', 'qa');
const viewportWidth = Number(process.env.VIEWPORT_WIDTH || 1920);
const viewportHeight = Number(process.env.VIEWPORT_HEIGHT || 1080);
const renderSubdir = process.env.RENDER_SUBDIR || 'renders';
const htmlFile = process.env.HTML_FILE || 'index.html';
const renderDir = path.join(qaDir, renderSubdir);
fs.mkdirSync(renderDir, { recursive: true });

function contentType(file) {
  if (file.endsWith('.html')) return 'text/html; charset=utf-8';
  if (file.endsWith('.js')) return 'text/javascript; charset=utf-8';
  if (file.endsWith('.png')) return 'image/png';
  if (file.endsWith('.jpg') || file.endsWith('.jpeg')) return 'image/jpeg';
  if (file.endsWith('.css')) return 'text/css; charset=utf-8';
  return 'application/octet-stream';
}

const server = http.createServer((req, res) => {
  const requested = decodeURIComponent((req.url || '/').split('?')[0]);
  const relative = requested === '/' ? '/index.html' : requested;
  const file = path.resolve(sourceDir, '.' + relative);
  if (!file.startsWith(sourceDir)) { res.writeHead(403); res.end('Forbidden'); return; }
  fs.readFile(file, (error, data) => {
    if (error) { res.writeHead(404); res.end('Not found'); return; }
    res.writeHead(200, { 'Content-Type': contentType(file), 'Cache-Control': 'no-store' });
    res.end(data);
  });
});

function relativeRect(rect, stageRect) {
  return { left: rect.left - stageRect.left, top: rect.top - stageRect.top, right: rect.right - stageRect.left, bottom: rect.bottom - stageRect.top, width: rect.width, height: rect.height };
}

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: viewportWidth, height: viewportHeight }, deviceScaleFactor: 1 });
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push('console: ' + msg.text()); });
  page.on('pageerror', error => errors.push('pageerror: ' + error.message));
  const url = `http://127.0.0.1:${port}/${htmlFile}`;
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const count = await page.locator('.slide').count();
  const report = [];
  for (let i = 0; i < count; i += 1) {
    await page.evaluate(index => window.presentation.showSlide(index), i);
    await page.waitForTimeout(900);
    const result = await page.evaluate(() => {
      const stage = document.getElementById('deckStage');
      const stageRect = stage.getBoundingClientRect();
      const active = document.querySelector('.slide.active');
      const overflow = [];
      active.querySelectorAll('*').forEach(el => {
        if (el.classList.contains('watermark') || el.classList.contains('chapter-number')) return;
        const rect = el.getBoundingClientRect();
        const r = { left: rect.left - stageRect.left, top: rect.top - stageRect.top, right: rect.right - stageRect.left, bottom: rect.bottom - stageRect.top, width: rect.width, height: rect.height };
        if ((r.left < -2 || r.top < -2 || r.right > 1922 || r.bottom > 1082) && r.width > 0 && r.height > 0) {
          overflow.push({ tag: el.tagName, className: el.className, rect: r });
        }
      });
      const images = [...active.querySelectorAll('img')].map(img => ({ src: img.getAttribute('src'), loaded: img.complete && img.naturalWidth > 0 }));
      return { title: active.dataset.title, overflow: overflow.slice(0, 20), imageFailures: images.filter(item => !item.loaded), images: images.length };
    });
    const output = path.join(renderDir, `slide-${String(i + 1).padStart(2, '0')}.png`);
    await page.screenshot({ path: output, animations: 'disabled' });
    report.push({ slide: i + 1, ...result, file: output });
  }
  await browser.close();
  server.close();
  fs.writeFileSync(path.join(qaDir, `render-report-${renderSubdir}.json`), JSON.stringify({ viewport: { width: viewportWidth, height: viewportHeight }, slideCount: count, errors, slides: report }, null, 2));
  console.log(JSON.stringify({ slideCount: count, errors, slides: report.map(item => ({ slide: item.slide, title: item.title, overflowCount: item.overflow.length, imageFailures: item.imageFailures })) }, null, 2));
})().catch(error => { console.error(error.stack || error); server.close(); process.exit(1); });
