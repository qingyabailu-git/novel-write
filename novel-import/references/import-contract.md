# Novel import contract

## Preview before writing

The preview must show:

- Source path and encoding.
- Number of detected chapter headings.
- Proposed title for each chapter.
- Character count for each segment.
- Text before the first heading and text not assigned to a chapter.
- Any headings that look ambiguous.

## Default file layout

- Preserve the source in a separate location.
- Write imported prose to chapters/.
- Record only the verified source endpoint in setting/progress.md.
- Put confirmed stable entities in lore/.
- Put proposed but unconfirmed entities in the import report, not in lore/.
- Create or update setting/outline.md only when the user confirms a structural outline.
- Create or update setting/character-states.md only for current facts supported by the imported text.

## Split rules

Prefer explicit chapter headings. Keep the heading as the chapter title, remove it from the body only when the output convention requires that behavior, and never discard unmatched text. A custom regular expression may be used for unusual source formats.

## Confirmation gate

Before writing, show the proposed output root, chapter files, metadata, candidate lore, and unresolved text. Require a clear confirmation for the import.
