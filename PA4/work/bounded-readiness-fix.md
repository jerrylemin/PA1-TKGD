# Bounded readiness fix

## Finding

- `package_pa4.py` accepted `READY_FOR_REAL_PARTICIPANTS` from aggregate browser QA, Chess validation, and analysis-file existence, while the current matrix makes R2AC01-R2AC27 the mandatory local gate.
- `final/Group10-PA4.zip` contained PDFs whose SHA-256 values differed from the current final PDFs; QA renders were 7/6/2 instead of 5/4/1.

## Change

- The executable local gate now reads the participant-readiness range from the acceptance matrix and requires every listed criterion to have status `PASS`; external evidence remains a submission-only blocker.
- The stale official ZIP was preserved at `final/archive/Group10-PA4-STALE.zip`.
- QA renders were regenerated from the current final PDFs.

## Validation

- `python -m py_compile PA4/scripts/package_pa4.py` — PASS.
- Readiness cases and `python PA4/scripts/package_pa4.py` — PASS; official generation refused with exit 2 and no official ZIP.
- Current PDF hashes unchanged; page/render counts are Hi-fi 5/5, Summative 4/4, Weekly 1/1; all render PNGs open.
- `python -m unittest discover -s . -p 'test_analyze_study.py'` — 15 tests passed.
- `graphify update PA4` — code graph updated; the CLI reported that document/paper/image semantic modalities were not incrementally refreshed. No Graphify repair was attempted.
