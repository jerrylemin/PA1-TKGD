"""Render PA4 PDFs to PNGs for visual inspection with PyMuPDF."""

from __future__ import annotations

import json
from pathlib import Path

import fitz


PA4 = Path(__file__).resolve().parents[1]
FINAL = PA4 / "final"
OUT = PA4 / "qa" / "pdf-renders"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report = []
    for pdf in sorted(FINAL.glob("*.pdf")):
        target = OUT / pdf.stem
        target.mkdir(parents=True, exist_ok=True)
        document = fitz.open(pdf)
        pages = []
        for index, page in enumerate(document, start=1):
            pixmap = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
            image_path = target / f"page-{index:02d}.png"
            pixmap.save(image_path)
            pages.append({"page": index, "image": str(image_path), "text_chars": len(page.get_text())})
        report.append({"file": str(pdf), "page_count": len(document), "pages": pages})
        document.close()
    (OUT / "render-manifest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
