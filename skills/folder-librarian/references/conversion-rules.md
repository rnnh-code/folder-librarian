# Conversion Rules

Use this reference before recommending markdown conversion, OCR/image handling, unzip work, duplicate cleanup, or markdown reference layers.

## Read Local Tool Notes First

If the workspace or machine has a local tool guide, read it before conversion work. Common examples include `AGENT_TOOLS.md`, `AGENTS.md`, `CLAUDE.md`, project README files, or other local instructions that explain available converters, OCR tools, image/table handling, and what to avoid.

## When To Use Markdown Conversion

Use MarkItDown, pandoc, document-specific parsers, or another available converter for high-value files that should become searchable or easy for agents to reference later:
- Strategy decks and playbooks.
- Training guides and frameworks.
- Reports, briefs, and meeting notes.
- Text-heavy PDFs, DOCX, PPTX, XLSX, CSV, HTML, and ZIP archives worth inspecting.

Save useful markdown copies next to the original with the same base name:

```text
Brand Framework.pdf
Brand Framework.md
```

In Full Safe Pass Mode, conversion is part of the default workflow when useful source files exist. Run a small curated first batch, usually 10-25 files, unless the user explicitly says not to convert. If the folder is too ambiguous, propose the batch instead of skipping conversion silently.

## OCR Fallback

Use PaddleOCR, Tesseract, cloud OCR, built-in vision, or another available OCR method only after normal conversion is weak or clearly unsuitable.

Good OCR candidates:
- Scanned PDFs.
- Image-only PDFs.
- Screenshots with important text.
- Photos of documents.
- Decks or PDFs where visible text is embedded as images.

Treat conversion output as weak when it is empty, near-empty, mostly metadata, obviously missing visible text, or too small for the apparent source document. Do not OCR tiny outputs blindly; first check whether the source is simply a short document.

In Full Safe Pass Mode, OCR may run on up to 5 high-value failed/weak converted files. If more than 5 files need OCR, create an OCR shortlist and ask before continuing.

Save OCR output next to the original as a separate file:

```text
Source.pdf
Source.md
Source.ocr.md
```

Do not replace normal `.md` conversion files with OCR output. Add a short note at the top of `.ocr.md` files saying the text was OCR-generated and may need review.

OCR output may feed indexes, wiki pages, and synthesized notes, but treat it as lower-confidence evidence unless visually checked. For important charts, tables, diagrams, or claims, use visual inspection in addition to OCR.

## When Not To Bulk-Convert

Do not convert everything just because the tool exists. Bulk conversion can create a second messy archive.

Avoid automatic conversion for:
- Throwaway transactional files.
- Files unlikely to be reused.
- Image-heavy decks where layout carries the meaning.
- Screenshots with no clear future use.
- Scanned PDFs where automated extraction returns little or nothing.
- Videos unless a specific transcript is needed.

## Images, Scans, And Tables

Automated converters may miss visual meaning, complex tables, scanned text, or screenshots. When visual content matters, inspect the image or rendered page directly and state what was captured manually.

Never pretend a markdown file fully represents a visual deck or scanned document unless visual review or OCR was actually performed.

## Videos

Keep videos in a video archive or training archive by topic. Transcribe only selected high-value videos. Do not mix large raw video files into the main reference flow unless they are the core material.

## Zips And Original Bundles

Preserve original zips and export bundles. If contents are extracted, keep the zip under an original/source bundle area unless the user explicitly asks to delete it.

## Duplicates

Duplicate filenames are only a clue. They are not proof that files are identical. Compare size, path, modified time, and content hash before recommending deletion.

Prefer `Possible Duplicates` or `Cleanup Review` over deletion.

## Partial Downloads And System Files

Files ending in `.partial` and `.DS_Store` are cleanup candidates, but still report them before deleting. In old backups, even junk cleanup should be explicit and reversible.
