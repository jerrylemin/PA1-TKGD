from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import re
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "pa1_config.json"
REPORT_NAMES = ("ProductResearch", "PotentialSolutions", "PeerReview", "WeeklyReport")
MEMBERS = (
    ("Le Minh", "21127645"),
    ("Nguyen Vu Bach", "21127224"),
    ("Pham Nguyen Gia Bao", "20127119"),
    ("Trang Minh Nhut", "22127318"),
)
GROUP_BLOCKER = "Real group ID is not provided. Replace GroupID before final Moodle submission if the course assigned a real ID."
PEER_BLOCKERS = (
    "Real peer-review feedback after lecture presentation is required before final PeerReview submission.",
    "Real peer feedback is missing. Fill this section after lecture presentation.",
)
OLD_PRODUCTS = ("Strava", "Nike Run Club", "Garmin Connect", "Forerunner", "smartwatch")
GENERIC_MEMBERS = ("Member1", "Member2", "Member3", "Member4", "Member5")

CANONICAL = {
    "F-D1": ("Ecosystem sprawl across sibling FIFA properties", "F-HCI6", ("F-S1", "F-S2"), "F", ("ecosystem", "sibling", "cross-property")),
    "F-D2": ("FIFA+ handoff breaks continuity", "F-HCI7", ("F-S3", "F-S4"), "F", ("fifa+", "handoff", "dazn", "continuity")),
    "F-D3": ("FIFA+ scan overload", "F-HCI8", ("F-S5", "F-S6"), "F", ("fifa+", "rail", "media", "watch")),
    "F-D4": ("Ticket status uncertainty", "F-HCI9", ("F-S7", "F-S8"), "F", ("ticket", "sale", "resale", "waiting", "availability")),
    "F-D5": ("Browse-first friction for quick utilitarian tasks", "F-HCI10", ("F-S9", "F-S10"), "F", ("article", "story", "utilitarian", "score", "ticket", "watch")),
    "C-D1": ("Menu and feature overload for novices", "C-HCI7", ("C-S1", "C-S2"), "C", ("menu", "feature", "novice", "beginner")),
    "C-D2": ("Analysis overload", "C-HCI10", ("C-S3", "C-S4"), "C", ("analysis", "chart", "line", "label", "review")),
    "C-D3": ("Premium gating interrupts learning momentum", "C-HCI10", ("C-S5", "C-S6"), "C", ("premium", "gat", "limit", "access", "learning")),
    "C-D4": ("Premove blunder risk", "C-HCI8", ("C-S7", "C-S8"), "C", ("premove", "blunder")),
    "C-D5": ("Focus Mode is hard to discover", "C-HCI9", ("C-S9", "C-S10"), "C", ("focus mode", "discover", "hover")),
}


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def markdown_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    lines = text.splitlines()
    index = 0
    while index + 1 < len(lines):
        if lines[index].lstrip().startswith("|") and re.match(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$", lines[index + 1]):
            header = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            tables.append((header, rows))
            continue
        index += 1
    return tables


def bounded_section(text: str, start: str, later_starts: tuple[str, ...]) -> str:
    pos = text.find(start)
    if pos < 0:
        return ""
    end = len(text)
    for marker in later_starts:
        candidate = text.find(marker, pos + len(start))
        if candidate >= 0:
            end = min(end, candidate)
    return text[pos:end]


def install_pdf_backend() -> tuple[bool, str]:
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--disable-pip-version-check", "pypdf"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120,
        )
        importlib.invalidate_caches()
        return True, "installed pypdf in the active Python environment"
    except Exception as exc:  # pragma: no cover - environment dependent
        return False, f"could not install pypdf safely: {exc}"


def pdf_extractor() -> tuple[Callable[[Path], str] | None, str]:
    try:
        from pypdf import PdfReader

        return lambda path: "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages), "pypdf"
    except ImportError:
        pass
    try:
        import pdfplumber

        def extract_plumber(path: Path) -> str:
            with pdfplumber.open(path) as document:
                return "\n".join(page.extract_text() or "" for page in document.pages)

        return extract_plumber, "pdfplumber"
    except ImportError:
        pass
    try:
        import fitz

        def extract_fitz(path: Path) -> str:
            with fitz.open(path) as document:
                return "\n".join(page.get_text() for page in document)

        return extract_fitz, "PyMuPDF"
    except ImportError:
        installed, detail = install_pdf_backend()
        if installed:
            try:
                from pypdf import PdfReader

                return lambda path: "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages), detail
            except ImportError:
                pass
        return None, detail


class Validator:
    def __init__(self, mode: str) -> None:
        self.mode = mode
        self.checks: list[Check] = []
        self.config: dict[str, str] = {}
        self.group_id = "GroupID"
        self.sources: dict[str, Path] = {}
        self.pdfs: dict[str, Path] = {}
        self.pdf_text: dict[str, str] = {}

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks.append(Check(name, bool(ok), detail))

    def load_config(self) -> None:
        if not CONFIG_PATH.is_file():
            self.add("Config exists", False, str(CONFIG_PATH.relative_to(ROOT)))
            return
        try:
            value = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception as exc:
            self.add("Config is valid JSON", False, str(exc))
            return
        required = {
            "group_id", "github_repo", "weekly_scrum_doc_link", "sprint_planning_doc_link",
            "sprint_review_doc_link", "google_drive_folder_link", "zoom_link",
        }
        missing = sorted(required - value.keys())
        self.add("Config schema", not missing, "missing: " + ", ".join(missing) if missing else "all required keys present")
        self.config = value
        configured = str(value.get("group_id", "")).strip()
        safe = bool(re.fullmatch(r"[A-Za-z0-9_-]+", configured))
        self.add("Group ID is filename-safe", safe, repr(configured))
        if safe:
            self.group_id = configured
        self.sources = {name: ROOT / "sources" / f"{self.group_id}-PA1-{name}.md" for name in REPORT_NAMES}
        self.pdfs = {name: ROOT / f"{self.group_id}-PA1-{name}.pdf" for name in REPORT_NAMES}

    def check_required_files(self) -> None:
        paths = [ROOT / "build_pa1_package.py", CONFIG_PATH, ROOT / "artifact_manifest.json", *self.sources.values()]
        missing = [str(path.relative_to(ROOT)) for path in paths if not path.is_file()]
        self.add("Required source and build files", not missing, "missing: " + ", ".join(missing) if missing else "present")

    def check_images(self) -> None:
        missing: list[str] = []
        checked = 0
        for markdown in (ROOT / "sources").glob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for raw in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
                raw = raw.strip()
                target_part = raw[1 : raw.find(">")].strip() if raw.startswith("<") and ">" in raw else raw.split(maxsplit=1)[0]
                target = unquote(target_part.strip("<>\"'"))
                if re.match(r"^(?:https?:|data:)", target, re.I):
                    continue
                checked += 1
                candidates = (markdown.parent / target, ROOT / target)
                if not any(path.is_file() for path in candidates):
                    missing.append(f"{markdown.relative_to(ROOT)} -> {target}")
        self.add("Markdown image references", not missing, f"checked={checked}; missing={missing}")

    def check_product_research(self, text: str) -> None:
        required = (
            "Product A: FIFA.com", "Product B: Chess.com", "FIFA user groups", "Chess.com user groups",
            "Use cases", "HCI findings", "Benefits summary", "Drawbacks summary", "Concrete scenario",
        )
        missing = [term for term in required if term.casefold() not in text.casefold()]
        context_labels = ("Where:", "When:", "Posture:", "Device:", "Attention level:", "Environment:", "Interaction method:")
        bad_context = [label for label in context_labels if text.count(label) < 10]
        figures = len(re.findall(r"!\[Figure\s+[FC]-\d+", text, re.I))
        self.add("ProductResearch required PA1 sections", not missing, f"missing={missing}")
        self.add("ProductResearch use-case contexts", not bad_context, f"labels below 10 occurrences={bad_context}")
        self.add("ProductResearch figure evidence", figures >= 20, f"figure references={figures}")

    def check_canonical_mapping(self, product: str, solutions: str) -> None:
        errors: list[str] = []
        product_findings = set(re.findall(r"\b[FC]-HCI\d+\b", product))
        tables = markdown_tables(solutions)
        seen_inventory: set[str] = set()
        seen_mapping: set[str] = set()
        seen_solutions: set[str] = set()
        figure_ids = set(re.findall(r"Figure\s+([FCS]-\d+)", product + "\n" + solutions, re.I))
        for header, rows in tables:
            normalized_header = [normalize(cell) for cell in header]
            for row in rows:
                if not row:
                    continue
                drawback = next((cell for cell in row if cell in CANONICAL), None)
                solution = next((cell for cell in row if re.fullmatch(r"[FC]-S\d+", cell)), None)
                if drawback:
                    title, finding, expected_solutions, prefix, keywords = CANONICAL[drawback]
                    row_text = " | ".join(row)
                    found_findings = set(re.findall(r"\b[FC]-HCI\d+\b", row_text))
                    found_solutions = set(re.findall(r"\b[FC]-S\d+\b", row_text))
                    figures = set(re.findall(r"\b([FC]-\d{2})\b", row_text))
                    if "linked finding" in normalized_header:
                        seen_inventory.add(drawback)
                        if title.casefold() not in row_text.casefold() or found_findings != {finding}:
                            errors.append(f"{drawback} inventory meaning/finding mismatch")
                    if "solutions" in normalized_header:
                        if found_solutions:
                            seen_mapping.add(drawback)
                            if found_solutions != set(expected_solutions):
                                errors.append(f"{drawback} maps to {sorted(found_solutions)}, expected {list(expected_solutions)}")
                    if "problem" in normalized_header:
                        problem_index = normalized_header.index("problem")
                        problem = normalize(row[problem_index]) if problem_index < len(row) else ""
                        if not any(keyword in problem for keyword in keywords):
                            errors.append(f"{drawback} problem contradicts canonical meaning")
                    if any(not figure.startswith(prefix + "-") for figure in figures):
                        errors.append(f"{drawback} references wrong-product figure {sorted(figures)}")
                    if any(figure not in figure_ids for figure in figures):
                        errors.append(f"{drawback} references missing figure {sorted(figures - figure_ids)}")
                if solution:
                    seen_solutions.add(solution)
                    reverse = next((did for did, data in CANONICAL.items() if solution in data[2]), None)
                    row_drawbacks = set(re.findall(r"\b[FC]-D\d+\b", " | ".join(row)))
                    if row_drawbacks and row_drawbacks != {reverse}:
                        errors.append(f"{solution} references {sorted(row_drawbacks)}, expected {reverse}")
        missing_findings = sorted({data[1] for data in CANONICAL.values()} - product_findings)
        if missing_findings:
            errors.append(f"linked ProductResearch findings missing: {missing_findings}")
        if seen_inventory != set(CANONICAL):
            errors.append(f"inventory incomplete: {sorted(set(CANONICAL) - seen_inventory)}")
        if seen_mapping != set(CANONICAL):
            errors.append(f"mapping table incomplete: {sorted(set(CANONICAL) - seen_mapping)}")
        expected_solution_ids = {solution for data in CANONICAL.values() for solution in data[2]}
        if not expected_solution_ids.issubset(seen_solutions):
            errors.append(f"solution rows missing: {sorted(expected_solution_ids - seen_solutions)}")
        self.add("PotentialSolutions canonical traceability", not errors, "; ".join(dict.fromkeys(errors)))

    def check_weekly(self, text: str, label: str) -> None:
        errors: list[str] = []
        if f"{self.group_id}-PA1 Sprint 1 Meeting Minutes and Weekly Report" not in text:
            errors.append("exact title missing")
        required = (
            "Process Overview", "RUP + Scrum", "Inception", "Elaboration", "Construction", "Transition",
            "One sprint lasted two weeks", "Google Docs and Google Drive Structure", "Team Roster and Meeting Schedule",
            "Sprint Planning Meeting Minutes", "Weekly Scrum Meeting Minutes",
            "Sprint Review and Retrospective Meeting Minutes", "Workload Summary",
            "Deliverable Acceptance Checklist", "Submission Status and Required Manual Inputs",
        )
        errors.extend(f"missing {term}" for term in required if term.casefold() not in text.casefold())
        ordered_sections = (
            "2. Process Overview", "3. Google Docs and Google Drive Structure", "4. Team Roster and Meeting Schedule",
            "5. Sprint Planning Meeting Minutes", "6. Weekly Scrum Meeting Minutes",
            "7. Sprint Review and Retrospective Meeting Minutes", "8. Workload Summary",
            "9. Deliverable Acceptance Checklist", "10. Submission Status and Required Manual Inputs",
        )
        positions = [text.casefold().find(section.casefold()) for section in ordered_sections]
        if any(position < 0 for position in positions) or positions != sorted(positions):
            errors.append("required Sections 1-10 are missing or out of order")
        for link_label in ("Weekly Scrum Google Doc", "Sprint Planning Google Doc", "Sprint Review Google Doc", "Google Drive README", "GitHub repository", "Moodle ZIP artifact"):
            if link_label.casefold() not in text.casefold():
                errors.append(f"missing {link_label}")
        for name, student_id in MEMBERS:
            if name not in text or student_id not in text:
                errors.append(f"roster missing {name}, {student_id}")
        if "Balanced contribution across four members".casefold() not in text.casefold():
            errors.append("balanced contribution explanation missing")
        markers = (
            "=========== 10/06/2026, Sprint 1, Sprint Planning ===============",
            "=========== 14/06/2026, Sprint 1 ===============",
            "=========== 19/06/2026, Sprint 1 ===============",
            "=========== 22/06/2026, Sprint 1, Sprint Review and Retrospective ===============",
        )
        expected_schedule = (
            ("10 June 2026", "20:00 to 20:45"),
            ("14 June 2026", "20:00 to 20:30"),
            ("19 June 2026", "20:00 to 20:30"),
            ("22 June 2026", "20:00 to 20:50"),
        )
        for date, time in expected_schedule:
            if date not in text or time not in text:
                errors.append(f"schedule missing {date}, {time}")
        for marker in markers:
            if marker not in text:
                errors.append(f"missing meeting heading {marker}")
        marker_positions = [text.find(marker) for marker in markers]
        if all(position >= 0 for position in marker_positions) and marker_positions != sorted(marker_positions):
            errors.append("meeting headings are out of order")
        for index, marker in enumerate(markers):
            block = bounded_section(text, marker, markers[index + 1 :])
            if not block:
                continue
            for field in ("Date", "Time", "Team members present", "Team members absent", "Actions", "Summary of the meeting"):
                if field.casefold() not in block.casefold():
                    errors.append(f"{marker}: missing {field}")
            if index in (0, 3) and "Meeting objective".casefold() not in block.casefold():
                errors.append(f"{marker}: missing Meeting objective")
            date, time = expected_schedule[index]
            if date not in block or time not in block:
                errors.append(f"{marker}: missing exact date/time {date}, {time}")
            if index == 0:
                for field in ("Sprint objective", "Product scope", "Priority and acceptance criteria", "Selected user stories", "Task assignment"):
                    if field.casefold() not in block.casefold():
                        errors.append(f"{marker}: missing {field}")
            if index == 3:
                for field in ("What went well", "What went wrong", "What problems occurred", "What caused the problems", "What the team will do differently in the next sprint", "Lessons learned"):
                    if field.casefold() not in block.casefold():
                        errors.append(f"{marker}: missing {field}")
            if index in (1, 2):
                exact_fields = ("Completed tasks", "To-do tasks", "Issues/Obstacles")
                if not all(block.casefold().count(field.casefold()) >= 4 for field in exact_fields):
                    errors.append(f"{marker}: missing four per-member Scrum field sets")
                if not all(name in block for name, _ in MEMBERS):
                    errors.append(f"{marker}: missing one or more members")
        if re.search(r"^(?:#{1,6}\s+)?References\s*$", text, re.I | re.M):
            errors.append("References section is forbidden")
        self.add(f"WeeklyReport strict template ({label})", not errors, "; ".join(dict.fromkeys(errors)))

    def real_peer_rows(self, text: str) -> list[list[str]]:
        heading = re.search(r"^#{1,6}\s+Real Classroom Peer Feedback(?:,\s*Pending)?\s*$", text, re.I | re.M)
        if not heading:
            return []
        tail = text[heading.end() :]
        next_heading = re.search(r"^#{1,6}\s+", tail, re.M)
        section = tail[: next_heading.start()] if next_heading else tail
        valid: list[list[str]] = []
        for header, rows in markdown_tables(section):
            wanted = ("Commenter name", "Feedback or question", "Group response", "Revision action", "Owner", "Status")
            if [normalize(cell) for cell in header] != [normalize(cell) for cell in wanted]:
                continue
            for row in rows:
                cells = [cell.strip() for cell in row[:6]]
                joined = normalize(" ".join(cells))
                if len(cells) == 6 and all(cells) and not re.search(r"\b(?:todo|pending|mock|internal|tbd)\b", joined):
                    valid.append(cells)
        return valid

    def check_peer(self, text: str, label: str, expected_real_rows: list[list[str]] | None = None) -> bool:
        errors: list[str] = []
        normalized = normalize(text)
        internal = "internal rehearsal feedback" in normalized
        pending = "real classroom peer feedback, pending" in normalized
        real_rows = self.real_peer_rows(text)
        if label == "PDF" and expected_real_rows:
            real_rows = expected_real_rows if all(all(cell in text for cell in row) for row in expected_real_rows) else []
        mock_present = bool(re.search(r"\b(?:mock|internal rehearsal)\b", text, re.I))
        if mock_present and not internal:
            errors.append("mock feedback is not under an Internal rehearsal feedback section")
        if not real_rows and not pending:
            errors.append("pending real-feedback section missing")
        if pending:
            for field in ("Commenter name", "Feedback or question", "Group response", "Revision action", "Owner", "Status"):
                if field.casefold() not in text.casefold():
                    errors.append(f"pending table missing {field}")
        if self.mode == "final" and (pending or not real_rows):
            errors.append("final mode requires populated real classroom feedback")
        if self.mode == "final" and real_rows and mock_present:
            errors.append("final PeerReview must not retain mock/internal feedback wording after real feedback is supplied")
        self.add(f"PeerReview authenticity ({label})", not errors, "; ".join(dict.fromkeys(errors)))
        return bool(real_rows) and not pending

    def check_blockers(self, real_peer: bool) -> None:
        path = ROOT / "docs" / "pa1_submission_blockers.md"
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        errors: list[str] = []
        placeholder_group = self.group_id.casefold() == "groupid"
        if placeholder_group and GROUP_BLOCKER not in text:
            errors.append("exact GroupID blocker line missing")
        if not real_peer and not any(line in text for line in PEER_BLOCKERS):
            errors.append("exact peer-feedback blocker line missing")
        self.add("Submission blocker documentation", not errors, "; ".join(errors))
        if self.mode == "final":
            self.add("Final group ID gate", not placeholder_group, f"group_id={self.group_id}")
            self.add("Final real peer-feedback gate", real_peer, "real classroom feedback must be populated")
        else:
            self.add("Draft placeholder policy", True, f"group_id={self.group_id}; real_peer_feedback={real_peer}")

    def check_pdfs(self) -> None:
        missing = [path.name for path in self.pdfs.values() if not path.is_file() or path.stat().st_size <= 10_000]
        self.add("Final PDFs exist and exceed 10 KB", not missing, f"missing/small={missing}")
        extractor, backend = pdf_extractor()
        self.add("PDF text extraction backend", extractor is not None, backend)
        if extractor is None:
            return
        errors: list[str] = []
        for name, path in self.pdfs.items():
            if not path.is_file():
                continue
            try:
                text = extractor(path)
                self.pdf_text[name] = text
                if len(text.strip()) < 200:
                    errors.append(f"{path.name}: extracted text too short ({len(text.strip())})")
            except Exception as exc:
                errors.append(f"{path.name}: {exc}")
        self.add("PDF text extraction", not errors and len(self.pdf_text) == 4, "; ".join(errors) or f"backend={backend}")

    def check_docx(self) -> None:
        paths = (ROOT / f"{self.group_id}-PA1-WorkDivision.docx", ROOT / "output" / f"{self.group_id}-PA1-WorkDivision.docx")
        missing = [str(path.relative_to(ROOT)) for path in paths if not path.is_file() or path.stat().st_size < 10_000]
        self.add("Expected WorkDivision DOCX files", not missing, f"missing/small={missing}")

    def check_zip(self) -> None:
        path = ROOT / f"{self.group_id}-PA1.zip"
        if not path.is_file():
            self.add("Submission ZIP exact contents and hashes", False, f"missing {path.name}")
            return
        expected = {pdf.name for pdf in self.pdfs.values()}
        errors: list[str] = []
        try:
            with zipfile.ZipFile(path) as archive:
                names = archive.namelist()
                if set(names) != expected or len(names) != 4:
                    errors.append(f"contents={names}, expected={sorted(expected)}")
                if any(PurePosixPath(name).parent != PurePosixPath(".") or not name.lower().endswith(".pdf") for name in names):
                    errors.append("ZIP contains a non-top-level or non-PDF entry")
                for pdf in self.pdfs.values():
                    if pdf.is_file() and pdf.name in names:
                        member_hash = hashlib.sha256(archive.read(pdf.name)).hexdigest()
                        if member_hash != sha256(pdf):
                            errors.append(f"{pdf.name} differs from root PDF")
        except (OSError, zipfile.BadZipFile) as exc:
            errors.append(str(exc))
        self.add("Submission ZIP exact contents and hashes", not errors, "; ".join(errors))

    def check_freshness(self) -> None:
        inputs = [ROOT / "build_pa1_package.py", CONFIG_PATH, *self.sources.values()]
        inputs = [path for path in inputs if path.is_file()]
        pdfs = [path for path in self.pdfs.values() if path.is_file()]
        zip_path = ROOT / f"{self.group_id}-PA1.zip"
        ok = bool(inputs and len(pdfs) == 4 and zip_path.is_file())
        detail = ""
        if ok:
            newest_input = max(path.stat().st_mtime_ns for path in inputs)
            oldest_pdf = min(path.stat().st_mtime_ns for path in pdfs)
            newest_pdf = max(path.stat().st_mtime_ns for path in pdfs)
            ok = oldest_pdf >= newest_input and zip_path.stat().st_mtime_ns >= newest_pdf
            detail = f"newest_input={newest_input}; oldest_pdf={oldest_pdf}; zip={zip_path.stat().st_mtime_ns}"
        self.add("Artifacts regenerated after source fixes", ok, detail or "required artifacts unavailable")

    def check_forbidden_terms(self, source_text: str) -> None:
        combined = source_text + "\n" + "\n".join(self.pdf_text.values())
        matches = [term for term in (*OLD_PRODUCTS, *GENERIC_MEMBERS) if re.search(rf"\b{re.escape(term)}\b", combined, re.I)]
        self.add("Old products and generic members absent", not matches, f"matches={matches}")

    def check_readiness_claims(self, blockers_exist: bool) -> None:
        offenders: list[str] = []
        if blockers_exist:
            patterns = (
                re.compile(r"^\s*Status:\s*READY(?:\s+FINAL|\s+10/10)\s*$", re.I | re.M),
                re.compile(r"^\s*Critical blockers:\s*0\s*\.?\s*$", re.I | re.M),
            )
            for path in (ROOT / "docs").glob("*.md"):
                text = path.read_text(encoding="utf-8")
                if "superseded" in text[:500].casefold():
                    continue
                if any(pattern.search(text) for pattern in patterns):
                    offenders.append(str(path.relative_to(ROOT)))
        self.add("No unsupported READY 10/10 claim", not offenders, f"offenders={offenders}")

    def run(self) -> int:
        self.load_config()
        self.check_required_files()
        self.check_images()
        texts = {name: path.read_text(encoding="utf-8") for name, path in self.sources.items() if path.is_file()}
        if "ProductResearch" in texts:
            self.check_product_research(texts["ProductResearch"])
        else:
            self.add("ProductResearch required PA1 sections", False, "source unavailable")
        if "ProductResearch" in texts and "PotentialSolutions" in texts:
            self.check_canonical_mapping(texts["ProductResearch"], texts["PotentialSolutions"])
        else:
            self.add("PotentialSolutions canonical traceability", False, "source unavailable")
        if "WeeklyReport" in texts:
            self.check_weekly(texts["WeeklyReport"], "source")
        else:
            self.add("WeeklyReport strict template (source)", False, "source unavailable")
        source_real_rows = self.real_peer_rows(texts.get("PeerReview", ""))
        real_peer = self.check_peer(texts.get("PeerReview", ""), "source")
        self.check_pdfs()
        if "WeeklyReport" in self.pdf_text:
            self.check_weekly(self.pdf_text["WeeklyReport"], "PDF")
        if "PeerReview" in self.pdf_text:
            pdf_real = self.check_peer(self.pdf_text["PeerReview"], "PDF", source_real_rows)
            real_peer = real_peer and pdf_real
        self.check_blockers(real_peer)
        self.check_docx()
        self.check_zip()
        self.check_freshness()
        self.check_forbidden_terms("\n".join(texts.values()))
        blockers_exist = self.group_id.casefold() == "groupid" or not real_peer
        self.check_readiness_claims(blockers_exist)
        failed = [check for check in self.checks if not check.ok]
        print(f"PA1 submission validation ({self.mode})")
        print("| Check | Result | Detail |")
        print("| --- | --- | --- |")
        for check in self.checks:
            detail = check.detail.replace("|", "\\|").replace("\n", " ")
            print(f"| {check.name} | {'PASS' if check.ok else 'FAIL'} | {detail} |")
        print(f"\nOverall: {'PASS' if not failed else 'FAIL'} ({len(failed)} failed checks)")
        return 0 if not failed else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the PA1 draft or final Moodle submission package.")
    parser.add_argument("--mode", choices=("draft", "final"), required=True)
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(Validator(parse_args().mode).run())
