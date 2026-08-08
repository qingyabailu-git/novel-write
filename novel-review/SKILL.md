---
name: novel-review
description: 独立审查小说章节或短篇剧情的连续性、设定、人物逻辑、节奏、语言、对白、文风、格式和用户要求。用户要严格审稿、最终门禁、AI味检查或带证据的阻塞项与建议项报告时使用。
---

# Novel Review

Perform a read-only, evidence-backed quality gate.

## Workflow

1. Confirm the review scope and locate the authoritative project root and target chapters.
2. Read CREATOR.md, outline, progress, character state, relevant chapter groups, relevant lore, the target text, and enough preceding and following text to test continuity.
3. Run scripts/check_novel_project.py when it is available and record whether it ran successfully. Static checks supplement but do not replace close reading.
4. Review the target against references/review-rubric.md.
5. Separate confirmed problems from uncertain concerns. Cite the exact file path and line, paragraph, or distinctive text.
6. For action-heavy scenes, trace time, place, action ownership, object/device state, physical constraints, and the handoff into the next action or line.
7. Return the verdict first. List only remaining blocking issues and advisory issues unless the user asks for praise or a full review log.
8. Give a concrete fix instruction for every blocker. Do not rewrite or modify files during a read-only review.

## Required report shape

Use:

Conclusion: pass or fail

Blocking:

- path and location
- evidence
- violated rule or continuity fact
- impact
- exact repair instruction

Advisory:

- path and location
- evidence
- risk
- optional improvement

## Integrity rules

- Do not call an issue fixed unless the current file proves it is fixed.
- Do not claim a check passed when it was not run or was incomplete.
- Do not treat a style preference as a continuity blocker unless the project contract makes it mandatory.
- Do not call AI-style detection proof of authorship; report observable prose patterns instead.

This Skill is strictly read-only.
