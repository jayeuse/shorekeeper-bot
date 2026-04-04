---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/jinzhou/changli/changli_kit.md
character: Changli
group: Huanglong / Jinzhou
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - fusion
  - sword
  - main-dps
  - sub-dps
  - swap-cancel
---

# Changli Kit Documentation
<!-- Sources: https://wuthering.wiki/character_1205.html, https://www.prydwen.gg/wuthering-waves/characters/changli/, https://wutheringlab.com/character/changli-build/, https://game8.co/games/Wuthering-Waves/archives/452826, https://game8.co/games/Wuthering-Waves/archives/504464 -->

## Changli: Combat Archetype and Role

- **Element:** Fusion
- **Weapon Type:** Sword
- **Role:** Main DPS or Sub-DPS — dual-threat hybrid
- **Archetype:** Skill-intensive swap-cancel specialist; True Sight state combatant
- **Introduced:** Version 1.1 (second half); second Fusion Main DPS in the game

Changli is Wuthering Waves' highest skill-ceiling character as of her release window. Her kit revolves entirely around entering the **True Sight** state and consuming it via enhanced Basic Attacks (**Conquest** or **Charge**) to build **Enflamement** stacks, which then unlock her primary burst: **Heavy Attack: Flaming Sacrifice**. At baseline she is a capable Main DPS without special optimization, but she rewards swap-canceling — a high-execution technique that chains her True Sight attacks into rapid Concerto Energy generation — with dramatically higher damage output than most characters in the game. Her Outro Skill also provides a potent 20% Fusion DMG + 25% Resonance Liberation DMG buff to the next character, making her equally functional as a high-damage buffer in Double DPS compositions.

## Changli: Key Resources (Forte Mechanics Overview)

Changli's Forte Circuit is centered on two interacting systems: **True Sight** (the temporary combat state that enables her Resonance Skill variant attacks) and **Enflamement** (the stacking resource that gates access to her main damage move). Both systems must be understood together to play her correctly.

- **True Sight** is a 12-second state activated by four different triggers: Resonance Skill, Intro Skill, Ground Basic Attack Stage 4, or Mid-air Attack Stage 4. During True Sight, her Basic Attack inputs convert into special directional dashes — one on the ground (**Conquest**) and one in mid-air (**Charge**). Each grants 1 Enflamement stack when it hits.
- **Enflamement** caps at 4 stacks. Reaching 4 stacks changes her Heavy Attack input into **Flaming Sacrifice**, the highest-damage move in her kit. It can be reached through 4 True Sight attacks across multiple True Sight windows, or instantly via Resonance Liberation.
- **Fiery Feather** is a 10-second buff applied automatically after casting Resonance Liberation — if Changli uses Flaming Sacrifice within that window, she gains +25% ATK.

## Changli Forte Circuit: True Sight & Enflamement

**Entering True Sight**
True Sight lasts 12 seconds and is triggered by any of these:
- Resonance Skill: True Sight: Capture (2 initial charges; 1 charge replenished every 12s)
- Intro Skill: Obedience of Rules (entering the field)
- Ground Basic Attack Stage 4 (completing the 4-hit chain)
- Mid-air Attack Stage 4 (completing the 4-hit aerial chain)

**True Sight Attack Variants**
- **True Sight: Conquest** — Used by pressing Ground Basic Attack while in True Sight; Changli dashes to the enemy dealing Fusion DMG counted as Resonance Skill DMG; grants 1 Enflamement on hit; consumes True Sight
- **True Sight: Charge** — Used by jumping or pressing Basic Attack in mid-air while in True Sight; Changli dashes to the enemy dealing Fusion DMG counted as Resonance Skill DMG; grants 1 Enflamement on hit; consumes True Sight

**Enflamement Stack Acquisition**
- +1 stack: Each True Sight: Conquest hit
- +1 stack: Each True Sight: Charge hit
- +4 stacks (instant full bar): Resonance Liberation: Radiance of Fealty

**At 4 Enflamement Stacks**
- Heavy Attack input becomes **Heavy Attack: Flaming Sacrifice**
- Consuming all 4 stacks, deals Fusion DMG counted as Resonance Skill DMG
- Changli takes 40% reduced DMG while casting it

**Swap-Cancel Mechanic**
Changli's most advanced technique involves swapping off-field immediately after hitting with Conquest or Charge to cut the True Sight state's exit animation, then swapping back to chain another True Sight entry. This creates much faster Enflamement accumulation and dramatically increases Concerto Energy generation per unit of time. This is the primary source of her elite-level DPS ceiling and the main reason Prydwen rates her as having the highest skill factor in the game.

## Changli: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | 831 | 37 | 90 |
| Lv. 20 | 2,161 | 96 | 230 |
| Lv. 40 | 4,116 | 186 | 437 |
| Lv. 60 | 6,624 | 304 | 702 |
| Lv. 80 | 9,133 | 412 | 967 |
| Lv. 90 | 10,387 | 462 | 1,099 |

*Note: Baseline stats exclude Forte Attribute Bonuses and equipment.*

## Changli: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | Crude Ring ×4, Pavo Plum ×4, Shell Credits ×5,000 |
| 2 | 40→50 | Basic Ring ×4, Pavo Plum ×8, Shell Credits ×10,000 |
| 3 | 50→60 | Improved Ring ×8, Pavo Plum ×12, Rage Tacet Core ×4, Shell Credits ×15,000 |
| 4 | 60→70 | Improved Ring ×8, Pavo Plum ×16, Rage Tacet Core ×8, Shell Credits ×20,000 |
| 5 | 70→80 | Tailored Ring ×12, Pavo Plum ×20, Rage Tacet Core ×12, Shell Credits ×40,000 |
| 6 | 80→90 | Tailored Ring ×12, Pavo Plum ×24, Rage Tacet Core ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Rings (Crude/Basic/Improved/Tailored):** Dropped by Exile-type enemies throughout Huanglong; also purchasable at Jinzhou weapon shop or via Synthesizer
- **Pavo Plum:** Gathered from overworld trees primarily in the Luminous Shore area of Mt. Firmament; also purchasable at Jinzhou's Pharmacy
- **Rage Tacet Core:** Dropped by the **Inferno Rider** boss (Sea of Flames, Port City of Guixu, Huanglong)

## Changli: Character Kit: Basic Attack — Blazing Enlightenment

**Ground Attack Chain (4 stages)**
- Stage 1: Two rapid slashes (14.84%×2 Fusion DMG at Lv.1 → 29.49%×2 at Lv.10)
- Stage 2: Two follow-up slashes (17.85%×2 → 35.49%×2)
- Stage 3: Three consecutive strikes (18.34%×3 → 36.45%×3)
- Stage 4: One overhead + four-hit spread (25.50% + 14.88%×4 → 50.70% + 29.58%×4); completing Stage 4 triggers **True Sight** for 12s

**Mid-Air Attack Chain (4 stages)**
- Stages 1–4 mirror the ground chain with slightly adjusted multipliers (Lv.10 peak: Stage 4 at 38.03% + 22.18%×4)
- Completing Stage 4 in the air also triggers **True Sight**

**Heavy Attack:** Upward strike consuming 25 Stamina (14.58%×3 + 18.75% → 28.99%×3 + 37.27%)
**Mid-air Heavy Attack:** Plunge consuming 30 Stamina (62.00% → 123.27%)
**Dodge Counter:** Three-hit counter after successful Dodge (41.57%×3 → 82.64%×3)

## Changli: Character Kit: Resonance Skill — Tripartite Flames

Changli's Resonance Skill has three variants under the Tripartite Flames umbrella, all of which involve entering or using True Sight.

**True Sight: Capture (Primary Resonance Skill)**
- Changli dashes toward the enemy, releasing a 3-hit strike followed by a plunging finisher (Lv.1: 41.19%×3 + 82.37%; Lv.10: 81.88%×3 + 163.76%)
- On cast: enters True Sight for 12s
- Has **2 initial charges**; maximum 2 charges held; 1 charge replenished every 12s
- Generates 14 Concerto Energy on cast
- Can be cast mid-air

**Basic Attack: True Sight — Conquest (Ground True Sight Attack)**
- While in True Sight: pressing Ground Basic Attack triggers Conquest, a dash dealing Fusion DMG counted as Resonance Skill DMG
- Lv.10 multiplier: 58.95%×2 + 82.52% + 94.31%
- Grants 1 Enflamement on hit; consumes True Sight
- Generates 7 Concerto Energy per use

**Basic Attack: True Sight — Charge (Aerial True Sight Attack)**
- While in True Sight: jumping or pressing aerial Basic Attack triggers Charge, a dash dealing Fusion DMG counted as Resonance Skill DMG
- Lv.10 multiplier: 72.68% + 109.02%
- Grants 1 Enflamement on hit; consumes True Sight
- Generates 6 Concerto Energy per use

## Changli: Character Kit: Resonance Liberation — Radiance of Fealty

- **Base Multiplier:** 610.00% Fusion DMG at Lv.1; 1,212.75% at Lv.10 — one of the highest Liberation multipliers in the game
- **Effect on Cast:** Deals Fusion DMG to nearby targets; instantly grants **4 stacks of Enflamement** (full Forte bar); enters **Fiery Feather** state
- **Fiery Feather:** Buff lasting 10s after Liberation — if Changli uses Flaming Sacrifice within this window, her ATK is increased by **+25%**
- **Cooldown:** 20 seconds
- **Resonance Cost:** 125 Energy
- **Concerto Generation:** 20 points per cast
- Can be cast mid-air

The Liberation is one of the fastest paths to Flaming Sacrifice — cast Liberation → immediately use Heavy Attack → Flaming Sacrifice hits with the full Fiery Feather ATK buff active.

## Changli: Character Kit: Heavy Attack — Flaming Sacrifice (Forte Ability)

**Flaming Sacrifice** is the conditional Heavy Attack unlocked at 4 Enflamement stacks and is Changli's primary damage source.

- Consumes all 4 Enflamement stacks to deal a powerful Fusion DMG attack, counted as Resonance Skill DMG
- While casting: Changli takes **40% reduced DMG** (important for survivability in timed content)
- Is the final move in her standard rotation after building stacks via True Sight attacks or Liberation

Approximate Lv.10 multiplier for Flaming Sacrifice: approximately 380–450% Fusion DMG (treated as Resonance Skill DMG for buff purposes)

## Changli: Inherent Passives

**Inherent Skill 1 — Secret Strategist**
- When Changli uses True Sight: Conquest or True Sight: Charge, for each current stack of Enflamement she holds, her Fusion DMG Bonus is increased by **+5%** (up to +20% at 3 pre-existing stacks when the 4th is being earned)
- Encourages building stacks deliberately — the later True Sight attacks in a sequence deal progressively more Fusion DMG

**Inherent Skill 2 — Sweeping Force**
- When Changli uses Heavy Attack: Flaming Sacrifice or Resonance Liberation: Radiance of Fealty, she gains **+20% Fusion DMG Bonus** and ignores **15% of the target's DEF**
- Both effects apply to the triggering move itself
- The DEF ignore extends to her Liberation as well, making both of her biggest damage moves hit harder against armored targets

## Changli: Intro/Outro Skills

**Intro Skill — Obedience of Rules**
- Triggered when Changli enters the field via swap
- Changli appears mid-air, attacks the target, and enters **True Sight** for 12s
- This means every rotation that starts with a swap onto Changli immediately gives her a True Sight window — no Basic Attack Stage 4 buildup needed on entry
- Enables faster Enflamement accumulation in high-turnover rotations

**Outro Skill — Strategy of Duality**
- Triggered when Changli swaps off-field (Concerto Energy full or Unison)
- The incoming Resonator receives:
  - **+20% Fusion DMG Amplification** for 10 seconds (or until they swap out)
  - **+25% Resonance Liberation DMG Amplification** for 10 seconds (or until they swap out)
- This is one of the strongest Outro buffs in Version 1.x — it both amplifies Fusion DMG generally and specifically rewards Liberation-heavy characters following Changli in rotation
- Makes Changli exceptional as a first-slot unit in Double DPS rotations feeding into Fusion or Liberation-focused partners

## Changli: Skill Upgrade Materials

| Skill Level | Key Materials |
|-------------|---------------|
| 1→2 | Metallic Drip (Inert) ×4, Crude Ring ×2, Shell Credits ×1,000 |
| 2→3 | Metallic Drip (Reactive) ×4, Basic Ring ×4, Shell Credits ×3,000 |
| 3→4 | Metallic Drip (Polarized) ×8, Improved Ring ×8, Shell Credits ×8,000 |
| 4→5 | Metallic Drip (Heterized) ×4, Sentinel's Dagger ×2, Tailored Ring ×12, Shell Credits ×20,000 |
| 5→6 | Metallic Drip (Heterized) ×4, Sentinel's Dagger ×3, Tailored Ring ×16, Shell Credits ×40,000 |
| 6→7 | Metallic Drip (Heterized) ×8, Sentinel's Dagger ×5, Tailored Ring ×20, Shell Credits ×80,000 |
| 7→8 | Metallic Drip (Heterized) ×8, Sentinel's Dagger ×8, Tailored Ring ×24, Shell Credits ×120,000 |
| 8→9 | Metallic Drip (Heterized) ×16, Sentinel's Dagger ×12, Tailored Ring ×28, Shell Credits ×160,000 |
| 9→10 | Metallic Drip (Heterized) ×16, Sentinel's Dagger ×16, Tailored Ring ×40, Shell Credits ×200,000 |

**Total Forte Shell Credits (all skills):** ~2,030,000
- **Metallic Drip:** Sword Forgery Challenge rewards (Huanglong Forgery recommended)
- **Sentinel's Dagger:** Weekly boss drop from **Jué** (Mt. Firmament; accessible after Chapter 1 Act 7)
- **Rings:** Exile-type enemies in Huanglong; weapon shop in Jinzhou; Synthesizer

**Forte Leveling Priority:** Resonance Skill = Resonance Liberation > Basic Attack

## Changli: Resonance Chains (Sequences)

**S1 — Hidden Thoughts**
- Resonance Skill: True Sight: Capture and Heavy Attack: Flaming Sacrifice increase Changli's DMG dealt by **+10%** and her resistance to interruption while casting
- *Impact:* Modest personal damage boost (~4–6% overall DPS); the interruption resistance is meaningful in tougher content where Flaming Sacrifice would otherwise be interrupted. A decent but unexciting first sequence.

**S2 — Unfettered Will**
- Each stack of Enflamement increases Changli's **CRIT DMG by +30%** for 8s (stacks are updated on each gain; up to 4 stacks = +120% CRIT DMG)
- *Impact:* One of the strongest S2 upgrades in Version 1.x; +120% CRIT DMG at full Enflamement is enormous and compounds with her base CRIT DMG. Approximately +17–25% overall DPS increase. Very high pull priority.

**S3 — Vermillion's Wrath**
- After casting Liberation: Radiance of Fealty, all team members' ATK is increased by **+20% for 30s**
- *Impact:* A team-wide ATK buff that benefits the full party for most of the rotation cycle (30s covers most standard team rotations). Best sequence for teams where teammates also scale heavily on ATK. Approximately +10–15% team DPS depending on composition.

**S4 — Illuminated Strategy**
- Liberation: Radiance of Fealty DMG is increased by **+80%**
- *Impact:* The Liberation at Lv.10 deals 1,212.75% Fusion DMG — an additional +80% multiplier on that base is substantial. Approximately +8–12% personal DPS increase. Also the most cinematically impactful sequence from a visual standpoint.

**S5 — Fiery Feather's Vow**
- Heavy Attack: Flaming Sacrifice Multiplier increased by **+50%**; when Flaming Sacrifice is cast, Changli's ATK is additionally increased by **+50%**
- *Impact:* Massive amplification to Changli's core move. Both the multiplier increase and the ATK buff stack. Approximately +20–28% personal DPS increase. One of the best S5 sequences in the game at her release.

**S6 — Eternal Blaze**
- Resonance Skill: True Sight: Capture, Heavy Attack: Flaming Sacrifice, and Resonance Liberation: Radiance of Fealty each ignore an additional **40% of the target's DEF** when dealing damage
- *Impact:* Approximately +38% overall DPS. DEF shred is multiplicatively very powerful against high-DEF enemies and in endgame content. Full S6 Changli is among the highest-damage characters in the game.

**Sequence Pull Priority:** S0 baseline is strong; S2 is the standout individual upgrade (CRIT DMG at Enflamement); S5 is excellent for personal DPS; S6 for absolute maximum. S3 is optimal for team-wide compositions.

## Changli: Recommended Echo Sets

**Best-in-Slot: Molten Rift (5-piece)**
- The standard best-in-slot set for Changli; provides Fusion DMG Bonus that scales with her already-high Resonance Skill multipliers
- The full 5-piece bonus is straightforward and reliable — no conditional activation requirements
- **Main Echo:** Inferno Rider — generates significant Resonance Energy (accelerating Liberation availability), provides ATK and Fusion DMG Bonus in combat; also grants a minor movement speed boost in overworld

**Echo Main Stats Priority**
- 4-Cost Echo (Inferno Rider): CRIT Rate or CRIT DMG (whichever completes the 1:2 ratio); CRIT Rate preferred if using signature weapon (which provides CRIT Rate as weapon stat)
- 3-Cost Echoes (×2): Fusion DMG Bonus (primary) or ATK% (close secondary); double Fusion DMG Bonus recommended for non-signature weapon builds; the difference between double Fusion and Fusion+ATK% is marginal — prioritize sub-stat quality
- 1-Cost Echoes: ATK% or HP (sub-stats matter more than mains here)

**Alternative Set: Moonlit Clouds**
- Used when running Changli in a Sub-DPS or buffer role rather than Main DPS
- Moonlit Clouds' Outro-focused buff synergizes with her role of feeding damage buffs to the next character
- Choose between Molten Rift and Moonlit Clouds based on whether Changli is the primary carry or a damage amplifier

**Sub-Stat Priority:** Energy Regen (to 20% breakpoint) ≥ CRIT Rate = CRIT DMG > ATK% > Flat ATK = Resonance Skill DMG Bonus

## Changli: Best Weapon

**Signature — Blazing Brilliance (5-Star Sword)**
- Purpose-built for Changli; best-in-slot by a meaningful margin
- Stat: CRIT Rate (highly efficient for her build; reduces need for CRIT Rate on Echo main stats)
- Effect: Stacking ATK and Fusion DMG Bonus buffs tied to her Resonance Skill usage — directly amplifying True Sight attacks and Flaming Sacrifice
- Also broadly usable on any damage-focused Sword character with significant Resonance Skill contribution

**Top 4-Star Alternatives**
- **Commando of Conviction:** Strong Resonance Skill DMG Bonus scaling; accessible; solid choice without the signature
- **Hollow Mirage:** ATK% sub-stat weapon with a useful passive; competitive with limited investment
- **Standard 5-Star Sword (Emerald of Genesis or similar):** ATK stat + ATK bonus passive; recommended if pulling on standard banner

**F2P Best — Sword of Night**
- Craftable via Jinzhou's weapon shop; provides ATK% boost without complex conditions
- Straightforward and reliable; the best option for early game without any premium investment

## Changli: Best Teams

**Premium Main DPS — Changli / Zhezhi / Shorekeeper**
- **Changli** (Main DPS): On-field True Sight combatant; Liberation into Flaming Sacrifice burst
- **Zhezhi** (Sub DPS/Buffer): Resonance Skill buffs Resonance Skill DMG for the next character, directly buffing Flaming Sacrifice; Coordinated Attacks provide passive damage; Outro provides Resonance Skill DMG Amplification
- **Shorekeeper** (Support): CRIT Rate and CRIT DMG team buffs via Stellarealm; healing; best-in-slot support for almost any DPS character
- *Rotation:* Shorekeeper Liberation → Zhezhi rotation + Outro → Changli Intro (True Sight) → True Sight: Capture ×2 → Conquest/Charge cycles → Liberation + Flaming Sacrifice burst

**Mono Fusion — Changli / Encore / Verina (or Baizhi)**
- **Changli** (Main DPS or Sub-DPS feed): True Sight combatant with Outro feeding Encore
- **Encore** (Main DPS): Benefits directly from Changli's +20% Fusion DMG + 25% Liberation DMG Outro buff; her Liberation is a major damage source that benefits from both buff components
- **Verina / Baizhi** (Support/Healer): Verina provides team ATK buff and healing; Baizhi is the F2P alternative

**Double DPS with Brant — Changli / Brant / Shorekeeper**
- **Changli** (Sub-DPS / Buffer): Fires Liberation, builds Enflamement, delivers Flaming Sacrifice, then swaps to feed Brant with Outro buff
- **Brant** (Main DPS): A damage dealer with Fusion synergy who directly benefits from Changli's Outro; Fusion DMG amplification compounds with Brant's own kit
- **Shorekeeper** (Support): Universal best-in-slot support
- *Note:* Changli's Outro is extremely valuable in this configuration since Brant can exploit both the Fusion DMG and Liberation DMG Amplification

**Budget — Changli / Chixia / Baizhi**
- **Chixia:** F2P-accessible Fusion DPS who also benefits from Changli's Outro buff; her Liberation contributes meaningfully
- **Baizhi:** Best F2P healer/support; provides team healing and ATK buffs

## Changli: DPS Benchmarks

- Changli is rated by Prydwen as one of the highest skill-ceiling characters in the entire game — at optimal play (full swap-cancel technique), she is among the top DPS performers regardless of version
- At S0 with signature weapon and standard play (no swap-cancel), she is a comfortable Main DPS capable of clearing all endgame content
- At S0 with swap-cancel mastery, she significantly outperforms her own baseline; Prydwen characterizes her as potentially far ahead of most competition when played optimally
- Her Liberation multiplier (1,212.75% at Lv.10) is one of the highest single-hit multipliers in the game, making Liberation windows visually and numerically spectacular
- **Primary limitation:** Skill-intensive. Players who cannot or do not wish to execute swap-cancel chains will see her perform adequately but not at the ceiling her kit theoretically enables
- At S6, the combination of S5 Flaming Sacrifice amplification and S6 40% DEF shred on all three major abilities creates one of the most powerful personal DPS profiles in Wuthering Waves 1.x

## Changli: Sources

- Wuthering.wiki — Changli data page (stats, multipliers): https://wuthering.wiki/character_1205.html
- Prydwen Institute — Changli build guide and DPS analysis: https://www.prydwen.gg/wuthering-waves/characters/changli/
- Wutheringlab — Changli build, sequences, Forte mechanics: https://wutheringlab.com/character/changli-build/
- Game8 — Changli builds, teams, ascension materials: https://game8.co/games/Wuthering-Waves/archives/452826
- Game8 — Changli ascension and Forte material farming: https://game8.co/games/Wuthering-Waves/archives/504464
- Pocket Tactics — Changli build guide: https://www.pockettactics.com/wuthering-waves/changli
- Clutchpoints — Changli kit and resonance chain breakdown: https://clutchpoints.com/gaming/changli-kit-skills-resonance-chains-more-in-wuthering-waves
- Charlie INTEL — Changli kit and materials: https://www.charlieintel.com/games/wuthering-waves-changli-kit-materials-build-326638/
