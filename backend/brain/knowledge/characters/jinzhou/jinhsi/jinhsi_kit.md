---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/jinzhou/jinhsi/jinhsi_kit.md
character: Jinhsi
group: Huanglong / Jinzhou
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - spectro
  - broadblade
  - main-dps
---

# Jinhsi Kit Documentation
<!-- Sources: https://wutheringwaves.fandom.com/wiki/Jinhsi, https://wuthering.gg/characters/jinhsi, https://www.prydwen.gg/wuthering-waves/characters/jinhsi/, https://game8.co/games/Wuthering-Waves/archives/455405, https://wutheringlab.com/character/jinhsi-build/ -->

## Jinhsi: Combat Archetype and Role

- **Element:** Spectro
- **Weapon Type:** Broadblade
- **Role:** Main DPS — aerial burst hypercarry
- **Archetype:** Incarnation-state combatant; Resonance Skill nuke specialist
- **Introduced:** Version 1.1 (first dedicated Spectro Main DPS in the game)

Jinhsi is an on-field Main DPS whose entire kit is built around a two-phase combat loop: building resources on the ground, then entering the airborne **Incarnation** state where her enhanced Basic Attacks and Resonance Skill variants deal the bulk of her damage. Her primary damage source is the final Resonance Skill variant **Illuminous Epiphany**, which consumes her Forte resource (Incandescence) for a massive multiplier burst. She requires team members with Coordinated Attacks to charge her gauge efficiently and excels in quickswap compositions that trigger free Intro/Outro swaps via the **Unison** mechanic.

## Jinhsi: Key Resources (Forte Mechanics Overview)

Jinhsi's Forte Circuit centers on two interlocking resources: **Incandescence** (her primary damage-scaling gauge) and **Unison** (her Outro bypass mechanic). These interact with her multi-stage Resonance Skill to define her rotation structure.

- **Incandescence** is the gauge tracked on her Forte Circuit, capping at 50. It fuels the damage multiplier of Illuminous Epiphany — more Incandescence consumed means exponentially higher burst damage.
- **Eras in Unity** is the passive field buff she applies to all nearby allies whenever she is in the party. Allies with Eras in Unity generate Incandescence for Jinhsi by dealing Attribute DMG (1 stack per 3s per attribute) and Coordinated Attack damage (2 stacks per 3s per attribute), making coordinated attack characters her strongest synergy.
- **Unison** is triggered after casting Illuminous Epiphany. While active, swapping off Jinhsi fires her Outro Skill and the incoming character's Intro Skill without spending any Concerto Energy — allowing multiple free Outro/Intro cycles per rotation.

## Jinhsi Forte Circuit: Incandescence & Unison

**Incandescence Generation**
- **From Eras in Unity (standard Attribute DMG):** +1 Incandescence per instance, up to 1 time per 3s per Attribute type
- **From Eras in Unity (Coordinated Attacks):** +2 Incandescence per instance, up to 1 time per 3s per Attribute type
- **Maximum cap:** 50 Incandescence
- **Consumption:** All stacks consumed on cast of Illuminous Epiphany; each point of Incandescence adds a bonus DMG Multiplier percentage to Stella Glamour

**Incandescence State Transitions**
- Jinhsi must complete 4 Basic Attacks (standard) → triggers Overflowing Radiance availability (5s window)
- Casting Overflowing Radiance → enters **Incarnation** (airborne state)
- In Incarnation: use Incarnation Basic Attacks (up to 4 stages) → after Stage 4, Incarnation terminates and **Ordination Glow** activates
- During Ordination Glow: Resonance Skill slot becomes **Illuminous Epiphany**; casting it consumes all Incandescence for the burst nuke and grants **Unison**

**Unison**
- Triggered once every 25 seconds (cooldown gated)
- Consumed on swap — removes Unison, triggers Jinhsi's Outro and incoming character's Intro simultaneously, without spending Concerto Energy
- If Concerto Energy is already full, Unison is consumed before Concerto Energy on swap

## Jinhsi: Stats Baseline

| Level | HP | ATK | DEF | Crit Rate | Crit DMG |
|-------|----|-----|-----|-----------|----------|
| Lv. 1 | ~836 | ~33 | ~100 | 5% | 150% |
| Lv. 20 | ~2,156 | ~85 | ~258 | 5% | 150% |
| Lv. 40 | ~4,302 | ~170 | ~516 | 5% | 150% |
| Lv. 60 | ~7,160 | ~283 | ~858 | 5% | 150% |
| Lv. 80 | ~10,530 | ~414 | ~1,260 | 5% | 150% |
| Lv. 90 | ~12,600 | ~495 | ~1,505 | 5% | 150% |

*Note: Baseline stats do not include Forte Attribute Bonuses or equipment. Actual values may vary slightly by source version.*

## Jinhsi: Ascension Materials

| Ascension | Level Cap | Materials Required |
|-----------|-----------|-------------------|
| 1 | 20→40 | Howler Core (Lv.1) ×4, Loong's Pearl ×4, Shell Credits ×5,000 |
| 2 | 40→50 | Howler Core (Lv.2) ×4, Loong's Pearl ×8, Shell Credits ×10,000 |
| 3 | 50→60 | Howler Core (Lv.3) ×8, Loong's Pearl ×12, Elegy Tacet Core ×4, Shell Credits ×15,000 |
| 4 | 60→70 | Howler Core (Lv.3) ×8, Loong's Pearl ×16, Elegy Tacet Core ×8, Shell Credits ×20,000 |
| 5 | 70→80 | Howler Core (Lv.3) ×12, Loong's Pearl ×20, Elegy Tacet Core ×12, Shell Credits ×40,000 |
| 6 | 80→90 | Howler Core (Lv.3) ×12, Loong's Pearl ×24, Elegy Tacet Core ×16, Shell Credits ×80,000 |

**Total Shell Credits (Ascension):** ~170,000
- **Loong's Pearl:** Found at Mt. Firmament and Mianloong Chamber; purchasable at Shifang Pharmacy
- **Elegy Tacet Core:** Dropped by Mourning Aix boss (near Whining Aix's Mire, southern Huanglong)
- **Howler Core:** Looted from beast/animal-type enemies in Huanglong

## Jinhsi: Character Kit: Basic Attack — Solar Flare

**Standard Phase (Ground)**
- Stage 1–4: Consecutive strikes dealing Spectro DMG, 4-hit chain
- Completing Stage 4 (or using Intro Skill Loong's Halo while not in Incarnation) makes **Overflowing Radiance** available for 5 seconds
- **Heavy Attack:** Stamina-consuming charged attack, Spectro DMG
- **Mid-Air Attack:** Stamina-consuming plunging attack, Spectro DMG
- **Dodge Counter:** Counter after successful Dodge, Spectro DMG

**Incarnation Phase (Airborne)**
- All Incarnation Basic Attacks deal Spectro DMG counted as Resonance Skill DMG
- **Incarnation: Basic Attack:** Up to 4 consecutive airborne strikes; attack cycle does not reset; castable mid-air
- **Incarnation: Heavy Attack:** Airborne stamina-consuming strike, Spectro DMG
- **Incarnation: Dodge:** Mid-air dodge, multi-cast at Stamina cost
- **Incarnation: Dodge Counter:** Counter after airborne dodge, Spectro DMG
- After Stage 4 of Incarnation Basic Attack → Incarnation ends, **Ordination Glow** activates

## Jinhsi: Character Kit: Resonance Skill — Overflowing Radiance / Crescent Divinity / Illuminous Epiphany

Jinhsi's Resonance Skill has four variants, the most of any character in the game. They are accessed sequentially through her state machine.

**Overflowing Radiance (Standard — Ground)**
- Available for 5s after Basic Attack Stage 4 or Intro Skill
- Dash forward, deal Spectro DMG
- Sends Jinhsi into **Incarnation** (airborne state)
- Cooldown: ~12 seconds (making Incarnation uptime very high)

**Crescent Divinity (Incarnation Skill)**
- Available in Incarnation state (replaces Resonance Skill slot)
- Dash forward in the air and summon a lightning strike, dealing Spectro DMG
- Castable mid-air

**Illuminous Epiphany (Ordination Glow Skill — Primary Damage)**
- Available after Stage 4 Incarnation Basic Attack triggers Ordination Glow
- Sends out **Solar Flare** which detonates as **Stella Glamour**, dealing Spectro DMG after a short delay
- Consumes all Incandescence (up to 50); each point of Incandescence adds a bonus DMG Multiplier to Stella Glamour
- After casting: grants **Unison** (once per 25s)
- Castable mid-air
- This is Jinhsi's highest-damage ability and the primary optimization target

## Jinhsi: Character Kit: Resonance Liberation — Purge of Evil / Purge of Light

- **Activation:** Casts Resonance Liberation consuming Resonance Energy
- **Effect:** Summons Sentinel Jué to the battlefield
  - Jué soars through the air, dealing Spectro DMG
  - Summons thunderbolts striking nearby enemies up to 5 times, each dealing Spectro DMG
  - Jué spirals downward, striking surrounding enemies twice, each hit dealing Spectro DMG
- Provides a large burst of AoE Spectro damage
- S4 Effect: Grants all nearby team members 20% Attribute DMG Bonus for 20s on cast

*Representative multipliers (wuthering.gg data): Jué's initial strike ~48.64% Spectro DMG; each thunderbolt ~19.46% Spectro DMG; each downward spiral strike ~48.64% Spectro DMG.*

## Jinhsi: Inherent Passives

**Inherent Skill 1 — Radiant Surge**
- When Jinhsi casts Resonance Liberation or Resonance Skill Illuminous Epiphany, all nearby Resonators on the team gain **20% Attribute DMG Bonus for 20s**
- This team-wide buff makes Jinhsi a partial support as well as DPS

**Inherent Skill 2 — Temporal Resonance**
- When Jinhsi is on the team, Eras in Unity's Coordinated Attack trigger frequency is enhanced
- Reduces internal cooldown on Coordinated Attack Incandescence generation, accelerating gauge fill in coordinated attack-heavy teams

## Jinhsi: Intro/Outro Skills

**Intro Skill — Loong's Halo**
- Triggered when Jinhsi enters the field from a swap
- Deals Spectro DMG (attack the target)
- When not in Incarnation, using Loong's Halo also makes Overflowing Radiance available (allowing early entry into Incarnation without completing the Basic Attack chain)
- S3: Grants +12 Incandescence and a stack of Immortal's Descendancy (+25% ATK, up to 2 stacks, 20s) on cast

**Outro Skill — (Eras in Unity Enhancement)**
- Triggered when Jinhsi swaps off via Unison or standard Concerto Energy
- Reduces the Eras in Unity internal cooldown for all allies to 1 second (from 3 seconds) for 20 seconds
- This dramatically accelerates Incandescence generation for the next rotation cycle when Jinhsi re-enters

## Jinhsi: Skill Upgrade Materials

| Skill Level | Materials Required |
|-------------|-------------------|
| 1→2 | Waveworn Residue 210 ×4, Howler Core ×2, Shell Credits ×1,000 |
| 2→3 | Waveworn Residue 226 ×4, Howler Core ×4, Shell Credits ×3,000 |
| 3→4 | Waveworn Residue 242 ×8, Howler Core ×8, Shell Credits ×8,000 |
| 4→5 | Waveworn Residue 258 ×4, Sentinel's Dagger ×2, Howler Core ×12, Shell Credits ×20,000 |
| 5→6 | Waveworn Residue 274 ×4, Sentinel's Dagger ×3, Howler Core ×16, Shell Credits ×40,000 |
| 6→7 | Waveworn Residue 290 ×8, Sentinel's Dagger ×5, Howler Core ×20, Shell Credits ×80,000 |
| 7→8 | Waveworn Residue 290 ×8, Sentinel's Dagger ×8, Howler Core ×24, Shell Credits ×120,000 |
| 8→9 | Waveworn Residue 290 ×16, Sentinel's Dagger ×12, Howler Core ×28, Shell Credits ×160,000 |
| 9→10 | Waveworn Residue 290 ×16, Sentinel's Dagger ×16, Howler Core ×40, Shell Credits ×200,000 |

**Total Shell Credits (Forte, all skills):** ~2,030,000
- **Sentinel's Dagger:** Weekly boss drop from **Jué** (Mt. Firmament, Huanglong; unlocked after Chapter 1 Act 7)
- **Waveworn Residue:** Broadblade Forgery Challenge rewards (use Huanglong Forgery for passive Howler Core gain)

## Jinhsi: Resonance Chains (Sequences)

**S1 — Herald of Revival**
- When casting Incarnation: Basic Attack or Resonance Skill Crescent Divinity, Jinhsi gains 1 stack of Herald of Revival (max 4 stacks, lasts 6s)
- Casting Illuminous Epiphany consumes all stacks; each stack increases Illuminous Epiphany DMG by **+20%** (up to +80% at 4 stacks)
- *Impact:* Meaningful single-rotation damage boost; requires clean 4-hit Incarnation Basic Attack chain to maximize

**S2 — Timeless Respite**
- Jinhsi restores **40–50 Incandescence** (full gauge) after being out of combat for more than 4 seconds (triggers every 4s)
- *Impact:* Strongest quality-of-life sequence; allows full-gauge Illuminous Epiphany at fight start without coordinated attack ramp-up. Approximately 18.9% more damage at fight opening vs. S1. Excellent for open world and Tower of Adversity boss phases. High priority pull.

**S3 — Immortal's Descendancy**
- After using Intro Skill Loong's Halo, Jinhsi gains **+12 Incandescence** and a stack of Immortal's Descendancy (**+25% ATK** per stack, up to 2 stacks, lasting 20s)
- *Impact:* Up to +50% ATK increase when 2 stacks are active, which is substantial. Stack duration extends on re-gain. Significant sustained damage upgrade.

**S4 — Eons United**
- When Jinhsi casts Resonance Liberation or Illuminous Epiphany, all nearby team members gain **+20% Attribute DMG Bonus for 20s**
- *Impact:* Transforms Jinhsi into a partial team buffer. Approximately +6.3% personal DPS increase; value scales with team strength. Good stopping point for players interested in support value.

**S5 — Lustrous Transcendence**
- The DMG Multiplier of Resonance Liberation is increased by **120%** (i.e., Liberation DMG × 2.2)
- *Impact:* Approximately +15.4% overall DPS boost. Liberation becomes a major damage contribution rather than supplementary.

**S6 — Radiant Sovereign**
- DMG Multiplier of Illuminous Epiphany (Stella Glamour component) increased by **45%**; the additional multiplier granted by each point of Incandescence is also increased by **45%** (effectively ×1.45 applied to all Incandescence scaling)
- *Impact:* Approximately +22.3% overall DPS. Massive boost to Jinhsi's core ability. Full S6 transforms her into one of the highest raw DPS characters in the game.

**Sequence Pull Priority:** S0R1 for baseline; S2R1 for best QoL and open world; S6R1 for absolute maximum damage.

## Jinhsi: Recommended Echo Sets

**Best-in-Slot: Celestial Light (5-piece)**
- Full 5-piece Celestial Light is Jinhsi's premier set, providing significant Spectro DMG Bonus that multiplies with her already-high Resonance Skill multipliers
- The Echo Set resonates with her Spectro identity and Sentinel connection
- **Main Echo:** Jué (the Sentinel itself) — Jué's Echo Skill summons the Sentinel, deals Spectro DoT damage, and grants a 16% Resonance Skill DMG Bonus for 15s; DoT ticks also generate Incandescence via Eras in Unity, adding roughly 12 additional Incandescence per rotation vs. alternatives

**Alternative:** Mourning Aix (4-Cost Echo, used when Jué is unavailable for Echo slot)
- Provides a significant ATK buff (~4.6% benefit), substantially weaker than Jué's ~20% Incandescence-enhanced advantage

**Echo Main Stats Priority**
- 4-Cost Echo: CRIT Rate or CRIT DMG (whichever brings you closer to 1:2 ratio)
- 3-Cost Echoes (×2): Spectro DMG Bonus (preferred for non-signature weapon users); ATK% + Spectro DMG Bonus combination offers ~1–3% improvement when specific team conditions apply
- 1-Cost Echoes: ATK% or HP (sub-stats matter more than mains here)

**Sub-Stat Priority:** Energy Regen (to breakpoint) ≥ CRIT Rate = CRIT DMG > ATK% > Resonance Skill DMG Bonus > Flat ATK

## Jinhsi: Best Weapon

**Signature — Ages of Harvest (5-Star Broadblade)**
- Best-in-slot by a significant margin; purpose-built for Jinhsi's kit
- Stat: CRIT Rate (highly valued on her)
- Effect: 24% Attribute DMG Bonus baseline; Intro Skill grants **Ageless Marking** (+48% Resonance Skill DMG Bonus for 12s); Resonance Skill use grants **Ethereal Endowment** (+48% Resonance Skill DMG Bonus for 12s)
- Both buffs directly amplify Illuminous Epiphany, her primary damage source

**F2P Best — Broadblade of Night**
- Craftable/obtainable via chest exploration
- Provides ATK stat increase; no complex conditional requirements
- Best free-to-play option; recommended for players without premium weapons

**General Alternatives**
- Any Broadblade providing CRIT Rate, ATK%, or Energy Regen is viable
- Energy Regen weapons are especially valuable for reducing Concerto buildup time and enabling more reliable Liberation uptime

## Jinhsi: Best Teams

**Premium Meta — Jinhsi / Zhezhi / Shorekeeper**
- **Jinhsi** (Main DPS): Primary on-field damage; Illuminous Epiphany burst
- **Zhezhi** (Sub DPS/Buffer): Inklit Spirits provide Coordinated Attacks in Spectro element, generating Incandescence at accelerated rate; Outro provides Resonance Skill DMG buff
- **Shorekeeper** (Support): Resonance Liberation buffs team Crit Rate; paired with Zhezhi's Outro buff, Jinhsi's Resonance Skill damage becomes enormous
- *Rotation:* Shorekeeper buffs → Zhezhi Outro → Jinhsi Loong's Halo (Intro) → Incarnation chain → Illuminous Epiphany burst

**Standard Budget — Jinhsi / Yuanwu / Baizhi**
- **Yuanwu** (Sub DPS): Resonance Skill summons lightning orbs that deal Electro Coordinated Attacks; generates Incandescence from a different element attribute; Outro reduces enemy Vibration Strength for faster Stagger
- **Baizhi** (Support/Healer): Best F2P healing option; provides team sustainability
- *Note:* Yuanwu provides Electro Coordinated Attacks — these contribute Incandescence via the 2-stack Electro Eras in Unity trigger

**Key Team-Building Principle:** Jinhsi wants teammates who deal Attribute DMG via Coordinated Attacks of different element types. Having two different-element Coordinated Attack characters (e.g., Electro Yuanwu + Spectro Zhezhi) enables simultaneous Incandescence generation from multiple attribute channels.

## Jinhsi: DPS Benchmarks

- Jinhsi consistently ranks at the top of Spectro DPS and is considered one of the highest burst-damage characters in the game as of Version 1.x–2.x
- She excels in both single-target and AoE thanks to Jué's Lightning strikes and Stella Glamour's wide hitbox
- **Cleave:** Stella Glamour hits all enemies in range simultaneously, making her exceptional for mob-clearing while maintaining competitive single-target output
- At S0 with signature weapon and premium team (Zhezhi + Shorekeeper), she achieves among the highest DPS in the game
- At S6, she surpasses most characters by a significant margin due to compounding multipliers on Illuminous Epiphany
- Her main limitation is team dependency: solo or low-coordinated-attack teams drastically reduce her Incandescence generation and therefore her burst damage ceiling

## Jinhsi: Sources

- Wuthering Waves Fandom Wiki — Jinhsi: https://wutheringwaves.fandom.com/wiki/Jinhsi
- Wuthering.gg — Jinhsi kit and Forte mechanics: https://wuthering.gg/characters/jinhsi
- Prydwen Institute — Jinhsi build guide and DPS analysis: https://www.prydwen.gg/wuthering-waves/characters/jinhsi/
- Game8 — Jinhsi builds, teams, ascension materials: https://game8.co/games/Wuthering-Waves/archives/455405
- Game8 — Jinhsi ascension and forte materials: https://game8.co/games/Wuthering-Waves/archives/494451
- Wutheringlab — Jinhsi sequences and mechanics: https://wutheringlab.com/character/jinhsi-build/
- Esports.gg — Jinhsi full kit and skills: https://esports.gg/guides/wuthering-waves/jinhsi-skills-and-full-kit-revealed-in-wuthering-waves-leaks/
- GuildJen — Jinhsi character guide: https://guildjen.com/jinhsi-character-guide/
- Sportskeeda — Jinhsi resonance chain guide: https://www.sportskeeda.com/esports/wuthering-waves-jinshi-resonance-chain-guide
