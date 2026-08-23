# Requirement 2 Testing Plan

**Methodology:** AI-Agent Formative Testing  
**Scope:** Two scenarios, six paper-prototype alternatives, five independent AI reviewers, and 19 task outcomes per reviewer.  
**Working files:** `formative-testing-results.md`, `ai-testing/R1.md` through `ai-testing/R5.md`, slides 19-42, and `presentation-script.md`.

## Purpose and assignment alignment

Requirement 2 asks the team to define a comprehensive formative-testing plan, apply it to the paper prototypes, record observations and feedback, identify points of improvement, and select a promising low-fidelity direction for PA4. This plan turns those requirements into one repeatable task protocol for both scenarios.

The method is explicitly labelled **AI-Agent Formative Testing**. Five independent AI reviewer agents were configured as novice users. Each reviewer received the same scenario prompts, task wording, prototype images, moderator rules, and success criteria. Reviewer profiles and prototype orders varied to expose different scan paths, confidence levels, and learning preferences. All reviewer records are stored separately and are linked from the consolidated results.

## Objectives and signals

| ID | Objective | Signal captured |
|---|---|---|
| O1 | Learnability | First action and ability to find the entry point without instruction |
| O2 | Task completion | Independent success, hesitation, failure, stopping point, and intervention |
| O3 | Comprehension | Explanation of ticket state or chess mistake in the reviewer’s own words |
| O4 | Next-step clarity | Whether the reviewer identifies the intended next action or practice step |
| O5 | Trust and confidence | Freshness, official source, partner boundary, return path, and confidence language |
| O6 | Cognitive load | Repeated scans, uncertainty, terminology friction, and choice overload |
| O7 | Learning continuity | Ability to connect an explanation or move to a useful practice action |
| O8 | Alternative differentiation | Whether each interaction model creates an understandable trade-off |
| O9 | Recovery | Ability to return to the useful path after exploring or misunderstanding a state |
| O10 | Revision priority | Which issue is important enough to change before PA4 |

## Reviewer profiles and independence

Every reviewer is labelled `AI Reviewer 1` through `AI Reviewer 5` (short IDs `R1`-`R5`). No reviewer receives another reviewer’s output. Each session begins from the same written protocol and the same six prototype images.

| Reviewer | Novice profile | FIFA order | Chess order |
|---|---|---|---|
| R1 | Higher digital literacy; low FIFA familiarity; no Chess analysis familiarity | Alt 1 → Alt 2 → Alt 3 | Alt 1 → Alt 2 → Alt 3 |
| R2 | Careful reader; low FIFA and Chess.com familiarity | Alt 2 → Alt 3 → Alt 1 | Alt 2 → Alt 3 → Alt 1 |
| R3 | Lower digital confidence; action-oriented; low domain familiarity | Alt 3 → Alt 1 → Alt 2 | Alt 3 → Alt 1 → Alt 2 |
| R4 | Fast-scanning novice; low patience for long text | Alt 1 → Alt 3 → Alt 2 | Alt 1 → Alt 3 → Alt 2 |
| R5 | Guided-workflow preference; moderate digital literacy | Alt 2 → Alt 1 → Alt 3 | Alt 2 → Alt 1 → Alt 3 |

The order rotation reduces learning-effect bias. Every alternative is reset to the same paper state before the next task sequence. The reviewer is not told which alternative the team expects to carry into PA4.

## Method and moderator protocol

The method combines task-based formative evaluation, think-aloud observation, structured issue capture, and a short comparative reflection. Each reviewer is evaluated against behavior rather than visual polish.

The moderator uses this neutral instruction:

> “Please think aloud as you work. Tell us what you expect, what you are looking for, and what you believe each state means. We will show the next paper state only after an action or an explicit request for help. I will not point to the intended control or explain the workflow while you are working.”

Moderator rules:

- Use the same scenario wording, task IDs, order, reset, and probe wording for every reviewer.
- Do not point to a control, praise a choice, teach a later alternative, or reveal a preferred design.
- Use neutral probes such as “What would you try next?” and “What makes you think that?”
- Intervene only after an explicit help request, a dead end, or the same unproductive path twice; record the intervention.
- Keep observed behavior, reviewer feedback, and team interpretation in separate fields.
- Ask for clarity and confidence ratings after each alternative; treat preference as a supporting signal rather than a standalone decision rule.

Suggested session sequence: introduction and profile check (3 minutes), think-aloud practice (2), FIFA alternatives (12-15), Chess alternatives (12-15), comparative reflection (5-8), and close (1-2). The exact duration is a planning guide; behavior and issue traceability matter more than speed.

## Scenario 1 — FIFA ticket confidence before travel

### Scenario prompt

“You have tickets connected to two football events. One event is confirmed and one is pending. Understand whether everything is okay, what happens next, and how to perform a common ticket action before travelling.”

### Tasks

| ID | Task | Success signal |
|---|---|---|
| F1 | Find the confirmed event | Correctly identifies the confirmed event or order |
| F2 | Find the pending event | Correctly identifies what still requires attention |
| F3 | Explain the current state | Explains the state in own words |
| F4 | Find what happens next | Identifies the next step and who owns it |
| F5 | Judge freshness and source | Locates current-information and official-source cues |
| F6 | Find a common action | Finds Transfer Tickets or Add to Calendar |
| F7 | Explain the handoff | Explains the official external partner and return path |
| F8 | Check ticket freshness | Finds last-updated or current-information evidence |
| F9 | Choose the safest next action | Selects an action that matches the state and explains why |
| F10 | Recover from an unresolved state | Returns to the useful status path and identifies remaining support or resolution |

### Functionalities under test

- **Alt 1 — Status Dashboard:** status cards, confirmed/pending distinction, event list, primary next action, quick actions, support, and current-state summary.
- **Alt 2 — Timeline Tracker:** completed/current/upcoming stages, current marker, freshness cue, official-source indicator, update history, ownership, and next-step guide.
- **Alt 3 — Action Hub:** task discovery, shortcut recognition, official options, partner handoff, security/support, return path, and action grouping.

Core comparison: Alt 1 answers “What is true now?”, Alt 2 answers “Where am I in the process?”, and Alt 3 answers “What can I do right now?”

## Scenario 2 — Chess mistake to practice

### Scenario prompt

“You have finished a chess game. You know that you made mistakes, but you are not familiar with analysis tools. Understand one important mistake, learn a better move, and decide what to practice next.”

### Tasks

| ID | Task | Success signal |
|---|---|---|
| C1 | Find where to begin | Starts review without analysis-tool instruction |
| C2 | Identify one mistake | Selects an important moment or explanation |
| C3 | Explain why | Describes why the move was a mistake in own words |
| C4 | Find the better move | Locates and interprets the suggested move |
| C5 | Try or inspect it | Uses the board or control to explore the better move |
| C6 | Reach practice | Finds a relevant lesson, puzzle, or practice activity |
| C7 | Review another moment | Finds another explanation or returns to the review path |
| C8 | Connect explanation to practice | States how the better move becomes a useful practice activity |
| C9 | Return to a useful next step | Identifies what to do next after exploring |

### Functionalities under test

- **Alt 1 — Beginner Review Flow:** guided sequence, progress indicator, plain-language explanation, better move, practice bridge, and optional depth.
- **Alt 2 — Card Review Mode:** visual scan, self-selected moments, mini-board previews, expanded explanation, review/try/puzzle actions, and practice bridge.
- **Alt 3 — Side-by-Side AI Assistant:** question entry, assistant explanation, board highlights, context awareness, follow-up prompts, flexible exploration, and practice action.

Core comparison: Alt 1 uses system-selected order, Alt 2 uses user-selected content, and Alt 3 uses a user-selected question.

## Success criteria

Each task is coded as one of three outcomes:

- **Independent success:** the reviewer completes or explains the task without help.
- **Hesitation:** the reviewer completes after rereading, a neutral probe, a visible recovery, or a short uncertainty sequence.
- **Failure:** the reviewer cannot complete, forms a critical wrong mental model, or stops at the relevant state.

Decision thresholds:

| Measure | Strong | Acceptable | Needs improvement | Critical |
|---|---|---|---|---|
| Independent completion | ≥80% of reviewers | 60-79% | 40-59% | <40% or a repeated blocker |
| Correct comprehension | ≥80% explain in own words | 60-79% | 40-59% | Same critical wrong model in 2+ reviewers |
| Next-step clarity | ≥80% identify the intended action | 60-79% | 40-59% | Ownership or destination remains ambiguous |
| Intervention burden | 0-1 reviewer needs intervention | 2 reviewers | 3 reviewers | 4-5 reviewers or same-step rescue |
| Clarity rating | Median 4-5/5 | Median 3/5 | Median 2/5 | Median 1/5 or repeated low confidence |
| Critical issue recurrence | 0 repeated critical issues | One isolated critical issue | One repeated high-impact issue | Two or more repeated critical issues |

The results use the task outcome counts, recurring observations, reviewer feedback, issue severity, and revision effort together. A preference count alone cannot select a direction.

## Data-collection schema

One auditable row represents `reviewer × scenario × alternative × task`. Capture:

1. Reviewer ID, profile, scenario, alternative, and order position.
2. Task ID and exact task wording.
3. Outcome: independent success, hesitation, or failure; stopping point and intervention.
4. First action, expectation, scan path, wrong path, and recovery.
5. Comprehension statement in the reviewer’s own words.
6. Feedback: clear, confusing, missing, unnecessary, or preferred and why.
7. Clarity and confidence rating where relevant.
8. Issue category, severity, affected alternative, evidence trace, and proposed improvement.
9. Comparative reaction and recommendation for the next prototype iteration.

Issue categories: entry/learnability, comprehension, hierarchy, terminology, navigation, ownership, trust/provenance, action visibility, practice continuity, control/flexibility, and recovery. Severity is Critical when the core task or trust boundary breaks; High when a repeated blocker or wrong mental model appears; Medium when the task is possible but inefficient or unclear; Low when the issue is polish or optional detail.

## Synthesis and PA4 selection

First, calculate task outcomes for each alternative. Next, group recurring observations and feedback into issue themes. Then rank issues by severity, recurrence, affected task, trust or learning impact, and revision effort. Finally, compare alternatives using learnability, completion, comprehension, next-step clarity, trust or practice continuity, error risk, flexibility, and preference.

The selected direction should retain a clear core task, avoid repeated high-severity blockers, and have a feasible revision path. The current AI-Agent Formative Testing synthesis selects **FIFA Alt 1 — Status Dashboard** and **Chess Alt 1 — Beginner Review Flow** for PA4 refinement, while borrowing the strongest timeline, action-grouping, card-priority, prompt, and handoff cues from the other alternatives.

## Limitations and responsible interpretation

AI reviewers model novice interpretation through the supplied images and written protocol. They are useful for exposing likely hierarchy, terminology, workflow, comprehension, trust, and learning-continuity issues, but they do not reproduce physical paper manipulation, motor behavior, accessibility needs, emotional response, or every variability of a live moderated session. Therefore, the evidence is presented with the AI-agent methodology attached to every result and is used to guide revisions and validation checks rather than to make unsupported population claims.

## Deliverable traceability

- Reviewer records: `ai-testing/R1.md`, `ai-testing/R2.md`, `ai-testing/R3.md`, `ai-testing/R4.md`, `ai-testing/R5.md`.
- Consolidated analysis: `formative-testing-results.md`.
- Presentation evidence: slides 19-42 in `Group10-PA3-PaperPrototypes.pptx`.
- Talk track: `presentation-script.md`.
- Native authoring source: `slides-src/export_native.mjs`.
