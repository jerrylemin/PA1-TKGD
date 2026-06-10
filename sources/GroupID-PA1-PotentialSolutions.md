# GroupID-PA1 Potential Solutions: Strava and Nike Run Club

## Executive summary
This report maps every Strava and Nike Run Club drawback from ProductResearch to two concrete interface solutions. Strava work prioritizes recoverability, privacy clarity, route simplification, healthier social comparison, and post-activity readability. Nike Run Club work prioritizes missed audio recovery, beginner plan selection, healthy motivation, live-sharing privacy, and safer during-run metrics.

## Problem inventory
| ID | Product | Problem | Severity |
| --- | --- | --- | --- |
| S-D1 | Strava | Irrecoverable discard risk | High |
| S-D2 | Strava | Privacy audience uncertainty | High |
| S-D3 | Strava | Route planning overload | Medium |
| S-D4 | Strava | Leaderboard pressure | Medium |
| S-D5 | Strava | Post-activity detail density | Medium |
| N-D1 | Nike Run Club | Audio-guided run cues may be missed in noisy outdoor contexts. | Medium |
| N-D2 | Nike Run Club | Training plan selection may overload beginners. | Medium |
| N-D3 | Nike Run Club | Challenge and achievement mechanics may pressure casual users. | Medium |
| N-D4 | Nike Run Club | Live location sharing may create privacy uncertainty. | High |
| N-D5 | Nike Run Club | During-run metric density may distract runners in motion. | Medium |

## Solution framework
Each design concept states affected product, personas, contexts, UI behavior, HCI principle mapping, expected improvement, tradeoffs, priority, and effort.

| ID | Product | Drawback | Design concept | UI and behavior detail | HCI principles | Affected personas | Affected contexts | Expected improvement, tradeoffs, priority, effort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-S1 | Strava | S-D1 | Recoverable Activity Trash | After discard, move activity to a 7-day trash with Restore and Delete forever. | Error recovery; user control | Maya/Lina | End-of-run fatigue | Expected gain: fewer lost recordings. Tradeoff: storage and extra state. Priority High. Effort Medium. |
| S-S2 | Strava | S-D1 | Safer Finish Hierarchy | Make Save primary, move Discard behind a confirm sheet with activity summary. | Error prevention; motor efficiency | Maya/Lina | Sweaty hands after activity | Expected gain: fewer accidental destructive actions. Tradeoff: one extra tap for true discard. Priority High. Effort Low. |
| S-S3 | Strava | S-D2 | Privacy Receipt | Show audience, map visibility, and home-area warning before save. | Privacy mental model; visibility | Maya/Lina | Home route sharing | Expected gain: higher confidence. Tradeoff: more review text. Priority High. Effort Low. |
| S-S4 | Strava | S-D2 | Sensitive Route Reminder | Detect route near saved home area and suggest Only You or hidden map zone. | Error prevention; feedforward | Maya | Campus/home start | Expected gain: lower accidental exposure. Tradeoff: false positives. Priority High. Effort Medium. |
| S-S5 | Strava | S-D3 | Simple Route Wizard | Ask distance, sport, and loop/out-back, then recommend one editable route. | Progressive disclosure; recognition | Dara/Maya | Planning a new route | Expected gain: lower setup effort. Tradeoff: less initial control. Priority Medium. Effort Medium. |
| S-S6 | Strava | S-D3 | Route Confidence Labels | Label routes Easy, Hilly, Unfamiliar, or Busy based on visible criteria. | Feedforward; mental model | Dara/Maya | Map route choice | Expected gain: faster decision. Tradeoff: requires clear criteria. Priority Medium. Effort Medium. |
| S-S7 | Strava | S-D4 | Peer-Band Leaderboards | Default casual users to similar-level comparison bands before global ranking. | Motivation design; satisfaction | Maya/Dara | Segment review | Expected gain: less demotivation. Tradeoff: competitive users may prefer global view. Priority Medium. Effort High. |
| S-S8 | Strava | S-D4 | Personal Progress First | Show PR delta and trend before rank for casual profiles. | Feedback; user fit | Maya | Post-run review | Expected gain: healthier motivation. Tradeoff: rank is one tap deeper. Priority Medium. Effort Low. |
| S-S9 | Strava | S-D5 | Post-Activity Summary Mode | Show map, distance, time, privacy first; hide comments/segments behind tabs. | Cognitive load reduction | Lina | Low-light review | Expected gain: less visual overload. Tradeoff: advanced metrics are less immediate. Priority Medium. Effort Medium. |
| S-S10 | Strava | S-D5 | Large-Type Review | Offer high-contrast, large-type post-run summary for tired or low-light contexts. | Vision; accessibility | Lina | Evening walk | Expected gain: better readability. Tradeoff: more display modes. Priority Low. Effort Medium. |
| N-S1 | Nike Run Club | N-D1 | Audio Cue Replay button | Small accessible control on run screen and headphone gesture shortcut; shows last cue text summary for 5 seconds. | Recovery; auditory limitation support; reduced memory load | Anh/Sofia/Minh | Noisy streets, fatigue, music playback | Expected gain: fewer missed instructions. Tradeoff: adds control to run screen. Priority High. Effort Low. |
| N-S2 | Nike Run Club | N-D1 | Adaptive cue mode | User selects Quiet route, Normal, or Noisy street; app increases cue clarity, haptic emphasis, and text summary by mode. | Context-aware feedback; multimodal interaction | Anh/Sofia/Minh | Traffic or crowded route | Expected gain: better guidance in traffic. Tradeoff: mode setup can add complexity. Priority Medium. Effort High. |
| N-S3 | Nike Run Club | N-D2 | Beginner Plan Wizard | Ask current ability, target distance, available days, injury concern; recommend one plan with a clear reason. | Recognition over recall; progressive disclosure | Anh/Minh | First 5K or return after break | Expected gain: lower setup effort. Tradeoff: users may want full list immediately. Priority High. Effort Medium. |
| N-S4 | Nike Run Club | N-D2 | Plan difficulty receipt | Before starting a plan, show weekly load, rest days, expected longest run, and Edit Difficulty. | Feedforward; user control; error prevention | Anh/Minh | Low-confidence plan selection | Expected gain: lower overcommitment. Tradeoff: more pre-plan reading. Priority Medium. Effort Medium. |
| N-S5 | Nike Run Club | N-D3 | Healthy Streak mode | Rest day counts as protected training when user selects recovery. | Motivation design; overtraining prevention | Anh/Minh | Rest-day anxiety | Expected gain: less pressure to run every day. Tradeoff: streak semantics change. Priority Medium. Effort Medium. |
| N-S6 | Nike Run Club | N-D3 | Challenge pressure filter | Label challenges Casual, Consistent, Competitive; default new users to Casual. | Mental model alignment; choice architecture | Anh/Minh | Monthly challenge browsing | Expected gain: better fit by user type. Tradeoff: challenge taxonomy maintenance. Priority Medium. Effort Low. |
| N-S7 | Nike Run Club | N-D4 | Live Sharing Receipt | After starting sharing, show recipients, duration, stop button, and finish notification status. | Visibility of system status; privacy mental model | Sofia/Minh | Night run family sharing | Expected gain: higher trust. Tradeoff: extra status surface. Priority High. Effort Low. |
| N-S8 | Nike Run Club | N-D4 | Auto-stop and expiry control | Default live sharing expires at run end or chosen duration; end screen confirms sharing stopped. | Error prevention; closure feedback | Sofia/Minh | Safety sharing with family | Expected gain: lower privacy risk. Tradeoff: edge cases for extended runs. Priority Medium. Effort Medium. |
| N-S9 | Nike Run Club | N-D5 | Focus Run screen | During movement, show only distance, pace, and elapsed time with large type; move other metrics behind swipe or post-run detail. | Cognitive load reduction; human vision; motor efficiency | Sofia/Anh | Bright sunlight and fast pace | Expected gain: safer glance behavior. Tradeoff: fewer metrics visible by default. Priority High. Effort Medium. |
| N-S10 | Nike Run Club | N-D5 | Crossing-safe interaction lock | If phone detects fast movement and screen wake, delay nonessential overlays and use voice or haptic cues. | Interruption management; safety; attention support | Sofia/Anh | Road crossings | Expected gain: fewer distraction moments. Tradeoff: may suppress desired messages. Priority Medium. Effort High. |

## Drawback-to-solution mapping
| Drawback | Solutions |
| --- | --- |
| S-D1 | S-S1, S-S2 |
| S-D2 | S-S3, S-S4 |
| S-D3 | S-S5, S-S6 |
| S-D4 | S-S7, S-S8 |
| S-D5 | S-S9, S-S10 |
| N-D1 | N-S1, N-S2 |
| N-D2 | N-S3, N-S4 |
| N-D3 | N-S5, N-S6 |
| N-D4 | N-S7, N-S8 |
| N-D5 | N-S9, N-S10 |

## Detailed implementation notes
### S-S1 Recoverable Activity Trash
Affected product: Strava. Drawback: S-D1. Affected personas: Maya/Lina. Affected contexts: End-of-run fatigue.
UI and behavior level: After discard, move activity to a 7-day trash with Restore and Delete forever. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Error recovery; user control. Expected gain: fewer lost recordings. Tradeoff: storage and extra state. Priority High. Effort Medium.

### S-S2 Safer Finish Hierarchy
Affected product: Strava. Drawback: S-D1. Affected personas: Maya/Lina. Affected contexts: Sweaty hands after activity.
UI and behavior level: Make Save primary, move Discard behind a confirm sheet with activity summary. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Error prevention; motor efficiency. Expected gain: fewer accidental destructive actions. Tradeoff: one extra tap for true discard. Priority High. Effort Low.

### S-S3 Privacy Receipt
Affected product: Strava. Drawback: S-D2. Affected personas: Maya/Lina. Affected contexts: Home route sharing.
UI and behavior level: Show audience, map visibility, and home-area warning before save. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Privacy mental model; visibility. Expected gain: higher confidence. Tradeoff: more review text. Priority High. Effort Low.

### S-S4 Sensitive Route Reminder
Affected product: Strava. Drawback: S-D2. Affected personas: Maya. Affected contexts: Campus/home start.
UI and behavior level: Detect route near saved home area and suggest Only You or hidden map zone. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Error prevention; feedforward. Expected gain: lower accidental exposure. Tradeoff: false positives. Priority High. Effort Medium.

### S-S5 Simple Route Wizard
Affected product: Strava. Drawback: S-D3. Affected personas: Dara/Maya. Affected contexts: Planning a new route.
UI and behavior level: Ask distance, sport, and loop/out-back, then recommend one editable route. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Progressive disclosure; recognition. Expected gain: lower setup effort. Tradeoff: less initial control. Priority Medium. Effort Medium.

### S-S6 Route Confidence Labels
Affected product: Strava. Drawback: S-D3. Affected personas: Dara/Maya. Affected contexts: Map route choice.
UI and behavior level: Label routes Easy, Hilly, Unfamiliar, or Busy based on visible criteria. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Feedforward; mental model. Expected gain: faster decision. Tradeoff: requires clear criteria. Priority Medium. Effort Medium.

### S-S7 Peer-Band Leaderboards
Affected product: Strava. Drawback: S-D4. Affected personas: Maya/Dara. Affected contexts: Segment review.
UI and behavior level: Default casual users to similar-level comparison bands before global ranking. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Motivation design; satisfaction. Expected gain: less demotivation. Tradeoff: competitive users may prefer global view. Priority Medium. Effort High.

### S-S8 Personal Progress First
Affected product: Strava. Drawback: S-D4. Affected personas: Maya. Affected contexts: Post-run review.
UI and behavior level: Show PR delta and trend before rank for casual profiles. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Feedback; user fit. Expected gain: healthier motivation. Tradeoff: rank is one tap deeper. Priority Medium. Effort Low.

### S-S9 Post-Activity Summary Mode
Affected product: Strava. Drawback: S-D5. Affected personas: Lina. Affected contexts: Low-light review.
UI and behavior level: Show map, distance, time, privacy first; hide comments/segments behind tabs. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Cognitive load reduction. Expected gain: less visual overload. Tradeoff: advanced metrics are less immediate. Priority Medium. Effort Medium.

### S-S10 Large-Type Review
Affected product: Strava. Drawback: S-D5. Affected personas: Lina. Affected contexts: Evening walk.
UI and behavior level: Offer high-contrast, large-type post-run summary for tired or low-light contexts. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Vision; accessibility. Expected gain: better readability. Tradeoff: more display modes. Priority Low. Effort Medium.

### N-S1 Audio Cue Replay button
Affected product: Nike Run Club. Drawback: N-D1. Affected personas: Anh/Sofia/Minh. Affected contexts: Noisy streets, fatigue, music playback.
UI and behavior level: Small accessible control on run screen and headphone gesture shortcut; shows last cue text summary for 5 seconds. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Recovery; auditory limitation support; reduced memory load. Expected gain: fewer missed instructions. Tradeoff: adds control to run screen. Priority High. Effort Low.

### N-S2 Adaptive cue mode
Affected product: Nike Run Club. Drawback: N-D1. Affected personas: Anh/Sofia/Minh. Affected contexts: Traffic or crowded route.
UI and behavior level: User selects Quiet route, Normal, or Noisy street; app increases cue clarity, haptic emphasis, and text summary by mode. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Context-aware feedback; multimodal interaction. Expected gain: better guidance in traffic. Tradeoff: mode setup can add complexity. Priority Medium. Effort High.

### N-S3 Beginner Plan Wizard
Affected product: Nike Run Club. Drawback: N-D2. Affected personas: Anh/Minh. Affected contexts: First 5K or return after break.
UI and behavior level: Ask current ability, target distance, available days, injury concern; recommend one plan with a clear reason. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Recognition over recall; progressive disclosure. Expected gain: lower setup effort. Tradeoff: users may want full list immediately. Priority High. Effort Medium.

### N-S4 Plan difficulty receipt
Affected product: Nike Run Club. Drawback: N-D2. Affected personas: Anh/Minh. Affected contexts: Low-confidence plan selection.
UI and behavior level: Before starting a plan, show weekly load, rest days, expected longest run, and Edit Difficulty. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Feedforward; user control; error prevention. Expected gain: lower overcommitment. Tradeoff: more pre-plan reading. Priority Medium. Effort Medium.

### N-S5 Healthy Streak mode
Affected product: Nike Run Club. Drawback: N-D3. Affected personas: Anh/Minh. Affected contexts: Rest-day anxiety.
UI and behavior level: Rest day counts as protected training when user selects recovery. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Motivation design; overtraining prevention. Expected gain: less pressure to run every day. Tradeoff: streak semantics change. Priority Medium. Effort Medium.

### N-S6 Challenge pressure filter
Affected product: Nike Run Club. Drawback: N-D3. Affected personas: Anh/Minh. Affected contexts: Monthly challenge browsing.
UI and behavior level: Label challenges Casual, Consistent, Competitive; default new users to Casual. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Mental model alignment; choice architecture. Expected gain: better fit by user type. Tradeoff: challenge taxonomy maintenance. Priority Medium. Effort Low.

### N-S7 Live Sharing Receipt
Affected product: Nike Run Club. Drawback: N-D4. Affected personas: Sofia/Minh. Affected contexts: Night run family sharing.
UI and behavior level: After starting sharing, show recipients, duration, stop button, and finish notification status. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Visibility of system status; privacy mental model. Expected gain: higher trust. Tradeoff: extra status surface. Priority High. Effort Low.

### N-S8 Auto-stop and expiry control
Affected product: Nike Run Club. Drawback: N-D4. Affected personas: Sofia/Minh. Affected contexts: Safety sharing with family.
UI and behavior level: Default live sharing expires at run end or chosen duration; end screen confirms sharing stopped. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Error prevention; closure feedback. Expected gain: lower privacy risk. Tradeoff: edge cases for extended runs. Priority Medium. Effort Medium.

### N-S9 Focus Run screen
Affected product: Nike Run Club. Drawback: N-D5. Affected personas: Sofia/Anh. Affected contexts: Bright sunlight and fast pace.
UI and behavior level: During movement, show only distance, pace, and elapsed time with large type; move other metrics behind swipe or post-run detail. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Cognitive load reduction; human vision; motor efficiency. Expected gain: safer glance behavior. Tradeoff: fewer metrics visible by default. Priority High. Effort Medium.

### N-S10 Crossing-safe interaction lock
Affected product: Nike Run Club. Drawback: N-D5. Affected personas: Sofia/Anh. Affected contexts: Road crossings.
UI and behavior level: If phone detects fast movement and screen wake, delay nonessential overlays and use voice or haptic cues. Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.
HCI principle mapping: Interruption management; safety; attention support. Expected gain: fewer distraction moments. Tradeoff: may suppress desired messages. Priority Medium. Effort High.


## Impact-effort prioritization
| Priority band | Solutions | Reason |
| --- | --- | --- |
| Quick wins | N-S1 Audio Cue Replay; N-S3 Beginner Plan Wizard; N-S7 Live Sharing Receipt; N-S9 Focus Run screen; S-S2 Safer Finish Hierarchy; S-S3 Privacy Receipt | Low-to-medium effort with direct reduction in missed cues, beginner overload, privacy uncertainty, motion distraction, destructive action, and sensitive route exposure. |
| Deeper redesign | N-S2 Adaptive cue mode; N-S4 Plan difficulty receipt; N-S5 Healthy Streak mode; N-S8 Auto-stop and expiry control; N-S10 Crossing-safe interaction lock; S-S1 Recoverable Activity Trash; S-S7 Peer-Band Leaderboards | Requires more product state, context sensing, or motivation-model changes. |
| Later enhancements | S-S5 Simple Route Wizard; S-S6 Route Confidence Labels; S-S8 Personal Progress First; S-S9 Post-Activity Summary Mode; S-S10 Large-Type Review; N-S6 Challenge pressure filter | Useful improvements after high-risk privacy, safety, and destructive-action issues are handled. |

## Phased recommendation plan
Phase 1 implements quick wins for Nike Run Club and Strava. Phase 2 tests deeper redesigns with beginner and night-run scenarios. Phase 3 revisits social motivation defaults after peer review. The design team should prototype N-S1, N-S3, N-S7, and N-S9 first because they are visible in the exact moments where the HCI risk occurs.

## References
[1] Strava | Running, Cycling & Hiking App. Official product page. https://www.strava.com/. Accessed 2026-06-10. Supports: Strava positions itself around activity tracking, maps, performance data, and community sharing.
[2] Recording an Activity - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216917397-Recording-an-Activity. Accessed 2026-06-10. Supports: Mobile recording includes activity capture, save/discard choices, activity details, privacy controls, and Beacon entry points.
[3] Activity Privacy Controls - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919377-Activity-Privacy-Controls. Accessed 2026-06-10. Supports: Activities can use Everyone, Followers, or Only You visibility, with default and per-activity changes.
[4] Creating Routes on Mobile - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/18001474720397-Creating-Routes-on-Mobile. Accessed 2026-06-10. Supports: The mobile Maps tab and Create Route flow support route planning by sport type and map interaction.
[5] Segment Leaderboard Guidelines - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919507-Segment-Leaderboard-Guidelines. Accessed 2026-06-10. Supports: Segments use matched GPS efforts and leaderboards separated by activity type.
[6] Strava Challenges - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919177-Strava-Challenges. Accessed 2026-06-10. Supports: Challenges motivate activity through distance, elevation, time, segment, and frequency goals.
[9] Nike Run Club App. Official product page. https://www.nike.com/nrc-app. Accessed 2026-06-10. Supports: Nike Run Club is a running app with guided runs, training plans, challenges, run tracking, and community motivation.
[10] Nike Run Club: Running Coach - App Store. Official app store. https://apps.apple.com/us/app/nike-run-club-running-coach/id387771637. Accessed 2026-06-10. Supports: The listing describes Guided Runs, Training Plans, Apple Watch support, challenges, achievements, and safety features.
[11] Nike Run Club - Running Coach - Google Play. Official app store. https://play.google.com/store/apps/details?id=com.nike.plusgps. Accessed 2026-06-10. Supports: The listing describes GPS run tracking, Audio-Guided Runs, Training Plans, challenges, and coaching.
[12] Running Training Plans. Nike.com. Official Nike page. https://www.nike.com/running/training-plans. Accessed 2026-06-10. Supports: Nike training plans include guided runs, mindset advice, recovery tips, and goal-oriented running schedules.
[13] Does the NRC App Have Training Plans? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-plan. Accessed 2026-06-10. Supports: Nike states the app features training plans created by NRC coaches for all levels of runners.
[14] How Do I Get Started in the NRC App? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-start-run. Accessed 2026-06-10. Supports: The Run tab supports basic runs, distance or time targets, speed runs, and Guided Runs.
[15] Nike Run Club App Delivers New Features. Official Nike newsroom. https://about.nike.com/en/newsroom/releases/nike-run-club-app-new-features. Accessed 2026-06-10. Supports: Nike describes localized run tips, real-time location sharing with friends and family, six training plans, and about 300 audio guided runs.
[16] How the Nike Run Club App Can Help You Reach Your Running Goals. Official Nike page. https://www.nike.com/a/running-goals. Accessed 2026-06-10. Supports: Nike describes pace, location, distance, elevation, heart rate, mile splits, progress history, and wearable pairing.
