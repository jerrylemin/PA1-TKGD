# PA1 FIFA and Chess.com Migration Audit

Date: 2026-06-10

## Phase 0 findings

Working directory: C:\Users\Administrator\Documents\MEGA\tkgd\PA1

Repository tree was listed to depth 3. Source and output files were enumerated by extension. The generation pipeline is build_pa1_package.py using ReportLab for PDF generation and Python zipfile for packaging. Source-of-truth files are build_pa1_package.py, pa1_project_data.json, pa1_sources_fifa_chess.json, and sources/*.md. Output files are the four GroupID-PA1 PDFs and GroupID-PA1.zip.

## Decision table

| File path | Current product content | Old product terms found | Required FIFA / Chess.com replacement | Edit action | Validation method |
| --- | --- | --- | --- | --- | --- |
| build_pa1_package.py | Generated package source of truth | previous Product A, previous Product B, previous wearable framing, previous mobile-fitness framing, S-, G-, N-, SA-, GA- | FIFA/Chess.com data, source log, Markdown, PDF, zip, docs generator | Replace generator | Run generator; scan generated files and extracted PDF text |
| pa1_project_data.json | Generated shared fact base | S-, G-, N-, SA-, GA- | products.fifa_web and products.chesscom_web with F/C ID families | Regenerate | JSON scan |
| pa1_sources_fifa_chess.json | New official source log | Previous source log removed | FIFA and Chess.com official sources with required metadata | Create | Validate source count by product |
| sources/GroupID-PA1-ProductResearch.md | Editable report source | Old product analysis and mobile fitness framing | FIFA vs Chess.com web research report | Regenerate | Markdown and PDF text scan |
| sources/GroupID-PA1-PotentialSolutions.md | Editable solution source | Old drawback/solution ID families | F-D/C-D drawbacks and F-S/C-S solutions | Regenerate | Mapping check and scan |
| sources/GroupID-PA1-PeerReview.md | Editable peer-review source | Old slides, Q&A, feedback | FIFA/Chess.com seven-minute script and slide plan | Regenerate | Script and feedback count check |
| sources/GroupID-PA1-WeeklyReport.md | Editable process source | Old sprint wording and unavailable-template fallback | Two-week RUP plus Scrum report aligned to actual process | Regenerate | Meeting and 14-day plan check |
| GroupID-PA1-*.pdf | Generated PDFs | Old PDF text | Regenerated PDFs from corrected Markdown | Archive previous PDFs and overwrite | pypdf extraction and old-term scan |
| GroupID-PA1.zip | Submission package | Old PDFs in previous package | Exactly four regenerated PDFs at top level | Overwrite | zipfile listing |

## Removed content

The previous product pair, previous mobile fitness framing, previous source log, previous ID families, and previous generated PDF text were removed from final deliverables. The visual migration audit records the exact removed names in its allowed Removed Content section.

## Validation plan

Final source files and extracted PDF text are scanned for removed product terms and old ID families. The migration audit is the only retained changelog location for removed terms.
