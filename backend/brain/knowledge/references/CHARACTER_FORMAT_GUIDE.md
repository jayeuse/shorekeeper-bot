# Character Knowledge File Format Guide

This guide defines the detailed structure for files in `knowledge/characters/`.

Use this guide together with `FORMAT_GUIDE.md`:

- `FORMAT_GUIDE.md` contains shared RAG, frontmatter, and formatting rules for the whole knowledge folder.
- `CHARACTER_FORMAT_GUIDE.md` contains the character-specific file templates and conventions.

---

## Voice Actor Reference

The file `knowledge/characters/voice_actors.txt` is the single source of truth for all voice actor data. It is a pipe-delimited table covering EN, CN, JP, and KR voice actors for every character.

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

This file covers identity, appearance, personality, and relationships. All sections below are required unless marked optional.

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

Personality analysis organized with bolded trait headers (e.g., `**Composure Under Pressure**`), each followed by explanatory text.

**Section 5 — Relationships:**

```
## <Name>: Relationships
```

Grouped by person. Each relationship starts with a bold name header (e.g., `**Rover (Protagonist)**`) followed by the relationship description.

**Section 6 — Sources:**

```
## <Name>: Sources
- <Source Name> — <URL>
- <Source Name> — <URL>
```

---

## Character File: `<name>_kit.md`

This file covers combat mechanics, abilities, stats, materials, and build recommendations. All sections below are required unless marked optional.

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
Each sub-story gets its own `## ` heading — do NOT nest under a single parent heading:

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

## Quick Reference: Character Heading Naming Patterns

| File Type       | Heading Pattern                                   | Example                                                            |
| --------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| `_character.md` | `## <Name> Profile: <Topic>`                      | `## Carlotta Profile: Basic Information`                           |
| `_character.md` | `## <Name>: <Topic>`                              | `## Carlotta: Relationships`                                       |
| `_character.md` | `## <Name> — <Topic>`                             | `## Carlotta — Character/Appearance Design`                        |
| `_kit.md`       | `## <Name>: <Topic>`                              | `## Carlotta: Combat Archetype and Role`                           |
| `_kit.md`       | `## <Name>: Character Kit: <Skill Type> — <Name>` | `## Carlotta: Character Kit: Resonance Skill — Chromatic Splendor` |
| `_story.md`     | `## <Name> <Topic>`                               | `## Carlotta Official Introduction`                                |
| `_story.md`     | `## <Name> Character Story <N>: "<Title>"`        | `## Carlotta Character Story I: "The Night Rain"`                  |