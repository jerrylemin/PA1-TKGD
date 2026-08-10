# Project Structure

Generated from tracked repository files on 2026-07-07. Depth is limited to four path segments; dependency, Git-object, archive contents, and render-frame listings are summarized.

```text
.
|-- build_pa1_package.py
|-- package.json
|-- package-lock.json
|-- pa1_project_data.json
|-- pa1_sources_fifa_chess.json
|-- artifact_manifest.json
|-- Group10-PA1-ProductResearch.pdf
|-- Group10-PA1-PotentialSolutions.pdf
|-- Group10-PA1-PeerReview.pdf
|-- Group10-PA1-WeeklyReport.docx
|-- Group10-PA1-WeeklyReport.pdf
|-- Group10-PA1-WeeklyReport-Review.md
|-- Group10-PA1-PeerReview-Revised.docx
|-- Group10-PA1-PeerReview-Revised.pdf
|-- Group10-PA1-PeerReview-Revised-English.pdf
|-- Group10-PA1-PeerReview-Review.md
|-- Group10-PA1-WorkDivision.docx
|-- PA1.pptx
|-- Group10-PA1.zip
|-- assets/
|   |-- figures_manifest.json
|   |-- diagrams/
|   |   |-- mermaid/                 # Six canonical .mmd sources
|   |   |-- rendered/                # Six rendered traceability/workflow PNGs
|   |   |-- s-01_fifa_solution.png ... s-08_chess_solution.png
|   |-- screenshots/
|   |   |-- raw/{fifa,chess}/
|   |   |-- annotated/{fifa,chess}/
|   |   |-- crops/{fifa,chess}/
|   |-- presentation/
|       |-- raw/{fifa,chess}/
|       |-- annotated/{fifa,chess}/
|       |-- crops/{fifa,chess}/
|       |-- presentation_visual_manifest.json
|-- config/                          # PA1 naming/link configuration (created by strict-fix pass)
|-- sources/
|   |-- Group10-PA1-ProductResearch.md
|   |-- Group10-PA1-PotentialSolutions.md
|   |-- Group10-PA1-PeerReview.md
|   |-- Group10-PA1-WeeklyReport.md
|   |-- mermaid-fifa-browse-watch-flow.mmd
|   |-- mermaid-chess-play-review-learn-flow.mmd
|   |-- mermaid-sprint-timeline.mmd
|-- generated_text/
|   |-- Group10-PA1-ProductResearch.txt
|   |-- Group10-PA1-PotentialSolutions.txt
|   |-- Group10-PA1-PeerReview.txt
|   |-- Group10-PA1-WeeklyReport.txt
|-- scripts/
|   |-- capture-pa1-screenshots.js
|   |-- annotate-pa1-screenshots.js
|   |-- annotate_presentation_screenshots.js
|   |-- create_pa1_work_division_docx.py
|   |-- create_teacher_feedback_response.py
|   |-- create_teacher_feedback_response_english.py
|   |-- validate_pa1_balance_diagrams.py
|   |-- validate_pa1_final_fix.py
|   |-- validate_pa1_submission.py   # Strict draft/final validator (created by strict-fix pass)
|-- docs/
|   |-- codex_context.md
|   |-- project_structure.md
|   |-- setup_and_run.md
|   |-- feature_progress.md
|   |-- session_handoff.md
|   |-- pa1_strict_gap_audit.md
|   |-- pa1_submission_blockers.md
|   |-- pa1_final_validation_report.md
|   |-- google_drive_readme_template.md
|   |-- other historical audit and visual-QA reports
|-- output/
|   |-- Group10-PA1-WorkDivision.docx
|   |-- Group10-PA1-{ProductResearch,PotentialSolutions,PeerReview,WeeklyReport}.pdf
|   |-- Group10-PA1.zip
|   |-- artifact_manifest.json
|   |-- presentation_render_before/ # 21 slide PNGs + contact sheet
|   |-- presentation_render_after/  # 21 slide PNGs + contact sheet
|-- archive/
|   |-- previous_pa1_outputs_20260610_233509/ # Historical four PDFs + ZIP
|-- node_modules/                    # Installed dependencies; never edited directly
|-- .git/
```
