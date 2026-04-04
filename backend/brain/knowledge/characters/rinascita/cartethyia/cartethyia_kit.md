---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/ragunna_characters/cartethyia/cartethyia_kit.md
character: Cartethyia
group: Ragunna / Rinascita
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - aero
  - sword
  - dps
  - hp-scaling
  - aero-erosion
  - dual-form
---

# Cartethyia Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/cartethyia/, https://game8.co/games/Wuthering-Waves/archives/507777, https://wutheringlab.com/character/cartethyia-build/, https://wutheringwaves.fandom.com/wiki/Cartethyia -->

## Cartethyia: Combat Archetype and Role
- **Element/Attribute:** Aero
- **Weapon Type:** Sword
- **Role:** Main DPS — dual-form hypercarry dealing massive HP-scaled Aero and Aero Erosion DMG; uniquely capable of both self-applying Aero Erosion debuffs and maximizing Aero Erosion DMG amplification buffs, reducing reliance on dedicated enablers
- **Scaling:** HP (all multipliers scale off Max HP, not ATK — a first in WuWa at her release)
- **Damage Profile:** Aero DMG, Basic Attack DMG, and Aero Erosion DMG in combination; finisher burst via Resonance Liberation — Blade of Howling Squall

## Cartethyia: Key Resources (Forte Mechanics Overview)

Cartethyia's gameplay revolves around two interconnected resource systems across her two forms.

In her **Cartethyia (normal) form**, she generates three distinct **Sword Shadows** through specific attacks: the Sword of Divinity (Basic Attack Stage 4), the Sword of Discord (Heavy Attack or Intro Skill), and the Sword of Virtue (Resonance Skill). Each shadow lingers on the field for up to 20 seconds (max 1 of each). A Mid-air Plunge Attack recalls all active shadows; the recalled combination determines bonus damage type and quantity, and grants her one or more of three special buffs — **Heart of Virtue**, **Mandate of Divinity**, and **Power of Discord**.

In her **Fleurdelys (transformed) form**, she builds **Conviction** (0–120) through all attacks. Reaching 120 Conviction unlocks **Resonance Liberation — Blade of Howling Squall**, her massive finishing nuke. The three buff states carried from the Sword Shadow recall persist into this form and fundamentally alter her Fleurdelys moveset's properties.

## Cartethyia Forte Circuit: Sword Shadows / Conviction

**Sword Shadow Generation (Cartethyia form):**
- Basic Attack Stage 4 → summons **Sword of Divinity's Shadow** (lasts 20s, max 1)
- Heavy Attack → summons **Sword of Discord's Shadow** (lasts 20s, max 1)
- Resonance Skill — Sword to Bear Their Names → summons **Sword of Virtue's Shadow** (lasts 20s, max 1)
- Intro Skill — Sword to Mark Tide's Trace → summons Sword of Discord's Shadow

**Mid-air Plunge (Cartethyia form — recall mechanic):**
- Recalling 0 swords: 2.84% HP
- Recalling 1 sword: 2.84% HP
- Recalling 2 swords: 1.66%×3 HP
- Recalling 3 swords: **5.68%×3 HP** (Aero Erosion DMG — peak recall damage)
- Recalling all 3 grants Heart of Virtue + Mandate of Divinity + Power of Discord simultaneously

**Buff State Effects in Fleurdelys form:**
- **Heart of Virtue:** Basic Attack Stage 4 creates a force field that Stagnates nearby targets; Fleurdelys's interruption resistance increases
- **Mandate of Divinity:** Aero Erosion DMG Amplified by 50% and Aero Erosion tick interval halved for nearby enemies
- **Power of Discord:** Stages 5/Mid-air 2/Enhanced Heavy/May Tempest Break the Tides raise Aero Erosion stacks on all nearby targets to the highest count among targets

**Conviction Generation (Fleurdelys form):**
- All attacks restore Conviction on hit
- At 120 Conviction → Resonance Liberation button replaces to cast Blade of Howling Squall
- Below 120 Conviction → pressing Resonance Liberation swaps back to Cartethyia form (no energy cost)

## Cartethyia: Stats Baseline

| Stat | Lv. 1 | Lv. 20 | Lv. 40 | Lv. 60 | Lv. 80 | Lv. 90 |
|------|-------|--------|--------|--------|--------|--------|
| HP | ~830 | ~2,163 | ~5,665 | ~10,785 | ~18,260 | ~21,735 |
| ATK | ~18 | ~47 | ~123 | ~235 | ~397 | ~473 |
| DEF | ~95 | ~248 | ~649 | ~1,236 | ~2,091 | ~2,490 |
| Crit Rate | 5% | 5% | 5% | 5% | 5% | 5% |
| Crit DMG | 150% | 150% | 150% | 150% | 150% | 150% |
| Energy Regen | 100% | 100% | 100% | 100% | 100% | 100% |

*Note: All damage multipliers scale from Max HP, not ATK. Target ~50,000 HP fully built. HP% is the primary stat bonus at each ascension.*

## Cartethyia: Ascension Materials

| Ascension | Level Cap | Materials |
|-----------|-----------|-----------|
| 1 | 20 → 40 | Bamboo Iris ×4, LF Tidal Residuum ×4, Shell Credits ×5,000 |
| 2 | 40 → 50 | Bamboo Iris ×8, MF Tidal Residuum ×4, Unfading Glory ×2, Shell Credits ×10,000 |
| 3 | 50 → 60 | Bamboo Iris ×12, MF Tidal Residuum ×8, Unfading Glory ×4, Shell Credits ×15,000 |
| 4 | 60 → 70 | Bamboo Iris ×16, HF Tidal Residuum ×4, Unfading Glory ×8, Shell Credits ×20,000 |
| 5 | 70 → 80 | Bamboo Iris ×20, HF Tidal Residuum ×8, Unfading Glory ×12, Shell Credits ×40,000 |
| 6 | 80 → 90 | Bamboo Iris ×24, FF Tidal Residuum ×4, Unfading Glory ×16, Shell Credits ×80,000 |

**Material Sources:**
- **Bamboo Iris:** Gathered in Septimont near Titanbone Expanse and Capitoline Hill; purchasable from Silver Helmet vendor
- **Unfading Glory:** Drops from Lioness of Glory boss (northwest Septimont)
- **Tidal Residuum (LF/MF/HF/FF):** Rinascita Forgery Challenges; Item Exchange for LF/MF tiers via Oscillate Corals

## Cartethyia: Character Kit: Basic Attack — Sword to Carve My Forms

**Basic Attack — Cartethyia (4-hit chain)**

All hits deal Aero DMG (also counted as Aero Erosion DMG):
- Stage 1: 2.41% HP
- Stage 2: 1.98% + 1.98% + 2.64% HP
- Stage 3: 2.15%×4 HP
- Stage 4: 1.27%×3 + 3.80% HP — **inflicts 1 stack of Aero Erosion; summons Sword of Divinity's Shadow**

**Heavy Attack — Cartethyia**
- Deals Aero DMG; counted as Basic Attack DMG
- Multiplier: 1.05%×3 + 3.14% HP
- **Summons Sword of Discord's Shadow**; can be used mid-air; costs 20 STA

**Mid-air Attack — Cartethyia (Plunge)**
- Base plunge: 2.84% HP (Aero Erosion DMG)
- 1 shadow recalled: 2.84% HP
- 2 shadows recalled: 1.66%×3 HP
- 3 shadows recalled: **5.68%×3 HP** (peak)
- Recalling shadows also grants Heart of Virtue / Mandate of Divinity / Power of Discord
- Costs 30 STA

**Dodge Counter — Cartethyia**
- 3.45%×4 HP; Aero DMG

## Cartethyia: Character Kit: Resonance Skill — Sword to Bear Their Names

Cartethyia launches nearby enemies into the air and slams them down, dealing Aero DMG (counted as both **Basic Attack DMG** and **Aero Erosion DMG**), inflicting **2 stacks of Aero Erosion**, and summoning **Sword of Virtue's Shadow**.

- Multiplier: 3.47%×3 + 4.46% HP
- Concerto Regen: 10
- Cooldown: 14s
- Can be used mid-air

This is Cartethyia's primary Aero Erosion applicator and the key activator of the Sword of Virtue Shadow — essential to gathering all 3 swords before a recall plunge.

## Cartethyia: Character Kit: Resonance Liberation — A Knight's Heartfelt Prayers

**Phase 1 — Transformation**
- Consumes **50% of Max HP** (no cost if HP is already below 50%)
- Transforms Cartethyia into **Fleurdelys**, entering **Manifest state** for **12 seconds**
- Grants **+60% Aero DMG Bonus** while in Manifest
- Clears all Conviction on entry; Resonance Energy is NOT cleared
- Concerto Regen on cast: 20; Cooldown: 25s; Resonance Energy Cost: 125

**Phase 2 — Conviction Building (Fleurdelys)**
All Fleurdelys attacks restore Conviction. At 120 Conviction, Resonance Liberation button changes to cast Blade of Howling Squall. Below 120, pressing it swaps back to Cartethyia form (no energy cost).

**Phase 3 — Blade of Howling Squall (Finisher)**
- Removes all Conviction; ends Manifest; **restores 50% Max HP**
- Deals Aero DMG to all targets in a straight-line AoE in front
- On hit: removes all Aero Erosion stacks from the target; **each stack removed Amplifies DMG taken by 20%, up to 5 stacks (100% maximum amplification)**
- Multiplier: 6.60%×7 HP
- Can be cast mid-air

**Avatar Skills (Form Toggle):**
- **Avatar — Cartethyia:** While Fleurdelys and Conviction < 120, press Reso Lib → performs BA Stage 2 as Cartethyia; pauses Manifest timer. Cooldown: 1.5s
- **Avatar — Fleurdelys:** While in Manifest as Cartethyia, press Reso Lib → performs BA Stage 2 as Fleurdelys (no energy cost); resumes Manifest timer

## Cartethyia: Inherent Passives

**A Heart's Truest Wishes**
- Healing received by all non-Cartethyia/Fleurdelys Resonators is increased by **20%**, and their resistance to interruption is enhanced
- If **Rover: Aero** is in the team, Rover: Aero additionally restores **25 Windstrings** upon casting Omega Storm

**Wind's Indelible Imprint**
- Targets with **1–3 stacks** of Aero Erosion take **+30% DMG** from Cartethyia and Fleurdelys
- Targets with **more than 3 stacks** additionally take **+10% DMG** per extra stack (up to 3 additional stacks = maximum +60% total)
- This makes maximizing and maintaining Aero Erosion stacks critical for her damage ceiling

## Cartethyia: Intro/Outro Skills

**Intro Skill — Sword to Mark Tide's Trace (Cartethyia)**
- Dashes to target and strikes, dealing Aero DMG
- **Inflicts 2 stacks of Aero Erosion**; summons **Sword of Discord's Shadow**

**Intro Skill — Sword to Call for Freedom (Fleurdelys)**
- Forward thrust dealing Aero DMG; restores Conviction on hit

**Outro Skill**
- Cartethyia leaves the field, spawning an Aero vortex that continuously deals Aero Erosion DMG for **8 seconds**
- Active characters striking debuffed targets gain a **+17.5% DMG bonus** during this window

## Cartethyia: Skill Upgrade Materials

Skill upgrades require: **Inert / Reactive / Polarized / Heterized Metallic Drip** (Forgery Challenge — Rinascita), **When Irises Bloom** (weekly boss drop from Fleurdelys at Avinoleum, accessible after completing Chapter 2 Act 4), and **Tidal Residuum** (LF/MF/HF/FF) from Rinascita Forgery Challenges.

| Skill Level | Metallic Drip | When Irises Bloom | Tidal Residuum | Shell Credits |
|-------------|--------------|-------------------|----------------|---------------|
| 2 | Inert ×3 | — | LF ×2 | 5,000 |
| 3 | Inert ×5 | — | LF ×4 | 10,000 |
| 4 | Reactive ×4 | — | MF ×3 | 15,000 |
| 5 | Reactive ×6 | — | MF ×5 | 20,000 |
| 6 | Polarized ×5 | When Irises Bloom ×1 | HF ×3 | 30,000 |
| 7 | Polarized ×8 | When Irises Bloom ×1 | HF ×5 | 45,000 |
| 8 | Heterized ×5 | When Irises Bloom ×2 | FF ×3 | 60,000 |
| 9 | Heterized ×8 | When Irises Bloom ×2 | FF ×5 | 75,000 |
| 10 | Heterized ×10 | When Irises Bloom ×3 | FF ×6 | 90,000 |

**Skill Priority:** Resonance Liberation > Resonance Skill > Forte Circuit > Basic Attack > Intro Skill

## Cartethyia: Resonance Chains (Sequences)

**S1**
Max HP increased by 12%. For 15s after casting Intro Skill or Basic Attacks, ignore 8% of the target's DEF when dealing damage. If the target has at least 1 stack of Aero Erosion, DMG taken by the target is Amplified by 20%.
*Value: Solid QoL and damage amplification. Worthwhile for Aero Erosion synergy, but not dramatically transformative.*

**S2**
Upon casting Resonance Liberation, the Aero Erosion stack limit of opponents within range is increased by 3 (above the standard max). Her next attack applies 3 Aero Erosion stacks to all affected targets and triggers additional Aero Erosion DMG. Cartethyia gains increased damage multipliers and her Mid-air Attacks deal 200% additional damage. Resonance Skill cooldown is reduced.
*Value: Game-changing — the single strongest Sequence Node. Dramatically increases mid-air attack burst damage and expands Erosion stack headroom, synergizing with her entire kit.*

**S3**
Fleurdelys's Basic Attack Stage 5, Mid-air Attack Stage 2, Enhanced Heavy Attack, and May Tempest Break the Tides inflict 2 stacks of Aero Erosion on targets. The damage multiplier of Blade of Howling Squall is boosted by 100%.
*Value: Extremely high ceiling impact — doubling the Blade of Howling Squall multiplier is massive in her burst rotation.*

**S4**
After any ally inflicts debuff damage, the entire team gains a 20% DMG bonus for all attributes.
*Value: Strong team-wide multiplicative buff. Benefits all team members, especially in debuff-heavy compositions.*

**S5**
When Cartethyia or Fleurdelys takes a fatal blow, they will not be downed; instead they gain a Shield equal to 20% of Max HP for 10 seconds (once per 10 minutes). The HP cost for casting Resonance Liberation — A Knight's Heartfelt Prayers is reduced to 25% of Max HP.
*Value: Meaningful survivability utility. Reducing the Liberation HP cost from 50% to 25% also improves combat flow.*

**S6**
Cartethyia's Outro Skill, Intro Skills, Resonance Liberation — A Knight's Heartfelt Prayers, and Resonance Liberation — Blade of Howling Squall raise Aero Erosion stacks on targets hit to the maximum count. Blade of Howling Squall no longer removes Aero Erosion stacks on cast. Within 30s after using these skills, when any Resonator inflicts Aero Erosion on a max-stack target, immediately triggers one additional Aero Erosion DMG instance. Targets take 40% more DMG from Fleurdelys.
*Value: S6 enables a perpetual Erosion-stacked state and adds a 40% amplifier for Fleurdelys — transformational for sustained encounter DPS.*

## Cartethyia: Recommended Echo Sets

**Best (with Ciaccona): Windward Pilgrimage — 4-4-1-1-1**
Since Cartethyia scales HP and not ATK, she can run two 4-cost echoes rather than the standard 4-3-3-1-1 configuration. The **Windward Pilgrimage** (Gusts of Welkin) sonata set provides Aero DMG Bonus synergy perfectly suited for her kit. Ciaccona's presence covers the remaining Aero DMG needs.

**Best (without Ciaccona): Windward Pilgrimage — 4-3-1-1-1**
Without Ciaccona, replace the second 4-cost with a 3-cost bearing an **Aero DMG Bonus** main stat to compensate for the missing buff source.

**Main Echo:** Windcleaver (4-cost Aero main echo) — deals 27.36%×8 + 136.80% Aero DMG; grants +10% Aero DMG Bonus passive to equipped character

**Echo Main Stats:**
- 4-cost #1: CRIT Rate or CRIT DMG
- 4-cost #2: CRIT Rate or CRIT DMG (with Ciaccona) / Aero DMG Bonus (without)
- 3-cost (if used): Aero DMG Bonus
- 1-cost ×3: HP% (flat HP from 1-cost echoes scales favorably given her HP-scaling kit)

**Sub-stat Priority:** CRIT Rate > CRIT DMG (maintain ~1:2 ratio) > HP% > Flat HP > Energy Regen
**Target Stats:** ~50,000 HP | 70% CRIT Rate | 270%+ CRIT DMG | 115–120% Energy Regen

## Cartethyia: Best Weapon

**Signature — Defier's Thorn (5★ Sword)**
The only 5-star Sword with an **HP% sub-stat**, purpose-built for Cartethyia's scaling. Provides HP increases, DEF ignore on attacks, and Amplified DMG bonus when targets have Aero Erosion.
- R1: HP +12%; after casting Intro Skill or Basic Attacks, ignores 8% DEF for 15s; targets with 1+ Aero Erosion stack take +20% Amplified DMG
- R5: HP +24%; DEF ignore 16%; +40% Amplified DMG (effectively mandatory for full optimization)

**Alternative — Red Spring (5★ Sword)**
Strong Resonance Skill DMG focus. Viable when Defier's Thorn is unavailable; lacks HP scaling but offers high multipliers.

**Alternative — Unflickering Valor (5★ Sword)**
Increases Basic Attack DMG, which covers a substantial portion of Cartethyia's kit. Competitive option at R1.

**F2P Option — Guardian Sword (4★ Sword)**
The only 4-star Sword carrying HP% as a main stat, making it Cartethyia's sole F2P-accessible weapon that meaningfully contributes to her core scaling.

## Cartethyia: Best Teams

**S-Tier: Cartethyia + Ciaccona + Chisa**
- **Cartethyia** (Main DPS): Core Aero Erosion damage and finisher
- **Ciaccona** (Sub-DPS/Buffer): Maintains Aero Erosion stacks, provides massive Aero Erosion DMG bonus, enables full Aero set
- **Chisa** (Sub-DPS/Support/Healer): Increases max Aero Erosion stack count by 3 (same as Aero Rover), provides DEF Shred via Havoc Bane and Outro, more consistent healing than Aero Rover
*Rotation: Chisa skills → Ciaccona skills + Outro → Cartethyia enters with 5 Aero Erosion stacks, summons all 3 swords, recall plunge, Liberation → Blade of Howling Squall*

**A-Tier: Cartethyia + Ciaccona + Aero Rover**
- **Aero Rover** (Sub-DPS/Support): Increases max Aero Erosion stack limit by 3; restores 25 Windstrings via Cartethyia's inherent passive when casting Omega Storm; provides healing and Aero DMG
*Best in single-target situations where Aero Erosion is easy to maintain at max stacks.*

**A-Tier: Cartethyia + Ciaccona + Shorekeeper**
- **Shorekeeper** (Support): Preferred for multi-wave Whimpering Wastes content where Aero Erosion ramping is unreliable; her buffs and rotation speed compensate
*Best when Erosion uptime is inconsistent.*

**F2P Option: Cartethyia + Sanhua + Baizhi or Verina**
- **Sanhua** rotates in and out at high speed while providing Basic Attack DMG buffing; excellent F2P synergy
- **Baizhi/Verina** provides healing and minor buffs
*Capable of top-tier performance in right hands despite lacking Erosion-synergy support.*

## Cartethyia: DPS Benchmarks

Cartethyia is rated as the **highest-damage single-target DPS in Wuthering Waves** at her full investment ceiling (Prydwen, Patch 3.0 update). Key benchmarks:

- **Optimal team (S6 + Sig + Ciaccona + Chisa S0):** Effectively free-clears 30–50% of end-game content without effort
- **S0 + Signature + BIS team:** Top-tier single-target; competitive with best-in-class unit pairs; slight weakness in AoE multi-wave content (Whimpering Wastes) due to Aero Erosion re-application gaps when entire waves die simultaneously
- **S0 + No Signature (Guardian Sword) + F2P team:** Still top-tier — her baseline kit is strong enough that the F2P team with Sanhua remains viable for high-end content
- **S2 impact:** Mid-air Attack damage increases by 200%, representing the largest single-sequence power spike in her chain

**Rotation Outline (S0, BIS):**
1. Pre-rotation: Apply Aero Erosion stacks via supports (Ciaccona → 5 stacks)
2. Cartethyia enters via Intro Skill (Sword of Discord summoned, 2 Aero Erosion inflicted)
3. Basic Attack Stage 4 (Sword of Divinity) → Resonance Skill (Sword of Virtue) → Heavy Attack if needed → Mid-air Plunge recalling all 3 Swords (5.68%×3 HP Aero Erosion DMG + buff states)
4. Resonance Liberation → Fleurdelys form (60% Aero DMG Bonus active)
5. Full Fleurdelys combo building Conviction to 120
6. Blade of Howling Squall (removes up to 5 Aero Erosion stacks → +100% DMG taken amplification at max)
7. Outro Skill → swap to supports

## Cartethyia: Sources
- Prydwen Build Guide — https://www.prydwen.gg/wuthering-waves/characters/cartethyia/
- Game8 Build Guide — https://game8.co/games/Wuthering-Waves/archives/507777
- WutheringLab Build — https://wutheringlab.com/character/cartethyia-build/
- Wuthering.gg — https://wuthering.gg/characters/cartethyia
- Sportskeeda Resonance Chain Guide — https://www.sportskeeda.com/esports/wuthering-waves-wuwa-cartethyia-resonance-chain-guide
- Game8 Ascension Materials — https://game8.co/games/Wuthering-Waves/archives/524308
- LootBar Build Guide — https://lootbar.gg/blog/en/wuthering-waves-cartethyia-build-guide.html
- Steam Community Build Guide — https://steamcommunity.com/sharedfiles/filedetails/?id=3493689407
