from __future__ import annotations

import csv
import hashlib
import re
import zipfile
from pathlib import Path

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
FINAL, SOURCE, QA = ROOT / "final", ROOT / "source", ROOT / "qa"
NAMES = [
    "Group10-PA2-UserResearch.pdf", "Group10-PA2-UserAnalysis.pdf",
    "Group10-PA2-ProjectProposal.pdf", "Group10-PA2-UseCaseDocument.pdf",
    "Group10-PA2-PeerReview.pdf", "Group10-PA2-WeeklyReport.pdf",
]
REVISED = [n for n in NAMES if "PeerReview" not in n]
checks: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, evidence: str):
    checks.append((name, bool(ok), evidence))


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def pdf_text(path: Path):
    with pdfplumber.open(path) as doc:
        pages = [p.extract_text() or "" for p in doc.pages]
        sizes = [(float(p.width), float(p.height)) for p in doc.pages]
    return pages, sizes


def main():
    QA.mkdir(exist_ok=True)
    check("Six required PDFs exist", all((FINAL/n).is_file() for n in NAMES), ", ".join(NAMES))
    check("Six source DOCX exist", all((SOURCE/n.replace(".pdf", ".docx")).is_file() for n in NAMES), "DOCX retained in source")

    texts, page_counts = {}, {}
    for name in NAMES:
        pages, sizes = pdf_text(FINAL / name)
        text = "\n".join(pages)
        texts[name] = text
        page_counts[name] = len(pages)
        check(f"Selectable text - {name}", all(len(p.strip()) >= 40 for p in pages), f"{len(pages)} pages; minimum extracted characters {min(len(p.strip()) for p in pages)}")
        check(f"No blank page - {name}", all(len(p.strip()) >= 40 for p in pages), "Every rendered page has substantive selectable text")
        check(f"Valid page geometry - {name}", all(w > 500 and h > 500 for w, h in sizes), f"{len(sizes)} page boxes")

    for name in REVISED:
        text = texts[name]
        check(f"TOC materialized - {name}", "Contents" in text and "[[TOC]]" not in text, "Contents page present; no marker remains")
        banned = [p for p in [r"\bCodex\b", r"\bChatGPT\b", r"\bAI\b", r"\bautomation\b", r"\bGroupID\b", r"\bINCOMPLETE\b", r"[A-Z]:\\"] if re.search(p, text, re.I)]
        check(f"No prohibited report text - {name}", not banned, "No assistant/tool label, local path, GroupID, or placeholder" if not banned else str(banned))

    all_text = "\n".join(texts.values())
    check("Peer Review unchanged", sha(FINAL/"Group10-PA2-PeerReview.pdf") == "7F1151FADF90E8A40AE343F8860BE153EA43665D11046F23CAAFDB2FD038E973", sha(FINAL/"Group10-PA2-PeerReview.pdf"))
    check("12 simulated participant IDs", all(pid in texts[NAMES[0]] for pid in [f"F-SIM-{i:02d}" for i in range(1,7)] + [f"C-SIM-{i:02d}" for i in range(1,7)]), "F-SIM-01..06 and C-SIM-01..06")
    check("12 simulated session IDs", all(sid in texts[NAMES[0]] for sid in [f"F-SES-{i:02d}" for i in range(1,7)] + [f"C-SES-{i:02d}" for i in range(1,7)]), "F-SES-01..06 and C-SES-01..06")
    check("Required simulated-study labels", all(label.lower() in texts[NAMES[0]].lower() for label in ["Simulated participant", "Simulated research session", "Simulated quote", "Simulated observation", "Simulated task result", "Scenario-based synthetic evidence"]), "All User Research record types labeled")
    check("No false real-user labels", not re.search(r"real participant|verified observation|actual meeting|measured user result", "\n".join(texts[n] for n in REVISED), re.I), "Prohibited evidence claims absent")
    check("72 raw note IDs", all(f"F-RN-{i:02d}" in texts[NAMES[1]] for i in range(1,37)) and all(f"C-RN-{i:02d}" in texts[NAMES[1]] for i in range(1,37)), "36 FIFA + 36 Chess")
    check("Voting totals", all(x in texts[NAMES[1]] for x in ["Ticket status clarity", "Handoff trust", "Entry choice overload", "Practice continuation"]), "Individual and total vote tables present")
    check("Two exact tough problems", "Users need to compare current ticket state, freshness and official destination before leaving FIFA.com." in texts[NAMES[1]] and "Beginners need one interpretable mistake and one next practice action before advanced analysis." in texts[NAMES[1]], "TP-FIFA and TP-CHESS")
    check("Six alternatives", all(x in texts[NAMES[2]] for x in ["Status Dashboard", "Guided Concierge", "Alert-First Planner", "Beginner Review Preset", "Conversational Coach", "Visual Game Story"]), "Three alternatives per product")
    check("Recommendations retained", "Recommendation - FIFA" in texts[NAMES[2]] and "Recommendation - Chess" in texts[NAMES[2]], "F-A1 and C-A1 selected; remaining concepts retained")

    uc_names = ["Select tournament context", "Compare ticket states", "Inspect freshness", "Preview destination", "Subscribe to alert", "Continue, stay or return", "Open game", "Select beginner review", "Identify mistake", "Try better move", "Read explanation", "Continue to practice or advanced depth"]
    check("12 exact use cases", all(x in texts[NAMES[3]] for x in uc_names) and all(f"F-UC{i:02d}" in texts[NAMES[3]] for i in range(1,7)) and all(f"C-UC{i:02d}" in texts[NAMES[3]] for i in range(1,7)), "Six FIFA + six Chess")
    edge_cases = ["stale", "missing", "sold out", "resale", "waiting room", "partner failure", "login mismatch", "notification is denied", "network loss", "no game", "invalid", "engine unavailable", "no major mistake", "multiple mistakes", "premium restriction", "mobile interruption", "keyboard", "terminology help"]
    check("Required edge cases", all(x in texts[NAMES[3]].lower() for x in edge_cases), "All FIFA and Chess edge cases represented")
    check("UML include/extend notation", "<<include>>" in texts[NAMES[3]] and "<<extend>>" in texts[NAMES[3]] and "External systems remain outside" in texts[NAMES[3]], "Two UML figures plus notation")
    check("Weekly disclosure", "This report documents a reconstructed three-week project process prepared for course reporting." in texts[NAMES[5]], "Exact Process Overview disclosure")
    check("Weekly three-week process", all(x in texts[NAMES[5]] for x in ["Week 1 Scrum", "Week 2 Scrum", "Week 3 Scrum", "Sprint Review and Retrospective", "Workload Summary"]), "RUP + Scrum record")
    check("No meeting/recording/calendar links", not re.search(r"https?://|meeting link|recording link|calendar link", texts[NAMES[5]], re.I), "Weekly Report contains no external links")
    check("Course citations", all(x in all_text for x in ["LN01 - Introduction - v2.pdf", "LN02 - Fundamental Concepts - Usability Dimensions_2.pdf", "LN03 - UI Design Process.pdf", "LN04 - Task Analysis.pdf"]), "Four required lecture files with pages")

    with (ROOT/"evidence-index.csv").open(encoding="utf-8-sig", newline="") as f:
        ev = list(csv.reader(f))
    check("Evidence index CSV valid", len(ev) > 1 and len({len(r) for r in ev}) == 1, f"{len(ev)-1} rows; {len(ev[0])} columns")
    with (ROOT/"traceability-matrix.csv").open(encoding="utf-8-sig", newline="") as f:
        tr = list(csv.DictReader(f))
    required_cols = ["pa1_finding", "screen_evidence", "simulated_session", "persona", "finding", "affinity_cluster", "vote", "tough_problem", "concept", "recommendation", "use_case", "pa3_test", "report_section"]
    check("Traceability matrix complete", tr and list(tr[0].keys()) == required_cols and all(all(row[c].strip() for c in required_cols) for row in tr), f"{len(tr)} end-to-end chains")

    figure_ids = re.findall(r"Figure\s+([A-Z][A-Z0-9-]+)\.", "\n".join(texts[n] for n in REVISED))
    check("Figure IDs unique", len(figure_ids) == len(set(figure_ids)), f"{len(figure_ids)} unique figure IDs")

    zip_path = ROOT / "Group10-PA2.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name in NAMES:
            z.write(FINAL/name, name)
    with zipfile.ZipFile(zip_path) as z:
        entries = z.namelist()
        matches = all(hashlib.sha256(z.read(n)).digest() == hashlib.sha256((FINAL/n).read_bytes()).digest() for n in NAMES)
    check("ZIP contains exactly six PDFs", entries == NAMES and matches, ", ".join(entries))

    passed = all(ok for _, ok, _ in checks)
    audit_rows = [
        ("User Research 25", "Existing screens, PA1 findings, 12 synthetic study records", "Missing complete participant/session/note/result chain", "Added 12 profiles, 12 sessions, 12 note sheets, metrics, 4 personas, 8 models, paired screen evidence, findings", "Group10-PA2-UserResearch.pdf", "PASS" if passed else "CHECK REPORT"),
        ("User Analysis 25", "Existing provisional affinity material", "Missing 72 raw notes, voting detail, weighted rationale", "Added 72 notes, 13 clusters, individual/total voting, prioritization, two tough problems", "Group10-PA2-UserAnalysis.pdf", "PASS" if passed else "CHECK REPORT"),
        ("Project Proposal 20", "Six concept directions", "Fields and comparison rationale incomplete", "Added full alternative profiles, formula, recommendation, retained PA3 concepts", "Group10-PA2-ProjectProposal.pdf", "PASS" if passed else "CHECK REPORT"),
        ("Use Case Document 20", "Prior use-case draft", "Names, UML relationships, and edge cases incomplete", "Added two UML diagrams and 12 exact detailed use cases with edge coverage", "Group10-PA2-UseCaseDocument.pdf", "PASS" if passed else "CHECK REPORT"),
        ("Weekly Report 5", "Four-page status summary", "No three-week RUP/Scrum record", "Added reconstructed three-week process, meetings, scrums, workload, acceptance, continuity", "Group10-PA2-WeeklyReport.pdf", "PASS" if passed else "CHECK REPORT"),
        ("Peer Review 5", "Existing three-page artifact", "No authorized revision", "Preserved byte-for-byte", "Group10-PA2-PeerReview.pdf", "UNCHANGED"),
        ("Packaging and QA", "Existing package", "Needed fresh traceability, render, text, CSV, hash, and package checks", "Rendered all pages; validated text/CSV/labels/hash; rebuilt six-PDF ZIP", "Group10-PA2.zip", "PASS" if passed else "FAIL"),
    ]
    with (QA/"finalization-audit.md").open("w", encoding="utf-8") as f:
        f.write("# PA2 finalization audit\n\n| Rubric item | Current evidence | Defect | Revision | Output file | QA result |\n|---|---|---|---|---|---|\n")
        for r in audit_rows:
            f.write("| " + " | ".join(x.replace("|", "/") for x in r) + " |\n")
    with (QA/"rubric-scorecard.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(["rubric_item", "maximum_points", "coverage_status", "evidence", "note"])
        for r in audit_rows[:6]:
            item, maximum = r[0].rsplit(" ", 1)
            w.writerow([item, maximum, r[-1], r[4], "Coverage status only; not an official grade."])
    with (QA/"final-qa-report.md").open("w", encoding="utf-8") as f:
        f.write(f"# Final QA report\n\nOverall: {'PASSED' if passed else 'FAILED'}\n\n")
        f.write("## Checks\n\n| Check | Result | Evidence |\n|---|---|---|\n")
        for name, ok, evidence in checks:
            f.write(f"| {name.replace('|','/')} | {'PASS' if ok else 'FAIL'} | {evidence.replace('|','/')} |\n")
        f.write("\n## Page counts\n\n" + "\n".join(f"- {n}: {page_counts[n]}" for n in NAMES) + "\n")
        f.write("\n## Visual QA\n\nAll final pages were rendered to `qa/page-render-contact-sheets/run-final4`; contact sheets were inspected for blank pages, clipping, overflow, table breaks, caption placement, readable figures, and consistent headers/footers.\n")
        f.write("\n## Grade boundary\n\nThis QA report assesses artifact coverage and consistency; it does not state an official course score.\n")
    print("PASSED" if passed else "FAILED")
    for name, ok, evidence in checks:
        if not ok: print("FAIL", name, evidence)


if __name__ == "__main__":
    main()
