# Novel project layout

Use the existing project convention when one exists. For a new file-backed project, use this separation:

## Files and ownership

- CREATOR.md: durable writing rules, viewpoint, voice, pacing, formatting, boundaries, and author-confirmed process rules.
- setting/outline.md: long-term premise, volumes, chapter goals, major arcs, and foreshadowing direction.
- setting/progress.md: actual latest chapter, completed chapter summaries, recent events, and short-term handoff notes.
- setting/character-states.md: current location, body, mind, goals, knowledge, possessions, relationships, and unresolved hooks.
- setting/chapter-groups/: one short-term group plan per file, normally 3 to 8 chapters.
- chapters/: actual prose, treated as the primary record of events.
- lore/: stable entity records such as characters, places, factions, rules, and items.
- reviews/: optional read-only review reports and repair plans.

## Update matrix

| Task | May update | Must not silently update |
| --- | --- | --- |
| Project initialization | CREATOR.md, initial lore, outline, empty state files | Chapters |
| Long-term outlining | outline.md, proposed lore candidates | Progress and current state |
| Chapter-group planning | chapter-groups/ | Chapters, progress, character state |
| New chapter | chapters/, progress, character state, immediate hooks | Long-term outline |
| Substantive rewrite | target chapter, progress, character state | Long-term outline unless requested |
| Stable canon change | lore entry after confirmation | Temporary state |
| Review | review report only | Any project file |

If the platform cannot persist files, return the intended file contents or a patch and explicitly state that persistence did not occur.
