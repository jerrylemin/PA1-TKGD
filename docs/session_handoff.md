# Session Handoff

Current state: PA1 package has been migrated and regenerated for FIFA and Chess.com.

Important files:

- Final zip: `GroupID-PA1.zip`
- Final PDFs: `GroupID-PA1-ProductResearch.pdf`, `GroupID-PA1-PotentialSolutions.pdf`, `GroupID-PA1-PeerReview.pdf`, `GroupID-PA1-WeeklyReport.pdf`
- Generator: `build_pa1_package.py`
- Visual pipeline: `npm run visuals:pa1`
- Visual manifest: `assets/figures_manifest.json`
- Shared data: `pa1_project_data.json`
- Source log: `pa1_sources_fifa_chess.json`
- Audit: `docs/pa1_fifa_chess_migration_audit.md`

Next session guidance:

- To change group ID or member names, edit constants near the top of `build_pa1_package.py` and rerun it.
- To change evidence, edit `SOURCES` and cited findings in `build_pa1_package.py`, then rerun.
- Do not hand-edit generated PDFs; regenerate from the shared script.
