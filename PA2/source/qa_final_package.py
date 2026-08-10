from __future__ import annotations

import csv
import json
import re
import subprocess
import zipfile
from collections import Counter
from pathlib import Path

import pdfplumber
from PIL import Image, ImageChops, ImageDraw
from docx import Document
from pypdf import PdfReader


ROOT = Path(r"C:\Users\Administrator\Documents\MEGA\tkgd\PA2")
FINAL = ROOT / "final"
SOURCE = ROOT / "source" / "rebuilt"
QA = ROOT / "tmp" / "qa"
POPPLER = Path(
    r"C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime"
    r"\dependencies\native\poppler\Library\bin\pdftoppm.exe"
)
EXPECTED = [
    "Group10-PA2-UserResearch.pdf",
    "Group10-PA2-UserAnalysis.pdf",
    "Group10-PA2-ProjectProposal.pdf",
    "Group10-PA2-UseCaseDocument.pdf",
    "Group10-PA2-PeerReview.pdf",
    "Group10-PA2-WeeklyReport.pdf",
]


def page_ink_ratio(image: Image.Image) -> float:
    rgb = image.convert("RGB")
    white = Image.new("RGB", rgb.size, "white")
    diff = ImageChops.difference(rgb, white).convert("L")
    hist = diff.histogram()
    nonwhite = sum(hist[10:])
    return nonwhite / (rgb.width * rgb.height)


def contact_sheet(images: list[Path], output: Path, cols: int = 4) -> None:
    opened = [Image.open(path).convert("RGB") for path in images]
    thumb_w = 300
    thumb_h = 420
    rows = (len(opened) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (thumb_w + 20) + 20, rows * (thumb_h + 45) + 20), "#D8DEE8")
    draw = ImageDraw.Draw(sheet)
    for i, image in enumerate(opened):
        image.thumbnail((thumb_w, thumb_h))
        x = 20 + (i % cols) * (thumb_w + 20)
        y = 20 + (i // cols) * (thumb_h + 45)
        sheet.paste(image, (x + (thumb_w - image.width) // 2, y))
        draw.text((x, y + thumb_h + 5), f"Page {i+1}", fill="#111827")
    sheet.save(output, dpi=(150, 150))


def docx_media_count(path: Path) -> int:
    with zipfile.ZipFile(path) as archive:
        return len([n for n in archive.namelist() if n.startswith("word/media/")])


def strict_csv_checks() -> dict:
    evidence_schema = [
        "figure_id","product","local_path","visible_page_or_state","supported_claims",
        "unsupported_claims","related_persona","related_task","related_drawback",
        "report_usage","caption",
    ]
    result = {}
    for name, width in (("evidence-index.csv", 11), ("traceability-matrix.csv", 10)):
        path = ROOT / name
        with path.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream, strict=True))
        if not rows or any(len(row) != width for row in rows):
            raise AssertionError(f"{name}: every row must contain exactly {width} fields")
        if name == "evidence-index.csv":
            if rows[0] != evidence_schema:
                raise AssertionError(f"{name}: schema mismatch")
            for row in rows[1:]:
                if Path(row[2]).is_absolute():
                    raise AssertionError(f"{name}: absolute report-facing path: {row[2]}")
                if not (ROOT / row[2]).exists():
                    raise AssertionError(f"{name}: missing local evidence file: {row[2]}")
            f2e19 = next(row for row in rows[1:] if row[0] == "F2-E19")
            if not all(f2e19[index].strip() for index in (8, 9, 10)):
                raise AssertionError("F2-E19: drawback, report usage, and caption must be restored")
        else:
            joined = "\n".join(",".join(row) for row in rows)
            if "All core reports" in joined:
                raise AssertionError("traceability-matrix.csv contains vague report reference")
            if any("§" not in row[-1] for row in rows[1:]):
                raise AssertionError("traceability-matrix.csv requires exact section references")
        result[name] = {"data_rows": len(rows) - 1, "field_count": width}
    return result


def use_case_uniqueness() -> dict:
    doc = Document(SOURCE / "Group10-PA2-UseCaseDocument.docx")
    paragraphs = doc.paragraphs
    starts = [
        (index, re.match(r"^([FC]-UC\d{2})\s+", paragraph.text.strip()).group(1))
        for index, paragraph in enumerate(paragraphs)
        if re.match(r"^([FC]-UC\d{2})\s+", paragraph.text.strip())
    ]
    if len(starts) != 12:
        raise AssertionError(f"Expected 12 use-case headings in DOCX; found {len(starts)}")
    main_blocks, alt_blocks = {}, {}
    for item_index, (start, uid) in enumerate(starts):
        end = starts[item_index + 1][0] if item_index + 1 < len(starts) else len(paragraphs)
        mode = None
        main, alternate = [], []
        for paragraph in paragraphs[start + 1:end]:
            text = re.sub(r"\s+", " ", paragraph.text).strip()
            if text == "Main success scenario":
                mode = "main"
                continue
            if text == "Alternative and exception flows":
                mode = "alternate"
                continue
            if text == "Use-case-specific data, rules, and special requirements":
                mode = None
                continue
            if not text:
                continue
            if mode == "main" and paragraph.style.name.startswith("List Number"):
                main.append(text.casefold())
            elif mode == "alternate" and paragraph.style.name.startswith("List Bullet"):
                alternate.append(text.casefold())
        main_blocks[uid] = " | ".join(main)
        alt_blocks[uid] = " | ".join(alternate)
    main_counts = Counter(main_blocks.values())
    alt_counts = Counter(alt_blocks.values())
    if max(main_counts.values(), default=0) >= 5:
        raise AssertionError("Five or more use cases share the same main scenario wording")
    if max(alt_counts.values(), default=0) >= 5:
        raise AssertionError("Five or more use cases share the same alternate-flow wording")
    if any(not value for value in main_blocks.values()) or any(not value for value in alt_blocks.values()):
        raise AssertionError("Every use case requires a main scenario and alternate/exception flows")
    return {
        "use_cases": len(starts),
        "largest_shared_main_block": max(main_counts.values()),
        "largest_shared_alternate_block": max(alt_counts.values()),
    }


def edge_ink_ratio(image: Image.Image, border: int = 5) -> float:
    rgb = image.convert("RGB")
    strips = [
        rgb.crop((0, 0, rgb.width, border)),
        rgb.crop((0, rgb.height - border, rgb.width, rgb.height)),
        rgb.crop((0, 0, border, rgb.height)),
        rgb.crop((rgb.width - border, 0, rgb.width, rgb.height)),
    ]
    nonwhite = 0
    pixels = 0
    for strip in strips:
        diff = ImageChops.difference(strip, Image.new("RGB", strip.size, "white")).convert("L")
        hist = diff.histogram()
        nonwhite += sum(hist[10:])
        pixels += strip.width * strip.height
    return nonwhite / pixels


def figure_legibility_checks() -> dict:
    crop_dir = ROOT / "generated-diagrams" / "evidence-crops"
    crops = sorted(crop_dir.glob("*.png"))
    if len(crops) < 8:
        raise AssertionError(f"Expected at least 8 readable evidence crops; found {len(crops)}")
    crop_data = []
    for path in crops:
        with Image.open(path) as image:
            aspect = image.width / image.height
            if image.width < 1000 or not 0.8 <= aspect <= 2.2:
                raise AssertionError(f"Unreadable evidence crop geometry: {path.name} {image.size}")
            crop_data.append({"file": path.name, "width": image.width, "height": image.height})
    lowfi = sorted((ROOT / "generated-diagrams").glob("*-lowfi.png"))
    if len(lowfi) != 6:
        raise AssertionError(f"Expected six low-fidelity screen maps; found {len(lowfi)}")
    return {"evidence_crops": crop_data, "lowfi_screen_maps": len(lowfi)}


def write_zip() -> list[str]:
    zip_path = ROOT / "Group10-PA2.zip"
    temp_path = ROOT / "tmp" / "Group10-PA2.rebuilt.zip"
    with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in EXPECTED:
            archive.write(FINAL / name, arcname=name)
    with zipfile.ZipFile(temp_path) as archive:
        names = archive.namelist()
        if names != EXPECTED:
            raise AssertionError(f"ZIP contents/order mismatch: {names}")
    temp_path.replace(zip_path)
    return names


def main() -> None:
    QA.mkdir(parents=True, exist_ok=True)
    csv_results = strict_csv_checks()
    uniqueness = use_case_uniqueness()
    legibility = figure_legibility_checks()
    reports = {}
    all_text = ""
    for name in EXPECTED:
        pdf = FINAL / name
        if not pdf.exists():
            raise FileNotFoundError(pdf)
        text_pages = []
        with pdfplumber.open(pdf) as document:
            for page in document.pages:
                text_pages.append(page.extract_text() or "")
        text = "\n".join(text_pages)
        all_text += "\n" + text
        render_dir = QA / pdf.stem
        render_dir.mkdir(exist_ok=True)
        for stale_page in render_dir.glob("page-*.png"):
            stale_page.unlink()
        prefix = render_dir / "page"
        subprocess.run(
            [str(POPPLER), "-png", "-r", "110", str(pdf), str(prefix)],
            check=True,
            capture_output=True,
        )
        images = sorted(render_dir.glob("page-*.png"))
        ratios = [round(page_ink_ratio(Image.open(path)), 4) for path in images]
        edge_ratios = [round(edge_ink_ratio(Image.open(path)), 5) for path in images]
        contact_sheet(images, QA / f"{pdf.stem}-contact.png")
        reports[name] = {
            "pages": len(PdfReader(str(pdf)).pages),
            "selectable_text_chars": len(text),
            "figure_caption_count": len(re.findall(r"\bFigure\s+[A-Z0-9-]+\.", text)),
            "diagram_caption_count": len(re.findall(r"\b(?:WM-|UC-|PP-)", text)),
            "use_case_heading_count": len(set(re.findall(r"\b[FC]-UC\d{2}\b", text))),
            "absolute_local_path_hits": sorted(set(re.findall(r"[A-Z]:\\Users\\[^\n]+", text))),
            "blank_page_candidates": [i + 1 for i, ratio in enumerate(ratios) if ratio < 0.003],
            "edge_ink_candidates": [i + 1 for i, ratio in enumerate(edge_ratios) if ratio > 0.01],
            "ink_ratios": ratios,
            "edge_ink_ratios": edge_ratios,
            "docx_media_count": docx_media_count(SOURCE / name.replace(".pdf", ".docx")),
        }
        (QA / f"{pdf.stem}.txt").write_text(text, encoding="utf-8")

    forbidden_terms = {
        r"C:\Users\\": bool(re.search(r"C:\\Users\\", all_text)),
        "Awaiting": "Awaiting" in all_text,
        "PARTIAL": "PARTIAL" in all_text,
        "To be verified": "To be verified" in all_text,
        "GroupID": "GroupID" in all_text,
        "placeholder": bool(re.search(r"\bplaceholder\b", all_text, re.I)),
        "generic copied scenario": "System presents the current context, provenance, and primary action." in all_text,
        "submission-ready": "submission-ready" in all_text.lower(),
    }
    if any(forbidden_terms.values()):
        raise AssertionError(f"Forbidden final-PDF text found: {[key for key,value in forbidden_terms.items() if value]}")
    incomplete_reports = {
        name: "INCOMPLETE" in (QA / f"{Path(name).stem}.txt").read_text(encoding="utf-8")
        for name in EXPECTED
    }
    allowed_incomplete = {
        "Group10-PA2-UserAnalysis.pdf",
        "Group10-PA2-PeerReview.pdf",
        "Group10-PA2-WeeklyReport.pdf",
    }
    if {name for name, value in incomplete_reports.items() if value} != allowed_incomplete:
        raise AssertionError(f"INCOMPLETE labels do not match evidence blockers: {incomplete_reports}")
    if any(report["blank_page_candidates"] for report in reports.values()):
        raise AssertionError("Blank-page candidate detected")
    if any(report["edge_ink_candidates"] for report in reports.values()):
        raise AssertionError("Possible clipping detected at rendered page edge")
    if any(report["absolute_local_path_hits"] for report in reports.values()):
        raise AssertionError("Absolute local path detected in final PDF")
    required = {
        "group10": all("Group10" in (QA / f"{Path(n).stem}.txt").read_text(encoding="utf-8") for n in EXPECTED),
        "student_ids": all(sid in all_text for sid in ("21127645", "21127224", "20127119", "22127318")),
        "evidence_blockers_visible": all(incomplete_reports[name] for name in allowed_incomplete),
        "twelve_use_cases": reports["Group10-PA2-UseCaseDocument.pdf"]["use_case_heading_count"] == 12,
        "three_fifa_concepts": all(cid in all_text for cid in ("F-A1", "F-A2", "F-A3")),
        "three_chess_concepts": all(cid in all_text for cid in ("C-A1", "C-A2", "C-A3")),
        "lecture_citations": all(label in all_text for label in ("LN01", "LN02", "LN03", "LN04")),
        "uml_system_boundaries": all(label in all_text for label in ("FIFA UML use-case diagram", "Chess UML use-case diagram")),
        "flow_model_label": "flow model" in all_text.lower(),
    }
    if not all(required.values()):
        raise AssertionError(f"Required content check failed: {required}")
    zip_contents = write_zip()
    result = {
        "csv_validation": csv_results,
        "reports": reports,
        "forbidden": forbidden_terms,
        "required": required,
        "incomplete_justification": incomplete_reports,
        "use_case_uniqueness": uniqueness,
        "figure_legibility": legibility,
        "zip_contents": zip_contents,
    }
    (QA / "qa-results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
