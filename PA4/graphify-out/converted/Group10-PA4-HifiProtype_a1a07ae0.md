<!-- converted from Group10-PA4-HifiProtype.docx -->

Group10 PA4 · Hi-fi Prototype
FIFA Status Dashboard + Chess Beginner Review Flow

This editable report records the locally achievable hi-fi implementation. No genuine external demo URL is invented while that evidence is missing.
# Project continuity
PA1 established FIFA.com as a browse-first official football ecosystem and Chess.com as an action-first play, review, and learning platform. PA2 translated those findings into the Status Dashboard and Beginner Review concepts. PA3 selected FIFA Alt 1 and Chess Alt 1 for the PA4 hi-fi implementation.
# Hi-fi design objectives
- Make the current state or learning moment visible before secondary detail.
- Place the next action beside the explanation that makes it meaningful.
- Use text, icon, and state treatment together so color is not the only cue.
- Make external transitions and recovery states testable in a deterministic offline demo.
- Keep the responsive surface usable at 1440 × 900 and 390 × 844.
# FIFA Status Dashboard
The FIFA flow uses a status-first editorial surface with fictional Mexico City pending and Toronto confirmed events. Official source, freshness, ownership, action adjacency, and the partner boundary remain visible without claiming a live transaction.

Figure: fifa desktop overview
## FIFA key interactions
- Select Pending or Confirmed event rows.
- Reveal the status definition and next owner.
- Open order or ticket detail.
- Save the confirmed event to the calendar.
- Preview the partner destination before transfer.
- Stay or continue, then return with context.
- Presenter mode can preview unavailable and reset states; study mode removes those researcher controls.

Figure: fifa desktop handoff
# Chess Beginner Review Flow
The Chess flow uses a guided one-mistake-at-a-time route. The validated scenario checks Qh5: Nxh5 captures the queen. The revealed alternative is Qe2, and the separate practice position uses Qd3. Check an opponent's attack before moving a valuable piece.

Figure: chess desktop mistake
- Start from an intro state that does not reveal the answer.
- Read the mistake and immediate consequence in plain language.
- Reveal the better move only at the appropriate stage.
- Select the source piece and destination on the trial board; wrong moves give feedback and can be retried.
- Complete the separate practice position with the same source-to-destination interaction.
- Finish the route or return to the review without losing context.

Figure: chess desktop practice
# Study routes and responsive validation


# Limitations and external evidence

| YOUTUBE DEMO LINK
YouTube demo link: REQUIRED EXTERNAL EVIDENCE BEFORE SUBMISSION |
| --- |
| Route | URL |
| --- | --- |
| FIFA study | ?mode=study&product=fifa#fifa |
| Chess study | ?mode=study&product=chess#chess |
| Viewport | Validated behavior |
| --- | --- |
| 1440 × 900 | Product hierarchy, rail guidance, board interaction, and primary controls remain usable. |
| 390 × 844 | Columns stack, board remains readable, controls wrap, and no horizontal overflow is expected. |
| Study mode | Researcher branding, launcher, reset/preview controls, and demo help are removed from the participant DOM. |
| Presenter mode | Launcher, demo labels, help, reset, and unavailable-state preview remain available for demonstration and QA. |
| BLOCKED EXTERNALLY
A genuine YouTube demo URL, real participant sessions, verified recordings, questionnaire/interview evidence, and measured task timings are not local facts. The prototype is locally runnable and browser-tested, but it does not use live FIFA, ticketing, partner, or Chess.com backends. |
| --- |