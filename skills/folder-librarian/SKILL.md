---
name: folder-librarian
description: Inspect, organize, index, clean up, archive, or propose structures for local folders and mixed file collections. Use when an AI agent needs to handle a messy Downloads folder, old backup, work archive, reference library, admin record set, creative/media folder, data/research folder, or knowledge vault; also use before bulk file moves, renames, deduplication, archive extraction, markdown conversion, OCR, or generated wiki/synthesis work.
---

# Folder Librarian

## Core Principle

Treat a folder as a retrieval system, not just storage. Optimize for how the user will find, trust, and reuse files later.

Default to a full safe pass for action-oriented folder requests. Stay read-only when the user asks for thoughts, advice, a review, a plan, or says not to change files yet.

A full safe pass may inspect, organize, index, quarantine, convert a curated markdown batch, propose renames, and build optional wiki/synthesis layers. It must not delete, deduplicate, unzip archives, bulk-convert, run large OCR batches, execute renames, or make irreversible changes unless the user explicitly approves that risky step.

## Operating Modes

Use the user's wording to decide whether to act or advise.

### Plan-First Mode

Use this when the user asks for thoughts, advice, a recommendation, a review, or says not to change files yet.

Inspect the folder, diagnose the folder type, recommend a structure, and wait before changing files.

### Full Safe Pass Mode

Use this by default for action requests such as "organize this folder," "clean this up," "use folder-librarian here," or "run the skill."

Continue through low-risk steps in one run:
- Run an inventory and inspect representative files.
- Create or update a `00 Start Here` index when the folder is a library, archive, vault, or mixed dump.
- Create clear top-level organization folders.
- Move obvious files and folders into retrieval-based buckets when safe.
- Put uncertain files, screenshots, partial downloads, system files, and cleanup candidates into review/quarantine folders instead of deleting them.
- Evaluate whether markdown conversion would make high-value documents easier to reuse.
- If useful, run a small curated conversion batch with the user's available tools.
- If conversion output is weak because files are scanned or image-heavy, create a small OCR shortlist or run a tiny approved OCR fallback when OCR tools are available.
- Create converted-reference indexes or synthesized notes from high-value converted text.
- Create an optional generated wiki layer when the folder is a durable knowledge system, not just a one-time cleanup.
- Create a controlled rename proposal when clearer filenames would materially improve recall.
- Re-run inventory and report what changed.

Pause for approval before:
- Deleting files.
- Deduplicating files.
- Unzipping or extracting archives.
- Bulk-converting large folders.
- Running large OCR batches.
- Renaming original source files unless the user approved a specific rename plan or controlled rename pass.
- Making irreversible or externally visible changes.

Do not ask for confirmation after every low-risk step. If a file is ambiguous, place it in a review area and keep going.

## First Pass

1. State whether you are inspecting only or running a safe pass.
2. Read any local project or machine guidance that governs file handling, conversion, OCR, image/table handling, or archive cleanup.
3. If shell access is available, run the bundled inventory script:

```bash
python3 scripts/inventory_folder.py "/path/to/folder"
```

4. Inspect current folder names and representative filenames before recommending a structure.
5. Identify the job type: organizing, indexing, cleanup, conversion, OCR fallback, controlled rename, dedupe review, knowledge extraction, knowledge wiki, or active-work reset.

## Diagnose The Folder

Classify the folder before choosing a structure. Load `references/folder-types.md` when the folder type is unclear or mixed.

Common folder types:
- Active work: current projects, deliverables, drafts, client work, job search, operating work.
- Reference library: playbooks, training, research, frameworks, examples, old professional archives.
- Admin records: tax, legal, finance, contracts, receipts, healthcare, immigration, HR.
- Creative/media: images, video, audio, design files, assets, exports.
- Data/research: source files, survey data, transcripts, models, analysis outputs.
- Backup/mixed dump: old computer exports, Downloads piles, duplicate bundles, uncertain provenance.
- Knowledge vault: inbox/raw/wiki/index systems, synthesized notes, source logs.

## Choose The Pattern

Load `references/organization-patterns.md` when designing the folder structure.

Choose the organizing principle that matches retrieval:
- Action-based for active work.
- Topic/library-based for durable reference material.
- Time-based for records, exports, events, and periodic reporting.
- Source/origin-based when provenance matters.
- Audience/client-based when handoff or sharing matters.
- Numbered stable areas for large libraries that need long-term navigation.
- Quarantine/review folders for uncertain, duplicate, incomplete, or risky cleanup candidates.

Prefer a small number of clear top-level folders. Add a `00 Start Here` index for libraries, archives, vaults, and mixed dumps.

## Controlled Rename Mode

Use this when filenames block recall. Renaming should improve retrieval, not merely make files look prettier.

Load `references/rename-rules.md` when the user asks to rename files, make filenames clearer, improve recall, standardize names, or when a full safe pass includes a rename proposal.

Default rename posture:
- Start with a dry-run rename proposal unless the user explicitly approves execution.
- Rename only files where the current name is vague, cluttered, misleading, or hard to search.
- Do not bulk-rename an entire folder by default.
- Preserve extensions and useful dates, version numbers, source names, regions, clients, and document type cues.
- Do not rename ambiguous files without review; keep them in a review list instead.
- Log every executed rename with old path, new path, date, and reason.
- Update indexes, wiki links, and markdown references after approved renames.

## Conversion And Cleanup

Load `references/conversion-rules.md` before recommending markdown conversion, OCR/image handling, unzip work, duplicate cleanup, or markdown reference layers.

Default cleanup posture:
- Preserve originals.
- Quarantine instead of delete.
- Keep markdown copies next to originals when converting for future reference.
- Keep OCR output separate from normal markdown conversion output.
- Do not bulk-convert everything; curate high-value files first.
- Call out files that need human review, especially partial downloads, screenshots, old archives, duplicate-looking files, and visual/scanned documents.

In Full Safe Pass Mode, do not skip conversion silently. Always report one of:
- A curated conversion batch was run.
- Conversion was intentionally skipped because there were no high-value reusable documents, tools were unavailable, or the user excluded conversion.
- A conversion plan was proposed because the likely batch was too large or too ambiguous.

For weak conversion outputs, also report one of:
- OCR fallback was run for selected failed/weak files.
- OCR was skipped because the files were low-value, visually better handled by available vision tools, or OCR tools were unavailable.
- An OCR shortlist was created because the batch was too large or too ambiguous.

## Optional Visual Review

Use visual inspection tools when direct preview would improve judgment.

Good uses:
- Preview screenshots before deciding whether they are meaningful references or cleanup candidates.
- Inspect scanned or image-heavy PDFs/decks when conversion returns weak text.
- Inspect complex tables, slide layouts, or embedded visuals that conversion may miss.
- Preview media folders before recommending transcription, conversion, or archival treatment.
- Sanity-check the top-level folder layout after a reorganization.

Avoid visual tools for bulk moves, renames, deletions, deduplication, archive extraction, or repetitive conversion work when filesystem tools are safer.

## Optional Knowledge Wiki Mode

Use this only for folders meant to become durable knowledge systems: reference libraries, research archives, training libraries, business archives, or long-running topic collections.

Load `references/knowledge-wiki-mode.md` when the user asks to build a wiki, playbook, knowledge base, persistent notes layer, compounding synthesis, or when a cleaned-up reference library clearly deserves more than an index.

Core rules:
- Raw source files stay untouched and remain the source of truth.
- The generated wiki is a separate markdown layer, usually `00 Wiki/`.
- Prefer synthesis pages over one summary page per source.
- Maintain both `00 Wiki/index.md` and `00 Wiki/log.md`.
- Use converted markdown and source files as evidence; flag weak conversions, image-heavy sources, contradictions, and stale-looking claims.
- Use OCR-derived text as lower-confidence evidence unless visually checked.
- File useful query answers back into the wiki only when the user wants the insight to persist.

## Output Shape

For advisory requests, answer with:
- Plain-English diagnosis of the folder.
- Recommended structure.
- What should stay untouched.
- What should be indexed, converted, or reviewed.
- Verification or inventory facts that support the recommendation.

For implementation requests, briefly state the safe-pass scope and success checks, then execute unless the user asked for plan-only. After executing changes, report exactly what changed, what was left untouched, and what could not be verified.
