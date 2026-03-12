---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/ashinohara_characters/chisa/chisa_kit.md
character: Chisa
group: Ashinohara
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - havoc
  - broadblade
  - support
  - negative_status
  - havoc_bane
  - 5star
  - version_2_8
---

# Chisa Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/chisa/, https://game8.co/games/Wuthering-Waves/archives/524880, https://wuthering.gg/characters/chisa, https://wutheringlab.com/character/chisa-build/ -->

## Chisa: Combat Archetype and Role

- **Element/Attribute:** Havoc
- **Weapon Type:** Broadblade
- **Role:** Support / Sub-DPS — Negative Status enabler and flex support. The first unit in Wuthering Waves to utilize the Havoc Bane mechanic, Chisa provides DEF Shred, DEF Ignore, Negative Status stack amplification, team-wide healing, and team-wide shielding, all while dealing respectable personal Havoc damage.
- **Tier / Pull Value:** S-Rank support; SS-Rank in Tower of Adversity (ToA) and Whispering Wastes (WhiWa) endgame modes. Most valuable to players running Spectro Frazzle, Aero Erosion, or Fusion Burst team compositions.

## Chisa: Key Resources (Forte Mechanics Overview)

Chisa's Forte Circuit revolves around two tracked bars:

- **Ring of Chainsaw** (primary bar, 0–100): Charged by Normal Attacks, Resonance Skill hits, casting Resonance Liberation (+40), and casting Intro Skill (+20). When Ring of Chainsaw reaches 100, the Resonance Skill transforms from Eye of Unraveling into **Serrated Loop**, which activates **Chainsaw Mode** — Chisa's primary damage state.
- **Lifethread – Jetstream** (secondary bar, 0–100): Regenerates passively over time; instantly refills to 100 upon defeating a target; also resets to 100 when exiting Chainsaw Mode. Consumed (50 pts) to cast **Lifethread – Glide**, an aerial dash that pulls Unseen Snare–marked enemies.
- **Chainsaw Fever** (in-mode gauge, replaces Lifethread): While in Chainsaw Mode, inactivity rapidly drains this gauge; hitting zero triggers a Burnout State and forces Chisa out of Chainsaw Mode. Dealing damage resets it.

The practical gameplay loop is: generate Ring of Chainsaw via Normal Attacks and Intro/Skill → reach full charge → cast Serrated Loop to enter Chainsaw Mode → use Sawring – Blitz combos and Sawring – Eradication finisher → exit and swap.

## Chisa Forte Circuit: Ring of Chainsaw / Chainsaw Mode

**Unseen Snare** is Chisa's core debuff. She applies it to enemies in four ways: hitting with Resonance Skill, hitting within a window after casting Serrated Loop, hitting with Dodge Counter – Eye of Unraveling: Retraction, or locking on to a target. The mark lasts 30s. While marked, every time a Resonator deals direct damage to the target, Chisa inflicts 1 stack of **Havoc Bane** (max trigger: once per 2s).

**Havoc Bane** stacks reduce the enemy's DEF by 2% per stack, capping at 6 stacks (–12% DEF total). Additionally, through the Forte passive **Thread of Bane**, Chisa and any teammate with the Thread of Bane effect ignores 18% of the affected enemy's DEF when dealing damage to targets marked by Unseen Snare.

**Chainsaw Mode** unlocks:
- **Sawring – Blitz** (3-stage combo, Resonance Liberation DMG): Consumes Ring of Chainsaw on hit. Each 1 pt of Ring consumed by Sawring – Blitz or Chainsaw Mode – Dodge Counter adds 1.30% DMG multiplier to the next Sawring – Eradication (up to 100 pts tracked).
- **Chainsaw Mode – Dodge Counter** (Resonance Liberation DMG): Pressing Normal Attack after a successful dodge in Chainsaw Mode; chains into Sawring – Blitz Stage 3.
- **Sawring – Eradication** (finisher, Resonance Liberation DMG): Triggered by Sawring – Blitz Stage 3 → Falltone chain or by consuming all Ring of Chainsaw. Deals heavy Havoc DMG scaled by Ring consumed; grants shields to all nearby teammates (+30s); ends Chainsaw Mode and Woven Myriad – Convergence.

**Woven Myriad – Convergence** (15s, granted by casting Resonance Liberation): While active, Sawring – Blitz, Chainsaw Mode – Dodge Counter, and Sawring – Eradication all gain +120% DMG multiplier. The bonus multiplier for Sawring – Eradication from Ring consumption gains an additional +120%.

## Chisa: Stats Baseline

| Stat | Lv. 1 | Lv. 90 |
|---|---|---|
| HP | 862 | 10,775 |
| ATK | 35 | 437 |
| DEF | 93 | 1,136 |
| Crit. Rate | 5% | 5% |
| Crit. DMG | 150% | 150% |
| Energy Regen | 100% | 100% |
| Max Resonance Energy | 140 | 140 |

*Stat values do not include Attribute Bonuses from Chisa's Forte Circuit minor nodes.*

## Chisa: Ascension Materials

| Ascension | Boss Material | Local Specialty | Common Material | Credits |
|---|---|---|---|---|
| 1 (→Lv.40) | LF Polygon Core ×4 | Summer Flower ×4 | Abyssal Husk ×4 | 5,000 |
| 2 (→Lv.50) | MF Polygon Core ×4 | Summer Flower ×4 | Abyssal Husk ×8 | 10,000 |
| 3 (→Lv.60) | HF Polygon Core ×4 | Summer Flower ×8 | Abyssal Husk ×4 (HF tier) | 15,000 |
| 4 (→Lv.70) | HF Polygon Core ×8 | Summer Flower ×8 | — | 20,000 |
| 5 (→Lv.80) | FF Polygon Core ×4 | Summer Flower ×4 | — | 30,000 |
| 6 (→Lv.90) | FF Polygon Core ×4 | Summer Flower ×4 | — | 40,000 |
| **Total (approx.)** | **FF Polygon Core ×4, HF ×12, MF ×4, LF ×4** | **Summer Flower ×20** | **Abyssal Husk ×16** | **~80,000** |

*Summer Flower is a local specialty gathered from the Lahai-Roi map. The Prydwen interactive map can assist with locations.*

## Chisa: Character Kit: Basic Attack — Reign of Silence

Chisa performs up to 2 consecutive attacks (Stage 1 and Stage 2), both dealing Havoc DMG. Stage 2 can be immediately followed by **Rending Lunge** (press Normal Attack shortly after), which chains into **Death Snip** on ground or **Hanging Finality** in air.

**Death Snip** is the signature move of the basic chain: Chisa opens her scissors (first hit), and after a brief delay the scissors snap shut (second hit, Resonance Liberation DMG). Pressing Normal Attack during Death Snip adds additional Havoc DMG and can cancel to the immediate snip. Death Snip also **restores HP for all nearby Resonators**.

| Stage | Multiplier (Lv.1) |
|---|---|
| Stage 1 DMG | 8.40% × 2 |
| Stage 2 DMG | 4.80% + 9.60% + 33.60% |
| Death Snip DMG | 15.00% + 7.50% + 52.48% |
| Death Snip Additional DMG | 24.03% |
| Death Snip Healing | 600 + 24.00% ATK |
| Thread Withdrawn DMG | 5.11% × 2 + 23.82% |
| Rending Lunge DMG | 7.61% × 4 + 45.61% |
| Heavy Attack DMG | 18.00% × 2 |
| Mid-air Attack DMG | 37.20% |
| Severed Facet DMG | 22.50% × 2 |
| Hanging Finality DMG | 6.00% + 12.00% × 2 + 30.00% |
| Dodge Counter DMG | 12.00% + 24.00% + 84.00% |
| Eye of Unraveling – Retraction DMG | 90.00% |

## Chisa: Character Kit: Resonance Skill — Fractured Composition

The Resonance Skill has two states:

**Eye of Unraveling** (base state): Stagnates targets and deals Havoc DMG. Leads into Rending Lunge on ground (or in mid-air) when not in Chainsaw Mode. In Chainsaw Mode, leads into Sawring – Blitz Stage 2. Can be cast in mid-air. Cooldown: 12s.

**Serrated Loop** (enhanced state, Ring of Chainsaw at 100): Replaces Eye of Unraveling while on the ground. Stagnates targets, deals Havoc DMG, and **pulls in nearby enemies**. Instantly activates Chainsaw Mode, replaces the Resonance Skill with Eye of Unraveling, and resets its cooldown (via Inherent 1 on kill). Can be held to continuously attack and pull enemies.

| Move | Multiplier (Lv.1) |
|---|---|
| Eye of Unraveling DMG | 18.00% |
| Serrated Loop DMG | 8.78% × 8 |
| Serrated Loop Hold DMG | 3.76% × 16 |

## Chisa: Character Kit: Resonance Liberation — Moment of Nihility

Chisa deals Havoc DMG to nearby enemies and simultaneously **restores HP for all nearby Resonators** in the team. Activating the Liberation grants Chisa **40 Ring of Chainsaw** and sends her into **Woven Myriad – Convergence** for 15s, which dramatically amplifies all Chainsaw Mode damage multipliers.

| Stat | Value (Lv.1) |
|---|---|
| Skill DMG | 480.00% |
| Healing | 1,400 + 56.00% ATK |
| Cooldown | 25s |
| Resonance Cost | 125 |
| Concerto Regen | 20 |

*Note: Death Snip DMG and all Sawring – Blitz / Chainsaw Mode skills are classified as Resonance Liberation DMG.*

## Chisa: Inherent Passives

**Inescapable Fate (Inherent 1):** When any Resonator in the team defeats a target marked by Unseen Snare, the cooldown of Chisa's Resonance Skill Eye of Unraveling is immediately reset. This effect can trigger up to once every 3s. This is critical in multi-wave scenarios for maintaining Unseen Snare coverage without Chisa needing to be on field.

**All Ends Here (Inherent 2):** Casting Intro Skill Reverberance – Return or Resonance Liberation Moment of Nihility grants Chisa **+20% Havoc DMG Bonus** and **+20% Healing Bonus** for 12s. Additionally, when a Resonator in the team with Thread of Bane defeats a target marked by Unseen Snare, Chisa gains **Sight of Unraveling** (lasts 3s). While in Sight of Unraveling, any target damaged by a Resonator with Thread of Bane automatically receives Chisa's Unseen Snare (30s) even while Chisa is off-field. This effectively makes the 18% DEF Ignore from the Outro permanent across multi-wave content.

## Chisa: Intro/Outro Skills

**Intro Skill — Reverberance – Return:**
Chisa attacks the target dealing Havoc DMG. While not in Chainsaw Mode, pressing Normal Attack shortly after allows Basic Attack Stage 2 to follow. While in Chainsaw Mode, leads into Sawring – Blitz Stage 2. Grants **+20 Ring of Chainsaw** and **+10 Concerto Energy** on cast.

| Stat | Value (Lv.1) |
|---|---|
| Skill DMG | 48.00% |
| Concerto Regen | 10 |

**Outro Skill — Unraveling – Law Zero:**
Grants **Resonant Thread of Closure** to all nearby Resonators for 20s. While active: when an attack hits, the maximum stack count of all **Negative Statuses** and **Electro Rage** the target can receive is increased by **+3** for 15s (unstackable). Additionally, inflicting a Negative Status or dealing Negative Status DMG grants any Resonator in the team the **Thread of Bane** effect for 15s — enabling 18% DEF Ignore on Unseen Snare targets.

This Outro is Chisa's primary team-support mechanic: the +3 max stack increase is a substantial buff for Aero Erosion (Ciaccona, Cartethyia), Spectro Frazzle (Phoebe, Zani), and Fusion Burst (Aemeath) teams.

## Chisa: Skill Upgrade Materials

| Material Type | Materials Required |
|---|---|
| Common | LF Polygon Core → MF → HF → FF (escalating quantities) |
| Specialty | Summer Flower |
| Weekly Boss | Abyssal Husk (from relevant endgame boss) |
| Credits | Shell Credits |

*Full per-tier quantities follow the standard 5-star Forte upgrade curve in Wuthering Waves. Prioritize Inherent Skills → Resonance Liberation → Forte Circuit → Normal Attack = Resonance Skill → Intro Skill.*

## Chisa: Resonance Chains (Sequences)

**S1 — Sequence Node 1:**
Chisa becomes **immune to interruption** during Sawring – Blitz, Sawring – Eradication, and Chainsaw Mode – Dodge Counter. Additionally, inflicting Unseen Snare grants: Chisa's ATK is increased by **+30%** for 15s; and deals a fixed **61,803 Havoc DMG** to the target (target HP can only be reduced to 61.80% at most per target; this instance of damage is Basic Attack DMG and is not affected by damage bonuses). This is considered the strongest stopping point for most players: it ensures reliable rotation execution and boosts both personal damage and healing (which scales with ATK).

**S2 — Sequence Node 2:**
Havoc Bane stacks are applied once every **1s** (down from 2s), doubling the DEF Shred ramp speed. The entire team gains a substantial **All-Attribute DMG Bonus** (approximately 50%, per analyst sources), a buff that significantly exceeds similar effects from other endgame supports. Chisa also ignores an additional 10% of enemy DEF. S2 is widely considered Chisa's most impactful support power spike, substantially elevating Negative Status team damage ceilings.

**S3 — Sequence Node 3:**
Resonance Liberation **Moment of Nihility** gains **+100% DMG Bonus**, substantially amplifying Chisa's on-field burst damage and enabling a main DPS playstyle. Her Liberation also provides the bulk of her Havoc Bane scaling in Chainsaw Mode, meaning this sequence strengthens both roles.

**S4 — Sequence Node 4:**
Minor utility upgrade. Provides incremental improvements to Chisa's stats or secondary effects. Considered low priority ("mosquito legs") relative to S1, S2, and S6 investments by most analysts.

**S5 — Sequence Node 5:**
**Lifethread – Jetstream** consumption is reduced by **50%** (from 50 pts to 25 pts per Lifethread – Glide use). This effectively allows up to four consecutive aerial glides, enabling advanced aerial combat and pull chaining. Primarily a mobility/style upgrade rather than a direct damage increase.

**S6 — Sequence Node 6:**
**Cheat-death survival**: During Sawring – Blitz, Sawring – Eradication, and Chainsaw Mode – Dodge Counter, if Chisa would receive a fatal blow she instead survives at 1 HP (no trigger limit). Furthermore, **Unseen Snare becomes Unseen Snare – Finality** with enhanced effects: targets affected by Unseen Snare – Finality take **+30% Amplified DMG from all Negative Statuses** and **+40% increased DMG from Chisa specifically**. S6 transforms Chisa into a high-damage main DPS with elite debuff value. Per Prydwen calculations, S6 Chisa outputs approximately 251.57% of S0 damage (650k+ vs 258k in their benchmark rotation).

| Sequence | Relative DPS (Prydwen Benchmark) |
|---|---|
| S0 | 100.00% (258,433 / 31,136 DPS) |
| S1 | 118.05% (305,068 / 36,755 DPS) |
| S2 | 155.59% (402,080 / 48,443 DPS) |
| S3 | 187.94% (485,706 / 58,518 DPS) |
| S4 | 187.94% (485,706 / 58,518 DPS) |
| S5 | 200.62% (518,473 / 62,466 DPS) |
| S6 | 251.57% (650,146 / 78,330 DPS) |

## Chisa: Recommended Echo Sets

**Primary Build — Thread of Severed Fate (3-piece):**
Best for damage-oriented Chisa. The 3-piece bonus activates on Havoc Bane application, granting **+20% ATK** and **+30% Resonance Liberation DMG Bonus** for 5s. Since Chisa's primary damage (Sawring – Blitz, Sawring – Eradication, Death Snip) is all classified as Resonance Liberation DMG, this directly amplifies her most important hits. Pair with a 2-piece Havoc Eclipse for +10% Havoc DMG.

**Recommended Main Echo:** Reminiscence: Threnodian – Leviathan (4-cost) — provides passive +12% Havoc DMG Bonus and +12% Resonance Liberation DMG Bonus, plus its active summons a Collapsing Horizon dealing 131.04% × 2 Havoc DMG and generating persistent proc damage boosted by Havoc Bane stacks.

**Cost Pattern:** ④ ③ ③ ① ①

**Stat Priority:**
- 4-cost: Crit Rate or Crit DMG
- 3-cost: ATK% or Havoc DMG Bonus
- 1-cost: ATK%
- Substats: CRIT Rate ★★★ > CRIT DMG ★★★ > Energy Regen ★★★ > Resonance Liberation DMG Bonus ★★ > ATK% ★★ > Flat ATK ★

**Support/Healing Build — Rejuvenating Glow (5-piece):**
Trades personal damage to increase team ATK. Best for teams with ATK-scaling DPS (Ciaccona, Phoebe). Not recommended for Cartethyia (scales on HP). Main Echo: Fallacy of No Return (4-cost). Same stat priorities.

## Chisa: Best Weapon

**Kumokiri (Signature, 5-star Broadblade):**
ATK 500 | Crit Rate 36% (Lv. 90). Passive: ATK +24%. Casting Intro Skill or applying Negative Status grants +16% Resonance Liberation DMG Bonus per stack (up to 3 stacks, 15s). At max stacks, when any Resonator in the team applies Negative Status, they gain +48% All-Attribute DMG Bonus for 15s. This last effect makes Kumokiri a team-wide buffer, contributing roughly half of Chisa's total team buffing value on its own.

**Wildfire Mark (5-star alternative):** Provides Resonance Liberation DMG Bonus. Strong alternative but its effect window cannot be extended by Chisa's skill interactions.

**Lustrous Razor (5-star alternative):** Also offers Resonance Liberation DMG Bonus with generally applicable effects.

**4-star options:** Autumntrace (Crit Rate), Waning Redshift, Helios Cleaver, Aureate Zenith (Crit DMG) — all viable due to general stat/effect coverage. For F2P: **Meditations on Mercy** — Chisa activates its passive through Havoc Bane application.

## Chisa: Best Teams

**Team 1 — Aero Erosion (Meta):**
Cartethyia (Main DPS) / Ciaccona (Sub-DPS) / **Chisa** (Support/Healer). Chisa increases the Aero Erosion stack cap by 3 (via Outro), provides DEF Shred via Havoc Bane, and handles healing and shielding that sustains Cartethyia (who consumes her own HP). This frees Rover (Aero) for other teams. Considered the premier team for Chisa at patch 2.8.

**Team 2 — Spectro Frazzle (Meta):**
Phoebe (Main DPS) / support / **Chisa** (Support/Healer). Phoebe applies Spectral Frazzle as a Negative Status and benefits from both Kumokiri's all-DMG buff (she applies Negative Status) and Chisa's DEF Shred. Zani can also slot in as the DPS but does not benefit from Kumokiri's team buff since she deals Spectro Frazzle DMG without applying it directly.

**Team 3 — Fusion Burst:**
Aemeath (Main DPS) / Lynae (Sub-DPS) / **Chisa** (Support). Chisa's Outro raises the Fusion Burst stack cap by 3 and provides DEF Shred. Lynae amplifies All DMG and Resonance Liberation DMG, which Aemeath scales from.

**Team 4 — F2P Friendly:**
Rover (Spectro) (Main DPS) / **Chisa** (Support) / Verina (Healer). Spectro Rover applies Negative Statuses to trigger Chisa's Thread of Bane, and Verina provides additional ATK buffs and healing. Balanced and durable across all content.

**Team 5 — Chisa On-Field:**
**Chisa** (Main DPS) / Danjin or Sanhua (Sub-DPS) / Verina (Healer). At S0 personal damage is lower than dedicated main DPS characters; significantly improved by S3 and S6.

## Chisa: DPS Benchmarks

Benchmarks from Prydwen (Chisa solo-rotation, S0, Kumokiri R1, Thread of Severed Fate 3-pc, Lv.90 stats 500 ATK / 36% CR):

| Investment | Total DMG | DPS |
|---|---|---|
| S0 | 258,433 | 31,136 |
| S1 | 305,068 | 36,755 |
| S2 | 402,080 | 48,443 |
| S3 | 485,706 | 58,518 |
| S6 | 650,146 | 78,330 |

Recommended rotation (from Prydwen): Intro → Basic 2 → Rending Lunge → Death Snip Full (cancel endlag via Liberation) → Liberation → Serrated Loop → Sawring Blitz 2 → Sawring Blitz 3 → Falltone (auto) → Eradication (swap) → Outro.

Rotation duration is approximately 12–15s, similar in cadence to Iuno. Priority swap is after Sawring – Eradication to maximize off-field buff uptime from Outro.

## Chisa: Sources

- Prydwen Institute — Chisa Guide and Build — https://www.prydwen.gg/wuthering-waves/characters/chisa/
- Game8 — Chisa Best Builds and Teams — https://game8.co/games/Wuthering-Waves/archives/524880
- wuthering.gg — Chisa Build and Info — https://wuthering.gg/characters/chisa
- Wutheringlab — Chisa Build — https://wutheringlab.com/character/chisa-build/
- Sportskeeda — Chisa Resonance Chain Guide — https://www.sportskeeda.com/esports/wuthering-waves-chisa-resonance-chain-guide
- LDShop — Chisa Sequences Guide — https://www.ldshop.gg/blog/wuthering-waves/chisa-sequences.html
