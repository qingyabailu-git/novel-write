---
name: novel-chapter-plan
description: 规划接下来三到八章的短期剧情组，安排冲突升级、信息揭示、章节钩子和伏笔推进。用户询问接下来几章写什么或要生成章节组细纲时使用。
---

# Novel Chapter Plan

Create one short-term chapter group from the actual current project state.

## Workflow

1. Read setting/outline.md, setting/progress.md, setting/character-states.md, relevant lore, and the most recent two non-empty chapters.
2. Read the previous one or two chapter-group files when available, only to compare planned and actual events.
3. Locate the actual latest chapter from the chapter files, not from progress.md alone.
4. Compare the current story against the long-term outline.
5. If the story has materially diverged, explain the divergence and ask whether to realign or continue from the current reality. Do not hide the conflict.
6. Plan only the next group. Do not generate a backlog of many groups unless explicitly requested.
7. Use the format in references/chapter-plan-format.md.
8. Write setting/chapter-groups/groupXX-topic.md only when the user asks to save it, then read it back.

## Planning constraints

- Prefer 3 to 8 chapters, adjusted to the actual arc.
- Keep the plan concise, normally about 800 to 1200 Chinese characters.
- Give every chapter a goal, conflict or payoff, reveal, and ending hook where appropriate.
- Make each ending hook a concrete next action, choice, discovery, or answerable question rather than a generic continuation.
- For a multi-threaded serialized story, label the active threads by role when useful (for example, primary escalation, stable relationship, or new thread). Use this to detect stalled lines and repeated low-impact chapters, not to impose a fixed payoff frequency on every genre.
- Keep future details out of lore and keep current state out of the long-term outline.
- Do not write prose chapters or update progress and character state during planning.

## Output

Return the proposed group, the current-state assumptions it relies on, unresolved choices, and any outline divergence. Do not claim a file was created unless it was read back successfully.

Read references/chapter-plan-format.md for the output schema.
