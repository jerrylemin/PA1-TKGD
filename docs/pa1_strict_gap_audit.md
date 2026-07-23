# PA1 Strict Gap Audit

Date: 2026-07-07

## 1. Executive verdict

Verdict: NOT READY FINAL. The current ZIP is structurally correct, but the package fails the requested strict content and authenticity gates. Safe disposition: repair and validate as READY DRAFT while retaining explicit blockers for the missing real group ID and real classroom peer feedback.

## 2. Current repo state

- Branch: `main`.
- Baseline commit: `c5ce65b4a36759349011fe73f109bb6ea7914ec8`.
- Baseline dirty status: clean.
- Root artifacts: four PDFs, one exact four-PDF ZIP, and WorkDivision DOCX all exist.
- PDF pages: ProductResearch 40; PotentialSolutions 14; PeerReview 4; WeeklyReport 4.
- PDF extraction: pypdf succeeds for every PDF; no PDF has empty extracted text.
- DOCX: root/output WorkDivision copies are hash-identical and structurally readable; visual render is blocked because LibreOffice/soffice is unavailable.

## 3. PA1 requirement checklist

| Requirement | Baseline | Decision |
| --- | --- | --- |
| FIFA.com and Chess.com only | PASS | Preserve |
| Four required PDFs | PASS | Regenerate after fixes |
| Exact four-PDF ZIP | PASS | Rebuild and hash-check |
| Real group ID | BLOCKED | Keep `GroupID` in draft; final mode fails |
| Real classroom peer feedback | BLOCKED | Preserve rehearsal entries; add pending real-feedback table |
| Strict RUP + Scrum WeeklyReport | FAIL | Rewrite generator and source |
| Canonical solution traceability | FAIL | Correct contradictory evidence table and validate semantics |
| PDF text extraction | PASS, weak legacy gate | Make non-empty extraction mandatory |
| Missing-image validation | PASS manually | Automate repo-root Markdown path validation |
| Honest readiness language | FAIL | Supersede unsupported READY 10/10 claims |

## 4. WeeklyReport strict format audit

The baseline report lacks Process Overview, RUP phase descriptions, Scrum cadence/templates, Drive structure/links, meeting times, present/absent fields, exact meeting headings, exact per-member Scrum subsections, meeting summaries, and several review fields. It incorrectly includes a product References section. The generator contains the same defects and would overwrite a source-only repair.

## 5. ProductResearch audit

The report contains two products, six personas, ten detailed use cases, explicit contexts, findings, evidence, and citations. Canonical finding IDs exist. Gaps: the product-selection domain field is descriptive rather than the literal domains; the summary narrative drifts from the canonical drawback table; several figure IDs are relabeled from manifest IDs or use solution sketches as research evidence; several screen-to-claim links do not visibly support the claimed control. The strict fix will preserve useful evidence, correct canonical narrative, and avoid claiming a screenshot proves controls it does not show.

## 6. PotentialSolutions traceability audit

The drawback inventory and solution-detail table use the requested canonical IDs. The `Drawback evidence and visual solution mapping` table contradicts the canonical meaning in nine of ten rows and assigns wrong solution pairs in multiple rows. The same contradictions are hard-coded in `build_pa1_package.py` and extracted PDF text. This is a release blocker; the table must be rebuilt from one canonical map and validated row by row.

## 7. PeerReview authenticity audit

No real classroom peer feedback was found. Existing named entries are explicitly labeled mock/internal rehearsal and therefore are not fraudulent, but the report lacks a separate `Internal rehearsal feedback` heading and the required `Real Classroom Peer Feedback, Pending` empty table. Final mode must fail until real classroom rows replace the pending state.

## 8. Google Drive folder structure audit

No repository evidence provides real Weekly Scrum, Sprint Planning, Sprint Review, or Google Drive README URLs. The strict fix will use `TODO` link values from config in draft mode, add the required Drive README folder template, and expose GitHub and ZIP names. Link placeholders are draft warnings, not fabricated links.

## 9. Artifact packaging audit

The current ZIP contains exactly the four top-level PDFs and each archived member is byte-identical to its root PDF. WorkDivision is correctly excluded. Gaps: root PDF copies are missing from `output/`; stale report DOCX files are not rebuilt; the manifest uses a hard-coded date and lacks hashes/freshness/config/authenticity state. PDF visual QA found 5.8 pt table text, orphaned figure headings, excess whitespace around small images, no page numbers, and dense reference spill pages.

## 10. Build and validation audit

The build hardcodes `GROUP_ID`, writes only root PDFs/ZIP, and has no draft/final mode. Legacy validators check sizes, terms, and ID presence but not semantic mappings or strict process/authenticity requirements. PDF extraction can silently return an empty string and still pass. Required npm scripts and `scripts/validate_pa1_submission.py` are absent.

## 11. Exact fix plan

1. Add `config/pa1_config.json`; derive artifact/source names and links from it.
2. Rebuild WeeklyReport generator to the exact ten-section RUP + Scrum format and remove References.
3. Define one canonical drawback map; generate all PotentialSolutions traceability rows from it and add semantic validator checks.
4. Separate internal rehearsal feedback from a pending real-classroom feedback table; retain blockers without inventing data.
5. Correct ProductResearch canonical narrative and domain labels while preserving detailed use cases and evidence.
6. Add strict draft/final validator covering source/image/PDF/DOCX/ZIP/extraction/freshness/readiness gates.
7. Add npm build/validate/full scripts; use existing dependencies.
8. Regenerate Markdown, JSON, extracted text, PDFs, WorkDivision DOCX, output copies, ZIP, and manifest.
9. Re-render and inspect all final PDF pages; structurally validate DOCX and disclose the unavailable visual renderer.
10. Publish a final validation report with an honest READY DRAFT or NOT READY verdict and exact remaining blockers.

