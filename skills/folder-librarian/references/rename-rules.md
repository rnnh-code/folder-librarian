# Rename Rules

Use controlled renaming when clearer filenames would make a folder easier to remember, search, and reuse.

## When To Rename

Good rename candidates:
- Vague names: `final.pdf`, `deck.pptx`, `scan001.pdf`, `copy.docx`.
- Machine exports or messy downloads with random ids.
- Files where the title is clear from the document but not from the filename.
- High-value frameworks, playbooks, templates, training docs, and source notes.
- Converted markdown/source pairs where matching clearer names would improve navigation.

Poor rename candidates:
- Files already clearly named.
- Legal, tax, finance, medical, HR, or admin records where exact original names may matter.
- Source bundles, zips, exports, datasets, and vendor/customer-provided originals where provenance matters.
- Duplicates or near-duplicates that have not been compared.
- Ambiguous files whose content has not been inspected.

## Proposal First

Before renaming, create a dry-run table:

```md
| Current path | Proposed path | Reason | Confidence |
| --- | --- | --- | --- |
| old.pdf | Clear Topic - Source - 2024.pdf | Filename was vague; title found on page 1. | High |
```

Only execute the rename plan after approval, unless the user has explicitly approved a controlled rename pass.

For a controlled rename pass, execute only high-confidence renames and keep ambiguous cases in the proposal/review list.

## Naming Style

Prefer names that answer: "What is this, and why would I look for it?"

Useful pattern:

```text
Topic Or Framework - Document Type - Date Or Version.ext
```

Examples:

```text
Brand Building Framework - One Page Summary - 2014.pdf
Finance Module - Marketing ROI And Initiative Economics.pptx
eCommerce Search - 101 Training Deck.pptx
Trial And Penetration - 15 Lessons Training.pdf
```

Rules:
- Preserve the original extension.
- Use plain words over cryptic abbreviations unless the abbreviation is the user's language.
- Keep names readable, not exhaustive.
- Keep dates as `YYYY-MM-DD` or `YYYY` when useful.
- Keep version markers like `v2`, `final`, `draft`, region names, source names, and owner names when they help distinguish files.
- Remove clutter such as duplicate spaces, random ids, repeated `final_final`, download suffixes, and unsafe filename characters when doing so does not remove meaning.
- Avoid slashes, colons, and characters that create cross-platform filename problems.

## Source Pairs

When a markdown copy sits next to an original source file:
- Prefer renaming the source and markdown copy together so their base names match.
- If only the markdown is renamed, explain why.
- Update any index or wiki links that pointed to the old markdown path.

## Rename Log

When renames are executed, create or update a local rename log such as:

```text
00 Rename Log.md
```

For folders with `00 Wiki/log.md`, the wiki log may also record the rename batch.

Each entry should include:
- Date.
- Old path.
- New path.
- Reason.
- Whether related markdown/index/wiki links were updated.

## Safety Checks

Before executing:
- Check that the proposed destination path does not already exist.
- Keep a machine-readable or markdown log of the mapping.
- Avoid changing case only on case-insensitive file systems unless necessary.
- Do not rename files open in another app if that may confuse the user.

After executing:
- Verify old paths no longer exist and new paths do exist.
- Re-run inventory when the rename batch is large.
- Search indexes/wiki pages for old filenames and update links.
