# Group10 PA4

## Purpose

PA4 turns the validated PA3 concepts into two offline hi-fi prototypes and prepares a non-fabricated summative user-study package.

## Prototype start command

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory PA4/prototype
```

Then open `http://127.0.0.1:4173/index.html`.

Use the presenter shell for the 15–20 minute demo:

- `http://127.0.0.1:4173/index.html?mode=presenter#home`

Use a direct study route for a participant session. Study mode hides the lab shell, launcher, offline/demo labels, and researcher-only controls:

- `http://127.0.0.1:4173/index.html?mode=study&product=fifa#fifa`
- `http://127.0.0.1:4173/index.html?mode=study&product=chess#chess`

## Build / QA command

```powershell
node PA4/scripts/capture-prototype-qa.mjs
```

This checks the primary interaction paths at 1440 × 900 and 390 × 844 and writes screenshots to `PA4/evidence/prototype-screenshots/`.

## Study-data ingestion and analysis

Place only real, consented, anonymized data into `PA4/study/data/`, verify recordings under `PA4/evidence/recordings/`, then run:

```powershell
python PA4/study/analysis/analyze_study.py
```

## Artifact generation

```powershell
python PA4/scripts/build_pa4_reports.py
```

The script creates the three editable DOCX sources and three final PDFs under `PA4/source/` and `PA4/final/`.

## Final package

```powershell
python PA4/scripts/package_pa4.py
```

The package command validates the final filenames and creates two archives without adding recordings or synthetic study rows:

- `PA4/final/Group10-PA4-WorkingEvidence.zip` — source, study, QA, audit, and report-generation evidence for the team.
- `PA4/final/Group10-PA4.zip` — minimal official submission package containing only the three required PDFs.

## External evidence still required

- Genuine YouTube hi-fi demo URL for the first page of the hi-fi PDF.
- At least five real participant sessions.
- A verified recording for every session.
- Real task timings, success/error observations, questionnaire responses, and interview feedback.

## Resume instructions

Run the browser QA, conduct the study with the facilitator script, verify the recordings, fill the CSV templates, run the analysis, rebuild reports, then rerun package validation. Do not replace an external blocker with a placeholder URL or synthetic evidence.
