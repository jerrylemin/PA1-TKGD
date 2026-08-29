# PA4 Graph Coverage

Run date: 2026-08-23  
Graphify: 0.8.18  
Root: `PA4/`  
Graph: `PA4/graphify-out/graph.json`

## Current build summary

Graphify detection currently finds 70 files: 13 code, 37 documents, 4 papers, 16 images, and 0 video files, with 119,880 words and 23 ignore patterns. No sensitive files were skipped. The final navigation graph contains 584 nodes, 909 links, and 82 communities.

The mandatory `graphify update PA4` completed after the remediation and rebuilt the AST layer. Because Graphify 0.8.18's CLI update is AST-only for this workspace, the final graph was then rebuilt through Graphify's `build`, `cluster`, and `export` APIs using the refreshed AST plus a validated local semantic fragment. `graphify cluster-only PA4 --graph PA4/graphify-out/graph.json` regenerated `GRAPH_REPORT.md` and `graph.html`. `graph.json` was never edited by hand.

## Coverage matrix

| Source family | Detected | Current representation | Status and notes |
|---|---:|---|---|
| Prototype and runtime QA | 13 code/JSON files | Current `app.js`, HTML/CSS, Chess validator, browser QA, analysis, report, and package surfaces | PASS; current Qh5/Nxh5/Qe2/Qd3 flow is indexed |
| Study protocol and continuity | 37 documents | Study plan, facilitator script, recording policy, report source/sidecars, work context, and memory continuity | PASS; current readiness and external-blocker state are indexed |
| Brief and final PDFs | 4 papers | Official brief plus current Hi-fi, Summative, and Weekly outputs | PASS; generated artifacts are linked back to source/report nodes |
| Prototype screenshots | 16 images | Current FIFA/Chess desktop and mobile evidence nodes | PASS; screenshots demonstrate prototype behavior only, not participant findings |
| Recordings and participant media | 0 video files | Recording policy and validator nodes | PASS; absent recordings remain an external blocker, not a participant result |
| Study schema CSVs | Included in detection, not auto-parsed as graph nodes | Explicit schema/zero-row adapter and analysis-result nodes | PASS; no participant values are copied or inferred |
| ZIP archives and build noise | Excluded by project ignore policy | Working/official package concepts remain in the semantic graph | PASS; archive contents are not recursively indexed |
| Sensitive files | 0 skipped | None | PASS |

## Current semantic anchors

The refreshed graph contains source-backed or explicitly validated anchors for:

- `READY_FOR_REAL_PARTICIPANTS` versus the separate `SUBMISSION_READY?` state;
- current Chess disclosure, Qh5/Nxh5 ground truth, source-to-destination trial input, wrong-move feedback, and interactive Qd3 practice;
- FIFA study-mode chrome removal versus presenter tools;
- positive-duration/video-stream recording verification, audio-only rejection, and unverified media;
- `condition_order`, separate `hesitation_count`, canonical `analysis-result.json`, dynamic report state, URL escaping, and pagination;
- working evidence archive versus the refused official package gate; and
- current prototype screenshots and generated reports without participant evidence.

## Provenance boundary

Source files remain authoritative. `EXTRACTED` edges are direct source relationships; `INFERRED` edges remain hypotheses until source verification. Header-only study CSVs, absent recordings, and external blockers are not participant findings. Synthetic fixtures remain test-only and were not copied into real evidence directories.

The pre-refresh graph contained stale Qa4/Qc2 semantic nodes. This source/graph conflict is recorded in the remediation memory and was resolved by treating current source and validation output as authoritative; the current graph contains no `Qa4`, `Qc2`, `Move 8`, `loose c3`, or `c3 pawn` labels.
