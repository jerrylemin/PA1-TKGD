# Peer Review finalization plan

## Phase 0 findings

- Target: `submission-final/Group10-PA3-PeerReview.docx`.
- The existing DOCX is a one-page placeholder capture template with 17 body paragraphs and 4 tables.
- Its current header/footer and tables use capture/audit language, including `Peer Review Capture`, `Evidence mode`, `Submission artifact`, `HARD EXTERNAL BLOCKER`, `Not yet captured`, `How to complete before submission`, and `BLOCKED EXTERNALLY`.
- No relevant `AGENTS.md` was found under the PA project root. The repository is dirty with unrelated PA3 changes; those changes are out of scope and will be preserved.
- The current DOCX has one section, no explicit page breaks, no comments, and no tracked changes. It uses a restrained Georgia/Arial/Consolas visual system with bordered tables.

## Planned change

Replace only the target report content with a completed Requirement 3 peer-review report covering:

1. presentation feedback;
2. the lecturer's separate flow assessment;
3. the distinction among lecturer, group, and novice interview perspectives;
4. the paraphrased lecturer question;
5. the group's reflection on Chess Alt 3 versus Chess Alt 2;
6. the novice-versus-experienced design insight;
7. response/action implications; and
8. a concise conclusion and official Requirement 3 feedback table.

Use `Lecturer` / `Course Lecturer` because no verified personal name was supplied. Keep the factual viewpoints separate:

- Lecturer: FIFA Alt 1 and Chess Alt 1.
- Group: FIFA Alt 1 and Chess Alt 3.
- Novice interview trend from 5 people: FIFA Alt 1 and Chess Alt 2.

Do not alter Requirement 2 testing results or any other PA3 artifact. Do not invent vote counts, names, quotes, demographics, timings, percentages, or a final redesign.

## Acceptance checks

- Create a timestamped backup before replacing the target DOCX.
- Final report is approximately 3-4 pages, readable at 11-12 pt body text, with clear headings, bordered tables, and one highlighted paraphrased question box.
- All required factual viewpoints, reflection, and actions are present and unambiguous.
- No placeholder, blocker, capture-template, audit, or AI-like submission-status language remains in the final DOCX.
- No forbidden exact vote distribution is introduced.
- Render the final DOCX to PNGs and inspect every page for clipping, overlap, broken tables, bad line breaks, orphan headings, large whitespace, and missing glyphs.
- Review the final DOCX structure and the scoped Git diff; preserve unrelated PA3 work and do not commit or push.

## Rollback

If content or render QA fails, restore the target from the timestamped backup and rework the document before handoff.

Phase 0 complete; proceeding to backup and implementation.

## Final verification

- Backup: `submission-final/backup/20260823-170547/Group10-PA3-PeerReview.docx`.
- Final DOCX renders to 3 pages in `submission-final/qa-peer-review-final-20260823-170547-r3/`.
- Render inspection: all three pages checked; no clipping, overlap, broken tables, missing glyphs, or unexpected blank pages.
- Content scan: required lecturer feedback, three viewpoint distinction, group reflection, novice insight, and response/action content present.
- Integrity scan: no exact vote distribution, invented lecturer name, placeholder language, or capture/audit wording in the final DOCX.
- Table geometry audit: passed with matching table widths, indents, grids, and cell widths.
- Accessibility audit: 0 high, 2 medium, 0 low; the two medium findings are expected because the metadata table and one-cell question callout are not header-row data tables.
- Requirement 2 and all unrelated PA3 files were left unchanged.
