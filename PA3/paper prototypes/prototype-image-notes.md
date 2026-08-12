# PA3 prototype image notes

This is the standalone reference explanation for the six approved prototype images. The filenames below are the six primary sections required for the PA3 presentation. The images are treated as approved artifacts: this document describes them but does not redraw or alter them.

## alt1scenario1.png

**Scenario:** Scenario 1 — FIFA.com, plan and manage tickets with confidence.  
**Alternative:** Alt 1 — Status Dashboard.  
**One-sentence concept:** A status-first dashboard gives a user one account-level view of current ticket states, upcoming events, quick actions, and support.  
**Source UI patterns:** FIFA desktop global navigation and ticket-entry card pattern from `fifa-20-tickets-hospitality-landing.png`; account-style “My Tickets” and overview framing are the prototype’s proposed interaction structure.  
**Problem being addressed:** A user may know which tournament they want but still lack a consolidated answer to whether their tickets are valid, pending, cancelled, or waiting on them.  
**Design motivation:** PA2 identifies a lack of consolidated ticket decision confidence and the need for stronger outbound-route trust. The prototype applies “state before action”: explain the current state first, then show the appropriate primary action.  
**Interaction model:** Status-first, confidence-first. The system summarizes state, then the user opens an event card or a task.  

**Detailed walkthrough from top-left to bottom-right:**

1. The browser chrome and FIFA global navigation establish the proposed desktop context and retain recognizable FIFA top-level destinations.
2. The left rail makes Overview, My Tickets, Orders, Preferences, and Help & Support persistent. The selected Overview state signals that this is a home surface rather than a single event detail page.
3. The greeting and “Here’s the status of your FIFA events” line frame the page around confidence. A last-updated line adds a freshness cue.
4. The four summary cards show Confirmed, Pending, Action needed, and Cancelled. Each state has a count, a short explanation, and a distinct visual treatment.
5. The upcoming-event region gives each event a tournament image, opponent, date, venue, ticket quantity, seating details, state label, and primary action such as View Tickets or View Order.
6. The right column holds Quick Actions, Need Help?, and support / notification entry points. These are secondary to the state summary but remain visible.
7. The bottom strip prompts the user to enable notifications, extending the status model over time.
8. The annotations at the right and the problems-solved / traceability notes at the bottom explain why the regions exist; they are part of the approved artifact and not additional interface claims.

**Meaning of each major UI region:**

- **Overview rail:** Persistent orientation and recovery path.
- **State summary:** Recognition of the current ticket portfolio before a user chooses a task.
- **Upcoming event cards:** Event-specific detail and direct action after the overview read.
- **Quick Actions:** Common tasks that should not require hunting through event pages.
- **Need Help / notifications:** Support and freshness mechanisms for uncertainty.
- **Annotations / legend:** Design rationale, traceability, and color meaning for the paper test artifact.

**Primary user path:** Open Overview → read the state summary → select a pending or confirmed event → choose View Order or View Tickets → use support or notifications if the state remains unclear.  
**Alternative paths:** Open My Tickets directly; choose Transfer Tickets, Add to Calendar, or Share Itinerary; open Help & Support; enable notifications.

**Difference from original website:** The PA2 FIFA capture is a tournament-first Tickets & Hospitality landing page with tournament cards and ticket / hospitality entry actions. It does not show a consolidated cross-tournament status dashboard in the captured state. This prototype proposes that persistent status layer while retaining FIFA-style global navigation and official framing.  
**Difference from the other two alternatives in the same scenario:** Alt 1 optimizes state recognition. Alt 2 optimizes process visibility through a timeline. Alt 3 optimizes task execution through an action hub. Alt 1 is therefore the least process-diagnostic of the three, but the fastest for the question “are my tickets okay?”

**Strengths:** Fast scanning; direct status recognition; clear distinction between confirmed and pending; support and notifications are easy to find; useful for multi-event triage.  
**Weaknesses:** Pending may still be ambiguous without ownership or expected resolution; “View Order” versus “View Tickets” may require explanation; state counts can reassure without diagnosing the cause.  
**Usability dimensions affected:** Learnability, recognition rather than recall, visibility of system status, error prevention through clear state/action pairing, perceived control, and confidence calibration.  
**Formative-testing questions:** Can a participant explain what Confirmed and Pending mean in their own words? Which action do they take first for the pending event? Do they understand whether the next step belongs to them or FIFA? Can they find help or turn on updates?  
**What evidence would support or reject the design hypothesis:** Support would be consistent state interpretation and appropriate next-action selection without facilitator intervention. Rejection would be repeated confusion about pending ownership, wrong selection between View Order and View Tickets, or reliance on labels without an explanation of what to do next.

**Suggested 60–90 second explanation:**

“This is our FIFA Status Dashboard. The key decision is to show state before action. Instead of asking the user to open several tournament pages, the page begins with four states: confirmed, pending, action needed, and cancelled. The event cards then add the context and the primary action. Quick actions and support stay visible, so the user can move from confidence to action without searching. The main benefit is quick recognition. The main risk is that pending still may not explain ownership or expected resolution. In formative testing we would ask participants to explain one confirmed and one pending event, then measure the first action and any wrong paths. This is a hypothesis, not a result.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — approved primary ticket-entry evidence, figure `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-02-global-navigation-desktop.png` — supporting global-navigation context when needed.

## alt2scenario1.png

**Scenario:** Scenario 1 — FIFA.com, plan and manage tickets with confidence.  
**Alternative:** Alt 2 — Timeline Tracker.  
**One-sentence concept:** A progress-first ticket surface shows the lifecycle, the current milestone, freshness signals, and official next steps.  
**Source UI patterns:** FIFA Tickets & Hospitality card entry from `fifa-20-tickets-hospitality-landing.png`; global navigation and official-source framing are retained as comparison anchors.  
**Problem being addressed:** A state label does not necessarily tell a user where the order is in its process, whether an update is current, or what will happen next.  
**Design motivation:** The prototype makes progress and freshness visible so that waiting can be interpreted as normal system work rather than failure or an unexplained delay.  
**Interaction model:** Progress-first, freshness-first. The user reads the lifecycle left to right, then uses update history or official next-step guidance.  

**Detailed walkthrough from top-left to bottom-right:**

1. The browser and FIFA global navigation frame the proposed page inside a familiar FIFA desktop shell.
2. The left rail highlights Timeline, separating process tracking from the general Overview and My Tickets areas.
3. The greeting establishes the goal: track every ticket step with confidence. Last updated and Official FIFA source sit at the top of the content region.
4. The primary event card includes competition image, match, date, venue, ticket quantity, state, and order identifier.
5. The horizontal timeline marks Order placed, Payment received, Verification, Ticket ready, and Event day. Completed milestones are green, the current step is blue, and future steps are neutral.
6. A status sentence translates the timeline into plain language, and actions expose the full timeline or update history.
7. A second event card shows a pending order using the same lifecycle structure, so users can compare what is complete and what is waiting.
8. The bottom update history lists recent changes, while the right column separates Freshness & Updates, Official Next Steps, and Need Help?

**Meaning of each major UI region:**

- **Timeline rail:** Makes process position visible rather than inferring it from a single status label.
- **Current milestone:** Identifies the step that matters now.
- **Freshness & Updates:** Makes recency and change history inspectable.
- **Official Next Steps:** Groups guidance about delivery, entry, and hospitality options.
- **Help area:** Offers recovery without making the user search the wider FIFA site.

**Primary user path:** Open Timeline → identify the current milestone → read the normal next step → inspect update history if needed → follow the official guide.  
**Alternative paths:** Enable notifications; sync to calendar; open the full timeline; open update details; contact support; review the second event’s pending state.

**Difference from original website:** The captured FIFA ticket page exposes tournament-based entry cards, not a persistent lifecycle for an order. This prototype adds a process model and freshness layer; it does not claim the captured screenshot already contains this dashboard.  
**Difference from the other two alternatives in the same scenario:** Alt 1 answers “what is my status now?” with counts and event cards. Alt 2 answers “where am I in the process?” with milestones and history. Alt 3 answers “what can I do now?” with a task hub.

**Strengths:** Strong visibility of progress; makes normal waiting legible; exposes freshness and official source; supports troubleshooting and escalation.  
**Weaknesses:** More visual density than Alt 1; future steps may look like user obligations; users may need explicit ownership, normal duration, and exception handling.  
**Usability dimensions affected:** Visibility of system status, feedback, recognition, trust calibration, perceived control, and cognitive load during waiting.  
**Formative-testing questions:** Can participants identify the current milestone? Can they distinguish system-owned from user-owned steps? Do they understand what “last updated” means? Do they know what happens next without treating every gray milestone as a task?  
**What evidence would support or reject the design hypothesis:** Support would be accurate current-step and next-step explanations with low wrong-path behavior. Rejection would be repeated interpretation of future milestones as required user actions, or failure to use freshness and official-source cues.

**Suggested 60–90 second explanation:**

“Alt 2 is our Timeline Tracker. It is not just a more detailed status label. The central model is progress: order placed, payment received, verification, ticket ready, and event day. The current step is highlighted, and the page also shows when the information was updated and where official next steps live. This should help a user interpret normal waiting and understand what happens next. The main risk is ownership. A future milestone might look like a task the user has to complete. We would test whether participants can point to the current step, explain the next step, and distinguish system work from their own work.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — approved primary ticket-entry evidence, `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-02-global-navigation-desktop.png` — supporting global-navigation context.

## alt3scenario1.png

**Scenario:** Scenario 1 — FIFA.com, plan and manage tickets with confidence.  
**Alternative:** Alt 3 — Action Hub.  
**One-sentence concept:** A tasks-first hub puts common ticket actions, official options, support, and partner-handoff trust in one place.  
**Source UI patterns:** FIFA global navigation and ticket / hospitality entry from `fifa-20-tickets-hospitality-landing.png`; partner-boundary evidence from `fifa-32-before-partner-handoff.png` and `fifa-33-partner-after-public-redirect.png`.  
**Problem being addressed:** A user who already owns or is managing a ticket may need to do something quickly, but the original entry experience is organized around event discovery rather than routine actions.  
**Design motivation:** Reduce friction for high-frequency tasks and make external-service boundaries explicit before the user leaves FIFA.com.  
**Interaction model:** Tasks-first, shortcuts-first. The user selects an action card rather than interpreting a status or timeline first.  

**Detailed walkthrough from top-left to bottom-right:**

1. The FIFA global shell and left rail provide orientation; the selected Action Hub marks the page’s role.
2. The top event strip grounds actions in a confirmed ticket and keeps a state summary visible without making it the dominant interaction.
3. The Quick Actions grid offers View Tickets, Transfer Tickets, Resell Official, Add to Calendar, Share Itinerary, Venue Guide, Fan Guide, and Contact Support.
4. The Official Options row collects hospitality, travel packages, and an official resale marketplace. Each card has an official label or provider cue.
5. The right column groups Need Help?, Ticketing Updates, and Your Security Matters so support and risk information are not hidden.
6. The bottom handoff banner explains that some options open official partner services and that the user’s data and security are protected.
7. Annotation cards on the right explain task-first shortcuts, official options, and handoff trust. The bottom strip records problems solved and traceability.

**Meaning of each major UI region:**

- **Event strip:** Establishes which ticket context the actions apply to.
- **Quick Actions:** Shortcuts for routine post-purchase work.
- **Official Options:** Optional or extended services separated from core management tasks.
- **Need Help / Security:** Support, policy, and trust entry points.
- **Handoff banner:** Feedforward before leaving FIFA.com.

**Primary user path:** Open Action Hub → choose View, Transfer, Resell, Calendar, or itinerary action → inspect destination / provider cue → continue or stay.  
**Alternative paths:** Open venue or fan guidance; contact support; enable ticketing updates; browse official options; return to My Tickets.

**Difference from original website:** The original capture is a tournament-first landing page and the PA2 handoff captures show a public-to-partner boundary. This prototype proposes a task-oriented layer and makes that boundary visible before outbound navigation.  
**Difference from the other two alternatives in the same scenario:** Alt 1 prioritizes state recognition; Alt 2 prioritizes process understanding; Alt 3 prioritizes execution of common actions and trust at the boundary.

**Strengths:** Recognition over recall; strong routine-action discoverability; clear grouping of optional options; explicit support and handoff context.  
**Weaknesses:** Many equal-weight actions can create choice overload; optional packages may compete with core ticket tasks; “official” labels need careful provenance and policy detail.  
**Usability dimensions affected:** Efficiency, recognition, user control, error prevention before external navigation, trust calibration, and decision load.  
**Formative-testing questions:** Can a user find Transfer Tickets without opening unrelated areas? Can they distinguish core ticket management from optional services? Do they understand when the destination changes? Can they explain how to return or recover?  
**What evidence would support or reject the design hypothesis:** Support would be a direct first action on common tasks and accurate explanation of the provider boundary. Rejection would be repeated selection of optional extras for a core task, uncertainty about what a link does, or failure to notice the handoff cue.

**Suggested 60–90 second explanation:**

“Alt 3 is the Action Hub. It starts from the tasks a ticket holder is likely to perform: view, transfer, resale, calendar, itinerary, venue, and support. The central design choice is to make these actions scannable and then separate official options from core ticket management. We also added a ‘before you leave FIFA.com’ banner because PA2 includes evidence of a public-to-partner boundary. The strength is fast execution. The risk is that a large action grid can create a new choice problem. Testing should check first action, category mistakes, and whether users understand the provider and return path.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — ticket-entry and card hierarchy, `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-32-before-partner-handoff.png` — pre-handoff context in the PA2 capture inventory.
- `PA2/capture-work/fifa/desktop/fifa-33-partner-after-public-redirect.png` — partner destination context.

## alt1scenario2.png

**Scenario:** Scenario 2 — Chess.com, beginner review after a game.  
**Alternative:** Alt 1 — Beginner Review Flow.  
**One-sentence concept:** A guided review mode controls the order from one mistake to a better move and a relevant practice path.  
**Source UI patterns:** Chess.com Analysis entry from `chess-29-analysis-board.png`; progressive Learn-to-Play pattern from `chess-26-learn-page.png`; the prototype also retains the persistent Chess.com navigation and board context.  
**Problem being addressed:** A beginner may not know which analysis entry path to choose, how to interpret a mistake, or how to continue into practice.  
**Design motivation:** Bring the progressive “prompt → next step” pattern from Learn into post-game review, reducing entry-choice overload and terminology load.  
**Interaction model:** Fixed linear guided review. The system selects the order and the user follows one focused path.  

**Detailed walkthrough from top-left to bottom-right:**

1. The browser chrome and Chess.com side navigation establish the product context. The artifact’s handwritten header contains “SCENE 1”; the fixed PA3 task mapping treats this file as Scenario 2 because it is the Chess beginner-review alternative.
2. The Game Review header shows the game context and lets the user select Beginner Review instead of Full Analysis.
3. The board remains the main visual reference. Highlighted squares connect the explanation to a concrete position.
4. The result summary states the outcome, accuracy, and number of key mistakes.
5. The progress indicator shows Step 2 of 3, making the review order and remaining work visible.
6. The mistake card explains what happened in plain language and offers Show me on the board.
7. The better-move card explains the safer move and offers Try this move.
8. The practice card turns the review into a short targeted exercise, while Back and Next mistake keep the flow navigable.

**Meaning of each major UI region:**

- **Beginner Review / Full Analysis switch:** Explicit mode choice that avoids forcing advanced analysis on a novice.
- **Board:** Visual grounding for the explanation.
- **Progress indicator:** System-selected sequence and closure.
- **Mistake explanation:** Feedback in plain language rather than engine jargon alone.
- **Better move:** Actionable correction and immediate trial.
- **Practice bridge:** Continuation from explanation to skill-building.

**Primary user path:** Choose Beginner Review → read the current mistake → show it on the board → try the better move → start practice → move to the next mistake.  
**Alternative paths:** Choose Full Analysis; use Previous / Next move controls; go Back; skip to another mistake; return to the wider Chess.com navigation.

**Difference from original website:** The PA2 Analysis capture shows multiple setup and analysis paths but does not show completed beginner review output. This prototype proposes a guided bridge using the simpler Learn-to-Play progression as a pattern.  
**Difference from the other two alternatives in the same scenario:** Alt 1 is the only system-selected sequence. Alt 2 makes the user choose a review card. Alt 3 makes the user choose a question and explores beside the board.

**Strengths:** Low entry decision burden; clear progress; one mistake at a time; feedback and practice are connected; strong closure.  
**Weaknesses:** Reduced flexibility for experienced users; a fixed sequence may not match a learner’s priority; notation or vocabulary may remain a barrier; practice could feel like leaving the review state.  
**Usability dimensions affected:** Learnability, feedback, memory load, recognition, user control, comprehension, and practice continuity.  
**Formative-testing questions:** Can a beginner explain the mistake without repeating the label? Can they identify and try the better move? Do they understand why practice is relevant? Can they return to review?  
**What evidence would support or reject the design hypothesis:** Support would be a coherent explanation of the mistake and next step with minimal facilitator help. Rejection would be repeated confusion about the progress sequence, memorization of “Qe2” without understanding, or loss of context when practice begins.

**Suggested 60–90 second explanation:**

“This is our Beginner Review Flow. We start from the Analysis entry problem: Chess.com exposes several choices, but a beginner may not know where to begin. The user can select Beginner Review, then the system guides them through one mistake, a plain explanation, a better move, and practice. The board stays visible so the explanation is grounded. The main strength is low decision burden and a clear next step. The main risk is reduced flexibility and remaining notation load. We would ask participants to explain the mistake in their own words, try the better move, and reach practice.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry choices, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progressive Learn-to-Play pattern, `C2-E08`.

## alt2scenario2.png

**Scenario:** Scenario 2 — Chess.com, beginner review after a game.  
**Alternative:** Alt 2 — Card Review Mode / Visual Card Dashboard.  
**One-sentence concept:** A non-linear review dashboard lets users browse key moments, choose a card, and move directly into explanation or practice.  
**Source UI patterns:** Chess.com Analysis board from `chess-29-analysis-board.png`; Learn-to-Play progressive guidance from `chess-26-learn-page.png`; card and mini-board content are the proposed review model.  
**Problem being addressed:** A fixed sequence may hide the user’s learning priority when a game contains several mistakes, tactical moments, or concepts worth revisiting.  
**Design motivation:** Reduce recall by making important moments recognizable, while preserving user control over what to review first.  
**Interaction model:** Non-linear visual dashboard. The user controls selection and order through cards.  

**Detailed walkthrough from top-left to bottom-right:**

1. The Chess.com navigation and board create a stable product frame and keep the user oriented.
2. The game result banner provides a high-level summary with accuracy and a short prompt to review key moments.
3. Summary chips show categories such as Good Moves, Mistakes, Blunders, Opening, and Endgame, providing a visual index.
4. The key-moment grid contains mini-board previews, names, move numbers, and short descriptions. Selection controls show which card is active.
5. The expanded card explains the chosen moment, pairs it with a better move, and provides Review, Try this move, or Go to puzzle actions.
6. Back to dashboard and Choose another card preserve the non-linear model. Open in Analysis Board offers optional depth rather than the default start.

**Meaning of each major UI region:**

- **Summary chips:** Recognition-first overview of the game’s shape.
- **Card grid:** Browseable set of learning moments.
- **Mini-boards:** Visual recognition of the position, reducing reliance on notation.
- **Expanded explanation:** Deeper feedback only after a user selects a moment.
- **Practice actions:** Direct bridge from selected review content to a relevant exercise.
- **Analysis link:** Optional advanced depth for users who want it.

**Primary user path:** Scan summary → choose a key-moment card → read the explanation → try the better move or open a puzzle → return to dashboard or choose another card.  
**Alternative paths:** Filter cards; select an opening or endgame concept; open the analysis board; choose another card; return to the dashboard without practicing.

**Difference from original website:** The original Analysis entry shows setup and analysis choices before a beginner knows what matters. This prototype begins from recognizable moments in a completed game and delays deeper analysis until after selection.  
**Difference from the other two alternatives in the same scenario:** Alt 1 provides system-selected order and strongest guidance. Alt 2 provides user-selected content through cards. Alt 3 provides user-selected questions in a conversation.

**Strengths:** Strong scanability; supports recognition and comparison; user control; visible practice bridges; easy to revisit several moments.  
**Weaknesses:** More choices can increase decision load; visual severity can bias selection; users may skip the most teachable moment; card taxonomy may introduce vocabulary.  
**Usability dimensions affected:** Recognition, choice, perceived control, information density, comparison, decision load, and practice continuity.  
**Formative-testing questions:** What card does the participant choose first and why? Can they summarize the selected moment? Do they understand the difference between Review, Try this move, and Go to puzzle? Can they return to the dashboard?  
**What evidence would support or reject the design hypothesis:** Support would be purposeful card selection, understandable mini-board recognition, and correct practice continuation. Rejection would be random or severity-only choice, inability to explain the selected moment, or skipping practice because the card’s next action is unclear.

**Suggested 60–90 second explanation:**

“Alt 2 changes the control model. Instead of forcing a fixed first mistake, it gives the player a visual dashboard of key moments. Summary chips support scanning, cards show mini-board previews, and the selected card expands into an explanation with practice actions. The strength is recognition and choice: the user can start with what they care about. The risk is decision load. A dramatic blunder might attract attention even if another moment is more useful for learning. We would observe the first card selected, ask why, and check whether the participant understands and uses the practice bridge.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry choices, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progressive learning pattern, `C2-E08`.

## alt3scenario2.png

**Scenario:** Scenario 2 — Chess.com, beginner review after a game.  
**Alternative:** Alt 3 — Side-by-Side Assistant.  
**One-sentence concept:** A conversational review assistant stays beside the chessboard, answers natural questions, highlights relevant squares, and suggests follow-ups.  
**Source UI patterns:** Chess.com Analysis board and persistent navigation from `chess-29-analysis-board.png`; plain-language progressive guidance from `chess-26-learn-page.png`; assistant content and highlights are proposed lo-fi interaction behavior.  
**Problem being addressed:** A beginner may not know which analysis control to choose or how to translate engine-like output into a simple question about the board.  
**Design motivation:** Keep board context visible while allowing the user to ask what they need, with suggested prompts to prevent a blank conversational state.  
**Interaction model:** Conversational, user-directed exploration beside the board.  

**Detailed walkthrough from top-left to bottom-right:**

1. The Chess.com left navigation offers persistent access to Play, Puzzles, Learn, Train, Watch, News, Social, and More, while the top bar provides account and search context.
2. The game summary row reports result, accuracy, mistakes, and blunders before the user begins asking questions.
3. The board remains large and central, with the current move and highlighted squares showing the spatial context for explanations.
4. The assistant tab is selected beside other depth areas such as Analysis, Review, Details, and Openings. This creates a bounded assistant mode rather than a generic chat screen.
5. The conversation shows a user question, a plain-language response, a mini-board explanation, and a second question about a better move.
6. The Key Moments panel lists moves with positive, warning, or mistake indicators. The Game Summary groups performance categories.
7. Suggested follow-up chips such as Show variations, Why is ...Bxc3 good?, and Any similar ideas? provide direction.
8. The input field lets the user continue asking while Share review, key moments, and other persistent areas remain available.

**Meaning of each major UI region:**

- **Game summary:** Establishes context before conversation.
- **Board:** Persistent visual anchor and location for highlights.
- **Assistant conversation:** Plain-language explanation and user questions.
- **Key Moments:** Navigable review index that grounds the conversation in the game.
- **Suggested follow-ups:** Bounded next steps that reduce the blank-chat problem.
- **Input field:** User control over what to ask next.

**Primary user path:** Select Assistant → ask why a move was a mistake → read the answer with board highlight → ask for a better move → follow a suggested question → choose practice or another key moment.  
**Alternative paths:** Open Review, Details, or Openings; select a key moment directly; ask about a variation; share the review; return to the game archive.

**Difference from original website:** The captured Analysis entry exposes several advanced routes but does not show a beginner conversational explanation surface. This prototype keeps the board and key moments visible while adding a question-led explanation layer. It does not claim AI answer quality from the capture.  
**Difference from the other two alternatives in the same scenario:** Alt 1 controls the sequence; Alt 2 lets the user choose a card; Alt 3 lets the user choose a question. It offers the most flexible exploration and therefore carries the greatest response-predictability and trust risk.

**Strengths:** Contextual explanation; reduced context switching; natural question path; board highlights; suggested follow-ups; flexible exploration.  
**Weaknesses:** Open-ended interaction may be inconsistent; users may over-trust an answer; broad prompts can produce shallow or contradictory responses; practice may not follow naturally without a deliberate bridge.  
**Usability dimensions affected:** Learnability, user control, conversational clarity, trust calibration, feedback, context retention, and recovery from uncertainty.  
**Formative-testing questions:** Can the participant formulate a useful question? Do they understand the answer and the board highlight? Do they notice uncertainty or ask for clarification? Can they reach a relevant practice action? What happens after an ambiguous follow-up?  
**What evidence would support or reject the design hypothesis:** Support would be understandable question-answer cycles, correct interpretation of highlights, and confident but calibrated next-step choice. Rejection would be repeated dependence on moderator prompting, misplaced trust in unclear answers, or loss of review context when the conversation expands.

**Suggested 60–90 second explanation:**

“Alt 3 is our Side-by-Side Assistant. The user can ask why a move was a mistake or what a better move would be, while the board and key moments remain visible. The assistant answers in plain language and highlights the relevant position. Suggested follow-ups keep the interaction bounded, so the user is not dropped into an empty chat. The main benefit is contextual flexibility. The main risk is answer quality and trust: an open-ended answer can be inconsistent or over-trusted. Testing should include a normal question and an ambiguous follow-up, then check comprehension, confidence, and recovery.”

**Exact original screenshot references used for comparison:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry choices and board context, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progressive explanatory pattern, `C2-E08`.
