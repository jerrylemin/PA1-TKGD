---
type: "query"
date: "2026-08-23T17:25:49.929779+00:00"
question: "Where does the Summative User Study report obtain participant and evidence status?"
contributor: "graphify"
source_nodes: ["Summative report participant and evidence status from canonical analysis", "Summative report reads canonical analysis state", "analysis-result.json"]
---

# Q: Where does the Summative User Study report obtain participant and evidence status?

## Answer

The Summative report reads analysis-result.json through the canonical model. Participant, recording, task, questionnaire, interview, and blocked-state values are dynamic and shared across substantive DOCX/PDF content.

## Source Nodes

- Summative report participant and evidence status from canonical analysis
- Summative report reads canonical analysis state
- analysis-result.json