# Setup And Run

Use the bundled Codex Python runtime because it includes `reportlab` and `pypdf`.

Regenerate the package:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\Administrator\Documents\MEGA\tkgd\PA1\build_pa1_package.py'
```

Validate PDF text anchors:

```powershell
@'
from pathlib import Path
from pypdf import PdfReader
for pdf in Path('.').glob('GroupID-PA1-*.pdf'):
    reader = PdfReader(str(pdf))
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    print(pdf.name, len(reader.pages), len(text))
'@ | & 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -
```

Check zip contents:

```powershell
& 'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m zipfile -l 'GroupID-PA1.zip'
```

