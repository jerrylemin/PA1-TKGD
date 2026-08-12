# PA3 Paper Prototypes

**Presentation target duration:** about 9 minutes 12 seconds  
**Speaking pace:** clear student presentation pace, roughly 115–125 words per minute  
**Audience:** CSC13112 UI/UX Design lecture / peer review  
**Evidence boundary:** original-interface claims come from approved PA1/PA2 captures and evidence tables; formative-testing language is planned or hypothetical, not reported results.

## Slide 01 — Cover

**Purpose:** Set the scope: two scenarios, six parallel paper prototypes.  
**Estimated time:** 25 seconds  

**Spoken script:**

“This presentation covers our PA3 paper prototypes for two different tasks. The first is FIFA.com, where a user needs to plan and manage tickets with confidence. The second is Chess.com, where a beginner wants to review a game after playing. For each scenario, we created three deliberately different alternatives. These are not six features that we expect to combine. They are six interaction hypotheses that we want formative testing to compare before PA4.”

**Pointer cues:** [Point to the two scenario labels] [Point to the six-alternative mark]  
**Transition to next slide:** “First, I’ll make the design space explicit.”

## Slide 02 — PA3 Design Space

**Purpose:** Explain the axes that keep all six alternatives visibly distinct.  
**Estimated time:** 20 seconds  

**Spoken script:**

“The FIFA alternatives vary by the question the interface answers. Alt 1 is status: what is true now? Alt 2 is progress: where am I in the process? Alt 3 is actions: what can I do now? The Chess alternatives vary by who controls the review. Alt 1 is a guided sequence, Alt 2 is a set of self-selected cards, and Alt 3 is a conversation beside the board. This distinction is important because the alternatives should differ in workflow, not only in styling.”

**Pointer cues:** [Trace the three FIFA cards] [Trace the three Chess cards]  
**Transition to next slide:** “Before showing our solutions, we need to define the original interface baseline.”

## Slide 03 — Scenario 1 Baseline: Original FIFA.com

**Purpose:** Ground the FIFA comparison in the captured desktop state.  
**Estimated time:** 30 seconds  

**Spoken script:**

“This is the approved PA2 capture of FIFA.com’s Tickets and Hospitality page. The visible structure is tournament-first: users see tournament logos, then ticket or hospitality cards, with actions such as registering interest or buying now. The capture supports a discovery model, but it does not show one consolidated cross-tournament status dashboard, a persistent ticket timeline, or an account-level next-step overview. So our three alternatives are trying to add decision confidence after or around that entry model. We are not claiming that this screenshot shows a post-purchase account state that is not visible.”

**Pointer cues:** [Point to tournament logos] [Point to the ticket and hospitality cards] [Point to the source footer]  
**Transition to next slide:** “The first alternative makes the state itself the starting point.”

## Slide 04 — FIFA Alt 1 Overview: Status Dashboard

**Purpose:** Introduce the status-first FIFA alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 1 is the Status Dashboard. Its core idea is status first and confidence first. The user sees four state counts, then upcoming event cards with the current state and a primary action. Quick actions, support, and notifications are kept nearby. Compared with the original tournament-first entry, this is a persistent account-level overview across events. The hypothesis is that a user can identify the current state and the safest next action without opening several separate event pages.”

**Pointer cues:** [Point to the four status cards] [Point to the pending event] [Point to Quick Actions]  
**Transition to next slide:** “The next slide separates the key regions and the risk we would test.”

## Slide 05 — FIFA Alt 1 Interaction Anatomy

**Purpose:** Explain the Status Dashboard’s workflow, strengths, weakness, and test.  
**Estimated time:** 27 seconds  

**Spoken script:**

“The top-left crop is the four-state summary. The second crop shows upcoming events with a direct action, and the third crop keeps support and freshness visible. This design is strong for recognition because the user can scan counts, validity copy, and events in one pass. The risk is that a pending label may still be ambiguous. A user might not know who owns the next step, what resolution is expected, or whether View Order and View Tickets mean different things. In testing, we would ask users to explain one confirmed and one pending event in their own words, then record the first action, wrong paths, and hesitation.”

**Pointer cues:** [Zoom to the four-state summary] [Zoom to the pending card] [Point to the hypothesis text]  
**Transition to next slide:** “Alt 2 addresses that uncertainty by showing movement through the process.”

## Slide 06 — FIFA Alt 2 Overview: Timeline Tracker

**Purpose:** Introduce the progress-first FIFA alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 2 is the Timeline Tracker. It answers a different question: where am I in the process, and what happens next? The main event card contains completed, current, and upcoming milestones. The side panel adds freshness and update history, while the official-source label and next-step guide support trust. Compared with the original ticket entry screenshot, this adds lifecycle visibility and provenance signals. Its hypothesis is that users can locate the current milestone, explain the next step, and judge whether the update is current and official.”

**Pointer cues:** [Trace the timeline from left to right] [Point to Last updated] [Point to Official source]  
**Transition to next slide:** “The interaction anatomy shows why this is not just a more detailed status card.”

## Slide 07 — FIFA Alt 2 Interaction Anatomy

**Purpose:** Contrast progress and status as separate mental models.  
**Estimated time:** 27 seconds  

**Spoken script:**

“Here the key regions are the milestone line, the freshness and update-history panel, the official next steps, and the current position of a pending order. The strength is that normal waiting gets a visible shape. The user can see what has happened and what has not happened yet. The weakness is ownership: future gray stages may look like tasks assigned to the user. We would test whether people can distinguish system work, user work, and normal waiting. Alt 1 asks, ‘What is my status now?’ Alt 2 asks, ‘Where am I in the process?’”

**Pointer cues:** [Zoom to completed/current/upcoming markers] [Point to Official Next Steps] [Compare the Alt 1 and Alt 2 labels]  
**Transition to next slide:** “The third FIFA alternative makes a different trade-off: it optimizes task execution.”

## Slide 08 — FIFA Alt 3 Overview: Action Hub

**Purpose:** Introduce the tasks-first FIFA alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 3 is the Action Hub. Instead of beginning with a dashboard or a timeline, it begins with the user’s likely tasks: view, transfer, resell, add to calendar, share an itinerary, find a venue guide, or contact support. It also separates official options and includes a ‘before you leave FIFA.com’ trust banner. Compared with the original, this reorders the entry surface around doing rather than browsing. The hypothesis is that users find a common action quickly and can tell which options are core ticket management versus optional or external services.”

**Pointer cues:** [Point to Quick Actions] [Point to Official Options] [Point to the handoff banner]  
**Transition to next slide:** “That handoff region is the most important risk to inspect.”

## Slide 09 — FIFA Alt 3 Interaction Anatomy

**Purpose:** Explain task execution, handoff trust, and the choice-load risk.  
**Estimated time:** 27 seconds  

**Spoken script:**

“The quick-action crop shows recognition over recall. The official-options crop shows how add-ons are grouped, while the handoff and security crops explain when a task leaves FIFA.com. The strength is fast routine action. The risk is choice overload: optional packages or resale could look as important as managing an existing ticket. We would give users one core task and one official-options task. We would record their first selection and ask them to explain the provider, destination, and expected return. In one sentence: Alt 1 optimizes state recognition, Alt 2 process understanding, and Alt 3 task execution.”

**Pointer cues:** [Point to the shortcut grid] [Point to the provider boundary] [Compare all three FIFA labels]  
**Transition to next slide:** “This matrix puts the three models side by side without selecting a winner.”

## Slide 10 — Scenario 1 Alternative Comparison

**Purpose:** Summarize the FIFA trade-offs.  
**Estimated time:** 30 seconds  

**Spoken script:**

“The original is useful for discovering an event, but its captured state does not provide the later overview represented by these alternatives. Alt 1 is the best fit for a quick status triage. Alt 2 is the best fit for understanding waiting and next steps. Alt 3 is the best fit for post-purchase actions such as transfer, calendar, venue, or support. Each has a corresponding risk: ambiguous pending states, unclear ownership, or too many options. We would compare them with the same scenario tasks rather than declaring a winner from the sketches.”

**Pointer cues:** [Read the Primary user question row] [Read the Main risk row] [Point to the formative focus row]  
**Transition to next slide:** “The Chess baseline has a different kind of problem: too much choice before the beginner knows what matters.”

## Slide 11 — Scenario 2 Baseline: Original Chess.com

**Purpose:** Ground the Chess comparison in the captured analysis-entry state and Learn pattern.  
**Estimated time:** 30 seconds  

**Spoken script:**

“This PA2 capture shows Chess.com’s Analysis entry. Beside the board, a user can set up a position, explore, search games, use collections, import a file, or start analysis. The evidence supports multiple advanced paths, but it does not show completed review output or a beginner explanation. In PA2, the Learn-to-Play surface provides a simpler pattern: a progressive lesson path, an explanatory prompt, and a clear Next Lesson action. Our three Chess alternatives test three different bridges from that analysis entry toward a beginner review after a game.”

**Pointer cues:** [Point to the Analysis choices] [Point to the board] [Point to the source footer]  
**Transition to next slide:** “Alt 1 brings the progressive pattern directly into review.”

## Slide 12 — Chess Alt 1 Overview: Beginner Review Flow

**Purpose:** Introduce the guided Chess alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 1 is the Beginner Review Flow. The system controls the sequence: choose Beginner Review, move through one mistake, read a plain-language explanation, see the better move, try it, and then practice the idea. This reduces the number of decisions a beginner must make at the start. It keeps the board visible and gives a direct next action. Compared with the original, this is a constrained mode rather than a general analysis entry. The hypothesis is that beginners can explain one mistake and reach relevant practice with low decision burden.”

**Pointer cues:** [Point to the Beginner Review selector] [Trace Step 2 of 3] [Point to Try this move and Start practice]  
**Transition to next slide:** “Its strength is guidance, but that guidance also reduces user control.”

## Slide 13 — Chess Alt 1 Interaction Anatomy

**Purpose:** Explain the guided workflow’s usability trade-offs.  
**Estimated time:** 27 seconds  

**Spoken script:**

“The progress indicator makes the sequence legible. The mistake panel explains why the move matters, the better-move panel supports feedback, and the practice card provides closure. The likely benefit is lower memory load and stronger learnability. The risk is that experienced users may find the flow restrictive, and beginners may still need piece names or visual arrows before notation. We would ask the participant to explain the mistake without simply repeating a label, try the better move, and tell us what they would do next. The measures are hypotheses, not results.”

**Pointer cues:** [Point to the progress indicator] [Point to the mistake explanation] [Point to the practice bridge]  
**Transition to next slide:** “Alt 2 keeps the learning content but gives the user control over where to start.”

## Slide 14 — Chess Alt 2 Overview: Card Review Mode

**Purpose:** Introduce the non-linear card-based alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 2 is Card Review Mode. It starts with performance summary chips and a grid of key moments. Each card has a mini-board and a short description. The user can choose a card, expand the explanation, try the move, or jump to a puzzle. This is not a renamed wizard. The defining change is that the user selects the content and the order. Compared with the original Analysis entry, the interface begins from recognizable moments in the completed game rather than from setup commands. The hypothesis is that users can browse and choose a meaningful learning moment without recalling analysis vocabulary.”

**Pointer cues:** [Point to the summary chips] [Point to the card grid] [Point to the expanded selected card]  
**Transition to next slide:** “The benefit is choice and scanability; the risk is a larger decision surface.”

## Slide 15 — Chess Alt 2 Interaction Anatomy

**Purpose:** Explain card selection, choice load, and practice continuation.  
**Estimated time:** 27 seconds  

**Spoken script:**

“The card grid makes recognition possible through mini-boards, labels, and visual severity. The selected card expands into an explanation with review, better move, and puzzle actions. The strength is scanability and user control. The weakness is that a beginner may select the most dramatic card instead of the most teachable one, or may see too many choices at once. We would record the first card selected, ask why it was selected, and check whether the participant understands the practice connection. Alt 1 gives the system-selected order; Alt 2 gives the user-selected content.”

**Pointer cues:** [Point to the card grid] [Point to the selected card] [Compare Alt 1 and Alt 2]  
**Transition to next slide:** “Alt 3 changes the unit of control again: the user controls the question.”

## Slide 16 — Chess Alt 3 Overview: Side-by-Side Assistant

**Purpose:** Introduce the conversational alternative.  
**Estimated time:** 28 seconds  

**Spoken script:**

“Alt 3 is the Side-by-Side Assistant. The board and assistant remain visible together. The user can ask why a move was a mistake, ask for a better move, and follow suggested questions. Responses include contextual board highlights and key moments. Compared with the original Analysis entry, the user does not have to know which analysis command to choose first. Instead, the user starts with a natural question while keeping board context. The hypothesis is that contextual answers reduce switching and help a beginner continue exploring.”

**Pointer cues:** [Point to the board] [Point to the user question] [Point to the contextual assistant response]  
**Transition to next slide:** “That flexibility comes with a trust and consistency risk.”

## Slide 17 — Chess Alt 3 Interaction Anatomy

**Purpose:** Explain conversational strengths, risks, and test questions.  
**Estimated time:** 27 seconds  

**Spoken script:**

“The board crop shows the current position and key moments. The assistant crop shows a question and plain-language response, while the follow-up crop keeps exploration moving. The strength is contextual explanation without leaving the board. The risk is that open-ended answers can be inconsistent or over-trusted. We would include one normal question and one ambiguous follow-up. We would observe how the user formulates the question, whether the answer is understood, whether uncertainty is noticed, and whether the user can recover. Alt 1 controls the sequence, Alt 2 controls the card, and Alt 3 controls the question.”

**Pointer cues:** [Point to the red key moment] [Point to the assistant response] [Point to suggested follow-ups]  
**Transition to next slide:** “The Chess comparison makes those three control models explicit.”

## Slide 18 — Scenario 2 Alternative Comparison

**Purpose:** Summarize the Chess trade-offs.  
**Estimated time:** 30 seconds  

**Spoken script:**

“The original Analysis entry offers flexible depth, but it puts more entry decisions on the user. Alt 1 offers the highest guidance and the clearest closure, with less flexibility. Alt 2 makes important moments recognizable and selectable, but adds choice. Alt 3 keeps context and flexibility, but depends on the quality and predictability of the conversation. The formative focus should match the model: mistake comprehension for Alt 1, choice and practice for Alt 2, and question quality plus trust for Alt 3.”

**Pointer cues:** [Read Who controls sequence?] [Read Main risk] [Point to the formative focus row]  
**Transition to next slide:** “Because these are hypotheses, the next step is a shared test protocol.”

## Slide 19 — Formative Testing: What the Alternatives Need to Prove

**Purpose:** Define neutral, evidence-safe formative measures.  
**Estimated time:** 32 seconds  

**Spoken script:**

“PA3 requires several sessions with two or three participants who have no prior knowledge of the prototypes. For FIFA, candidate tasks are to identify the current state, find what happens next, find a common action, and judge whether the information looks current and official. For Chess, the tasks are to find where to start, explain one mistake, identify and try a better move, and reach relevant practice. We would record completion, own-words comprehension, wrong paths, hesitation, perceived control, and handoff or practice continuation. These are planned measures. Our existing project files do not evidence real participant results yet.”

**Pointer cues:** [Point to FIFA candidate tasks] [Point to Chess candidate tasks] [Point to “not results”]  
**Transition to next slide:** “So PA3 is not deciding from the drawings alone.”

## Slide 20 — What PA3 Decides for PA4

**Purpose:** Close with the evidence-led decision and PA4 handoff.  
**Estimated time:** 25 seconds  

**Spoken script:**

“The six sketches represent six distinct interaction hypotheses. Formative testing will tell us which FIFA model gives stronger ticket confidence, which Chess model supports beginner understanding with acceptable decision load, which weaknesses need revision, and which lo-fi alternative should advance to PA4 hi-fi work. The next step is to run the same neutral tasks with real participants, keep observed behavior separate from interpretation, and document the evidence before selecting a direction. Thank you.”

**Pointer cues:** [Point across the six-prototype strip] [Point to PA1 → PA2 → PA3 → PA4]  
**Transition to next slide:** “End.”

## Timing check

The estimated slide times sum to **552 seconds / 9 minutes 12 seconds**, which is within the PA3 5–10 minute presentation requirement and the requested 9–10 minute target.
