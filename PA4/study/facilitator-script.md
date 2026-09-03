# PA4 facilitator script

## Greeting

“Thank you for joining. We are evaluating two interface prototypes, not you. There are no right answers. Please say what you expect to happen and try the interface naturally. I may ask what you are looking for, but I will not tell you where to click.”

## Purpose and consent

“The first prototype is a fictional FIFA ticket-status experience and the second is a fictional Chess.com review experience. The records are demo data, not your real account. With your permission, we would like to record this session so we can review your interactions and task timing for this course assignment. The recording will use an anonymized participant ID and be stored in the Group10 course-assignment workspace, with access limited to the project team and teaching staff as required for the course. It will be retained only for the course assignment/evaluation period and handled or deleted according to our agreed retention process and applicable course requirements. You may ask to stop at any time. Do you consent to participate and to the recording?”

Record the answer before continuing. If consent is not confirmed, do not record or proceed.

## Background questions

Ask only what is needed:

- What device do you normally use for these kinds of tasks?
- How often do you use football ticketing or event-planning websites?
- How familiar are you with Chess.com or chess game review?
- Is there anything about the device or display that would help you use it comfortably today?

Do not ask for account credentials or unnecessary personal details.

## Think-aloud practice

“Before the tasks, please practice saying what you notice on this neutral screen. You do not need to solve anything.”

If the participant goes silent, use only: “What are you looking for?” or “What do you expect that control to do?”

## Task protocol

Use the assigned `condition_order` from `participants.csv`. Read one task exactly as written, then start the timer. This is a moderated concurrent think-aloud: invite the participant to verbalize during the task, but keep prompts neutral. Record task time for descriptive within-study comparison only because verbalization and prompts can affect duration. Do not compare it with an unrelated current-practice baseline. Do not paraphrase toward a control. Do not point, gesture, or name interface labels that give away the answer. If the participant asks for help, use one neutral prompt and increment assistance count.

Allowed neutral prompts:

- “What would you try next?”
- “What information would help you decide?”
- “Please continue when you are ready.”
- “You can stop if you no longer want to continue.”

Do not say “click the button,” “look at the card,” or any equivalent coaching instruction.

Record a hesitation separately when there is no task-progress action for at least 5 consecutive seconds while the participant is visibly attending to the task. Exclude expected reading of substantial explanatory content. Add the timestamp and observable behavior to the task notes; hesitation alone does not lower the success score.

## Assigned-order procedure

Run the two product sections in the assigned order. “First product” and “second product” below refer to the participant’s stored `condition_order`, not a fixed report order.

### FIFA task wording

1. “Determine the overall ticket situation, then explain what needs to happen next for one event.”
2. “Find the relevant order or ticket detail from the status dashboard.”
3. “Start the transfer action and identify the destination before leaving FIFA.”
4. “Return to the FIFA prototype and re-establish the current status context.”

After the FIFA section, administer the five-item questionnaire when FIFA is the first or second assigned product.

### Chess task wording

Reset the prototype before the Chess section and say: “You have finished this fictional game and want to learn from the moments in it. Please use the review dashboard naturally.”

1. “Scan the available key moments and choose what you want to review first.”
2. “Open the chosen moment and explain what happened and why it matters in your own words.”
3. “From a relevant moment, find or try a safer move.”
4. “Find the related optional practice activity, enter or complete it, and return to the card dashboard.”

After the Chess section, administer the same five-item questionnaire when Chess is the first or second assigned product.

### Counterbalanced sequences

- `A_FIFA_FIRST`: FIFA tasks → FIFA questionnaire → reset → Chess tasks → Chess questionnaire.
- `B_CHESS_FIRST`: Chess tasks → Chess questionnaire → reset → FIFA tasks → FIFA questionnaire.

## Interview and closing

Use `post-test-interview.md`. Do not argue with a participant’s interpretation or reveal the expected answer. Thank the participant and say: “We are finished. I will verify the recording filename now.”

Confirm the file convention `P01-session.mp4`, `P02-session.mp4`, and so on. The recorder must verify the expected extension, positive duration, and at least one `codec_type=video` stream through the available media probe before marking the participant row complete. If no probe is available, record `RECORDING_PRESENT_UNVERIFIED`; do not mark it verified.
