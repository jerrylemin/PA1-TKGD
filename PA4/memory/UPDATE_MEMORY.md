# Updating PA4 Memory

This is the resume procedure for future Codex sessions. Keep the scope at `PA4/` and preserve unrelated working-tree changes.

## 1. Start with the boundary

1. Read `PA4/memory/PA4_MEMORY_INDEX.md`, `PA4/memory/MEMORY_BUILD_AUDIT.md`, and the nearest source/work docs.
2. Run `git status --short` and inspect the relevant diff.
3. Run `graphify query "<question>" --graph PA4/graphify-out/graph.json` before broad source browsing for a codebase question.
4. Treat source files and current QA as authoritative over stale graph output.

## 2. Code-only changes

For prototype, QA, analysis, report, or packaging code changes:

```text
graphify update PA4
graphify check-update PA4
```

`graphify update` is AST-only in Graphify 0.8.18 and does not incur semantic API cost. Re-run the relevant QA/test command, inspect `GRAPH_REPORT.md`, and compare graph freshness to `git rev-parse HEAD`.

## 3. Document or image changes

For new/modified Markdown, PDF, DOCX, or image evidence:

1. Re-run the PA4 detection audit and confirm `.graphifyignore` still preserves the intended source.
2. Use local Codex workers for semantic extraction, one image per worker chunk. Do not send participant media to an external backend.
3. Validate every fragment, normalize provenance/confidence, merge semantic and AST output, and rebuild `graph.json`, `GRAPH_REPORT.md`, `graph.html`, and `BENCHMARK.json`.
4. Refresh `GRAPH_COVERAGE.md`, `GRAPH_QUERY_VALIDATION.md`, and the source manifest when coverage changes.
5. Re-run the ten required round-2 query tests, the three smoke queries, six current path tests, and five explain tests. Save concise Q&A results with `graphify save-result`.

The final PA4 refresh uses Graphify's `build`, `cluster`, and `export` APIs after `graphify update PA4` when the AST-only CLI update would otherwise omit the local semantic fragment. Never hand-edit `graph.json`.

If no semantic backend is configured, do not silently fall back to fabricated or regex-generated findings. Use Codex semantic workers and record the local-only mode in the audit.

## 4. Critical smoke queries

Run these after any continuity, study, or graph rebuild:

```text
graphify query "Why was FIFA Status Dashboard selected?" --graph PA4/graphify-out/graph.json
graphify query "What blocks SUBMISSION_READY?" --graph PA4/graphify-out/graph.json
graphify query "Which script builds the official PA4 package?" --graph PA4/graphify-out/graph.json
```

## 5. Hooks and privacy

The project-scoped Codex PreToolUse hook is registered in `.codex/hooks.json`. Existing Git LFS `post-commit` and `post-checkout` hooks were not overwritten; `graphify hook status` reports them as unavailable because Graphify is not on that hook process path. Do not replace those hooks without explicit direction.

Keep `PA4/study/data/` schema-only until real consented sessions exist. Do not add participant identities, recordings, quotes, timings, or findings to memory merely to make a query pass.
