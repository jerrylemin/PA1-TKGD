# PA4 remediation history

This is a concise continuity index. Detailed evidence remains in the round-specific work logs and acceptance matrices.

## 2026-08-23 · Remediation round 2

- Starting readiness: `READY_FOR_REAL_PARTICIPANTS` was previously asserted, but the graph and source were stale relative to the round-2 contract.
- Issues addressed: Chess disclosure leakage, non-authoritative scenario/consequence, destination-only trial success, passive practice, FIFA participant-mode researcher chrome, audio-only recording promotion, fixed-order study wording, hesitation scoring ambiguity, divergent/hardcoded report state, PDF URL escaping, avoidable pagination, and premature official package generation.
- Key files changed: `prototype/app.js`, `prototype/index.html`, `prototype/styles.css`, `qa/validate_chess_scenario.py`, `scripts/capture-prototype-qa.mjs`, `study/analysis/analyze_study.py`, `study/analysis/test_analyze_study.py`, `scripts/build_pa4_reports.py`, `scripts/test_build_pa4_reports.py`, `scripts/package_pa4.py`, study protocol/recording docs, round-2 work logs, and round-2 acceptance matrix.
- Validation: Chess validator PASS; 15 analysis tests PASS; 3 shared-report-model tests PASS; browser QA PASS with no console errors; generated reports PASS URL/pagination checks; working ZIP PASS; official ZIP REFUSED with explicit external blockers and prior official ZIP preserved.
- Final local readiness: `READY_FOR_REAL_PARTICIPANTS`.
- Remaining external blockers: real YouTube URL, five or more real participants, consented session videos, task results, questionnaire responses, interview evidence, final evidence-backed analysis, and official Weekly Report template if unavailable.
- Memory boundary: study CSVs remain schema-only; no participant media, identities, quotes, timings, or findings were added.
