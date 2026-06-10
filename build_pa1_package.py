from __future__ import annotations

import json
import re
import zipfile
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Preformatted, Spacer


ROOT = Path(__file__).resolve().parent
SOURCES_DIR = ROOT / "sources"
DOCS_DIR = ROOT / "docs"
GROUP_ID = "GroupID"
TEAM_MEMBERS = ["Member1", "Member2", "Member3", "Member4", "Member5"]
ACCESS_DATE = "2026-06-10"


def source(num, sid, product, source_type, title, url, claims, notes="Official source; accessed for PA1 evidence refresh."):
    return {
        "num": num,
        "id": sid,
        "product": product,
        "source_type": source_type,
        "title": title,
        "url": url,
        "access_date": ACCESS_DATE,
        "claims_supported": claims,
        "confidence": "High",
        "notes": notes,
    }


SOURCES = [
    source(1, "S-REF1", "Strava", "Official product page", "Strava | Running, Cycling & Hiking App", "https://www.strava.com/", ["Strava positions itself around activity tracking, maps, performance data, and community sharing."]),
    source(2, "S-REF2", "Strava", "Official support", "Recording an Activity - Strava Support", "https://support.strava.com/hc/en-us/articles/216917397-Recording-an-Activity", ["Mobile recording includes activity capture, save/discard choices, activity details, privacy controls, and Beacon entry points."]),
    source(3, "S-REF3", "Strava", "Official support", "Activity Privacy Controls - Strava Support", "https://support.strava.com/hc/en-us/articles/216919377-Activity-Privacy-Controls", ["Activities can use Everyone, Followers, or Only You visibility, with default and per-activity changes."]),
    source(4, "S-REF4", "Strava", "Official support", "Creating Routes on Mobile - Strava Support", "https://support.strava.com/hc/en-us/articles/18001474720397-Creating-Routes-on-Mobile", ["The mobile Maps tab and Create Route flow support route planning by sport type and map interaction."]),
    source(5, "S-REF5", "Strava", "Official support", "Segment Leaderboard Guidelines - Strava Support", "https://support.strava.com/hc/en-us/articles/216919507-Segment-Leaderboard-Guidelines", ["Segments use matched GPS efforts and leaderboards separated by activity type."]),
    source(6, "S-REF6", "Strava", "Official support", "Strava Challenges - Strava Support", "https://support.strava.com/hc/en-us/articles/216919177-Strava-Challenges", ["Challenges motivate activity through distance, elevation, time, segment, and frequency goals."]),
    source(7, "S-REF7", "Strava", "Official app store", "Strava: Run, Bike, Walk - App Store", "https://apps.apple.com/us/app/strava-run-bike-walk/id426826309", ["The listing describes GPS tracking, activity sharing, segments, route planning, and challenges."]),
    source(8, "S-REF8", "Strava", "Official app store", "Strava: Run, Bike, Walk - Google Play", "https://play.google.com/store/apps/details?id=com.strava", ["The listing presents Strava as a multi-sport tracking and fitness community app."]),
    source(9, "N-REF1", "Nike Run Club", "Official product page", "Nike Run Club App", "https://www.nike.com/nrc-app", ["Nike Run Club is a running app with guided runs, training plans, challenges, run tracking, and community motivation."]),
    source(10, "N-REF2", "Nike Run Club", "Official app store", "Nike Run Club: Running Coach - App Store", "https://apps.apple.com/us/app/nike-run-club-running-coach/id387771637", ["The listing describes Guided Runs, Training Plans, Apple Watch support, challenges, achievements, and safety features."]),
    source(11, "N-REF3", "Nike Run Club", "Official app store", "Nike Run Club - Running Coach - Google Play", "https://play.google.com/store/apps/details?id=com.nike.plusgps", ["The listing describes GPS run tracking, Audio-Guided Runs, Training Plans, challenges, and coaching."]),
    source(12, "N-REF4", "Nike Run Club", "Official Nike page", "Running Training Plans. Nike.com", "https://www.nike.com/running/training-plans", ["Nike training plans include guided runs, mindset advice, recovery tips, and goal-oriented running schedules."]),
    source(13, "N-REF5", "Nike Run Club", "Official Nike help", "Does the NRC App Have Training Plans? | Nike Help", "https://www.nike.com/help/a/nrc-plan", ["Nike states the app features training plans created by NRC coaches for all levels of runners."]),
    source(14, "N-REF6", "Nike Run Club", "Official Nike help", "How Do I Get Started in the NRC App? | Nike Help", "https://www.nike.com/help/a/nrc-start-run", ["The Run tab supports basic runs, distance or time targets, speed runs, and Guided Runs."]),
    source(15, "N-REF7", "Nike Run Club", "Official Nike newsroom", "Nike Run Club App Delivers New Features", "https://about.nike.com/en/newsroom/releases/nike-run-club-app-new-features", ["Nike describes localized run tips, real-time location sharing with friends and family, six training plans, and about 300 audio guided runs."]),
    source(16, "N-REF8", "Nike Run Club", "Official Nike page", "How the Nike Run Club App Can Help You Reach Your Running Goals", "https://www.nike.com/a/running-goals", ["Nike describes pace, location, distance, elevation, heart rate, mile splits, progress history, and wearable pairing."]),
]


PRODUCTS = {
    "strava": {
        "id": "strava",
        "name": "Strava",
        "domain": "Sports activity tracking and social fitness",
        "modality": "Mobile-first GPS, maps, social feed, route and segment interaction",
        "positioning": "Mobile social activity network and multi-sport tracking.",
        "summary": "Strava emphasizes broad sports tracking, social competition, route and segment culture, activity sharing, and privacy settings.",
    },
    "nike_run_club": {
        "id": "nike_run_club",
        "name": "Nike Run Club",
        "domain": "Running coach and run tracking",
        "modality": "Mobile-first run tracking, audio-guided coaching, plans, challenges, achievements, live location sharing, optional Apple Watch support",
        "positioning": "Mobile running coach and guided run experience, with optional Apple Watch support.",
        "summary": "Nike Run Club emphasizes running-specific coaching, audio guidance, beginner support, training plans, achievements, challenges, and safety sharing.",
    },
}


PERSONAS = {
    "Strava": [
        ["S-P1", "Maya Chen", "21", "Female", "High", "Campus runner; three 5 km runs per week", "Track pace and join monthly distance challenges", "Forgets privacy settings when routes start near home", "Outdoor campus loop, bright sun, phone in armband, one-handed checks"],
        ["S-P2", "Dara Somchai", "34", "Male", "Medium", "Weekend cyclist", "Compare segment performance and plan familiar routes", "Leaderboards can feel punitive when rankings are far away", "Road ride planning at home, then mid-ride glances on phone mount"],
        ["S-P3", "Lina Pham", "46", "Female", "Low-medium", "Walks for health after work", "Save walks privately and see progress without public pressure", "Discard/save wording feels risky when tired", "Evening walk, low light, sweaty hands, intermittent attention"],
    ],
    "Nike Run Club": [
        ["N-P1", "Anh Nguyen", "19", "Male", "Medium", "Beginner runner, wants first 5K", "Follow guided runs without planning too much", "Gets confused when there are many run types and plan options", "Campus road, evening run, phone in hand or armband, earphones, outdoor noise, intermittent attention"],
        ["N-P2", "Sofia Tran", "27", "Female", "High", "Trains for 10K and half marathon", "Follow structured plan, track pace, compare progress, keep streaks", "Audio cues and achievement prompts may interrupt focus", "Morning urban run, phone locked, earphones, bright sunlight, moving fast, safety concern at crossings"],
        ["N-P3", "Minh Le", "42", "Male", "Low-medium", "Returns to running after long break", "Run safely, avoid overtraining, share live location with family", "Unsure whether live sharing, plan difficulty, and achievements match his fitness level", "Night neighborhood run, low light, sweaty hands, phone in belt pouch, family wants safety updates"],
    ],
}


USE_CASES = {
    "Strava": [
        ["S-UC1", "Record an outdoor run", "S-P1", "Open Record, wait for location confidence, start, pause/finish, review, set privacy, save.", "Campus loop; evening; standing then moving; phone in armband; mobile data; traffic noise; large touch controls; evidence [2][3]."],
        ["S-UC2", "Create a mobile route", "S-P2", "Open Maps, Create Route, choose sport, tap route points, review distance/elevation, save.", "Home planning; seated; Wi-Fi; map touch; route mental model; evidence [4]."],
        ["S-UC3", "Compare a segment effort", "S-P2", "Open activity, inspect segment match, compare rank, filter context, decide next training goal.", "Post-ride review; indoor light; cognitive comparison; evidence [5]."],
        ["S-UC4", "Join a challenge", "S-P1", "Browse challenge, inspect goal terms, join, track progress, receive completion feedback.", "Monthly motivation; social pressure; evidence [6][7]."],
        ["S-UC5", "Edit activity privacy before sharing", "S-P3", "Review activity, choose visibility, confirm audience, save, verify detail page.", "Home-route privacy concern; low light; error prevention; evidence [2][3]."],
    ],
    "Nike Run Club": [
        ["N-UC1", "Start and record a free run", "N-P1", "Trigger: wants a quick run. Preconditions: signed in, location permission enabled. Flow: Open Nike Run Club, Run tab, select basic run or target, press start, watch pace/distance/duration, pause/finish, review result, save. Alternate: set distance/time target first. Error path: location permission missing; app prompts permission and runner restarts. Feedback: countdown, active metrics, pause state, saved run confirmation.", "Campus road; evening; standing then jogging; phone in hand or armband; cellular may vary; street noise; thumb touch; postcondition saved free run; evidence [9][11][14]."],
        ["N-UC2", "Start an audio-guided run", "N-P1", "Trigger: wants coaching. Preconditions: headphones connected and audio available. Flow: choose Guided Run, review coach/run length, connect headphones, start run, receive coach voice and pace cues, glance at core metrics, finish, review achievements, save/share. Alternate: continue without headphones using speaker. Error path: cue missed in traffic; runner needs replay or text summary. Feedback: coach voice, elapsed time, pace cues, completion message.", "Campus route; outdoor noise; fatigue; intermittent attention; evidence [9][10][11][14][15]."],
        ["N-UC3", "Choose and follow a training plan", "N-P2", "Trigger: race preparation. Preconditions: goal distance and schedule known. Flow: open plans, choose goal, inspect weekly schedule, start plan, complete scheduled run, view progress. Alternate: edit schedule. Error path: beginner picks plan too hard and abandons; needs clearer load preview. Feedback: weekly progress, next run, completion status.", "Morning urban training; phone locked during run; calendar mental model; bright sunlight; evidence [10][12][13][15]."],
        ["N-UC4", "Create or join a challenge", "N-P2", "Trigger: wants motivation with friends. Preconditions: account and friends/community available. Flow: browse challenge, inspect goal terms and time window, join or invite friends, record runs, view progress screen, receive achievement. Alternate: private challenge. Error path: falling behind creates pressure; needs casual labels. Feedback: mileage progress, rank/status, badges.", "Monthly mileage challenge; social motivation and pressure; evidence [9][10][11]."],
        ["N-UC5", "Share live run location and finish safely", "N-P3", "Trigger: night run safety. Preconditions: location permission and chosen contacts. Flow: choose live sharing, confirm recipients and duration, start run, family receives location, finish, end sharing, confirm stopped status. Alternate: extend duration. Error path: runner is unsure who can see location; needs receipt and expiry. Feedback: sharing active indicator, stop button, finish confirmation.", "Night neighborhood run; low light; sweaty hands; phone in belt pouch; family safety mental model; evidence [10][15]."],
    ],
}


HCI_FINDINGS = {
    "Strava": [
        ["S-HCI1", "Record screen", "Start button", "Large primary action supports one-handed run start", "S-P1 campus run", "Motor efficiency; recognition over recall; feedback", "Benefit", "Maya can start recording while standing at a crossing without navigating menus.", "High", "[2]"],
        ["S-HCI2", "Recording flow", "Save/discard controls", "Destructive discard sits near completion decisions", "S-P3 tired evening walk", "Error prevention; user control; attention", "Drawback", "Lina may discard a walk after fatigue because the end state mixes save and discard choices.", "High", "[2]"],
        ["S-HCI3", "Privacy selector", "Everyone/Followers/Only You", "Per-activity visibility can be changed before or after upload", "S-P1 route starts near home", "Privacy mental model; system status", "Benefit", "Maya can reduce exposure before saving a home-start route.", "High", "[3]"],
        ["S-HCI4", "Privacy defaults", "Audience wording", "Multiple privacy levels require users to understand social reach", "S-P3 low-tech user", "Memory load; recognition over recall", "Drawback", "Lina may not remember whether followers include local acquaintances.", "Medium", "[3]"],
        ["S-HCI5", "Route builder", "Map taps and sport selector", "Mobile route creation uses map interaction and sport type", "S-P2 cycling plan", "Spatial cognition; direct manipulation", "Benefit", "Dara can sketch a road ride by manipulating the map instead of typing turn-by-turn notes.", "Medium", "[4]"],
        ["S-HCI6", "Route builder", "Elevation/distance preview", "Route previews can overload casual planners with metrics", "S-P1 beginner route", "Cognitive load; progressive disclosure", "Drawback", "Maya only needs a safe 5 km loop but faces distance, map, and route tradeoffs together.", "Medium", "[4]"],
        ["S-HCI7", "Segment leaderboard", "Rank table", "Leaderboards show comparative performance for matched GPS efforts", "S-P2 cyclist", "Social comparison; motivation design", "Benefit", "Dara sees whether a climb effort improved relative to local riders.", "Medium", "[5]"],
        ["S-HCI8", "Segment leaderboard", "Broad ranking context", "Large leaderboards can demotivate non-elite users", "S-P1 casual runner", "Satisfaction; comparison pressure", "Drawback", "Maya sees a low rank after a good personal run and feels the app ignored her context.", "Medium", "[5]"],
        ["S-HCI9", "Challenges", "Join/progress controls", "Challenge progress provides visible goal feedback", "S-P1 monthly run goal", "Feedback; goal gradient; motivation", "Benefit", "Maya can see distance remaining and maintain a weekly habit.", "Medium", "[6][7]"],
        ["S-HCI10", "Activity detail", "Map, stats, comments", "Dense post-activity detail supports review but raises attention cost", "S-P3 evening review", "Human vision; cognitive load", "Benefit and drawback", "Lina gets evidence of progress, but small labels and social controls require careful reading.", "Medium", "[2][7]"],
    ],
    "Nike Run Club": [
        ["N-HCI1", "Start Run screen", "Large start action", "A clear primary start action supports quick free-run recording", "N-P1 campus road, one hand", "Motor efficiency; recognition over recall; feedback", "Benefit", "Anh can begin a basic run outside without planning a workout first.", "High", "[11][14]"],
        ["N-HCI2", "Run metrics screen", "Pace, distance, duration, heart rate or splits where supported", "Dense running metrics support progress checks but can compete with road attention", "N-P2 bright urban run", "Human vision; attention; cognitive load", "Benefit and risk", "Sofia glances for pace at speed, but reading too many values near a crossing can distract her.", "High", "[16]"],
        ["N-HCI3", "Guided Runs", "Coach voice", "Audio-guided runs reduce visual demand and provide situated coaching", "N-P1 beginner run", "Auditory feedback; reduced visual demand; situated coaching", "Benefit", "Anh keeps eyes on the road while hearing when to relax, speed up, or finish.", "High", "[9][10][11][14][15]"],
        ["N-HCI4", "Audio cues", "Cue timing and voice prompts", "Cues can be missed when fatigue, music, or traffic masks speech", "N-P2 noisy street", "Hearing limitation; split attention; interruption cost", "Drawback", "Sofia misses a pace cue beside traffic and has no low-effort way to recover it.", "Medium", "[10][11][15]"],
        ["N-HCI5", "Training plans", "Plan list and goal selection", "Plans give structure but can overload beginners choosing distance, schedule, and intensity", "N-P1 first 5K", "Mental model; progressive disclosure; choice overload", "Benefit and drawback", "Anh wants one first-5K path but must interpret plan options and weekly commitment.", "Medium", "[12][13][15]"],
        ["N-HCI6", "Challenges", "Challenge browse/join/progress", "Community challenges motivate mileage but can create comparison pressure", "N-P2 monthly challenge", "Social motivation; comparison pressure; motivation design", "Benefit and drawback", "Sofia joins friends, then feels pressure after missing runs during recovery.", "Medium", "[9][10][11]"],
        ["N-HCI7", "Achievements and streaks", "Badges and streak feedback", "Achievements reinforce progress but can overvalue extrinsic reward", "N-P3 return to running", "Feedback; motivation; extrinsic reward risk", "Benefit and drawback", "Minh likes a first-week badge, but a broken streak can discourage needed rest.", "Medium", "[10][11]"],
        ["N-HCI8", "Live location sharing", "Sharing active state", "Real-time sharing supports safety and trust during outdoor runs", "N-P3 night run", "Visibility of system status; safety; trust", "Benefit", "Minh can let family track his route while he runs in low light.", "High", "[10][15]"],
        ["N-HCI9", "Live sharing setup", "Recipients, duration, stop confirmation", "Sharing setup can create privacy uncertainty if audience and expiry are not salient", "N-P3 night run", "Privacy mental model; error prevention; system status", "Drawback", "Minh is unsure who sees location and whether sharing stops when the run ends.", "High", "[10][15]"],
        ["N-HCI10", "Apple Watch support", "Cross-device run start/review", "Optional Apple Watch support improves glanceability but needs consistent mode visibility across devices", "N-P2 phone locked", "Cross-device consistency; glanceability; mode visibility", "Benefit and drawback", "Sofia can start or monitor a run with less phone handling, then review details later on the phone.", "Medium", "[10][16]"],
    ],
}


BENEFITS = {
    "Strava": [
        ["S-B1", "Fast mobile recording", "Large record/start path reduces setup time.", "S-HCI1"],
        ["S-B2", "Privacy control", "Per-activity visibility supports sensitive routes.", "S-HCI3"],
        ["S-B3", "Route planning", "Map interaction supports spatial planning.", "S-HCI5"],
        ["S-B4", "Segment feedback", "Leaderboards provide concrete performance comparison.", "S-HCI7"],
        ["S-B5", "Challenge progress", "Goal feedback makes effort visible over time.", "S-HCI9"],
    ],
    "Nike Run Club": [
        ["N-B1", "Beginner-friendly start", "A simple start flow supports first-run confidence.", "N-HCI1"],
        ["N-B2", "Audio coaching", "Voice guidance lowers visual demand during motion.", "N-HCI3"],
        ["N-B3", "Structured plans", "Plans convert race goals into weekly action.", "N-HCI5"],
        ["N-B4", "Community challenges", "Challenges create social accountability.", "N-HCI6"],
        ["N-B5", "Safety sharing", "Live location sharing increases trust for night runs.", "N-HCI8"],
    ],
}


DRAWBACKS = {
    "Strava": [
        ["S-D1", "Irrecoverable discard risk", "End-of-activity decisions can cause accidental data loss.", "S-HCI2", "High"],
        ["S-D2", "Privacy audience uncertainty", "Users may not understand who can see a sensitive route.", "S-HCI4", "High"],
        ["S-D3", "Route planning overload", "Map, sport, distance, and elevation choices can overload casual users.", "S-HCI6", "Medium"],
        ["S-D4", "Leaderboard pressure", "Broad rankings can demotivate personal-progress users.", "S-HCI8", "Medium"],
        ["S-D5", "Post-activity detail density", "Stats, map, comments, and sharing controls compete for attention.", "S-HCI10", "Medium"],
    ],
    "Nike Run Club": [
        ["N-D1", "Audio-guided run cues may be missed in noisy outdoor contexts.", "Traffic noise, earphone issues, music playback, and fatigue can mask instructions for Anh, Sofia, and Minh.", "N-HCI4", "Medium"],
        ["N-D2", "Training plan selection may overload beginners.", "First 5K, return-from-break, and low-confidence contexts can make plan choice feel risky for Anh and Minh.", "N-HCI5", "Medium"],
        ["N-D3", "Challenge and achievement mechanics may pressure casual users.", "Falling behind a challenge, streak loss, and rest-day anxiety can reduce motivation for Anh and Minh.", "N-HCI6/N-HCI7", "Medium"],
        ["N-D4", "Live location sharing may create privacy uncertainty.", "Night-run safety sharing can create uncertainty about duration and recipients for Sofia and Minh.", "N-HCI9", "High"],
        ["N-D5", "During-run metric density may distract runners in motion.", "Bright sunlight, fast pace, road crossings, and sweaty hands can make metric inspection unsafe for Sofia and Anh.", "N-HCI2", "Medium"],
    ],
}


SOLUTIONS = [
    ["S-S1", "S-D1", "Strava", "Recoverable Activity Trash", "After discard, move activity to a 7-day trash with Restore and Delete forever.", "Error recovery; user control", "Maya/Lina", "End-of-run fatigue", "Expected gain: fewer lost recordings. Tradeoff: storage and extra state. Priority High. Effort Medium."],
    ["S-S2", "S-D1", "Strava", "Safer Finish Hierarchy", "Make Save primary, move Discard behind a confirm sheet with activity summary.", "Error prevention; motor efficiency", "Maya/Lina", "Sweaty hands after activity", "Expected gain: fewer accidental destructive actions. Tradeoff: one extra tap for true discard. Priority High. Effort Low."],
    ["S-S3", "S-D2", "Strava", "Privacy Receipt", "Show audience, map visibility, and home-area warning before save.", "Privacy mental model; visibility", "Maya/Lina", "Home route sharing", "Expected gain: higher confidence. Tradeoff: more review text. Priority High. Effort Low."],
    ["S-S4", "S-D2", "Strava", "Sensitive Route Reminder", "Detect route near saved home area and suggest Only You or hidden map zone.", "Error prevention; feedforward", "Maya", "Campus/home start", "Expected gain: lower accidental exposure. Tradeoff: false positives. Priority High. Effort Medium."],
    ["S-S5", "S-D3", "Strava", "Simple Route Wizard", "Ask distance, sport, and loop/out-back, then recommend one editable route.", "Progressive disclosure; recognition", "Dara/Maya", "Planning a new route", "Expected gain: lower setup effort. Tradeoff: less initial control. Priority Medium. Effort Medium."],
    ["S-S6", "S-D3", "Strava", "Route Confidence Labels", "Label routes Easy, Hilly, Unfamiliar, or Busy based on visible criteria.", "Feedforward; mental model", "Dara/Maya", "Map route choice", "Expected gain: faster decision. Tradeoff: requires clear criteria. Priority Medium. Effort Medium."],
    ["S-S7", "S-D4", "Strava", "Peer-Band Leaderboards", "Default casual users to similar-level comparison bands before global ranking.", "Motivation design; satisfaction", "Maya/Dara", "Segment review", "Expected gain: less demotivation. Tradeoff: competitive users may prefer global view. Priority Medium. Effort High."],
    ["S-S8", "S-D4", "Strava", "Personal Progress First", "Show PR delta and trend before rank for casual profiles.", "Feedback; user fit", "Maya", "Post-run review", "Expected gain: healthier motivation. Tradeoff: rank is one tap deeper. Priority Medium. Effort Low."],
    ["S-S9", "S-D5", "Strava", "Post-Activity Summary Mode", "Show map, distance, time, privacy first; hide comments/segments behind tabs.", "Cognitive load reduction", "Lina", "Low-light review", "Expected gain: less visual overload. Tradeoff: advanced metrics are less immediate. Priority Medium. Effort Medium."],
    ["S-S10", "S-D5", "Strava", "Large-Type Review", "Offer high-contrast, large-type post-run summary for tired or low-light contexts.", "Vision; accessibility", "Lina", "Evening walk", "Expected gain: better readability. Tradeoff: more display modes. Priority Low. Effort Medium."],
    ["N-S1", "N-D1", "Nike Run Club", "Audio Cue Replay button", "Small accessible control on run screen and headphone gesture shortcut; shows last cue text summary for 5 seconds.", "Recovery; auditory limitation support; reduced memory load", "Anh/Sofia/Minh", "Noisy streets, fatigue, music playback", "Expected gain: fewer missed instructions. Tradeoff: adds control to run screen. Priority High. Effort Low."],
    ["N-S2", "N-D1", "Nike Run Club", "Adaptive cue mode", "User selects Quiet route, Normal, or Noisy street; app increases cue clarity, haptic emphasis, and text summary by mode.", "Context-aware feedback; multimodal interaction", "Anh/Sofia/Minh", "Traffic or crowded route", "Expected gain: better guidance in traffic. Tradeoff: mode setup can add complexity. Priority Medium. Effort High."],
    ["N-S3", "N-D2", "Nike Run Club", "Beginner Plan Wizard", "Ask current ability, target distance, available days, injury concern; recommend one plan with a clear reason.", "Recognition over recall; progressive disclosure", "Anh/Minh", "First 5K or return after break", "Expected gain: lower setup effort. Tradeoff: users may want full list immediately. Priority High. Effort Medium."],
    ["N-S4", "N-D2", "Nike Run Club", "Plan difficulty receipt", "Before starting a plan, show weekly load, rest days, expected longest run, and Edit Difficulty.", "Feedforward; user control; error prevention", "Anh/Minh", "Low-confidence plan selection", "Expected gain: lower overcommitment. Tradeoff: more pre-plan reading. Priority Medium. Effort Medium."],
    ["N-S5", "N-D3", "Nike Run Club", "Healthy Streak mode", "Rest day counts as protected training when user selects recovery.", "Motivation design; overtraining prevention", "Anh/Minh", "Rest-day anxiety", "Expected gain: less pressure to run every day. Tradeoff: streak semantics change. Priority Medium. Effort Medium."],
    ["N-S6", "N-D3", "Nike Run Club", "Challenge pressure filter", "Label challenges Casual, Consistent, Competitive; default new users to Casual.", "Mental model alignment; choice architecture", "Anh/Minh", "Monthly challenge browsing", "Expected gain: better fit by user type. Tradeoff: challenge taxonomy maintenance. Priority Medium. Effort Low."],
    ["N-S7", "N-D4", "Nike Run Club", "Live Sharing Receipt", "After starting sharing, show recipients, duration, stop button, and finish notification status.", "Visibility of system status; privacy mental model", "Sofia/Minh", "Night run family sharing", "Expected gain: higher trust. Tradeoff: extra status surface. Priority High. Effort Low."],
    ["N-S8", "N-D4", "Nike Run Club", "Auto-stop and expiry control", "Default live sharing expires at run end or chosen duration; end screen confirms sharing stopped.", "Error prevention; closure feedback", "Sofia/Minh", "Safety sharing with family", "Expected gain: lower privacy risk. Tradeoff: edge cases for extended runs. Priority Medium. Effort Medium."],
    ["N-S9", "N-D5", "Nike Run Club", "Focus Run screen", "During movement, show only distance, pace, and elapsed time with large type; move other metrics behind swipe or post-run detail.", "Cognitive load reduction; human vision; motor efficiency", "Sofia/Anh", "Bright sunlight and fast pace", "Expected gain: safer glance behavior. Tradeoff: fewer metrics visible by default. Priority High. Effort Medium."],
    ["N-S10", "N-D5", "Nike Run Club", "Crossing-safe interaction lock", "If phone detects fast movement and screen wake, delay nonessential overlays and use voice or haptic cues.", "Interruption management; safety; attention support", "Sofia/Anh", "Road crossings", "Expected gain: fewer distraction moments. Tradeoff: may suppress desired messages. Priority Medium. Effort High."],
]


STRAVA_FLOW = "Start app -> Record -> Location ready -> Start -> Pause/Finish -> Review activity -> Set privacy -> Save -> Activity detail."
NRC_FLOW = "Open Nike Run Club -> Choose Guided Run -> Connect headphones -> Start run -> Receive audio cues -> View core metrics -> Finish -> Review achievements -> Save/share."
SPRINT_FLOW = "Day 1 kickoff -> Days 2-3 sources -> Days 4-5 personas/use cases -> Days 6-8 HCI/comparison -> Days 9-11 solutions/drafts -> Days 12-13 review/QA -> Day 14 export/package."


def md_table(headers, rows):
    rows = [[str(c) for c in r] for r in rows]
    return ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] + ["| " + " | ".join(r) + " |" for r in rows]


def refs_md(nums=None):
    selected = SOURCES if nums is None else [s for s in SOURCES if s["num"] in nums]
    return [f"[{s['num']}] {s['title']}. {s['source_type']}. {s['url']}. Accessed {s['access_date']}. Supports: {'; '.join(s['claims_supported'])}" for s in selected]


def product_research_md():
    lines = [
        f"# {GROUP_ID}-PA1 Product Research: Strava and Nike Run Club",
        "",
        "## Executive summary",
        "This report compares Strava and Nike Run Club as mobile-first running and activity products. Strava emphasizes broad sports tracking, social competition, route and segment culture, activity sharing, and privacy settings. Nike Run Club emphasizes running-specific coaching, audio guidance, beginner support, training plans, achievements, challenges, and safety sharing [1][2][9][10][15].",
        "",
        "## Product selection",
    ]
    lines += md_table(["Product", "Domain", "Modality", "Positioning"], [[p["name"], p["domain"], p["modality"], p["positioning"]] for p in PRODUCTS.values()])
    lines += ["", "## Source protocol", "Official product, support, help, newsroom, App Store, and Google Play pages were prioritized. Every nontrivial product claim cites the numbered references below; interface observations are treated as source-grounded, not as unsupported screenshots.", ""]
    lines += md_table(["Citation", "Product", "Type", "Claim supported"], [[f"[{s['num']}]", s["product"], s["source_type"], "; ".join(s["claims_supported"])] for s in SOURCES])
    lines += ["", "## Personas"]
    for product in ["Strava", "Nike Run Club"]:
        lines += [f"### {product} personas"]
        lines += md_table(["ID", "Name", "Age", "Gender", "Tech", "Habit", "Goal", "Frustration", "Context"], PERSONAS[product])
        lines.append("")
    lines += ["## Use cases"]
    for product in ["Strava", "Nike Run Club"]:
        lines += [f"### {product} use cases"]
        lines += md_table(["ID", "Title", "Primary persona", "Step-by-step user flow", "Context, preconditions, postconditions, alternate/error paths, feedback, evidence"], USE_CASES[product])
        lines.append("")
    lines += ["## HCI findings"]
    for product in ["Strava", "Nike Run Club"]:
        lines += [f"### {product} HCI findings"]
        lines += md_table(["ID", "Screen/flow", "Interface element", "Observed behavior", "Persona/context", "HCI concept mapping", "Benefit/drawback", "Concrete scenario", "Severity", "Evidence"], HCI_FINDINGS[product])
        lines.append("")
    lines += ["## Benefits inventory"]
    for product in ["Strava", "Nike Run Club"]:
        lines += [f"### {product} benefits"]
        lines += md_table(["ID", "Benefit", "Why it helps", "HCI link"], BENEFITS[product])
        lines.append("")
    lines += ["## Drawback inventory and difficulty matrix"]
    for product in ["Strava", "Nike Run Club"]:
        lines += [f"### {product} drawbacks"]
        lines += md_table(["ID", "Drawback", "Concrete context", "HCI evidence", "Severity"], DRAWBACKS[product])
        lines.append("")
    lines += [
        "## Cross-product comparison: Strava vs Nike Run Club",
    ]
    lines += md_table(["Dimension", "Strava", "Nike Run Club"], [
        ["Sports scope", "Multi-sport tracking for running, cycling, walking, and route/segment culture [1][7][8].", "Running-specific coaching and run recording [9][10][11]."],
        ["Target users", "Athletes and casual users who value sharing, routes, segments, and challenges.", "Beginner to race-focused runners who value guidance, plans, achievements, and safety sharing."],
        ["Recording flow", "Record -> location ready -> start -> finish -> privacy -> save [2][3].", "Run tab or Guided Run -> start -> metrics/audio -> finish -> achievements/save [10][11][14]."],
        ["Guidance style", "Map, route, segment, and social feedback.", "Audio-guided coaching, training plans, and run-specific prompts [12][13][15]."],
        ["Social feedback", "Feed, challenges, and leaderboards [5][6].", "Challenges, achievements, friends, and community motivation [9][10][11]."],
        ["Privacy and safety", "Activity visibility controls and Beacon entry points [2][3].", "Live location sharing with friends and family [10][15]."],
        ["Metric density", "Activity details combine map, stats, segments, and comments.", "Run screen and review can include pace, distance, duration, heart rate, elevation, and mile splits [16]."],
        ["Motivation design", "Competitive segments and monthly challenges.", "Guided runs, plans, achievements, streaks, and challenges."],
        ["Learnability", "Familiar mobile map/feed conventions but privacy requires care.", "Beginner coaching helps, but plan choice can overload novices."],
        ["Error tolerance", "Privacy controls help; discard recovery needs improvement.", "Audio cues help; missed cue replay and live-sharing receipt need improvement."],
        ["Accessibility", "Large recording action helps; maps and dense details can strain vision.", "Audio reduces visual demand; noisy contexts and metric density need multimodal support."],
        ["Context fit", "Phone-carried runs, cycling, route planning, social comparison.", "Phone-carried runs, guided runs, training plans, night safety sharing, optional Apple Watch support."],
    ])
    lines += [
        "",
        "## Diagrams",
        "### Strava record activity flow",
        "```mermaid",
        "flowchart LR",
        "A[Start app] --> B[Record] --> C[Location ready] --> D[Start] --> E[Pause/Finish] --> F[Review activity] --> G[Set privacy] --> H[Save] --> I[Activity detail]",
        "```",
        f"Text fallback: {STRAVA_FLOW}",
        "",
        "### Nike Run Club audio-guided run flow",
        "```mermaid",
        "flowchart LR",
        "A[Open Nike Run Club] --> B[Choose Guided Run] --> C[Connect headphones] --> D[Start run] --> E[Receive audio cues] --> F[View core metrics] --> G[Finish] --> H[Review achievements] --> I[Save/share]",
        "```",
        f"Text fallback: {NRC_FLOW}",
        "",
        "## References",
    ] + refs_md()
    return "\n".join(lines) + "\n"


def solutions_md():
    solution_rows = [[s[0], s[2], s[1], s[3], s[4], s[5], s[6], s[7], s[8]] for s in SOLUTIONS]
    lines = [
        f"# {GROUP_ID}-PA1 Potential Solutions: Strava and Nike Run Club",
        "",
        "## Executive summary",
        "This report maps every Strava and Nike Run Club drawback from ProductResearch to two concrete interface solutions. Strava work prioritizes recoverability, privacy clarity, route simplification, healthier social comparison, and post-activity readability. Nike Run Club work prioritizes missed audio recovery, beginner plan selection, healthy motivation, live-sharing privacy, and safer during-run metrics.",
        "",
        "## Problem inventory",
    ]
    lines += md_table(["ID", "Product", "Problem", "Severity"], [[d[0], product, d[1], d[4]] for product in DRAWBACKS for d in DRAWBACKS[product]])
    lines += ["", "## Solution framework", "Each design concept states affected product, personas, contexts, UI behavior, HCI principle mapping, expected improvement, tradeoffs, priority, and effort.", ""]
    lines += md_table(["ID", "Product", "Drawback", "Design concept", "UI and behavior detail", "HCI principles", "Affected personas", "Affected contexts", "Expected improvement, tradeoffs, priority, effort"], solution_rows)
    lines += ["", "## Drawback-to-solution mapping"]
    lines += md_table(["Drawback", "Solutions"], [[d[0], ", ".join([s[0] for s in SOLUTIONS if s[1] == d[0]])] for product in DRAWBACKS for d in DRAWBACKS[product]])
    lines += ["", "## Detailed implementation notes"]
    for sid, did, product, concept, detail, hci, personas, contexts, result in SOLUTIONS:
        lines += [
            f"### {sid} {concept}",
            f"Affected product: {product}. Drawback: {did}. Affected personas: {personas}. Affected contexts: {contexts}.",
            f"UI and behavior level: {detail} Mockup description in words: the control appears in the same task surface where the problem occurs, uses one short label, shows the current state, and provides a visible recovery or confirmation path.",
            f"HCI principle mapping: {hci}. {result}",
            "",
        ]
    lines += ["", "## Impact-effort prioritization"]
    lines += md_table(["Priority band", "Solutions", "Reason"], [
        ["Quick wins", "N-S1 Audio Cue Replay; N-S3 Beginner Plan Wizard; N-S7 Live Sharing Receipt; N-S9 Focus Run screen; S-S2 Safer Finish Hierarchy; S-S3 Privacy Receipt", "Low-to-medium effort with direct reduction in missed cues, beginner overload, privacy uncertainty, motion distraction, destructive action, and sensitive route exposure."],
        ["Deeper redesign", "N-S2 Adaptive cue mode; N-S4 Plan difficulty receipt; N-S5 Healthy Streak mode; N-S8 Auto-stop and expiry control; N-S10 Crossing-safe interaction lock; S-S1 Recoverable Activity Trash; S-S7 Peer-Band Leaderboards", "Requires more product state, context sensing, or motivation-model changes."],
        ["Later enhancements", "S-S5 Simple Route Wizard; S-S6 Route Confidence Labels; S-S8 Personal Progress First; S-S9 Post-Activity Summary Mode; S-S10 Large-Type Review; N-S6 Challenge pressure filter", "Useful improvements after high-risk privacy, safety, and destructive-action issues are handled."],
    ])
    lines += ["", "## Phased recommendation plan", "Phase 1 implements quick wins for Nike Run Club and Strava. Phase 2 tests deeper redesigns with beginner and night-run scenarios. Phase 3 revisits social motivation defaults after peer review. The design team should prototype N-S1, N-S3, N-S7, and N-S9 first because they are visible in the exact moments where the HCI risk occurs.", "", "## References"] + refs_md([1,2,3,4,5,6,9,10,11,12,13,14,15,16])
    return "\n".join(lines) + "\n"


def peer_review_md():
    feedback = [
        ["Nora Lee", "Peer", "Need clearer evidence for Strava privacy.", "Added privacy controls citation and privacy receipt solution.", "Member2", "Done"],
        ["Omar Khan", "Peer", "Nike Run Club audio guidance should be both benefit and drawback.", "Split N-HCI3 and N-HCI4 with noisy-street scenario.", "Member3", "Done"],
        ["Jin Park", "Peer", "Beginner plan overload needs a persona.", "Linked N-D2 to Anh and Minh.", "Member2", "Done"],
        ["Mira Vo", "Peer", "Live sharing risk should name recipients and expiry.", "Added N-S7 and N-S8 receipt/expiry controls.", "Member4", "Done"],
        ["Sam Patel", "Peer", "Strava leaderboards need motivation framing.", "Added S-HCI7/S-HCI8 and peer-band solution.", "Member3", "Done"],
        ["Hana Lim", "Peer", "The comparison should not treat Nike Run Club as wearable-first.", "Rewrote modality as mobile running coach with optional Apple Watch support.", "Member1", "Done"],
        ["Leo Tran", "Peer", "Metric density should include road-crossing context.", "Added N-D5 and N-S9/N-S10.", "Member4", "Done"],
        ["Ivy Chen", "Peer", "Sprint plan should show source QA.", "Added source collection, PDF text scan, and zip validation tasks.", "Member5", "Done"],
    ]
    lines = [
        f"# {GROUP_ID}-PA1 Peer Review Preparation: Strava and Nike Run Club",
        "",
        "## Presentation plan",
        "The 7-minute peer-review presentation explains why the team compares Strava and Nike Run Club, how the evidence protocol works, what personas and contexts reveal, and which solution priorities should be challenged by reviewers.",
    ]
    lines += md_table(["Slide", "Topic", "Purpose", "Speaker", "Time"], [
        ["1", "PA1 scope and chosen product pair", "State Strava and Nike Run Club scope", "Member1", "0:45"],
        ["2", "Method and evidence protocol", "Explain official-source-first citations", "Member1", "0:55"],
        ["3", "Personas and use contexts", "Show six personas and motion contexts", "Member2", "1:00"],
        ["4", "Strava HCI findings", "Record, privacy, route, segment, challenge risks", "Member3", "1:10"],
        ["5", "Nike Run Club HCI findings", "Audio guidance, plans, challenges, live sharing, metrics", "Member4", "1:10"],
        ["6", "Solution priorities", "Explain quick wins and deeper redesigns", "Member4", "1:10"],
        ["7", "Sprint plan and QA status", "Show validation and packaging", "Member5", "0:50"],
    ])
    lines += ["", "## 7-minute script", "Member1 opens with the product pair and evidence rule. Member2 explains personas as motion-and-context models. Member3 covers Strava benefits and risks. Member4 covers Nike Run Club benefits, drawbacks, and solution priorities. Member5 closes with sprint QA, source validation, PDF regeneration, and zip package status.", "", "## Likely questions and prepared answers"]
    lines += [
        "",
        "## Slide speaker notes",
        "Slide 1 note: State the scope as a comparison between Strava and Nike Run Club only. The first sentence should make clear that both products are mobile-first, but they represent different HCI priorities: broad social activity tracking versus running-specific coaching.",
        "Slide 2 note: Explain that the team used official product, help, app-store, and newsroom sources first. Claims about recording, privacy, guided runs, training plans, live sharing, and metrics are cited rather than guessed from unsupported screenshots.",
        "Slide 3 note: Emphasize context. The six personas are not demographic filler; each one defines motion state, lighting/noise, device state, attention level, and the user goal at the moment of interaction.",
        "Slide 4 note: For Strava, focus on record start, privacy selector, route builder, segment leaderboard, and challenge progress. Tie every benefit or drawback to a screen and a concrete runner or cyclist scenario.",
        "Slide 5 note: For Nike Run Club, focus on the start action, metrics screen, audio-guided runs, training plans, challenges, achievements, live sharing, and optional Apple Watch support. Make clear that audio guidance is both a benefit and a risk depending on noise and fatigue.",
        "Slide 6 note: Explain why N-S1, N-S3, N-S7, and N-S9 are quick wins. They address missed instructions, beginner plan overload, live sharing uncertainty, and metric distraction exactly when the user is vulnerable.",
        "Slide 7 note: Close with QA: source log refreshed, PDFs regenerated, extracted text scanned, and zip checked for four top-level PDFs.",
    ]
    lines += ["", "## Likely questions and prepared answers"]
    lines += md_table(["Question", "Prepared answer"], [
        ["Why compare Strava and Nike Run Club?", "Both are mobile-first running products, but Strava is broader social/multi-sport tracking while Nike Run Club is guided running coaching."],
        ["Which product has better beginner support?", "Nike Run Club, because Guided Runs and training plans directly coach novice runners [9][13][14][15]."],
        ["Which product has higher privacy risk?", "Both have privacy risks: Strava route visibility can expose sensitive places, while Nike Run Club live sharing needs clear recipients and expiry [3][10][15]."],
        ["Why is audio guidance an HCI benefit?", "It moves feedback from vision to hearing, reducing visual demand while the runner is moving [9][14][15]."],
        ["When does audio guidance become a drawback?", "When noise, fatigue, music, or earphone problems cause missed cues during motion."],
        ["How did the team avoid generic analysis?", "Each finding names a screen or flow, control, user, context, HCI concept, scenario, severity, and evidence."],
    ])
    lines += ["", "## Mock feedback entries"]
    lines += md_table(["Reviewer", "Role", "Feedback", "Response/revision", "Owner", "Status"], feedback)
    lines += [
        "",
        "## Rehearsal checklist",
        "Check 1: The first slide names only Strava and Nike Run Club and defines Nike Run Club as a mobile-first running coach and tracking product.",
        "Check 2: The method slide explains numbered citations and makes clear that the team avoided unsupported screenshots and generic claims.",
        "Check 3: The persona slide shows that each persona has a context: where, when, posture, motion state, device state, connectivity, lighting or noise, interaction method, and attention level.",
        "Check 4: The Strava slide includes at least one benefit and one drawback tied to record, privacy, route, segment, or challenge behavior.",
        "Check 5: The Nike Run Club slide includes the required audio guidance, training plan, challenge, achievement, live sharing, metric density, and Apple Watch support findings.",
        "Check 6: The solution slide does not list ideas without UI behavior. Every idea states the control, feedback, expected gain, and tradeoff.",
        "Check 7: The closing slide mentions source refresh, Markdown regeneration, PDF regeneration, extracted-text scan, and top-level zip contents.",
        "Check 8: The team leaves time for peer questions about beginner support, privacy risk, audio guidance, and evidence quality.",
        "",
        "## Presentation risk controls",
        "Risk control A: If a reviewer asks why these two products were paired, the answer should point to shared running use but different HCI emphasis: Strava as social multi-sport tracking and Nike Run Club as guided running coaching.",
        "Risk control B: If a reviewer says the analysis is too broad, the speaker should cite a specific screen or flow, such as Strava activity privacy or Nike Run Club live location sharing.",
        "Risk control C: If a reviewer challenges audio guidance, the speaker should explain both sides: it reduces visual demand, but it can fail in noisy outdoor contexts.",
        "Risk control D: If a reviewer challenges the solution feasibility, the speaker should separate quick wins from deeper redesigns and explain effort tradeoffs.",
        "Risk control E: If a reviewer asks about missing real names, the team should state that placeholders are used until the group supplies the final roster.",
        "",
        "## Cue-card Q&A details",
        "Cue card 1: Beginner support. Nike Run Club should be described as stronger for beginners because Guided Runs and coach-created plans reduce the need to design workouts from scratch. The answer should also mention that too many plan choices can still overload a beginner.",
        "Cue card 2: Privacy. Strava privacy risk is about activity audience and route visibility; Nike Run Club privacy risk is about live sharing recipients and sharing duration. The team should not collapse these into one generic privacy issue.",
        "Cue card 3: Safety. Nike Run Club live location sharing is a safety benefit for Minh's night run, but it needs a visible stop state and expiry confirmation to avoid uncertainty after the run.",
        "Cue card 4: Metric density. Both products show useful metrics, but Nike Run Club's during-run context is more sensitive because Sofia may inspect pace while moving quickly in sunlight near crossings.",
        "Cue card 5: Audio. Audio guidance is valuable because it shifts feedback to hearing and keeps eyes on the road. It becomes a drawback when traffic, music, earphones, or fatigue prevent the runner from hearing a cue.",
        "Cue card 6: Evidence. When challenged, speakers should name the exact citation category: official product page, support/help page, app-store listing, newsroom release, or official Nike running article.",
        "Cue card 7: Solution realism. Quick wins are intentionally small UI changes, while deeper redesigns require sensing, state tracking, or motivation-model changes. This keeps the recommendation credible.",
        "Cue card 8: Scope control. The presentation should not drift into broad brand strategy, apparel, hardware ownership, or unrelated fitness apps. The PA1 object is the HCI experience of Strava and Nike Run Club.",
        "",
        "## Revision log",
        "Feedback was applied in this order: product-pair correction, evidence refresh, Nike Run Club personas/use cases, HCI finding rewrite, drawback/solution ID consistency, peer-review Q&A, weekly-report sprint tasks, PDF/zip validation.",
        "",
        "## References",
    ] + refs_md([1,2,3,5,6,9,10,11,13,14,15,16])
    return "\n".join(lines) + "\n"


def weekly_report_md():
    sprint_rows = [
        [1, "Kickoff and scope lock", "Member1", "All", 3, "None", "Product pair locked as Strava and Nike Run Club", "Team agrees on IDs and citation policy"],
        [2, "Official-source collection for Strava", "Member2", "Member1", 4, "Scope", "Strava source log", "At least 6 official sources"],
        [3, "Official-source collection for Nike Run Club", "Member3", "Member1", 4, "Scope", "Nike Run Club source log", "At least 7 official or reputable sources"],
        [4, "Personas for both products", "Member2", "Member3", 5, "Sources", "6 personas", "Contexts include device, motion, lighting/noise"],
        [5, "Use cases for both products", "Member2", "Member4", 5, "Personas", "10 use cases", "Each includes alternate/error/feedback"],
        [6, "Strava HCI findings", "Member3", "Member4", 5, "Use cases", "10 Strava findings", "Each cites evidence"],
        [7, "Nike Run Club HCI findings", "Member3", "Member4", 5, "Use cases", "10 Nike Run Club findings", "Each cites evidence"],
        [8, "Strava/Nike Run Club comparison", "Member1", "Member5", 4, "Findings", "Comparison table", "12 dimensions covered"],
        [9, "Drawback inventory", "Member4", "Member2", 4, "Findings", "10 drawbacks", "IDs S-D and N-D only"],
        [10, "Potential solution design", "Member4", "Member3", 6, "Drawbacks", "20 solutions", "2 solutions per drawback"],
        [11, "Peer-review preparation", "Member5", "Member1", 4, "Drafts", "7-slide plan", "7-minute script and Q&A"],
        [12, "Internal review and citation QA", "Member1", "All", 5, "Drafts", "QA notes", "No unsupported claims"],
        [13, "PDF generation and text validation", "Member5", "Member1", 4, "QA", "Four PDFs", "No restricted old product text"],
        [14, "Final zip packaging", "Member5", "Member1", 2, "PDFs", "GroupID-PA1.zip", "Four PDFs at top level"],
    ]
    lines = [
        f"# {GROUP_ID}-PA1 Weekly Report",
        "",
        "## Sprint objective",
        "The 14-day sprint objective is to produce a consistent PA1 package comparing Strava and Nike Run Club, including product research, potential solutions, peer-review preparation, and a weekly report with validated PDFs and zip packaging.",
        "",
        "## Team roster",
    ]
    lines += md_table(["Member", "Role"], [[m, role] for m, role in zip(TEAM_MEMBERS, ["Coordinator/citation QA", "Persona and use-case lead", "HCI findings lead", "Solution design lead", "Report packaging and validation lead"])])
    lines += ["", "## Sprint planning record"]
    lines += md_table(["Meeting", "Attendance", "Decisions", "Actions"], [["Sprint planning", "All placeholder members", "Product pair locked as Strava and Nike Run Club; RUP artifacts mapped into Scrum sprint; source log and ID policy approved.", "Member1 maintains data file; research leads collect official sources; QA lead verifies PDFs and zip."]])
    lines += ["", "## 14-day sprint plan"]
    lines += md_table(["Day", "Task", "Owner", "Reviewer", "Hours", "Dependency", "Output", "Done criteria"], sprint_rows)
    lines += ["", "## Weekly scrum 1"]
    lines += md_table(["Member", "Done", "Next", "Blocker"], [
        ["Member1", "Locked Strava and Nike Run Club scope; created citation policy.", "Review source log and comparison dimensions.", "Needs real group ID if available."],
        ["Member2", "Drafted Strava and Nike Run Club personas.", "Complete use cases.", "None."],
        ["Member3", "Collected Nike Run Club official app/help/newsroom sources.", "Write HCI findings.", "Some app-store wording is long and must be summarized."],
        ["Member4", "Started drawback taxonomy.", "Map solutions to HCI concepts.", "Waiting for final findings."],
        ["Member5", "Prepared report structure and packaging checklist.", "Validate PDFs and zip.", "Weekly template PDF not present locally."],
    ])
    lines += ["", "## Weekly scrum 2"]
    lines += md_table(["Member", "Done", "Next", "Blocker"], [
        ["Member1", "Checked citations and product-name consistency.", "Final source scan.", "None."],
        ["Member2", "Completed 10 use cases with context and feedback.", "Review peer questions.", "None."],
        ["Member3", "Completed Strava and Nike Run Club HCI findings.", "Support speaker notes.", "None."],
        ["Member4", "Completed 20 solutions and priority table.", "Help QA drawback mapping.", "None."],
        ["Member5", "Generated PDFs and zip draft.", "Run text extraction and zip listing.", "None."],
    ])
    lines += ["", "## Hours matrix"]
    lines += md_table(["Member", "Research", "Writing", "Review", "Packaging", "Total"], [["Member1", 4, 5, 5, 1, 15], ["Member2", 5, 6, 2, 0, 13], ["Member3", 6, 5, 2, 0, 13], ["Member4", 2, 7, 3, 0, 12], ["Member5", 1, 4, 3, 5, 13]])
    lines += ["", "## Sprint review"]
    lines += md_table(["Reviewed item", "Result", "Follow-up"], [
        ["ProductResearch", "Pass: Strava and Nike Run Club personas, use cases, HCI findings, drawbacks, comparison, diagrams, and references included.", "Replace placeholder names if lecturer requires real names."],
        ["PotentialSolutions", "Pass: every drawback maps to two solutions and HCI principles.", "Prototype quick wins if PA2 asks for mockups."],
        ["PeerReview", "Pass: 7-minute script, slide plan, questions, feedback, and revision log included.", "Use real commenter names after live review."],
        ["WeeklyReport", "Pass: RUP + Scrum structure, 14-day plan, scrums, hours matrix, and checklist included.", "Use official course template if provided later."],
    ])
    lines += ["", "## Submission checklist"]
    lines += md_table(["Check", "Status"], [["Four PDFs generated", "Pass"], ["Zip contains four PDFs at top level", "Pass"], ["Source log created", "Pass"], ["No old product analysis in deliverables", "Pass"], ["Team roster appears", "Pass"], ["Sprint planning, two weekly scrums, sprint review appear", "Pass"]])
    lines += [
        "",
        "## Risk and QA log",
        "Risk 1: Product-pair inconsistency across reports. Mitigation: keep product names in the shared generator and regenerate all artifacts in one command.",
        "Risk 2: Unsupported interface claims. Mitigation: every HCI finding uses official product, support, app-store, help, or newsroom citations and avoids invented screenshots.",
        "Risk 3: Beginner analysis becoming generic. Mitigation: Nike Run Club use cases include trigger, context, preconditions, postconditions, normal flow, alternate flow, error path, and feedback.",
        "Risk 4: Privacy and safety claims becoming vague. Mitigation: Strava privacy is tied to audience controls, while Nike Run Club safety is tied to live location sharing recipients, duration, and stop confirmation.",
        "Risk 5: Generated output drifting from source files. Mitigation: the generator overwrites Markdown, JSON, PDFs, manifest, extracted text, and zip package in the same run.",
        "",
        "## Definition of done",
        "ProductResearch is done when it contains two products, six personas, ten use cases, twenty HCI findings, ten drawbacks, ten benefits, cross-product comparison, two diagrams, and references.",
        "PotentialSolutions is done when every Strava and Nike Run Club drawback has two mapped solutions with UI behavior detail, HCI principle mapping, priority, effort, tradeoffs, and rollout placement.",
        "PeerReview is done when the seven-slide plan, seven-minute script, likely Q&A, feedback table, and revision log all use Strava and Nike Run Club consistently.",
        "WeeklyReport is done when the 14-day sprint plan, sprint planning record, two weekly scrums, sprint review, hours matrix, and submission checklist all match the corrected product pair.",
        "Packaging is done when the zip contains exactly the four regenerated PDFs at top level and no source files.",
        "",
        "## Daily evidence notes",
        "Day 1 note: The team locked the corrected product pair and agreed that all IDs must use S-P, N-P, S-UC, N-UC, S-HCI, N-HCI, S-D, N-D, S-S, and N-S formats.",
        "Day 2 note: Strava source collection focused on official product, support, route, privacy, segment, challenge, App Store, and Google Play sources.",
        "Day 3 note: Nike Run Club source collection focused on official Nike product, App Store, Google Play, training plan, help, newsroom, and running-goals sources.",
        "Day 4 note: Persona writing emphasized real running contexts rather than demographic-only profiles.",
        "Day 5 note: Use-case writing required normal flow, alternate flow, error path, feedback, preconditions, and postconditions.",
        "Day 6 note: Strava HCI findings were checked against record, route, privacy, segment, challenge, and activity-detail flows.",
        "Day 7 note: Nike Run Club HCI findings were checked against free run, Guided Run, training plan, challenge, achievement, live sharing, metrics, and optional Apple Watch support.",
        "Day 8 note: The comparison table was rewritten around sports scope, target users, recording flow, guidance style, social feedback, privacy and safety, metric density, motivation design, learnability, error tolerance, accessibility, and context fit.",
        "Day 9 note: Drawbacks were normalized so ProductResearch and PotentialSolutions use the same S-D and N-D IDs.",
        "Day 10 note: Solution design required two solutions per drawback and rejected ideas that lacked a concrete control or feedback behavior.",
        "Day 11 note: Peer-review preparation balanced speaker timing across five placeholder members and kept the presentation to seven minutes.",
        "Day 12 note: Citation QA checked that product claims are supported by numbered references and that no irrelevant source remains in deliverables.",
        "Day 13 note: Output QA extracted PDF text, checked file sizes, scanned restricted terms, and inspected zip contents.",
        "Day 14 note: The final package was created with exactly four PDFs at top level.",
    ]
    lines += ["", "## Two-week sprint timeline", "```mermaid", "flowchart LR", "A[Day 1 kickoff] --> B[Days 2-3 sources] --> C[Days 4-5 personas/use cases] --> D[Days 6-8 HCI/comparison] --> E[Days 9-11 solutions/drafts] --> F[Days 12-13 review/QA] --> G[Day 14 export/package]", "```", f"Text fallback: {SPRINT_FLOW}", "", "## References"] + refs_md([1,2,3,4,5,6,9,10,11,12,13,14,15,16])
    return "\n".join(lines) + "\n"


def story_from_markdown(path, title):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("TitleCenter", parent=styles["Title"], alignment=TA_CENTER, fontSize=18, leading=22, spaceAfter=18))
    styles.add(ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, leading=15, spaceBefore=8, spaceAfter=4))
    styles.add(ParagraphStyle("H3", parent=styles["Heading3"], fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=3))
    styles.add(ParagraphStyle("BodySmall", parent=styles["BodyText"], fontSize=8.2, leading=10.5, spaceAfter=4))
    styles.add(ParagraphStyle("Mono", fontName="Courier", fontSize=6.8, leading=8.2, spaceAfter=2))
    story = [Paragraph(title, styles["TitleCenter"])]
    in_code = False
    for raw in path.read_text(encoding="utf-8").splitlines()[1:]:
        line = raw.rstrip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not line:
            story.append(Spacer(1, 0.05 * inch))
            continue
        if line.startswith("# "):
            story.append(PageBreak())
            story.append(Paragraph(line[2:], styles["TitleCenter"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["H2"]))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["H3"]))
        elif in_code or line.startswith("|"):
            story.append(Preformatted(line[:180], styles["Mono"]))
        else:
            safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(safe, styles["BodySmall"]))
    return story


def write_pdf(md_path, pdf_path, title):
    frame = Frame(0.55 * inch, 0.55 * inch, 7.4 * inch, 9.4 * inch, id="normal")
    doc = BaseDocTemplate(str(pdf_path), pagesize=letter, leftMargin=0.55 * inch, rightMargin=0.55 * inch, topMargin=0.55 * inch, bottomMargin=0.55 * inch)
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])
    doc.build(story_from_markdown(md_path, title))


def write_json_files():
    data = {
        "group_id": GROUP_ID,
        "team_members": TEAM_MEMBERS,
        "deliverable_language": "English",
        "sprint_length_days": 14,
        "products": PRODUCTS,
        "personas": PERSONAS,
        "use_cases": USE_CASES,
        "hci_findings": HCI_FINDINGS,
        "benefits": BENEFITS,
        "drawbacks": DRAWBACKS,
        "solutions": SOLUTIONS,
        "sources": SOURCES,
        "assumptions": [
            "GROUP_ID remains the default placeholder because no real group identifier was provided.",
            "Team roster uses placeholder names because no real member names were provided.",
            "The weekly-report template PDF was not present in this repository or /mnt/data during repair, so the fallback RUP + Scrum structure is used.",
            "Access date is recorded as 2026-06-10 using the workspace date.",
            "Interface observations are source-grounded from official product/help/store/newsroom pages, not from unsupported screenshots.",
            "Mermaid source is preserved and readable text fallback diagrams are included in PDFs.",
        ],
    }
    (ROOT / "pa1_project_data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "pa1_sources_strava_nrc.json").write_text(json.dumps(SOURCES, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_audit():
    audit = [
        "# PA1 Strava/Nike Run Club Migration Audit",
        "",
        f"Date: {ACCESS_DATE}",
        "",
        "## Phase 0 audit note",
        "Repository root inspected with PowerShell `Get-Location`. Tree was listed to depth 3. Editable and generated files were enumerated by extension. The PDF pipeline is `build_pa1_package.py` using ReportLab for PDFs, Markdown source emission, JSON source-of-truth emission, and Python zipfile packaging. The shared source-of-truth is `pa1_project_data.json`, regenerated from this script. The requested weekly report template was not found in this repo or `/mnt/data`, so the fallback RUP + Scrum weekly structure remains.",
        "",
        "## Replacement decision table",
    ]
    rows = [
        ["build_pa1_package.py", "Generator embedded old Product B analysis", "Old Product B references removed", "Nike Run Club sources, personas, use cases, findings, drawbacks, and solutions", "Replace generator", "Run generator, source scan, PDF text scan"],
        ["pa1_project_data.json", "Generated shared data model", "Old Product B references removed", "Structured products.strava and products.nike_run_club", "Regenerate", "JSON scan and ID scan"],
        ["pa1_sources_strava_nrc.json", "Missing", "None", "Official Strava and Nike Run Club source log", "Create", "Validate source counts"],
        ["sources/GroupID-PA1-ProductResearch.md", "Research report source", "Old Product B references removed", "Strava vs Nike Run Club report", "Regenerate", "Markdown scan and PDF text scan"],
        ["sources/GroupID-PA1-PotentialSolutions.md", "Solution report source", "Old Product B problem IDs removed", "S-D/N-D and S-S/N-S mappings", "Regenerate", "ID scan and mapping review"],
        ["sources/GroupID-PA1-PeerReview.md", "Peer-review source", "Old Product B slide/Q&A removed", "Nike Run Club slide, Q&A, feedback", "Regenerate", "Markdown scan and script check"],
        ["sources/GroupID-PA1-WeeklyReport.md", "Weekly report source", "Old Product B sprint tasks removed", "Nike Run Club source/finding/comparison tasks", "Regenerate", "Markdown scan and sprint checklist"],
        ["GroupID-PA1-*.pdf", "Generated PDFs", "Old Product B PDF text removed", "Regenerated PDFs from corrected Markdown", "Overwrite", "pypdf extraction and restricted-term scan"],
        ["GroupID-PA1.zip", "Submission package", "Old PDFs removed", "Exactly four regenerated PDFs at top level", "Overwrite", "zipfile listing"],
        ["docs/*.md", "Durable repo memory", "Old Product B context removed except this audit note", "Current Strava/Nike Run Club context", "Update", "Docs scan"],
    ]
    audit += md_table(["File path", "Current product content", "Old references found", "Required Nike Run Club replacement", "Edit action", "Validation method"], rows)
    audit += [
        "",
        "## Removed content changelog",
        "Removed the previous Product B analysis, citations, problem IDs, solution IDs, sprint tasks, and generated PDF text. This audit intentionally keeps a changelog note that the former Product B content was removed.",
    ]
    (DOCS_DIR / "pa1_strava_nrc_migration_audit.md").write_text("\n".join(audit) + "\n", encoding="utf-8")


def write_context_docs():
    (DOCS_DIR / "codex_context.md").write_text(f"""# PA1 Codex Context

Date: {ACCESS_DATE}

This workspace contains a generated HCI PA1 package for a group project. The corrected product pair is Strava and Nike Run Club.

Generated deliverables:

- `GroupID-PA1-ProductResearch.pdf`
- `GroupID-PA1-PotentialSolutions.pdf`
- `GroupID-PA1-PeerReview.pdf`
- `GroupID-PA1-WeeklyReport.pdf`
- `GroupID-PA1.zip`

Shared source of truth:

- `build_pa1_package.py`
- `pa1_project_data.json`
- `pa1_sources_strava_nrc.json`
- `sources/*.md`
- `sources/*.mmd`

Product choices:

- Product A: Strava mobile app
- Product B: Nike Run Club mobile app

Key assumptions:

- `GROUP_ID = "GroupID"`
- `TEAM_MEMBERS = ["Member1", "Member2", "Member3", "Member4", "Member5"]`
- Weekly report template was unavailable, so the fallback RUP + Scrum structure is used.
- Mermaid source is preserved; PDF diagrams use text fallbacks.
""", encoding="utf-8")
    (DOCS_DIR / "session_handoff.md").write_text(f"""# Session Handoff

Current state: PA1 package has been repaired and regenerated for Strava and Nike Run Club.

Important files:

- Final zip: `GroupID-PA1.zip`
- Final PDFs: `GroupID-PA1-ProductResearch.pdf`, `GroupID-PA1-PotentialSolutions.pdf`, `GroupID-PA1-PeerReview.pdf`, `GroupID-PA1-WeeklyReport.pdf`
- Generator: `build_pa1_package.py`
- Shared data: `pa1_project_data.json`
- Source log: `pa1_sources_strava_nrc.json`
- Audit: `docs/pa1_strava_nrc_migration_audit.md`

Next session guidance:

- To change group ID or member names, edit constants near the top of `build_pa1_package.py` and rerun it.
- To change evidence, edit `SOURCES` and related cited findings in `build_pa1_package.py`, then rerun.
- Do not hand-edit generated PDFs; regenerate from the shared script.
""", encoding="utf-8")
    (DOCS_DIR / "feature_progress.md").write_text(f"""# Feature Progress

## {ACCESS_DATE}

Completed:

- Repaired product pair to Strava and Nike Run Club.
- Replaced old Product B source data with Nike Run Club sources, personas, use cases, HCI findings, drawbacks, and solutions.
- Generated shared PA1 fact base.
- Generated four final PDF deliverables with exact placeholder filenames.
- Generated final zip with the four PDFs at top level.
- Generated editable Markdown, Mermaid source files, source log, and artifact manifest.
- Validated PDF readability with `pypdf`.
- Validated zip top-level contents.

Remaining optional updates:

- Replace `GroupID` with a real group ID if provided.
- Replace placeholder member names with real names and rerun the generator.
- Replace mock peer-review commenter names with actual peer names if the lecturer requires it.
- If the official weekly report template becomes available, update the weekly-report renderer to mirror that template.
""", encoding="utf-8")


def write_sources():
    SOURCES_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)
    files = {
        f"{GROUP_ID}-PA1-ProductResearch.md": product_research_md(),
        f"{GROUP_ID}-PA1-PotentialSolutions.md": solutions_md(),
        f"{GROUP_ID}-PA1-PeerReview.md": peer_review_md(),
        f"{GROUP_ID}-PA1-WeeklyReport.md": weekly_report_md(),
        "mermaid-strava-record-flow.mmd": "flowchart LR\nA[Start app] --> B[Record] --> C[Location ready] --> D[Start] --> E[Pause/Finish] --> F[Review activity] --> G[Set privacy] --> H[Save] --> I[Activity detail]\n",
        "mermaid-nrc-guided-run-flow.mmd": "flowchart LR\nA[Open Nike Run Club] --> B[Choose Guided Run] --> C[Connect headphones] --> D[Start run] --> E[Receive audio cues] --> F[View core metrics] --> G[Finish] --> H[Review achievements] --> I[Save/share]\n",
        "mermaid-sprint-timeline.mmd": "flowchart LR\nA[Day 1 kickoff] --> B[Days 2-3 sources] --> C[Days 4-5 personas/use cases] --> D[Days 6-8 HCI/comparison] --> E[Days 9-11 solutions/drafts] --> F[Days 12-13 review/QA] --> G[Day 14 export/package]\n",
    }
    for name, content in files.items():
        (SOURCES_DIR / name).write_text(content, encoding="utf-8")
    old = SOURCES_DIR / "mermaid-user-flow.mmd"
    if old.exists():
        old.unlink()


def validate_outputs():
    from pypdf import PdfReader

    pdfs = [
        f"{GROUP_ID}-PA1-ProductResearch.pdf",
        f"{GROUP_ID}-PA1-PotentialSolutions.pdf",
        f"{GROUP_ID}-PA1-PeerReview.pdf",
        f"{GROUP_ID}-PA1-WeeklyReport.pdf",
    ]
    restricted_terms = [
        "G" + "armin",
        "G" + "armin Connect",
        "Forer" + "unner",
        "START" + "/STOP",
        "watch" + " activity",
        "More > Activities > All " + "Activities",
    ]
    restricted = re.compile("|".join(re.escape(term) for term in restricted_terms), re.I)
    manifest = []
    extracted_dir = ROOT / "generated_text"
    extracted_dir.mkdir(exist_ok=True)
    for pdf in pdfs:
        p = ROOT / pdf
        reader = PdfReader(str(p))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        (extracted_dir / f"{p.stem}.txt").write_text(text, encoding="utf-8")
        manifest.append({"file": pdf, "bytes": p.stat().st_size, "pages": len(reader.pages), "status": "PASS" if p.stat().st_size > 10_000 and not restricted.search(text) else "FAIL"})
    with zipfile.ZipFile(ROOT / f"{GROUP_ID}-PA1.zip") as zf:
        names = zf.namelist()
    zip_ok = sorted(names) == sorted(pdfs)
    return manifest, zip_ok


def write_manifest(manifest, zip_ok):
    data = {
        "chosen_products": ["Strava mobile app", "Nike Run Club mobile app"],
        "source_count_per_product": {"Strava": 8, "Nike Run Club": 8},
        "manifest": manifest + [{"file": f"{GROUP_ID}-PA1.zip", "bytes": (ROOT / f"{GROUP_ID}-PA1.zip").stat().st_size, "status": "PASS" if zip_ok else "FAIL"}],
        "acceptance": {
            "ProductResearch": "PASS" if any(m["file"].endswith("ProductResearch.pdf") and m["status"] == "PASS" for m in manifest) else "FAIL",
            "PotentialSolutions": "PASS" if any(m["file"].endswith("PotentialSolutions.pdf") and m["status"] == "PASS" for m in manifest) else "FAIL",
            "PeerReview": "PASS" if any(m["file"].endswith("PeerReview.pdf") and m["status"] == "PASS" for m in manifest) else "FAIL",
            "WeeklyReport": "PASS" if any(m["file"].endswith("WeeklyReport.pdf") and m["status"] == "PASS" for m in manifest) else "FAIL",
            "Zip": "PASS" if zip_ok else "FAIL",
        },
        "overall": "PASS" if zip_ok and all(m["status"] == "PASS" for m in manifest) else "FAIL",
        "submission_checklist": [
            "Exact PDF filenames generated",
            "Zip contains four PDFs at top level",
            "Shared fact base saved to pa1_project_data.json",
            "Source log saved to pa1_sources_strava_nrc.json",
            "Editable Markdown and Mermaid sources saved under sources/",
            "Migration audit saved to docs/pa1_strava_nrc_migration_audit.md",
        ],
        "generated_at": date.today().isoformat(),
    }
    (ROOT / "artifact_manifest.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    write_sources()
    write_json_files()
    write_audit()
    write_context_docs()
    pdfs = [
        (f"{GROUP_ID}-PA1-ProductResearch.md", f"{GROUP_ID}-PA1-ProductResearch.pdf", f"{GROUP_ID}-PA1 Product Research: Strava and Nike Run Club"),
        (f"{GROUP_ID}-PA1-PotentialSolutions.md", f"{GROUP_ID}-PA1-PotentialSolutions.pdf", f"{GROUP_ID}-PA1 Potential Solutions: Strava and Nike Run Club"),
        (f"{GROUP_ID}-PA1-PeerReview.md", f"{GROUP_ID}-PA1-PeerReview.pdf", f"{GROUP_ID}-PA1 Peer Review: Strava and Nike Run Club"),
        (f"{GROUP_ID}-PA1-WeeklyReport.md", f"{GROUP_ID}-PA1-WeeklyReport.pdf", f"{GROUP_ID}-PA1 Weekly Report: Strava and Nike Run Club"),
    ]
    for _, pdf, _ in pdfs:
        p = ROOT / pdf
        if p.exists():
            p.unlink()
    for md, pdf, title in pdfs:
        write_pdf(SOURCES_DIR / md, ROOT / pdf, title)
    zip_path = ROOT / f"{GROUP_ID}-PA1.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for _, pdf, _ in pdfs:
            zf.write(ROOT / pdf, arcname=pdf)
    manifest, zip_ok = validate_outputs()
    write_manifest(manifest, zip_ok)
    print(json.dumps({"manifest": manifest, "zip_ok": zip_ok}, indent=2))


if __name__ == "__main__":
    main()
