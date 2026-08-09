# Evidence Validation

## Corpus audit

- Website screenshots inventoried: 105 capture files (54 FIFA and 51 Chess.com).
- Approved primary figure pool checked visually: 20 FIFA files and 16 Chess.com files.
- The full PA1/PA2 filesystem inventory is stored in `tmp/source-audit/file-inventory.csv`.
- Exact image hashes and duplicate groups are stored in `tmp/source-audit/audit.json`.
- Filenames are treated as labels only. Claims are limited to visible pixels and the approved evidence rules.

## Validation decisions

- Use `fifa-06-match-centre.png` and `fifa-10-match-centre-filters.png` for distinct match-centre and filter-drawer evidence.
- Use `fifa-20-tickets-hospitality-landing.png` as the primary ticket-state evidence. It shows tournament entry cards but no consolidated cross-tournament status dashboard.
- Use `fifa-35-fifa-plus-dazn-landing.png` for brand/account-boundary evidence and `fifa-37-fifa-plus-after-cookie-dismiss.png` only for the unobstructed landing entry.
- Use `chess-29-analysis-board.png` only for the analysis-entry choices. It does not show completed review output, engine lines, move classifications, or a beginner explanation.
- Use `chess-24-lessons-landing-loaded.png` and `chess-49-lessons-mobile.png` for long learning-list evidence.
- `chess-53-ad-panel-natural.png` is restricted: the inspected pixels do not unambiguously show a high-salience advertisement, so it is not used as primary proof of advertising competition.

## Excluded or misleading filename groups

- FIFA homepage duplicates: `fifa-02`, `fifa-03`, `fifa-44`, `fifa-45`, and `fifa-54`.
- FIFA mobile menu mislabel: `fifa-05`.
- FIFA match-state near-duplicates: `fifa-07`, `fifa-08`, and `fifa-09`.
- FIFA search/article/tournament near-duplicates: `fifa-12`, `fifa-14`, `fifa-15`, `fifa-17`, `fifa-18`, and `fifa-53`.
- FIFA ticket-state misleading series: `fifa-21` through `fifa-33`.
- FIFA+ rail duplicates: `fifa-38` through `fifa-43`.
- Chess.com homepage/menu/cookie repeats: `chess-02`, `chess-04`, `chess-51`, and `chess-52`.
- Chess.com play/active-game misleading series: `chess-06`, `chess-08`, `chess-09`, and `chess-11` through `chess-18`.
- Chess.com puzzle-result ambiguous series: `chess-21` through `chess-23`.
- Chess.com lesson/detail repeat: `chess-25`.
- Chess.com analysis-output misleading series: `chess-28`, `chess-30` through `chess-34`.
- Chess.com premium/entitlement ambiguous series: `chess-35` and `chess-36`.
- Chess.com premove and Focus Mode unsupported series: `chess-37` through `chess-44`.

## Research integrity boundary

No PA2 interview notes, observation transcripts, survey exports, participant recordings, or research-session photographs were found. The study therefore uses source analysis and an artifact-based try-it-yourself walkthrough. Screenshots record system states, not participant behavior. Personas and work models are provisional and require future validation with direct user research.
