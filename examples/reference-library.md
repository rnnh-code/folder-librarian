# Example: Reference Library

## Prompt

```text
Use folder-librarian to run a full safe pass on this professional reference archive.
```

## Expected Agent Behavior

The agent should treat the folder as a library, not a normal working folder.

Good top-level structure:

```text
00 Start Here - Reference Library Index.md
01 Core Frameworks
02 Topic Areas
03 Case Studies
04 Templates And Tools
05 Training
90 Original Bundles
98 Needs Review
99 Cleanup Candidates
```

Good index sections:

```md
# Reference Library Index

## What This Folder Contains

Plain-English description of the archive.

## Best First Places To Look

- If you need the main framework: start in `01 Core Frameworks`.
- If you need examples: start in `03 Case Studies`.
- If you need reusable files: start in `04 Templates And Tools`.

## Conversion And OCR

- Ran a curated markdown conversion batch for 15 high-value files.
- Created an OCR shortlist for 3 scanned PDFs.
- Did not bulk-convert the full folder.

## Review Areas

- `98 Needs Review`: unclear files and screenshots.
- `99 Cleanup Candidates`: system files, partial downloads, duplicate-looking files.
```

## Notes

Reference libraries should be organized by retrieval need. Avoid sorting by file type unless the file type is the actual retrieval question.
