# PA1 Final Fix Plan

Date: 2026-06-22
Workspace: `C:\Users\Administrator\Documents\MEGA\tkgd\PA1`

## Phase 0 Findings

- Current working directory printed: `C:\Users\Administrator\Documents\MEGA\tkgd\PA1`.
- Repository structure listed to depth 2.
- Required audit/source/generator/context files were read.
- `README.md` is absent; durable context files already exist under `docs/`.
- Source-of-truth blocker: `build_pa1_package.py` defines `TEAM_MEMBERS = ["Member1", "Member2", "Member3", "Member4", "Member5"]`.
- Generated shared data blocker: `pa1_project_data.json` contains the same five generic member labels and an assumption that member names are generic.
- ProductResearch source blocker: generated header contains `Member1` through `Member5`; use-case tables combine context into one row instead of strict labels.
- PeerReview source blocker: seven-minute script, slide owners, mock feedback owners, and revision owner mapping use `Member1` through `Member5`.
- WeeklyReport source blocker: it says "five placeholder team members", uses `Member1` through `Member5`, has meeting-level scrum rows, and includes "Manual placeholders remain".
- WorkDivision blocker: script currently generates an English/ProductResearch-only document, not the required Vietnamese all-deliverable work-division document.
- Old product terms found only in `todo.txt`, existing audit/changelog context, and allowed supporting docs, not in final source reports.
- Final generated text under `generated_text/` still contains old generic member labels because PDFs were generated before the final fixes.

## Decision Table

| File | Problem found | Root cause | Required fix | Edit target | Validation method | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `build_pa1_package.py` | Five generic member labels drive multiple final sources | `TEAM_MEMBERS` and hard-coded report tables use default labels | Replace with four real members and roles | Generator constants and report builders | Regenerate data, sources, PDFs; scan text | Completed |
| `pa1_project_data.json` | Generic member labels and generic-name assumption | Generated from `build_pa1_package.py` | Regenerate from corrected generator | Generated JSON | JSON scan for real names and no generic labels | Completed |
| `sources/GroupID-PA1-ProductResearch.md` | Header has generic members; use-case tables lack exact labels | Generated from `product_research_md()` and `use_case_sections()` | Add real members and strict use-case fields | Generator | Markdown and PDF text scan; label count | Completed |
| `sources/GroupID-PA1-PeerReview.md` | Owner fields use generic members | Hard-coded peer review script/tables | Replace owners with real names and balanced owner mapping | Generator | Markdown/PDF scan and owner-table scan | Completed |
| `sources/GroupID-PA1-WeeklyReport.md` | Generic roster, no per-member scrum detail, disallowed wording | Hard-coded WeeklyReport body | Replace with four-member roster, planned dates, per-member scrum rows, sprint review, checklist | Generator | Markdown/PDF scan and weekly rubric checks | Completed |
| `scripts/create_pa1_work_division_docx.py` | WorkDivision is English and ProductResearch-only | Earlier helper script scoped to one deliverable | Regenerate Vietnamese document with required sections, RACI, checklist, signatures | DOCX generator | python-docx text/table validation and render attempt | Completed |
| `GroupID-PA1-*.pdf` | Generated before fixes | Sources were stale | Regenerate four PDFs | Build pipeline | File size, extracted text, visual evidence presence | Completed |
| `GroupID-PA1.zip` | Generated before fixes | Contains stale PDFs | Regenerate exact four-PDF top-level zip | Build pipeline | Zip listing exact match | Completed |
| `docs/session_handoff.md` | Needs decision scratchpad before edits and final handoff after fixes | Project workflow | Append decision summary, then update final state | Generator/manual docs | File inspection | Completed |

## Decision Summary Before Editing

The safest fix path is generator-first. I will update `build_pa1_package.py` so regenerated Markdown, JSON, PDFs, extracted text, manifest, and memory docs share one four-member model. I will separately update `scripts/create_pa1_work_division_docx.py` because WorkDivision is not produced by the PDF package generator. Existing screenshots, citations, visual manifests, and zip shape will be preserved.

## Completion Summary

- Final validation status: READY 10/10.
- Total score after fix: 99.5/100.
- Critical blockers after fix: 0.
- Validation report: `docs/pa1_final_fix_validation.md`.
- After-fix audit: `docs/pa1_final_10_10_audit_after_fix.md`.
