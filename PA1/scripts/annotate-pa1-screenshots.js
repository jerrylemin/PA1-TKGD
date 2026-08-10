const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const ROOT = path.resolve(__dirname, "..");
const MANIFEST_PATH = path.join(ROOT, "assets", "figures_manifest.json");

const concepts = {
  fifa: {
    Home: ["visual hierarchy", "hero and task entry compete for attention"],
    navigation: ["recognition over recall", "global labels expose important football tasks"],
    Mobile: ["progressive disclosure", "mobile navigation hides task paths behind an extra step"],
    Search: ["information scent", "search/discovery needs category clarity for official lookup"],
    Match: ["mental model", "fixture lists need date and competition alignment"],
    News: ["reading load", "article pages must support scanning in interrupted contexts"],
    Tournament: ["information architecture", "competition pages group deep tournament content"],
    Footer: ["international support", "footer and language areas support global users"],
    "FIFA+": ["attention", "media rails can become dense when users want one highlight"],
  },
  chess: {
    Home: ["information scent", "core chess actions are visible from the start"],
    Mobile: ["motor accuracy", "small screens compress navigation and action controls"],
    navigation: ["memory load", "feature-rich menus require clear grouping"],
    Play: ["efficiency", "play entry points reduce time to first game"],
    Game: ["direct manipulation", "the board uses the familiar chess metaphor for piece movement"],
    Puzzle: ["feedback", "puzzle surfaces need clear correctness and next-step feedback"],
    Learn: ["progressive disclosure", "beginner learning paths need obvious first steps"],
    News: ["content discovery", "news pages shift the product from play to reading"],
    Account: ["user control", "sign-in prompts can interrupt fast-play intent"],
  },
};

function rel(...parts) {
  return parts.join("/").replace(/\\/g, "/");
}

function pickConcept(item) {
  const table = concepts[item.product] || {};
  const key = Object.keys(table).find((name) => item.screen.toLowerCase().includes(name.toLowerCase()));
  const [hci_concept, claim] = key ? table[key] : ["attention", "the visible UI region shapes task success"];
  return { hci_concept, claim };
}

function regionsFor(item, width, height) {
  const mobile = item.viewport === "mobile";
  const base = [];
  if (item.screen.toLowerCase().includes("navigation")) {
    base.push({ label: "A", element: "navigation entry", x: 0.04, y: 0.06, w: mobile ? 0.35 : 0.74, h: mobile ? 0.11 : 0.08 });
  } else if (item.screen.toLowerCase().includes("footer")) {
    base.push({ label: "A", element: "footer language and ecosystem links", x: 0.05, y: 0.55, w: 0.9, h: 0.35 });
  } else if (item.screen.toLowerCase().includes("match")) {
    base.push({ label: "A", element: "date and fixture selector", x: 0.04, y: 0.18, w: 0.9, h: 0.18 });
    base.push({ label: "B", element: "match list area", x: 0.06, y: 0.36, w: 0.82, h: 0.36 });
  } else if (item.screen.toLowerCase().includes("play") || item.screen.toLowerCase().includes("game board")) {
    base.push({ label: "A", element: "board or play surface", x: mobile ? 0.02 : 0.24, y: mobile ? 0.18 : 0.12, w: mobile ? 0.96 : 0.42, h: mobile ? 0.44 : 0.62 });
    base.push({ label: "B", element: "start or game controls", x: mobile ? 0.08 : 0.68, y: mobile ? 0.64 : 0.18, w: mobile ? 0.84 : 0.25, h: mobile ? 0.22 : 0.36 });
  } else if (item.screen.toLowerCase().includes("puzzle")) {
    base.push({ label: "A", element: "puzzle task area", x: mobile ? 0.04 : 0.2, y: 0.18, w: mobile ? 0.9 : 0.42, h: 0.48 });
  } else if (item.screen.toLowerCase().includes("account")) {
    base.push({ label: "A", element: "sign-in form or account prompt", x: 0.32, y: 0.18, w: 0.36, h: 0.46 });
  } else {
    base.push({ label: "A", element: "primary page heading and hero/task area", x: 0.05, y: 0.12, w: 0.62, h: 0.34 });
    base.push({ label: "B", element: "secondary action or content cards", x: mobile ? 0.06 : 0.56, y: mobile ? 0.48 : 0.44, w: mobile ? 0.86 : 0.36, h: 0.28 });
  }
  return base.slice(0, 3).map((r) => ({
    ...r,
    x: Math.round(r.x * width),
    y: Math.round(r.y * height),
    width: Math.round(r.w * width),
    height: Math.round(r.h * height),
  }));
}

function overlaySvg(width, height, regions) {
  const rects = regions
    .map(
      (r) => `
<rect x="${r.x}" y="${r.y}" width="${r.width}" height="${r.height}" fill="none" stroke="#ff2d20" stroke-width="6"/>
<rect x="${r.x}" y="${Math.max(0, r.y - 34)}" width="34" height="30" fill="#ff2d20"/>
<text x="${r.x + 10}" y="${Math.max(22, r.y - 12)}" fill="white" font-size="22" font-family="Arial" font-weight="700">${r.label}</text>`
    )
    .join("\n");
  return Buffer.from(`<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">${rects}</svg>`);
}

async function annotate(item) {
  const rawPath = path.join(ROOT, item.raw_path);
  if (item.capture_status !== "success" || !fs.existsSync(rawPath)) return item;
  const image = sharp(rawPath);
  const meta = await image.metadata();
  const regions = regionsFor(item, meta.width, meta.height);
  const annotatedRel = rel("assets", "screenshots", "annotated", item.product, path.basename(item.raw_path));
  const cropRel = rel("assets", "screenshots", "crops", item.product, path.basename(item.raw_path).replace(/\.png$/, "_crop_A.png"));
  const annotatedPath = path.join(ROOT, annotatedRel);
  const cropPath = path.join(ROOT, cropRel);
  fs.mkdirSync(path.dirname(annotatedPath), { recursive: true });
  fs.mkdirSync(path.dirname(cropPath), { recursive: true });
  await sharp(rawPath)
    .composite([{ input: overlaySvg(meta.width, meta.height, regions), top: 0, left: 0 }])
    .png({ compressionLevel: 8 })
    .toFile(annotatedPath);
  const first = regions[0];
  const cropBox = {
    left: Math.max(0, first.x - 20),
    top: Math.max(0, first.y - 20),
    width: Math.min(meta.width - Math.max(0, first.x - 20), first.width + 40),
    height: Math.min(meta.height - Math.max(0, first.y - 20), first.height + 40),
  };
  await sharp(rawPath).extract(cropBox).png({ compressionLevel: 8 }).toFile(cropPath);
  const { hci_concept, claim } = pickConcept(item);
  const productName = item.product === "fifa" ? "FIFA.com" : "Chess.com";
  return {
    ...item,
    annotated_path: annotatedRel,
    crop_path: cropRel,
    highlighted_regions: regions.map((r) => ({
      label: r.label,
      element: r.element,
      box: { x: r.x, y: r.y, width: r.width, height: r.height },
      hci_concept,
      claim,
    })),
    hci_concept,
    claim,
    caption: `Figure ${item.figure_id}. ${productName} - ${item.screen}. The highlighted area shows ${regions[0].element}. This matters because ${hci_concept} affects the target persona while ${claim}.`,
  };
}

function solutionSvg(id, title, product, labels) {
  const fill = product === "fifa" ? "#0b4fbd" : "#6b8e23";
  const text = labels
    .map((label, i) => `<text x="72" y="${190 + i * 62}" font-family="Arial" font-size="28" fill="#111">${label}</text>`)
    .join("");
  return Buffer.from(`<svg width="1200" height="720" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" fill="#f7f8fb"/>
<rect x="52" y="52" width="1096" height="86" fill="${fill}"/>
<text x="72" y="106" font-family="Arial" font-size="34" font-weight="700" fill="white">${id}. ${title}</text>
<rect x="72" y="170" width="1056" height="420" rx="8" fill="white" stroke="#c8ccd6" stroke-width="3"/>
${text}
<rect x="72" y="622" width="1056" height="42" fill="#fff3cd" stroke="#d8a300"/>
<text x="92" y="651" font-family="Arial" font-size="24" fill="#111">Visual solution sketch: proposed UI labels are illustrative redesign annotations, not captured live UI.</text>
</svg>`);
}

async function writeSolutionFigures() {
  const solutions = [
    ["S-01", "FIFA task-first navigation", "fifa", ["A. Scores, News, Rankings, Tickets, Watch stay visible", "B. Store, Collect, Rewards move into More FIFA", "C. Mobile menu starts with match tasks"]],
    ["S-02", "FIFA Match Centre filter bar", "fifa", ["A. Today, Live, Results tabs remain sticky", "B. Competition filter opens as a searchable sheet", "C. Selected filters appear as removable chips"]],
    ["S-03", "FIFA article utility rail", "fifa", ["A. Article header links to related match centre", "B. Ticket and watch actions use compact chips", "C. Reader can continue without searching again"]],
    ["S-04", "FIFA+ handoff explainer", "fifa", ["A. Modal states destination and account expectation", "B. Continue and stay controls preserve user control", "C. Breadcrumb keeps FIFA.com return path visible"]],
    ["S-05", "Chess.com beginner home", "chess", ["A. First-run cards: Play, Learn basics, Solve puzzle", "B. Advanced features remain below the fold", "C. Progress chip remembers the user's last goal"]],
    ["S-06", "Chess.com mobile board guard", "chess", ["A. Larger move controls and confirmation option", "B. Clock remains visible without covering board", "C. Clear premove action appears near status area"]],
    ["S-07", "Chess.com beginner analysis preset", "chess", ["A. Beginner, Standard, Expert presets", "B. Plain-language coach note above charts", "C. Glossary explains accuracy and move labels"]],
    ["S-08", "Chess.com learn path", "chess", ["A. One recommended beginner path", "B. Access limits are visible before click", "C. Free alternative appears when a limit is reached"]],
  ];
  const written = [];
  for (const [id, title, product, labels] of solutions) {
    const relPath = rel("assets", "diagrams", `${id.toLowerCase()}_${product}_solution.png`);
    const abs = path.join(ROOT, relPath);
    await sharp(solutionSvg(id, title, product, labels)).png().toFile(abs);
    written.push({ figure_id: id, product, screen: title, annotated_path: relPath, caption: `Figure ${id}. ${title}. This solution sketch maps observed evidence to a proposed HCI improvement.` });
  }
  return written;
}

(async () => {
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, "utf8"));
  const updated = [];
  for (const item of manifest) {
    const result = await annotate(item);
    updated.push(result);
    console.log(`${result.annotated_path ? "ANNOTATED" : "SKIPPED"} ${item.figure_id}`);
  }
  const solutionFigures = await writeSolutionFigures();
  fs.writeFileSync(MANIFEST_PATH, JSON.stringify({ screenshots: updated, solution_figures: solutionFigures }, null, 2), "utf8");
  console.log(`Annotation complete: ${updated.filter((item) => item.annotated_path).length} screenshots annotated; ${solutionFigures.length} solution figures written.`);
})();
