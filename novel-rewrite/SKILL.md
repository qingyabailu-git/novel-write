---
name: novel-rewrite
description: 在保留指定故事事实、人物声线、叙事视角和连续性的前提下修改已有小说正文。用户要重写、扩写、缩写、调整对白、切换视角或改变文风时使用。
---

# Novel Rewrite

Make the smallest effective revision that satisfies the user's requested change.

## Workflow

1. Identify the exact target file, passage, and requested change. If the target is ambiguous, ask for the path or quote a short identifying passage.
2. Read the target, the relevant preceding and following context, CREATOR.md, outline, progress, character state, chapter group, and relevant lore.
3. Classify the change: dialogue, plot, viewpoint, expansion, compression, pacing, voice, or structural repair.
4. Preserve all user-protected content, valid plot beats, established facts, strong paragraphs, and character voice unless the request explicitly replaces them.
5. Draft the revised passage or chapter and check forward and backward continuity.
6. Write only the requested file or passage when persistence is requested. Use precise edits for local changes and a full replacement only for a full-chapter rewrite.
7. If the revision changes what happened, update progress.md and character-states.md from the revised final text.
8. If stable canon changed, propose a separate lore patch. Do not silently alter the long-term outline.
9. Read back every changed file and report any downstream chapters that may be affected.

## Guardrails

- Do not turn a targeted repair into a different story.
- Do not remove ambiguity that the user asked to preserve.
- Do not use a style reference to introduce new plot facts.
- Do not claim a revision was saved when persistence or read-back failed.
- If the user asks for analysis only, do not modify the text.

Read references/rewrite-matrix.md to choose the right preservation and state-update behavior.
