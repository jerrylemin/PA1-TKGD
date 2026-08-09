import fs from "node:fs";
import path from "node:path";
import { imageSize } from "image-size";
import { allCaptureTargets } from "./capture-plan.js";
import { manifestColumns, parseCsvLine } from "./manifest.js";
import type { ManifestRow } from "./types.js";
import {
  captureWorkRoot,
  localTimestamp,
  manifestPath,
  summaryPath,
  urlsPath
} from "./utils.js";

const pngSignature = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function readManifest(): ManifestRow[] {
  if (!fs.existsSync(manifestPath)) {
    throw new Error(`Manifest does not exist: ${manifestPath}`);
  }
  const lines = fs.readFileSync(manifestPath, "utf8").split(/\r?\n/).filter(Boolean);
  const header = parseCsvLine(lines[0]);
  if (header.join(",") !== manifestColumns.join(",")) {
    throw new Error("Manifest header does not match the required columns.");
  }
  return lines.slice(1).map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(
      manifestColumns.map((column, index) => [column, cells[index] ?? ""])
    ) as ManifestRow;
  });
}

function enumerateCapturePngs(): string[] {
  const roots = [
    path.join(captureWorkRoot, "fifa"),
    path.join(captureWorkRoot, "chess"),
    path.join(captureWorkRoot, "failed")
  ];
  const results: string[] = [];
  const visit = (directory: string) => {
    if (!fs.existsSync(directory)) {
      return;
    }
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        visit(fullPath);
      } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".png")) {
        results.push(path.resolve(fullPath));
      }
    }
  };
  roots.forEach(visit);
  return results;
}

function countPdfPages(): number {
  const root = path.join(captureWorkRoot, "rendered-pdfs");
  if (!fs.existsSync(root)) {
    return 0;
  }
  let count = 0;
  const visit = (directory: string) => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        visit(fullPath);
      } else if (/^page-\d+\.png$/i.test(entry.name)) {
        count += 1;
      }
    }
  };
  visit(root);
  return count;
}

function countPdfFilesProcessed(): number {
  const root = path.join(captureWorkRoot, "extracted-text");
  return fs.existsSync(root)
    ? fs.readdirSync(root).filter((name) => name.toLowerCase().endsWith(".txt")).length
    : 0;
}

const rows = readManifest();
const failures: string[] = [];
const captureIds = new Set<string>();
const filenames = new Set<string>();
const manifestImages = new Set<string>();
const validImages = new Set<string>();

for (const row of rows) {
  if (captureIds.has(row.capture_id)) {
    failures.push(`Duplicate capture ID: ${row.capture_id}`);
  }
  captureIds.add(row.capture_id);

  if (row.filename) {
    const normalizedFilename = row.filename.toLowerCase();
    if (filenames.has(normalizedFilename)) {
      failures.push(`Duplicate filename: ${row.filename}`);
    }
    filenames.add(normalizedFilename);
  }

  if (row.absolute_path) {
    const absolutePath = path.resolve(row.absolute_path);
    manifestImages.add(absolutePath);
    if (!path.isAbsolute(row.absolute_path)) {
      failures.push(`Path is not absolute: ${row.absolute_path}`);
    }
    if (path.extname(row.absolute_path).toLowerCase() !== ".png") {
      failures.push(`Capture extension is not PNG: ${row.absolute_path}`);
    }
    if (!fs.existsSync(absolutePath)) {
      failures.push(`Capture file does not exist: ${absolutePath}`);
      continue;
    }
    const stat = fs.statSync(absolutePath);
    if (stat.size <= 0) {
      failures.push(`Capture file is empty: ${absolutePath}`);
      continue;
    }
    const buffer = fs.readFileSync(absolutePath);
    if (!buffer.subarray(0, 8).equals(pngSignature)) {
      failures.push(`Invalid PNG signature: ${absolutePath}`);
      continue;
    }
    try {
      const dimensions = imageSize(buffer);
      const width = dimensions.width ?? 0;
      const height = dimensions.height ?? 0;
      if (width <= 0 || height <= 0) {
        failures.push(`Invalid image dimensions: ${absolutePath}`);
        continue;
      }
      if (String(width) !== row.width_px || String(height) !== row.height_px) {
        failures.push(`Manifest dimensions differ from PNG: ${absolutePath}`);
      }
      const documentHeight = Number(row.document_scroll_height || 0);
      if (
        (row.status === "SUCCESS" || row.status === "PARTIAL") &&
        documentHeight > 0 &&
        height + 4 < documentHeight
      ) {
        failures.push(
          `Image height ${height} is below document height ${documentHeight}: ${absolutePath}`
        );
      }
      validImages.add(absolutePath);
    } catch (error) {
      failures.push(
        `Unable to read PNG dimensions: ${absolutePath}: ${
          error instanceof Error ? error.message : String(error)
        }`
      );
    }
  } else if (row.status === "SUCCESS") {
    failures.push(`SUCCESS row has no file: ${row.capture_id}`);
  }
}

for (const target of allCaptureTargets) {
  if (!captureIds.has(target.captureId)) {
    failures.push(`Planned capture has no manifest row: ${target.captureId}`);
  }
}

for (const imagePath of enumerateCapturePngs()) {
  if (!manifestImages.has(imagePath)) {
    failures.push(`PNG exists outside manifest: ${imagePath}`);
  }
}

for (const imagePath of manifestImages) {
  if (!enumerateCapturePngs().includes(imagePath)) {
    failures.push(`Manifest image is outside capture output folders: ${imagePath}`);
  }
}

const uniqueAttempted = new Set(rows.map((row) => row.capture_id));
const urlsDiscovered = fs.existsSync(urlsPath)
  ? fs.readFileSync(urlsPath, "utf8").split(/\r?\n/).filter(Boolean).length
  : 0;
const timestamps = rows.map((row) => row.captured_at_local).filter(Boolean).sort();
const statusCount = (status: ManifestRow["status"]) =>
  rows.filter((row) => row.status === status).length;
const screenshotRows = rows.filter((row) => row.absolute_path && validImages.has(path.resolve(row.absolute_path)));

const summary = {
  pdfFilesProcessed: countPdfFilesProcessed(),
  pdfPagesRendered: countPdfPages(),
  urlsDiscovered,
  targetsPlanned: allCaptureTargets.length,
  targetsAttempted: uniqueAttempted.size,
  screenshotsSuccessful: statusCount("SUCCESS"),
  screenshotsPartial: statusCount("PARTIAL"),
  screenshotsBlocked: statusCount("BLOCKED"),
  statesMissing: statusCount("MISSING_CURRENT_STATE"),
  screenshotsFailed: statusCount("FAILED"),
  desktopScreenshots: screenshotRows.filter((row) => row.viewport === "desktop").length,
  mobileScreenshots: screenshotRows.filter((row) => row.viewport === "mobile").length,
  startedAt: timestamps[0] ?? "",
  completedAt: localTimestamp(),
  outputDirectory: captureWorkRoot
};

fs.writeFileSync(summaryPath, `${JSON.stringify(summary, null, 2)}\n`, "utf8");

if (failures.length) {
  process.stderr.write(`VERIFICATION FAILED (${failures.length} issue(s))\n`);
  for (const failure of failures) {
    process.stderr.write(`- ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write(
    `VERIFICATION PASSED\nRows: ${rows.length}\nImages: ${validImages.size}\nSummary: ${summaryPath}\n`
  );
}
