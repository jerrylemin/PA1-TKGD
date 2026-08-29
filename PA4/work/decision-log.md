# PA4 decision log

Decision date: 2026-08-23

| Condition | Evidence | Decision |
|---|---|---|
| PA3 selected directions remain supported | PA3 selected FIFA Alt 1 and Chess Alt 1; both retained the clearest core task and a bounded revision path. | Promote both directions to hi-fi. |
| Unresolved issue is addressable by localized redesign | FIFA pending/ownership/handoff issues and Chess start/terminology/practice issues are explicit in PA3. | Preserve the selected directions and patch the affected interactions. |
| Real summative evidence exists | No PA4 participant rows, recordings, questionnaire answers, interview coding, or timing records exist. | Build collection schema, scripts, and report scaffold; mark results `BLOCKED EXTERNALLY`. |
| Genuine YouTube demo links exist | No PA4 YouTube URL exists locally. | Put the exact visible gate `YouTube demo link: REQUIRED EXTERNAL EVIDENCE BEFORE SUBMISSION` on hi-fi report page 1; never invent a URL. |
| Existing PA4 implementation exists | PA4 contained only the official brief PDF. | Start a dependency-free prototype under `PA4\prototype`. |

## Product decisions

### FIFA

Refine the Status Dashboard. The hi-fi flow keeps status first, then explanation, then next action. Pending is defined as awaiting FIFA confirmation; owner, expected timing, official source, and last-updated state are adjacent. View Order, View Tickets, Add to Calendar, and Transfer Tickets are functional. External actions open a guardrail modal with partner name, destination, context preservation, and Stay/Continue choices. Return restores the dashboard context.

### Chess

Refine the Beginner Review Flow. The hi-fi flow starts at an explicit `Start Beginner Review` state, moves one mistake at a time, explains the move in plain language, reveals a better move, supports a try/retry state, carries a visible practice bridge, and offers a beginner-help path plus a return to review. Advanced detail stays secondary.

## Current-state conclusion

FIFA PA4 should refine the validated Status Dashboard rather than restart the FIFA experience.

Chess PA4 should refine the validated Beginner Review Flow rather than restart the Chess experience.
