# Example: Downloads Cleanup

## Prompt

```text
Use folder-librarian to run a full safe pass on my Downloads folder.
```

## Expected Agent Behavior

The agent should inspect first, then continue through low-risk cleanup without asking after every small step.

Good output shape:

```md
## Inventory

- 842 files, 31 folders, 18.4 GB.
- 213 root-level files.
- Top file types: PDF, PNG, ZIP, DMG, DOCX, MP4.
- Risk flags: duplicate-looking names, installers, screenshots, partial downloads, old zips.

## Actions Taken

- Created `00 Start Here - Downloads Index.md`.
- Created `01 Active`, `02 Documents`, `03 Media`, `04 Installers`, `90 Archives`, `98 Needs Review`, `99 Cleanup Candidates`.
- Moved obvious screenshots to `98 Needs Review/Screenshots`.
- Moved obvious installers to `04 Installers`.
- Moved partial downloads and system files to `99 Cleanup Candidates`.

## Not Done Without Approval

- No files deleted.
- No duplicate cleanup.
- No archives extracted.
- No bulk conversion.
```

## Notes

For Downloads folders, the skill should prefer shallow buckets and review folders. It should not build a complicated taxonomy from random downloads.
