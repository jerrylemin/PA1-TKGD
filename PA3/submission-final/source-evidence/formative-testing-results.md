# PA3 Requirement 2 - Formative Testing Results

## AI-Agent Formative Testing

### Method

Five independent AI reviewer agents were configured as novice users and evaluated all six paper prototypes using the same task-based formative testing protocol.

Each reviewer received the same FIFA and Chess scenarios, the same neutral moderator instruction, the same six fixed prototype images, a distinct novice profile, and a counterbalanced alternative order. Each reviewer evaluated FIFA Alt 1-3 and Chess Alt 1-3 independently. No reviewer received another reviewer's output, an aggregate conclusion, an expected winner, the design-team rationale, or the PA2 recommendation ranking.

The lead analyst saved the five isolated responses in ai-testing/R1.md through ai-testing/R5.md, verified coverage, and aggregated only after all five responses returned. Across the five sessions, the study produced 30 alternative evaluations and 285 task outcomes: 150 FIFA decisions and 135 Chess decisions.

### Outcome labels

- **Independent Success:** the reviewer identified the correct control or interpretation without moderator intervention.
- **Success With Hesitation:** the reviewer eventually succeeded but reported uncertainty, repeated scanning, or a wrong first path.
- **Failure:** the reviewer chose a wrong function, formed an incorrect mental model, or could not identify a workable action.

The notation I / H / F in the tables below means Independent Success / Success With Hesitation / Failure across five reviewers.

## Reviewer Profiles

| Reviewer | Digital literacy | Domain familiarity | Behavior | Assigned order |
|---|---|---|---|---|
| R1 | High | FIFA ticket familiarity low; Chess.com analysis none | Confident digital novice; explores quickly and expects obvious actions. | FIFA 1 -> 2 -> 3; Chess 1 -> 2 -> 3 |
| R2 | Medium | FIFA ticket familiarity none; Chess analysis none | Careful reader; reads labels before acting and notices terminology problems. | FIFA 2 -> 3 -> 1; Chess 2 -> 3 -> 1 |
| R3 | Low-to-medium | FIFA ticket familiarity none; Chess analysis none | Low-confidence novice; hesitates when many choices appear and prefers explicit guidance. | FIFA 3 -> 1 -> 2; Chess 3 -> 1 -> 2 |
| R4 | High | FIFA and Chess familiarity low | Fast scanner; scans headings, cards, status colors, and prominent actions first. | FIFA 1 -> 3 -> 2; Chess 1 -> 3 -> 2 |
| R5 | Medium | FIFA and Chess familiarity low | Guided-flow preference; prefers sequential instructions and clear next actions. | FIFA 2 -> 1 -> 3; Chess 2 -> 1 -> 3 |

## Scenario 1 Results - FIFA.com

### FIFA Alt 1 - Status Dashboard

**Task outcomes:** 31 / 50 Independent Success, 11 / 50 Success With Hesitation, 8 / 50 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| F1 status | 5 / 0 / 0 | Status tiles and event cards reliably exposed current state. |
| F2 pending/attention | 5 / 0 / 0 | Pending count and event card were visible; no-action state was readable. |
| F3 meaning | 2 / 3 / 0 | Plain-language labels helped, but reviewers wanted the content behind What does this mean?. |
| F4 next step | 0 / 2 / 3 | Awaiting FIFA confirmation did not define a next event, owner, or timing. |
| F5 currentness | 4 / 1 / 0 | Last updated: 2 mins ago was visible, but it was page-level rather than event-level. |
| F6 officiality | 0 / 5 / 0 | FIFA branding and URL suggested legitimacy, but no explicit official-source marker was shown. |
| F7 View Tickets | 5 / 0 / 0 | The confirmed event card exposed a direct action. |
| F8 Transfer Tickets | 5 / 0 / 0 | Quick Actions exposed a direct transfer path. |
| F9 Add to Calendar | 5 / 0 / 0 | The label and calendar icon were immediately recognizable. |
| F10 external handoff | 0 / 0 / 5 | No visible message explained what happens before an external service opens. |

**Common observations:** R1, R3, R4, and R5 looked first at the summary tiles, then used event cards; R2 read the status copy and compared View Order with View Tickets. All five recognized the confirmed/pending distinction. The dashboard communicates the current situation and common actions more effectively than the next state or partner boundary.

**Positive feedback:** Reviewers repeatedly valued the compact status summary, event-level labels, direct Quick Actions, and the visible 0 Action needed signal. R1 described the summary as a fast current-state check; R3 and R5 valued the status-to-action path.

**Problems:** The repeated High themes were the missing pending next step (F4, R1-R5) and missing external-service explanation (F10, R1-R5). Medium issues included ambiguous View Order versus View Tickets, page-level freshness, similar pending labels, and a help link whose result was not visible.

**Points of improvement:** Add Current status, Next step, Expected timing, and Owner to each event card; state explicitly whether the reviewer should wait or act; add an Official FIFA source label beside freshness; explain View Order versus View Tickets; place a handoff warning beside any outgoing action; keep status colors paired with text.

### FIFA Alt 2 - Timeline Tracker

**Task outcomes:** 26 / 50 Independent Success, 9 / 50 Success With Hesitation, 15 / 50 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| F1 status | 5 / 0 / 0 | The current stage and ON TRACK/PENDING labels were clear. |
| F2 pending/attention | 5 / 0 / 0 | Pending payment and unfinished stages were visible, but ownership was not. |
| F3 meaning | 2 / 3 / 0 | Progress was readable; Payment received - Pending and Verification required interpretation. |
| F4 next step | 4 / 1 / 0 | Ticket ready - 72h before match gave a concrete expected milestone. |
| F5 currentness | 5 / 0 / 0 | Last-updated, What changed?, and update history supported freshness. |
| F6 officiality | 5 / 0 / 0 | The Official FIFA source badge was directly visible. |
| F7 View Tickets | 0 / 0 / 5 | No direct View Tickets control was visible. |
| F8 Transfer Tickets | 0 / 0 / 5 | No direct Transfer Tickets control was visible. |
| F9 Add to Calendar | 0 / 5 / 0 | Sync to calendar was the closest visible action, but the wording was not equivalent. |
| F10 external handoff | 0 / 0 / 5 | Official-source copy did not explain leaving FIFA.com. |

**Common observations:** All five reviewers used the timeline, current marker, update history, and official-source badge to understand progress. The timeline was strongest for current stage, future milestone, freshness, and provenance. It was weakest when the task changed from monitoring to acting.

**Positive feedback:** Reviewers valued the numbered stages, Ticket ready - 72h before match, Last updated, What changed?, and View update history. R2 preferred the timeline because it supported a careful reading of status and freshness; R5 made the same preference despite the missing action controls.

**Problems:** The same High issues appeared across the five records: missing View Tickets and Transfer Tickets controls (F7/F8) and no external handoff warning (F10). Medium issues included Sync to calendar, unclear ownership of a pending stage, and information density in the full timeline.

**Points of improvement:** Add a compact ticket action row with View Tickets, Transfer Tickets, and Add to Calendar; rename or explain Sync to calendar; attach Official Next Steps to the selected ticket and current stage; state whether payment verification requires user action; add a Before you leave FIFA.com notice before partner navigation.

### FIFA Alt 3 - Action Hub

**Task outcomes:** 37 / 50 Independent Success, 3 / 50 Success With Hesitation, 10 / 50 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| F1 status | 3 / 2 / 0 | Confirmed status was clear, but only one event was represented. |
| F2 pending/attention | 0 / 0 / 5 | No pending or attention-needed information was visible. |
| F3 meaning | 5 / 0 / 0 | Confirmed and Tickets are valid were direct. |
| F4 next step | 0 / 0 / 5 | Shortcuts did not supply a ticket lifecycle or expected next step. |
| F5 currentness | 5 / 0 / 0 | Last updated and refresh were visible. |
| F6 officiality | 5 / 0 / 0 | Official FIFA source and Official option labels were visible. |
| F7 View Tickets | 5 / 0 / 0 | View Tickets appeared on the event card and in Quick Actions. |
| F8 Transfer Tickets | 5 / 0 / 0 | Transfer Tickets was a prominent shortcut. |
| F9 Add to Calendar | 5 / 0 / 0 | Add to Calendar was a prominent shortcut. |
| F10 external handoff | 4 / 1 / 0 | The bottom Before you leave FIFA.com notice was useful but separated from individual actions. |

**Common observations:** All five reviewers found common actions quickly. The Action Hub had the clearest official-source and partner-handoff language, but it presented one confirmed event and no visible progressing state. The large action grid competed with the smaller status area and several optional services.

**Positive feedback:** Reviewers consistently valued the direct labels, action descriptions, Official Options, security message, and Before you leave FIFA.com banner. R1, R3, R4, and R5 described the action shortcuts as fast or prominent.

**Problems:** All five reviewers reported the missing pending state and missing next expected step (F2/F4). Medium issues included optional services competing with core ticket actions, duplicated support/resale terms, and the handoff notice being visually distant from the action that triggers it.

**Points of improvement:** Add confirmed, pending, and action-needed status summaries; add a per-event next-step and timing line; state No pending items when appropriate; attach external-destination copy to each outgoing option; separate core ticket management from optional partner services; keep text labels alongside color and icons.

### FIFA Cross-Reviewer Comparison

| Dimension | Alt 1 - Status Dashboard | Alt 2 - Timeline Tracker | Alt 3 - Action Hub |
|---|---|---|---|
| Status clarity | Strong: 5/5 identified current state independently. | Strong: 5/5 found current stage and status. | Mixed: 3/5 independent; 2/5 hesitated because only one event was shown. |
| Progress clarity | Limited: current state is clearer than what comes next. | Strongest: current, next, timing, freshness, and update history are visible. | Weak: shortcuts do not explain ticket progression. |
| Task discovery | Strong: F7-F9 were 15/15 independent. | Weak: F7/F8 were 0/10 independent. | Strong: F7-F9 were 15/15 independent. |
| Trust | Medium: branding/URL suggested officiality; explicit source and handoff were absent. | Strong source signal; partner handoff still absent. | Strongest source and handoff copy; placement still needs tightening. |
| Next-step clarity | Weak: F4 had 0/5 independent and F10 had 0/5. | Strongest: F4 had 4/5 independent; F10 still failed. | Weak: F4 had 0/5 independent; F2 also failed for all five. |
| Hesitation pattern | Pending meaning, next step, source, and View Order wording. | Pending wording, calendar label, and action absence. | Full-state understanding and action-grid density. |
| High-severity issues | F4/F10 themes affected R1-R5. | F7/F8/F10 themes affected R1-R5. | F2/F4 themes affected R1-R5. |
| Reviewer preference | 3/5: R1, R3, R4. | 2/5: R2, R5. | 0/5. |
| Main strength | Balanced state summary plus common actions. | Best progress and provenance explanation. | Fastest common actions and clearest handoff. |
| Main weakness | Does not turn pending state into a next step or explain handoff. | Does not expose common ticket actions. | Does not show pending state or ticket lifecycle. |

## Scenario 2 Results - Chess.com

### Chess Alt 1 - Beginner Review Flow

**Task outcomes:** 36 / 45 Independent Success, 8 / 45 Success With Hesitation, 1 / 45 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| C1 start review | 2 / 3 / 0 | The named Beginner Review mode helped, but the step-2 opening confused some reviewers. |
| C2 important mistake | 5 / 0 / 0 | The red mistake panel and move label were consistently findable. |
| C3 why it is a mistake | 5 / 0 / 0 | Plain-language cause and consequence were understood. |
| C4 better move | 5 / 0 / 0 | Better move was directly labeled. |
| C5 why it is better | 4 / 1 / 0 | The protection reason was clear; develops safely and notation needed explanation. |
| C6 try/inspect move | 5 / 0 / 0 | Show me on the board and Try this move were visible. |
| C7 practice activity | 5 / 0 / 0 | Practice this idea and Start practice formed a direct bridge. |
| C8 another moment | 5 / 0 / 0 | Next mistake provided a clear continuation. |
| C9 additional help | 0 / 4 / 1 | Full Analysis was visible but did not read as beginner help. |

**Common observations:** All five reviewers recognized the guided chain from mistake to explanation, better move, practice, and next mistake. The main friction was the screen opening at Step 2 of 3 and the presence of multiple progress concepts: review step, mistake count, and game move.

**Positive feedback:** The plain-language mistake explanation, visible Better move, Try this move, Practice this idea, and Next mistake were the clearest learning sequence in the study. All five reviewers preferred this alternative.

**Problems:** The recurring improvement needs were a clearer start/restart, inline explanations for Qd3/Qe2/...Nxd4 and terms such as develops safely or hanging pieces, a visible result after Try this move, and a beginner-oriented alternative to Full Analysis. R5 marked C9 as Failure; R1, R2, R3, and R4 marked it Success With Hesitation.

**Points of improvement:** Add Start Beginner Review or Start with the most important mistake; distinguish Review step, Mistake, and Game move counters; pair notation with plain-language move descriptions; show the result of Try this move; add Explain another way or Need more help?; keep Review another moment visible.

### Chess Alt 2 - Card Review Mode

**Task outcomes:** 34 / 45 Independent Success, 11 / 45 Success With Hesitation, 0 / 45 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| C1 start review | 0 / 5 / 0 | All five eventually selected a card but hesitated because no card was recommended first. |
| C2 important mistake | 5 / 0 / 0 | Summary cards and key-moment labels exposed mistakes. |
| C3 why it is a mistake | 5 / 0 / 0 | Expanded card copy explained the mistake. |
| C4 better move | 5 / 0 / 0 | Better move was clearly labeled. |
| C5 why it is better | 4 / 1 / 0 | Qxc3 and material were understandable with some terminology friction. |
| C6 try/inspect move | 5 / 0 / 0 | Try this move and Analysis Board were visible. |
| C7 practice activity | 5 / 0 / 0 | Go to puzzle was a direct practice route. |
| C8 another moment | 5 / 0 / 0 | Choose another card and the card grid supported continuation. |
| C9 additional help | 0 / 5 / 0 | Analysis Board was found as a deeper route but sounded advanced. |

**Common observations:** The selected card connected mistake, reason, better move, try action, and puzzle in one unit. The card grid, summary metrics, filters, and checkbox-like controls created a recognition-first but choice-heavy starting point.

**Positive feedback:** All five reviewers valued the direct Go to puzzle bridge and the way a selected card kept the evidence and next actions together. R2 and R4 noted that a careful reader or fast scanner can compare cards effectively once a card is selected.

**Problems:** C1 was Success With Hesitation for all five; R3 marked the choice load High. Unexplained terms included Missed Tactic, Blunder, Opening, Endgame, material, and Analysis Board. The selected/completed state was not always distinguishable.

**Points of improvement:** Mark one card Start here and explain why; replace checkbox-like affordances with Open review; add plain-language category descriptions; explain what Analysis Board provides; keep Try this move and Go to puzzle; use text labels as well as color.

### Chess Alt 3 - Side-by-Side AI Assistant

**Task outcomes:** 26 / 45 Independent Success, 14 / 45 Success With Hesitation, 5 / 45 Failure.

| Task | I / H / F | Cross-reviewer reading |
|---|---:|---|
| C1 start review | 0 / 5 / 0 | Assistant, Key Moments, and free-form input offered possible starts but no recommended first action. |
| C2 important mistake | 5 / 0 / 0 | Red Qd3 in Key Moments was consistently findable. |
| C3 why it is a mistake | 5 / 0 / 0 | The assistant explained the move in context. |
| C4 better move | 5 / 0 / 0 | Qe2 was visible in the answer. |
| C5 why it is better | 3 / 2 / 0 | The answer was understandable but the c3/e2 relationship required reconciliation. |
| C6 try/inspect move | 0 / 5 / 0 | Reviewers could inspect highlights or Show variations but did not see Try this move. |
| C7 practice activity | 0 / 0 / 5 | No contextual puzzle or practice route was visible. |
| C8 another moment | 3 / 2 / 0 | Key Moments provided a route, but no explicit Next mistake/next key moment control existed. |
| C9 additional help | 5 / 0 / 0 | Suggested questions and free-form input directly supported follow-up help. |

**Common observations:** The assistant kept the board, key moment, question, explanation, and follow-up prompts in context. It was strongest for asking why and weakest for starting, trying, and practicing.

**Positive feedback:** All five reviewers valued the plain-language answer, board highlights, mini-board feedback, suggested questions, and flexible follow-up. R2 specifically valued the ability to request more explanation without a separate support route.

**Problems:** All five reviewers reported C7 Failure because no concrete practice activity was connected to the explanation. All five marked C6 Success With Hesitation because the prototype showed inspection rather than a Try this move control. All five hesitated at C1. R2 and R5 flagged a consistency problem between the c3 loss explanation and the e2 protection explanation.

**Points of improvement:** Add Start with the biggest mistake, suggested starter prompts, Try this move/Play Qe2, Practice this idea/Go to puzzle, Next key moment, beginner explanations for tabs and notation, and a visible move sequence that reconciles c3, ...Bxc3, and Qe2.

### Chess Cross-Reviewer Comparison

| Dimension | Alt 1 - Beginner Review Flow | Alt 2 - Card Review Mode | Alt 3 - Side-by-Side AI Assistant |
|---|---|---|---|
| Where to start | Better than the other two but 3/5 hesitated at the Step 2 opening. | All five hesitated at card selection. | All five hesitated between Key Moments, Assistant, and free-form input. |
| Mistake comprehension | 5/5 independent. | 5/5 independent. | 5/5 independent. |
| Better-move comprehension | 4/5 independent, 1/5 hesitant. | 4/5 independent, 1/5 hesitant. | 3/5 independent, 2/5 hesitant. |
| Practice connection | 5/5 independent via Practice this idea. | 5/5 independent via Go to puzzle. | 0/5; all five failed to find a contextual practice activity. |
| Decision load | Low-to-medium; fixed path. | Highest; six cards, metrics, and filters compete. | Medium-high; tabs, board, assistant, Key Moments, and summary compete. |
| Flexibility | Lowest; can feel fixed. | High; user selects a card. | Highest; free-form questions and follow-ups. |
| Hesitation pattern | Start/restart, terminology, Full Analysis help. | First-card choice, terminology, Analysis Board. | Start, Try this move, next moment, and practice. |
| High-severity issues | One reviewer failed C9; otherwise mostly Medium issues. | High choice-load issue reported by R3 and R5. | Practice and move-action gaps were repeated across R1-R5. |
| Reviewer preference | 5/5. | 0/5. | 0/5. |
| Main strength | Clear beginner sequence from mistake to practice. | Strong card-level evidence and puzzle bridge. | Best contextual explanation and follow-up help. |
| Main weakness | Start and additional-help cues are under-specified. | Too many equal starting choices. | Explanation is not connected to trying and practice. |

## Prioritized Issues

### FIFA

| Priority | Issue type | Affected reviewers | Evidence | Severity | Revision |
|---|---|---|---|---|---|
| F-P0 | Workflow / Trust | R1-R5 | Alt 1 F4 and F10; all five lacked a pending next-step explanation and external handoff copy. | High | Add current state -> next step -> expected timing -> owner, plus a per-action external destination warning. |
| F-P0 | Visibility / Workflow | R1-R5 | Alt 2 F7/F8 were 0/10 independent; every reviewer searched for direct View Tickets and Transfer Tickets. | High | Add a compact action row to the timeline pattern or carry the actions into the selected direction. |
| F-P1 | Information hierarchy | R1-R5 | Alt 3 F2/F4 were 0/10 independent; the action grid displaced progressing-ticket information. | High | Keep the action model secondary to a compact status strip and next-step line. |
| F-P1 | Terminology / Consistency | R1-R5 | Pending, Awaiting update, Awaiting FIFA confirmation, View Order, and Sync to calendar required interpretation. | Medium | Use one status vocabulary and direct action labels; explain any necessary distinction inline. |
| F-P1 | Trust / Feedback | R1, R3, R4, R5 | Alt 1 freshness was page-level; source labels and handoff details were not adjacent to every event/action. | Medium | Pair Last updated and Official FIFA source with the selected event; show the result after refresh or handoff selection. |

### Chess

| Priority | Issue type | Affected reviewers | Evidence | Severity | Revision |
|---|---|---|---|---|---|
| C-P0 | Learning support / Workflow | R1-R5 | Alt 3 C7 was Failure for all five; no contextual puzzle or practice activity was visible. | High | Add Practice this idea or Go to puzzle beside the explanation. |
| C-P0 | Visibility / User control | R1-R5 | Alt 3 C6 was Success With Hesitation for all five; no Try this move action was visible. | High | Add Try this move/Play Qe2 and show the resulting board state. |
| C-P1 | Navigation / Cognitive load | R1-R5 | Alt 2 and Alt 3 C1 were Success With Hesitation for all five; no recommended start. | High | Add Start here/Start review and identify the first learning moment. |
| C-P1 | Terminology | R1-R5 | All three alternatives exposed notation or terms such as Qd3, Qe2, Qxc3, Blunder, Analysis Board, develops safely, and material. | Medium | Pair every term with plain-language meaning at first use. |
| C-P1 | Consistency / Trust | R2, R5 | Alt 3 connected losing c3 with protecting e2 without showing the move sequence. | High | Show the line or board transition that explains why Qe2 addresses the position. |
| C-P2 | Learning support | R1-R5 | Alt 1 C9 was 0/4/1; Full Analysis did not clearly promise beginner-friendly help. | Medium | Add Need more help? or Explain another way beside the current explanation. |

## Recommended Prototype Revisions

### Selected FIFA direction: Alt 1 - Status Dashboard

**Keep**

- Status tiles and event-level cards.
- Direct View Tickets, Transfer Tickets, and Add to Calendar actions.
- Visible Last updated signal and the no-action-needed status.

**Improve**

- Add Current status, Next step, Expected timing, Owner, and No action needed or Action required to each event.
- Add Official FIFA source beside freshness and place Before you leave FIFA.com next to each outgoing action.
- Explain View Order versus View Tickets and expose the result of What does this mean?.

**Simplify**

- Use one pending vocabulary instead of three near-synonyms.
- Reduce duplicate support/resale paths and keep optional partner services visually secondary.
- Keep status meaning in text, not color alone.

**Validate again in PA4**

- Repeat F1-F10 on the revised dashboard.
- Add a specific check that the reviewer can state who owns the next step, how current the information is, and what destination opens after an external action.
- Recheck whether the timeline and handoff cues can be added without recreating the choice load seen in Alt 2 or Alt 3.

### Selected Chess direction: Alt 1 - Beginner Review Flow

**Keep**

- Beginner Review mode and guided step sequence.
- Plain-language mistake explanation, Better move, Try this move, Practice this idea, and Next mistake.
- The direct mistake-to-practice relationship.

**Improve**

- Add Start Beginner Review/Start with the most important mistake.
- Pair Qd3, Qe2, and ...Nxd4 with plain-language move descriptions and explain develops safely/hanging pieces.
- Add a visible board/result state after Try this move.
- Add Need more help? or Explain another way beside the current explanation.
- Preserve a visible Review another moment route.

**Simplify**

- Separate Review step, Mistake, and Game move counters.
- Rename or explain Full Analysis so a novice knows whether it provides beginner help or advanced detail.
- Keep the main path visually dominant and offer optional depth after the simple explanation.

**Validate again in PA4**

- Repeat C1-C9 on the revised flow.
- Require the reviewer to explain the mistake in their own words, try the better move, identify why it is better, select the practice activity, and request help if needed.
- Check that the improved flow remains recoverable when a reviewer wants to skip or review another moment.

## Alternative Selection for PA4

### Editable decision matrix

Scores are lead synthesis scores from the documented task outcomes, repeated issue patterns, reviewer preferences, scenario fit, and estimated revision effort. Scores are on a 1-5 scale; they are not direct reviewer ratings. The raw outcome counts remain the primary evidence.

| Criterion (higher is better) | FIFA Alt 1 | FIFA Alt 2 | FIFA Alt 3 | Decision reading |
|---|---:|---:|---:|---|
| Independent task coverage | 4 | 3 | 4 | Alt 1 has 31/50 independent outcomes; Alt 2 has 26/50; Alt 3 has 37/50 but its failures cluster on the core pending/next-step tasks. |
| Status comprehension | 5 | 5 | 3 | Alt 1 and Alt 2 expose state; Alt 3 shows only a confirmed event. |
| Next-step clarity | 2 | 5 | 2 | Alt 2 is strongest; Alt 1 and Alt 3 need explicit lifecycle copy. |
| Trust and handoff | 2 | 4 | 5 | Alt 3 is strongest; Alt 1 lacks source/handoff cues; Alt 2 lacks handoff behavior. |
| Low high-severity burden | 3 | 2 | 2 | Alt 1 has two recurring themes; Alt 2 and Alt 3 have action/state gaps that block required tasks. |
| Scenario fit | 5 | 4 | 3 | Alt 1 balances status understanding and common ticket actions. |
| Reviewer preference | 4 | 3 | 1 | Alt 1 3/5; Alt 2 2/5; Alt 3 0/5. |
| Revision cost | 4 | 2 | 2 | Alt 1 can add timeline and handoff cues inside the existing model; Alt 2 needs a new action layer; Alt 3 needs a status/progress layer. |
| **Recommendation** | **Select** | Close second | Do not select | Alt 1 is the strongest balanced base for PA4 after targeted revisions. |

**FIFA PA4 selection:** **Alt 1 - Status Dashboard.** It has the highest reviewer preference, the lowest failure burden among the status-and-action balance, and a smaller revision than rebuilding the timeline or adding full lifecycle status to the Action Hub. The selected direction carries forward Alt 2's freshness/ownership cues and Alt 3's adjacent handoff warning.

| Criterion (higher is better) | Chess Alt 1 | Chess Alt 2 | Chess Alt 3 | Decision reading |
|---|---:|---:|---:|---|
| Independent task coverage | 5 | 5 | 3 | Alt 1 has 36/45 independent outcomes; Alt 2 has 34/45; Alt 3 has 26/45 and five failures. |
| Where-to-start clarity | 4 | 2 | 2 | Alt 1 names Beginner Review; Alt 2 and Alt 3 lack a recommended first step. |
| Mistake/better-move comprehension | 5 | 4 | 4 | All three expose a mistake; Alt 1 best supports the novice explanation chain. |
| Practice connection | 5 | 5 | 1 | Alt 1 and Alt 2 provide direct practice; Alt 3 provides none in the visible state. |
| Low decision load | 5 | 2 | 3 | Alt 1 is guided; Alt 2 has six cards; Alt 3 has tabs, board, assistant, and key moments. |
| Learning support | 4 | 3 | 4 | Alt 3 is strongest for follow-up explanation, but not for acting or practicing. |
| Reviewer preference | 5 | 1 | 1 | Alt 1 5/5; Alt 2 0/5; Alt 3 0/5. |
| Revision cost | 4 | 3 | 2 | Alt 1 needs start/help/terminology refinements; Alt 3 needs a practice and action workflow. |
| **Recommendation** | **Select** | Close second | Do not select | Alt 1 is the clearest beginner base for PA4. |

**Chess PA4 selection:** **Alt 1 - Beginner Review Flow.** All five reviewers preferred it, it delivered the strongest mistake-to-practice chain, and its issues are targeted copy and entry refinements rather than a missing core workflow.

## What We Improve Before PA4

| Selected prototype | Keep | Improve | Simplify | Validate again |
|---|---|---|---|---|
| FIFA Alt 1 - Status Dashboard | Status summary, event cards, direct ticket actions, freshness cue. | Pending next step, owner, timing, official source, per-action handoff, action result. | Status vocabulary, duplicate labels, optional-service density. | Re-run F1-F10 with explicit ownership, source, and handoff checks. |
| Chess Alt 1 - Beginner Review Flow | Guided sequence, plain-language cause, Better move, Try, Practice, Next mistake. | Start cue, notation translation, Try result, beginner help, alternate review. | Progress counters and Full Analysis framing. | Re-run C1-C9 and require own-words explanation, move trial, practice, and help recovery. |

## Testing Limitations

AI reviewers model novice interaction and provide structured formative critique. They do not reproduce every aspect of physical user interaction, motor behavior, accessibility needs, emotional response, or the variability of a live moderated session. Paper-prototype testing remains useful for identifying likely hierarchy, terminology, workflow, and comprehension issues. These results guide revisions and PA4 validation targets; they do not establish population-level usability claims.

## Reviewer Records

The complete task-level evidence is preserved in the five independent records below. The records retain reviewer-specific observations, feedback, problem classifications, improvement suggestions, and preferences without collapsing disagreements.

- [AI Reviewer R1 record](ai-testing/R1.md)
- [AI Reviewer R2 record](ai-testing/R2.md)
- [AI Reviewer R3 record](ai-testing/R3.md)
- [AI Reviewer R4 record](ai-testing/R4.md)
- [AI Reviewer R5 record](ai-testing/R5.md)

## Full Reviewer Evidence

### AI Reviewer R1 - Full Record

# AI Reviewer R1

## Reviewer Profile

- Digital literacy: high
- Domain familiarity: FIFA ticket familiarity low; Chess.com analysis familiarity none
- Behavior model: explores quickly and expects obvious actions
- Assigned prototype order: FIFA Alt 1 -> Alt 2 -> Alt 3; Chess Alt 1 -> Alt 2 -> Alt 3

## Scenario 1 - FIFA

### Alt 1 - Status Dashboard

#### Task Outcomes

F1: **Independent Success** - I would first scan the four status cards, then the event cards. “2 Confirmed,” “1 Pending,” and the event-level labels clearly show the current ticket situation.

F2: **Independent Success** - I would look at the orange Pending card and the second event. “Awaiting FIFA confirmation” and “What does this mean?” identify the progressing information; “0 Action needed” indicates that no user action is currently requested.

F3: **Independent Success** - I would read “Confirmed / Ready to go” and “Pending / Awaiting FIFA confirmation.” The plain-language descriptions explain the displayed status, with the information icon offering a possible next explanation.

F4: **Success With Hesitation** - I would start with the pending event and inspect “What does this mean?” or “See details.” I can infer that I should wait for FIFA confirmation, but there is no clear next stage, expected date, or explicit sequence.

F5: **Independent Success** - I would look at “Last updated: 2 mins ago” and the refresh icon near the top of the dashboard. The freshness signal is immediately visible.

F6: **Success With Hesitation** - The FIFA branding and `fifa.com/tickets` address make the page appear official. I would still look for an explicit official-source label, which is absent.

F7: **Independent Success** - I would look inside the confirmed Argentina vs Brazil event card and select “View Tickets.” The control is clearly connected to the ticket details.

F8: **Independent Success** - I would scan Quick Actions and select “Transfer Tickets.” Its description, “Send to friends or family,” confirms the meaning.

F9: **Independent Success** - I would use the visible “Add to Calendar” Quick Action. The label directly matches the task.

F10: **Failure** - I would look around Quick Actions and the event cards for an external-link warning or security message. Nothing visibly explains whether an action leaves FIFA.com or what service receives me.

#### Observations

- The first visual scan provides counts for confirmed, pending, action-needed, and cancelled information.
- Event cards provide different actions: “View Tickets” for the confirmed event and “View Order” for the pending event.
- “Last updated: 2 mins ago” is visible but is not paired with an official-source indicator.
- The dashboard explains the current state better than it explains the next state.

#### Feedback

- The status summary would let me orient myself quickly, but the pending state stops at “Awaiting FIFA confirmation.”
- “View Tickets” and “View Order” make the relationship between an order and the actual tickets uncertain.
- The page needs a visible next-step statement and a clear explanation of any external handoff.

#### Problems Encountered

- [Workflow; High] F4: The pending event has no explicit next expected step, timing, or progression beyond waiting for confirmation.
- [Consistency; Medium] F7: “View Tickets” and “View Order” use different labels for similar event cards without explaining the distinction.
- [Trust; Medium] F6 and F10: FIFA branding suggests official status, but there is no explicit source badge or external-service warning.
- [Feedback; Medium] F3 and F4: “What does this mean?” is visible, but the explanation is not shown in the prototype state.

#### Points of Improvement

- Add a per-event “Next step” line such as “Await FIFA confirmation” with an expected update or delivery point.
- Add an “Official FIFA source” label next to the freshness indicator.
- Explain whether “View Order” contains tickets, pending information, or both.
- Add an external-handoff warning to any action that opens an official partner service.

#### Main Strength

The status cards and event-level labels make confirmed and pending information immediately scannable.

#### Main Weakness

The dashboard shows the current state without giving a dependable next-step path or external-service explanation.

### Alt 2 - Timeline Tracker

#### Task Outcomes

F1: **Independent Success** - I would first inspect the event cards and their timelines. “ON TRACK,” the blue current step “Verification,” and the orange “PENDING” state clearly show where each order stands.

F2: **Independent Success** - I would look at the second event’s timeline and find “Payment received — Pending” in orange. The later stages marked with dashes also show that information is not yet available.

F3: **Independent Success** - I would read the completed check marks, the blue current step, and the message “Your order is progressing normally.” The stage names explain what each status means.

F4: **Success With Hesitation** - For Argentina vs Brazil, I would look at “Ticket ready — 72h before match” and the message “Mobile ticket expected 72h before match.” For the pending event, the later stages show dashes, so I cannot find a concrete next step for that order.

F5: **Independent Success** - I would look at “Last updated: 2 mins ago,” “Freshness & Updates,” and “View update history.” Several visible controls support checking whether information is current.

F6: **Independent Success** - The “Official FIFA source” badge is visible beside the update time. I would treat that as a direct official-source signal.

F7: **Failure** - I would first look for a “View Tickets” button on the event card. It is not present; “My Tickets” in the left navigation is only an inferred route and does not show the requested control.

F8: **Failure** - I would scan the timeline and right-side panels for “Transfer Tickets,” but no transfer action is visible.

F9: **Success With Hesitation** - I would select “Sync to calendar” in Freshness & Updates. I would hesitate because “Sync” does not clearly mean adding the selected event to my calendar.

F10: **Failure** - I would look for a warning before selecting an official next-step link. The screen shows an official source and official guides, but no message explains what happens when leaving FIFA.com.

#### Observations

- The timeline makes completed, current, and upcoming stages visually distinct.
- The first event includes both an expected delivery point and a progress message.
- The pending event uses orange for the current pending stage but leaves later stages as unexplained dashes.
- The right rail emphasizes freshness and official guidance, while ticket-management actions are absent.

#### Feedback

- The timeline gives me a stronger understanding of order progress than a single status label.
- The pending event needs an explanation of whether the user should wait, provide information, or contact support.
- The page feels like a tracking view, so I would not know where to transfer or open tickets without leaving this screen.

#### Problems Encountered

- [Visibility; High] F7 and F8: “View Tickets” and “Transfer Tickets” are not visible actions on the tracker.
- [Terminology; Medium] F9: “Sync to calendar” does not clearly communicate whether it adds one event or synchronizes all events.
- [Workflow; Medium] F4: The pending timeline has no visible next milestone or expected timing.
- [Trust; High] F10: No external-service handoff or security explanation appears before official next-step links.

#### Points of Improvement

- Add “View Tickets” and “Transfer Tickets” to each relevant event card.
- Rename “Sync to calendar” to “Add to Calendar” or explain the difference.
- Replace unexplained dashes with language such as “Waiting for verification” and identify the next expected update.
- Add an external-link icon and a before-leaving notice to links that open partner services.

#### Main Strength

The timeline and freshness controls make the order’s progress and update status concrete.

#### Main Weakness

The tracker does not support the common ticket actions required after understanding the status.

### Alt 3 - Action Hub

#### Task Outcomes

F1: **Independent Success** - I would first look at the main event card and read “CONFIRMED” and “Tickets are valid.” The current displayed status is clear, although only one event is shown.

F2: **Failure** - I would scan the event card, Quick Actions, and official options for pending or attention-needed information. No pending or action-needed state is visible, so I cannot determine whether all information is complete or whether progressing information is omitted.

F3: **Independent Success** - “CONFIRMED” and “Tickets are valid” provide a direct explanation of the displayed status.

F4: **Failure** - I would first look at the event status and then at the action cards. The page offers user-selected actions such as transfer or resale, but no ticket lifecycle, delivery stage, or next expected system step.

F5: **Independent Success** - “Last updated: 2 mins ago” is visible near the top of the page.

F6: **Independent Success** - The “Official FIFA source” badge and “Official” labels on the options provide direct official-status signals.

F7: **Independent Success** - “View Tickets” appears both on the event card and as a large Quick Action. I would use either visible control.

F8: **Independent Success** - “Transfer Tickets” is a prominent Quick Action with the explanation “Send tickets securely to friends or family.”

F9: **Independent Success** - “Add to Calendar” is a prominent Quick Action with a matching calendar icon and label.

F10: **Independent Success** - The bottom notice says “Before you leave FIFA.com” and explains that some options open on official partner sites, with security and data protection information. I would know that a handoff may occur.

#### Observations

- The page makes common ticket actions the dominant visual content.
- The event status is clear but occupies much less space than the action grid.
- “Official FIFA source,” “Official,” and “Before you leave FIFA.com” provide visible trust cues.
- The screen presents only a confirmed event, so it does not show how progressing information would appear.

#### Feedback

- I can locate ticket actions without searching through navigation.
- The action cards do not help me understand what happens next to a pending or incomplete ticket.
- “Some options” in the handoff notice is broad; it does not identify which individual cards leave FIFA.com.

#### Problems Encountered

- [Visibility; High] F2: No pending or attention-needed information is visible, so the status of progressing tickets cannot be determined.
- [Workflow; High] F4: The action hub has shortcuts but no lifecycle or next-step sequence.
- [Information hierarchy; Medium] F1 and F4: The large action grid competes with the small event-status area.
- [Feedback; Medium] F10: The handoff warning does not identify the external destination for each option.
- [Cognitive load; Medium] F7-F10: Numerous action cards, official options, help panels, and security content require several scans.

#### Points of Improvement

- Show all relevant events with confirmed, pending, and attention-needed states.
- Add a per-event next-step and expected-timing line above the action shortcuts.
- Mark each external action with an external-link indicator and a specific destination or partner description.
- Separate “Manage my tickets” actions from optional marketplace, hospitality, and travel options.

#### Main Strength

The core ticket actions are highly visible, labeled plainly, and supported by an explicit handoff warning.

#### Main Weakness

The page is action-complete for the displayed confirmed event but does not reveal pending information or the next ticket-processing step.

### FIFA Preference

- Preferred alternative: Alt 1 - Status Dashboard
- Reason: It gives me a single first scan for confirmed and pending counts, explains the event-level status, and still exposes View Tickets, Transfer Tickets, and Add to Calendar.
- Trade-off: It is less precise than Alt 2 about timeline progression and less explicit than Alt 3 about official external handoffs.

## Scenario 2 - Chess

### Alt 1 - Beginner Review Flow

#### Task Outcomes

C1: **Independent Success** - I would first look at the Game Review header and the Beginner Review / Full Analysis toggle. “Beginner Review” is selected, so I would use that as the starting mode; I would briefly notice that the screen is already at “Step 2 of 3” and has no explicit Start or Restart control.

C2: **Independent Success** - I would read the red “Mistake 2 of 3” panel and the move “Qd3.” The mistake is clearly identified without needing chess analysis knowledge.

C3: **Independent Success** - The text says the queen stopped protecting the pawn on d4 and that Black wins the pawn after `...Nxd4`. That directly explains the mistake.

C4: **Independent Success** - I would look at the blue Better move panel and find “Qe2.”

C5: **Independent Success** - “Keeps the pawn protected and develops safely” explains why Qe2 is better.

C6: **Independent Success** - “Try this move” is a direct action, and “Show me on the board” offers a separate inspection action. I would select Try this move first.

C7: **Independent Success** - I would look at “Practice this idea,” read “Puzzle: protect hanging pieces,” and select “Start practice.”

C8: **Independent Success** - “Next mistake” is visible at the bottom of the review panel, and the bottom navigation also shows Next. I would use the panel control to continue.

C9: **Success With Hesitation** - If the explanation were insufficient, I would first use “Show me on the board,” then consider “Full Analysis.” Both are visible, but neither is labeled as additional help, and “Full Analysis” sounds more advanced.

#### Observations

- The review uses a visible sequence from mistake, to explanation, to better move, to practice, and then to the next mistake.
- The plain-language explanation reduces dependence on chess notation.
- The screen includes both “Move 23 of 41” and “Step 2 of 3,” which represent different kinds of progress.
- The beginner mode is visible, but the current screen does not show how to restart at the first mistake.

#### Feedback

- The relationship between the red mistake panel and the blue better-move panel is clear.
- “Show me on the board” and “Try this move” are understandable labels, but their different outcomes are not demonstrated in the static screen.
- The flow needs a more visible fallback for users who still do not understand the explanation.

#### Problems Encountered

- [Learning support; Medium] C9: No explicit help, glossary, or alternate explanation path is labeled for a confused beginner.
- [Terminology; Medium] C2-C5: `Qd3`, `Qe2`, and `...Nxd4` remain unfamiliar even though surrounding prose explains them.
- [Information hierarchy; Low] C1 and C8: “Step 2 of 3” and “Move 23 of 41” could be mistaken for the same progress measure.
- [Feedback; Medium] C6: The prototype does not show what changes after selecting “Try this move.”

#### Points of Improvement

- Add “Start review” or “Restart from first mistake” and clarify why the current screen opens at Step 2.
- Add a short notation explanation or describe the moves in plain language beside the algebraic notation.
- Explain that “Show me on the board” highlights the idea while “Try this move” lets the user attempt it.
- Add a clearly labeled “Need more help?” route connected to the current mistake.

#### Main Strength

The sequence connects a specific mistake to a reason, a better move, practice, and the next review item.

#### Main Weakness

The flow offers limited support when the first plain-language explanation is still not enough.

### Alt 2 - Card Review Mode

#### Task Outcomes

C1: **Success With Hesitation** - I would first look at “Review your key moments” and the grid of cards. I could select the already highlighted “Missed Tactic” card, but the summary metrics, filter, and six cards make it unclear whether there is a recommended starting card.

C2: **Independent Success** - I would use the red “Mistakes 3” and “Blunders 1” summary chips, then choose a red card such as “Missed Tactic — Move 23” or “Queen Safety.” One important mistake is easy to identify.

C3: **Independent Success** - The expanded card states that the queen on c3 was attacked and that capturing the pawn would have gained material. This explains the mistake in plain language.

C4: **Independent Success** - The expanded card visibly says “Better move: Qxc3.”

C5: **Independent Success** - “Captures the pawn on c3 and wins material” explains why the suggested move is better.

C6: **Independent Success** - I would select “Try this move,” with the mini-board preview providing additional inspection.

C7: **Independent Success** - I would select “Go to puzzle,” which is a direct practice route connected to the reviewed card.

C8: **Independent Success** - I would use “Choose another card” or select another key-moment card such as Queen Safety or Hanging Pawn.

C9: **Success With Hesitation** - I would look at “Open in Analysis Board” for deeper help. The action is visible, but “Analysis Board” is unfamiliar to someone with no Chess.com analysis experience, and its benefit is not explained.

#### Observations

- The card grid supports non-linear review and exposes several possible mistakes or concepts.
- The selected card expands into a clear explanation, better move, trial action, and puzzle action.
- The checkmark, blue border, and checkbox-like control may not immediately communicate whether a card is selected or completed.
- Several chess terms appear before the user has received any explanation of them.

#### Feedback

- I can find a mistake by scanning red cards, but I would hesitate over which one is most important.
- The selected card gives a strong concrete explanation and clear actions.
- The screen provides flexibility at the cost of a more demanding first decision.

#### Problems Encountered

- [Cognitive load; Medium] C1: Summary chips, filters, board controls, and six cards compete for attention at the review entry point.
- [Terminology; Medium] C1-C5 and C9: “Missed Tactic,” “Blunder,” “Opening,” “Endgame,” and “Analysis Board” are not explained for a domain novice.
- [Feedback; Medium] C1 and C8: The checkmark and blue border do not clearly distinguish selected, reviewed, and completed states.
- [Workflow; Medium] C1: There is no visible recommended first card or guided review order.

#### Points of Improvement

- Add a “Start with the most important mistake” recommendation or rank cards by learning priority.
- Define chess terms with short plain-language descriptions on the cards.
- Use a stronger selected-state treatment and separate it from completion indicators.
- Explain what opens in the Analysis Board and how it provides additional help.

#### Main Strength

Each selected card connects an identifiable moment to an explanation, better move, trial action, and practice puzzle.

#### Main Weakness

The dashboard asks a chess-inexperienced user to choose among many cards and unfamiliar categories before providing guidance.

### Alt 3 - Side-by-Side AI Assistant

#### Task Outcomes

C1: **Success With Hesitation** - I would first look at the Assistant greeting and the red Qd3 entry in Key Moments. I could click the red key moment or type a question, but there is no explicit “Start review” action and several tabs compete with those two entry points.

C2: **Independent Success** - The Key Moments list marks “23. Qd3” in red with a question symbol, while the summary shows three mistakes and one blunder. I would select Qd3 as an important mistake.

C3: **Independent Success** - I would use the visible question field to ask “Why is Qd3 a mistake?” or select the red key moment. The assistant response explains that Qd3 loses the pawn on c3 and that Black improves its position after `...Bxc3`.

C4: **Independent Success** - I would ask “What’s the better move here?” using the visible input or follow the displayed conversation. The response identifies Qe2.

C5: **Independent Success** - The assistant says “Qe2 is safer,” protects the pawn on e2, and keeps the queen safe. The reason is visible in plain language.

C6: **Success With Hesitation** - I would inspect the green-highlighted Qe2 square or select “Show variations.” There is no explicit “Try this move” control, so I would not know whether I could play the move or only view it.

C7: **Failure** - I would look for “Practice,” “Puzzle,” or a learning link after the explanation. “Any similar ideas?” may produce more discussion, but no related practice activity is visibly available.

C8: **Independent Success** - I would select another move from the Key Moments list, such as `...Bxc3` or another colored move. The list provides a visible route to another review point even without a Next button.

C9: **Independent Success** - The Assistant greeting, free-form question field, and follow-up prompts provide an obvious way to ask for more help when the explanation is insufficient.

#### Observations

- The interface combines the board, highlighted squares, conversation, and Key Moments list in one view.
- The displayed questions demonstrate how a novice might ask about a mistake and a better move.
- The assistant gives explanations, but the screen does not show a direct trial or practice action.
- Multiple tabs and panels create several possible starting points.

#### Feedback

- The conversation and board highlights make the explanation feel connected to the selected position.
- The free-form question field is useful for follow-up help, but it requires the user to formulate a question before the first response.
- The review can continue through Key Moments, but the path from explanation to practice is missing.

#### Problems Encountered

- [Workflow; Medium] C1, C3, and C4: The user must choose between selecting a key moment, opening a tab, and composing a question without a clearly recommended first action.
- [Visibility; High] C6 and C7: No direct “Try this move” or practice/puzzle control is visible.
- [Terminology; Medium] C1 and C9: “Assistant,” “Analysis,” “Review,” “Details,” and “Openings” are not differentiated for a first-time chess-analysis user.
- [Cognitive load; Medium] C1 and C8: Board, chat, tabs, key moments, and game summary require coordination across several areas.
- [Feedback; Medium] C6: Board highlights show a suggested move but do not show what happens after attempting it.

#### Points of Improvement

- Add a prominent “Start with your biggest mistake” action that selects the first key moment and opens the relevant explanation.
- Provide initial question prompts such as “Why is this a mistake?” and “What should I play instead?” before the user types.
- Add “Try this move” and “Go to puzzle” actions beside the assistant’s suggested move.
- Label the tabs in beginner language or reduce the number of competing destinations.
- Show whether board highlights are an explanation, a variation, or an interactive move attempt.

#### Main Strength

The assistant combines plain-language explanations with board and mini-board highlights and supports follow-up questions.

#### Main Weakness

It explains mistakes well but does not provide a visible route from the explanation to trying or practicing the better move.

### Chess Preference

- Preferred alternative: Alt 1 - Beginner Review Flow
- Reason: It gives the clearest novice path from identifying a mistake to understanding it, trying a better move, practicing the idea, and continuing to the next mistake.
- Trade-off: It is less flexible than the card dashboard and less open-ended than the assistant, with weaker support when the guided explanation is insufficient.

## Overall Review

- Most confusing element: FIFA Alt 2’s pending timeline, especially “Payment received — Pending” followed by later stages marked only with dashes.
- Clearest element: Chess Alt 1’s visible sequence from “Mistake” to “Better move,” “Try this move,” “Practice this idea,” and “Next mistake.”
- Most useful concept: Connecting an explanation directly to an action, especially the better-move, trial, and practice bridge in Chess Alt 1.
- Highest-priority improvement: For every FIFA event, show the current state, pending reason, next expected step and timing, freshness, and any relevant external-service warning together.

### AI Reviewer R2 - Full Record

# AI Reviewer R2

## Reviewer Profile

- Digital literacy: Medium
- Domain familiarity: FIFA ticket familiarity none; Chess analysis familiarity none
- Behavior model: Careful reader; reads labels before acting and notices terminology problems
- Assigned prototype order: FIFA Alt 2 → Alt 3 → Alt 1; Chess Alt 2 → Alt 3 → Alt 1
- Methodology: AI-Agent Formative Testing

## Scenario 1 - FIFA

### Alt 2 - Timeline Tracker

#### Task Outcomes

F1: **Independent Success** - I would first look at the large ticket cards and their status labels. “ON TRACK,” the green progress line, and the blue current step indicate that Argentina vs Brazil is progressing through verification. The second card is marked “PENDING.” I would consider the current statuses identified.

F2: **Independent Success** - I would look at the second ticket card, where “PENDING” and “Payment received — Pending” are both visible. I would interpret payment as the information still progressing. I would not assume that I personally need to take action because no user-action warning is shown.

F3: **Success With Hesitation** - I would read the message “Your order is progressing normally” and the numbered stages to explain “ON TRACK.” For the second card, I would infer that payment is still being processed, but I would hesitate because “PENDING” is not separately explained as an order status or a payment status. I would count the task as eventually complete for the first ticket, but only partly clear for the second.

F4: **Independent Success** - I would look at the highlighted current stage, “Verification,” then read the next stage, “Ticket ready — 72h before match.” I would use “See full timeline” if I wanted more detail. The next expected step and approximate timing are visible, so I would consider this complete.

F5: **Independent Success** - I would first look beside the page heading for “Last updated: 2 mins ago,” then notice “View update history.” I would interpret the timestamp as evidence that the information appears current. I would consider the task complete, while recognizing that the timestamp is page-level rather than clearly attached to each ticket.

F6: **Independent Success** - I would look near the timestamp and find the explicit “Official FIFA source” label. This directly answers whether the displayed information appears official.

F7: **Failure** - I would scan the ticket cards and right-side panels for “View Tickets.” I would then notice “My Tickets” in the left navigation, but I would not assume that it is the same as a direct View Tickets action. No visible control opens the tickets from this screen, so I would not consider the task complete.

F8: **Failure** - I would scan the right-side panels and ticket cards for “Transfer Tickets.” Only freshness, update-history, calendar, next-step, and support options are visible. There is no workable transfer control shown.

F9: **Success With Hesitation** - I would look in “Freshness & Updates” and choose “Sync to calendar.” I would interpret the calendar icon and wording as related to adding the event, but “Sync” could mean maintaining an existing calendar connection rather than adding one event. I would count this as eventual success with uncertainty, not independent success.

F10: **Failure** - I would look for a warning or explanation near any external link or official option. There is an “Official FIFA source” label, but there is no visible statement about leaving FIFA.com, the destination service, or what happens to my data. I would not consider this task complete.

#### Observations

The timeline and numbered stages are the first elements I would use to understand the ticket state. The current step, future “Ticket ready” step, last-updated time, update history, and official-source label are all visible. The second ticket’s pending state is visible, but the interface does not explain what caused the pending state or what the user should do while waiting.

The screen is organized around progress rather than ticket actions. “My Tickets” is present in navigation, but direct ticket access, transfer, and other common actions are not visible. “Sync to calendar” is the nearest calendar control, but it does not use the task’s expected “Add to Calendar” wording. No post-action result or confirmation is visible in the paper prototype.

#### Feedback

The screen answers status, freshness, officiality, and the next expected delivery stage with relatively little interpretation. After attempting the tasks, I would want the pending card to state the exact next event, who is responsible for it, and whether I need to wait or act. I would also want common ticket actions placed on each ticket card rather than requiring a separate route.

#### Problems Encountered

- [Visibility; High] F7 and F8 fail because no visible “View Tickets” or “Transfer Tickets” control is present.
- [Workflow; High] The timeline explains progress but does not provide a complete path to common ticket actions or external-service handoff.
- [Terminology; Medium] F3 and F9 are weakened by “ON TRACK” and “Sync to calendar,” which are not as specific as the task language.
- [Feedback; Medium] F2 shows a pending payment stage but gives no visible reason, expected resolution, or user action.
- [Information hierarchy; Medium] “Official Next Steps” contains general guides, but it is not clear which next step applies to which ticket or current stage.

#### Points of Improvement

- Add a ticket-level action row containing “View Tickets,” “Transfer Tickets,” and “Add to Calendar.”
- Replace or supplement “Sync to calendar” with “Add event to calendar,” and state what will happen after selecting it.
- Add pending-state copy such as the next expected update, responsible party, and whether the user needs to act.
- Associate “Official Next Steps” with the selected ticket and current timeline stage.
- Add an explicit external-handoff message before any official partner link opens.

#### Main Strength

The visible timeline connects the current state to a concrete future stage: verification is current, ticket readiness is expected 72 hours before the match, and update freshness is shown.

#### Main Weakness

The screen makes progress understandable but leaves common ticket actions and external handoff behavior outside the visible workflow.

### Alt 3 - Action Hub

#### Task Outcomes

F1: **Independent Success** - I would first look at the event card at the top, where “CONFIRMED” and “Tickets are valid” are shown for Argentina vs Brazil. I would interpret this as the current ticket status and consider the task complete.

F2: **Failure** - I would scan the event card, Quick Actions, Ticketing Updates, and help panels for a pending or attention-needed item. The visible event is confirmed, and “Enable Notifications” is an optional update feature rather than a pending ticket state. I would not infer that no pending information exists; I would report that none is displayed.

F3: **Independent Success** - I would use the visible “CONFIRMED” and “Tickets are valid” text to explain the status. The explanation is short but directly connected to the event card, so I would consider this complete.

F4: **Failure** - I would look below the status for a timeline or “next step.” “See details,” “Ticketing Updates,” and the action cards are visible, but none states what happens next to the ticket or when. I could guess that enabling notifications is useful, but I would not count that as identifying the expected next step.

F5: **Independent Success** - I would look beside the heading and find “Last updated: 2 mins ago.” I would interpret this as evidence that the page information appears current.

F6: **Independent Success** - I would look at the green “Official FIFA source” label and the “Official” labels on the marketplace, hospitality, and travel cards. These provide direct visible evidence of official status.

F7: **Independent Success** - I would first notice the “View Tickets” button on the confirmed event card, then the larger “View Tickets” Quick Action. Either control is clearly labeled and describes ticket details.

F8: **Independent Success** - I would scan the Quick Actions and find “Transfer Tickets,” with the supporting text “Send tickets securely to friends or family.” I would choose that card.

F9: **Independent Success** - I would scan the Quick Actions and find “Add to Calendar,” with the supporting text “Save match details to your calendar.” The wording and calendar icon are direct.

F10: **Independent Success** - I would look at the bottom banner beginning “Before you leave FIFA.com.” It explains that some options open on official partner sites and states that the destination is an official partner service. I would use “Learn more” if I needed additional detail and consider the task complete.

#### Observations

The Quick Actions section makes the common ticket actions visually prominent and gives each action a short description. The external handoff banner is also explicit. However, the page shows only a confirmed event and does not expose a pending state, timeline, or ticket-specific next step. “Official Options” contains multiple commercial or partner choices, but the relationship between those options and the current ticket status is not explained.

“Resell Official” and “Official Resale Marketplace” use similar but different wording for resale. “Contact Support” appears both as a Quick Action and in the help panel. The static image provides no visible result after selecting an action.

#### Feedback

After attempting the tasks, I would want the Action Hub to retain its direct action cards but add the status information needed to understand tickets before acting. The handoff message is useful, but it should appear directly beside each action that can leave FIFA.com so that the warning is not separated from the decision.

#### Problems Encountered

- [Workflow; High] F2 and F4 fail because the screen does not show pending information or a ticket-specific next expected step.
- [Information hierarchy; Medium] The large action grid dominates the screen while status progression is limited to one confirmed event.
- [Consistency; Medium] “Resell Official” and “Official Resale Marketplace” may describe related destinations but use different terms.
- [Visibility; Medium] F10 is supported by a bottom banner, but the warning is visually distant from the individual external options.
- [Feedback; Low] The prototype shows action labels but no visible confirmation, destination, or completed state after an action.

#### Points of Improvement

- Add a pending/attention section or timeline for every ticket, including the next expected update.
- Place the external-service warning directly on or beside each action that leaves FIFA.com.
- Use one consistent resale label across Quick Actions and Official Options.
- Keep the direct action cards but add state-specific actions, such as what to do while a ticket is pending.
- Show the expected result after each action, such as tickets opened, transfer started, or calendar event prepared.

#### Main Strength

“View Tickets,” “Transfer Tickets,” and “Add to Calendar” are clearly labeled, described, and located together, while the official-source and partner-handoff information is visible.

#### Main Weakness

The action-first layout does not show the pending information or expected status progression needed before deciding what to do.

### Alt 1 - Status Dashboard

#### Task Outcomes

F1: **Independent Success** - I would first look at the four status tiles, then confirm them against the event cards. “Confirmed” and “Pending” are recognizable labels, and the event cards repeat those states for Argentina vs Brazil and Al Hilal vs Real Madrid. I would consider the current statuses identified.

F2: **Independent Success** - I would look at the “Pending 1” tile and the second event card, which says “PENDING” and “Awaiting FIFA confirmation.” The “Action needed 0” tile also tells me that no visible user action is currently required. I would consider the pending information found.

F3: **Independent Success** - I would read “Ready to go” and “Tickets are valid” under the confirmed state, and “Awaiting FIFA confirmation” under the pending state. The “What does this mean?” link is an additional visible explanation route, but the status text itself is sufficient to explain the display.

F4: **Success With Hesitation** - I would look at the pending event and read “Awaiting FIFA confirmation.” I would interpret FIFA confirmation as the next expected event, but I would hesitate because there is no date, progress stage, responsible party, or statement about what happens after confirmation. I would count the immediate next step as inferred but not fully explained.

F5: **Independent Success** - I would look near the page heading and find “Last updated: 2 mins ago” beside a refresh icon. I would interpret the timestamp as evidence that the dashboard appears current, although it does not identify which event fields were refreshed.

F6: **Success With Hesitation** - I would look at the browser address and FIFA branding, including “fifa.com/tickets.” This makes the page appear official, but there is no explicit “Official FIFA source” label or source explanation. I would treat the task as eventually complete with some uncertainty.

F7: **Independent Success** - I would look at the confirmed event card and find “View Tickets.” The left navigation also includes “My Tickets.” The card button is the clearest direct control, so I would choose it.

F8: **Independent Success** - I would scan the “Quick Actions” panel and find “Transfer Tickets,” with the explanation “Send to friends or family.” I would choose that item.

F9: **Independent Success** - I would scan the same Quick Actions panel and find “Add to Calendar,” with “Never miss your event.” The label is direct enough to complete the task.

F10: **Failure** - I would look for a message explaining what happens before using an external service. The screen contains FIFA ticket actions and support links but no visible external-service destination, official-partner notice, security statement, or leaving-page warning. I would not consider this complete.

#### Observations

The dashboard gives status information priority through summary tiles and event cards. The confirmed and pending states are easy to locate, and the pending card includes a short explanation. The quick-action panel makes transfer and calendar actions visible. However, the pending state stops at “Awaiting FIFA confirmation,” and “What does this mean?” does not show its answer in the paper prototype.

The confirmed card uses “View Tickets,” while the pending card uses “View Order.” I would notice the difference but would not know whether it reflects a meaningful workflow distinction or simply different wording. The dashboard has a timestamp but no official-source label or external handoff explanation.

#### Feedback

After attempting the tasks, I would want the pending card to show the next expected step in the same way a timeline does. I would also want a visible official-source and external-partner explanation, especially for actions involving resale, transfer, or ticket delivery.

#### Problems Encountered

- [Workflow; High] F4 and F10 are incomplete because the pending workflow and external handoff are not visibly defined.
- [Trust; Medium] F6 is based on branding and the URL rather than an explicit source indicator.
- [Consistency; Medium] F7 is affected by the difference between “View Tickets” for the confirmed event and “View Order” for the pending event.
- [Learning support; Medium] F3 and F4 rely on a “What does this mean?” link whose resulting explanation is not visible.
- [Information hierarchy; Medium] Summary counts identify states but do not connect each state to a detailed next action.

#### Points of Improvement

- Add an event-level next-step line with timing and responsibility for every pending state.
- Use consistent ticket-action wording across confirmed and pending cards, or explain why the actions differ.
- Add an explicit “Official FIFA source” indicator and a handoff warning for external services.
- Make the explanation behind “What does this mean?” visible or label the control with the information it opens.
- Connect each summary tile to the relevant event details and action.

#### Main Strength

The combination of status counts, event-level labels, explanations, and Quick Actions lets a novice locate the main ticket state and common actions from one screen.

#### Main Weakness

The dashboard identifies that something is pending but does not make the next step, officiality, or external-service behavior sufficiently explicit.

### FIFA Preference

- Preferred alternative: Alt 2 - Timeline Tracker
- Reason: It provides the clearest evidence for current status, pending progress, freshness, officiality, and the next expected ticket stage.
- Trade-off: It lacks direct “View Tickets” and “Transfer Tickets” controls. Alt 3 is better for immediate actions and external handoff, while Alt 2 is better for understanding what is happening before acting.

## Scenario 2 - Chess

### Alt 2 - Card Review Mode

#### Task Outcomes

C1: **Success With Hesitation** - I would first look at the “Game Review” heading, summary metrics, and “Review your key moments.” I would interpret the cards as possible review starting points and select the already-highlighted “Missed Tactic” card. There is no explicit “Start review” control, and the checkboxes make selection behavior uncertain, so I would count this as eventual success with hesitation.

C2: **Independent Success** - I would look at the red “Mistakes” and “Blunders” summary cards, then the key-moment cards. “Missed Tactic — Move 23” is visibly selected and expanded. I would identify it as one important mistake without needing to decide that it is the single most serious mistake.

C3: **Independent Success** - I would read the expanded explanation: the queen on c3 was attacked, and a capture of the pawn on c3 was available. This explains the mistake in ordinary language even though the move notation is unfamiliar.

C4: **Independent Success** - I would look in the expanded card and find “Better move: Qxc3.” The supporting mini-board also indicates the alternative. I would consider the better move found.

C5: **Independent Success** - I would read “Captures the pawn on c3 and wins material.” This gives a concrete reason the suggested move is better. The notation “Qxc3” is unfamiliar, but the sentence explains its effect.

C6: **Independent Success** - I would choose “Try this move.” I would also recognize “Review this card” and “Open in Analysis Board” as related controls. The task is complete at the level of finding a visible way to try or inspect the move, although the paper state does not show the resulting interaction.

C7: **Independent Success** - I would look for an action connected to practice and find the orange “Go to puzzle” button. I would interpret it as the related practice activity.

C8: **Independent Success** - I would use “Choose another card” or select another visible key-moment card such as “Queen Safety” or “Hanging Pawn.” The screen exposes a concrete route to another review item.

C9: **Success With Hesitation** - I would look at “Open in Analysis Board” as the route for more explanation. I would hesitate because “Analysis Board” sounds like an advanced tool rather than help for a beginner, but it is the only visible route to more detailed inspection.

#### Observations

The selected card creates a useful chain from mistake explanation to better move, trying the move, and puzzle practice. The cards also expose multiple review topics without forcing a fixed order. However, “Review your key moments” does not identify a recommended starting point, and the checkboxes do not clearly communicate whether multiple cards can be selected or whether they simply indicate the current card.

Terms such as “Missed Tactic,” “Hanging Pawn,” “King Safety,” “Blunders,” and “Qxc3” are unfamiliar to a non-chess user. The prose explanations reduce the problem, but the card titles and summary metrics still require interpretation. No post-action result is visible in the paper prototype.

#### Feedback

After attempting the tasks, I would want the selected card to be clearly marked as the current review item and the entry action to be explicit. I would also want the interface to explain the chess notation and provide a beginner-oriented help route separate from the advanced Analysis Board.

#### Problems Encountered

- [Workflow; Medium] C1 has no clear “Start review” action or recommended first card.
- [User control; Medium] The checkboxes and selected-card styling do not explain whether cards are single-select, multi-select, or simply clickable.
- [Terminology; Medium] C2–C5 contain domain terms and notation such as “Missed Tactic,” “Blunders,” and “Qxc3.”
- [Cognitive load; Medium] Summary metrics, six cards, a board, filters, and multiple navigation controls compete for attention.
- [Learning support; Medium] C9 offers “Open in Analysis Board” but does not explain whether it is suitable for a beginner or what extra help it provides.

#### Points of Improvement

- Add a clear “Start with recommended mistake” control and identify why that card is recommended.
- Replace ambiguous checkboxes with explicit selectable-card states and instructions.
- Add plain-language move descriptions or a small notation glossary.
- Label “Open in Analysis Board” with its purpose, such as “See more detailed analysis.”
- Keep “Go to puzzle” connected to the specific skill being practiced.

#### Main Strength

The expanded card directly connects an important mistake, its explanation, a better move, an attempt action, and a related puzzle.

#### Main Weakness

The card dashboard requires a novice to choose among unfamiliar categories before the review path is clear.

### Alt 3 - Side-by-Side AI Assistant

#### Task Outcomes

C1: **Success With Hesitation** - I would first look at the selected “Assistant” tab and the greeting, “How can I help you understand this game?” I would interpret the suggested questions and question field as the starting point. Because there is no “Start review” or recommended first action, I would hesitate before selecting a suggested question or typing one. I would count this as eventual success.

C2: **Independent Success** - I would look at the Key Moments panel and see the red-marked “23. Qd3,” then confirm it against “Mistakes 3” and the visible chat question about Qd3. I would identify Qd3 as an important mistake.

C3: **Independent Success** - I would read the assistant response to “Why is Qd3 a mistake?” It states that Qd3 loses the pawn on c3 and that after “...Bxc3,” Black wins the pawn and gets a better position. The explanation is directly visible and understandable without calculating the game myself.

C4: **Independent Success** - I would read the assistant’s answer to “What’s the better move here?” and find “Qe2 is safer!” The suggested move is clearly displayed.

C5: **Success With Hesitation** - I would read that Qe2 protects the pawn on e2 and keeps the queen safe. I would hesitate because the previous explanation focused on losing the pawn on c3, so the visible relationship between protecting e2 and solving the c3 problem is not obvious. I would count the task as eventually complete but not fully convincing.

C6: **Success With Hesitation** - I would inspect the highlighted main board and the mini-board feedback for the suggested move. There is no explicit “Try this move” or “Play Qe2” control, so I would not assume that the move can be executed. The inspection path is visible, but the action path is not.

C7: **Failure** - I would look for “Practice,” “Puzzle,” or a related activity. “Any similar ideas?” may produce more explanation, but it is not a visible practice activity. No concrete puzzle or training action is shown.

C8: **Success With Hesitation** - I would look at the Key Moments list and try selecting another row, such as “24. ...Bxc3” or “22. ...e5.” The list suggests that other moments can be reviewed, but the rows do not have a clear button or “Next mistake” affordance. I would count this as tentative success only.

C9: **Independent Success** - I would use the visible follow-up prompts or type a question in “Type your question…” when the explanation is insufficient. The assistant provides a direct help mechanism without requiring a separate support route.

#### Observations

The assistant panel already shows a question, an explanation, a better move, board highlights, and follow-up prompts. This gives a novice a way to ask for clarification without needing to understand the full analysis interface. The Key Moments list also exposes other game moments.

The workflow is open-ended. A novice must know what to ask, there is no explicit beginner review start, and no practice activity is connected to the explanation. The explanation refers to Qd3 losing a pawn on c3, while the Qe2 explanation refers to protecting the pawn on e2. Without a visible move sequence connecting those statements, I would question whether the suggested move addresses the stated problem.

#### Feedback

After attempting the tasks, I would want starter prompts such as “Show my biggest mistake,” “Explain this move in plain language,” and “Give me a practice puzzle.” I would also want a visible way to play or preview the suggested move and a clear control for moving to the next mistake.

#### Problems Encountered

- [Workflow; High] C1, C7, and C8 have no explicit start, practice, or next-review path.
- [Learning support; High] The interface expects the novice to formulate questions, which may be difficult for someone unfamiliar with chess analysis.
- [Visibility; Medium] C6 has board highlights but no visible “Try this move” or equivalent action.
- [Consistency; Medium] C5 is confusing because the mistake explanation references pawn c3 while the better-move explanation references pawn e2 without showing the connection.
- [Terminology; Medium] C2–C5 use notation such as Qd3, Qe2, and ...Bxc3, plus unexplained key-moment icons.
- [Cognitive load; Medium] Board, assistant tabs, chat, key moments, summary metrics, and follow-up prompts compete for attention.
- [Trust; Medium] The assistant gives definitive explanations, but no visible line, comparison, or confidence information helps a novice verify them.

#### Points of Improvement

- Add guided starter prompts for reviewing the biggest mistake and finding the next mistake.
- Add “Try this move” or “Play/preview Qe2” with visible board feedback.
- Add a direct “Practice this idea” or “Go to puzzle” action.
- Show a consistent move sequence connecting Qd3, ...Bxc3, and Qe2.
- Explain key-moment icons and chess notation in plain language.
- Keep free-form questions as an additional route rather than the only way to request help.

#### Main Strength

The assistant combines plain-language responses with board and mini-board highlights, allowing a novice to ask follow-up questions in context.

#### Main Weakness

The conversational interface explains individual questions but does not provide a complete path from mistake discovery to trying, practicing, and reviewing the next mistake.

### Alt 1 - Beginner Review Flow

#### Task Outcomes

C1: **Independent Success** - I would first look at the “Game Review” heading and the selected “Beginner Review” mode. I would interpret this as the intended starting point for a novice and follow the visible step indicator. I would consider the review entry point clear.

C2: **Independent Success** - I would look at the red “Mistake 2 of 3” panel. The move “Qd3?” is identified, and the explanation states what went wrong. I would identify one important mistake without needing another control.

C3: **Independent Success** - I would read that the queen stopped protecting the pawn on d4 and that Black wins the pawn after “...Nxd4.” The prose explains the cause and consequence directly.

C4: **Independent Success** - I would look immediately below the mistake panel and find “Better move: Qe2.” The label is direct.

C5: **Success With Hesitation** - I would read “Keeps the pawn protected and develops safely.” The first reason is understandable, but “develops safely” is unfamiliar chess terminology and is not explained. I would consider the task eventually complete because the protection reason is clear, with hesitation about the second reason.

C6: **Independent Success** - I would use “Show me on the board” to inspect the move or “Try this move” to attempt it. The two controls communicate different purposes clearly enough to find the required action, although the paper state does not show the result after selection.

C7: **Independent Success** - I would look at “Practice this idea,” read “Puzzle: protect hanging pieces,” and choose “Start practice.” This is a direct connection from the mistake to a practice activity.

C8: **Independent Success** - I would choose “Next mistake” in the review panel or the bottom navigation. The action is clearly labeled and tells me what will happen next.

C9: **Success With Hesitation** - I would look for a help or explanation control. “Full Analysis” is visible, but it sounds like a more advanced mode rather than beginner help. I would try it if the explanation were insufficient, but I would hesitate about whether it would make the problem easier to understand.

#### Observations

The screen presents a fixed sequence: current mistake, explanation, better move, practice, and next mistake. “Show me on the board” and “Try this move” provide two visible ways to inspect or act on the recommendation. The practice card is specifically connected to “protect hanging pieces.”

The main friction is terminology. Qd3, Qe2, d4, and ...Nxd4 are displayed without a plain-language move description. “Develops safely” and “hanging pieces” may also be unfamiliar to a non-chess user. There are several progress indicators: “Step 2 of 3,” “Mistake 2 of 3,” and “Move 23 of 41,” which may be different concepts but are not clearly distinguished.

#### Feedback

After attempting the tasks, I would want the interface to keep the guided sequence but explain notation and terminology at the point of use. I would also want “Full Analysis” to state whether it provides more beginner explanation, engine detail, or both.

#### Problems Encountered

- [Terminology; Medium] C2–C5 use chess notation and phrases such as “develops safely” and “hanging pieces” without definitions.
- [Cognitive load; Medium] C1 and C8 show multiple progress counters that may make it unclear whether the user is progressing through steps, mistakes, or game moves.
- [Learning support; Medium] C5 and C9 do not explain the unfamiliar term “develops safely” or what “Full Analysis” will provide.
- [Visibility; Medium] C6 has clear controls, but the paper state gives no visible result after trying or showing the move.
- [User control; Low] “Show me on the board” and “Try this move” have different implied effects, but the resulting state is not shown.

#### Points of Improvement

- Add a short plain-language description alongside each chess notation label.
- Explain “develops safely” and “hanging pieces” with a small glossary or inline helper.
- Distinguish the progress indicators, such as “Review step,” “Mistake,” and “Game move.”
- Rename “Full Analysis” or add supporting text explaining whether it is beginner-friendly.
- Show the board state or confirmation that appears after “Try this move.”

#### Main Strength

The flow provides a concrete sequence from identifying a mistake to understanding it, finding a better move, practicing the idea, and reviewing another mistake.

#### Main Weakness

The guided path is clear, but unfamiliar chess terminology can prevent a novice from fully understanding why the suggested move is better.

### Chess Preference

- Preferred alternative: Alt 1 - Beginner Review Flow
- Reason: It gives the clearest novice path from mistake to explanation, better move, practice, and next review item without requiring the user to choose among many cards or formulate questions.
- Trade-off: Alt 2 provides more flexible self-selection and a direct puzzle link, while Alt 3 provides richer follow-up explanation. Alt 1 is less flexible and its “Full Analysis” help route remains unclear.

## Overall Review

- Most confusing element: The Chess Alt 3 explanation connects Qd3 to losing the pawn on c3, then describes Qe2 as protecting the pawn on e2 without visibly explaining how those positions relate.
- Clearest element: FIFA Alt 3’s Quick Actions, especially “View Tickets,” “Transfer Tickets,” and “Add to Calendar,” because each has a direct label and supporting description.
- Most useful concept: Connecting a current state or mistake to a concrete next action, such as FIFA Alt 2’s “Ticket ready — 72h before match” and Chess Alt 1’s “Practice this idea.”
- Highest-priority improvement: Make every workflow explicit as “current state → next expected step → concrete action,” while replacing unexplained chess notation and ambiguous controls with plain-language guidance.
- Accessibility evidence limit: Static paper images cannot establish keyboard access, focus order, screen-reader labels, zoom behavior, or inclusive interaction support; those require separate accessibility testing.

### AI Reviewer R3 - Full Record

# AI Reviewer R3

## Reviewer Profile

- Methodology label: AI-Agent Formative Testing
- Digital literacy: Low-to-medium
- Domain familiarity: FIFA ticket familiarity none; Chess analysis familiarity none
- Behavior model: Hesitates when many choices appear and prefers explicit guidance
- Assigned prototype order: FIFA Alt 3 -> Alt 1 -> Alt 2; Chess Alt 3 -> Alt 1 -> Alt 2

## Scenario 1 - FIFA

### Alt 1 - Status Dashboard

#### Task Outcomes

F1: Independent Success - I first look at the four status tiles, then the event cards. I interpret Confirmed, Pending, Action needed, and Cancelled as the main ticket states. The counts and event labels let me identify the displayed status without another route.

F2: Independent Success - I first scan for the orange Pending tile and the orange Al Hilal vs Real Madrid card. I interpret “Awaiting FIFA confirmation” as the information still needing attention or progress. The screen also shows zero items under “Action needed,” which is clear.

F3: Success With Hesitation - I first read the text beneath each status label. “Ready to go” and “Tickets are valid” explain Confirmed, while “Awaiting update” and “Awaiting FIFA confirmation” explain Pending. I would select “What does this mean?” to verify the pending state, but the actual explanation is not visible, so I hesitate.

F4: Failure - I first look inside the pending event card and at “See details.” I would probably select “See details,” but I do not know whether that shows the next expected step or only more ticket information. No explicit “Next step” or expected date is displayed.

F5: Success With Hesitation - I first look beside the greeting and read “Last updated: 2 mins ago,” with a refresh icon. This makes the information appear current. However, the “Upcoming Events” section includes one event dated June 16, 2025 and another dated March 25, 2026, which makes me question whether all event information is current.

F6: Success With Hesitation - I first inspect the browser address and FIFA branding. I would tentatively treat `fifa.com/tickets` as official, but I hesitate because there is no visible “Official FIFA source” label beside the information.

F7: Independent Success - I first look inside the confirmed event card and see a clearly labeled “View Tickets” button. I would select it to access ticket details or entry information.

F8: Independent Success - I first scan the “Quick Actions” panel on the right. “Transfer Tickets” is clearly labeled with a description about sending tickets to friends or family, so I would select that shortcut.

F9: Independent Success - I first scan the same “Quick Actions” panel. “Add to Calendar” is visible with the explanation “Never miss your event,” so I would select it.

F10: Failure - I first look around the quick actions and the lower page for a warning about leaving FIFA.com. I do not find a partner-site notice, external-service explanation, or confirmation step. I would not assume that any action leaves FIFA.com.

#### Observations

The four status tiles are the clearest starting point for a novice who wants a quick account-level summary. The event cards then connect the summary to specific matches. “View Tickets,” “View Order,” “Transfer Tickets,” and “Add to Calendar” use familiar labels.

The pending card explains the immediate state but not what will happen next. “What does this mean?” is a useful help cue, but the prototype does not show the explanation after selecting it. The page also does not visibly identify the source as official beyond the FIFA branding and URL.

Accessibility/inclusive observation from the image only: status colors are paired with text labels, which helps, but the interface still relies heavily on green, orange, blue, and gray. Refresh, information, and some other controls are icon-based or small, so their text alternatives and assistive-technology behavior are not evident.

#### Feedback

The dashboard should add a short line under each event such as “Next: FIFA confirmation” or “Next: mobile ticket delivery 72 hours before the match.” The pending state should also state whether the user must act or simply wait.

Add an “Official FIFA source” label and a visible handoff warning for actions that may open a partner service. The “What does this mean?” link should reveal plain-language status details directly.

The date shown under “Upcoming Events” should be corrected or clarified because the 2025 date conflicts with the surrounding future-event presentation.

#### Problems Encountered

- [Workflow; High] F4: No explicit next expected step is shown; “See details” is a guess rather than clear guidance.
- [Trust; Medium] F6 and F10: FIFA branding suggests legitimacy, but there is no official-source marker or external-service handoff warning.
- [Consistency; Medium] F5: An event dated June 16, 2025 appears under “Upcoming Events” beside a 2026 event.
- [Terminology; Medium] F3: “Pending,” “Awaiting update,” and “Awaiting FIFA confirmation” require the novice to reconcile several similar phrases.
- [Feedback; Medium] F2 and F4: The pending state does not show whether the user should wait, provide information, or take another action.

#### Points of Improvement

- Add a visible “Next step” line and expected timing to every event card.
- Show an explicit “No action needed” or “Action required” message for each pending state.
- Add an “Official FIFA source” badge near the status information.
- Display a handoff warning directly beside any action that opens an official partner service.
- Correct or explain the inconsistent event date.
- Provide text labels or accessible descriptions for icon-only controls.

#### Main Strength

The status counts and event cards provide a compact path from overall ticket status to direct actions such as viewing, transferring, and calendaring tickets.

#### Main Weakness

The dashboard identifies the current state but does not clearly explain what happens next or how to verify official status.

### Alt 2 - Timeline Tracker

#### Task Outcomes

F1: Independent Success - I first look at the large timeline for Argentina vs Brazil. I interpret the green checks, blue current step, and “ON TRACK” label as the current ticket status. The second timeline separately shows a pending state.

F2: Independent Success - I first scan for orange markers and the “PENDING” label. The USA vs Mexico order has “Payment received Pending,” with later stages still shown as dashes. I can identify that this order is still progressing.

F3: Success With Hesitation - I first read the status message below each timeline. “Your order is progressing normally” explains the first event, while the orange payment step explains the second. However, “Payment received” followed by “Pending” sounds contradictory, so I am not fully certain whether payment is complete or still waiting.

F4: Independent Success - I first look at the numbered timeline stages. For Argentina vs Brazil, Verification is current, Ticket ready is next, and the mobile ticket is expected 72 hours before the match. For USA vs Mexico, Verification follows the pending payment step. The next expected step is visible.

F5: Independent Success - I first look at “Last updated: 2 mins ago,” then at “Freshness & Updates,” “View update history,” and the visible update log. These signals make it clear that the information was recently refreshed and that prior changes can be checked.

F6: Independent Success - I first look beside the timestamp and see the explicit “Official FIFA source” label. I would use that label as the visible indication that the information appears official.

F7: Failure - I first scan both timeline cards for “View Tickets.” No such control is visible. I might try “My Tickets” in the left navigation, but that is a guess and does not identify a visible View Tickets action.

F8: Failure - I scan the timeline cards and right-side panels for “Transfer Tickets.” It is not present. I would have to guess that the action is somewhere under My Tickets or Orders.

F9: Success With Hesitation - I first look in “Freshness & Updates” and find “Sync to calendar.” I would interpret this as the likely calendar action, but I hesitate because the task wording and visible control do not match exactly.

F10: Failure - I first inspect “Official Next Steps” and the source label for an external-service warning. The page says the source is official but does not state what happens before leaving FIFA.com or which step opens another service.

#### Observations

The timeline makes current, completed, and upcoming stages visible. “Ticket ready 72h before match” is especially useful because it answers both status and timing. “What changed?” and “View update history” provide a clearer freshness model than the other FIFA screens.

The page is more information-dense than Alt 1. “Verification,” “On track,” and “Sync to calendar” may require interpretation for someone unfamiliar with ticket workflows. The timeline is strong for monitoring but does not expose common ticket actions.

Accessibility/inclusive observation from the image only: the status words and timeline numbers are present in addition to color, which is helpful. The filter/refresh-style icons and small timeline labels could still be difficult to interpret without visible text or a larger layout.

#### Feedback

Keep the timeline and update history, but add a direct action row to each ticket with “View Tickets,” “Transfer Tickets,” and “Add to Calendar.” Rename “Sync to calendar” to “Add to Calendar,” or show both terms.

Clarify the pending payment wording with a sentence such as “Payment information is still being verified.” Add a “Before you leave FIFA.com” warning if any official next step opens a partner site.

#### Problems Encountered

- [Visibility; High] F7 and F8: View Tickets and Transfer Tickets are absent from the visible workflow.
- [Workflow; High] F7 and F8: The novice must guess whether My Tickets or Orders contains common actions.
- [Terminology; Medium] F3 and F9: “Payment received Pending” and “Sync to calendar” are not immediately equivalent to the requested concepts.
- [Trust; Medium] F10: Official-source labeling does not explain the external handoff process.
- [Cognitive load; Medium] F1-F4: Five stages, multiple timelines, update history, and side panels require repeated scanning.

#### Points of Improvement

- Add clearly labeled ticket actions to each timeline card.
- Use a plain-language pending explanation instead of combining “Payment received” with “Pending.”
- Rename “Sync to calendar” to “Add to Calendar.”
- Add a partner-service warning before external navigation.
- Visually emphasize the current step and the next step with text as well as color.
- Provide a simpler default view with optional expansion for the full timeline.

#### Main Strength

The timeline clearly shows what has happened, what is happening now, and what is expected next, with supporting freshness information.

#### Main Weakness

The design handles monitoring well but leaves basic ticket actions such as viewing and transferring tickets outside the visible flow.

### Alt 3 - Action Hub

#### Task Outcomes

F1: Success With Hesitation - I first look at the central event card and read “CONFIRMED” and “Tickets are valid.” I can identify the displayed event status, but only one confirmed event is shown and no progressing or pending event is visible, so I cannot determine the complete account situation described in the scenario.

F2: Failure - I first scan the event card, Quick Actions, and status-related areas for Pending or Action needed. None is visible. I would not infer that the absence means no information needs attention because the screen gives no explicit pending or empty-state message.

F3: Independent Success - I first read the event-card status. “CONFIRMED” and “Tickets are valid” directly explain the displayed state, so I can describe it without opening another panel.

F4: Failure - I first look below the status for a timeline or “Next step” message. “See details,” notifications, and the action tiles are visible, but none says what is expected to happen next for the confirmed ticket.

F5: Independent Success - I first look near the greeting and read “Last updated: 2 mins ago,” alongside a refresh icon. I would conclude that the displayed information appears recently updated.

F6: Independent Success - I first look beside the timestamp and see “Official FIFA source.” The official-source label and FIFA branding make the information appear official.

F7: Independent Success - I first look at the confirmed event card and then at the first Quick Actions tile. Both provide a clearly labeled “View Tickets” action, so I would select either one.

F8: Independent Success - I first scan the Quick Actions grid. “Transfer Tickets” is a large labeled tile with a description about sending tickets securely, so I would select it.

F9: Independent Success - I first scan the top row of Quick Actions. “Add to Calendar” is clearly labeled and paired with a calendar icon.

F10: Independent Success - I first look at the bottom notice titled “Before you leave FIFA.com.” It says some options open on official partner sites and explains that security and data are protected. I would read “Learn more” before selecting an option such as the marketplace.

#### Observations

The Action Hub puts the three requested common actions—View Tickets, Transfer Tickets, and Add to Calendar—in prominent tiles. The official-source label and “Before you leave FIFA.com” notice answer trust questions more directly than Alt 1.

The screen is action-oriented but shows only a confirmed event. There is no visible pending count, attention-needed state, event timeline, or next expected step. Eight Quick Actions, three Official Options cards, support content, notifications, and security information create a large number of possible starting points for a low-confidence novice.

Accessibility/inclusive observation from the image only: most action icons have text labels, which supports recognition. The design still uses many border colors to separate actions, and controls such as refresh, close, and some information symbols do not have visible text alternatives.

#### Feedback

Keep the prominent Quick Actions, but add a compact status summary and a “What happens next” line to the event card. If there are no pending items, state that explicitly; if there are pending items, show them in the same hub.

Place the external-service warning immediately beside each relevant option, not only in a page-wide notice. Reduce the number of equally prominent optional cards or add a “Start here” recommendation for first-time users.

#### Problems Encountered

- [Information hierarchy; High] F2 and F4: The action hub gives priority to actions but does not show pending information or the next expected ticket step.
- [Visibility; Medium] F2: There is no explicit pending or “no attention needed” state.
- [Cognitive load; Medium] F1-F4: Eight Quick Actions plus Official Options and support panels create many competing choices.
- [Workflow; Medium] F4: “See details” is available, but no visible path explains what happens next.
- [Terminology; Low] F10: “Official Options,” “Official Resale Marketplace,” and “partner service” may need explanation for a novice.

#### Points of Improvement

- Add confirmed, pending, and action-needed status summaries to the hub.
- Add an explicit next-step sentence to every event card.
- Show “No pending items” when there is nothing requiring attention.
- Add “Opens an official partner site” beside each external option.
- Group optional services below primary ticket actions or add a clear recommended starting point.
- Provide text alternatives for icon-only controls and do not rely on color alone.

#### Main Strength

The most common ticket actions and external-service trust information are visible together with clear labels.

#### Main Weakness

The page makes it easy to act on a confirmed ticket but does not help a novice monitor progressing or attention-needed information.

### FIFA Preference

- Preferred alternative: Alt 1 - Status Dashboard
- Reason: I would first read the four status counts, then inspect the event card, and finally use the small Quick Actions group. It gives the best balance between understanding status and finding common ticket actions without requiring me to interpret a five-step timeline or scan many action cards.
- Trade-off: It does not provide Alt 2’s explicit next-step timeline or Alt 3’s clear official handoff warning, so I would still need guidance about what happens next and whether an action leaves FIFA.com.

## Scenario 2 - Chess

### Alt 1 - Beginner Review Flow

#### Task Outcomes

C1: Success With Hesitation - I first look at “Game Review” and the selected “Beginner Review” mode. These suggest where a novice should begin, but the page opens at “STEP 2 OF 3” and does not show a clear Start Review control. I would hesitate between using Beginner Review, Back, and Previous.

C2: Independent Success - I first look at the red “Mistake 2 of 3” panel and the highlighted board squares. The move Qd3 is clearly identified as the mistake.

C3: Independent Success - I first read the mistake explanation. It says the queen stopped protecting the pawn on d4 and that Black wins the pawn after ...Nxd4. This explains the consequence in plain language.

C4: Independent Success - I first look directly below the mistake explanation and see “Better move: Qe2.” I would use Qe2 as the suggested alternative.

C5: Independent Success - I read the sentence under Qe2: “Keeps the pawn protected and develops safely.” This gives a concrete reason the suggested move is better.

C6: Independent Success - I first look for an action connected to the better move. “Try this move” is clearly labeled, and “Show me on the board” provides a second way to inspect the position.

C7: Independent Success - I first scan below the suggested move and find “Practice this idea” with “Start practice.” The connection to a practice activity is explicit.

C8: Independent Success - I first look at the bottom-right navigation and find “Next mistake.” I would select it to review another key moment.

C9: Success With Hesitation - I first look at the top “Full Analysis” option because the beginner explanation may be insufficient. I would select it, but I am unsure whether it will provide help or expose a more difficult interface. No clearly labeled Help or ask-a-question control is visible.

#### Observations

The flow connects mistake explanation, better move, move inspection, practice, and the next mistake in one vertical sequence. The wording “protects the pawn” and “develops safely” is understandable without chess-analysis knowledge.

The page opens mid-review, with both “STEP 2 OF 3” and “Move 23 of 41.” A novice may not know whether the numbered step or the move number controls progress. The chess notation Qd3, Qe2, and ...Nxd4 is unfamiliar, although the plain-language explanation reduces the problem.

Accessibility/inclusive observation from the image only: the board has coordinates and the controls have text labels. Meaning is still partly carried by red, blue, green, and orange highlighting, and the small gear icon has no visible explanation.

#### Feedback

Provide a clear entry state such as “Start Beginner Review” or “Start with the most important mistake.” Distinguish review-step navigation from move-by-move board navigation.

Add a visible “Need more explanation?” action that opens a plain-language explanation or question field. After “Try this move,” show what changed or why the move succeeds so the result is not left implicit.

#### Problems Encountered

- [Workflow; Medium] C1: The screen opens at step 2 without showing how to start the review.
- [Cognitive load; Medium] C1 and C8: Review steps, move numbers, Back, Previous, and Next controls create overlapping navigation models.
- [Learning support; Medium] C9: Full Analysis is the only apparent deeper-help route, but its purpose and difficulty are unclear.
- [Terminology; Low] C2-C5: Algebraic chess notation remains unfamiliar despite the plain-language explanation.
- [Feedback; Medium] C6: The static screen shows the Try this move control but not the result after using it.

#### Points of Improvement

- Add an explicit beginner entry point and identify the recommended first mistake.
- Separate “next mistake” navigation from board move navigation with distinct labels.
- Add an in-context question or help action.
- Explain chess notation the first time it appears.
- Show the board state and learning result after trying the better move.
- Keep text labels alongside color and icons.

#### Main Strength

The flow gives a novice a direct sequence from identifying a mistake to understanding it, trying a better move, practicing the idea, and continuing.

#### Main Weakness

The entry point and deeper-help path are unclear because the prototype starts at step 2 and offers no simple way to ask for more explanation.

### Alt 2 - Card Review Mode

#### Task Outcomes

C1: Success With Hesitation - I first look at the game summary and then the “Review your key moments” card grid. There are six possible cards and no single “Start review” choice, so I would scan the cards and select the highlighted Missed Tactic card or “Review this card.” I can start, but I hesitate because several choices look equally important.

C2: Independent Success - I first look at the red Mistakes and Blunders summary chips and the red “Missed Tactic” card. The selected card identifies a specific important mistake at Move 23.

C3: Independent Success - I first read the expanded card text. It says the queen on c3 was attacked and that capturing the pawn on c3 would have gained material. This explains why the move was a problem.

C4: Independent Success - I first look at the expanded detail beside the mini-board and see “Better move: Qxc3.” I would use Qxc3 as the suggested move.

C5: Independent Success - The text immediately explains that Qxc3 captures the pawn on c3 and wins material. I can understand the benefit without additional analysis.

C6: Independent Success - I first look at the expanded card actions. “Try this move,” the mini-board preview, and “Open in Analysis Board” all provide ways to inspect or try the suggestion.

C7: Independent Success - I first scan the orange action buttons and find “Go to puzzle.” The label directly connects the mistake to a practice activity.

C8: Independent Success - I first look at “Choose another card” and the other key-moment cards. I would select another card such as Hanging Pawn, Queen Safety, or Best Move to continue reviewing.

C9: Success With Hesitation - I first look at “Open in Analysis Board” for deeper help. The control is visible, but I do not know what an Analysis Board does or whether it will explain the mistake in simpler language. I would select it only after some hesitation.

#### Observations

The selected card contains the mistake, reason, better move, explanation, mini-board, Try this move, and puzzle route in one place. “Go to puzzle” is a particularly concrete bridge from review to practice.

The dashboard presents summary metrics, six cards, a filter, several card states, and multiple actions. The small square controls on the cards may look like checkboxes for selecting multiple cards rather than controls for opening one review. Terms such as Opening, Endgame, Blunders, and Analysis Board are unfamiliar to a non-chess user.

Accessibility/inclusive observation from the image only: the cards use text and small board previews in addition to color, but the red/green/blue coding remains prominent. The small card controls and filter icon may need larger targets and explicit labels.

#### Feedback

Add a “Start here” recommendation, such as the most important mistake, before presenting all six cards. Make the card interaction explicit by labeling cards as “Open review” rather than using checkbox-like controls.

Describe “Analysis Board” in beginner language and provide a “Explain more simply” or equivalent help action. Keep the direct puzzle and Try this move actions.

#### Problems Encountered

- [Cognitive load; High] C1: Six cards, summary metrics, and filters create too many possible starting points for a low-confidence novice.
- [Visibility; Medium] C1 and C8: Checkbox-like marks do not clearly communicate whether a card should be selected, opened, or multi-selected.
- [Workflow; Medium] C1: There is no recommended first card or guided review sequence.
- [Learning support; Medium] C9: Analysis Board is visible but does not explain how it helps.
- [Terminology; Medium] C2-C9: Blunder, Opening, Endgame, and Analysis Board may be unfamiliar.

#### Points of Improvement

- Mark one card as “Start here” and explain why it is recommended.
- Replace ambiguous checkbox styling with clear card-button or “Open review” affordances.
- Add beginner explanations for chess categories and Analysis Board.
- Add a plain-language deeper-help action beside the explanation.
- Keep the existing direct “Try this move” and “Go to puzzle” actions.
- Provide non-color status labels for all card states.

#### Main Strength

Each selected card combines the mistake, reason, better move, move inspection, and practice action without requiring several separate screens.

#### Main Weakness

The large number of equally visible cards makes the starting point unclear for a novice who prefers explicit guidance.

### Alt 3 - Side-by-Side AI Assistant

#### Task Outcomes

C1: Success With Hesitation - I first look at the Assistant panel, which asks how it can help, and then at the Key Moments list. There is no “Start Review” control, so I would either select the red Qd3 moment or type a question. A plausible starting point exists, but I have to choose it myself.

C2: Independent Success - I first look at Key Moments and see Move 23, Qd3 marked with a red question icon. The conversation also refers to Qd3, so the important mistake is easy to identify.

C3: Independent Success - I first read the assistant’s response. It says Qd3 loses the pawn on c3 and that after ...Bxc3 Black wins the pawn and gets a better position. The mini-board and board highlights reinforce the explanation.

C4: Independent Success - I first look at the user’s displayed question “What’s the better move here?” and the assistant’s response “Qe2 is safer!” The better move is directly visible.

C5: Independent Success - I read the explanation under Qe2: it protects the pawn on e2 and keeps the queen safe. This gives a clear reason for the recommendation.

C6: Success With Hesitation - I first inspect the green-highlighted board square and the mini-board response. I can visually inspect the suggested move, and I might select “Show variations,” but there is no explicit “Try this move” control or clear move-entry action.

C7: Failure - I first look at the suggested follow-up prompts and the assistant input. “Any similar ideas?” could produce another explanation, but there is no visible puzzle, practice, or training activity to open.

C8: Success With Hesitation - I first look at the Key Moments list and see other moves such as d4 and ...Bxc3. I would try selecting another row, but there is no “Next mistake” button or clear instruction that the rows are the continuation path.

C9: Independent Success - I first look at the suggested questions and the “Type your question...” field. If the explanation were insufficient, I would type a follow-up question or choose “Show variations.”

#### Observations

The assistant provides contextual explanations in plain language and keeps the relevant board position visible. Suggested questions reduce the burden of inventing a prompt, which is useful for someone unfamiliar with chess analysis.

The interface has several competing areas: Assistant, Analysis, Review, Details, Openings, Key Moments, Game Summary, the board, and the conversation. The displayed exchange already contains answers, but the image does not show how a novice reaches the first question or changes to another mistake.

The screen supports inspection but not an obvious move-trying or practice workflow. Chess notation such as Qd3, ...Bxc3, and Qe2 remains visible even though the explanation is conversational.

Accessibility/inclusive observation from the image only: the conversation uses text labels and board highlights, but key-moment state still relies on red, orange, and green icons. The send icon and several navigation icons have no visible text explanation.

#### Feedback

Add a prominent “Start with the most important mistake” action and a clear “Next key moment” control. Make Key Moments visibly selectable and state what happens when a row is selected.

Add “Try this move” or “Practice this idea” beside the assistant’s recommendation. If the intended action is only visual inspection, label it “Show the move on the board.” Keep the suggested questions and free-form input because they offer a clear route to additional help.

#### Problems Encountered

- [Workflow; Medium] C1 and C8: The assistant does not provide an explicit start or continuation sequence.
- [Visibility; Medium] C6: Board highlights and “Show variations” do not clearly indicate how to try the move.
- [Learning support; High] C7: No concrete practice activity or puzzle route is visible.
- [Cognitive load; Medium] C1 and C9: Multiple tabs, panels, metrics, and conversation controls compete for attention.
- [Terminology; Medium] C2-C6: Algebraic notation and analysis tabs may be unfamiliar to a novice.

#### Points of Improvement

- Add “Start review” and “Next key moment” controls.
- Add a clearly labeled Try this move or Practice this idea action.
- Provide a direct puzzle or practice link from an important mistake.
- Make Key Moments rows visibly interactive.
- Explain chess notation and advanced tabs in beginner language.
- Keep color as reinforcement, not the only indication of mistake or progress.

#### Main Strength

The assistant answers “why” and “what is better” questions in context while showing corresponding board highlights.

#### Main Weakness

It offers flexible explanation but does not provide a clear path from the first review step to trying and practicing the recommended move.

### Chess Preference

- Preferred alternative: Alt 1 - Beginner Review Flow
- Reason: The visible sequence from Mistake to Better move to Try this move to Practice this idea to Next mistake matches how I would expect a beginner review to proceed. The plain-language explanation reduces the need to understand chess terminology before acting.
- Trade-off: It is less flexible than the assistant and less selectable than the card dashboard. Full Analysis is also an unclear route when I need additional help.

## Overall Review

- Most confusing element: The Chess Alt 2 card grid, especially the six cards with small checkbox-like controls. I would not immediately know whether to check several cards, open one card, or follow a recommended order.
- Clearest element: FIFA Alt 3 Quick Actions, where “View Tickets,” “Transfer Tickets,” and “Add to Calendar” are visible as large, direct labels.
- Most useful concept: Pairing an explanation with a concrete next action, especially “Better move” followed by “Try this move” and “Practice this idea.”
- Highest-priority improvement: Add explicit beginner guidance for the next step in every flow: “Start here,” “What happens next,” and a clearly labeled action or practice route.

### AI Reviewer R4 - Full Record

# AI Reviewer R4
## Reviewer Profile
- Methodology: AI-Agent Formative Testing
- Digital literacy: High
- Domain familiarity: Low familiarity with FIFA and Chess
- Behavior model: Fast scanner; scans headings, cards, status colors, and prominent actions before detail
- Assigned prototype order: FIFA Alt 1 -> Alt 3 -> Alt 2; Chess Alt 1 -> Alt 3 -> Alt 2

## Scenario 1 - FIFA

### Alt 1 - Status Dashboard

#### Task Outcomes

F1: Independent Success - I first scan the four status cards, then the event cards. “Confirmed,” “Pending,” and “Action needed” provide a clear summary, while each event card gives its own status.

F2: Independent Success - I look at the orange Pending card and the Al Hilal vs Real Madrid card. “Pending” and “Awaiting FIFA confirmation” clearly identify the information still progressing.

F3: Success With Hesitation - I interpret “Confirmed” and “Tickets are valid” as ready for use, and “Pending” as awaiting confirmation. I would select the small “What does this mean?” link, but the visible screen does not explain the exact consequence or expected timing.

F4: Failure - I first look inside the pending event card. I would choose “View Order” or “What does this mean?” as exploratory actions, but no visible control states the next expected step or when the update should occur.

F5: Independent Success - I scan the top-right “Last updated: 2 mins ago” text and refresh icon. This makes the page appear current, although freshness is shown for the page rather than separately for each event.

F6: Success With Hesitation - I check the browser address and FIFA branding and infer that the page appears official. I hesitate because there is no explicit “Official FIFA source” label.

F7: Independent Success - I first scan the confirmed event card and find the clearly labeled “View Tickets” button.

F8: Independent Success - I scan the Quick Actions panel and select “Transfer Tickets.”

F9: Independent Success - I scan the same Quick Actions panel and select “Add to Calendar.”

F10: Failure - I look around the Quick Actions, event cards, and support panels for an external-service warning. No visible element explains what happens before leaving FIFA.com.

#### Observations

The summary cards are highly visible and separate confirmed, pending, action-needed, and cancelled states. The event cards repeat the status with supporting text. Common actions are placed in a separate Quick Actions panel. The pending status has several similar phrases—“Pending,” “Awaiting update,” and “Awaiting FIFA confirmation”—but no visible timeline or next-step instruction.

#### Feedback

Keep the status summary and direct ticket actions. Add a per-event line such as “Next: Await FIFA confirmation” or “Next update expected…” and show the official source directly beside each event. The “What does this mean?” link should reveal a plain-language explanation and expected user action.

#### Problems Encountered

- [Workflow; High] F4 lacks an explicit next expected step; “View Order” does not communicate whether the user should wait, verify something, or take action.
- [Terminology; Medium] F3-F4 use several overlapping pending labels without distinguishing their meanings.
- [Trust; Medium] F6 relies on the URL and branding because no official-source badge is visible.
- [Visibility; High] F10 has no visible handoff warning or external-service explanation.

#### Points of Improvement

- Add a per-event “Current status,” “Next step,” and “Expected timing” block.
- Replace or supplement “Pending” and “Awaiting update” with one plain-language explanation.
- Add an “Official FIFA source” label beside each event.
- Add a “Before you leave FIFA.com” warning connected to any external action.

#### Main Strength

The combination of status cards and event-level labels lets a fast scanner identify confirmed versus pending tickets quickly.

#### Main Weakness

The dashboard shows status clearly but does not explain what the user should do next or what happens when an action leaves FIFA.com.

### Alt 2 - Timeline Tracker

#### Task Outcomes

F1: Independent Success - I first scan the large event cards for “ON TRACK” and “PENDING,” then inspect the highlighted timeline stage. The blue “Verification” stage makes the current state clear.

F2: Independent Success - I look at the second event card and find the orange “PENDING” label on “Payment received.” The update log also shows that verification has started, so I can identify the progressing information.

F3: Independent Success - I read “Your order is progressing normally,” the highlighted “Verification” stage, and the pending payment label. These elements explain the displayed statuses without requiring a different page.

F4: Independent Success - I follow the timeline from the current “Verification” stage to “Ticket ready 72h before match.” The “Official Next Steps” panel also provides delivery and entry guidance.

F5: Independent Success - I first look at “Last updated: 2 mins ago,” then use “What changed?” and “View update history” to confirm that recent updates are visible.

F6: Independent Success - I notice the “Official FIFA source” badge beside the freshness information and the FIFA URL. The source appears official without needing further interpretation.

F7: Failure - I scan the event cards and side panels but find “See full timeline,” “View update history,” and “Ticket delivery guide,” not a “View Tickets” control.

F8: Failure - I search the action and next-step panels but find no “Transfer Tickets” option or equivalent control.

F9: Success With Hesitation - I find “Sync to calendar” in the Freshness & Updates panel and interpret it as the calendar action. I hesitate because “Sync” could mean ongoing synchronization rather than adding this event.

F10: Failure - I look for a warning before an external action, but the screen only identifies the source as official. It does not state what happens before leaving FIFA.com.

#### Observations

The timeline makes completed, current, and upcoming stages visible in one horizontal sequence. “Last updated,” “What changed?,” and “View update history” support freshness. However, the design prioritizes progress tracking over direct ticket management; the required ticket actions are not visible.

#### Feedback

Keep the timeline and official-source badge. Add direct “View Tickets” and “Transfer Tickets” controls to each relevant event, rename “Sync to calendar” to “Add to Calendar” if that is the intended action, and add an explicit external-service handoff message.

#### Problems Encountered

- [Workflow; High] F7-F8 require ticket actions that are not visible in the timeline view.
- [Terminology; Medium] F9 uses “Sync to calendar,” which is less direct than “Add to Calendar.”
- [Trust; High] F10 has an official-source label but no warning about leaving FIFA.com.
- [Information hierarchy; Medium] Progress controls dominate the page while common ticket actions are absent.

#### Points of Improvement

- Add “View Tickets” and “Transfer Tickets” beside each event.
- Use a direct “Add to Calendar” label with the event name.
- Add a “Before you leave FIFA.com” message beside any partner or external action.
- Preserve the timeline but provide a compact action row below each event.

#### Main Strength

The timeline clearly communicates current progress, expected timing, freshness, and official sourcing.

#### Main Weakness

It does not support common ticket actions, especially viewing or transferring tickets.

### Alt 3 - Action Hub

#### Task Outcomes

F1: Success With Hesitation - I first scan the confirmed event card and see “CONFIRMED” and “Tickets are valid.” I can identify the visible event status, but there is no second progressing event or overall status summary, so I cannot establish the full situation described in the scenario.

F2: Failure - I scan the event card, Quick Actions, and official options for a pending or attention-needed label. No pending event or attention state is visible.

F3: Independent Success - I read “CONFIRMED” and “Tickets are valid” on the event card. These phrases provide a direct explanation of the displayed status.

F4: Failure - I first look at the event card and then the Quick Actions. “See details” is available, but there is no visible timeline or explicit next expected step.

F5: Independent Success - I find “Last updated: 2 mins ago” and the refresh icon at the top of the page.

F6: Independent Success - I see the FIFA URL, the “Official FIFA source” badge, and “Official” labels on the options. These provide several visible signals of official status.

F7: Independent Success - I find “View Tickets” both on the event card and in the Quick Actions grid.

F8: Independent Success - I find the prominent “Transfer Tickets” shortcut.

F9: Independent Success - I find the prominent “Add to Calendar” shortcut.

F10: Independent Success - I read the “Before you leave FIFA.com” banner, including the statement that some options open on official partner sites and that security and data are protected.

#### Observations

The page is organized around large, labeled action cards. View, transfer, resale, calendar, itinerary, venue, guide, and support actions are immediately visible. Official options and the external handoff message are also visible. Status coverage is limited to one confirmed event, with no pending or timeline state.

#### Feedback

Keep the action grid and the explicit handoff warning. Add a status summary or additional event cards so pending and attention-needed information remains visible. Include a per-event next-step message above the shortcuts.

#### Problems Encountered

- [Visibility; High] F2 has no visible pending or attention-needed information.
- [Workflow; High] F4 provides shortcuts but no explicit next expected step.
- [Information hierarchy; Medium] F1 presents one confirmed event prominently, which can make the page appear complete even though progressing information is not represented.
- [Cognitive load; Medium] The large shortcut grid, official options, support panel, and security panel compete for attention after the single event card.

#### Points of Improvement

- Add confirmed, pending, and attention-needed status cards or event rows.
- Add “Next step” and “Expected timing” to the event card.
- Keep the handoff banner visible but associate it with the specific external option being selected.
- Group the most common ticket actions separately from lower-frequency guides and marketplace options.

#### Main Strength

The required ticket actions and the external-service warning are highly visible and easy to locate.

#### Main Weakness

The action-first layout does not show the full current ticket situation, especially pending information.

### FIFA Preference

- Preferred alternative: Alt 1 - Status Dashboard
- Reason: It is the best balance between status understanding and common actions. I can see both confirmed and pending information, then find View Tickets, Transfer Tickets, and Add to Calendar.
- Trade-off: Alt 2 explains progress, freshness, and official sourcing more clearly, while Alt 3 gives the clearest handoff warning and shortcut actions. Alt 1 lacks those explicit next-step and external-service explanations.

## Scenario 2 - Chess

### Alt 1 - Beginner Review Flow

#### Task Outcomes

C1: Success With Hesitation - I first look for the “Game Review” heading and the selected “Beginner Review” mode. The “STEP 2 OF 3” indicator shows where I am, but the lack of a visible “Start review” or “Review from beginning” control makes the starting point slightly unclear.

C2: Independent Success - I scan the red card labeled “Mistake 2 of 3” and identify the move “Qd3?” as the important mistake.

C3: Independent Success - I read that the queen stopped protecting the pawn on d4 and that Black wins the pawn after “…Nxd4.” The notation is unfamiliar, but the plain-language explanation gives the reason.

C4: Independent Success - I scan the blue “Better move” card and find “Qe2.”

C5: Independent Success - I read that Qe2 keeps the pawn protected and develops safely. The first explanation is understandable even though “develops” is chess-specific language.

C6: Independent Success - I would first choose “Show me on the board” to inspect the position, then use “Try this move” to attempt Qe2. Both controls have clear labels, although the resulting feedback is not shown in this prototype state.

C7: Independent Success - I find “Practice this idea,” the “protect hanging pieces” description, and the orange “Start practice” button.

C8: Independent Success - I find “Next mistake” at the bottom of the review panel and would use it to continue.

C9: Success With Hesitation - I first look at the “Full Analysis” toggle as a possible source of more help. I would select it, but it is not clear whether it will provide a clearer explanation or switch to a more advanced mode.

#### Observations

The screen creates a visible chain from mistake identification to explanation, better move, board inspection, practice, and the next mistake. Red, blue, and orange sections separate problem, guidance, and practice. Chess notation appears in several places without a plain-language translation.

#### Feedback

The guided sequence is easy to follow once the current review screen is understood. Add a clear starting control, translate notation into move descriptions, and provide an in-context “Need more explanation?” option instead of relying on Full Analysis.

#### Problems Encountered

- [Visibility; Medium] C1 shows the user at step 2 of 3 but does not show how to restart or begin from step 1.
- [Terminology; Medium] C3-C5 use “Qd3,” “Qe2,” “…Nxd4,” and “develops safely,” which may be unfamiliar to a low-domain-familiarity user.
- [Learning support; Medium] C9 has no clearly labeled additional-help path; Full Analysis may feel like an advanced mode rather than assistance.
- [Feedback; Low] C6 does not show what happens after “Try this move” or “Show me on the board.”

#### Points of Improvement

- Add “Start beginner review” and “Review from beginning” controls.
- Pair each move notation with plain text such as “Move the queen to e2.”
- Add a “Explain this another way” or “Ask for help” control beside the explanation.
- Show the expected result after trying or inspecting the suggested move.

#### Main Strength

The screen directly connects an important mistake to a better move, practice activity, and the next review step.

#### Main Weakness

Additional help and chess terminology are less accessible than the main guided workflow.

### Alt 2 - Card Review Mode

#### Task Outcomes

C1: Success With Hesitation - I first scan “Game Review” and “Review your key moments.” Six cards are available, so I hesitate about which one should come first, but the selected “Missed Tactic” card and expanded review panel provide a workable starting point.

C2: Independent Success - I scan the red Mistakes and Blunders summary cards and the selected “Missed Tactic - Move 23” card. The important mistake is visible without opening several cards.

C3: Independent Success - I read that the queen on c3 was attacked and that a capture on c3 was missed. This explains the mistake in plain language, even though “Missed Tactic” is domain terminology.

C4: Independent Success - The expanded card explicitly labels “Better move: Qxc3.”

C5: Independent Success - The text states that Qxc3 captures the pawn on c3 and wins material. The explanation is concrete, although the move notation itself is unfamiliar.

C6: Independent Success - I would select “Try this move,” with “Open in Analysis Board” as another inspection path. The controls clearly indicate what to do, though the next state is not shown.

C7: Independent Success - I find the orange “Go to puzzle” button directly in the expanded card.

C8: Independent Success - I can select another card or use “Choose another card” to continue reviewing a different moment.

C9: Success With Hesitation - I identify “Open in Analysis Board” as the additional-help path. I hesitate because the label suggests a more advanced workspace rather than a clearer explanation.

#### Observations

The dashboard is easy to scan through summary metrics, colored categories, and key-moment cards. The selected card expands into an explanation, better move, try action, and puzzle link. There is no visible recommendation for which card a beginner should review first.

#### Feedback

The selected-card pattern provides a strong path from discovery to action. Add a recommended starting card, explain chess terms such as “Blunder” and “Endgame,” and make the Analysis Board’s purpose clearer for someone seeking help.

#### Problems Encountered

- [Information hierarchy; Medium] C1 presents several possible starting cards without identifying a beginner-priority mistake.
- [Terminology; Medium] C2-C5 use “Missed Tactic,” “Blunders,” “Opening,” “Endgame,” and “Qxc3.”
- [Learning support; Medium] C9 offers Analysis Board access but no clearly labeled explanation or beginner-help option.
- [Feedback; Low] C6 does not show the result of trying the suggested move in the visible prototype.

#### Points of Improvement

- Mark one card as “Recommended first.”
- Add plain-language subtitles to chess categories and move notation.
- Rename or explain “Open in Analysis Board” as a way to inspect variations or ask for more detail.
- Show a visible result state after selecting “Try this move.”

#### Main Strength

Each selected card connects a specific mistake to an explanation, better move, try action, and puzzle.

#### Main Weakness

The self-selection dashboard gives a novice too many possible starting points and assumes familiarity with chess vocabulary.

### Alt 3 - Side-by-Side AI Assistant

#### Task Outcomes

C1: Success With Hesitation - I first scan the Assistant tab, the “How can I help you understand this game?” prompt, and the Key Moments list. I hesitate between selecting the red Qd3 moment and asking a question, but the suggested question provides a clear starting route.

C2: Independent Success - I scan the red question icon beside “23. Qd3” and the Game Summary count for mistakes. The problematic move is clearly distinguished from green and orange moments.

C3: Independent Success - I read the assistant’s response that Qd3 loses the pawn on c3 and that after “…Bxc3,” Black wins the pawn and gets a better position. The notation is unfamiliar, but the surrounding explanation is understandable.

C4: Independent Success - I ask or follow the visible question “What’s the better move here?” and find the assistant response “Qe2 is safer!”

C5: Independent Success - The assistant explains that Qe2 protects the pawn on e2 and keeps the queen safe.

C6: Success With Hesitation - There is no visible “Try this move” control. I would use “Show variations” or the Analysis tab to inspect Qe2, but I would hesitate because neither control explicitly says that I can try the move.

C7: Failure - I see “Any similar ideas?” and a general Puzzles link in the sidebar, but no practice activity connected to the current mistake. I cannot confirm that either path will provide the requested related practice.

C8: Independent Success - I would select another entry in the Key Moments list, such as the adjacent Bxc3 moment, to continue reviewing.

C9: Independent Success - I find the “Type your question…” field and suggested follow-up questions. I would use the field when the visible explanation is insufficient.

#### Observations

The assistant places the question, explanation, board highlight, and mini-board feedback together. The Key Moments list provides another way to move through the game. Multiple tabs and entry points are visible, but there is no direct try-move or task-specific practice control.

#### Feedback

The conversational explanation and free-form question field are useful for a novice who needs more detail. Add explicit actions for trying the suggested move and opening a related practice exercise. Make the selected moment and recommended starting point more prominent.

#### Problems Encountered

- [Cognitive load; Medium] C1 requires choosing among Assistant, Analysis, Review, Details, Openings, and Key Moments before the review path is obvious.
- [User control; Medium] C6 lacks a direct “Try this move” action and does not show what happens after inspecting variations.
- [Workflow; High] C7 has no visible practice activity tied to the current mistake.
- [Terminology; Medium] C3-C5 still rely on move notation such as Qd3, Qe2, and …Bxc3.

#### Points of Improvement

- Add a visible “Start with this key moment” action.
- Add “Try Qe2” and “Open on board” controls beside the assistant answer.
- Add “Practice this idea” or “Go to related puzzle” to the assistant response.
- Pair chess notation with plain-language move descriptions.

#### Main Strength

The assistant gives context-aware explanations and supports follow-up questions without forcing a fixed sequence.

#### Main Weakness

The flexible conversation does not provide a complete path from mistake explanation to trying and practicing the better move.

### Chess Preference

- Preferred alternative: Alt 1 - Beginner Review Flow
- Reason: It gives the clearest novice sequence: identify the mistake, understand why, find the better move, try it, practice the idea, and review the next mistake.
- Trade-off: Alt 2 offers better self-selection and a direct puzzle link, while Alt 3 offers the strongest follow-up help. Alt 1 is less flexible when its explanation is insufficient.

## Overall Review

- Most confusing element: FIFA pending information uses “Pending,” “Awaiting update,” and “Awaiting FIFA confirmation” without showing a clear next step.
- Clearest element: Chess Alt 1’s sequence from “Better move: Qe2” to “Try this move,” “Start practice,” and “Next mistake.”
- Most useful concept: Pairing a visible problem or status with one concrete next action.
- Highest-priority improvement: Add explicit per-item next steps and expected timing to FIFA status views, while adding direct “Try this move” and “Go to practice” actions to the Chess assistant.

### AI Reviewer R5 - Full Record

# AI Reviewer R5

## Reviewer Profile

- Methodology: AI-Agent Formative Testing.
- Digital literacy: Medium.
- Domain familiarity: Low familiarity with FIFA and Chess.
- Behavior model: Prefers sequential instructions and clear next actions.
- Assigned prototype order: FIFA Alt 2 -> Alt 1 -> Alt 3; Chess Alt 2 -> Alt 1 -> Alt 3.
- Evidence constraint: Evaluation is based only on the six static low-fidelity prototype images; no post-action state is assumed.

## Scenario 1 - FIFA

### Alt 1 - Status Dashboard

#### Task Outcomes

F1: Independent Success - I would first scan the four status cards and then the event cards. I interpret “Confirmed” and “Tickets are valid” as ready, and “Pending” and “Awaiting FIFA confirmation” as still progressing. The current status is identifiable.

F2: Independent Success - I would look at the “1 Pending” card and the orange Al Hilal vs Real Madrid event. I interpret “0 Action needed” as no user action currently required. The pending information is clear, although the required next action is not.

F3: Success With Hesitation - I would read the status text and select “What does this mean?” for the pending event. I can explain confirmed and pending from the visible copy, but I would hesitate because the detailed explanation is not shown directly.

F4: Failure - I would look at the pending event, “View Order,” and the Quick Actions panel. I would probably select “View Order” as a fallback, but no explicit next expected step or date is displayed for the pending ticket.

F5: Independent Success - I would first look at “Last updated: 2 mins ago” and the refresh icon. I interpret this as a current page-level update signal and would select refresh if needed. The information appears current.

F6: Success With Hesitation - I would inspect the `fifa.com/tickets` address and FIFA branding. These suggest an official source, but there is no visible “Official FIFA source” label or policy signal, so I could not verify it confidently.

F7: Independent Success - I would look at the confirmed event card and select “View Tickets.” The label and placement clearly match the task.

F8: Independent Success - I would scan Quick Actions and select “Transfer Tickets.” The icon and description indicate sending tickets to friends or family.

F9: Independent Success - I would scan Quick Actions and select “Add to Calendar.” The label directly matches the task.

F10: Failure - I would inspect the ticket buttons and Quick Actions for an external-service warning. No visible message explains whether an action leaves FIFA.com, which service opens, or what happens to my data.

#### Observations

The status cards and event cards make the current ticket state the first obvious place to look. The orange pending card is recognizable, but “View Order” and “View Tickets” imply different destinations without explaining the distinction. “Last updated: 2 mins ago” is visible, while official-source and external-handoff information are absent.

#### Feedback

After attempting the tasks, the screen gives direct routes for viewing, transferring, and adding tickets to a calendar. The main unresolved questions are what happens next for a pending ticket and whether outgoing actions remain within FIFA.com.

#### Problems Encountered

- [Workflow; High] F4: The pending event has a status and “Awaiting FIFA confirmation,” but no explicit next expected step or expected update time.
- [Trust; Medium] F6: FIFA branding and the URL suggest legitimacy, but no explicit official-source indicator is visible.
- [Trust; High] F10: There is no warning or explanation before an action might open an external service.
- [Terminology; Medium] F3 and F7: “What does this mean?”, “View Order,” and “View Tickets” require the user to infer different purposes.
- [Feedback; Medium] F5: Freshness is shown globally, but no per-ticket update time or refresh result is visible.

#### Points of Improvement

- Add a “Next expected step” line to each event card, especially the pending card.
- Add an “Official FIFA source” indicator near the page status and a handoff message next to outgoing actions.
- Explain “View Order” versus “View Tickets” with short supporting text.
- Show the last update time for each ticket and a visible confirmation after refresh.

#### Main Strength

The combination of summary status cards, event-level status labels, and direct ticket actions supports quick status checking and common ticket tasks.

#### Main Weakness

The dashboard identifies the current state but does not clearly explain the next step or external-service handoff.

### Alt 2 - Timeline Tracker

#### Task Outcomes

F1: Independent Success - I would first look at the large event timeline. I interpret “ON TRACK,” the numbered stages, and the blue current step “Verification” as the current ticket state. The second event is visibly marked “PENDING.”

F2: Independent Success - I would inspect the orange USA vs Mexico timeline. “Payment received — Pending” and the unfinished later stages identify progressing information. I can find the pending item, although no direct attention action is offered.

F3: Success With Hesitation - I would read the timeline labels and the message “Your order is progressing normally.” I understand completed, current, and upcoming stages, but “Verification” is unfamiliar and its exact meaning is not explained.

F4: Independent Success - I would look at the upcoming timeline stages and “Official Next Steps.” “Ticket ready 72h before match” gives a concrete expected step, and the delivery guide provides a related route.

F5: Independent Success - I would look at “Last updated: 2 mins ago,” the “What changed?” timestamps, and “View update history.” These provide multiple visible freshness signals.

F6: Independent Success - I would first look at the “Official FIFA source” label, then “Official Next Steps” and “Official policies.” The source status is directly communicated.

F7: Failure - I would scan the event card and then select “My Tickets” in the left navigation as a fallback. No visible control says “View Tickets,” and the next screen is not shown, so I cannot count this as a completed task.

F8: Failure - I would scan the timeline card and right-side panels, but no “Transfer Tickets” control is visible. I would not infer that another navigation item provides this action.

F9: Success With Hesitation - I would look at “Freshness & Updates” and select “Sync to calendar” as the closest control. “Sync” may perform the desired action, but it is not the same wording as “Add to Calendar,” so the result is uncertain.

F10: Failure - I would look around the timeline actions and update panels for a handoff warning. No message explains what happens before leaving FIFA.com for another service.

#### Observations

This alternative makes status, progress, freshness, and source legitimacy visible in one sequence. The timeline tells me what has happened and what is expected next. The pending event is identifiable, but the interface focuses on tracking rather than common ticket actions.

#### Feedback

After attempting the tasks, the numbered progression is the clearest route for a novice who wants to understand what happens next. The main blockage is that direct ticket management actions are missing or renamed.

#### Problems Encountered

- [Visibility; High] F7 and F8: “View Tickets” and “Transfer Tickets” are not visible as direct controls.
- [Terminology; Medium] F3 and F9: “Verification” and “Sync to calendar” may not match a novice’s expected language.
- [Workflow; Medium] F2: The pending payment is visible, but there is no clear explanation of whether the user must do anything.
- [Trust; High] F10: No external-service handoff warning is shown.
- [Navigation; Medium] F7: “My Tickets” is an indirect fallback whose destination is not visible.

#### Points of Improvement

- Add “View Tickets” and “Transfer Tickets” buttons to each event card.
- Rename or clarify “Sync to calendar” as “Add to Calendar.”
- Add an “Action needed” explanation beside the pending payment stage.
- Add an external-service warning before any partner-site action.
- Define “Verification” with a short explanation or information icon.

#### Main Strength

The numbered timeline, current-stage marker, update history, and official-source label make the ticket state and next expected milestone easy to follow.

#### Main Weakness

The tracker explains progress well but leaves common ticket actions hidden or unavailable.

### Alt 3 - Action Hub

#### Task Outcomes

F1: Independent Success - I would first look at the Argentina vs Brazil event card. “CONFIRMED” and “Tickets are valid” clearly communicate the displayed ticket status, although only one confirmed event is shown.

F2: Failure - I would scan the event card, Quick Actions, and update panel for pending or attention-needed information. No pending ticket, pending label, or “Action needed” state is visible.

F3: Independent Success - I would read “CONFIRMED” and “Tickets are valid.” The displayed status has a direct explanation.

F4: Failure - I would look below the event status and in Quick Actions for a next event-processing step. “See details” and the action shortcuts do not tell me what will happen next in the ticket lifecycle.

F5: Independent Success - I would look at “Last updated: 2 mins ago” and the refresh icon. The page provides a clear currentness signal.

F6: Independent Success - I would look at “Official FIFA source,” the “Official” badges, and the security panel. These elements directly communicate official status.

F7: Independent Success - I would use either the event-card “View Tickets” button or the Quick Actions tile. Both controls match the task.

F8: Independent Success - I would select the “Transfer Tickets” Quick Actions tile. The icon, label, and description make its function clear.

F9: Independent Success - I would select the “Add to Calendar” Quick Actions tile. The label directly matches the task.

F10: Success With Hesitation - I would first inspect the action cards and then scan the bottom strip. “Before you leave FIFA.com” explains that some options open on official partner sites and says security and data are protected, but the warning is visually separated from the individual actions.

#### Observations

The action cards are the first useful destination for common tasks. Official-source, security, and partner-service language are visible. However, the screen presents only a confirmed event and does not show the progressing or pending situation described in the scenario. There is also no visible ticket-lifecycle sequence.

#### Feedback

After attempting the tasks, this is the fastest alternative for viewing, transferring, and adding tickets to a calendar. It is less useful for understanding pending information or the next stage of ticket processing.

#### Problems Encountered

- [Visibility; High] F2: No pending or attention-needed ticket information is visible.
- [Workflow; High] F4: The screen has actions but no explicit next expected ticket step.
- [Cognitive load; Medium] F1 and F4: Many Quick Actions, Official Options, support links, and repeated Contact Support elements compete with the primary ticket state.
- [Visibility; Medium] F10: The handoff warning is at the bottom rather than adjacent to each outgoing action.
- [Consistency; Medium] F7-F9: Similar actions appear both in the event card and Quick Actions, which may create duplicate paths.

#### Points of Improvement

- Add a status summary or timeline for confirmed, pending, and attention-needed tickets.
- Add a visible “Next expected step” and expected timing to the event card.
- Place the external-service warning beside each relevant action.
- Separate core ticket actions from optional partner offers and remove duplicated support entry points.

#### Main Strength

The clearly labeled action tiles provide direct routes for View Tickets, Transfer Tickets, and Add to Calendar, while the official-source and handoff messages support trust.

#### Main Weakness

The action-first layout does not answer what is happening with pending information or what the next ticket-processing step will be.

### FIFA Preference

- Preferred alternative: Alt 2 - Timeline Tracker.
- Reason: The numbered timeline, current-stage marker, freshness signals, official-source label, and “Ticket ready 72h before match” provide the clearest sequential explanation for a novice.
- Trade-off: It does not provide direct View Tickets or Transfer Tickets controls, and “Sync to calendar” is ambiguous. Alt 3 is better for actions and handoff trust.

## Scenario 2 - Chess

### Alt 1 - Beginner Review Flow

#### Task Outcomes

C1: Success With Hesitation - I would first look at “Beginner Review” and the “STEP 2 OF 3” indicator. I understand this is the review mode, but the screen is already at step 2 and has no explicit “Start review” control, so I would use Previous or the step indicator to find the beginning.

C2: Independent Success - I would look at the red “Mistake 2 of 3” panel and the highlighted board position. “You moved Qd3?” identifies an important mistake.

C3: Independent Success - I would read “Your queen stopped protecting the pawn on d4. Black wins the pawn after ...Nxd4.” The plain-language explanation is sufficient, although the chess notation is unfamiliar.

C4: Independent Success - I would look at the blue “Better move: Qe2” panel. The better move is explicitly identified.

C5: Independent Success - I would read “Keeps the pawn protected and develops safely.” This explains the benefit without requiring detailed chess knowledge, even though “Qe2” itself is unfamiliar notation.

C6: Independent Success - I would select “Try this move.” The control directly matches trying the suggested move.

C7: Independent Success - I would select “Start practice” in the “Practice this idea” panel. The related practice activity is clearly connected to protecting hanging pieces.

C8: Independent Success - I would select “Next mistake.” The control directly communicates continuing to another mistake.

C9: Failure - I would scan the left navigation, settings icon, and review panel for help. “Learn” and “Full Analysis” are visible, but no contextual help or explanation-support route is shown.

#### Observations

The selected Beginner Review mode, step indicator, mistake explanation, better move, practice activity, and Next mistake control create a sequential path. The main uncertainty comes from starting in step 2 rather than at the beginning. Chess notation and the presence of both bottom “Next” and “Next mistake” controls require extra interpretation.

#### Feedback

After attempting the review path, the screen provides a clear route from mistake to explanation, better move, practice, and another mistake. It needs a more explicit entry point and a way to ask for help when the explanation is insufficient.

#### Problems Encountered

- [Navigation; Medium] C1: The review starts at “STEP 2 OF 3,” with no visible Start or Restart Review action.
- [Terminology; Medium] C3-C5: `Qd3`, `Qe2`, `...Nxd4`, and “develops safely” may be unfamiliar to a low-familiarity chess user.
- [Feedback; Medium] C6: “Try this move” does not explain whether it opens a variation, changes the board, or starts an exercise.
- [Consistency; Low] C8: Bottom “Next” and “Next mistake” appear to have different scopes but are not explicitly distinguished.
- [Learning support; High] C9: No contextual help route is visible for an explanation the user still does not understand.

#### Points of Improvement

- Add “Start review” or “Restart from first mistake” and show the current review position.
- Add plain-language definitions or expandable explanations for chess notation and terms.
- Explain the expected result of “Try this move.”
- Rename the bottom control to distinguish “Next move” from “Next mistake.”
- Add a contextual “Explain another way” or “Need help?” control.

#### Main Strength

The screen connects mistake explanation, better move, trying the move, practice, and the next mistake in a guided sequence.

#### Main Weakness

The user can follow the sequence once inside it, but the starting point and additional help route are unclear.

### Alt 2 - Card Review Mode

#### Task Outcomes

C1: Success With Hesitation - I would first look at “Game Review,” the “Review your key moments” heading, and the cards. I would select the “Missed Tactic” or another mistake card and use “Review this card,” but there is no recommended starting card or sequential entry point.

C2: Independent Success - I would look at the “Mistakes 3” and “Blunders 1” summary cards, then the selected “Missed Tactic - Move 23” card. One important mistake is clearly identified.

C3: Independent Success - I would read “Your queen on c3 was attacked. You could have captured the pawn on c3 and gained material.” The reason is stated in direct language.

C4: Independent Success - I would look at the expanded card and read “Better move: Qxc3.” The better move is visible.

C5: Success With Hesitation - I would read “Captures the pawn on c3 and wins material.” I understand the capture, but “material” is an unfamiliar chess term and I would not be fully sure whether it means a piece, advantage, or score.

C6: Independent Success - I would select “Try this move.” The control directly matches the task.

C7: Independent Success - I would select “Go to puzzle.” This is a visible related practice route.

C8: Independent Success - I would select “Choose another card” or choose another key-moment card. The card layout makes continuation visible.

C9: Success With Hesitation - I would select “Open in Analysis Board” for more detail. It is the closest visible route to additional help, but the label does not say whether it will provide a clearer explanation.

#### Observations

The dashboard makes mistakes, blunders, key moments, and practice links visible at once. The selected-card border and checkmark show which card is expanded, but the many cards, filters, performance categories, and chess terms create a self-selection burden for a novice.

#### Feedback

After attempting the tasks, the strongest path is the selected card’s sequence from mistake to better move to puzzle. The user still has to decide where to begin and what several category labels mean.

#### Problems Encountered

- [Cognitive load; Medium] C1: Several summary metrics and six cards provide no clear first choice.
- [Terminology; Medium] C2-C5: “Missed Tactic,” “Blunder,” “Opening,” “Endgame,” and “material” are not explained.
- [Visibility; Medium] C1: The dashboard does not visibly recommend a first card.
- [Feedback; Medium] C6: “Try this move” does not show the resulting interaction or board state.
- [Learning support; Medium] C9: “Open in Analysis Board” may provide depth, but it is not presented as help or explanation support.

#### Points of Improvement

- Mark one card “Start here” and provide an optional guided order.
- Add plain-language descriptions for mistake categories and “material.”
- Make the selected-card state explicit instead of relying mainly on a checkmark and border.
- Describe what happens after “Try this move.”
- Add a dedicated “Need more explanation?” action alongside the expanded card.

#### Main Strength

The card detail connects the important mistake, better move, try action, and puzzle activity in one visible review unit.

#### Main Weakness

The self-selection dashboard makes the novice decide what to review and decode several unfamiliar chess categories before starting.

### Alt 3 - Side-by-Side AI Assistant

#### Task Outcomes

C1: Success With Hesitation - I would first look at the “Game Review” heading, the active Assistant tab, and the message “How can I help you understand this game?” I could start by asking a question, but there is no explicit review starting point or guided first step.

C2: Independent Success - I would look at the Key Moments list and the red `23. Qd3` entry, then the red board highlight. The important mistake is clearly located.

C3: Independent Success - I would read the assistant’s explanation that Qd3 loses the pawn on c3 and that after `...Bxc3`, Black wins the pawn and gets a better position.

C4: Independent Success - I would read the assistant response to “What’s the better move here?” The suggested move `Qe2` is clearly displayed.

C5: Success With Hesitation - I would read “Qe2 is safer! It protects the pawn on e2 and keeps your queen safe.” I understand the safety claim, but I cannot reconcile the earlier reference to losing the pawn on c3 with the later reference to protecting the pawn on e2.

C6: Success With Hesitation - I would select “Show variations” or inspect the mini-board. These are the closest visible options, but there is no explicit “Try this move” control and no clear indication that the variation applies `Qe2`.

C7: Failure - I would look for a practice button, puzzle link, or related exercise. “Any similar ideas?” and the general Puzzles navigation are visible, but no activity is explicitly connected to this mistake.

C8: Independent Success - I would select another item in the Key Moments list, such as `24. ...Bxc3`. The list provides a clear way to continue to another key moment.

C9: Independent Success - I would use a suggested follow-up such as “Show variations” or type a question into “Type your question...” The interface directly supports further explanation requests.

#### Observations

The assistant, board highlights, mini-board feedback, and Key Moments list connect questions to visual explanations. The interaction is flexible, but the page has several tabs, a board, a chat stream, key moments, and summary metrics without a prescribed starting sequence. The square references in the two explanations are difficult to reconcile.

#### Feedback

After attempting the tasks, the assistant provides the strongest route for asking why and requesting more explanation. It does not provide a direct try-move or practice path, and the visible coordinate mismatch reduces confidence in the explanation.

#### Problems Encountered

- [Workflow; High] C1: There is no explicit first review step or recommended starting action.
- [Consistency; High] C5: The explanation moves from the pawn on c3 to protecting the pawn on e2 without clarifying the relationship.
- [Visibility; High] C6: No direct “Try this move” action is visible.
- [Visibility; High] C7: No contextual practice activity or puzzle link is visible.
- [Trust; Medium] C3-C5: The assistant gives concise conclusions, but no visible analysis basis or verification path is shown.
- [Cognitive load; Medium] C1 and C8: Multiple tabs and panels compete with the conversational review path.

#### Points of Improvement

- Add a guided “Start review” prompt and a visible “Next mistake” control.
- Reconcile the c3 and e2 references, or explain whether they are separate tactical reasons.
- Add “Try this move” with a clear board state and result.
- Add “Practice this idea” or a linked puzzle for the current mistake.
- Add a visible variation or analysis basis that lets the user verify the assistant’s explanation.
- Reduce or group the number of tabs and secondary panels for the beginner path.

#### Main Strength

The assistant answers why-questions in plain language and connects responses to highlighted board positions and follow-up prompts.

#### Main Weakness

The free-form interface lacks a guided review and practice workflow, and the visible square mismatch undermines comprehension.

### Chess Preference

- Preferred alternative: Alt 1 - Beginner Review Flow.
- Reason: Its step indicator, single highlighted mistake, plain-language explanation, Better Move, Try this move, Practice this idea, and Next mistake support a sequential novice workflow.
- Trade-off: It lacks the flexible follow-up help available in Alt 3 and the direct puzzle route available in Alt 2.

## Overall Review

- Most confusing element: In Chess Alt 3, the explanation shifts from losing the pawn on c3 to protecting the pawn on e2 without clarifying the connection.
- Clearest element: FIFA Alt 2’s numbered timeline with a highlighted current stage and “Ticket ready 72h before match.”
- Most useful concept: A direct chain from explanation to next action, such as Better Move -> Try this move -> Practice this idea.
- Highest-priority improvement: Provide a consistent, explicit first/next action and visible outcome for each workflow, including FIFA pending-ticket next steps and Chess try/practice actions.

## Traceability Summary

- FIFA status and action balance: R1, R3, R4, R5 observations for Alt 1; R2's Alt 1 comparison.
- FIFA progress and provenance: R1-R5 observations for Alt 2, especially F4-F6.
- FIFA action and handoff: R1-R5 observations for Alt 3, especially F7-F10.
- Chess guided learning: R1-R5 observations for Alt 1, especially C2-C9.
- Chess choice load and practice bridge: R1-R5 observations for Alt 2.
- Chess follow-up flexibility and missing practice: R1-R5 observations for Alt 3.
- Every High issue in the prioritized tables names the affected reviewers and task evidence.
- Every selected revision is tied to a documented problem in a reviewer record.

