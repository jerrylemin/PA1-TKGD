# PA1 Balanced Workload and Diagram Fix Plan

Date: 2026-07-02

## Phase 0 findings

- Member data and generated report text originate in `build_pa1_package.py`; `pa1_project_data.json` is regenerated from it.
- Report Markdown is produced by `product_research_md`, `solutions_md`, `peer_review_md`, and `weekly_report_md`.
- Existing diagrams are raw Mermaid strings in the generator and `.mmd` files under `sources/`.
- Canonical Mermaid sources belong in `assets/diagrams/mermaid/`; rendered PNGs belong in `assets/diagrams/rendered/`.
- Edit targets: `build_pa1_package.py`, `scripts/create_pa1_work_division_docx.py`, six Mermaid sources, validation script, consistency/audit docs, and memory docs.
- Validation: `npx mmdc --version`; `python -m py_compile build_pa1_package.py scripts/create_pa1_work_division_docx.py scripts/validate_pa1_balance_diagrams.py`; run both generators; run `scripts/validate_pa1_balance_diagrams.py`.

## Decision table

| Issue | Root cause | Files affected | Fix strategy | Validation method | Status |
| --- | --- | --- | --- | --- | --- |
| Four-person balance | Existing matrix uses unequal point totals and no percentages | Generator, WeeklyReport, WorkDivision | Canonical 25% rows with research, writing, review, and final QA for each member | Source/PDF/DOCX scan | In progress |
| Two people per website | Roles describe one research lead per site and cross-report leads | Generator and all reports | State FIFA co-owners Le Minh + Nguyen Vu Bach; Chess.com co-owners Pham Nguyen Gia Bao + Trang Minh Nhut | Ownership phrase scan | In progress |
| Cross-report consistency | Ownership and ID traceability are distributed | Four reports, WorkDivision | Add canonical ownership and traceability tables generated from existing IDs | ID and owner scan | In progress |
| Raw Mermaid sections | Generator emits fenced Mermaid text | ProductResearch and WeeklyReport | Replace with PNG image links and add images to remaining reports | Image-reference scan | In progress |
| PDF image support | Already implemented for Markdown image links | `build_pa1_package.py` | Reuse existing `RLImage` path | PDF size/render check | Pass |
| DOCX alignment | Separate generator has older responsibility language | WorkDivision generator | Update ownership and insert RACI PNG | DOCX text/media scan | In progress |
| Zip shape | Existing generator writes four PDFs | Zip | Preserve implementation | Exact zip listing | Pass |
| Prohibited terms | Matches are confined to historical docs, task text, and validators | Final sources/PDFs | Scan only final sources and extracted final PDF text | Zero-match validation | Pass before changes |

## Decision gate

Generator-first is required because Markdown is overwritten during regeneration. Mermaid CLI was absent, so `@mermaid-js/mermaid-cli` is installed locally as requested. PDF image support already exists; no new PDF abstraction is needed.
