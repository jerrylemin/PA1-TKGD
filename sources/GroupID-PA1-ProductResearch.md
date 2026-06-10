# GroupID-PA1 Product Research: Strava and Nike Run Club

## Executive summary
This report compares Strava and Nike Run Club as mobile-first running and activity products. Strava emphasizes broad sports tracking, social competition, route and segment culture, activity sharing, and privacy settings. Nike Run Club emphasizes running-specific coaching, audio guidance, beginner support, training plans, achievements, challenges, and safety sharing [1][2][9][10][15].

## Product selection
| Product | Domain | Modality | Positioning |
| --- | --- | --- | --- |
| Strava | Sports activity tracking and social fitness | Mobile-first GPS, maps, social feed, route and segment interaction | Mobile social activity network and multi-sport tracking. |
| Nike Run Club | Running coach and run tracking | Mobile-first run tracking, audio-guided coaching, plans, challenges, achievements, live location sharing, optional Apple Watch support | Mobile running coach and guided run experience, with optional Apple Watch support. |

## Source protocol
Official product, support, help, newsroom, App Store, and Google Play pages were prioritized. Every nontrivial product claim cites the numbered references below; interface observations are treated as source-grounded, not as unsupported screenshots.

| Citation | Product | Type | Claim supported |
| --- | --- | --- | --- |
| [1] | Strava | Official product page | Strava positions itself around activity tracking, maps, performance data, and community sharing. |
| [2] | Strava | Official support | Mobile recording includes activity capture, save/discard choices, activity details, privacy controls, and Beacon entry points. |
| [3] | Strava | Official support | Activities can use Everyone, Followers, or Only You visibility, with default and per-activity changes. |
| [4] | Strava | Official support | The mobile Maps tab and Create Route flow support route planning by sport type and map interaction. |
| [5] | Strava | Official support | Segments use matched GPS efforts and leaderboards separated by activity type. |
| [6] | Strava | Official support | Challenges motivate activity through distance, elevation, time, segment, and frequency goals. |
| [7] | Strava | Official app store | The listing describes GPS tracking, activity sharing, segments, route planning, and challenges. |
| [8] | Strava | Official app store | The listing presents Strava as a multi-sport tracking and fitness community app. |
| [9] | Nike Run Club | Official product page | Nike Run Club is a running app with guided runs, training plans, challenges, run tracking, and community motivation. |
| [10] | Nike Run Club | Official app store | The listing describes Guided Runs, Training Plans, Apple Watch support, challenges, achievements, and safety features. |
| [11] | Nike Run Club | Official app store | The listing describes GPS run tracking, Audio-Guided Runs, Training Plans, challenges, and coaching. |
| [12] | Nike Run Club | Official Nike page | Nike training plans include guided runs, mindset advice, recovery tips, and goal-oriented running schedules. |
| [13] | Nike Run Club | Official Nike help | Nike states the app features training plans created by NRC coaches for all levels of runners. |
| [14] | Nike Run Club | Official Nike help | The Run tab supports basic runs, distance or time targets, speed runs, and Guided Runs. |
| [15] | Nike Run Club | Official Nike newsroom | Nike describes localized run tips, real-time location sharing with friends and family, six training plans, and about 300 audio guided runs. |
| [16] | Nike Run Club | Official Nike page | Nike describes pace, location, distance, elevation, heart rate, mile splits, progress history, and wearable pairing. |

## Personas
### Strava personas
| ID | Name | Age | Gender | Tech | Habit | Goal | Frustration | Context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-P1 | Maya Chen | 21 | Female | High | Campus runner; three 5 km runs per week | Track pace and join monthly distance challenges | Forgets privacy settings when routes start near home | Outdoor campus loop, bright sun, phone in armband, one-handed checks |
| S-P2 | Dara Somchai | 34 | Male | Medium | Weekend cyclist | Compare segment performance and plan familiar routes | Leaderboards can feel punitive when rankings are far away | Road ride planning at home, then mid-ride glances on phone mount |
| S-P3 | Lina Pham | 46 | Female | Low-medium | Walks for health after work | Save walks privately and see progress without public pressure | Discard/save wording feels risky when tired | Evening walk, low light, sweaty hands, intermittent attention |

### Nike Run Club personas
| ID | Name | Age | Gender | Tech | Habit | Goal | Frustration | Context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N-P1 | Anh Nguyen | 19 | Male | Medium | Beginner runner, wants first 5K | Follow guided runs without planning too much | Gets confused when there are many run types and plan options | Campus road, evening run, phone in hand or armband, earphones, outdoor noise, intermittent attention |
| N-P2 | Sofia Tran | 27 | Female | High | Trains for 10K and half marathon | Follow structured plan, track pace, compare progress, keep streaks | Audio cues and achievement prompts may interrupt focus | Morning urban run, phone locked, earphones, bright sunlight, moving fast, safety concern at crossings |
| N-P3 | Minh Le | 42 | Male | Low-medium | Returns to running after long break | Run safely, avoid overtraining, share live location with family | Unsure whether live sharing, plan difficulty, and achievements match his fitness level | Night neighborhood run, low light, sweaty hands, phone in belt pouch, family wants safety updates |

## Use cases
### Strava use cases
| ID | Title | Primary persona | Step-by-step user flow | Context, preconditions, postconditions, alternate/error paths, feedback, evidence |
| --- | --- | --- | --- | --- |
| S-UC1 | Record an outdoor run | S-P1 | Open Record, wait for location confidence, start, pause/finish, review, set privacy, save. | Campus loop; evening; standing then moving; phone in armband; mobile data; traffic noise; large touch controls; evidence [2][3]. |
| S-UC2 | Create a mobile route | S-P2 | Open Maps, Create Route, choose sport, tap route points, review distance/elevation, save. | Home planning; seated; Wi-Fi; map touch; route mental model; evidence [4]. |
| S-UC3 | Compare a segment effort | S-P2 | Open activity, inspect segment match, compare rank, filter context, decide next training goal. | Post-ride review; indoor light; cognitive comparison; evidence [5]. |
| S-UC4 | Join a challenge | S-P1 | Browse challenge, inspect goal terms, join, track progress, receive completion feedback. | Monthly motivation; social pressure; evidence [6][7]. |
| S-UC5 | Edit activity privacy before sharing | S-P3 | Review activity, choose visibility, confirm audience, save, verify detail page. | Home-route privacy concern; low light; error prevention; evidence [2][3]. |

### Nike Run Club use cases
| ID | Title | Primary persona | Step-by-step user flow | Context, preconditions, postconditions, alternate/error paths, feedback, evidence |
| --- | --- | --- | --- | --- |
| N-UC1 | Start and record a free run | N-P1 | Trigger: wants a quick run. Preconditions: signed in, location permission enabled. Flow: Open Nike Run Club, Run tab, select basic run or target, press start, watch pace/distance/duration, pause/finish, review result, save. Alternate: set distance/time target first. Error path: location permission missing; app prompts permission and runner restarts. Feedback: countdown, active metrics, pause state, saved run confirmation. | Campus road; evening; standing then jogging; phone in hand or armband; cellular may vary; street noise; thumb touch; postcondition saved free run; evidence [9][11][14]. |
| N-UC2 | Start an audio-guided run | N-P1 | Trigger: wants coaching. Preconditions: headphones connected and audio available. Flow: choose Guided Run, review coach/run length, connect headphones, start run, receive coach voice and pace cues, glance at core metrics, finish, review achievements, save/share. Alternate: continue without headphones using speaker. Error path: cue missed in traffic; runner needs replay or text summary. Feedback: coach voice, elapsed time, pace cues, completion message. | Campus route; outdoor noise; fatigue; intermittent attention; evidence [9][10][11][14][15]. |
| N-UC3 | Choose and follow a training plan | N-P2 | Trigger: race preparation. Preconditions: goal distance and schedule known. Flow: open plans, choose goal, inspect weekly schedule, start plan, complete scheduled run, view progress. Alternate: edit schedule. Error path: beginner picks plan too hard and abandons; needs clearer load preview. Feedback: weekly progress, next run, completion status. | Morning urban training; phone locked during run; calendar mental model; bright sunlight; evidence [10][12][13][15]. |
| N-UC4 | Create or join a challenge | N-P2 | Trigger: wants motivation with friends. Preconditions: account and friends/community available. Flow: browse challenge, inspect goal terms and time window, join or invite friends, record runs, view progress screen, receive achievement. Alternate: private challenge. Error path: falling behind creates pressure; needs casual labels. Feedback: mileage progress, rank/status, badges. | Monthly mileage challenge; social motivation and pressure; evidence [9][10][11]. |
| N-UC5 | Share live run location and finish safely | N-P3 | Trigger: night run safety. Preconditions: location permission and chosen contacts. Flow: choose live sharing, confirm recipients and duration, start run, family receives location, finish, end sharing, confirm stopped status. Alternate: extend duration. Error path: runner is unsure who can see location; needs receipt and expiry. Feedback: sharing active indicator, stop button, finish confirmation. | Night neighborhood run; low light; sweaty hands; phone in belt pouch; family safety mental model; evidence [10][15]. |

## HCI findings
### Strava HCI findings
| ID | Screen/flow | Interface element | Observed behavior | Persona/context | HCI concept mapping | Benefit/drawback | Concrete scenario | Severity | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-HCI1 | Record screen | Start button | Large primary action supports one-handed run start | S-P1 campus run | Motor efficiency; recognition over recall; feedback | Benefit | Maya can start recording while standing at a crossing without navigating menus. | High | [2] |
| S-HCI2 | Recording flow | Save/discard controls | Destructive discard sits near completion decisions | S-P3 tired evening walk | Error prevention; user control; attention | Drawback | Lina may discard a walk after fatigue because the end state mixes save and discard choices. | High | [2] |
| S-HCI3 | Privacy selector | Everyone/Followers/Only You | Per-activity visibility can be changed before or after upload | S-P1 route starts near home | Privacy mental model; system status | Benefit | Maya can reduce exposure before saving a home-start route. | High | [3] |
| S-HCI4 | Privacy defaults | Audience wording | Multiple privacy levels require users to understand social reach | S-P3 low-tech user | Memory load; recognition over recall | Drawback | Lina may not remember whether followers include local acquaintances. | Medium | [3] |
| S-HCI5 | Route builder | Map taps and sport selector | Mobile route creation uses map interaction and sport type | S-P2 cycling plan | Spatial cognition; direct manipulation | Benefit | Dara can sketch a road ride by manipulating the map instead of typing turn-by-turn notes. | Medium | [4] |
| S-HCI6 | Route builder | Elevation/distance preview | Route previews can overload casual planners with metrics | S-P1 beginner route | Cognitive load; progressive disclosure | Drawback | Maya only needs a safe 5 km loop but faces distance, map, and route tradeoffs together. | Medium | [4] |
| S-HCI7 | Segment leaderboard | Rank table | Leaderboards show comparative performance for matched GPS efforts | S-P2 cyclist | Social comparison; motivation design | Benefit | Dara sees whether a climb effort improved relative to local riders. | Medium | [5] |
| S-HCI8 | Segment leaderboard | Broad ranking context | Large leaderboards can demotivate non-elite users | S-P1 casual runner | Satisfaction; comparison pressure | Drawback | Maya sees a low rank after a good personal run and feels the app ignored her context. | Medium | [5] |
| S-HCI9 | Challenges | Join/progress controls | Challenge progress provides visible goal feedback | S-P1 monthly run goal | Feedback; goal gradient; motivation | Benefit | Maya can see distance remaining and maintain a weekly habit. | Medium | [6][7] |
| S-HCI10 | Activity detail | Map, stats, comments | Dense post-activity detail supports review but raises attention cost | S-P3 evening review | Human vision; cognitive load | Benefit and drawback | Lina gets evidence of progress, but small labels and social controls require careful reading. | Medium | [2][7] |

### Nike Run Club HCI findings
| ID | Screen/flow | Interface element | Observed behavior | Persona/context | HCI concept mapping | Benefit/drawback | Concrete scenario | Severity | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N-HCI1 | Start Run screen | Large start action | A clear primary start action supports quick free-run recording | N-P1 campus road, one hand | Motor efficiency; recognition over recall; feedback | Benefit | Anh can begin a basic run outside without planning a workout first. | High | [11][14] |
| N-HCI2 | Run metrics screen | Pace, distance, duration, heart rate or splits where supported | Dense running metrics support progress checks but can compete with road attention | N-P2 bright urban run | Human vision; attention; cognitive load | Benefit and risk | Sofia glances for pace at speed, but reading too many values near a crossing can distract her. | High | [16] |
| N-HCI3 | Guided Runs | Coach voice | Audio-guided runs reduce visual demand and provide situated coaching | N-P1 beginner run | Auditory feedback; reduced visual demand; situated coaching | Benefit | Anh keeps eyes on the road while hearing when to relax, speed up, or finish. | High | [9][10][11][14][15] |
| N-HCI4 | Audio cues | Cue timing and voice prompts | Cues can be missed when fatigue, music, or traffic masks speech | N-P2 noisy street | Hearing limitation; split attention; interruption cost | Drawback | Sofia misses a pace cue beside traffic and has no low-effort way to recover it. | Medium | [10][11][15] |
| N-HCI5 | Training plans | Plan list and goal selection | Plans give structure but can overload beginners choosing distance, schedule, and intensity | N-P1 first 5K | Mental model; progressive disclosure; choice overload | Benefit and drawback | Anh wants one first-5K path but must interpret plan options and weekly commitment. | Medium | [12][13][15] |
| N-HCI6 | Challenges | Challenge browse/join/progress | Community challenges motivate mileage but can create comparison pressure | N-P2 monthly challenge | Social motivation; comparison pressure; motivation design | Benefit and drawback | Sofia joins friends, then feels pressure after missing runs during recovery. | Medium | [9][10][11] |
| N-HCI7 | Achievements and streaks | Badges and streak feedback | Achievements reinforce progress but can overvalue extrinsic reward | N-P3 return to running | Feedback; motivation; extrinsic reward risk | Benefit and drawback | Minh likes a first-week badge, but a broken streak can discourage needed rest. | Medium | [10][11] |
| N-HCI8 | Live location sharing | Sharing active state | Real-time sharing supports safety and trust during outdoor runs | N-P3 night run | Visibility of system status; safety; trust | Benefit | Minh can let family track his route while he runs in low light. | High | [10][15] |
| N-HCI9 | Live sharing setup | Recipients, duration, stop confirmation | Sharing setup can create privacy uncertainty if audience and expiry are not salient | N-P3 night run | Privacy mental model; error prevention; system status | Drawback | Minh is unsure who sees location and whether sharing stops when the run ends. | High | [10][15] |
| N-HCI10 | Apple Watch support | Cross-device run start/review | Optional Apple Watch support improves glanceability but needs consistent mode visibility across devices | N-P2 phone locked | Cross-device consistency; glanceability; mode visibility | Benefit and drawback | Sofia can start or monitor a run with less phone handling, then review details later on the phone. | Medium | [10][16] |

## Benefits inventory
### Strava benefits
| ID | Benefit | Why it helps | HCI link |
| --- | --- | --- | --- |
| S-B1 | Fast mobile recording | Large record/start path reduces setup time. | S-HCI1 |
| S-B2 | Privacy control | Per-activity visibility supports sensitive routes. | S-HCI3 |
| S-B3 | Route planning | Map interaction supports spatial planning. | S-HCI5 |
| S-B4 | Segment feedback | Leaderboards provide concrete performance comparison. | S-HCI7 |
| S-B5 | Challenge progress | Goal feedback makes effort visible over time. | S-HCI9 |

### Nike Run Club benefits
| ID | Benefit | Why it helps | HCI link |
| --- | --- | --- | --- |
| N-B1 | Beginner-friendly start | A simple start flow supports first-run confidence. | N-HCI1 |
| N-B2 | Audio coaching | Voice guidance lowers visual demand during motion. | N-HCI3 |
| N-B3 | Structured plans | Plans convert race goals into weekly action. | N-HCI5 |
| N-B4 | Community challenges | Challenges create social accountability. | N-HCI6 |
| N-B5 | Safety sharing | Live location sharing increases trust for night runs. | N-HCI8 |

## Drawback inventory and difficulty matrix
### Strava drawbacks
| ID | Drawback | Concrete context | HCI evidence | Severity |
| --- | --- | --- | --- | --- |
| S-D1 | Irrecoverable discard risk | End-of-activity decisions can cause accidental data loss. | S-HCI2 | High |
| S-D2 | Privacy audience uncertainty | Users may not understand who can see a sensitive route. | S-HCI4 | High |
| S-D3 | Route planning overload | Map, sport, distance, and elevation choices can overload casual users. | S-HCI6 | Medium |
| S-D4 | Leaderboard pressure | Broad rankings can demotivate personal-progress users. | S-HCI8 | Medium |
| S-D5 | Post-activity detail density | Stats, map, comments, and sharing controls compete for attention. | S-HCI10 | Medium |

### Nike Run Club drawbacks
| ID | Drawback | Concrete context | HCI evidence | Severity |
| --- | --- | --- | --- | --- |
| N-D1 | Audio-guided run cues may be missed in noisy outdoor contexts. | Traffic noise, earphone issues, music playback, and fatigue can mask instructions for Anh, Sofia, and Minh. | N-HCI4 | Medium |
| N-D2 | Training plan selection may overload beginners. | First 5K, return-from-break, and low-confidence contexts can make plan choice feel risky for Anh and Minh. | N-HCI5 | Medium |
| N-D3 | Challenge and achievement mechanics may pressure casual users. | Falling behind a challenge, streak loss, and rest-day anxiety can reduce motivation for Anh and Minh. | N-HCI6/N-HCI7 | Medium |
| N-D4 | Live location sharing may create privacy uncertainty. | Night-run safety sharing can create uncertainty about duration and recipients for Sofia and Minh. | N-HCI9 | High |
| N-D5 | During-run metric density may distract runners in motion. | Bright sunlight, fast pace, road crossings, and sweaty hands can make metric inspection unsafe for Sofia and Anh. | N-HCI2 | Medium |

## Cross-product comparison: Strava vs Nike Run Club
| Dimension | Strava | Nike Run Club |
| --- | --- | --- |
| Sports scope | Multi-sport tracking for running, cycling, walking, and route/segment culture [1][7][8]. | Running-specific coaching and run recording [9][10][11]. |
| Target users | Athletes and casual users who value sharing, routes, segments, and challenges. | Beginner to race-focused runners who value guidance, plans, achievements, and safety sharing. |
| Recording flow | Record -> location ready -> start -> finish -> privacy -> save [2][3]. | Run tab or Guided Run -> start -> metrics/audio -> finish -> achievements/save [10][11][14]. |
| Guidance style | Map, route, segment, and social feedback. | Audio-guided coaching, training plans, and run-specific prompts [12][13][15]. |
| Social feedback | Feed, challenges, and leaderboards [5][6]. | Challenges, achievements, friends, and community motivation [9][10][11]. |
| Privacy and safety | Activity visibility controls and Beacon entry points [2][3]. | Live location sharing with friends and family [10][15]. |
| Metric density | Activity details combine map, stats, segments, and comments. | Run screen and review can include pace, distance, duration, heart rate, elevation, and mile splits [16]. |
| Motivation design | Competitive segments and monthly challenges. | Guided runs, plans, achievements, streaks, and challenges. |
| Learnability | Familiar mobile map/feed conventions but privacy requires care. | Beginner coaching helps, but plan choice can overload novices. |
| Error tolerance | Privacy controls help; discard recovery needs improvement. | Audio cues help; missed cue replay and live-sharing receipt need improvement. |
| Accessibility | Large recording action helps; maps and dense details can strain vision. | Audio reduces visual demand; noisy contexts and metric density need multimodal support. |
| Context fit | Phone-carried runs, cycling, route planning, social comparison. | Phone-carried runs, guided runs, training plans, night safety sharing, optional Apple Watch support. |

## Diagrams
### Strava record activity flow
```mermaid
flowchart LR
A[Start app] --> B[Record] --> C[Location ready] --> D[Start] --> E[Pause/Finish] --> F[Review activity] --> G[Set privacy] --> H[Save] --> I[Activity detail]
```
Text fallback: Start app -> Record -> Location ready -> Start -> Pause/Finish -> Review activity -> Set privacy -> Save -> Activity detail.

### Nike Run Club audio-guided run flow
```mermaid
flowchart LR
A[Open Nike Run Club] --> B[Choose Guided Run] --> C[Connect headphones] --> D[Start run] --> E[Receive audio cues] --> F[View core metrics] --> G[Finish] --> H[Review achievements] --> I[Save/share]
```
Text fallback: Open Nike Run Club -> Choose Guided Run -> Connect headphones -> Start run -> Receive audio cues -> View core metrics -> Finish -> Review achievements -> Save/share.

## References
[1] Strava | Running, Cycling & Hiking App. Official product page. https://www.strava.com/. Accessed 2026-06-10. Supports: Strava positions itself around activity tracking, maps, performance data, and community sharing.
[2] Recording an Activity - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216917397-Recording-an-Activity. Accessed 2026-06-10. Supports: Mobile recording includes activity capture, save/discard choices, activity details, privacy controls, and Beacon entry points.
[3] Activity Privacy Controls - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919377-Activity-Privacy-Controls. Accessed 2026-06-10. Supports: Activities can use Everyone, Followers, or Only You visibility, with default and per-activity changes.
[4] Creating Routes on Mobile - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/18001474720397-Creating-Routes-on-Mobile. Accessed 2026-06-10. Supports: The mobile Maps tab and Create Route flow support route planning by sport type and map interaction.
[5] Segment Leaderboard Guidelines - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919507-Segment-Leaderboard-Guidelines. Accessed 2026-06-10. Supports: Segments use matched GPS efforts and leaderboards separated by activity type.
[6] Strava Challenges - Strava Support. Official support. https://support.strava.com/hc/en-us/articles/216919177-Strava-Challenges. Accessed 2026-06-10. Supports: Challenges motivate activity through distance, elevation, time, segment, and frequency goals.
[7] Strava: Run, Bike, Walk - App Store. Official app store. https://apps.apple.com/us/app/strava-run-bike-walk/id426826309. Accessed 2026-06-10. Supports: The listing describes GPS tracking, activity sharing, segments, route planning, and challenges.
[8] Strava: Run, Bike, Walk - Google Play. Official app store. https://play.google.com/store/apps/details?id=com.strava. Accessed 2026-06-10. Supports: The listing presents Strava as a multi-sport tracking and fitness community app.
[9] Nike Run Club App. Official product page. https://www.nike.com/nrc-app. Accessed 2026-06-10. Supports: Nike Run Club is a running app with guided runs, training plans, challenges, run tracking, and community motivation.
[10] Nike Run Club: Running Coach - App Store. Official app store. https://apps.apple.com/us/app/nike-run-club-running-coach/id387771637. Accessed 2026-06-10. Supports: The listing describes Guided Runs, Training Plans, Apple Watch support, challenges, achievements, and safety features.
[11] Nike Run Club - Running Coach - Google Play. Official app store. https://play.google.com/store/apps/details?id=com.nike.plusgps. Accessed 2026-06-10. Supports: The listing describes GPS run tracking, Audio-Guided Runs, Training Plans, challenges, and coaching.
[12] Running Training Plans. Nike.com. Official Nike page. https://www.nike.com/running/training-plans. Accessed 2026-06-10. Supports: Nike training plans include guided runs, mindset advice, recovery tips, and goal-oriented running schedules.
[13] Does the NRC App Have Training Plans? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-plan. Accessed 2026-06-10. Supports: Nike states the app features training plans created by NRC coaches for all levels of runners.
[14] How Do I Get Started in the NRC App? | Nike Help. Official Nike help. https://www.nike.com/help/a/nrc-start-run. Accessed 2026-06-10. Supports: The Run tab supports basic runs, distance or time targets, speed runs, and Guided Runs.
[15] Nike Run Club App Delivers New Features. Official Nike newsroom. https://about.nike.com/en/newsroom/releases/nike-run-club-app-new-features. Accessed 2026-06-10. Supports: Nike describes localized run tips, real-time location sharing with friends and family, six training plans, and about 300 audio guided runs.
[16] How the Nike Run Club App Can Help You Reach Your Running Goals. Official Nike page. https://www.nike.com/a/running-goals. Accessed 2026-06-10. Supports: Nike describes pace, location, distance, elevation, heart rate, mile splits, progress history, and wearable pairing.
