# Example: Rename Plan

## Prompt

```text
Use folder-librarian to propose clearer filenames for these documents. Do not rename them yet.
```

## Expected Agent Behavior

The agent should create a dry-run proposal before changing filenames.

Good output shape:

```md
# Rename Proposal

| Current path | Proposed path | Reason | Confidence |
| --- | --- | --- | --- |
| `final_final2.pdf` | `Q4 Budget Review - Final - 2025.pdf` | Title page identifies the document; current name is vague. | High |
| `scan001.pdf` | `Lease Agreement - 2024-06-01.pdf` | First page title and date are clear. | Medium |
| `deck.pptx` | Needs review | Deck topic is unclear without opening slides. | Low |
```

## Execution Rules

- Do not execute renames until approved.
- Preserve file extensions.
- Preserve dates, versions, source names, regions, and document type cues when useful.
- Do not rename ambiguous files just to make them look clean.
- When renames are executed, create or update `00 Rename Log.md`.

## Good Rename Log Shape

```md
## [YYYY-MM-DD] controlled rename

| Old path | New path | Reason | Links updated |
| --- | --- | --- | --- |
| `final_final2.pdf` | `Q4 Budget Review - Final - 2025.pdf` | Improved recall and search. | Yes |
```
