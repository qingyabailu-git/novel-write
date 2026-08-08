# Import Case: Shentongzhe

> Chinese case notes: [README.zh-CN.md](README.zh-CN.md)

## Purpose

This is a derived import-decomposition case built from a user-provided Chinese TXT source. It demonstrates how Novel write can preview a source, separate front matter from narrative chapters, preserve explicit metadata, keep candidate lore unconfirmed, and record the actual import endpoint.

The original TXT is intentionally not included in this repository. This directory contains metadata and structural analysis only; it is not a redistribution of the source novel and it is not canon for any other project.

## Source Preview

- Title in source: 神通者
- Author attribution in source: 天蚕土豆
- Source identifier: 7665193065501445145
- Status in source: serial
- Category in source: traditional xuanhuan
- Stated word count: 45,863
- Stated chapter count: 13
- Encoding check: UTF-8, no BOM detected, no replacement characters
- Detected chapter headings: 13
- Text before the first heading: 209 characters
- Local split total: 51,018 characters across detected blocks

The source's own word-count field and the local split character total are different measurements. An import report should preserve both labels instead of silently replacing one with the other.

## Detected Chapter Blocks

| # | Source heading | Characters | Import classification |
| ---: | --- | ---: | --- |
| 1 | 第0章 新书感言 | 1,303 | Front matter / author note |
| 2 | 第1章 雷火馆 | 7,008 | Narrative chapter |
| 3 | 第2章 神通骨 | 4,725 | Narrative chapter |
| 4 | 第3章 次天品神通骨 | 5,577 | Narrative chapter |
| 5 | 第4章 佛怒火莲 | 3,323 | Narrative chapter |
| 6 | 第5章 机缘在身 | 4,257 | Narrative chapter |
| 7 | 第6章 钟缨，景仪 | 3,431 | Narrative chapter |
| 8 | 第7章 黎家，黎妍 | 2,990 | Narrative chapter |
| 9 | 第8章 方浪 | 4,932 | Narrative chapter |
| 10 | 第9章 陆鸣带来的一点小震撼 | 3,387 | Narrative chapter |
| 11 | 第10章 神通前四境 | 3,600 | Narrative chapter |
| 12 | 第11章 宗师法网 | 3,335 | Narrative chapter |
| 13 | 第12章 高玉 | 3,150 | Narrative chapter |

## Proposed Import Handling

If the source were imported into a private novel project, the recommended plan would be:

1. Preserve the original source in a separate, clearly named location.
2. Keep the 209-character prefix in the import report and inspect it as metadata or front matter.
3. Store the author note separately from the narrative chapter sequence, unless the project explicitly wants it as chapter content.
4. Split the 12 narrative chapters using the source headings.
5. Record source metadata separately from project canon.
6. Put all extracted characters, places, rules, items, and plot facts into a candidate-lore report.
7. Record the endpoint after Chapter 12 without treating later plans as completed events.
8. Ask the user which candidate facts should become canon before writing lore, outline, progress, or character-state files.

## Candidate Lore and Story State

These are candidates extracted from the source, not confirmed canon:

- Main viewpoint candidate: 陆鸣, a teenage cultivator connected to 雷火馆 and the 陆 family.
- Family and institution candidates: 陆瑾, 陆青炎, 陆惊雷, 钟缨, 陆檬檬, and 雷火馆.
- Conflict candidates: 章岳's departure, pressure from 大金乌馆, the family curse called 封灵咒, and the need to protect the institution's resources.
- Power-system candidates: 神通骨 grades, 炼炁, 炼骨, 法纹, 神通大师, 神通宗师, 神通羽衣, and 宗师法网.
- Inheritance candidates: a black ring, 佛怒火莲, three named fire seeds, 火焰刀, 雷火鞭, 飞鹤信,炼骨丹, and 大圣火符.
- Setting candidates: 青原坊, 凤阳府, 大罗域, 黑雨区, 大金乌馆, 金钟玄罡馆, 黎家, and 景家.
- Relationship candidates: 景仪's connection with 陆鸣, 黎妍's mediation, and the unresolved tension involving 景仪's paternal family.

The source endpoint leaves several hooks unresolved: the new 坊主's arrival in three days, the upcoming 神通馆馆会, the resource shortage, the potential journey into 黑雨区, the family curse, the sealed deeper space in the black ring, and the future confrontation with the forces behind the family's misfortune.

## What This Case Demonstrates

- Do not mistake a source metadata block for a chapter.
- Keep source-reported metadata and locally measured counts separate.
- Preserve unmatched text instead of discarding it.
- Label extracted lore as candidate material until the user confirms it.
- Use the latest narrative endpoint, not a future promise, as the current state.
- Keep a public skill repository free of the original source text and long quotations.
