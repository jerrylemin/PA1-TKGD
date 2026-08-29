---
type: "query"
date: "2026-08-23T17:29:44.719810+00:00"
question: "Which script builds the official PA4 package?"
contributor: "graphify"
source_nodes: ["package_pa4.py", "Official Group10-PA4.zip gate", "Group10-PA4-WorkingEvidence.zip"]
---

# Q: Which script builds the official PA4 package?

## Answer

PA4/scripts/package_pa4.py builds the working evidence archive and guards the official Group10-PA4.zip gate through validate_local_readiness, submission_blockers, and build_submission_zip.

## Source Nodes

- package_pa4.py
- Official Group10-PA4.zip gate
- Group10-PA4-WorkingEvidence.zip