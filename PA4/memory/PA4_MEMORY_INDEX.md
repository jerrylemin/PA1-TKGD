# PA4 Memory Index

## 1. Purpose

This directory is the human/Codex navigation layer for the PA4 knowledge graph. It preserves continuity, decisions, evidence boundaries, source classifications, coverage, validation, and the next update procedure.

## 2. Source-of-truth boundary

PA4 repository artifacts remain authoritative. Graph nodes and query answers are navigation aids. When a graph statement conflicts with a source file or current QA result, inspect the source and update the memory adapter rather than trusting the graph.

## 3. Current PA4 state

Read [PA4_CURRENT_STATE.md](continuity/PA4_CURRENT_STATE.md) first. The offline demonstrator contains the FIFA Status Dashboard and current Chess Beginner Review flow, deterministic QA, study materials, schemas, and report/package builders. Round 2 validated Chess source-to-destination interaction, study-mode DOM boundaries, video-stream recording verification, shared report content, and official package refusal. The local handoff is `READY_FOR_REAL_PARTICIPANTS`; `SUBMISSION_READY` is not asserted.

## 4. Continuity and decision chain

- [PA1_CONTINUITY.md](continuity/PA1_CONTINUITY.md) records the browse-first FIFA trust problem and action-first Chess learning bridge.
- [PA2_CONTINUITY.md](continuity/PA2_CONTINUITY.md) records the evidence chains that selected the FIFA Status Dashboard and Chess Beginner Review direction.
- [PA3_CONTINUITY.md](continuity/PA3_CONTINUITY.md) records selected directions, formative AI-agent results, and remaining risks. Those results are not human-participant evidence.
- [PROJECT_DECISION_CHAIN.md](continuity/PROJECT_DECISION_CHAIN.md) is the shortest cross-phase explanation of why the two PA4 directions were promoted.

## 5. Glossary, traceability, and history

[PROJECT_GLOSSARY.md](continuity/PROJECT_GLOSSARY.md) defines `READY_FOR_REAL_PARTICIPANTS`, `SUBMISSION_READY`, `VERIFIED_RECORDING`, `BLOCKED_EXTERNALLY`, and `INFERRED`. [TRACEABILITY_AND_SCHEMA_INDEX.md](continuity/TRACEABILITY_AND_SCHEMA_INDEX.md) records the nine PA3-to-PA4 rows, header-only study schemas, generated analysis outputs, and deterministic adapters. [PA4_REMEDIATION_HISTORY.md](PA4_REMEDIATION_HISTORY.md) is the concise round history for future recovery.

## 6. Source manifest and coverage

[MEMORY_SOURCE_MANIFEST.csv](MEMORY_SOURCE_MANIFEST.csv) classifies PA4 files and sensitivity decisions. [GRAPH_COVERAGE.md](GRAPH_COVERAGE.md) records the current detection result: 70 files, 119,880 words, 13 code, 37 documents, 4 papers, 16 images, and 0 video files.

## 7. Machine graph artifacts

- `../graphify-out/graph.json` — machine-readable graph.
- `../graphify-out/GRAPH_REPORT.md` — communities, hubs, gaps, and confidence summary.
- `../graphify-out/graph.html` — visual graph.
- `../graphify-out/manifest.json` — Graphify incremental file manifest.
- `../graphify-out/BENCHMARK.json` — Graphify token-reduction benchmark.

The current graph contains 584 nodes, 909 links, and 82 communities. The final graph was rebuilt through Graphify APIs after the AST-only incremental update; `graph.json` was not edited by hand.

## 8. Query and path validation

[GRAPH_QUERY_VALIDATION.md](GRAPH_QUERY_VALIDATION.md) contains ten required round-2 queries, three smoke queries, six current path checks, and five explain checks. Concise Q&A results are saved under `../graphify-out/memory/` for the Graphify feedback loop.

## 9. Study evidence and privacy

Study input CSVs are header-only. There are no participant media files. Do not infer human outcomes from fictional prototype content, synthetic fixtures, empty schemas, formative AI-agent results, or generated reports. Keep future recordings local and consent-controlled.

## 10. Incremental maintenance

[UPDATE_MEMORY.md](UPDATE_MEMORY.md) is the operational resume point. Code changes use `graphify update PA4`; document/image changes require a local semantic extraction pass and refreshed graph artifacts.

## 11. Acceptance and unresolved blockers

[MEMORY_ACCEPTANCE.md](MEMORY_ACCEPTANCE.md) records the infrastructure, freshness, graph-query, and source-boundary checks. External submission gates remain a separate project state and are not silently promoted by this graph.
