# Knowledge File Format Guide

This guide is the **definitive formatting reference** for every file within `@knowledge/characters/` and `@knowledge/lore/`. Following these rules ensures the RAG system can chunk, embed, and retrieve knowledge accurately and consistently.

> **Scope:** This guide covers `characters/` and `lore/` only. The `personalization/` directory has its own conventions and is excluded.

---

## How the RAG Pipeline Works

Files are split on `## ` (H2) headings — each `## ` section becomes a standalone, searchable chunk. These chunks are embedded into a vector store and retrieved by semantic similarity when a user asks a question. This means:

- A chunk must make sense **on its own**, without relying on the file's H1 title or surrounding sections for context.
- Every chunk must clearly identify **what character or topic** it belongs to.

---

## Core RAG Chunking Rules

1. **Every distinct topic MUST have its own `## ` heading.**
2. **Keep each `## ` section focused on ONE topic** — ideal length is 3–15 lines; never exceed ~50 lines.
3. **Use bullet points and plain text** within sections — avoid deep nesting.
4. **Do NOT use `### ` for sub-topics** — promote them to `## ` instead. The RAG system only splits on `## `.
5. **HTML comments (`<!-- -->`) are stripped and ignored** by the pipeline.
6. **`# ` (H1) headings appear once per file** as the document title. They are NOT used for chunking and must never be repeated.
7. **Every `## ` heading MUST be prefixed with the character name or topic identifier** so that each chunk is self-identifying when retrieved out of context. Use `## Carlotta: Basic Information` — never `## Basic Information`.

---

## YAML Frontmatter Metadata

Every markdown file **MUST** include YAML frontmatter at the beginning of the file to provide metadata for improved RAG search accuracy. The frontmatter is parsed by the RAG system and used for:

- **Importance scoring:** `high`, `medium`, `low` priority for search ranking
- **Character/region identification:** Automatic filtering and boosting
- **Tag-based matching:** Additional keyword matching beyond content

### Required Frontmatter Fields

| Field | Required? | Description | Example |
|-------|-----------|-------------|---------|
| `version` | Yes | Semantic version of the document | `1.0.0` |
| `chunk_strategy` | Yes | Chunking method (always `heading_based`) | `heading_based` |
| `source_file` | Auto-generated | Relative path from `knowledge/` directory | `characters/black_shores/shorekeeper/shorekeeper_kit.md` |
| `document_type` | Yes | Type of document (see table below) | `character_kit` |
| `importance` | Yes | Search priority: `high`, `medium`, `low` | `high` |
| `tags` | Recommended | List of relevant tags | `[character, kit, combat]` |

### Document Type Values

| Category | Document Type | Used For |
|----------|---------------|----------|
| Characters | `character_profile` | `*_character.md` files |
| Characters | `character_kit` | `*_kit.md` files |
| Characters | `character_story` | `*_story.md` files |
| Lore | `region_story` | Regional story files |
| Lore | `region_places` | Geography/location files |
| Lore | `region_territories` | Territory description files |
| Lore | `quest` | Quest files (subtypes: `act`, `prologue`, `segment`) |
| Personalization | `personality` | Personality files |
| Personalization | `backstory` | Backstory files |
| Personalization | `relationships` | Relationship files |
| Systems | `game_mechanics` | Game mechanics files |

### Additional Fields by Document Type

- **Character files:** `character` (character name), `group` (faction/region group)
- **Lore files:** `region` (region name), `quest_type` (for quest files)
- **Personalization files:** No additional required fields

### Frontmatter Format

```yaml
---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/black_shores/shorekeeper/shorekeeper_kit.md
character: Shorekeeper
group: Black Shores
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
---
```

**Placement:** The frontmatter must be the **first content** in the file, before the H1 title. Use exactly `---` on its own line as opening and closing delimiter.

**Generation:** Use the `add_frontmatter.py` script to automatically add frontmatter to existing files. Manual editing should maintain consistency with the schema above.

---

## Universal Formatting Conventions

These rules apply to **all** knowledge files (characters and lore).

| Convention           | Rule                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **File naming**      | `lowercase_snake_case.md` — always `.md` extension                                                                                          |
| **H1 title**         | One per file. Format: `# <Name> — <File Type> Documentation` (characters) or `# <Region> - <Topic>` (lore)                                  |
| **Sources comment**  | Place `<!-- Sources: url1, url2 -->` or `<!-- RAG-optimized: each ## section is a standalone searchable chunk -->` immediately after the H1 |
| **YAML frontmatter** | Place YAML frontmatter at the very beginning of the file (before H1). Required for all files. See YAML Frontmatter Metadata section.        |
| **Heading prefix**   | Every `## ` heading includes the character/topic name for self-identification                                                               |
| **Horizontal rules** | Use `---` between major thematic groups in **lore files only**. Do not use in character files                                               |
| **Bold text**        | `**text**` for key terms, stat labels, NPC names, and field labels                                                                          |
| **Italics**          | `*text*` for direct in-game quotes and official descriptions only                                                                           |
| **Tables**           | Use Markdown pipe tables for structured data (stats, materials, voice actors). Keep each table within a single `## ` section                |
| **Bullet lists**     | Preferred for lists of facts. One level of nesting (`-` then indented `-`) is acceptable; avoid deeper nesting                              |
| **Sources section**  | Every character file MUST end with a `## <Name>: Sources` section listing all reference URLs                                                |
| **Line length**      | No hard line wrapping. One logical paragraph per line is acceptable                                                                         |

---

## Voice Actor Reference

The file `knowledge/characters/voice_actors.txt` is the **single source of truth** for all voice actor data. It is a pipe-delimited table covering EN, CN, JP, and KR voice actors for every character.

- Character files MUST cross-reference this file for accuracy.
- Include only the 4-language entries in each character's Basic Information section; do not duplicate the full table.
- Format in character files:
  ```
  - **Voice Actors:**
    - **JP:** <Name> (<Kanji>)
    - **EN:** <Name>
    - **CN:** <Name> (<Chinese Characters>)
    - **KR:** <Name> (<Hangul>)
  ```

---

## Character File Directory Structure

Each character lives in its own folder inside the appropriate character group directory:

```
knowledge/characters/
├── voice_actors.txt                    (master VA reference)
├── <group>_characters/                 (e.g., ragunna_characters/)
│   └── <character_name>/
│       ├── <name>_character.md
│       ├── <name>_kit.md
│       └── <name>_story.md
```

Every character folder contains exactly three files. The naming convention is `<lowercase_name>_<type>.md`.

---

## Character File: `<name>_character.md`

This file covers identity, appearance, personality, and relationships. All sections below are **required** unless marked optional.

### Required Sections (in order)

**H1 Title:**

```
# <Name> — Character Documentation
<!-- Sources: url1, url2 -->
```

**Section 1 — Basic Information:**

```
## <Name> Profile: Basic Information
- **Name:** <Name> (Chinese: <characters>, <pinyin>)
- **Alias / Title:** <titles, separated by semicolons>
- **Identity:** <one-line ontological description>
- **Affiliation:** <organization or group>
- **Birthplace / Origin:** <location>
- **Release Version:** Wuthering Waves Version X.X
- **Rarity:** 5-Star / 4-Star
- **Element:** <element>
- **Weapon Type:** <weapon>
- **Voice Actors:**
  - **JP:** <Name> (<Kanji>)
  - **EN:** <Name>
  - **CN:** <Name> (<Chinese>)
  - **KR:** <Name> (<Hangul>)
```

**Section 2 — Ontological Overview:**

```
## <Name> Profile: Ontological Overview
```

1–3 paragraphs describing who they are in the world — their nature, role, and significance.

**Section 3 — Appearance Design:**

```
## <Name> — Character/Appearance Design
```

Visual description: hair, eyes, outfit, color palette, dominant motifs, and design philosophy.

**Section 4 — Psychological Profile:**

```
## <Name>: Psychological Profile
```

Personality analysis organized with **bolded trait headers** (e.g., `**Composure Under Pressure**`), each followed by explanatory text.

**Section 5 — Relationships:**

```
## <Name>: Relationships
```

Grouped by person. Each relationship starts with a **bold name header** (e.g., `**Rover (Protagonist)**`) followed by the relationship description.

**Section 6 — Sources:**

```
## <Name>: Sources
- <Source Name> — <URL>
- <Source Name> — <URL>
```

---

## Character File: `<name>_kit.md`

This file covers combat mechanics, abilities, stats, materials, and build recommendations. All sections below are **required** unless marked optional.

### Required Sections (in order)

**H1 Title:**

```
# <Name> Kit Documentation
<!-- Sources: url1, url2 -->
```

**Section 1 — Combat Archetype and Role:**

```
## <Name>: Combat Archetype and Role
- **Element/Attribute:** <element>
- **Weapon Type:** <weapon>
- **Role:** <role description — e.g., "Main DPS — ranged hypercarry dealing heavy Resonance Skill burst damage">
```

**Section 2 — Key Resources:**

```
## <Name>: Key Resources (Forte Mechanics Overview)
```

Brief explanation of the character's unique resource systems and how they interact.

**Section 3 — Forte Circuit Details:**

```
## <Name> Forte Circuit: <Resource Name(s)>
```

Detailed breakdown of the Forte system: resource generation, consumption, thresholds, and state transitions. Include numerical values.

**Section 4 — Stats Baseline:**

```
## <Name>: Stats Baseline
```

Table of base stats at key levels (Lv. 1, Lv. 90, etc.). Use a Markdown table.

**Section 5 — Ascension Materials:**

```
## <Name>: Ascension Materials
```

Table of materials required per ascension level.

**Section 6 — Basic Attack:**

```
## <Name>: Character Kit: Basic Attack — <Attack Name>
```

Attack chain breakdown with stage-by-stage multipliers and mechanics.

**Section 7 — Resonance Skill:**

```
## <Name>: Character Kit: Resonance Skill — <Skill Name>
```

Skill mechanics, cooldowns, damage multipliers, and conditional effects.

**Section 8 — Resonance Liberation:**

```
## <Name>: Character Kit: Resonance Liberation — <Liberation Name>
```

Liberation mechanics, activation conditions, damage multipliers, and state changes.

**Section 9 — Inherent Passives:**

```
## <Name>: Inherent Passives
```

Each passive described with trigger conditions, effects, and numerical values.

**Section 10 — Intro/Outro Skills:**

```
## <Name>: Intro/Outro Skills
```

Transition skill descriptions with damage values and utility effects.

**Section 11 — Skill Upgrade Materials:**

```
## <Name>: Skill Upgrade Materials
```

Table of level-up materials per skill tier.

**Section 12 — Resonance Chains:**

```
## <Name>: Resonance Chains (Sequences)
```

S1 through S6 descriptions with effects, numerical values, and evaluation of each sequence's impact.

**Section 13 — Recommended Echo Sets:**

```
## <Name>: Recommended Echo Sets
```

Best Echo set combinations with reasoning, main stat and sub-stat priorities.

**Section 14 — Best Weapon:**

```
## <Name>: Best Weapon
```

Weapon recommendations (signature + alternatives) with reasoning and comparisons.

**Section 15 — Best Teams:**

```
## <Name>: Best Teams
```

Team compositions with role explanations for each slot and rotation notes.

**Section 16 — DPS Benchmarks (optional but recommended):**

```
## <Name>: DPS Benchmarks
```

Damage benchmarks, rotation DPS calculations, and comparisons to similar characters. Include investment levels where applicable.

**Section 17 — Sources:**

```
## <Name>: Sources
- <Source Name> — <URL>
```

---

## Character File: `<name>_story.md`

This file covers narrative content, backstory, personality analysis, and lore items. Sections marked optional should be included when data is available.

### Required Sections (in order)

**H1 Title:**

```
# <Name> Story Documentation
<!-- Sources: url1, url2 -->
```

**Section 1 — Official Introduction:**

```
## <Name> Official Introduction
```

Official description from the website/banner introduction. Use italics for direct quotes.

**Section 2 — Personality:**

```
## <Name> Personality
```

Analytical personality description — deeper than the character.md profile, focused on narrative characterization.

**Section 3 — Forte Examination Report:**

```
## <Name> Forte Examination Report
```

Summarized findings from the in-game Forte Examination Report, including Resonance metrics and anomalies.

**Section 4 — Character Stories:**
Each sub-story gets its **own** `## ` heading — do NOT nest under a single parent heading:

```
## <Name> Character Story I: "<Title>"
## <Name> Character Story II: "<Title>"
## <Name> Character Story III: "<Title>"
```

Include in-game text (italicized) followed by analysis/context.

**Section 5 — Cherished Items:**

```
## <Name>: Cherished Items
```

Item name, description, and significance to the character.

**Section 6 — Favorite/Disliked Food:**

```
## <Name>: Favorite/Disliked Food
```

Food preferences with in-game reasoning.

**Section 7 — Ideals:**

```
## <Name>: Ideals
```

Categorized ideals (Passion, Resonance, Gratitude, etc.) with descriptions.

**Section 8 — Narrative Chronicle:**

```
## <Name>: Narrative Chronicle
```

Chronological timeline of key events in the character's life.

**Section 9 — Sources:**

```
## <Name>: Sources
- <Source Name> — <URL>
```

---

## Lore File Directory Structure

```
knowledge/lore/
├── history.md                          (global timeline)
├── world.md                            (world overview)
└── regions/
    └── <region_name>/                  (e.g., rinascita/)
        ├── <region>_story.md           (history, politics, culture)
        ├── <region>_places.md          (geography, locations)
        ├── <city_name>/               (e.g., ragunna/, septimont/)
        │   ├── <city>_story.md
        │   └── <city>_territories.md
        └── quests/
            ├── main_quests/
            │   ├── <region>_mq_<chapter_id>.md           (chapter overview)
            │   ├── <region>_mq_<id>_prologue.md
            │   ├── <region>_mq_<id>_act<NN>.md           (per-act files)
            │   ├── <region>_mq_<id>_themes.md            (thematic analysis)
            │   ├── <region>_mq_seg<NN>.md                (segments)
            │   └── <region>_mq_seg<NN>_ic<NN>.md         (interludes)
            ├── side_quests/
            ├── companion_quests/
            └── exploration_quests/
```

---

## Lore: Regional Story and Places Files

These files document the history, culture, geography, and locations of a region or city.

**H1 Title:**

```
# <Region> - <Topic>
```

For example: `# Rinascita - History and Story` or `# Rinascita - Places and Locations`

**First section must be:**

```
## Overview
```

A 1–3 paragraph summary of the region/topic.

**Subsequent sections:**

- Each `## ` heading covers one distinct topic (a historical era, a location, a cultural tradition, etc.)
- Use `---` horizontal rules between major thematic groups (e.g., between "Founding Era" sections and "Modern Era" sections)
- Include region/city name or use clearly contextual headings (e.g., `## The Founding Era`, `## Ragunnan Maritime`, `## The Stormy Sea`)

---

## Lore: Quest Files — Act Format

Each main quest act is stored in its own file. The filename convention is:

```
<region>_mq_<chapter>_act<NN>.md
```

**Standard `## ` sections for act files (include only those relevant to the act):**

| Section                                | Required?    | Description                                           |
| -------------------------------------- | ------------ | ----------------------------------------------------- |
| `## Act <N>: <Title>`                  | **Required** | Act title                                             |
| `## Act <N>: Synopsis`                 | **Required** | Plot summary                                          |
| `## Act <N>: Key Revelations`          | **Required** | Major plot reveals (bulleted, bolded labels)          |
| `## Act <N>: Key Locations`            | **Required** | Locations visited with brief descriptions             |
| `## Act <N>: Important NPCs`           | **Required** | NPC list with roles and significance                  |
| `## Act <N>: Combat Encounters`        | Optional     | Boss fights, enemy types, mechanics                   |
| `## Act <N>: Cultural Elements`        | Optional     | Traditions, customs, or cultural details revealed     |
| `## Act <N>: Political Landscape`      | Optional     | Power structures, factions, governance details        |
| `## Act <N>: Political Developments`   | Optional     | Political changes or shifts that occur during the act |
| `## Act <N>: Thematic Elements`        | Optional     | Recurring themes and motifs                           |
| `## Act <N>: Character Development`    | Optional     | Character growth and arc progression                  |
| `## Act <N>: Key Items`                | Optional     | Important items introduced or used                    |
| `## Act <N>: Relationship Development` | Optional     | Changes in character relationships                    |
| `## Act <N>: Anomaly Details`          | Optional     | Waveworn/TD anomaly specifics                         |
| `## Act <N>: Unresolved Questions`     | Optional     | Open plot threads                                     |
| `## Act <N>: Gameplay Significance`    | Optional     | Rewards, achievements, unlocks                        |

---

## Lore: Quest Files — Segment and Interlude Format

Shorter quest files (segments, interludes, prologues) use fewer sections. At minimum:

```
## <Segment/Prologue Name>: Synopsis
## <Segment/Prologue Name>: Key Revelations
## <Segment/Prologue Name>: Key Locations
## <Segment/Prologue Name>: Important NPCs     (if applicable)
```

Use the same self-identifying heading prefix pattern (e.g., `## Prologue: Synopsis`).

---

## Quick Reference: Heading Naming Patterns

| File Type          | Heading Pattern                                   | Example                                                            |
| ------------------ | ------------------------------------------------- | ------------------------------------------------------------------ |
| `_character.md`    | `## <Name> Profile: <Topic>`                      | `## Carlotta Profile: Basic Information`                           |
| `_character.md`    | `## <Name>: <Topic>`                              | `## Carlotta: Relationships`                                       |
| `_character.md`    | `## <Name> — <Topic>`                             | `## Carlotta — Character/Appearance Design`                        |
| `_kit.md`          | `## <Name>: <Topic>`                              | `## Carlotta: Combat Archetype and Role`                           |
| `_kit.md`          | `## <Name>: Character Kit: <Skill Type> — <Name>` | `## Carlotta: Character Kit: Resonance Skill — Chromatic Splendor` |
| `_story.md`        | `## <Name> <Topic>`                               | `## Carlotta Official Introduction`                                |
| `_story.md`        | `## <Name> Character Story <N>: "<Title>"`        | `## Carlotta Character Story I: "The Night Rain"`                  |
| Lore regional      | `## <Topic>`                                      | `## The Founding Era`                                              |
| Lore quest act     | `## Act <N>: <Topic>`                             | `## Act V: Key Revelations`                                        |
| Lore quest segment | `## <Segment>: <Topic>`                           | `## Prologue: Synopsis`                                            |

---

## Anti-Patterns (What NOT to Do)

- ❌ `### ` sub-headings — the RAG system ignores them; promote to `## `
- ❌ `## Basic Information` without a character name — chunks lose context when retrieved alone
- ❌ Multiple `# ` titles in one file — only one H1 per file
- ❌ Sections longer than ~50 lines — split into multiple `## ` sections
- ❌ Deeply nested bullet lists (3+ levels) — flatten to 1–2 levels
- ❌ Repeating voice actor data that contradicts `voice_actors.txt` — always cross-reference
- ❌ Using `---` horizontal rules in character files — reserved for lore files only
- ❌ Empty `## ` sections with no content — either add content or remove the heading
