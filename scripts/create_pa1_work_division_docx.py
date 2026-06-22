from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
DOCS_DIR = ROOT / "docs"
OUT_DOCX = OUTPUT_DIR / "GroupID-PA1-WorkDivision.docx"
ROOT_DOCX = ROOT / "GroupID-PA1-WorkDivision.docx"
LOG_PATH = DOCS_DIR / "pa1_work_division_generation_log.md"
ROOT_COPY_STATUS = {"copied": False, "error": ""}

MEMBERS = [
    ("Le Minh", "21127645"),
    ("Nguyen Vu Bach", "21127224"),
    ("Pham Nguyen Gia Bao", "20127119"),
    ("Trang Minh Nhut", "22127318"),
]


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_width(cell, width_dxa: int) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn("w:tcW"))
    if tc_w is None:
        tc_w = OxmlElement("w:tcW")
        tc_pr.append(tc_w)
    tc_w.set(qn("w:w"), str(width_dxa))
    tc_w.set(qn("w:type"), "dxa")


def set_cell_margins(cell, top=80, start=120, bottom=80, end=120) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.find(qn("w:tcMar"))
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table, color="8A8F98", size="6") -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.find(qn("w:tblBorders"))
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = f"w:{edge}"
        element = borders.find(qn(tag))
        if element is None:
            element = OxmlElement(tag)
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:space"), "0")
        element.set(qn("w:color"), color)


def set_table_width(table, widths_dxa: list[int]) -> None:
    table.autofit = False
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_pr = table._tbl.tblPr
    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(sum(widths_dxa)))
    tbl_w.set(qn("w:type"), "dxa")

    tbl_ind = tbl_pr.find(qn("w:tblInd"))
    if tbl_ind is None:
        tbl_ind = OxmlElement("w:tblInd")
        tbl_pr.append(tbl_ind)
    tbl_ind.set(qn("w:w"), "120")
    tbl_ind.set(qn("w:type"), "dxa")

    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in widths_dxa:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)

    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            set_cell_width(cell, widths_dxa[idx])
            set_cell_margins(cell)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER


def style_cell_text(cell, bold=False, color="000000", size=9) -> None:
    for paragraph in cell.paragraphs:
        paragraph.paragraph_format.space_after = Pt(0)
        paragraph.paragraph_format.line_spacing = 1.05
        for run in paragraph.runs:
            run.font.name = "Calibri"
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = RGBColor.from_string(color)


def add_table(doc: Document, headers: list[str], rows: list[list[str]], widths: list[int]):
    table = doc.add_table(rows=1, cols=len(headers))
    set_table_borders(table)
    hdr = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr[i].text = header
        set_cell_shading(hdr[i], "F2F4F7")
        style_cell_text(hdr[i], bold=True, color="0B2545", size=9)
    for row_data in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row_data):
            cells[i].text = str(value)
            style_cell_text(cells[i], size=8.6)
    set_table_width(table, widths)
    doc.add_paragraph()
    return table


def add_heading(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    p.style = doc.styles["Heading 1"]
    p.add_run(text)


def add_body(doc: Document, text: str) -> None:
    p = doc.add_paragraph(text)
    p.style = doc.styles["Normal"]


def add_bullets(doc: Document, items: list[str]) -> None:
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item)


def add_page_break_heading(doc: Document, text: str) -> None:
    doc.add_page_break()
    add_heading(doc, text)


def configure_document(doc: Document) -> None:
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Inches(1)
    section.right_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.header_distance = Inches(0.49)
    section.footer_distance = Inches(0.49)

    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.10

    h1 = styles["Heading 1"]
    h1.font.name = "Calibri"
    h1.font.size = Pt(13)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor(46, 116, 181)
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(6)

    for style_name in ("List Bullet", "List Number"):
        style = styles[style_name]
        style.font.name = "Calibri"
        style.font.size = Pt(11)
        style.paragraph_format.space_after = Pt(4)
        style.paragraph_format.line_spacing = 1.10

    header = section.header.paragraphs[0]
    header.text = "PA1 Work Division"
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in header.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(85, 85, 85)

    footer = section.footer.paragraphs[0]
    footer.text = "FIFA.com and Chess.com HCI Project"
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in footer.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(85, 85, 85)


def build_docx() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)

    doc = Document()
    configure_document(doc)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_after = Pt(3)
    run = title.add_run("PA1 Work Division")
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.paragraph_format.space_after = Pt(12)
    run = subtitle.add_run("ProductResearch Work Division for FIFA.com and Chess.com")
    run.font.name = "Calibri"
    run.font.size = Pt(12)

    add_heading(doc, "1. Project objective")
    add_body(
        doc,
        "The group will complete only the ProductResearch part of PA1 by researching FIFA.com and Chess.com "
        "from HCI and UX perspectives. The work includes product overview, target users, personas, use cases, "
        "screenshot evidence, HCI findings, benefits, drawbacks, source citation, cross-product comparison, "
        "and final QA for GroupID-PA1-ProductResearch.pdf.",
    )

    add_heading(doc, "2. Team members")
    add_table(
        doc,
        ["No.", "Member", "Student ID", "Main role", "Supporting role"],
        [
            ["1", "Le Minh", "21127645", "FIFA.com ProductResearch Co-Lead", "Writing, source check, peer review within ProductResearch, and final QA"],
            ["2", "Nguyen Vu Bach", "21127224", "FIFA.com ProductResearch Co-Lead", "Writing, source check, peer review within ProductResearch, and final QA"],
            ["3", "Pham Nguyen Gia Bao", "20127119", "Chess.com ProductResearch Co-Lead", "Writing, source check, peer review within ProductResearch, and final QA"],
            ["4", "Trang Minh Nhut", "22127318", "Chess.com ProductResearch Co-Lead", "Writing, source check, peer review within ProductResearch, and final QA"],
        ],
        [600, 1900, 1200, 3000, 2660],
    )

    add_heading(doc, "3. General responsibility division")
    add_table(
        doc,
        ["Member", "Main responsibilities", "Supporting responsibilities", "Expected outputs"],
        [
            [
                "Le Minh",
                "Research FIFA.com together with Nguyen Vu Bach; collect sources and screenshot evidence; write FIFA.com product overview, users, personas, use cases, benefits, drawbacks, and HCI findings.",
                "Review Chess.com ProductResearch sections; check citations, screenshot captions, and comparison consistency.",
                "FIFA.com research content; FIFA.com screenshot notes; ProductResearch writing; review comments; ProductResearch QA checklist item.",
            ],
            [
                "Nguyen Vu Bach",
                "Research FIFA.com together with Le Minh; collect sources and screenshot evidence; write FIFA.com product overview, users, personas, use cases, benefits, drawbacks, and HCI findings.",
                "Review Chess.com ProductResearch sections; check citations, screenshot captions, and comparison consistency.",
                "FIFA.com research content; FIFA.com screenshot notes; ProductResearch writing; review comments; ProductResearch QA checklist item.",
            ],
            [
                "Pham Nguyen Gia Bao",
                "Research Chess.com together with Trang Minh Nhut; collect sources and screenshot evidence; write Chess.com product overview, users, personas, use cases, benefits, drawbacks, and HCI findings.",
                "Review FIFA.com ProductResearch sections; check citations, screenshot captions, and comparison consistency.",
                "Chess.com research content; Chess.com screenshot notes; ProductResearch writing; review comments; ProductResearch QA checklist item.",
            ],
            [
                "Trang Minh Nhut",
                "Research Chess.com together with Pham Nguyen Gia Bao; collect sources and screenshot evidence; write Chess.com product overview, users, personas, use cases, benefits, drawbacks, and HCI findings.",
                "Review FIFA.com ProductResearch sections; check citations, screenshot captions, and comparison consistency.",
                "Chess.com research content; Chess.com screenshot notes; ProductResearch writing; review comments; ProductResearch QA checklist item.",
            ],
        ],
        [1550, 3200, 2500, 2110],
    )

    add_page_break_heading(doc, "4. ProductResearch ownership")
    add_table(
        doc,
        ["ProductResearch part", "Assigned product", "Main members", "Cross-review members", "Required contribution"],
        [
            ["Product overview and source log", "FIFA.com", "Le Minh, Nguyen Vu Bach", "Pham Nguyen Gia Bao, Trang Minh Nhut", "Official sources, product purpose, target users, main HCI touchpoints"],
            ["Product overview and source log", "Chess.com", "Pham Nguyen Gia Bao, Trang Minh Nhut", "Le Minh, Nguyen Vu Bach", "Official sources, product purpose, target users, main HCI touchpoints"],
            ["Personas and use cases", "FIFA.com", "Le Minh, Nguyen Vu Bach", "Pham Nguyen Gia Bao, Trang Minh Nhut", "FIFA.com personas, realistic user goals, task flows, context, preconditions, feedback"],
            ["Personas and use cases", "Chess.com", "Pham Nguyen Gia Bao, Trang Minh Nhut", "Le Minh, Nguyen Vu Bach", "Chess.com personas, realistic user goals, task flows, context, preconditions, feedback"],
            ["HCI findings, benefits, drawbacks", "Both products", "All members by assigned product", "Opposite product pair", "Concrete HCI concepts, screenshots, benefits, drawbacks, and comparison notes for ProductResearch only"],
        ],
        [1650, 2200, 2050, 1900, 1560],
    )

    add_heading(doc, "5. Workload balance summary")
    add_table(
        doc,
        ["Work category", "Le Minh", "Nguyen Vu Bach", "Pham Nguyen Gia Bao", "Trang Minh Nhut"],
        [
            ["Project coordination", "Shared", "Shared", "Shared", "Shared"],
            ["FIFA.com research", "Co-lead", "Co-lead", "Cross-review", "Cross-review"],
            ["Chess.com research", "Cross-review", "Cross-review", "Co-lead", "Co-lead"],
            ["Screenshot collection", "FIFA.com screenshots", "FIFA.com screenshots", "Chess.com screenshots", "Chess.com screenshots"],
            ["Personas and use cases", "FIFA.com personas/use cases", "FIFA.com personas/use cases", "Chess.com personas/use cases", "Chess.com personas/use cases"],
            ["HCI findings", "FIFA.com HCI findings", "FIFA.com HCI findings", "Chess.com HCI findings", "Chess.com HCI findings"],
            ["Benefits and drawbacks", "FIFA.com benefits/drawbacks", "FIFA.com benefits/drawbacks", "Chess.com benefits/drawbacks", "Chess.com benefits/drawbacks"],
            ["Cross-product comparison", "FIFA.com comparison input", "FIFA.com comparison input", "Chess.com comparison input", "Chess.com comparison input"],
            ["ProductResearch review", "Review Chess.com section", "Review Chess.com section", "Review FIFA.com section", "Review FIFA.com section"],
            ["ProductResearch QA", "Citation and formatting check", "Citation and formatting check", "Screenshot and HCI consistency check", "Screenshot and HCI consistency check"],
        ],
        [2050, 1800, 1900, 1900, 1710],
    )

    add_page_break_heading(doc, "6. RACI matrix")
    add_body(doc, "Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.")
    add_table(
        doc,
        ["Task", "Le Minh", "Nguyen Vu Bach", "Pham Nguyen Gia Bao", "Trang Minh Nhut"],
        [
            ["ProductResearch scope and checklist", "R", "R", "R", "R"],
            ["FIFA.com research", "A/R", "A/R", "C", "C"],
            ["Chess.com research", "C", "C", "A/R", "A/R"],
            ["Screenshot evidence", "A/R for FIFA.com", "A/R for FIFA.com", "A/R for Chess.com", "A/R for Chess.com"],
            ["Personas and use cases", "A/R for FIFA.com", "A/R for FIFA.com", "A/R for Chess.com", "A/R for Chess.com"],
            ["HCI analysis", "A/R for FIFA.com", "A/R for FIFA.com", "A/R for Chess.com", "A/R for Chess.com"],
            ["ProductResearch report", "R", "R", "R", "R"],
            ["Cross-product comparison", "R", "R", "R", "R"],
            ["ProductResearch final QA", "R", "R", "R", "R"],
        ],
        [2600, 1500, 1900, 1900, 1460],
    )

    add_heading(doc, "7. Expected contribution from each member")
    contributions = {
        "Le Minh": "Responsible for the FIFA.com side together with Nguyen Vu Bach. He collects sources, screenshots, personas, use cases, HCI findings, benefits, drawbacks, comparison input, section writing, cross-review, and ProductResearch QA checks.",
        "Nguyen Vu Bach": "Responsible for the FIFA.com side together with Le Minh. He collects sources, screenshots, personas, use cases, HCI findings, benefits, drawbacks, comparison input, section writing, cross-review, and ProductResearch QA checks.",
        "Pham Nguyen Gia Bao": "Responsible for the Chess.com side together with Trang Minh Nhut. He collects sources, screenshots, personas, use cases, HCI findings, benefits, drawbacks, comparison input, section writing, cross-review, and ProductResearch QA checks.",
        "Trang Minh Nhut": "Responsible for the Chess.com side together with Pham Nguyen Gia Bao. He collects sources, screenshots, personas, use cases, HCI findings, benefits, drawbacks, comparison input, section writing, cross-review, and ProductResearch QA checks.",
    }
    for member, text in contributions.items():
        p = doc.add_paragraph()
        p.add_run(f"{member}: ").bold = True
        p.add_run(text)

    add_page_break_heading(doc, "8. Quality checklist")
    checklist = [
        "Product pair is FIFA.com and Chess.com.",
        "FIFA.com has exactly 2 research members: Le Minh and Nguyen Vu Bach.",
        "Chess.com has exactly 2 research members: Pham Nguyen Gia Bao and Trang Minh Nhut.",
        "All 4 members have clear responsibilities.",
        "No member has only minor tasks.",
        "ProductResearch has both products.",
        "ProductResearch has users, personas, use cases, screenshots, HCI findings, benefits, drawbacks, and comparison.",
        "Each website has product overview, source evidence, personas, use cases, HCI findings, benefits, drawbacks, and screenshots.",
        "Each member has research, writing, review, and ProductResearch QA responsibilities.",
        "Only GroupID-PA1-ProductResearch.pdf is divided in this document.",
    ]
    for item in checklist:
        p = doc.add_paragraph()
        p.style = doc.styles["Normal"]
        p.add_run("\u2610 ").font.size = Pt(11)
        p.add_run(item)

    add_heading(doc, "9. Signature table")
    add_table(
        doc,
        ["Member", "Student ID", "Confirmed responsibilities", "Signature"],
        [[name, sid, "Confirmed", ""] for name, sid in MEMBERS],
        [2300, 1500, 3100, 2460],
    )

    doc.save(OUT_DOCX)
    try:
        shutil.copy2(OUT_DOCX, ROOT_DOCX)
        ROOT_COPY_STATUS["copied"] = True
    except PermissionError as exc:
        ROOT_COPY_STATUS["copied"] = False
        ROOT_COPY_STATUS["error"] = str(exc)


def validate_docx(path: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "size": 0,
            "size_gt_10kb": False,
            "required_terms_ok": False,
            "balanced_research_ok": False,
            "no_detailed_timeline": False,
            "table_count": 0,
        }
    doc = Document(path)
    text = "\n".join(p.text for p in doc.paragraphs)
    for table in doc.tables:
        for row in table.rows:
            text += "\n" + "\t".join(cell.text for cell in row.cells)
    required = [
        "PA1 Work Division",
        "Le Minh",
        "Nguyen Vu Bach",
        "Pham Nguyen Gia Bao",
        "Trang Minh Nhut",
        "21127645",
        "21127224",
        "20127119",
        "22127318",
        "RACI matrix",
        "Quality checklist",
        "FIFA.com has exactly 2 research members",
        "Chess.com has exactly 2 research members",
    ]
    forbidden = ["14-day", "day-by-day", "Day 1", "Day 14"]
    return {
        "path": str(path),
        "exists": path.exists(),
        "size": path.stat().st_size if path.exists() else 0,
        "size_gt_10kb": path.exists() and path.stat().st_size > 10_000,
        "required_terms_ok": all(term in text for term in required),
        "balanced_research_ok": all(
            term in text
            for term in [
                "FIFA.com has exactly 2 research members: Le Minh and Nguyen Vu Bach.",
                "Chess.com has exactly 2 research members: Pham Nguyen Gia Bao and Trang Minh Nhut.",
                "FIFA.com ProductResearch Co-Lead",
                "Chess.com ProductResearch Co-Lead",
                "Only GroupID-PA1-ProductResearch.pdf is divided in this document.",
            ]
        ),
        "no_detailed_timeline": not any(term in text for term in forbidden),
        "table_count": len(doc.tables),
    }


def write_log(results: list[dict[str, object]]) -> None:
    cwd = ROOT
    lines = [
        "# PA1 Work Division Generation Log",
        "",
        f"Generated at: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Phase 0 inspection",
        f"- Current working directory: `{cwd}`",
        "- Repository tree listed to depth 3.",
        "- Existing folders checked: `docs` exists; `output` created if missing; no `reports` or `deliverables` folder required for this task.",
        "- Python check: bundled Codex Python 3.12.13.",
        "- python-docx check: OK.",
        "- Design preset: `standard_business_brief`, with A4 page-size override required by the user.",
        "",
        "## Generation actions",
        "- Created `output/GroupID-PA1-WorkDivision.docx`.",
        f"- Root copy status for `GroupID-PA1-WorkDivision.docx`: {ROOT_COPY_STATUS['copied']}.",
        f"- Root copy error: {ROOT_COPY_STATUS['error'] or 'None'}.",
        "- Applied A4 page size, normal margins, centered title/subtitle, bold section headings, visible table borders, header, footer, and required page breaks.",
        "- Updated assignment model: this document divides only `GroupID-PA1-ProductResearch.pdf`.",
        "- Le Minh + Nguyen Vu Bach are FIFA.com ProductResearch co-leads; Pham Nguyen Gia Bao + Trang Minh Nhut are Chess.com ProductResearch co-leads.",
        "- Each member now has matching ProductResearch research, writing, cross-review, and QA responsibilities.",
        "",
        "## Validation results",
    ]
    for result in results:
        lines.extend(
            [
                f"### {result['path']}",
                f"- Exists: {result['exists']}",
                f"- Size: {result['size']} bytes",
                f"- Size > 10 KB: {result['size_gt_10kb']}",
                f"- Required title/member/RACI/checklist terms present: {result['required_terms_ok']}",
                f"- Balanced 2-member-per-website research assignment present: {result['balanced_research_ok']}",
                f"- No detailed day-by-day or 14-day plan terms: {result['no_detailed_timeline']}",
                f"- Table count: {result['table_count']}",
                "",
            ]
        )
    LOG_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    build_docx()
    results = [validate_docx(OUT_DOCX), validate_docx(ROOT_DOCX)]
    write_log(results)
    for result in results:
        print(result)
    output_result = results[0]
    if not (
        output_result["exists"]
        and output_result["size_gt_10kb"]
        and output_result["required_terms_ok"]
        and output_result["balanced_research_ok"]
        and output_result["no_detailed_timeline"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
