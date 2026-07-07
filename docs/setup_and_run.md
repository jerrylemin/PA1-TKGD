# Setup And Run

Use the bundled Codex Python runtime because it includes `reportlab` and `pypdf`.

Regenerate the package:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\Administrator\Documents\MEGA\tkgd\PA1\build_pa1_package.py'
```

Regenerate visual evidence:

```powershell
npm run visuals:pa1
```

Validate zip contents:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m zipfile -l 'GroupID-PA1.zip'
```

Regenerate Vietnamese WorkDivision docx:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\create_pa1_work_division_docx.py'
```

Run final text validation:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\validate_pa1_final_fix.py'
```

Render Mermaid diagrams with `npx mmdc`, then run the balance/diagram validator:

```powershell
Get-ChildItem assets/diagrams/mermaid/*.mmd | ForEach-Object { npx mmdc -i $_.FullName -o (Join-Path assets/diagrams/rendered ($_.BaseName + '.png')) -b transparent }
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'scripts\validate_pa1_balance_diagrams.py'
```
