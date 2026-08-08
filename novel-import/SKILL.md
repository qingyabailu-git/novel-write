---
name: novel-import
description: 预览并整理已有的 TXT 或 Markdown 小说，完成章节拆分、元数据整理、候选设定提取和初始进度建立。用户要导入旧小说以便续写、改稿或结构化分析时使用。
---

# Novel Import

Import existing prose without destroying the source or inventing canon.

## Workflow

1. Confirm the source file, intended project root, encoding, desired chapter split behavior, and whether the user wants continuation, revision, or analysis.
2. Preserve the original source. Work in a new target directory or a clearly named imported copy.
3. Run or emulate scripts/split_novel.py in dry-run mode first. Show the detected chapter headings, counts, and unsplit remainder.
4. Identify metadata that is explicitly present: title, author, description, chapter titles, and source language.
5. Separate candidate lore from confirmed lore. Do not silently promote inferred facts or future plot details into canon.
6. Present an import plan listing output files, candidate lore entries, and unresolved issues.
7. Write only after the user confirms the plan.
8. Read back representative chapters, metadata, and state files. Report encoding or split problems.

## Default output

Use the project structure described in references/import-contract.md:

- chapters/ for imported prose.
- setting/outline.md only for a confirmed long-term structure.
- setting/progress.md for the actual imported endpoint.
- setting/character-states.md for current state that can be proved from the source.
- lore/ for stable, confirmed entities.

Do not generate a complete outline or lore database merely because the source is long. Offer candidates and let the user confirm.

## Safety

- Do not overwrite the source.
- Do not discard unmatched text during splitting.
- Do not claim all chapters were imported if the split preview found unassigned text.
- If the platform cannot write files, return the preview and a reproducible import plan instead.

Read references/import-contract.md before writing an imported project.
