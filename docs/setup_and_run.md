# Setup And Run

Use the bundled Codex Python runtime because it includes `reportlab` and `pypdf`.

Regenerate the package:

```powershell
npm run build:pa1
```

Validate the current draft:

```powershell
npm run validate:pa1:draft
```

Validate final submission eligibility:

```powershell
npm run validate:pa1:final
```

Final mode must fail while real classroom peer feedback is pending.

Regenerate visual evidence:

```powershell
npm run visuals:pa1
```

Run the complete visual-capture, build, and draft-validation pipeline only when fresh live screenshots are intended:

```powershell
npm run full:pa1
```

Validate zip contents:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m zipfile -l 'Group10-PA1.zip'
```

Regenerate WeeklyReport DOCX, PDF, and review file only:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\create_weekly_report.py'
```

Regenerate Vietnamese WorkDivision docx:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\create_pa1_work_division_docx.py'
```

Run final text validation:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\validate_pa1_final_fix.py'
```

`scripts/validate_pa1_final_fix.py` is a legacy check. Submission readiness is governed by `scripts/validate_pa1_submission.py`.

Render Mermaid diagrams with `npx mmdc`, then run the balance/diagram validator:

```powershell
Get-ChildItem assets/diagrams/mermaid/*.mmd | ForEach-Object { npx mmdc -i $_.FullName -o (Join-Path assets/diagrams/rendered ($_.BaseName + '.png')) -b transparent }
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\validate_pa1_balance_diagrams.py'
```
