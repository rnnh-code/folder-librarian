# Knowledge Wiki Mode

Use this mode when a folder should become a persistent knowledge base, not just a tidy file cabinet.

## When To Use

Good fits:
- Reference libraries with reusable frameworks, training, research, or playbooks.
- Research archives where sources accumulate over weeks or months.
- Business/team knowledge folders with recurring themes, entities, decisions, or operating principles.
- Knowledge vaults where the user wants synthesis, cross-links, and a maintained overview.

Poor fits:
- Temporary Downloads cleanup.
- One-time admin records.
- Pure media folders without a clear knowledge goal.
- Folders where the user only wants files moved into buckets.

## Three Layers

Keep the layers separate:

- Raw sources: original files. Do not edit, delete, unzip, or rename unless explicitly approved.
- Generated wiki: markdown pages written by the agent from sources and user discussions.
- Schema/conventions: the local instructions that explain how the wiki should be maintained.

For a normal folder-librarian job, the generated wiki should usually live in:

```text
00 Wiki/
  index.md
  log.md
```

Use a different name only if the folder already has a strong local convention.

## Core Files

### `00 Wiki/index.md`

Content-oriented map of the wiki.

Include:
- Page link.
- One-line purpose.
- Main source areas or source count when useful.
- Key tags or categories when helpful.

Read this before answering questions from the wiki.

### `00 Wiki/log.md`

Chronological, append-only activity record.

Use consistent headings so the log is searchable:

```md
## [YYYY-MM-DD] ingest | Source or batch name
## [YYYY-MM-DD] query | Question or output name
## [YYYY-MM-DD] lint | Wiki health check
```

Each entry should say what changed, which pages were touched, and what still needs review.

## Page Types

Prefer a small number of useful pages over many thin summaries.

Common page types:
- Overview page: the high-level map of the topic or archive.
- Concept page: a durable idea, framework, method, principle, or mental model.
- Entity page: a person, company, product, brand, customer, market, place, or team.
- Source note: a source-specific summary only when the source is important enough to revisit.
- Comparison page: differences between frameworks, versions, markets, competitors, or approaches.
- Question page: a useful answer from a user query that should persist.

## Workflows

### Ingest

Use when adding sources or converted markdown to the wiki.

1. Read the relevant source files or converted markdown.
2. Identify the durable ideas, entities, frameworks, contradictions, and open questions.
3. Create or update synthesis pages.
4. Add links between related pages.
5. Update `index.md`.
6. Append an entry to `log.md`.

Do not create one page per source by default. Create source notes only for high-value sources.

### Query

Use when the user asks a question against the archive.

1. Read `00 Wiki/index.md` first when it exists.
2. Read the most relevant wiki pages.
3. Use source markdown/original files to verify important claims when needed.
4. Answer in plain English with links to the relevant wiki/source pages.
5. If the answer is reusable, ask or infer from the request whether to save it as a question page.

### Lint

Use periodically or when the wiki starts feeling messy.

Check for:
- Pages with no useful inbound or outbound links.
- Important concepts mentioned repeatedly but lacking their own page.
- Contradictions between pages.
- Claims that look stale or superseded by newer sources.
- Thin pages that should be merged.
- Pages that need source links.
- Missing index entries.
- Log gaps.

Suggest fixes before making broad restructuring changes.

## Evidence And Source Handling

The wiki is generated and useful, but it is not the source of truth. Original files and converted markdown are evidence.

When writing wiki pages:
- Link back to relevant source files or converted markdown.
- Mark uncertain claims clearly.
- Flag image-heavy, scanned, or weak conversion outputs.
- Note when two sources disagree or when a newer source appears to supersede an older one.
- Avoid pretending that a synthesis is more certain than the sources allow.

## Suggested Minimal Wiki For A Business Archive

```text
00 Wiki/
  index.md
  log.md
  Overview.md
  Core Frameworks.md
  Customers And Segments.md
  Market Forces.md
  Activation And Execution.md
  Measurement.md
  Open Questions.md
```

Adapt the page names to the archive. Keep the first version small and useful.
