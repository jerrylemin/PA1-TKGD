# Session Handoff

Current state: PA1 package has been final-fixed and regenerated for FIFA.com and Chess.com.

Important files:

- Final zip: `GroupID-PA1.zip`
- Final PDFs: `GroupID-PA1-ProductResearch.pdf`, `GroupID-PA1-PotentialSolutions.pdf`, `GroupID-PA1-PeerReview.pdf`, `GroupID-PA1-WeeklyReport.pdf`
- WorkDivision: `GroupID-PA1-WorkDivision.docx` and `output/GroupID-PA1-WorkDivision.docx`
- Generator: `build_pa1_package.py`
- Visual pipeline: `npm run visuals:pa1`
- Visual manifest: `assets/figures_manifest.json`
- Shared data: `pa1_project_data.json`
- Source log: `pa1_sources_fifa_chess.json`
- Final-fix audit: `docs/pa1_final_10_10_audit_after_fix.md`
- Final-fix validation: `docs/pa1_final_fix_validation.md`

Next session guidance:

- To change group ID or member names, edit constants near the top of `build_pa1_package.py` and rerun it.
- To change evidence, edit `SOURCES` and cited findings in `build_pa1_package.py`, then rerun.
- Do not hand-edit generated PDFs; regenerate from the shared script.
- Manual item: replace `GroupID` with the real group ID when available.
