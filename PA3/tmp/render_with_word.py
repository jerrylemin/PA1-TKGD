from pathlib import Path
import sys
import win32com.client

src = Path(sys.argv[1]).resolve()
dst = Path(sys.argv[2]).resolve()
dst.parent.mkdir(parents=True, exist_ok=True)
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = 0
word.AutomationSecurity = 3
doc = None
try:
    doc = word.Documents.Open(
        str(src), ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False,
        Revert=False, Visible=False, OpenAndRepair=True, NoEncodingDialog=True,
    )
    doc.ExportAsFixedFormat(str(dst), 17)
    print(f"pages={doc.ComputeStatistics(2)} pdf={dst}")
finally:
    if doc is not None:
        doc.Close(False)
    word.Quit()
