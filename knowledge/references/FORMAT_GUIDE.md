# Knowledge File Format Guide

This guide is the general formatting reference for the entire `knowledge/` folder. Following these rules ensures the RAG system can chunk, embed, and retrieve knowledge accurately and consistently.

> **Scope:** This guide covers shared rules used across `characters/` and `lore/`. For file-type-specific templates, use the specialized guides in `knowledge/references/`.

---

## Specialized Guides

Use the base guide for universal rules, then use the specialized guide that matches the file family you are editing.

| Guide | Purpose |
|-------|---------|
| `FORMAT_GUIDE.md` | Shared RAG, frontmatter, naming, and source-policy rules for the whole knowledge folder |
| `CHARACTER_FORMAT_GUIDE.md` | Detailed structure for `*_character.md`, `*_kit.md`, and `*_story.md` files |
| `REGION_FORMAT_GUIDE.md` | Detailed structure for regional lore, territory, and quest files |

---

## Knowledge Folder Scope

```
knowledge/
├── characters/       (character profiles, kits, and stories)
├── lore/             (regions, places, quests, world lore)
├── personalization/  (persona-specific writing, excluded from this guide)
└── references/       (reference docs and formatting guides, excluded from RAG)
```

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

## Writing Guide by File Family

Use the specialized guides below for the detailed file templates:

- Characters: `knowledge/references/CHARACTER_FORMAT_GUIDE.md`
- Regions and lore: `knowledge/references/REGION_FORMAT_GUIDE.md`

---

## Quick Reference: Heading Naming Patterns

| File Type          | Heading Pattern                                   | Example                                                            |
| ------------------ | ------------------------------------------------- | ------------------------------------------------------------------ |
| Character profile  | `## <Name> Profile: <Topic>`                      | `## Carlotta Profile: Basic Information`                           |
| Character generic  | `## <Name>: <Topic>`                              | `## Carlotta: Relationships`                                       |
| Character design   | `## <Name> — <Topic>`                             | `## Carlotta — Character/Appearance Design`                        |
| Story section      | `## <Name> <Topic>`                               | `## Carlotta Official Introduction`                                |
| Story sub-entry    | `## <Name> Character Story <N>: "<Title>"`        | `## Carlotta Character Story I: "The Night Rain"`                  |
| Regional lore      | `## <Topic>`                                      | `## The Founding Era`                                              |
| Territory lore     | `## <Place>: <Sub-Area>`                          | `## Ragunna City: City Square`                                     |
| Quest act          | `## Act <N>: <Topic>`                             | `## Act V: Key Revelations`                                        |
| Quest segment      | `## <Segment>: <Topic>`                           | `## Prologue: Synopsis`                                            |

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

---

## Cited Sources Registry

This section lists all external websites and sources currently cited across the knowledge base. When adding new files, prefer sourcing from these established sites for consistency. New sources may be added here when first used.

### Official & Primary Game Sources

| Site | URL | Used For |
|------|-----|----------|
| Wuthering Waves Fandom Wiki | https://wutheringwaves.fandom.com | Primary source for all character data, lore, backstories, quest details, voicelines |
| Official Wuthering Waves X/Twitter | https://x.com/Wuthering_Waves | Official character announcements and artwork |

### Build Guides & Meta Analysis

| Site | URL | Used For |
|------|-----|----------|
| Prydwen Institute | https://www.prydwen.gg/wuthering-waves | Primary DPS benchmarks, tier list, full build guides |
| Game8 | https://game8.co/games/Wuthering-Waves | Builds, teams, lore pages, quest walkthroughs |
| Wuthering.gg | https://wuthering.gg | Character pages, kit details, build info |
| Wutheringlab | https://wutheringlab.com | Character build guides |
| LootBar | https://lootbar.gg/blog/en | Build guides, kit and resonance chain analyses |
| LDShop | https://www.ldshop.gg/blog | Build guides, kit breakdowns |
| OSLink | https://www.oslink.io/blog | Build guides and kit leak coverage |
| WutheringWaves-Builds | https://wutheringwaves-builds.com | Build guides, story/voice line aggregation |
| WuWaLabo | https://wuwalabo.com | Character guides and build recommendations |
| Pocket Tactics | https://www.pockettactics.com/wuthering-waves | Build guides, lore overviews, release date info |
| Genshin-Builds (WuWa section) | https://genshin-builds.com/en/wuthering-waves | Story pages, voice lines, team builds |
| Tacter | https://www.tacter.com/wuthering-waves | Build guides |
| Theria Games | https://theriagames.com | Ultimate build guides |
| GladiatorBoost | https://gladiatorboost.com | Build guides |
| Buffget | https://buffget.com | Team DPS benchmark articles |
| WuWaCompanion | https://wuwacompanion.com | Character stat databases |
| MisterMenPlays | https://www.mistermenplays.com/wutheringwaves | Build calculators and guides |
| WutheringTide | https://www.wutheringtide.com | Character guides |
| XboxPlay.games | https://xboxplay.games | Resonance chain guides |

### Character Lore & Community Wikis

| Site | URL | Used For |
|------|-----|----------|
| Wuthering.wiki | https://wuthering.wiki | Character data pages (stat numbers, story text) |
| TV Tropes | https://tvtropes.org/pmwiki/pmwiki.php/Characters | Character analysis pages (Black Shores, Rinascita, Septimont, Fractsidus) |
| VS Battles Wiki | https://vsbattles.fandom.com | Character power level analysis |
| Villains Wiki | https://villains.fandom.com | Antagonist character pages |
| Shipping Wiki | https://shipping.fandom.com | Relationship/ship pages |
| Steam Community | https://steamcommunity.com/app/3513350 | Lore discussions and player guides |
| Wikipedia | https://en.wikipedia.org/wiki/Wuthering_Waves | General game overview |

### Gaming News & Media

| Site | URL | Used For |
|------|-----|----------|
| Sportskeeda | https://www.sportskeeda.com/esports | Resonance chain guides, kit analyses, voiceline articles |
| GameRant | https://gamerant.com | Build guides, character explainers |
| GameLeap | https://www.gameleap.com | Build guides, character previews |
| Pocket Gamer | https://www.pocketgamer.com | Character previews and lore |
| Destructoid | https://www.destructoid.com | Build guides, weapon stat articles |
| Dot Esports | https://dotesports.com/wuthering-waves | Character lore explainers |
| The Gamer | https://www.thegamer.com | Build guides |
| Game Revolution | https://www.gamerevolution.com | Build guides |
| DBLTAP | https://www.dbltap.com | Build guides |
| India Today Gaming | https://www.indiatodaygaming.com | Character profile and lore articles |
| Esports.gg | https://esports.gg/guides/wuthering-waves | Ascension material guides |
| ComicBook.com | https://comicbook.com/gaming | Lore analysis articles |
| InGameNews | https://www.ingamenews.com | Character previews |
| Joytify | https://www.joytify.com | Kit and build articles |
| FdayTalk | https://www.fdaytalk.com | Build guides |
| GuildJen | https://guildjen.com | Character guides |
| The Illuminate | https://www.theilluminate.com | Resonance chain guides |
| The Flagship Eclipse | https://www.theflagshipeclipse.com | Lore analysis articles |
| WutheringWaves.gg | https://wutheringwaves.gg | Character guides |

### Voice Actor Reference

| Site | URL | Used For |
|------|-----|----------|
| Behind the Voice Actors | https://www.behindthevoiceactors.com/video-games/Wuthering-Waves | Voice actor verification |
