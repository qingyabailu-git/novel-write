---
name: novel-outline
description: 创建或修改小说的长期大纲，包括故事前提、分卷结构、章节目标、人物成长线、核心冲突和伏笔布局。用户要构建新故事或调整长期方向时使用。
---

# Novel Outline

Design the long-term story structure without mixing it with current progress.

## Workflow

1. Inspect the project root, CREATOR.md, existing lore, current outline, and recent progress when the project already exists.
2. Identify the requested scope: new outline, local structural change, volume redesign, chapter-level change, or premise repair.
3. Preserve confirmed canon and mark contradictions or unresolved choices before drafting.
4. Produce a concise outline with premise, core conflict, volume arc, chapter goals, character movement, and foreshadowing.
5. Keep each chapter summary focused on its core event and dramatic function.
6. If the user asks for a file change, edit only the requested structural section and read the result back.

## File boundaries

- Store the durable outline in setting/outline.md unless the project has an established alternative.
- Store current progress in setting/progress.md.
- Store current character facts in setting/character-states.md.
- Store short-term chapter groups in setting/chapter-groups/.
- Store stable entity facts in lore.
- Do not put completed-chapter recaps, temporary injuries, or future detailed scenes into the long-term outline.
- Do not silently rewrite the whole outline because one chapter changed.
- Do not create chapters while planning.

## Output

Return the outline or a focused change proposal first. If writing to disk, report the exact file and structural sections changed. Call out any downstream chapters or canon that may need review.

Read references/outline-format.md for the recommended outline shape.
