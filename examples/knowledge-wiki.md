# Example: Knowledge Wiki

## Prompt

```text
Use folder-librarian to turn this cleaned-up research library into a small wiki layer.
```

## Expected Agent Behavior

The agent should preserve raw sources and create a generated markdown layer.

Good output shape:

```text
00 Wiki/
  index.md
  log.md
  Overview.md
  Core Concepts.md
  People And Organizations.md
  Open Questions.md
```

Good `index.md` shape:

```md
# Wiki Index

## Overview

- [Overview](Overview.md): High-level map of the research library.

## Concepts

- [Core Concepts](Core Concepts.md): Durable ideas and frameworks found across sources.

## Open Loops

- [Open Questions](Open Questions.md): Gaps, contradictions, and questions worth investigating.
```

Good `log.md` shape:

```md
## [YYYY-MM-DD] ingest | Initial research library pass

- Created initial wiki layer.
- Used 12 converted markdown files and 3 source PDFs.
- Flagged two image-heavy sources for visual review.
- No raw sources were edited.
```

## Notes

The wiki is generated and useful, but raw sources remain the source of truth. OCR-derived text should be treated as lower-confidence unless visually checked.
