# PA1 Strava/Nike Run Club Migration Audit

Date: 2026-06-10

## Phase 0 audit note
Repository root inspected with PowerShell `Get-Location`. Tree was listed to depth 3. Editable and generated files were enumerated by extension. The PDF pipeline is `build_pa1_package.py` using ReportLab for PDFs, Markdown source emission, JSON source-of-truth emission, and Python zipfile packaging. The shared source-of-truth is `pa1_project_data.json`, regenerated from this script. The requested weekly report template was not found in this repo or `/mnt/data`, so the fallback RUP + Scrum weekly structure remains.

## Replacement decision table
| File path | Current product content | Old references found | Required Nike Run Club replacement | Edit action | Validation method |
| --- | --- | --- | --- | --- | --- |
| build_pa1_package.py | Generator embedded old Product B analysis | Old Product B references removed | Nike Run Club sources, personas, use cases, findings, drawbacks, and solutions | Replace generator | Run generator, source scan, PDF text scan |
| pa1_project_data.json | Generated shared data model | Old Product B references removed | Structured products.strava and products.nike_run_club | Regenerate | JSON scan and ID scan |
| pa1_sources_strava_nrc.json | Missing | None | Official Strava and Nike Run Club source log | Create | Validate source counts |
| sources/GroupID-PA1-ProductResearch.md | Research report source | Old Product B references removed | Strava vs Nike Run Club report | Regenerate | Markdown scan and PDF text scan |
| sources/GroupID-PA1-PotentialSolutions.md | Solution report source | Old Product B problem IDs removed | S-D/N-D and S-S/N-S mappings | Regenerate | ID scan and mapping review |
| sources/GroupID-PA1-PeerReview.md | Peer-review source | Old Product B slide/Q&A removed | Nike Run Club slide, Q&A, feedback | Regenerate | Markdown scan and script check |
| sources/GroupID-PA1-WeeklyReport.md | Weekly report source | Old Product B sprint tasks removed | Nike Run Club source/finding/comparison tasks | Regenerate | Markdown scan and sprint checklist |
| GroupID-PA1-*.pdf | Generated PDFs | Old Product B PDF text removed | Regenerated PDFs from corrected Markdown | Overwrite | pypdf extraction and restricted-term scan |
| GroupID-PA1.zip | Submission package | Old PDFs removed | Exactly four regenerated PDFs at top level | Overwrite | zipfile listing |
| docs/*.md | Durable repo memory | Old Product B context removed except this audit note | Current Strava/Nike Run Club context | Update | Docs scan |

## Removed content changelog
Removed the previous Product B analysis, citations, problem IDs, solution IDs, sprint tasks, and generated PDF text. This audit intentionally keeps a changelog note that the former Product B content was removed.
