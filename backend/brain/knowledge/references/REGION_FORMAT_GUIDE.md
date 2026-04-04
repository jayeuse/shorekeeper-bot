# Region Knowledge File Format Guide

This guide defines the detailed structure for files in `knowledge/lore/`.

Use this guide together with `FORMAT_GUIDE.md`:

- `FORMAT_GUIDE.md` contains shared RAG, frontmatter, and formatting rules for the whole knowledge folder.
- `REGION_FORMAT_GUIDE.md` contains lore, region, city, and quest-specific file templates.

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
        ├── <city_name>/                (e.g., ragunna/, septimont/)
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

## Lore File: `<region>_story.md`

This is the region-level history and identity file. It should read like the lore equivalent of a character story file: broad overview first, then organized deep-dive sections.

### Required Structure

**H1 Title:**

```
# <Region> - History and Story
<!-- Sources: url1, url2 -->
```

**Section 1 - Overview:**

```
## Overview
```

Write a 1-3 paragraph summary covering what the region is, why it matters, and its role in the wider world.

**Section 2 onward - Historical / cultural sections:**

Each later `## ` heading should cover one distinct lore block such as:

- a historical era (`## The Founding Era`, `## The Modern Era`)
- a political phase (`## The Rise of City-States`)
- a cultural institution (`## The Carnevale Tradition`)
- a defining theme (`## Recurring Themes`)
- a major figure or force (`## Key Historical Figures`)

**Organization rules:**

- Keep every `## ` section self-contained for RAG chunking.
- Use `---` between major thematic groups when the file shifts from history to culture, politics, themes, or source notes.
- Prefer broad-to-specific ordering: overview -> origins -> major eras -> modern state -> themes/legacy -> sources.
- End with a sources section when the file is mature enough for citation listing.

**Recommended closing section:**

```
## <Region>: Sources
- <Source Name> - <URL>
```

---

## Lore File: `<region>_places.md`

This is the region-level geography and location index. It should explain how the region is laid out before drilling into notable locations.

### Required Structure

**H1 Title:**

```
# <Region> - Places and Locations
<!-- Sources: url1, url2 -->
```

**Section 1 - Overview:**

```
## Overview
```

Summarize the region's overall layout, environmental identity, and what kinds of places exist there.

**Section 2 onward - Geography / location groups:**

Follow the repo's current pattern of grouped geographic sections, for example:

- `## Geographic Organization`
- `## <City/Territory Name>`
- `## Special Locations`
- `## Environmental Features`
- `## Architectural Styles`
- `## Economic Geography`
- `## Strategic Importance`
- `## Mysteries and Unknowns`

**Organization rules:**

- Start with macro geography before individual locations.
- Group related places together instead of making one massive unordered location list.
- Use `## <City/Territory Name>` when introducing a major subregion that also has its own folder.
- Keep place descriptions focused on lore, purpose, and distinguishing traits rather than gameplay routing.

---

## Lore File: `<city>_story.md`

This is the city-state or subregion identity file. Use it when a major location needs its own history, governing structure, cultural identity, or narrative role separate from the parent region file.

### Required Structure

**H1 Title:**

```
# <City> - History and Story
<!-- Sources: url1, url2 -->
```

**Section 1 - Overview:**

```
## Overview
```

**Section 2 onward - City-specific lore blocks:**

Typical topics include:

- origin and founding
- political structure
- ruling factions or families
- cultural identity and local customs
- major crises or historical turning points
- relationship to the parent region

**Organization rules:**

- Do not duplicate the entire parent region file. Focus on what is unique to the city/subregion.
- If source coverage is still sparse, frontmatter-only placeholder files are acceptable temporarily, but the target structure is still overview plus city-specific `## ` sections.

---

## Lore File: `<city>_territories.md`

This file is the detailed location catalog for a city or territory. It is more granular than `<region>_places.md` and usually reads like a location index.

### Required Structure

**H1 Title:**

```
# <City> Territory
<!-- Sources: url1, url2 -->
```

**Section pattern:**

Use one `## ` heading per notable place. Follow the current naming style used in territory files:

- `## <Primary Location>`
- `## <Primary Location>: <Sub-Area>`
- `## <Standalone Landmark>`

Examples:

- `## Ragunna City`
- `## Ragunna City: City Square`
- `## Averardo Vault`
- `## Penitent's End`

**Organization rules:**

- Lead with the main settlement or anchor location, then branch into districts, landmarks, vaults, ruins, or special sites.
- Each section should explain what the place is, who uses it, and why it matters.
- Keep headings precise so retrieval can distinguish neighboring districts and landmarks.

---

## Lore: Quest Files - Chapter Overview Format

Each chapter can have a single overview file that maps the full arc before act-by-act breakdowns.

**Filename convention:**

```
<region>_mq_<chapter_id>.md
```

**H1 Title:**

```
# <Region> Main Quests - Comprehensive Guide
```

**Required opening section:**

```
## Chapter <N>: <Chapter Title> (Structure Overview)
```

This section should summarize:

- where the chapter takes place
- how many acts/segues it contains
- the central conflict
- the chapter's high-level progression

**Optional follow-up sections:**

- `## Chapter <N>: Major Factions`
- `## Chapter <N>: Narrative Throughline`
- `## Chapter <N>: Key Characters`
- `## Chapter <N>: Regional Stakes`

Use this file for top-down structure only. Detailed plot beats belong in act, segment, or interlude files.

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

## Quick Reference: Lore Heading Naming Patterns

| File Type          | Heading Pattern         | Example                         |
| ------------------ | ----------------------- | ------------------------------- |
| Regional story     | `## <Topic>`            | `## The Founding Era`           |
| Regional places    | `## <Topic>`            | `## Geographic Organization`    |
| Territory file     | `## <Place>`            | `## Ragunna City`               |
| Territory sub-area | `## <Place>: <Sub-Area>` | `## Ragunna City: City Square`  |
| Quest act          | `## Act <N>: <Topic>`   | `## Act V: Key Revelations`     |
| Quest segment      | `## <Segment>: <Topic>` | `## Prologue: Synopsis`         |
| Chapter overview   | `## Chapter <N>: <Topic>` | `## Chapter II: Structure Overview` |