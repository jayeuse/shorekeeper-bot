---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/huanglong/yangyang/yangyang_kit.md
character: Yangyang
group: Huanglong / Jinzhou
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - aero
  - sword
  - sub-dps
  - energy-battery
  - melody-stacks
  - feather-release
  - grouping
  - resonance-energy-restoration
  - free-character
---

# Yangyang Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/yangyang/, https://wutheringlab.com/character/yangyang-build/, https://game8.co/games/Wuthering-Waves/archives/454215, https://guildjen.com/yangyang-character-guide/, https://wutheringwaves.gg/yangyang-guide/ -->

## Yangyang: Combat Archetype and Role

- **Element:** Aero
- **Weapon Type:** Sword
- **Role:** Sub-DPS / Energy Battery / Crowd Control Support
- **Archetype:** Melody-stack accumulator; Feather Release off-field burst; enemy grouping; Resonance Energy restoration via Outro
- **Availability:** Free — obtained by all players via the main story Prologue; also available from all Convene banners

Yangyang is a utility-focused Sub-DPS and the only character in Version 1.x whose Outro Skill directly restores Resonance Energy to the incoming character (alongside Zhezhi). This niche — **20 total Resonance Energy over 5 seconds to whoever she swaps into** — makes her uniquely valuable for Main DPS characters who are Liberation-dependent and whose energy management is otherwise difficult or slow (most relevantly Jiyan, Calcharo in early game, and Rover Spectro). Her Resonance Liberation (Wind Spirals) and Resonance Skill (Zephyr Domain) both generate AoE Aero vortices that pull enemies toward a center point — the best grouping in the 4-star tier at launch. Her personal damage is modest relative to limited 5-star characters even at full sequences, but her crowd control and energy battery utility carry real team value.

Prydwen describes her as the only **quickswap-friendly hybrid buffing archetype** in the game: when running Moonlit Clouds on Yangyang, her Outro triggers the Moonlit Clouds 4-piece buff for the incoming character without the buff expiring on character swap — unlike similar hybrid buffers such as Sanhua, Mortefi, or Zhezhi. This quirk of her Outro's energy-grant mechanic (which fires on swap, not on-field activity) is her unique competitive advantage in the support role even as a 4-star character.

## Yangyang: Key Resource — Melody Stacks

Yangyang's entire Forte Circuit is built around accumulating **Melody** stacks (maximum 3) and spending them on her aerial Forte attack. Every part of her rotation is oriented toward reaching 3 stacks quickly and safely.

**Melody Generation (4 sources)**
- **Basic Attack Stage 4 (final hit of the 4-hit chain) — on hit:** +1 Melody; requires completing the full Basic Attack sequence, which is the least efficient method per unit of time
- **Heavy Attack: Zephyr Song — on hit:** +1 Melody; Zephyr Song is triggered by using Basic Attack immediately after a Heavy Attack or after a Dodge Counter; the Heavy Attack → Basic Attack chain is the **fastest repeatable Melody generator** because it has no cooldown and completes quickly; the standard optimal non-Skill Melody charging loop is: Heavy Attack → Basic (Zephyr Song) → Heavy Attack → Basic (Zephyr Song) → Heavy Attack → Basic (Zephyr Song) → now at 3 Melodies
- **Resonance Skill: Zephyr Domain — on hit:** +1 Melody per cast; also generates Concerto Energy and groups enemies; top priority to cast on cooldown for both Melody generation and grouping value; dodge-cancellable after cast for animation speed
- **Intro Skill: Cerulean Song — on cast:** +1 Melody automatically; does not require a hit; fires whenever Yangyang enters the field via swap with full Concerto Energy; the guaranteed on-entry stack is why entering via Intro Skill advances the Forte rotation immediately

**Maximum Stacks:** 3 Melodies

**Melody Consumption — Forte Circuit: Feather Release**
When Yangyang holds 3 Melodies, the following attack sequence becomes available:
1. **Heavy Attack: Stormy Strike** (at 3 Melodies) — Yangyang lunges upward in a rising heavy attack; this also lifts smaller enemies into the air with her; deals Aero DMG; positions Yangyang in mid-air; does not consume Melodies itself but is the gateway to Feather Release
2. **Mid-Air Attack: Feather Release** (Basic Attack input while airborne after Stormy Strike) — consumes all 3 Melodies; performs consecutive aerial strikes, then dives from mid-air; deals Aero DMG (aerial hit portion); the landing sheath attack deals Aero DMG classified as **Basic Attack DMG**; on full completion, restores **30 Stamina** (Inherent Skill 1)
- Alternatively, Feather Release can also be accessed via: Heavy Attack input while airborne after any jump or after Intro Skill, Dodge Counter → Basic Attack, or simply jumping and then Basic Attacking — provided 3 Melodies are held
- The most reliable and rotation-efficient access method per Prydwen is via **jump → Basic Attack**: Yangyang jumps (consumes no special resources), then immediately inputs Basic Attack in mid-air, triggering Feather Release without requiring the Stormy Strike setup

**Concerto Energy from Feather Release**
Feather Release is Yangyang's primary Concerto Energy generator. Prydwen notes that using the jump → aerial Basic Attack → Feather Release path generates massive Concerto Energy per use and is the primary reason Yangyang can reach her Outro Skill quickly within a rotation. The animation can be **swap-canceled** after the aerial hit lands (before the landing sheath animation completes) — field time is saved and the sheath Basic Attack DMG is lost, but this is frequently worth the trade in tight rotations.

**Parry Window**
Feather Release provides a generous **omni-directional parry window** during its animation. This is a meaningful combat benefit: if an enemy attacks during Feather Release's execution, the attack is parried, providing both damage protection and positional safety. Liberation and Resonance Skill do not share this property.

## Yangyang: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | ~765 | ~27 | ~72 |
| Lv. 20 | ~1,985 | ~70 | ~187 |
| Lv. 40 | ~3,790 | ~134 | ~357 |
| Lv. 60 | ~6,110 | ~216 | ~576 |
| Lv. 80 | ~8,410 | ~298 | ~792 |
| Lv. 90 | ~9,570 | ~338 | ~901 |

*Approximate figures before Forte Attribute Bonuses and equipment. Verify exact values with the Wuthering Waves Fandom Wiki. As a 4-star character, Yangyang's base stats are meaningfully lower than 5-star characters; her combat value comes primarily from utility (grouping, energy restoration) rather than raw damage output.*

## Yangyang: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | Crude Ring ×4, Wintry Bell ×4, Shell Credits ×5,000 |
| 2 | 40→50 | Basic Ring ×4, Wintry Bell ×8, Shell Credits ×10,000 |
| 3 | 50→60 | Improved Ring ×8, Wintry Bell ×12, Roaring Rock Fist ×4, Shell Credits ×15,000 |
| 4 | 60→70 | Improved Ring ×8, Wintry Bell ×16, Roaring Rock Fist ×8, Shell Credits ×20,000 |
| 5 | 70→80 | Tailored Ring ×12, Wintry Bell ×20, Roaring Rock Fist ×12, Shell Credits ×40,000 |
| 6 | 80→90 | Tailored Ring ×12, Wintry Bell ×24, Roaring Rock Fist ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Crude/Basic/Improved/Tailored Rings:** Dropped by Exile enemies throughout the map; also available from the Forgery Challenge and purchasable from Jinzhou's weapon shop or exchanged for Oscillated Coral
- **Wintry Bells:** Local specialty flowers that grow in the **Gorges of Spirits** region; use the Interactive Map to locate efficiently; not available for purchase, so gathering must be done in the overworld
- **Roaring Rock Fist:** Boss material dropped by the **Feilian Beringal** boss (large Aero bird Tacet Discord); also used by Jiyan and other Aero characters

## Yangyang: Skill Upgrade Materials

| Skill Level | Key Materials |
|-------------|---------------|
| 1→2 | Inert Metallic Drip ×4, Lv.1 Skill Book ×4, Shell Credits ×1,000 |
| 2→3 | Inert Metallic Drip ×4, Lv.2 Skill Book ×4, Shell Credits ×3,000 |
| 3→4 | Inert Metallic Drip ×8, Lv.3 Skill Book ×8, Shell Credits ×8,000 |
| 4→5 | Reactive Metallic Drip ×12, Weekly Boss Material ×2, Lv.4 Skill Book ×4, Shell Credits ×20,000 |
| 5→6 | Reactive Metallic Drip ×16, Weekly Boss Material ×3, Lv.4 Skill Book ×4, Shell Credits ×40,000 |
| 6→7 | Polarized Metallic Drip ×20, Weekly Boss Material ×5, Lv.4 Skill Book ×8, Shell Credits ×80,000 |
| 7→8 | Polarized Metallic Drip ×24, Weekly Boss Material ×8, Lv.4 Skill Book ×8, Shell Credits ×120,000 |
| 8→9 | Heterized Metallic Drip ×28, Weekly Boss Material ×12, Lv.4 Skill Book ×16, Shell Credits ×160,000 |
| 9→10 | Heterized Metallic Drip ×40, Weekly Boss Material ×16, Lv.4 Skill Book ×16, Shell Credits ×200,000 |

**Total Forte Shell Credits (all skills):** ~2,030,000
- **Metallic Drips (Inert/Reactive/Polarized/Heterized):** Dropped by Exile enemies; available from the Forgery Challenge, Jinzhou weapon shop, or Exchange Store (Oscillated Coral); the same enemy type as the Ring ascension material
- **Weekly Boss Material:** Dropped by Scar at Chaotic Juncture (Ember in Central Plains) — the "Unending Destruction" weekly challenge; verify with the Fandom Wiki if this has changed in later versions
- **Skill Books:** From the appropriate Forgery Challenge

**Skill Upgrade Priority:** Resonance Liberation (Wind Spirals) → Resonance Skill (Zephyr Domain) → Forte Circuit (Feather Release) → Basic Attack → Intro Skill. Liberation is the primary damage source and deserves first investment; Skill and Forte Circuit provide both damage and utility; Basic Attack and Intro Skill are the lowest priority as they are primarily Melody generators rather than primary damage tools.

## Yangyang: Character Kit: Basic Attack — Gale

**Standard Ground Chain (4 stages)**
- Up to 4 consecutive Aero DMG attacks
- **Stage 4 (final hit) — on hit:** +1 Melody
- In practice, the full 4-hit chain is slow relative to the Heavy Attack → Zephyr Song loop and is typically used only when cooldowns are unavailable or when additional Concerto Energy is needed at the end of a rotation

**Heavy Attack**
- Consumes Stamina; Yangyang lunges forward, dealing Aero DMG
- Does not grant Melody directly — the follow-up Basic Attack (Zephyr Song) is what generates the stack

**Heavy Attack: Zephyr Song**
- Triggered by inputting Basic Attack immediately after a Heavy Attack or after a Dodge Counter
- Deals Aero DMG
- Grants **+1 Melody on hit**
- This is the primary Melody generation loop: Heavy Attack → Basic Attack (Zephyr Song) → Heavy Attack → Basic Attack (Zephyr Song) → Heavy Attack → Basic Attack (Zephyr Song), reaching 3 Melodies in ~3 cycles; no cooldown; efficient in field time

**Mid-Air Attack**
- Standard plunging attack from mid-air, dealing Aero DMG (Stamina cost)
- At 3 Melodies: replaced by **Mid-Air Attack: Feather Release** (see Forte Circuit section)

**Dodge Counter**
- Basic Attack after successful Dodge; Aero DMG; the subsequent Basic Attack counts as Zephyr Song if it follows the Dodge Counter, generating +1 Melody

**S2 Interaction — Heavy Attack Energy Recovery**
At S2, Heavy Attack recovers an additional **+10 Resonance Energy** for Yangyang when it hits a target, triggered once per 20 seconds. This provides meaningful Liberation cycling assistance when it fires, particularly in short rotations where Liberation uptime is the bottleneck.

## Yangyang: Character Kit: Resonance Skill — Zephyr Domain

- Yangyang wields her sword to create a **whirling vortex of winds** that pulls nearby enemies toward the center of the field, dealing Aero DMG in an area
- Grants **+1 Melody on hit**
- Generates Concerto Energy on cast and on hit
- **Grouping utility:** The vortex effect draws enemies inward; smaller enemies are pulled more strongly; this is Yangyang's primary crowd control contribution and makes her particularly valuable alongside AoE Main DPS characters who benefit from enemies being clustered (Jiyan's Qingloong sweeps, Encore's Cosmos Rampage)
- The pull range is relatively small in baseline form; S3 expands it by **+33%** and is a meaningful upgrade for AoE compositions
- Can be **hold-charged** (hold the Resonance Skill button during the animation) for enhanced or extended effect; the standard combat shortcut is to press-and-hold during the animation so it fires immediately upon completion
- Contributes Resonance Energy toward Liberation and Concerto Energy toward the Outro Skill

**Cooldown:** Approximately 12 seconds (verify with Fandom Wiki for exact value by skill level)

**Skill Upgrade Priority:** Second after Liberation; the DMG multiplier, Melody generation, and grouping range all improve with level.

## Yangyang: Character Kit: Resonance Liberation — Wind Spirals

- Yangyang creates a **large Aero vortex** significantly larger than Zephyr Domain, pulling all nearby enemies more aggressively toward the center, and dealing Aero DMG in a wide area
- **This is Yangyang's primary damage skill** — her highest-multiplier ability and the skill most worth leveling first
- The Liberation's pull is stronger and covers more area than Zephyr Domain; it is the premier enemy grouping tool in her kit and the optimal setup for any AoE follow-up from a teammate
- **S3 interaction:** Zephyr Domain's pulling range increases by +33% and deals +40% DMG
- **S5 interaction:** Wind Spirals DMG increased by +85% — the largest single-skill multiplier increase in her chain; the sequence that meaningfully elevates her damage contribution

**Timing Optimization:** Prydwen and Game8 both recommend casting Liberation **first** when entering Yangyang's field window, before building Melody stacks, so that all subsequent Zephyr Song and Feather Release attacks hit enemies that have been grouped. The grouping effect from Liberation is the force multiplier for everything that follows.

**Resonance Energy Cost:** Standard 4-star Liberation cost; Yangyang aims for ~140% Energy Regen to cast it reliably each rotation.

## Yangyang: Inherent Passives

**Inherent Skill 1 — Lazuline Mercy**
- After casting **Mid-Air Attack: Feather Release** (the Forte aerial attack at 3 Melodies), Yangyang restores **30 Stamina**
- Stamina is shared across all characters; this passive provides meaningful team-wide Stamina recovery after every Feather Release, partially offsetting the Stamina cost of the heavy attacks and aerial plunges used to build Melody stacks
- The Stamina restoration fires on every Feather Release, making it a consistent rotation benefit rather than a conditional one

**Inherent Skill 2 — Zephyr's Embrace**
- Casting **Intro Skill Cerulean Song** increases Yangyang's **Aero DMG Bonus by +8%** for **8 seconds**
- This baseline +8% Aero bonus fires every time she enters the field via Intro; S1 upgrades this to +15% total (the S1 description adds +15% — it either replaces IS2's +8% or stacks to +23%; verify the exact interaction with the Fandom Wiki for precise values)
- Incentivizes entering via Intro Skill at the start of each rotation where field time allows

## Yangyang: Intro/Outro Skills

**Intro Skill — Cerulean Song**
- Triggered when Yangyang enters the field via swap with full Concerto Energy
- Deals Aero DMG on cast
- Grants **+1 Melody** automatically (does not require a hit to land)
- Triggers Inherent Skill 2 (Zephyr's Embrace): +8% Aero DMG Bonus for 8 seconds (S1: +15%)
- This is the fastest possible way to start building Melodies — on the frame she arrives, she already has 1 stack
- In practice: Intro Skill (1 Melody) → Resonance Skill (2 Melodies) → Heavy Attack → Zephyr Song (3 Melodies) → Liberation → Feather Release is the tightest rotation entry

**Outro Skill — Zephyr's Gift**
- Triggered when Yangyang swaps off-field with full Concerto Energy
- The incoming Resonator receives **+4 Resonance Energy per second for 5 seconds** = **+20 total Resonance Energy** delivered over 5 seconds
- This is a sustained energy-over-time delivery, not an instant grant; the incoming character must remain on the field for the full 5 seconds to receive all 20 Energy
- **Unique mechanic:** This is the only Outro in Version 1.x that directly grants Resonance Energy to a teammate (Zhezhi also has energy restoration via Outro in Version 2.x). Most Outros provide DMG buffs, ATK buffs, or element-specific amplifications; Yangyang's provides the resource that enables Liberation casting
- **Moonlit Clouds synergy:** Because the Outro Skill counts as an Outro for Echo set triggering purposes, running Moonlit Clouds 4-piece on Yangyang causes the Outro to additionally grant the incoming character **+22.5% ATK for 15 seconds**; this transforms Yangyang's already-distinctive Outro into a dual-utility event: energy restoration + ATK amplification for the Main DPS simultaneously
- **Quickswap compatibility:** Prydwen notes that Yangyang is the only Hybrid buffing archetype character whose buffs do not expire on character swap, because her Outro-triggered Moonlit Clouds ATK buff is conferred to the incoming character directly and persists on them regardless of further swaps

## Yangyang: Resonance Chains (Sequences)

Yangyang can receive 4 free Resonance Chain nodes through story/event milestones in Version 1.x; additional nodes require pulling duplicate copies from convene banners where she appears as a featured 4-star.

**S1 — Whispering Gale**
- Intro Skill Cerulean Song additionally increases Yangyang's **Aero DMG Bonus by +15% for 8 seconds** (stacks with or replaces Inherent Skill 2's +8% — verify exact interaction with Fandom Wiki)
- *Impact:* A meaningful personal DPS improvement on every rotation entry via Intro Skill; the Aero DMG bonus applies to all of her Aero attacks during the 8-second window, including Liberation and Feather Release. Low investment for the value provided; commonly obtained alongside early free copies.

**S2 — Zephyr's Echo**
- Heavy Attack recovers an additional **+10 Resonance Energy** for Yangyang when it hits a target; can trigger **once per 20 seconds**
- *Impact:* Assists Liberation cycling, particularly in rotations where Yangyang uses multiple Heavy Attack → Zephyr Song cycles to build Melodies. Not transformative but meaningfully helpful for Liberation uptime in longer combat encounters.

**S3 — Storm's Embrace**
- Resonance Skill Zephyr Domain: DMG increased by **+40%**; Wind Field's pulling effect on surrounding targets is enhanced, and pulling range is expanded by **+33%**
- *Impact:* Both components are valuable — the DMG increase amplifies an already frequently-cast skill, and the expanded pulling range substantially improves crowd control coverage for AoE team compositions. The +33% range makes Zephyr Domain's grouping radius meaningfully larger and more forgiving; small enemies that previously escaped the vortex edge are now reliably pulled in. A recommended target for players using Yangyang heavily in AoE content.

**S4 — Featherfall**
- Mid-Air Attack Feather Release DMG increased by **+95%**
- *Impact:* Doubles the damage of her primary Forte attack. Feather Release is already her highest-multiplier Forte event; nearly doubling it makes her personal damage contribution substantially more competitive. This is the sequence where Yangyang transitions from utility character to meaningful damage contributor. Wutheringwaves.gg notes that starting from S3 and S4, her damage becomes genuinely noteworthy among 4-star characters.

**S5 — Cyclone's Roar**
- Resonance Liberation Wind Spirals DMG increased by **+85%**
- *Impact:* The largest multiplier increase in the chain; nearly doubles her Liberation damage, which is already her highest-multiplier individual skill. Combined with S4's Feather Release boost, S5 Yangyang has dramatically higher personal damage than base. Not commonly reached without dedicated banner investment in 4-star copies.

**S6 — Skylark's Aria**
- After casting Mid-Air Attack Feather Release, all team members' **ATK is increased by +20% for 20 seconds**
- *Impact:* Transforms Feather Release from a personal damage event into a team-wide offensive buff trigger. +20% ATK for 20 seconds applied to all team members after every Forte cycle is a significant offensive multiplier for the Main DPS. Combined with S4's DMG boost, S6 Yangyang becomes a character who deals meaningful personal damage AND buffs the team on the same cast. A very high ceiling but an expensive investment in a 4-star character; only recommended for players who play Yangyang as a primary unit.

**Sequence Pull Priority:** S0 and S1 (free/common pulls) are the baseline; S3 for AoE grouping investment; S4 for damage; S6 for full offensive support hybrid. Free 4 chains from story/events cover S1–S4 at launch; S5–S6 require deliberate banner pulls.

## Yangyang: Recommended Echo Sets

**Best-in-Slot (Energy Battery / Quickswap Support): Moonlit Clouds (5-piece) — Impermanence Heron**
- The definitive support-role echo set for Yangyang; purpose-matched to her Outro's energy-funneling mechanic
- **Moonlit Clouds 4-piece:** When the current Resonator casts an Outro Skill, the incoming Resonator gains **+22.5% ATK for 15 seconds** — this fires every time Yangyang uses her Outro, stacking on top of the +20 Resonance Energy already delivered; the incoming Main DPS thus receives both a Liberation energy top-up AND an ATK amplification simultaneously
- **Moonlit Clouds 2-piece:** Energy Regen +10%; helps Yangyang cycle her own Liberation faster
- **Main Echo: Impermanence Heron** — on cast: Yangyang transforms into the Heron, flies up, and dives to deal Aero DMG; on hit, grants **+10 Resonance Energy** to Yangyang and causes her next Outro to additionally give the incoming character **+12% DMG for 15 seconds**; this +12% DMG stacks on top of the Moonlit Clouds ATK buff and the energy grant for a three-layer Outro benefit
- Prydwen notes this combination makes Yangyang the **only quickswap-friendly hybrid buffer** in the game — all three Outro benefits are conferred to the incoming character directly and do not expire on further swapping

**Alternative (AoE Sub-DPS): Sierra Gale (5-piece) — Feilian Beringal / Nightmare Feilian Beringal**
- Used when Yangyang is intended as a damage-contributing Sub-DPS rather than a pure energy battery
- **Sierra Gale 5-piece:** Aero DMG Bonus; directly amplifies all of Yangyang's Aero skills including Feather Release and Wind Spirals
- **Main Echo: Nightmare Feilian Beringal** (if available) — deals Aero DMG and grants +12% Aero DMG + 12% Heavy ATK DMG Bonus for 15 seconds on hit; both bonuses directly amplify Feather Release (Aero, Heavy-type) and Zephyr Domain; use this echo skill **before** Feather Release for maximum benefit
- Wutheringwaves-builds.com recommends this set when running Yangyang in compositions where personal damage matters more than energy funneling

**Alternative (Shielding Utility): Bell-Borne Geochelone**
- Main echo for defensive compositions; generates a protective field that absorbs incoming damage and grants +12% ATK + 12% DEF to the active Resonator for 10 seconds; the shield transfers to the incoming character on swap
- Game8 recommends Bell-Borne specifically when running Yangyang in teams that need additional protection (content with high incoming damage where survivability is a concern)

**Echo Main Stats Priority**
- 4-Cost Echo (Heron, Beringal, or Geochelone): ATK% (general) or Aero DMG Bonus (Sierra Gale build)
- 3-Cost Echoes (×2): ATK% or Aero DMG Bonus
- 1-Cost Echoes: ATK%

**Sub-Stat Priority:** Energy Regen (to ~140% breakpoint) > CRIT Rate = CRIT DMG > ATK% > Liberation DMG Bonus. Energy Regen is the first and most important threshold — without sufficient ER, Liberation cannot be cast reliably each rotation. Once ER is reached, CRIT stats and Liberation DMG Bonus amplify her primary damage source.

## Yangyang: Recommended Weapons

**Best-in-Slot 5-Star — Emerald of Genesis**
- Stat: Energy Regen — directly addresses Yangyang's primary build requirement
- Passive: ATK increases by 6% (up to ×2 stacks) when casting Resonance Skill; at 2 stacks, +12% ATK total for 10 seconds; Zephyr Domain is cast frequently on cooldown, keeping this active
- Multiple sources including Prydwen, Game8, Pocket Tactics, and wutheringwaves.gg all list Emerald of Genesis as best-in-slot without close competition among weapons Yangyang can equip
- Available from the standard banner (Acquaint Fate / Permanent); not a limited weapon; obtainable over time for all players

**Best 4-Star — Commando of Conviction**
- ATK stat; passive grants ATK% on Intro Skill cast — fires every rotation when entering via Intro
- A strong standard 4-star option; available from the standard pool and weapon shop; commonly obtained

**Battle Pass Option — Lumingloss**
- Passive amplifies Heavy Attack and Forte DMG — directly relevant to both Stormy Strike and Feather Release
- At higher Syntony (refinement) levels can surpass Commando of Conviction; requires Battle Pass investment; best at Syntony 4–5

**Alternative 4-Star — Lunar Cutter**
- ATK-focused; decent baseline; less ideal than Commando of Conviction or Lumingloss but functional at higher refinement

**F2P Option — Sword of Night**
- A reasonable stand-in until a better option is available; not competitive with Emerald of Genesis or top 4-stars but accessible and free to craft/obtain

**Avoid for Yangyang**
- Weapons without Energy Regen or ATK as primary stats; Yangyang's viability as a utility character hinges on reaching the ~140% Energy Regen breakpoint before spending resources on offensive stats; weapons with DMG Bonus or elemental stats misalign with her primary build goal

## Yangyang: Best Teams

**Version 1.0 Classic — Jiyan / Yangyang / Verina (or Baizhi)**
- **Yangyang** (Sub-DPS / Energy Battery): Groups enemies for Jiyan's Qingloong sweeps; Outro grants +20 Resonance Energy to Jiyan, enabling faster access to Emerald Storm; Wind Spirals groups enemies before Jiyan enters to maximize Qingloong hit coverage; Moonlit Clouds Outro also provides +22.5% ATK to Jiyan via Impermanence Heron set
- **Jiyan** (Main DPS): Primary beneficiary; his Qingloong Mode sweep attacks profit from grouped enemies; the +20 energy from Yangyang's Outro meaningfully accelerates Liberation cycling; he is also an Aero character but Yangyang's Outro energy is not element-restricted
- **Verina or Baizhi** (Healer/Support): Sustain and additional ATK buffing; Verina preferred for the stronger universal Outro; Baizhi as the accessible free alternative
- *This is the dominant Version 1.0 use case for Yangyang that made her relevant even as a free 4-star alongside limited 5-stars*

**Early Game — Rover (Spectro) / Yangyang / Baizhi**
- **Yangyang** (Sub-DPS / Energy Battery): Outro grants Resonance Energy to Rover for faster Liberation access; Wind Spirals groups enemies before Rover's AoE attacks; both characters are free to all players, making this fully F2P
- **Rover (Spectro)** (Main DPS): Benefits from energy restoration to cast Resonance Liberation faster; Yangyang's grouping makes Rover's Liberation hit more enemies simultaneously
- **Baizhi** (Healer/Support): Standard F2P healer; ATK buff to Rover
- *Recommended by multiple sources including Game8 and MisterMenPlays as the optimal starting team for players who have not yet pulled a premium DPS or healer*

**Liberation-Dependent DPS — [Any Liberation-Heavy DPS] / Yangyang / [Healer]**
- Yangyang's +20 Resonance Energy Outro scales its value with the Liberation Energy cost and playstyle of the Main DPS; characters with expensive, high-impact Liberations (Calcharo at 150 energy, Chixia at 150 energy) benefit the most from Yangyang's energy delivery; characters who do not use Liberation as their primary damage source benefit less
- Game8 specifically highlights the Chixia pairing: Chixia's Liberation requires 150 energy and her personal energy generation is not efficient; Yangyang's Outro substantially reduces the time between Liberation casts for Chixia

**Limitations**
- Yangyang lacks the offensive Outro buffs that define top-tier supports (Verina's All-Type Deepen, Yinlin's Electro + Liberation DMG, Changli's Fusion + Liberation DMG); her energy grant is uniquely valuable but not multiplicatively powerful for teams that already have strong Liberation energy management
- Her personal damage falls behind limited 5-star Sub-DPS characters significantly without S4–S6 investment
- She does not provide healing; a third-slot healer is required in most compositions

## Yangyang: Rotation Guide

**Standard Sub-DPS Rotation**
1. Enter via Intro Skill Cerulean Song (→ +1 Melody; Aero DMG Bonus buff; Concerto Energy generated)
2. Resonance Liberation: Wind Spirals (→ AoE vortex groups enemies; Aero DMG; Resonance Energy generated; cast first so all subsequent attacks hit clustered enemies)
3. Resonance Skill: Zephyr Domain (→ +1 Melody; additional grouping; Aero DMG; Concerto Energy generated)
4. Heavy Attack → Basic Attack (Zephyr Song) (→ +1 Melody; now at 3 Melodies total)
5. Jump → Basic Attack: Feather Release (→ consumes all 3 Melodies; aerial multi-hit Aero DMG; +30 Stamina restored; massive Concerto Energy generated)
6. Swap-cancel after aerial hit lands (optional: wait for landing sheath for +1 Basic Attack hit before swap)
7. Outro Skill: Zephyr's Gift fires → incoming Main DPS receives +4 Resonance Energy/s × 5s = +20 Resonance Energy total + Moonlit Clouds ATK buff (if equipped)

**Alternate — No Liberation / Skill Available (Pure Forte Focus)**
1. Enter via Intro Skill (+1 Melody)
2. Heavy Attack → Zephyr Song (+1 Melody) × 2 → at 3 Melodies
3. Jump → Feather Release (aerial plunge)
4. Swap out immediately after aerial hit for Outro

**General Rotation Principles**
- Cast Liberation **before** building Melodies so enemies are grouped when Feather Release hits
- Keep Resonance Skill on cooldown — it generates both a Melody and grouping simultaneously
- The jump → aerial Basic Attack path is preferred over Heavy Attack → Stormy Strike → aerial Basic Attack; it is faster and produces the same Feather Release outcome
- Feather Release can be swap-canceled after the aerial hit for faster rotation without losing the Outro trigger; the landing animation (sheath attack) is the only part lost
- Energy Regen sub-stat investment should reach ~140% before adding offensive stats; below this threshold, Liberation cycling is inconsistent and Outro Skill triggers are irregular

**Echo Usage Timing**
- **Impermanence Heron:** Use the echo skill **during Yangyang's on-field window before Outro**, so the +10 Resonance Energy to Yangyang and the Outro +12% DMG boost to the incoming character both fire in the same rotation; using it just before Outro is the most efficient timing
- **Bell-Borne Geochelone:** Use before swapping out; the shield and ATK/DEF buff transfer to the incoming Main DPS and remain active during their field time
- **Nightmare Feilian Beringal:** Use just before Feather Release for the Aero DMG + Heavy ATK bonus to amplify the aerial hit directly

## Yangyang: Sources

- Prydwen Institute — Yangyang build guide, rotation optimization, Moonlit Clouds analysis: https://www.prydwen.gg/wuthering-waves/characters/yangyang/
- Wutheringlab — Yangyang build and rotation guide: https://wutheringlab.com/character/yangyang-build/
- Game8 — Yangyang best builds, teams, skill priority, combos: https://game8.co/games/Wuthering-Waves/archives/454215
- GuildJen — Yangyang character guide including sequence breakdown: https://guildjen.com/yangyang-character-guide/
- Wutheringwaves.gg — Yangyang guide (builds, rotations, echo comparison): https://wutheringwaves.gg/yangyang-guide/
- Pocket Tactics — Yangyang build and weapon guide: https://www.pockettactics.com/wuthering-waves/yangyang
- MisterMenPlays — Yangyang combo and rotation guide: https://www.mistermenplays.com/wutheringwaves/builds/yangyang
- Fextralife — Yangyang build guide: https://fextralife.com/wuthering-waves-yangyang-build-guide/
- Genshin-Builds (WuWa section) — Yangyang skills, teams, sequences: https://genshin-builds.com/en/wuthering-waves/characters/yangyang
