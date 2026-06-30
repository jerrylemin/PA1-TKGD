# Project Structure

```text
.
|-- build_pa1_package.py              # Reproducible generator for data, sources, PDFs, zip, manifest, docs
|-- pa1_project_data.json             # Shared PA1 fact base
|-- pa1_sources_fifa_chess.json       # FIFA and Chess.com source log
|-- package.json                       # Playwright and sharp visual pipeline commands
|-- artifact_manifest.json            # Last generation manifest and validation status
|-- GroupID-PA1-*.pdf                 # Final PDF deliverables
|-- GroupID-PA1.zip                   # Final package with four PDFs at top level
|-- GroupID-PA1-WorkDivision.docx     # Vietnamese work-division support document
|-- assets/
|   |-- figures_manifest.json          # Screenshot and solution figure manifest
|   |-- screenshots/raw/               # Playwright captures
|   |-- screenshots/annotated/         # sharp annotated screenshots
|   |-- screenshots/crops/             # UI detail crops
|   |-- diagrams/                      # Solution sketch figures
|-- scripts/
|   |-- capture-pa1-screenshots.js
|   |-- annotate-pa1-screenshots.js
|   |-- create_pa1_work_division_docx.py
|-- sources/
|   |-- GroupID-PA1-*.md              # Editable Markdown source artifacts
|   |-- mermaid-fifa-browse-watch-flow.mmd
|   |-- mermaid-chess-play-review-learn-flow.mmd
|   |-- mermaid-sprint-timeline.mmd
|-- docs/
|   |-- codex_context.md
|   |-- pa1_fifa_chess_migration_audit.md
|   |-- project_structure.md
|   |-- setup_and_run.md
|   |-- feature_progress.md
|   |-- session_handoff.md
```
