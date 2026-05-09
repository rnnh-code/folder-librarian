# Folder Librarian

Folder Librarian is an AI-agent skill for turning messy local folders into useful retrieval systems.

It is for agents working with real folders: Downloads piles, old backups, work archives, reference libraries, admin records, creative/media folders, data folders, and knowledge vaults.

The core idea: a good folder is not just tidy. It should help someone find, trust, and reuse files later.

## Who This Is For

This repo is for AI agents and people who use agents to manage local files. It is not a standalone app.

Use it when an agent needs a disciplined workflow for:

- Inspecting a messy folder before making changes.
- Choosing a folder structure based on how files will be retrieved later.
- Creating a plain-English `00 Start Here` index.
- Moving obvious files into useful buckets.
- Quarantining unclear files instead of deleting them.
- Proposing safer filename improvements.
- Running small curated markdown conversion or OCR fallback passes when tools are available.
- Building optional wiki/synthesis layers for durable reference libraries.

## Default Behavior

For action requests, the skill runs a **full safe pass**:

1. Inventory the folder.
2. Diagnose the folder type.
3. Create or update an index when useful.
4. Create clear top-level buckets.
5. Move only obvious files/folders.
6. Put uncertain items into review/quarantine folders.
7. Run a small curated conversion batch when useful tools exist.
8. Create an OCR shortlist or tiny OCR fallback for weak/scanned files when appropriate.
9. Propose rename plans when filenames block recall.
10. Optionally create synthesized notes or a wiki layer.
11. Re-run inventory and report what changed.

For advisory requests, such as "give me your thoughts" or "do not change files yet," the skill stays read-only and gives a plan.

## Safety Model

The skill is intentionally conservative. Agents should pause for approval before:

- Deleting files.
- Deduplicating files.
- Unzipping or extracting archives.
- Bulk-converting large folders.
- Running large OCR batches.
- Renaming original source files.
- Making irreversible or externally visible changes.

For uncertain files, the preferred move is review/quarantine, not deletion.

## Tool-Agnostic Design

Folder Librarian does not require a specific converter, OCR engine, or visual inspection tool.

The skill tells agents to use whatever is available in the local environment, such as:

- Markdown conversion: MarkItDown, Pandoc, document-specific parsers, built-in agent tools.
- OCR: PaddleOCR, Tesseract, cloud OCR, built-in vision.
- Visual review: local preview tools, screenshots, browser/computer-use tools, model vision.

The author's local setup currently uses **MarkItDown** for markdown conversion and **PaddleOCR** as an OCR fallback. Those are examples, not requirements.

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
examples/
  downloads-cleanup.md
  reference-library.md
  knowledge-wiki.md
  rename-plan.md
```

## Install

Install from GitHub with a skills-compatible agent CLI, or copy the skill folder into your agent's skills directory.

```bash
npx skills add rnnh-code/folder-librarian --skill folder-librarian -g
```

For a local checkout, point your agent directly at:

```text
skills/folder-librarian/SKILL.md
```

## Example Prompts

```text
Use folder-librarian to run a full safe pass on this old Downloads folder.
```

```text
Use folder-librarian to review this project archive and propose a structure. Do not move anything yet.
```

```text
Use folder-librarian to create a Start Here index and identify files that need human review.
```

```text
Use folder-librarian to propose clearer filenames for these vague PDFs, but do not rename them yet.
```

```text
Use folder-librarian to create a small wiki layer from this cleaned-up research library.
```

See [examples/](examples/) for lean examples of expected agent behavior.

## Helper Script

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
