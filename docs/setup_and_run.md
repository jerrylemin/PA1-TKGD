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
