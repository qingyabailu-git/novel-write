---
name: novel-project-init
description: 初始化或修复文件化小说项目，建立经确认的创作规则、长期设定、故事大纲、写作进度、角色状态和章节目录。用户要开始新书、导入项目骨架或在写正文前建立项目规范时使用。
---

# Novel Project Init

Initialize a durable, file-backed novel project without inventing unconfirmed canon.

## Workflow

1. Inspect the selected project root before creating anything. Preserve existing files and identify the current authoritative chapter, setting, and lore locations.
2. If the project is new or its contract is missing, gather the minimum facts: genre, premise, protagonist, core conflict, world rules, narrative viewpoint, prose preferences, length, content boundaries, and workflow preferences.
3. If important information is missing, ask focused questions. Do not fill gaps with invented facts.
4. Prepare a concise confirmation plan listing the files to create, the canon to record, unresolved decisions, and content that will remain unknown.
5. Write only after the user explicitly confirms the plan or clearly asks to save it.
6. Create the project structure described in references/project-layout.md. Keep CREATOR.md focused on durable writing rules; keep story facts in lore; keep temporary state in the state files.
7. Read back every created or changed file and verify headings, encoding, and key facts. Report any file that could not be persisted.

## Write boundaries

- Do not write a chapter during initialization.
- Do not create future plot details that the user did not confirm.
- Do not duplicate the full lore database inside CREATOR.md.
- Do not overwrite an existing project contract without showing the intended changes.
- If the platform cannot write files, return ready-to-save files or patches and state that nothing was persisted.

## Completion report

Report the project root, files created or updated, confirmed canon, unresolved decisions, and verification result. Keep the report short.

Read references/project-layout.md when deciding file ownership or initialization output.
