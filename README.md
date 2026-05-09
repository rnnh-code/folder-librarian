# Folder Librarian

Folder Librarian is an AI-agent skill for turning messy folders into useful retrieval systems.

It is designed for local folders such as Downloads piles, old backups, work archives, reference libraries, admin records, creative/media folders, data folders, and knowledge vaults.

The core idea: a good folder is not just tidy. It should help someone find, trust, and reuse files later.

## What It Helps Agents Do

- Inspect a folder before moving anything.
- Diagnose the folder type: active work, reference library, admin records, media, data, backup dump, or knowledge vault.
- Recommend or create a small, durable folder structure.
- Create `00 Start Here` indexes for archives and libraries.
- Quarantine uncertain files instead of deleting them.
- Propose safer rename plans.
- Run small curated markdown conversion or OCR passes when useful tools are available.
- Build optional wiki/synthesis layers for durable reference libraries.

## Safety Model

The skill is intentionally conservative.

Agents should ask before:

- Deleting files.
- Deduplicating files.
- Unzipping or extracting archives.
- Bulk-converting large folders.
- Running large OCR batches.
- Renaming original source files.
- Making irreversible or externally visible changes.

For uncertain files, the preferred move is review/quarantine, not deletion.

## Repository Layout

```text
skills/
  folder-librarian/
    SKILL.md
    agents/
      openai.yaml
    scripts/
      inventory_folder.py
    references/
      conversion-rules.md
      folder-types.md
      knowledge-wiki-mode.md
      organization-patterns.md
      rename-rules.md
```

## Install

After this repo is published to GitHub, install it with the Skills CLI:

```bash
npx skills add <github-user>/folder-librarian --skill folder-librarian -g
```

For a local checkout, point your agent directly at:

```text
skills/folder-librarian/SKILL.md
```

or copy the `skills/folder-librarian` folder into your agent's skills directory.

## Example Prompts

```text
Use folder-librarian to review this old Downloads folder and propose a structure. Do not move anything yet.
```

```text
Use folder-librarian to run a full safe pass on this project archive.
```

```text
Use folder-librarian to create a Start Here index and identify files that need human review.
```

```text
Use folder-librarian to propose clearer filenames for these vague PDFs, but do not rename them yet.
```

## Optional Helper Script

The skill includes a read-only inventory helper:

```bash
python3 skills/folder-librarian/scripts/inventory_folder.py "/path/to/folder"
```

It reports totals, top extensions, largest files/folders, duplicate filenames, cleanup candidates, and risk flags. The script does not move, rename, delete, unzip, or convert files.

## Development Checks

Validate the skill metadata:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/folder-librarian
```

Run the helper script against a harmless sample folder before publishing changes.

## License

MIT
