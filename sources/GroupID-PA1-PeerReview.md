# GroupID-PA1 Peer Review Preparation: Strava and Nike Run Club

## Presentation plan
The 7-minute peer-review presentation explains why the team compares Strava and Nike Run Club, how the evidence protocol works, what personas and contexts reveal, and which solution priorities should be challenged by reviewers.
| Slide | Topic | Purpose | Speaker | Time |
| --- | --- | --- | --- | --- |
| 1 | PA1 scope and chosen product pair | State Strava and Nike Run Club scope | Member1 | 0:45 |
| 2 | Method and evidence protocol | Explain official-source-first citations | Member1 | 0:55 |
| 3 | Personas and use contexts | Show six personas and motion contexts | Member2 | 1:00 |
| 4 | Strava HCI findings | Record, privacy, route, segment, challenge risks | Member3 | 1:10 |
| 5 | Nike Run Club HCI findings | Audio guidance, plans, challenges, live sharing, metrics | Member4 | 1:10 |
| 6 | Solution priorities | Explain quick wins and deeper redesigns | Member4 | 1:10 |
| 7 | Sprint plan and QA status | Show validation and packaging | Member5 | 0:50 |

## 7-minute script
Member1 opens with the product pair and evidence rule. Member2 explains personas as motion-and-context models. Member3 covers Strava benefits and risks. Member4 covers Nike Run Club benefits, drawbacks, and solution priorities. Member5 closes with sprint QA, source validation, PDF regeneration, and zip package status.

## Likely questions and prepared answers

## Slide speaker notes
Slide 1 note: State the scope as a comparison between Strava and Nike Run Club only. The first sentence should make clear that both products are mobile-first, but they represent different HCI priorities: broad social activity tracking versus running-specific coaching.
Slide 2 note: Explain that the team used official product, help, app-store, and newsroom sources first. Claims about recording, privacy, guided runs, training plans, live sharing, and metrics are cited rather than guessed from unsupported screenshots.
Slide 3 note: Emphasize context. The six personas are not demographic filler; each one defines motion state, lighting/noise, device state, attention level, and the user goal at the moment of interaction.
Slide 4 note: For Strava, focus on record start, privacy selector, route builder, segment leaderboard, and challenge progress. Tie every benefit or drawback to a screen and a concrete runner or cyclist scenario.
Slide 5 note: For Nike Run Club, focus on the start action, metrics screen, audio-guided runs, training plans, challenges, achievements, live sharing, and optional Apple Watch support. Make clear that audio guidance is both a benefit and a risk depending on noise and fatigue.
Slide 6 note: Explain why N-S1, N-S3, N-S7, and N-S9 are quick wins. They address missed instructions, beginner plan overload, live sharing uncertainty, and metric distraction exactly when the user is vulnerable.
Slide 7 note: Close with QA: source log refreshed, PDFs regenerated, extracted text scanned, and zip checked for four top-level PDFs.

## Likely questions and prepared answers
| Question | Prepared answer |
| --- | --- |
| Why compare Strava and Nike Run Club? | Both are mobile-first running products, but Strava is broader social/multi-sport tracking while Nike Run Club is guided running coaching. |
| Which product has better beginner support? | Nike Run Club, because Guided Runs and training plans directly coach novice runners [9][13][14][15]. |
| Which product has higher privacy risk? | Both have privacy risks: Strava route visibility can expose sensitive places, while Nike Run Club live sharing needs clear recipients and expiry [3][10][15]. |
| Why is audio guidance an HCI benefit? | It moves feedback from vision to hearing, reducing visual demand while the runner is moving [9][14][15]. |
| When does audio guidance become a drawback? | When noise, fatigue, music, or earphone problems cause missed cues during motion. |
| How did the team avoid generic analysis? | Each finding names a screen or flow, control, user, context, HCI concept, scenario, severity, and evidence. |

## Mock feedback entries
| Reviewer | Role | Feedback | Response/revision | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| Nora Lee | Peer | Need clearer evidence for Strava privacy. | Added privacy controls citation and privacy receipt solution. | Member2 | Done |
| Omar Khan | Peer | Nike Run Club audio guidance should be both benefit and drawback. | Split N-HCI3 and N-HCI4 with noisy-street scenario. | Member3 | Done |
| Jin Park | Peer | Beginner plan overload needs a persona. | Linked N-D2 to Anh and Minh. | Member2 | Done |
| Mira Vo | Peer | Live sharing risk should name recipients and expiry. | Added N-S7 and N-S8 receipt/expiry controls. | Member4 | Done |
| Sam Patel | Peer | Strava leaderboards need motivation framing. | Added S-HCI7/S-HCI8 and peer-band solution. | Member3 | Done |
| Hana Lim | Peer | The comparison should not treat Nike Run Club as wearable-first. | Rewrote modality as mobile running coach with optional Apple Watch support. | Member1 | Done |
| Leo Tran | Peer | Metric density should include road-crossing context. | Added N-D5 and N-S9/N-S10. | Member4 | Done |
| Ivy Chen | Peer | Sprint plan should show source QA. | Added source collection, PDF text scan, and zip validation tasks. | Member5 | Done |

## Rehearsal checklist
Check 1: The first slide names only Strava and Nike Run Club and defines Nike Run Club as a mobile-first running coach and tracking product.
Check 2: The method slide explains numbered citations and makes clear that the team avoided unsupported screenshots and generic claims.
Check 3: The persona slide shows that each persona has a context: where, when, posture, motion state, device state, connectivity, lighting or noise, interaction method, and attention level.
Check 4: The Strava slide includes at least one benefit and one drawback tied to record, privacy, route, segment, or challenge behavior.
Check 5: The Nike Run Club slide includes the required audio guidance, training plan, challenge, achievement, live sharing, metric density, and Apple Watch support findings.
Check 6: The solution slide does not list ideas without UI behavior. Every idea states the control, feedback, expected gain, and tradeoff.
Check 7: The closing slide mentions source refresh, Markdown regeneration, PDF regeneration, extracted-text scan, and top-level zip contents.
Check 8: The team leaves time for peer questions about beginner support, privacy risk, audio guidance, and evidence quality.

## Presentation risk controls
Risk control A: If a reviewer asks why these two products were paired, the answer should point to shared running use but different HCI emphasis: Strava as social multi-sport tracking and Nike Run Club as guided running coaching.
Risk control B: If a reviewer says the analysis is too broad, the speaker should cite a specific screen or flow, such as Strava activity privacy or Nike Run Club live location sharing.
Risk control C: If a reviewer challenges audio guidance, the speaker should explain both sides: it reduces visual demand, but it can fail in noisy outdoor contexts.
Risk control D: If a reviewer challenges the solution feasibility, the speaker should separate quick wins from deeper redesigns and explain effort tradeoffs.
Risk control E: If a reviewer asks about missing real names, the team should state that placeholders are used until the group supplies the final roster.

## Cue-card Q&A details
Cue card 1: Beginner support. Nike Run Club should be described as stronger for beginners because Guided Runs and coach-created plans reduce the need to design workouts from scratch. The answer should also mention that too many plan choices can still overload a beginner.
Cue card 2: Privacy. Strava privacy risk is about activity audience and route visibility; Nike Run Club privacy risk is about live sharing recipients and sharing duration. The team should not collapse these into one generic privacy issue.
Cue card 3: Safety. Nike Run Club live location sharing is a safety benefit for Minh's night run, but it needs a visible stop state and expiry confirmation to avoid uncertainty after the run.
Cue card 4: Metric density. Both products show useful metrics, but Nike Run Club's during-run context is more sensitive because Sofia may inspect pace while moving quickly in sunlight near crossings.
Cue card 5: Audio. Audio guidance is valuable because it shifts feedback to hearing and keeps eyes on the road. It becomes a drawback when traffic, music, earphones, or fatigue prevent the runner from hearing a cue.
Cue card 6: Evidence. When challenged, speakers should name the exact citation category: official product page, support/help page, app-store listing, newsroom release, or official Nike running article.
Cue card 7: Solution realism. Quick wins are intentionally small UI changes, while deeper redesigns require sensing, state tracking, or motivation-model changes. This keeps the recommendation credible.
Cue card 8: Scope control. The presentation should not drift into broad brand strategy, apparel, hardware ownership, or unrelated fitness apps. The PA1 object is the HCI experience of Strava and Nike Run Club.

## Revision log
Feedback was applied in this order: product-pair correction, evidence refresh, Nike Run Club personas/use cases, HCI finding rewrite, drawback/solution ID consistency, peer-review Q&A, weekly-report sprint tasks, PDF/zip validation.

## References
[1] Strava | Running, Cycling & Hiking App. Official product page. https://www.strava.com/. Accessed 2026-06-10. Supports: Strava positions itself around activity tracking, maps, performance data, and community sharing.
[2] Recording an Activity - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216917397-Recording-an-Activity. Accessed 2026-06-10. Supports: Mobile recording includes activity capture, save/discard choices, activity details, privacy controls, and Beacon entry points.
[3] Activity Privacy Controls - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919377-Activity-Privacy-Controls. Accessed 2026-06-10. Supports: Activities can use Everyone, Followers, or Only You visibility, with default and per-activity changes.
[5] Segment Leaderboard Guidelines - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919507-Segment-Leaderboard-Guidelines. Accessed 2026-06-10. Supports: Segments use matched GPS efforts and leaderboards separated by activity type.
[6] Strava Challenges - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919177-Strava-Challenges. Accessed 2026-06-10. Supports: Challenges motivate activity through distance, elevation, time, segment, and frequency goals.
[9] Nike Run Club App. Official product page. https://www.nike.com/nrc-app. Accessed 2026-06-10. Supports: Nike Run Club is a running app with guided runs, training plans, challenges, run tracking, and community motivation.
[10] Nike Run Club: Running Coach - App Store. Official app store. https://apps.apple.com/us/app/nike-run-club-running-coach/id387771637. Accessed 2026-06-10. Supports: The listing describes Guided Runs, Training Plans, Apple Watch support, challenges, achievements, and safety features.
[11] Nike Run Club - Running Coach - Google Play. Official app store. https://play.google.com/store/apps/details?id=com.nike.plusgps. Accessed 2026-06-10. Supports: The listing describes GPS run tracking, Audio-Guided Runs, Training Plans, challenges, and coaching.
[13] Does the NRC App Have Training Plans? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-plan. Accessed 2026-06-10. Supports: Nike states the app features training plans created by NRC coaches for all levels of runners.
[14] How Do I Get Started in the NRC App? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-start-run. Accessed 2026-06-10. Supports: The Run tab supports basic runs, distance or time targets, speed runs, and Guided Runs.
[15] Nike Run Club App Delivers New Features. Official Nike newsroom. https://about.nike.com/en/newsroom/releases/nike-run-club-app-new-features. Accessed 2026-06-10. Supports: Nike describes localized run tips, real-time location sharing with friends and family, six training plans, and about 300 audio guided runs.
[16] How the Nike Run Club App Can Help You Reach Your Running Goals. Official Nike page. https://www.nike.com/a/running-goals. Accessed 2026-06-10. Supports: Nike describes pace, location, distance, elevation, heart rate, mile splits, progress history, and wearable pairing.
