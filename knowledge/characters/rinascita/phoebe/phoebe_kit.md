---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/rinascita_characters/phoebe/phoebe_kit.md
character: Phoebe
group: Order of the Deep / Rinascita
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - spectro
  - rectifier
  - main_dps
  - hybrid
  - spectro_frazzle
  - absolution
  - confession
  - ring_of_mirrors
  - heavy_attack_dps
  - 5star
  - version_2_1
---

# Phoebe Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/phoebe/, https://game8.co/games/Wuthering-Waves/archives/486244, https://wuthering.gg/characters/phoebe, https://wutheringlab.com/character/phoebe-build/, https://www.mistermenplays.com/wutheringwaves/builds/phoebe -->

## Phoebe: Combat Archetype and Role

- **Element/Attribute:** Spectro
- **Weapon Type:** Rectifier
- **Role:** Dual-mode Spectro DPS and Hybrid. Phoebe has two distinct combat states — **Absolution** (Main DPS, Heavy Attack burst focused, enormous per-hit multipliers) and **Confession** (Sub-DPS/Hybrid, Spectro Frazzle applicator and amplifier). Both modes require Spectro Frazzle to be present on enemies and are built around the same core rotation structure, differing in how many Starflash casts she fires and whether her Outro deals damage or applies the "Silent Prayer" debuff buffer.
- **Tier:** DPS — T1 ToA / T2 WhiWa; Hybrid — T1.5 ToA and WhiWa (as of Version 2.6)

## Phoebe: Key Resources (Forte Mechanics Overview)

Phoebe's kit is governed by two stacked forte resources and a persistent environmental structure:

**Prayer (0–120, passive regen):**
Phoebe automatically regenerates 5 Prayer per second, filling to 120 in 24 seconds. When Prayer is full, she can consume all of it to enter either Absolution or Confession via the following activations:
- Hold Basic Attack → **Heavy Attack Absolution Litany** → enters Absolution
- Hold Resonance Skill → **Resonance Skill Utter Confession** → enters Confession

Both activations deal Spectro DMG, apply 1 stack of Spectro Frazzle, grant +12% Spectro DMG Bonus (Inherent 2 — Revelation), and restore 60 Divine Voice.

Prayer is the rotation timer. Every rotation cycle is effectively 24 seconds — the time required for Prayer to refill from empty. All of Phoebe's rotation planning operates on this baseline.

**Divine Voice (0–60):**
Restored to full (60 points) by casting Absolution Litany or Utter Confession. Consumed by Heavy Attack Starflash:
- In Absolution: each Starflash costs 15 Divine Voice → 4 Starflashes per rotation
- In Confession: each Starflash costs 30 Divine Voice → 2 Starflashes per rotation

Starflash can only be activated after Basic Attack Stage 3 or Dodge Counter, making those two inputs the "triggers" that allow the next Heavy Attack to become Starflash.

**Ring of Mirrors (persistent field, 30s duration):**
Summoned by the first press of the Resonance Skill (To Where Light Shines). Stagnates up to 12 targets on initial hit for 2s. Second Skill press teleports Phoebe inside the Ring. The Ring creates two distinct interaction modes:
- **Outside the Ring:** Any Basic Attack or Dodge Counter that hits the Ring refracts Holy Light — dealing Spectro DMG (Basic Attack class) to all targets inside and pulling them toward the center. Triggers every 0.5s.
- **Inside the Ring:** Basic Attack becomes Chamuel's Star (3-hit enhanced chain, all Spectro / Basic Attack class). Dodge Counter becomes Chamuel's Star: Dodge Counter.

The Ring persists for 30s and resets when a new one is summoned. Since Prayer refills in 24s, the Ring's 30s duration comfortably covers one full rotation.

## Phoebe: Absolution vs. Confession — Mode Comparison

| Feature | Absolution Mode | Confession Mode |
|---|---|---|
| **Role** | Main DPS | Sub-DPS / Hybrid buffer |
| **Heavy Attack Starflash** | 15 Divine Voice per cast, **+256% DMG Amplification** when target has Frazzle | 30 Divine Voice per cast, applies **+5 Frazzle stacks** per hit |
| **Starflash casts per rotation** | 4 | 2 |
| **Resonance Liberation enhancement** | **+255% DMG Multiplier** | Applies **8 stacks** of Spectro Frazzle |
| **Outro enhancement** | **+255% DMG Multiplier** (Outro hits deal massive Spectro burst) | Grants **Silent Prayer** to on-field Resonator: –10% Spectro RES on nearby targets + **+100% Spectro Frazzle DMG Amplification** for 30s |
| **Primary value** | Direct damage via empowered Starflash | Frazzle stacking and Frazzle DMG amplification for teammates |
| **Best team role** | Spectro Frazzle hypercarry | Buffer/enabler for Spectro Frazzle Main DPS (e.g., Zani) |

Note: Absolution and Confession cannot coexist — entering one ends the other. When Divine Voice is exhausted, Phoebe does not exit Absolution or Confession. She can continue in mode until she expends all Divine Voice, at which point she can no longer fire Starflash but remains in mode until she manually switches via another Prayer activation.

## Phoebe: Stats Baseline

| Stat | Lv. 1 | Lv. 90 |
|---|---|---|
| HP | ~870 | 10,825 |
| ATK | ~33 | 413 |
| DEF | ~101 | 1,259 |
| Crit. Rate | 5% | 5% |
| Crit. DMG | 150% | 150% |
| Energy Regen | 100% | 100% |
| Max Resonance Energy | 125 | 125 |

*Forte minor nodes add +16% Crit DMG and +12% ATK%. Stats above exclude minor forte bonuses.*

## Phoebe: Ascension Materials

| Material Type | Total Required |
|---|---|
| LF Whisperin Core | ×4 |
| MF Whisperin Core | ×12 |
| HF Whisperin Core | ×12 |
| FF Whisperin Core | ×4 |
| Cleansing Conch (Boss drop — Hecate in Rinascita) | ×46 |
| Firecracker Jewelweed (Local specialty, Rinascita) | ×60 |
| Shell Credits | 170,000 |

*Firecracker Jewelweed is found across Rinascita — use the Prydwen or wuthering.gg Interactive Map to locate them. Cleansing Conch comes from the Hecate weekly boss fight.*

## Phoebe: Character Kit: Basic Attack — O Come Divine Light

**Standard chain (no Ring / outside Ring):** Phoebe performs up to 3 consecutive attacks of Holy Light dealing Spectro DMG. Stage 3 is the key trigger: completing it enables the next Heavy Attack to become Starflash. Under normal conditions, the standard Basic Attack chain is not a primary damage source but rather a Starflash enabler.

**Inside Ring — Chamuel's Star:** Basic Attack becomes a 3-hit enhanced chain (Stages 1–3 all dealing Spectro DMG, Basic Attack class). Significantly higher multipliers than the standard chain. Stage 3 still enables Starflash.

**Heavy Attack:** Standard charged strike (STA cost: 25), dealing Spectro DMG. Mostly used as a fallback — in active modes, Heavy Attack becomes Starflash when Divine Voice is available post-Stage 3 or post-Dodge Counter.

**Mid-air Heavy Attack:** Costs 20 STA to ride the staff for a distance. Can be recast after a mid-air dodge or grapple. Inherent 1 (Presence) allows it to be cast one additional time per use. Used for mobility and positioning.

| Attack | Multiplier (Lv.1) |
|---|---|
| Stage 1 | 14.85% |
| Stage 2 | 11.25% + 13.75% |
| Stage 3 | 7.17% × 8 |
| Heavy Attack | 20.80% × 4 |
| Plunging Attack | 23.25% × 2 |
| Dodge Counter | 10.86% × 8 |
| Chamuel's Star: Dodge Counter | 22.05% × 6 |

## Phoebe: Character Kit: Resonance Skill — To Where Light Shines

**First press — Ring of Mirrors summoning:** Phoebe fires at the target location, dealing Spectro DMG (31.50% × 2 at Lv.1). Targets hit are stagnated for 2s (up to 12 targets). Creates the Ring of Mirrors at the target location for 30s. The stagnation is a significant crowd control tool, reliably locking groups at the start of every rotation.

**Second press — Teleport:** Shortly after summoning, a second Skill press teleports Phoebe to the Ring of Mirrors' center, dealing additional Spectro DMG. This is how she enters the Ring for the Chamuel's Star Basic Attack chain. Cannot teleport if too far from the Ring.

**Ring Interactions:**
- Outside Ring: Basic Attack or Dodge Counter hitting the Ring deals Spectro DMG (Basic class) and pulls targets to center (0.5s trigger cap) — 7.50% × 2 at Lv.1
- Inside Ring: Chamuel's Star replaces Basic Attack (Stage 1: 29.85% / Stage 2: 20.00% × 2 / Stage 3: 14.55% × 6)

| Stat | Value (Lv.1) |
|---|---|
| Skill DMG (initial) | 31.50% × 2 |
| Ring: Refracted Holy Light | 7.50% × 2 |
| Chamuel's Star Stage 1 | 29.85% |
| Chamuel's Star Stage 2 | 20.00% × 2 |
| Chamuel's Star Stage 3 | 14.55% × 6 |
| Cooldown | 12s |

## Phoebe: Character Kit: Resonance Liberation — Dawn of Enlightenment

Phoebe concentrates her light into the Mirror of Enlightenment and smashes it, dealing Spectro DMG.

The Liberation has two distinct enhancement versions based on active mode:
- **Absolution Enhancement:** Increase DMG Multiplier by **+255%** (base 202% → effectively 707% at Lv.1)
- **Confession Enhancement:** Apply **8 stacks** of Spectro Frazzle to all targets hit — the fastest single-cast Frazzle application in the game

Both versions deliver strong value in their respective roles. The Liberation animation can be canceled into other actions to reduce total field time — a key optimization in her rotation.

| Stat | Value (Lv.1) |
|---|---|
| Base Skill DMG | 202.00% |
| Absolution total DMG | ~707% effective (202% + 255% bonus) |
| Confession: Frazzle applied | 8 stacks per cast |
| Cooldown | 25s |
| Resonance Energy Cost | 125 |
| Concerto Regen | 20 |

## Phoebe: Forte Circuit: Radiant Invocation

**Prayer and mode activation:**
Prayer refills passively at 5/s, capping at 120 (24s to full). At full Prayer, hold Basic Attack for Absolution Litany or hold Resonance Skill for Utter Confession. Both consume all 120 Prayer, restore 60 Divine Voice, deal Spectro DMG, apply 1 Frazzle stack, and enter the corresponding mode.

**Heavy Attack Starflash:**
Available after Basic Attack Stage 3 or Dodge Counter when Divine Voice is available. Costs Divine Voice (15 in Absolution; 30 in Confession). Deals Spectro DMG at a high multiplier (41.59% × 3 at Lv.1 base, before mode enhancements).

Enhancements:
- **Absolution:** Starflash gains **+256% DMG Amplification** when target has Spectro Frazzle (the primary damage source in Absolution playstyle). 4 casts per rotation (60 ÷ 15).
- **Confession:** Starflash applies **5 stacks of Spectro Frazzle** per cast. 2 casts per rotation (60 ÷ 30).

| Stat | Value (Lv.1) |
|---|---|
| Absolution Litany DMG | 321.00% |
| Utter Confession DMG | 94.50% |
| Heavy Attack Starflash DMG | 41.59% × 3 |
| Absolution Litany Concerto | 10 |
| Utter Confession Concerto | 40 |

## Phoebe: Inherent Passives

**Presence (Inherent 1):** Mid-air Heavy Attack can be cast one additional time. Purely quality-of-life for mobility and repositioning; no direct damage optimization value in standard rotations.

**Revelation (Inherent 2):** When in Absolution or Confession, Phoebe's Spectro DMG Bonus is increased by **+12%**. This bonus applies throughout the duration of either active mode, effectively meaning Phoebe has +12% Spectro DMG Bonus for most of her field time (as she is nearly always in one mode or the other during combat).

## Phoebe: Intro/Outro Skills

**Intro Skill — Golden Grace:**
Phoebe knocks back nearby targets and deals Spectro DMG (100.00% Lv.1). Generates 10 Concerto. The knockback provides brief crowd control on entry; the primary value is the Concerto generation and the opportunity to immediately enter mode via Prayer timing.

**Outro Skill — Attentive Heart:**
Phoebe deals Spectro DMG equal to **528.41% of ATK** to nearby targets. Two mode-specific enhancements:
- **Absolution Enhancement:** Increase Outro DMG Multiplier by **+255%** (528.41% → effective ~1,376% total Spectro DMG burst)
- **Confession Enhancement:** Grant **Silent Prayer** to the on-field Resonator for 30s. While Silent Prayer is active: nearby target Spectro RES is reduced by **–10%**; the on-field character gains **+100% Spectro Frazzle DMG Amplification**; Spectro Frazzle's damage interval is extended by **+50%** (slower ticking = larger total damage per tick). This effect lasts 30s or until Phoebe switches to Absolution.

Confession Outro is one of the most powerful debuff/amplifier Outros in the game: the 100% Frazzle amplification combined with –10% Spectro RES is a multiplicative boost to all Frazzle damage dealt during its duration.

## Phoebe: Skill Upgrade Materials

| Material | Total (All 6 Skills) |
|---|---|
| LF Whisperin Core | ×25 |
| MF Whisperin Core | ×28 |
| HF Whisperin Core | ×40 |
| FF Whisperin Core | ×57 |
| Lento Helix | ×25 |
| Adagio Helix | ×28 |
| Andante Helix | ×55 |
| Presto Helix | ×67 |
| Sentinel's Dagger (Weekly Boss — Jué, Mt. Firmament) | ×26 |
| Shell Credits | 2,030,000 |

**Skill Priority (Absolution / DPS build):** Forte Circuit (Starflash multiplier and mode activation) > Resonance Liberation (Liberation enhancement) > Intro Skill > Resonance Skill > Normal Attack. The Forte Circuit upgrade is mandatory as it governs the core damage mechanic. Liberation scaling is the second-largest damage window. Normal Attack upgrades provide minor improvements to the Chamuel's Star chain but are lowest priority.

**Skill Priority (Confession / Hybrid build):** Forte Circuit > Resonance Liberation (for Frazzle stack application) > Resonance Skill > Intro > Normal Attack. The Liberation's 8-stack Frazzle application becomes proportionally more important in Confession.

## Phoebe: Resonance Chains (Sequences)

**S1 — Sequence Node 1:**
In Absolution, Resonance Liberation Dawn of Enlightenment increases DMG Multiplier by **480%** instead of 255% — approximately doubling the Liberation's damage output. In Confession, Liberation increases DMG Multiplier by **+90%** AND applies Spectro Frazzle to targets with the maximum stack they can receive (capping stacks instantly). S1 is a strong multiplier upgrade in both modes, with the Absolution bonus being the most straightforwardly impactful: the Liberation goes from a strong burst to an enormous one.

**S2 — Sequence Node 2:**
In Absolution, DMG dealt by Outro Skills to targets with Spectro Frazzle is **Amplified by 120%** — effectively tripling the Outro's already enormous output in Absolution. In Confession, Silent Prayer grants **+120% more DMG Amplification for Spectro Frazzle** (Confession Outro's 100% becomes 220%). The Absolution S2 is the single largest personal DPS upgrade in the chain; the Confession S2 is a major boost to any Frazzle Main DPS Phoebe is enabling.

**S3 — Sequence Node 3:**
In Absolution, the DMG Multiplier of Heavy Attack Starflash is increased by **+91%**. In Confession, the DMG Multiplier of Starflash is increased by **+249%** (dramatically amplifying Confession Phoebe's personal damage contribution during hybrid play). The Confession S3 bonus is surprisingly large and significantly narrows the personal damage gap between Absolution and Confession playstyles.

**S4 — Sequence Node 4:**
When Basic Attack, Chamuel's Star, Dodge Counter, or Chamuel's Star: Dodge Counter hits a target, that target's **Spectro RES is reduced by 10% for 30s**. This is a team-wide debuff that applies almost constantly during Phoebe's field time, stacking with Confession Outro's –10% Spectro RES for a total –20% Spectro RES shred when Confession is active. Valuable for any Spectro team composition regardless of mode. Note from Prydwen: S4's Spectro RES shred performs notably worse when Spectro Rover S6 or other characters with Spectro RES shred are already present (diminishing returns on RES reduction).

**S5 — Sequence Node 5:**
Casting Intro Skill Golden Grace increases Phoebe's Spectro DMG Bonus by **+12% for 15s**. A small unconditional damage upgrade that activates at the start of every rotation. Less impactful than S1–S4 but contributes consistently.

**S6 — Sequence Node 6:**
Targets entering the Ring of Mirrors are stagnated for an **additional 2s** (one additional proc, affects up to 12 targets, once each). When in Absolution or Confession, summoning the Ring of Mirrors via Resonance Skill increases Phoebe's ATK by **+10% for 20s** and triggers an **extra Heavy Attack Starflash** at the Ring of Mirrors' location — this extra Starflash does not consume Divine Voice and is not considered a Heavy Attack cast, making it a free additional hit at full multiplier on every Ring of Mirrors summoning. S6 adds consistent frontloaded damage and ATK amplification at the start of every rotation.

| Sequence | Estimated Relative DPS (Absolution vs S0) |
|---|---|
| S0 | 100% baseline |
| S1 | ~115–120% (Liberation ×480%) |
| S2 | ~150–165% (Outro ×120% amplification — largest single jump) |
| S3 | ~170–180% |
| S4 | –10% Spectro RES (team-wide benefit, less personal DPS) |
| S6 | ~190–205% (free Starflash + ATK per rotation) |

## Phoebe: Recommended Echo Sets

**Primary Build — Eternal Radiance (5-piece):**
Designed specifically for Spectro Frazzle-focused characters and released with Phoebe in Version 2.1. The 5-piece bonus provides: inflicting enemies with Spectro Frazzle increases Crit. Rate by **+20% for 15s**, and attacking enemies with **10 stacks** of Spectro Frazzle grants **+15% Spectro DMG Bonus for 15s**. Both conditions are trivially met by Phoebe in either mode. The +20% Crit Rate bonus means Phoebe needs approximately 30–40% Crit Rate from her own stats to reach the comfortable 70%+ effective Crit Rate (20% from the set + her base builds toward 50%+ prior to the proc), greatly freeing up Echo substats. Best-in-slot in both Absolution and Confession.

**Alternative Set (early game):** Celestial Light (5-piece) — grants +12% Spectro DMG Bonus and +12% from a stacking effect when hitting enemies. Inferior to Eternal Radiance but usable while farming the correct set.

**Main Echo — Mourning Aix (4-cost):**
Summons a Nightmare: Mourning Aix to attack surrounding enemies dealing **273.60% Spectro DMG** (base). Carries the Eternal Radiance sonata effect. Best 4-cost main echo for Phoebe, dealing direct AoE Spectro damage and contributing Frazzle-adjacent Spectro DMG. Use before entering the Ring for synergistic buff timing.

**Cost Pattern:** ④ ③ ③ ① ①

**Stat Priority:**
- 4-cost: Crit Rate or Crit DMG (balance toward 1:2 ratio; Eternal Radiance provides +20% Crit Rate so slight Crit DMG lean at well-geared levels)
- 3-cost: ATK% × 2 (Spectro DMG Bonus is an option if ATK% is already high)
- 1-cost: ATK% × 2
- Substats: Crit Rate ★★★ (until ~50%; then swap to Crit DMG) > Crit DMG ★★★ > ATK% ★★ > Energy Regen ★★ (until ~120%) > Heavy Attack DMG Bonus ★

**Energy Regen target:** ~120%. Phoebe needs just enough ER to reliably cast Liberation every rotation (once per 25s). The Liberation cooldown is longer than her Prayer refill (24s), so she naturally cycles through one Prayer refill before Liberation is ready. In practice, ~115–125% ER covers most team configurations.

## Phoebe: Best Weapon

**Rime-Draped Sprouts (Signature, 5-star Rectifier):**
ATK +500, Crit. Rate +36% (Lv.90 stats). Passive: Dealing DMG to targets with Spectro Frazzle grants **+28% Basic Attack DMG Bonus and +28% Heavy Attack DMG Bonus per stack, up to 3 stacks for 6s** (max +84% each at full stacks). Casting Outro Skill **amplifies Spectro Frazzle DMG on targets around the active Resonator by 60% for 30s** (effects of the same name cannot be stacked). The weapon is exceptionally well designed for Phoebe: the +36% Crit Rate dramatically lowers the substat requirements to hit the effective Crit Rate target when combined with Eternal Radiance's +20%, it directly buffs both her primary damage types (Basic Attack for Chamuel's Star, Heavy Attack for Starflash), and its Outro amplification extends Phoebe's value to teammates. Best-in-slot with a significant margin over all other options.

**Lustrous Razor (5-star alternative):** Strong ATK% substat and Resonance Skill DMG Bonus passive. Notably weaker than Rime-Draped Sprouts for Phoebe but one of the more accessible 5-star Rectifiers.

**Variation (5-star):** Energy Regen mainstat — eases reaching 120% ER target, freeing Echo substats for offense. Solid all-rounder when signature is unavailable.

**Stellar Symphony (5-star):** Primarily a Shorekeeper signature but usable on Phoebe as an ER option.

**Rectifier of Voyager (4-star, BP weapon):** Best accessible 4-star for Absolution Phoebe. Provides ATK% and Crit Rate substat.

**Jinzhou Keeper (4-star):** Energy Regen primary — achieves 120% ER requirement from the weapon alone, freeing all Echo substats for offensive stats. Best F2P option for players without any strong 5-star Rectifier.

## Phoebe: Best Teams

**Team 1 — Absolution Premium:**
**Phoebe** (Main DPS / Absolution) / Spectro Rover (Frazzle applier / Support) / Shorekeeper (Healer / Crit Buffer)

Spectro Rover is Phoebe's mandatory Spectro Frazzle co-applier in Absolution mode. They apply Frazzle stacks rapidly, provide Spectro RES shred at S0 via Forte, heal via Liberation, and slow enemies with their Outro. Shorekeeper provides +12.5% Crit Rate, +25% Crit DMG, +15% Damage Amplification, and team healing. This is the highest-ceiling Absolution Phoebe team and one of the top team compositions available through Version 2.1–2.6. Full rotation: Shorekeeper Liberation → Outro → Spectro Rover Intro → Rover full kit → Rover Outro → Phoebe Intro → Ring of Mirrors → Absolution Litany (mode entry) → Liberation (cancel animation) → Chamuel's Star Stage 3 → Starflash × 4 → Outro (Absolution enhanced, massive burst) → swap.

**Team 2 — Absolution Standard (Budget):**
**Phoebe** (Main DPS / Absolution) / Spectro Rover (Frazzle applier) / Sanhua (Sub-DPS / Basic Attack buffer)

Sanhua's Outro provides +38% Basic Attack DMG Amplification and has an extremely fast rotation (~8–10s), maximizing Phoebe's field time. While Sanhua's buff is slightly less directly impactful than Shorekeeper's Crit buffs on Phoebe (who already heavily amplifies her Heavy Attacks and benefits less from additional Heavy Attack DMG), the extremely short Sanhua field time and F2P accessibility make this the recommended casual team. Spectro Rover on Rejuvenating Glow + Moonlit Clouds variants offers flexibility in the third slot depending on Sanhua/Shorekeeper availability.

**Team 3 — Absolution (Mortefi Variant):**
**Phoebe** (Main DPS / Absolution) / Spectro Rover / Mortefi (Sub-DPS / Heavy Attack buffer)

Mortefi's Outro provides +38% Heavy Attack DMG Amplification, which is the most directly relevant buff type for Starflash. However, his longer field time requirement and the diminishing returns on Heavy ATK DMG (Phoebe already self-amplifies Starflash so heavily) make him slightly inferior to Sanhua in most scenarios. Notable advantage: Mortefi can equip Static Mist for an additional +10% ATK party buff. Contested versus Sanhua but viable and often recommended when the team needs access to Sanhua for a different composition.

**Team 4 — Confession (Zani Dual-DPS):**
**Phoebe** (Confession mode) / Zani (Spectro Frazzle Main DPS) / Spectro Rover or Shorekeeper

With Version 2.3's introduction of Zani — a Main DPS who deals damage proportional to Spectro Frazzle stacks — Phoebe's Confession mode found its dedicated partner. Confession Phoebe provides: Utter Confession (1 Frazzle stack), 2 × Starflash (5 stacks each = 10 stacks), Liberation (8 stacks), and Outro (Silent Prayer: –10% Spectro RES + 100% Frazzle amplification + extended ticking interval). This is the highest-value team for Confession Phoebe as of its inception. S4+ further adds –10% Spectro RES shred from Basic Attack hits.

**Team 5 — Changli Dual-DPS (Alternative DPS):**
**Phoebe** (Absolution) / Spectro Rover (Frazzle support) / Changli (Sub-DPS)

Changli acts as a secondary DPS during Phoebe's Starflash animation for higher total team output in certain encounter types. Less common than the Shorekeeper or Sanhua configurations due to added rotation complexity, but viable in the right hands.

## Phoebe: DPS Benchmarks

Based on community calculation aggregates (Phoebe S0, Rime-Draped Sprouts R1, Eternal Radiance 5-pc, Lv.90 full stats, Spectro Rover + Shorekeeper support, Absolution mode):

| Investment | Notes |
|---|---|
| S0R0 (Jinzhou Keeper) | Functional; approximately 30–35% below S0R1; strong F2P performance |
| S0R1 (Rime-Draped Sprouts R1) | Full S0 benchmark — among highest DPS characters at launch |
| S1R1 | ~115–120% of S0R1 (Liberation multiplier ×480%) |
| S2R1 | ~150–165% of S0R1 (Outro ×120% Frazzle Amplify — largest single jump) |
| S6R1 | ~190–210% of S0R1 (free Starflash + ATK buff per rotation) |

Phoebe at S0 is specifically noted by Prydwen as one of the most F2P-friendly limited 5-star DPS characters in the game: she functions effectively with free weapons, common echo sets, and teams built around the free Spectro Rover, delivering top-tier performance without any investment beyond the character herself.

## Phoebe: Sources

- Prydwen Institute — Phoebe Guide and Build — https://www.prydwen.gg/wuthering-waves/characters/phoebe/
- Game8 — Phoebe Best Builds and Teams — https://game8.co/games/Wuthering-Waves/archives/486244
- wuthering.gg — Phoebe Build and Info — https://wuthering.gg/characters/phoebe
- wutheringlab — Phoebe Build Guide — https://wutheringlab.com/character/phoebe-build/
- MisterMenPlays — Phoebe Build Guide — https://www.mistermenplays.com/wutheringwaves/builds/phoebe
- LDShop — Phoebe Build Guide v2.8 — https://www.ldshop.gg/blog/guide/phoebe-wuthering-waves-build-guide.html
