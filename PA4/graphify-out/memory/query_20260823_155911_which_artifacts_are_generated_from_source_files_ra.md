---
type: "query"
date: "2026-08-23T15:59:11.770845+00:00"
question: "Which artifacts are generated from source files rather than manually authored?"
contributor: "graphify"
---

# Q: Which artifacts are generated from source files rather than manually authored?

## Answer

scripts/build_pa4_reports.py generates the PA4 DOCX/PDF reports; scripts/package_pa4.py packages them; Graphify generates graph.json, GRAPH_REPORT.md, graph.html, and benchmark output. Source documents remain authoritative.