# Novel write

A portable ChatGPT/Codex skill suite for file-backed novel projects.

> Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

## What This Is

Novel write breaks novel work into reusable, reviewable, and resumable stages: import, project initialization, lore management, long-term outlining, short-term chapter planning, writing, continuation, revision, review, and style management.

The suite is designed for projects whose authoritative material lives in a directory. It keeps prose, stable canon, current state, future plans, and review reports separate so later writing can be checked against what actually happened.

The workflow is confirmation-driven whenever a write could establish canon, change the story direction, or create substantive prose. It distinguishes confirmed facts from candidates, plans, inferences, and unresolved decisions. The review skill is read-only; repairs are handled by a separate rewrite step after authorization.

## Included Skills

| Skill | Purpose |
| --- | --- |
| novel-workflow | Orchestrates the end-to-end file-backed novel workflow. |
| novel-project-init | Creates or repairs the project contract and file layout. |
| novel-lore | Maintains stable characters, places, rules, factions, abilities, and items. |
| novel-outline | Designs and updates long-term story structure. |
| novel-chapter-plan | Plans the next short-term group of chapters. |
| novel-write | Writes fragments, scenes, or chapters at an appropriate depth. |
| novel-continue | Continues from the actual latest chapter and current state. |
| novel-rewrite | Performs targeted revisions while preserving continuity. |
| novel-review | Runs a read-only, evidence-based quality gate. |
| novel-import | Previews and structures TXT or Markdown source material. |
| novel-style | Defines reusable prose behavior without storing plot canon. |

## Package Layout

Each skill directory contains the following components when applicable:

~~~text
novel-*/
├── SKILL.md                 # Main instructions
├── agents/openai.yaml       # Interface metadata
├── references/              # Reusable contracts and formats
└── scripts/                 # Local helper scripts
~~~

The root manifest is novel-write.json. It records the package name, display name, version, included skills, excluded features, and release notes.

## Design Principles

### 1. File-backed continuity

Actual chapter prose is the primary evidence of events. Progress, character state, lore, outline, and chapter groups have separate ownership and must not silently replace one another.

### 2. Confirmation before canon

Import previews, project initialization, structural plans, and broad style changes are shown before persistence. Unconfirmed candidates and future plans remain explicitly marked.

### 3. Continuity at the action level

Reviews and writing passes trace time, place, viewpoint knowledge, physical condition, action ownership, object location, device procedures, and real-world constraints.

### 4. Dialogue under pressure

Each question or answer should respond to the preceding action, information, or intent. Evasion should be visible through behavior, distance, pauses, or viewpoint inference rather than unexplained topic changes.

### 5. Concrete scene shape

Openings establish the minimum event context. Suspense may show an anomaly or result before its cause. Endings point to a concrete next action, choice, discovery, or answerable question.

### 6. Adaptive serial pacing

For multi-threaded serial fiction, active lines can be labeled as primary, stable, or exploratory to expose stalled threads and repeated low-impact chapters. These are editorial heuristics, not universal frequency rules.

## Typical Workflow

~~~text
Source or existing project
        ↓
Import preview or project inspection
        ↓
Confirmed project contract and style
        ↓
Long-term outline
        ↓
Short-term chapter group
        ↓
Write or continue
        ↓
Read-only review
        ↓
Authorized revision and state write-back
~~~

The orchestration skill can move through these stages without asking the user to manually choose each lower-level skill. It still pauses at decisions that would establish canon, change project direction, or write substantive content.

## Review and Quality Gates

The review process checks:

- user requirements, protected material, and content boundaries;
- time, place, sequence, objects, injuries, knowledge, and causality;
- character motivation, decision pressure, voice, and behavior;
- actor, target, possession, device state, and physical feasibility;
- dialogue response pressure and meaningful action;
- pacing, escalation, scene openings, suspense order, and concrete hooks;
- vague explanation, repetitive patterns, and observable AI-like prose habits.

Reviews return a pass/fail conclusion, remaining blockers, advisory items, evidence, violated rules, impact, and repair instructions. The review skill does not modify the project.

## Helper Scripts

### split_novel.py

Previews or splits UTF-8 TXT/Markdown files by chapter headings. It supports dry-run and JSON output, preserves unmatched prefix text in the report, and writes only to an explicitly supplied output directory.

### check_novel_project.py

Performs conservative local structure and UTF-8 checks for a file-backed novel project. It reports missing required items, unreadable text, empty chapters, and replacement characters.

Both scripts are local-only and do not make network requests.

## Installation

1. Copy the desired novel-* directories into a Codex-compatible skill directory.
2. Preserve each directory's SKILL.md file.
3. Keep agents/openai.yaml and references/ beside the main instruction when the host supports them.
4. Keep scripts/ available for import and structural checks.
5. Start with novel-workflow for a guided end-to-end process, or invoke a focused skill directly.

## Scope and Privacy

This package contains only skill instructions, reusable references, local helper scripts, interface metadata, and package metadata. It does not contain:

- novel prose or chapter files;
- character dossiers, lore databases, or world settings;
- private project paths, author notes, browser data, credentials, or API keys;
- illustrations, covers, interactive images, interactive stories, story directors, or scheduled automation execution.

When using the skills, treat the selected project and the user's current explicit materials as the source boundary. Do not fill gaps with unrelated projects, old summaries, or unconfirmed assumptions.

## Example Import Case

The repository includes a derived import-decomposition case for a user-provided Chinese TXT source:

- English case notes: [examples/import-case/shentongzhe/README.md](examples/import-case/shentongzhe/README.md)
- Chinese case notes: [examples/import-case/shentongzhe/README.zh-CN.md](examples/import-case/shentongzhe/README.zh-CN.md)

The case demonstrates metadata extraction, chapter-heading detection, front-matter handling, candidate-lore separation, endpoint tracking, and unresolved-hook reporting. The original TXT, full chapter bodies, and long quotations are intentionally not included.

## Version and License

- Package version: 1.2.0
- Display name: Novel write
- Manifest: novel-write.json
- License: MIT; see [LICENSE](LICENSE)

The included MIT license is the standard license identified by SPDX as MIT. Review the copyright-holder line before publication if a different holder name is required.
