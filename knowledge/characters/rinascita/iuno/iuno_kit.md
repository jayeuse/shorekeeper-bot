---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/septimont_characters/iuno/iuno_kit.md
character: Iuno
group: Septimont
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - aero
  - gauntlets
  - sub-dps
  - healer
  - buffer
  - lunar-cycle
  - sentience
  - full-moon-domain
  - heavy-attack-amplification
---

# Iuno Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/iuno/, https://game8.co/games/Wuthering-Waves/archives/524889, https://wuthering.gg/characters/iuno, https://wutheringwaves.fandom.com/wiki/Iuno -->

## Iuno: Combat Archetype and Role
- **Element/Attribute:** Aero
- **Weapon Type:** Gauntlets
- **Role:** Sub-DPS / Healer / Support — a complete hybrid that deals significant personal Resonance Liberation-tagged Aero DMG, continuously heals the team, provides self-shielding (enabling Crown of Valor synergy), restores STA via her Full Moon Domain, and delivers a best-in-class **50% Heavy Attack DMG Amplification** via Outro; her signature buff (Blessing of the Wan Light: up to 40% all-DMG Amplification at S2) is currently fully achievable only with Augusta as Main DPS
- **Scaling:** ATK (healing scales ATK; personal damage scales ATK via Resonance Liberation DMG multipliers)
- **Damage Profile:** Virtually all meaningful personal damage carries the **Resonance Liberation DMG** tag — Moonbow Basic Attacks, Arc Beyond the Edge, Absolute Fullness, Flux Heavy Attacks in Lunar Cycle, and Dodge Counters in New Moon all count as Resonance Liberation DMG; this makes her the primary target for Resonance Liberation DMG Bonus investment
- **Best-fit Team:** Augusta + Iuno + Shorekeeper or Augusta + Iuno + Qiuyuan (S-tier Augusta pair); functions as capable sub-DPS in non-Augusta teams but loses the 40% Blessing cap and key shield-cycle synergies

## Iuno: Key Resources (Forte Mechanics Overview)

Iuno's entire kit revolves around **Lunar Cycle**, a persistent two-state mode with its own stance-specific weapons, moves, and resource logic. It is activated by Resonance Skill — Closing Refrain or by casting Resonance Liberation, and it has two phases: **Half Moon** (default entry; Moonring weapon; Sentience builds) and **New Moon** (Moonbow weapon; Sentience consumed for enhanced hits, healing, and Concerto Regen).

The transition between phases is handled by **Heavy Attack — Flux**: from Half Moon, Flux: Moonbow switches to New Moon; from New Moon, Flux: Moonring switches back to Half Moon. Both Flux attacks deal Aero DMG counted as Resonance Liberation DMG.

**Sentience** (0–100) is Iuno's Forte gauge. It builds in Half Moon via attacks and specific skill casts, then is consumed in New Moon to enhance Moonbow Basic Attacks, Arc Beyond the Edge, and Moonbow Dodge Counter — increasing their DMG Multipliers, restoring extra Concerto Energy, and healing nearby teammates. Healing, enhanced damage, and Concerto acceleration all trigger together whenever Sentience is spent.

The third major system is **Blessing of the Wan Light**, applied by stacking shield triggers through the Inherent Skill or Full Moon Domain. Each stack grants 4% all-DMG Amplification (up to 10 stacks = 40%) for 10s, refreshed on new stack gain, and removed if the benefiting Resonator leaves the field. This makes her unusually "quickswap-unfriendly" — she does not distribute buffs on leave; they persist only while the buffed character remains on field.

## Iuno Forte Circuit: Lunar Cycle / Sentience

**Activating Lunar Cycle:**
- Resonance Skill — Closing Refrain (after: BA Stage 3, Intro Skill, or Pulse of Origins)
- Resonance Liberation — Beneath Lunar Tides
- Duration: 15s; ends on environmental interaction, Utility use, or holding Jump

**Sentience Generation:**
- Intro Skill: +40 Sentience
- Resonance Liberation: +60 Sentience
- Resonance Skill — Closing Refrain / Unfinished Refrain: +25 Sentience
- Moonring Basic Attack, Moonring Dodge Counter, Mid-air Attack (while in Lunar Cycle): restore Sentience on hit

**Sentience Consumption (New Moon only):**
Each of the following consumes Sentience when cast in Lunar Cycle — New Moon:
- Enhanced Moonbow - Basic Attack Stages 1/2/3
- Enhanced Moonbow - Dodge Counter
- Enhanced Arc Beyond the Edge (Resonance Skill in New Moon; 2 charges)
Each consumption: increases that skill's DMG Multiplier, restores extra Concerto Energy, and heals nearby Resonators by an ATK-scaling amount

**Lunar Cycle State Transitions:**
- Half Moon → Heavy Attack - Flux: Moonbow → New Moon (deals 126.00% Aero / Reso Lib DMG)
- New Moon → Heavy Attack - Flux: Moonring → Half Moon (deals 39.83%×4 Aero / Reso Lib DMG)
- Both Flux attacks cost 25 STA and are available mid-air

**Heavy Attack — Absolute Fullness** (unlocked when Concerto Energy is full):
- Replaces Heavy Attack entirely; ends Lunar Cycle; triggers once every 25s
- Heals nearby Resonators (97.71% ATK); deals 80.00% Aero DMG (Resonance Liberation tag) to nearby targets
- Conjures **Full Moon Domain** at her location for 30s:
  - Restores HP periodically (16.29% ATK every 5s) and STA (20 STA per interval) for Resonators inside
  - Gaining a Shield inside the Domain grants 1 stack of **Blessing of the Wan Light** (triggers once per 0.5s, up to 10 stacks max)

**Blessing of the Wan Light (stack details):**
- 1 stack = 4% all-DMG Amplification for 10s (refreshed on new stack); max 10 stacks = 40% all-DMG Amplification
- Removed if the receiving Resonator is switched off the field
- Inherent Skill — Waxing Ascent generates a micro-Shield on nearly every action, enabling solo stack accumulation outside the Domain
- S2 (10 stacks) grants an additional +40% all-DMG Amplification → 80% total amplification at full stacks with S2

## Iuno: Stats Baseline

| Stat | Lv. 1 | Lv. 90 |
|------|-------|--------|
| HP | ~870 | 10,525 |
| ATK | ~32 | 450 |
| DEF | ~95 | 1,124 |
| CRIT Rate | 5% | 5% (+8% from Forte nodes) |
| CRIT DMG | 150% | 150% |
| Energy Regen | 100% | 100% |
| Max Resonance Energy | 125 | 125 |

Forte minor nodes add: +8% CRIT Rate and +12% ATK% at full unlock.
Target stats: CRIT Rate 70–80% | CRIT DMG 250%+ | Energy Regen 120–125% | ATK 2,000+

## Iuno: Ascension Materials

| Ascension | Level Cap | Materials |
|-----------|-----------|-----------|
| 1 | 20 → 40 | Sliverglow Bloom ×4, LF Polygon Core ×4, Shell Credits ×5,000 |
| 2 | 40 → 50 | Sliverglow Bloom ×8, MF Polygon Core ×4, Abyssal Husk ×2, Shell Credits ×10,000 |
| 3 | 50 → 60 | Sliverglow Bloom ×12, MF Polygon Core ×8, Abyssal Husk ×4, Shell Credits ×15,000 |
| 4 | 60 → 70 | Sliverglow Bloom ×16, HF Polygon Core ×4, Abyssal Husk ×8, Shell Credits ×20,000 |
| 5 | 70 → 80 | Sliverglow Bloom ×20, HF Polygon Core ×8, Abyssal Husk ×12, Shell Credits ×40,000 |
| 6 | 80 → 90 | Sliverglow Bloom ×24, FF Polygon Core ×4, Abyssal Husk ×16, Shell Credits ×80,000 |

**Total Ascension:** 60× Sliverglow Bloom, 4× LF + 12× MF + 12× HF + 4× FF Polygon Core, 46× Abyssal Husk, 170,000 Shell Credits
- **Sliverglow Bloom:** Field-gathered in Septimont; use interactive map (prydwen.gg) to locate nodes efficiently
- **Abyssal Husk:** Boss drop from the enemy unlocked in later Septimont area content (cross-reference in-game boss index)
- **Polygon Core (LF/MF/HF/FF):** Forgery Challenges in the Septimont/Rinascita region

## Iuno: Character Kit: Basic Attack — Moon Steps

**Moonring - Basic Attack (outside Lunar Cycle; 3-hit chain):**
- Stage 1: 44.10% Aero DMG
- Stage 2: 23.17%×2 + 23.87% Aero DMG
- Stage 3: 44.26%×2 + 45.60% Aero DMG — casting this enables Closing Refrain for 5s

**Moonring - Dodge Counter (outside Lunar Cycle):**
- 41.29%×2 + 42.54% Aero DMG; can chain into BA Stage 3

**Mid-air Attack:** 27.00%×2 Aero DMG; STA Cost 30

**Moonbow - Basic Attack (New Moon; 3-hit chain; all Resonance Liberation DMG):**
- Stage 1: 63.60% (enhanced: 103.60%)
- Stage 2: 28.00%×3 (enhanced: 48.00%×3)
- Stage 3: 84.00%×2 (enhanced: 134.00%×2)

**Moonbow - Dodge Counter (New Moon; Resonance Liberation DMG):**
- 52.00%×3 (enhanced: 78.67%×3)

*Enhanced versions activate when Sentience is available and is consumed on cast; also heal (e.g., Stage 1: 13.03% ATK; Stage 3: 24.43% ATK) and restore extra Concerto Energy.*

## Iuno: Character Kit: Resonance Skill — Foresight Fugue

**Pulse of Origins** (base skill; dash):
- 9.38%×7 + 65.65% Aero DMG; Cooldown: 6s; Concerto Regen: 6
- Casting enables Closing Refrain for 5s

**Closing Refrain** (after: BA Stage 3, Intro Skill, or Pulse of Origins; replaces Resonance Skill for 5s):
- 70.79%×2 + 72.93% Aero DMG; activates Lunar Cycle (Half Moon); Concerto Regen: 8
- Cooldown: 8s (shared with Unfinished Refrain)

**Unfinished Refrain** (in Lunar Cycle - Half Moon; same stats as Closing Refrain):
- 70.79%×2 + 72.93% Aero DMG; Concerto Regen: 8; same cooldown

**Arc Beyond the Edge** (in Lunar Cycle - New Moon; 2 charges; Resonance Liberation DMG):
- 110.55%×2 (enhanced with Sentience: 160.55%×2); Cooldown: 10s; Concerto Regen: 8
- Directional input extends travel distance; if Iuno is hit mid-air, cast immediately recovers from the attack
- Key source of both Sentience spending, healing, Concerto Regen acceleration, and heavy Resonance Liberation DMG

## Iuno: Character Kit: Resonance Liberation — Beneath Lunar Tides

Iuno unleashes a powerful strike dealing **550.00% Aero DMG** (Resonance Liberation tag), activating Lunar Cycle state on hit.
- Concerto Regen: 20; Cooldown: 25s; Resonance Energy Cost: 125
- On cast: restores **60 Sentience**
- Inherent Skill — **Derivation**: casting Intro Skill or Resonance Liberation immediately grants **5 stacks of Blessing of the Wan Light**

The Liberation's role in rotations is dual: it is both a high-damage personal hit and the primary re-entry point into Lunar Cycle when Closing Refrain cannot be triggered immediately. It also front-loads the Blessing stack ramp for the incoming DPS.

## Iuno: Inherent Passives

**Waxing Ascent**
- Every time Iuno casts Basic Attack, Heavy Attack, Dodge Counter, Resonance Skill, Resonance Liberation, or Intro Skill, she gains a Shield equal to **32% of her ATK** for 15s
- Triggers on virtually every action; Shield does not transfer to incoming Resonators
- This perpetual micro-shielding is the engine for Crown of Valor set stacking, her signature weapon's DEF-ignore passive, and S1's extra Crown of Wills — the Shield itself is too small to block real attacks, but its consistent generation is the kit's backbone

**Derivation**
- When Iuno casts Intro Skill or Resonance Liberation, she immediately gains **5 stacks of Blessing of the Wan Light**
- Front-loads the buff stack ramp on rotation entry; the incoming DPS benefits from a head-start toward the 10-stack cap the moment Iuno enters and casts

## Iuno: Intro/Outro Skills

**Intro Skill — Illuminated Manifestation**
- DMG: 8.00%×7 + 24.00% Aero DMG; Concerto Regen: 10
- On cast: restores **40 Sentience**
- Triggers **Derivation** → immediately grants 5 stacks of Blessing of the Wan Light to the incoming or nearby Resonator
- Enables Closing Refrain for 5s after cast

**Outro Skill — From Gloom to Gleam**
- Deals 100% Aero DMG to the target
- The incoming Resonator gains **50% Heavy Attack DMG Amplification** for **14s** (ends if they are switched out)
- Casting Outro Skill does NOT interrupt Heavy Attack — Absolute Fullness, and the buff still applies if Absolute Fullness is mid-animation
- One of the strongest Outro buffs available for Heavy Attack-centric teams; 50% amplification for 14s exceeds Mortefi's Outro in coverage and competes with it in amplitude

## Iuno: Skill Upgrade Materials

Requires: **Cadence Seed / Bud / Leaf / Blossom** (Forgery Challenge), **The Netherworld's Stare** (weekly boss drop), and **Polygon Core** (LF/MF/HF/FF).

| Skill Level | Cadence Material | Netherworld's Stare | Polygon Core | Shell Credits |
|-------------|-----------------|---------------------|--------------|---------------|
| 2 | Seed ×3 | — | LF ×2 | 5,000 |
| 3 | Seed ×5 | — | LF ×4 | 10,000 |
| 4 | Bud ×4 | — | MF ×3 | 15,000 |
| 5 | Bud ×6 | — | MF ×5 | 20,000 |
| 6 | Leaf ×5 | Stare ×1 | HF ×3 | 30,000 |
| 7 | Leaf ×8 | Stare ×1 | HF ×5 | 45,000 |
| 8 | Blossom ×5 | Stare ×2 | FF ×3 | 60,000 |
| 9 | Blossom ×8 | Stare ×2 | FF ×5 | 75,000 |
| 10 | Blossom ×10 | Stare ×3 | FF ×6 | 90,000 |

**Total Skill Upgrade (all skills):** 25× Seed, 28× Bud, 55× Leaf, 67× Blossom, 26× The Netherworld's Stare, 25× LF + 28× MF + 40× HF + 57× FF Polygon Core, 2,030,000 Shell Credits

**Skill Priority:** Resonance Liberation > Forte Circuit > Intro Skill > Resonance Skill > Basic Attack

## Iuno: Resonance Chains (Sequences)

**S1**
When Iuno is in Lunar Cycle, her ATK is increased by 40%. When inside the Full Moon Domain, she additionally restores 1 point of Resonance Energy per second. Resonance Skill — Arc Beyond the Edge and Heavy Attack — Absolute Fullness become immune to interruption.
*Value: Solid baseline upgrade. The 40% ATK boost applies to all ATK-scaling elements including healing and personal damage during the entire Lunar Cycle window. Interruption immunity on Arc Beyond the Edge is highly practical given her aerial combat vulnerability.*

**S2**
Resonators in the team with 10 stacks of Blessing of the Wan Light gain an additional 40% all-DMG Amplification.
*Value: The single most impactful node — doubles the buff ceiling from 40% to 80% all-DMG Amplification at 10 stacks. This is the primary reason Augusta + Iuno is a dominant team: S2 is the tipping point where Iuno's buff output becomes best-in-class for Heavy Attack-centric DPS. S0→S2 is the priority investment bracket for competitive play.*

**S3**
When Iuno is in Lunar Cycle, DMG dealt by Moonbow - Basic Attack, Arc Beyond the Edge, and Moonbow - Dodge Counter is Amplified by 65%. Additionally, within a certain period after performing Moonbow Basic Attack or Dodge Counter, casting Arc Beyond the Edge does not reset the Moonbow Basic Attack cycle.
*Value: Significant personal DPS increase and rotation flexibility. The cycle-preservation QoL on Arc Beyond the Edge meaningfully improves her New Moon damage windows.*

**S4**
Casting Heavy Attack — Absolute Fullness grants a Shield equal to 160% of Iuno's ATK to all Resonators in the team for 30s (cannot be passed to the incoming Resonator).
*Value: Team-wide survivability. At S1+, Iuno's ATK is boosted 40% in Lunar Cycle, making this Shield more substantial than the base number implies. Useful for content with heavy incoming damage but not a DPS node.*

**S5**
Iuno gains 20% Resonance Liberation DMG Bonus.
*Value: Moderate personal damage upgrade. Resonance Liberation DMG is her dominant damage tag, so +20% applies broadly — but the ceiling is lower than S2 and S3.*

**S6**
The DMG Multiplier of Heavy Attack — Absolute Fullness is increased by 1600%. Upon casting this skill, Iuno re-enters Lunar Cycle — New Moon, gains 100 points of Sentience, and resets all cooldowns of Resonance Skill — Arc Beyond the Edge.
*Value: Transformational for her personal damage profile — Absolute Fullness was previously a moderate utility/healing tool; at S6 it becomes a massive burst hit. Full Sentience reset and Arc Beyond the Edge cooldown reset enables an extended New Moon burst window after every Absolute Fullness cast. S6 Iuno functions as a viable Main DPS.*

## Iuno: Recommended Echo Sets

**Best: Crown of Valor (3-pc) + Sierra Gale (2-pc)**
Iuno's Inherent Skill — Waxing Ascent generates a Shield on virtually every action, satisfying Crown of Valor's shield-uptime requirement with almost no effort. Crown of Valor's ATK% and Crit. DMG% buffs stack on each shield-gain; its Heavy Attack DMG% bonus and DEF-ignore effect pair with her signature weapon to amplify her Resonance Liberation DMG output. Sierra Gale's 2-pc adds Aero DMG Bonus to complete the set hybrid.

**Alternative: Moonlit Clouds (5-pc)**
Sacrifices Iuno's personal damage entirely in exchange for buffing the incoming Resonator via ATK% Outro boost. Best as an early/mid-game setup before Crown of Valor pieces are available in Sanguis Plateaus. Weaker overall once full Crown of Valor is accessible.

**Main Echo:** Lady of the Sea (4-cost Aero)
The best main Echo for Iuno. Provides both Aero DMG Bonus and Resonance Liberation DMG Bonus passively by equipping. Its Echo Skill provides crowd control capabilities in multi-target scenarios. Belongs to the Crown of Valor set.

**Alternative Main Echo:** Impermanence Heron (4-cost Energy Regen)
Used specifically with the Moonlit Clouds 5-pc support build. Enables the set while providing Energy Regen to keep Liberation cycling. Not recommended once Crown of Valor pieces are available.

**Echo Main Stats:**
- 4-cost: CRIT DMG or CRIT Rate
- 3-cost #1: Aero DMG Bonus
- 3-cost #2: Aero DMG Bonus (or ATK% if unavailable)
- 1-cost ×2: ATK%

**Sub-stat Priority:** CRIT Rate > CRIT DMG > Resonance Liberation DMG Bonus > ATK% > Energy Regen > Flat ATK
**Target Ratio:** 70–80% CRIT Rate / 250%+ CRIT DMG / 120–125% Energy Regen

## Iuno: Best Weapon

**Signature — Moongazer's Sigil (5★ Gauntlets)**
Iuno's purpose-built signature. Provides CRIT Rate as its sub-stat. Passive (Plenilune Radiance): ATK +12%; casting Intro Skill or Resonance Liberation increases Resonance Liberation DMG by 20% for 15s; gaining a Shield causes Resonance Liberation DMG to ignore 7.2% of target's DEF for 7s, stacking up to 5 times (once per 0.5s). On Intro Skill cast, immediately reaches max stacks for 3s. Iuno's Waxing Ascent makes the DEF ignore stack to 5 automatically within seconds, giving her near-permanent DEF penetration on all Resonance Liberation DMG.

**Alternative — Verity's Handle (5★ Gauntlets)**
Grants Attribute DMG Bonus (12%) and upon casting Resonance Liberation provides 48% Resonance Liberation DMG Bonus for 8s, extendable up to 3 times via Resonance Skill casts (up to 8+5+5+5 = 23s at max extension). Competitive with the signature in sustained rotations where Resonance Skill is cast frequently within the Liberation window.

**Alternative — Blazing Justice (5★ Gauntlets)**
ATK% sub-stat; grants DEF ignore (8%) and Spectro Frazzle DMG amplification on Basic Attack. The DEF ignore applies broadly to Iuno's kit. Weaker than Verity's Handle but usable.

**Alternative — Tragicomedy (5★ Gauntlets)**
ATK% sub-stat; grants Heavy Attack DMG Bonus (+48%) on Basic Attack or Intro Skill cast. Synergizes with Iuno's ATK scaling and the Heavy Attack DMG Amplification loop, but does not directly benefit her Resonance Liberation DMG ceiling.

**4-Star Options:** Aether Strike, Stonard, Hollow Mirage, Marcato — all viable budget alternatives. Stonard's Resonance Skill passive pairs well with Closing Refrain. Marcato's Concerto Regen on Skill can accelerate rotations.

## Iuno: Best Teams

**S-Tier: Augusta + Iuno + Shorekeeper**
- **Augusta** (Main DPS): builds Majesty via Undying Sunlight Plunge, time-stops via Sublime is the Sun; her continuous Shield generation from Glory's Favor builds Blessing of the Wan Light stacks in Iuno's Full Moon Domain rapidly
- **Iuno** (Sub-DPS/Healer/Buffer): Full Moon Domain + Waxing Ascent enables fast Blessing stack accumulation; Outro provides +50% Heavy Attack DMG Amplification to Augusta for 14s; personal Resonance Liberation DMG contributes meaningfully
- **Shorekeeper** (Support): Universal buff platform; CRIT Rate buff and DMG Amplification accelerate Augusta's Liberation cycling and improve Iuno's own ceiling
*Best overall team. Handles both Tower of Adversity (single-target) and Whimpering Wastes (multi-wave) at high performance.*

**S-Tier: Augusta + Iuno + Qiuyuan**
- **Qiuyuan** (Sub-DPS/Support): When his CRIT Rate reaches 65%, grants the entire team a CRIT DMG bonus; Aero element adds minor amplification synergies; competitive with Shorekeeper in pure single-target content
*Recommended when Shorekeeper is unavailable or when pushing single-target DPS ceilings.*

**A-Tier: Augusta + Iuno + Verina**
- **Verina** (Support/Healer): Consistent healing and ATK% buff via Outro; less buff ceiling than Shorekeeper but high reliability and Concerto Regen support for rotations

**A-Tier: Non-Augusta + Iuno + Support**
- Iuno functions as a capable sub-DPS/healer with non-Heavy Attack DPS units, but her Blessing of the Wan Light stacking requires shield generation from the Main DPS; without Augusta's Glory's Favor, reaching 10 stacks per rotation is unreliable
- Jiyan + Iuno + Support is a community-discussed pairing; Jiyan lacks sufficient self-shielding for Blessing max-stack, making the full buff ceiling inaccessible
- Solo Iuno (Main DPS at S6): viable in lower-difficulty content; S6 resets make Absolute Fullness a primary damage tool; not competitive with dedicated Main DPS units at endgame

## Iuno: DPS Benchmarks

Iuno is rated **SS-Tier** as Sub-DPS in both Tower of Adversity and Whimpering Wastes (Game8, Patch 3.0). Prydwen rates her T0.5/Hybrid in Tower of Adversity and T1/Hybrid in Whimpering Wastes.

**In the Augusta + Iuno team (S0 both, BIS):**
- Full Blessing of the Wan Light (10 stacks) enables 40% all-DMG Amplification on Augusta throughout her Sworn Allegiance window — one of the largest single sustained buffs in the game
- At S2, the buff doubles to 80% all-DMG Amplification — the benchmark against which competing support buffs are measured
- Iuno's personal damage contribution is non-trivial even at S0: her Resonance Liberation (550%) and New Moon burst windows are meaningful secondary damage sources

**Standard Rotation Outline (Augusta team):**
1. Iuno enters via Intro Skill → +40 Sentience, +5 Blessing stacks, enables Closing Refrain
2. Pulse of Origins → Closing Refrain → Lunar Cycle Half Moon activates
3. Flux: Moonbow → New Moon; expend Sentience via Enhanced Moonbow attacks and Arc Beyond the Edge (healing and Concerto acceleration)
4. Absolute Fullness (when Concerto full) → Full Moon Domain conjured; team begins restoring HP and STA; Blessing stacks ramp via Augusta's shield generation inside Domain
5. Outro Skill → Augusta enters with +50% Heavy Attack DMG Amplification; begins Prowess/Ascendancy buildback and Liberation rotation
6. Repeat Liberation cycle; Iuno re-enters via Intro Skill next rotation

## Iuno: Sources
- Prydwen Build Guide — https://www.prydwen.gg/wuthering-waves/characters/iuno/
- Game8 Build Guide — https://game8.co/games/Wuthering-Waves/archives/524889
- Wuthering.gg Character Data — https://wuthering.gg/characters/iuno
- Wuthering Waves Fandom Wiki — https://wutheringwaves.fandom.com/wiki/Iuno
- Genshin-Builds WuWa — https://genshin-builds.com/en/wuthering-waves/characters/iuno/info
