import fs from "node:fs";
import path from "node:path";
import type { ManifestRow } from "./types.js";
import { manifestPath } from "./utils.js";

export const manifestColumns: Array<keyof ManifestRow> = [
  "capture_id",
  "product",
  "viewport",
  "page_area",
  "state",
  "source_url",
  "final_url",
  "page_title",
  "filename",
  "absolute_path",
  "captured_at_local",
  "width_px",
  "height_px",
  "file_size_bytes",
  "document_scroll_width",
  "document_scroll_height",
  "auto_scroll_iterations",
  "reached_bottom",
  "popup_action",
  "authentication_state",
  "status",
  "attempt_count",
  "failure_reason",
  "related_pa1_figure",
  "related_pa1_use_case",
  "notes_factual_only"
];

function csvCell(value: string): string {
  return `"${value.replace(/"/g, "\"\"").replace(/\r?\n/g, " ")}"`;
}

export function ensureManifest(): void {
  fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
  if (!fs.existsSync(manifestPath) || fs.statSync(manifestPath).size === 0) {
    fs.writeFileSync(manifestPath, `${manifestColumns.join(",")}\n`, "utf8");
  }
}

export function appendManifest(row: ManifestRow): void {
  ensureManifest();
  const line = manifestColumns.map((column) => csvCell(String(row[column] ?? ""))).join(",");
  fs.appendFileSync(manifestPath, `${line}\n`, "utf8");
}

export function successfulCaptureIds(): Set<string> {
  if (!fs.existsSync(manifestPath)) {
    return new Set();
  }
  const rows = fs.readFileSync(manifestPath, "utf8").split(/\r?\n/).slice(1);
  const ids = new Set<string>();
  for (const row of rows) {
    const cells = parseCsvLine(row);
    if (cells.length < manifestColumns.length) {
      continue;
    }
    const record = Object.fromEntries(manifestColumns.map((column, index) => [column, cells[index]]));
    if (
      record.status === "SUCCESS" &&
      record.absolute_path &&
      fs.existsSync(record.absolute_path)
    ) {
      ids.add(record.capture_id);
    }
  }
  return ids;
}

export function parseCsvLine(line: string): string[] {
  const cells: string[] = [];
  let value = "";
  let quoted = false;
  for (let index = 0; index < line.length; index += 1) {
    const character = line[index];
    if (character === "\"") {
      if (quoted && line[index + 1] === "\"") {
        value += "\"";
        index += 1;
      } else {
        quoted = !quoted;
      }
    } else if (character === "," && !quoted) {
      cells.push(value);
      value = "";
    } else {
      value += character;
    }
  }
  cells.push(value);
  return cells;
}
