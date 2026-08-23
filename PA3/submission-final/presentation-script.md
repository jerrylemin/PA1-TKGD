# PA3 Presentation Script

## Delivery plan

Use this as the classroom talk track for the 42-slide deck. Aim for 8–9 minutes at approximately 125 spoken words per minute. Slides 1–18 establish the Requirement 1 design space; slides 19–42 present the completed AI-Agent Formative Testing plan and results. Bracketed cues are delivery notes, not slide copy.

## Slides 1–18 — Requirement 1 context · about 1 minute

### Slides 1–5 — Two jobs, two scenarios

“This presentation covers two paper-prototype scenarios: FIFA ticket confidence and Chess mistake-to-practice learning. FIFA asks: is my ticket okay, what happens next, and what can I safely do before travel? Chess asks: what mistake did I make, what is a better move, and what should I practise next?”

### Slides 6–10 — FIFA alternatives

“We explored three different mental models, not three visual skins. The Status Dashboard foregrounds what is true now. The Timeline Tracker foregrounds process and ownership. The Action Hub foregrounds what I can do right now. Requirement 2 tests the same ticket-confidence tasks across all three.”

### Slides 11–18 — Chess alternatives

“The Chess alternatives use three control models: a guided beginner flow, user-selected review cards, and a side-by-side AI assistant. The design question is how much control a beginner should have before understanding the learning path. We evaluate entry, mistake comprehension, practice continuity, and recovery.”

## Slides 19–30 — Requirement 2 plan · about 3 minutes

### Slide 19 — AI-Agent Formative Testing

“Requirement 2 has a plan and completed results. Five independent AI reviewer agents were configured as novice users. Each received the same written protocol, prompts, prototype images, and task wording. There are six alternatives and 19 tasks per reviewer: 285 coded outcomes in total.”

**Pointer cues:** [methodology banner] [two-part structure] [19-task count]

### Slides 20–24 — Objectives, reviewers, method, criteria

“The objectives cover learnability, completion, comprehension, next-step clarity, trust, cognitive load, alternative differentiation, improvement, and revision priority. R1–R5 vary in scan speed, digital confidence, domain familiarity, and guidance preference, but no reviewer receives another reviewer’s output.

The method combines task-based evaluation, think-aloud reasoning, structured observation, neutral probes, ratings, and a comparison reflection. We reset the paper context between alternatives and do not point to controls or reveal the expected direction. Each outcome is Independent Success, Success With Hesitation, or Failure. Repeated critical misunderstanding escalates an issue even when a reviewer eventually finishes.”

### Slides 25–30 — Tasks, data, bias control

“FIFA moves from confirmed and pending status to meaning, next step, freshness, official source, handoff, ticket actions, safe action, and recovery. Chess moves from review entry to mistake, explanation, better move, trial, practice, help, another moment, and next step.

The evidence row is reviewer × scenario × alternative × task. We keep outcome, first action, hesitation, wrong path, feedback, interpretation, issue severity, and revision separate. Five rotated orders record the learning effect instead of hiding it.”

## Slides 31–42 — Results, selection, improvement · about 4 minutes

### Slides 31–35 — Independent reviewer records

“R1’s status-first FIFA scan was clear but needed Pending resolution and handoff cues; the guided Chess flow was easiest to trust. R2 valued FIFA timeline freshness and ownership and still preferred a guided Chess path. R3 was action-oriented and more sensitive to choice load. R4 scanned headings and actions first, making FIFA safety copy easy to miss. R5 preferred guided workflow and reinforced the Chess practice bridge. These are independent AI-review records, not human participant sessions.”

### Slide 36 — FIFA synthesis

“Across 50 FIFA outcomes per alternative, Alt 1 has 31 independent successes, Alt 2 has 26, and Alt 3 has 37. Alt 3 is fastest for action discovery, but its context and handoff risks remain. Three reviewers preferred Alt 1, two preferred Alt 2, and none preferred Alt 3. We select Alt 1 because its stable status-first entry has a bounded revision path, then borrow timeline ownership and action-grouping cues.”

### Slide 37 — Chess synthesis

“Across 45 Chess outcomes per alternative, Alt 1 has 36 independent successes, Alt 2 has 34, and Alt 3 has 26. All five reviewers preferred Alt 1. Its guided mistake-to-practice continuity is the strongest base; cards contribute a Start here cue, and the assistant contributes bounded prompts and follow-up help.”

### Slides 38–39 — Issues and improvements

“For FIFA, the priority is to give Pending a reason, owner, expected timing, and explicit action requirement; show the official source beside freshness; clarify View Order versus View Tickets; and preview the partner boundary before Continue. For Chess, the priority is visible Start Beginner Review, clear step versus game-move labels, plain-language movement, visible feedback after Try this move, persistent Practice this idea, help, and recovery.”

### Slide 40 — Decision matrix · Select the strongest PA4 direction

“The matrix combines task outcomes, recurring issues, preference signals, and revision effort. FIFA Alt 1 and Chess Alt 1 are the selected bases. The choice is not preference alone: it preserves the clearest core task while addressing the highest-impact issues with focused revisions.”

**Pointer cues:** [independent counts] [preference row] [implementation implication]

### Slide 41 — Keep / Improve / Simplify / Validate

“For FIFA, keep the compact status summary, improve Pending and handoff, simplify competing actions, and validate the hybrid direction in PA4. For Chess, keep the guided sequence, improve plain-language explanation and practice continuity, simplify first-choice load, and validate recovery and confidence bounds.”

### Slide 42 — Requirement 2 conclusion

“The plan is complete, five independent AI reviewer sessions are complete, all six alternatives were evaluated, 285 outcomes were synthesized, and revisions were defined. The selected PA4 directions are FIFA Alt 1 Status Dashboard and Chess Alt 1 Beginner Review Flow. The AI-agent methodology stays attached to the evidence so the scope of the findings is clear.”

## Closing sentence

“Requirement 2 turns six paper alternatives into a traceable PA4 decision: preserve the clearest novice path, carry the strongest cues from the other models, and validate the prioritized risks next.”
