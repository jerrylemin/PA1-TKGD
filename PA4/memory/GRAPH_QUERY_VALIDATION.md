# Graph Query Validation

Run date: 2026-08-23  
Graphify: 0.8.18  
Graph: `PA4/graphify-out/graph.json`  
Final graph: 584 nodes, 909 links, 82 communities  
Command form: `graphify query "<question>" --graph PA4/graphify-out/graph.json --budget 550`

All ten required round-2 continuity queries exited 0 after the final Graphify refresh. The answers were also filed with `graphify save-result` under `PA4/graphify-out/memory/`. The graph contains no stale `Qa4`, `Qc2`, `Move 8`, `loose c3`, or `c3 pawn` labels.

## Required post-update queries

| ID | Exact question | Result |
|---|---|---|
| Q01 | What is the current PA4 readiness state and why? | PASS — returns `READY_FOR_REAL_PARTICIPANTS`, current blocked participant count, external blockers, canonical report state, and the official package gate. |
| Q02 | What defects from remediation round 2 were fixed? | PASS — returns the round-2 acceptance matrix, current Chess flow, current screenshots, and historical context without stale Chess labels. |
| Q03 | How does the current Chess trial interaction work? | PASS — returns Qh5/Nxh5, source-to-destination input, wrong-move feedback, and the practice continuation. |
| Q04 | How does the current Chess practice flow work? | PASS — returns interactive practice, retry behavior, Qd3, and the current Chess trial chain. |
| Q05 | What does FIFA study mode hide compared with presenter mode? | PASS — returns the study-mode boundary, presenter tools, and current FIFA screenshots. |
| Q06 | How is a recording verified as a valid video recording? | PASS — the query alias resolves to the positive-duration/video-stream rule, audio-only rejection, unverified-media state, validator, and analysis result. |
| Q07 | How does condition_order affect the summative study procedure? | PASS — returns counterbalanced order, the order-neutral procedure, canonical analysis, and report source. |
| Q08 | Where does the Summative User Study report obtain participant and evidence status? | PASS — returns the canonical report model, `analysis-result.json`, and dynamic participant/recording/task/questionnaire/interview state. |
| Q09 | When is Group10-PA4.zip allowed to be generated? | PASS — returns the official gate, local readiness state, external blockers, and working-evidence archive. |
| Q10 | What still blocks SUBMISSION_READY? | PASS — returns the separate `SUBMISSION_READY?` alias, external blockers, official gate, and `READY_FOR_REAL_PARTICIPANTS` distinction. |

## Query smoke tests

| Question | Result |
|---|---|
| Why FIFA Status Dashboard selected? | PASS — source-backed FIFA Status Dashboard and PA1–PA4 decision-chain context returned. |
| What blocks SUBMISSION_READY? | PASS — external blocker alias, official gate, and separate local-readiness state returned. |
| Which script builds the official PA4 package? | PASS — `package_pa4.py`, working archive, and official gate returned. |

## Post-update path tests

These use the exact current node labels returned by `graphify explain` or by the query result. Graphify emitted ambiguity warnings for some natural-language matches, but each selected endpoint and path was the expected source-backed node.

| ID | Path | Result |
|---|---|---|
| P01 | `Current Participant Chess Flow` → `Current Chess scenario Qh5 Nxh5` | PASS — 1 hop through `contains`. |
| P02 | `Current Chess scenario Qh5 Nxh5` → `Chess trial requires source-to-destination input` | PASS — 1 hop through `leads_to`. |
| P03 | `Chess trial requires source-to-destination input` → `Interactive Chess practice with retry` | PASS — 1 hop through `advances_to`. |
| P04 | `Current PA4 recording evidence` → `Current PA4 recording video validator` | PASS — 1 hop through `validated_by`. |
| P05 | `Current PA4 recording video validator` → `Summative report state` | PASS — 3 hops through the video-stream gate and `analyze()`. |
| P06 | `READY_FOR_REAL_PARTICIPANTS` → `Group10-PA4-WorkingEvidence.zip` | PASS — 2 hops through the official package gate. |

## Explain tests

| Node | Result |
|---|---|
| `Current Chess scenario: Qh5 is met by Nxh5` | PASS — `prototype/app.js`, connected to current flow, Qe2, trial, validator, and screenshot nodes. |
| `Current Participant Chess Flow` | PASS — `prototype/README.md`, connected to the current scenario, historical review flow, acceptance matrix, and current screenshots. |
| `FIFA Status Dashboard` | PASS — `memory/continuity/PROJECT_DECISION_CHAIN.md`, connected to PA1–PA4 continuity and the selection rationale. |
| `analyze()` | PASS — `study/analysis/analyze_study.py` L410, connected to all gates and the canonical Summative report model. |
| `package_pa4.py` | PASS — `scripts/package_pa4.py` L1, connected to the working archive, readiness validator, blockers, and official gate. |

## Interpretation

Graphify is a navigation and continuity layer. A PASS means the graph returned a useful, source-located neighborhood or path; it does not promote an inferred edge into proven history and it does not convert empty study schemas, absent recordings, or synthetic fixtures into participant evidence.
