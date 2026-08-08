---
name: novel-lore
description: 管理文件化小说项目中的长期设定，包括角色、世界规则、地点、势力、能力和重要物品。用户要添加、查询、修改、合并或删除长期故事事实时使用。
---

# Novel Lore

Maintain a small, reliable long-term canon for a novel.

## Authority boundaries

Stable lore may contain identity, personality, background, durable relationships, ability limits, world rules, recurring places, factions, and important objects.

Keep current position, temporary injury, current mood, immediate goal, temporary inventory, chapter summary, and future plot plans outside lore. Use progress.md, character-states.md, outline.md, or chapter groups for those purposes.

## Workflow

1. Locate the project root and the current lore directory or index.
2. Read the index or filenames first. Do not load every lore document unless the user asks for a complete audit.
3. Read only the entries relevant to the current request and label facts by source: user input, existing canon, or inference.
4. For a new or changed entry, prepare a concise proposed record with type, name, aliases, keywords, stable facts, and uncertainty.
5. Write only when the user asks to save or when the current writing task explicitly confirms a stable canon change.
6. For updates, preserve unrelated fields and replace the complete entry rather than silently dropping facts.
7. For deletion, require an explicit deletion request and report the exact identifiers removed.
8. Read back changed files and check that no temporary state or future plot was accidentally added.

## Safe behavior

- Never present an inferred fact as confirmed canon.
- Never rewrite the whole lore collection for a one-entry change.
- Do not update lore merely because a chapter advanced.
- Do not claim persistence when the platform could only return a proposed patch.

## Output

When reading, report the entries used. When proposing changes, show the proposed entry and its reason. When writing, report the paths or identifiers changed and the read-back result.

Read references/lore-boundaries.md for the recommended entry shape and examples.
