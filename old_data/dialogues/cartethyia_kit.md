# Cartethyia — Kit & Mechanics Knowledge File

<!-- RAG-optimized: each ## section is a standalone searchable chunk -->

## Cartethyia: Combat Archetype and Role
- **Attribute (Element):** Aero
- **Weapon:** Sword
- **Primary Role:** Main Damage Dealer (S-Tier) — premier Aero Erosion DPS in the game
- **Secondary Roles:** Aero Erosion applicator; DMG Amplification for team; Traction (enemy grouping)
- **Scaling:** ALL damage scales off **Max HP** (not ATK) — Cartethyia is the first major HP-scaling DPS in Wuthering Waves
- **Key Resources:**
  - **Aero Erosion** — a stackable debuff (up to 5 stacks base, up to 8 with S2) applied to enemies by many of Cartethyia's attacks; dealt as periodic Aero DMG; consumed by Fleurdelys's key attacks
  - **Sword Shadows** — up to 3 different spectral swords summoned in Cartethyia form: Sword of Divinity's Shadow (from Basic Attack Stage 4), Sword of Discord's Shadow (from Heavy Attack, Intro Skill), Sword of Virtue's Shadow (from Resonance Skill); recalled by Mid-air Plunge Attack; each grants a distinct Manifest buff
  - **Conviction** — a 0–120 resource built by Fleurdelys's attacks during Manifest; reaching 120 unlocks the Resonance Liberation finisher: Blade of Howling Squall
  - **Resonance Energy** — 125 cost to cast the initial transformation Liberation (A Knight's Heartfelt Prayers); free to re-enter Fleurdelys form mid-rotation via Avatar skill

## Cartethyia: Stats Baseline (Exact — from wuthering.wiki RA-X006 data)
All damage scales with HP. Build stats accordingly.

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | 1,184 | 25 | 50 |
| Lv. 20 | 3,079 | 65 | 128 |
| Lv. 20+ (ascended) | 3,868 | 83 | 160 |
| Lv. 40 | 5,864 | 125 | 243 |
| Lv. 40+ | 6,653 | 144 | 128 |
| Lv. 50 | 7,651 | 165 | 316 |
| Lv. 50+ | 8,440 | 184 | 349 |
| Lv. 60 | 9,438 | 205 | 390 |
| Lv. 60+ | 10,227 | 224 | 422 |
| Lv. 70 | 11,225 | 245 | 463 |
| Lv. 70+ | 12,015 | 257 | 496 |
| Lv. 80 | 13,012 | 278 | 537 |
| Lv. 80+ | 13,802 | 291 | 569 |
| Lv. 90 | 14,800 | 312 | 611 |

## Cartethyia: Stats Baseline: Analysis
Cartethyia has the highest HP pool of any Sword character in the game as of Version 2.4, which is by design: every damaging ability she has scales off Max HP, not ATK. Her ATK stat is low by DPS standards (312 at Lv.90) and should be essentially ignored when building. Her DEF is also below average, meaning she relies on her Resonance Liberation's HP-restoration mechanic and the survivability granted by her Inherent Skill (S5 survivability shield) for tankiness.

Target build stats:
- **HP:** Primary — aim for 50,000+ HP with echoes + Signature Weapon
- **Crit Rate / Crit DMG:** Balanced at roughly 70% / 270% (challenging but achievable with proper echo rolls + weapon)
- **Energy Regen:** 115%–120% is sufficient due to 125 Liberation energy cost and natural regen from combat
- **Aero DMG Bonus:** Provided abundantly through Inherent Skills, echo set bonuses, and the Reminiscence: Fleurdelys echo; 3-cost Aero DMG echoes are largely unnecessary

## Cartethyia: Ascension Materials (Total — Level 1 to Level 90)
- **Shell Credits:** 170,000 (ascension) + 2,030,000 (all Forte upgrades) = **2,200,000 total**
- **Unfading Glory** — the unique ascension boss material; obtained from the Fleurdelys weekly boss (Avinoleum region, unlocked via Rinascita main quest)
- **Tidal Residuum** (LF / MF / HF / FF tiers) — Forgery Challenge material (Aero affinity); required in all four rarity tiers for both ascension and Forte upgrades
  - LF: 4 (ascension), 25 (Forte)
  - MF: 12 (ascension), 28 (Forte)
  - HF: 12 (ascension), 40 (Forte)
  - FF: 4 (ascension), 57 (Forte)
- **Bamboo Iris** — world material gathered from Rinascita's Avinoleum area (46 for full ascension)
- **Howling Core** (4-tier enemy drops from Aero Discord enemies) — 60 total for ascension
- **Waveplates** (Common item): 6 → 7 → 6 → 118 across ascension tiers
- **When Irises Bloom** — weekly boss Forte upgrade material; 26 total

## Cartethyia: Basic Attack: Sword to Carve My Forms (Cartethyia Form)
Perform up to 4 consecutive attacks dealing Aero DMG. Following Stage 4, inflicts **1 stack of Aero Erosion** on targets hit and summons **Sword of Divinity's Shadow** (max 1 active, lasts 20s).

**Attribute Scaling (% of Max HP per hit — Aero DMG):**

| Stage | Lv 1 | Lv 2 | Lv 3 | Lv 4 | Lv 5 | Lv 6 | Lv 7 | Lv 8 | Lv 9 | Lv 10 |
|-------|------|------|------|------|------|------|------|------|------|-------|
| Stage 1 | 2.41% | 2.60% | 2.80% | 3.08% | 3.27% | 3.50% | 3.82% | 4.13% | 4.45% | 4.78% |
| Stage 2 | 1.98%+1.98%+2.64% | 2.14%+2.14%+2.86% | 2.31%+2.31%+3.07% | 2.53%+2.53%+3.38% | 2.70%+2.70%+3.59% | 2.88%+2.88%+3.84% | 3.14%+3.14%+4.19% | 3.40%+3.40%+4.53% | 3.66%+3.66%+4.88% | 3.94%+3.94%+5.25% |
| Stage 3 | 2.15%×4 | 2.33%×4 | 2.51%×4 | 2.75%×4 | 2.93%×4 | 3.13%×4 | 3.41%×4 | 3.70%×4 | 3.98%×4 | 4.28%×4 |
| Stage 4 | 1.27%×3+3.80% | 1.37%×3+4.11% | 1.48%×3+4.42% | 1.62%×3+4.85% | 1.73%×3+5.17% | 1.84%×3+5.52% | 2.01%×3+6.02% | 2.18%×3+6.52% | 2.34%×3+7.02% | 2.52%×3+7.54% |
| Dodge Counter | 3.45%×4 | 3.73%×4 | 4.01%×4 | 4.41%×4 | 4.69%×4 | 5.02%×4 | 5.47%×4 | 5.92%×4 | 6.37%×4 | 6.85%×4 |

## Cartethyia: Basic Attack: Heavy Attack and Mid-Air Attack (Cartethyia Form)
**Heavy Attack — Cartethyia:** Consume 20 STA to attack, dealing Aero DMG, summoning **Sword of Discord's Shadow** (max 1, lasts 20s). Counts as Basic Attack DMG. Can be performed in mid-air.

| | Lv 1 | Lv 5 | Lv 10 |
|-|------|------|-------|
| Heavy Attack DMG | 1.05%×3+3.14% | 1.43%×3+4.27% | 2.08%×3+6.24% |
| Mid-air Attack (no sword) | 2.84% | 3.87% | 5.65% |
| Mid-air Attack (1 sword recalled) | 2.84% | 3.87% | 5.65% |
| Mid-air Attack (2 swords recalled) | 1.66%×3 | 2.26%×3 | 3.30%×3 |
| Mid-air Attack (3 swords recalled) | 5.68%×3 | 7.73%×3 | 11.29%×3 |

**Mid-air Plunge Attack mechanics:**
- Recalling all 3 Sword Shadows (3-sword plunge) is the highest-damage variant and the standard rotation target
- Each recalled shadow grants its buff to the subsequent Manifest (Fleurdelys) state
- STA Cost: 30 for mid-air plunge; 20 for heavy attack

## Cartethyia: Resonance Skill: Sword to Bear Their Names (Cartethyia Form)
Attack the target, launch nearby enemies into the air, then plunge them to the ground — dealing Aero DMG and inflicting **2 stacks of Aero Erosion** on targets hit. Counts as Basic Attack DMG. Summons **Sword of Virtue's Shadow** (max 1, lasts 20s). Can be cast in mid-air.
- **Cooldown:** 14 seconds
- **Concerto Regen:** 10 per cast

**Attribute Scaling (% of Max HP):**
| | Lv 1 | Lv 2 | Lv 3 | Lv 4 | Lv 5 | Lv 6 | Lv 7 | Lv 8 | Lv 9 | Lv 10 |
|-|------|------|------|------|------|------|------|------|------|-------|
| Skill DMG | 3.47%×3+4.46% | 3.75%×3+4.83% | 4.04%×3+5.19% | 4.44%×3+5.70% | 4.72%×3+6.07% | 5.05%×3+6.49% | 5.50%×3+7.07% | 5.96%×3+7.66% | 6.41%×3+8.24% | 6.89%×3+8.86% |

## Cartethyia: Resonance Liberation: A Knight's Heartfelt Prayers (Transformation)
**Energy Cost:** 125 | **Cooldown:** 25s | **Concerto Regen on Cast:** 20

By reducing current HP to 50% of Max HP (or no cost if already at/below 50%), Cartethyia transforms into **Fleurdelys**, entering the **Manifest state** for **12 seconds**. On entering Manifest, all Conviction is cleared but Resonance Energy is retained. Manifest grants Fleurdelys a new complete skill set (see Forte Circuit), restoring Conviction with every attack.

While in Manifest with Conviction below 120, pressing Liberation reverts to Cartethyia (no energy cost), executing Basic Attack Stage 2 (or Mid-air in air). From Cartethyia during Manifest, pressing Liberation re-enters Fleurdelys with no energy cost.

**Buff conditions entering Manifest:**
- **Heart of Virtue** (from Sword of Virtue's Shadow recalled): Fleurdelys Stage 4 generates a stasis force field; increased interruption resistance
- **Mandate of Divinity** (from Sword of Divinity's Shadow recalled): Aero Erosion DMG amplified by **+50%**; Aero Erosion tick interval halved (every 1.5s vs 3s)
- **Power of Discord** (from Sword of Discord's Shadow recalled): After key Fleurdelys hits, raises all nearby targets' Aero Erosion stacks to the highest count among them (stack equalization)

All three buffs are removed when Manifest ends. Fleurdelys can **walk on water** and **walk on mid-air** (continuous STA consumption). Reverts to Cartethyia for dialogue, utilities, and grappling hook interactions.

## Cartethyia: Resonance Liberation: Blade of Howling Squall (Finisher — Fleurdelys Form)
Unlocked when Fleurdelys reaches **120 Conviction**. Replaces A Knight's Heartfelt Prayers.
- **Cooldown:** 25s | **Concerto Regen:** 20
- Removes all Conviction, ends Manifest, **restores 50% of Max HP**, and deals Aero DMG in a straight-line AoE in front
- Upon hitting, **removes all Aero Erosion stacks** from the target; each stack removed amplifies DMG taken by **+20%**, up to **5 stacks = +100% DMG multiplier**
- This is the single highest-damage ability in her kit — the rotation is built entirely to maximize this hit

**Attribute Scaling (% of Max HP — 7 hits):**
| | Lv 1 | Lv 2 | Lv 3 | Lv 4 | Lv 5 | Lv 6 | Lv 7 | Lv 8 | Lv 9 | Lv 10 |
|-|------|------|------|------|------|------|------|------|------|-------|
| Blade DMG per hit | 6.60% | 7.14% | 7.68% | 8.44% | 8.98% | 9.61% | 10.47% | 11.34% | 12.20% | 13.12% |
| **Total (×7 hits)** | **46.20%** | **49.98%** | **53.76%** | **59.08%** | **62.86%** | **67.27%** | **73.29%** | **79.38%** | **85.40%** | **91.84%** |

*With 5 stacks of Aero Erosion on target (+100%), the effective total at Lv.10 approaches ~183% of Max HP in a single cast — before Inherent Skill and echo amplifications.*

## Cartethyia: Forte Circuit: Tempest (Fleurdelys Form Skill Set)
When Cartethyia enters Manifest as Fleurdelys, her entire moveset changes. All Fleurdelys attacks restore **Conviction** on hit (max 120 points).

**Basic Attack — Fleurdelys:** 5-hit combo, dealing Aero DMG and restoring Conviction. Stage 5 hits nearly as hard as stages 1–4 combined — do not cancel early.

**Fleurdelys Basic Attack Scaling (% of HP, approximate, Lv 1 → Lv 10):**
| Stage | Lv 1 | Lv 10 |
|-------|------|-------|
| Stage 1 | 3.61% | 7.17% |
| Stage 2 | 2.97%+2.97%+3.96% | 5.90%+5.90%+7.87% |
| Stage 3 | 3.23%×4 | 6.41%×4 |
| Stage 4 | 1.90%×3+5.69% | 3.77%×3+11.31% |
| Stage 5 | ~8.52%×4 (Aero Erosion DMG) | ~16.95%×4 |

**Mid-air Attack — Fleurdelys:** Up to 3 consecutive aerial attacks (STA cost), restoring Conviction. Hold Normal Attack while airborne to go directly to Stage 3. Cast Resonance Skill during aerial sequence to reset the cycle.

**Heavy Attack — Fleurdelys:** Forward thrust dealing Aero DMG; Enhanced version (press Basic during thrust) steps back then surges forward. Restores Conviction.

**Resonance Skill — Sword to Answer Waves' Call (Fleurdelys):** Summons a pull-force field near the target, dealing Aero DMG and restoring Conviction. Follow up with another skill press to cast:

**Resonance Skill — May Tempest Break the Tides (Fleurdelys):** Calls down a giant Sword Shadow to crush an AoE around the target, creating a pull field, dealing Aero DMG to ground targets, restoring Conviction. Follow with Basic Attack to start at Stage 3. Separate cooldown from Cartethyia's Resonance Skill — both can be used in the same rotation window.

**Forte Attribute Scaling (Fleurdelys Stage 5 and Mid-air Stage 2 — key Aero Erosion DMG hits, % HP):**
| | Lv 1 | Lv 10 |
|-|------|-------|
| Stage 5 Aero Erosion hit ×4 | 8.52% each | 16.95% each |
| Mid-air Stage 2 / Enhanced HA | ~17.04% | ~33.87% |

## Cartethyia: Inherent Skill 1: Wind's Indelible Imprint (Passive DMG Bonus)
Targets with **1–3 stacks** of Aero Erosion take **+30% more DMG** from Cartethyia and Fleurdelys (regardless of stack count within range).

For each stack of Aero Erosion **above 3**, targets take an additional **+10% more DMG** from Cartethyia/Fleurdelys per extra stack, up to 3 extra stacks.
- At 4 stacks: +30% + 10% = **+40% total**
- At 5 stacks: +30% + 20% = **+50% total**
- At 6 stacks (S2): +30% + 30% = **+60% total DMG Bonus**

This makes Aero Erosion stack count directly proportional to Cartethyia's damage amplification — synergizing critically with Ciaccona as a stack enabler/maintainer.

## Cartethyia: Inherent Skill 2: Heartwoven Prayer (Team Support Passive)
The healing received by all Resonators **other than Cartethyia/Fleurdelys** in the team is increased by **+20%**, and their **resistance to interruption is enhanced**.

If **Rover: Aero** is in the team, Rover: Aero additionally restores **25 Windstrings** upon casting Omega Storm — a specific synergy bonus enabling stronger Aero support rotations.

## Cartethyia: Intro Skill: Sword to Mark Tide's Trace (Cartethyia) / Sword to Call for Freedom (Fleurdelys)
**Cartethyia — Sword to Mark Tide's Trace:**
- Dashes in and slashes, dealing Aero DMG; inflicts **2 stacks of Aero Erosion** on targets hit
- Summons **Sword of Discord's Shadow** (max 1, lasts 20s)
- Follow with Normal Attack to start Basic Attack Stage 2
- **Concerto Regen:** 10

| | Lv 1 | Lv 5 | Lv 10 |
|-|------|------|-------|
| Mark Tide's Trace DMG | 1.05%×3+3.14% | 1.43%×3+4.27% | 2.08%×3+6.24% |

**Fleurdelys — Sword to Call for Freedom:**
- Thrusts forward to impale, dealing Aero DMG and restoring Conviction
- Follow with Normal Attack to start Basic Attack Fleurdelys Stage 2
- **Concerto Regen:** 10

| | Lv 1 | Lv 5 | Lv 10 |
|-|------|------|-------|
| Call for Freedom DMG | 2.15%+5.02% | 2.93%+6.83% | 4.28%+9.97% |

## Cartethyia: Outro Skill: Wind's Divine Blessing
When Cartethyia/Fleurdelys exits the field, for **20 seconds**:
- Aero DMG dealt by the **active Resonator (non-Cartethyia)** to **targets with Negative Statuses** is **Amplified by 17.5%**
- A "Negative Status" in this context includes Aero Erosion, meaning this buff is nearly always active if Aero Erosion has been applied
- Duration: 20 seconds — long enough to cover a full rotation for most DPS teammates

## Cartethyia: Materials Costs: Forte Skill Upgrade (Total — All Skills to Lv.10)
Per skill upgrade set to Level 10:
- Shell Credits: 280,000 per skill
- Tidal Residuum (all tiers): 5+5+5+9 per skill
- Unfading Glory: 4 per skill
- When Irises Bloom (weekly boss): variable per skill
- Total Shell Credits for all skills: ~2,030,000

## Cartethyia: Resonance Chain Level 1 (S1): The Tower Unseen
Defeating enemies **as Cartethyia or Fleurdelys** while they have Aero Erosion grants **Zeal** (lasts 10s). With Zeal, the next hit by Cartethyia or Fleurdelys transfers the fallen enemy's Aero Erosion stacks to a surviving target.

Additionally: at 30/60/90/120 Conviction, Fleurdelys gains **+25% Crit DMG** per threshold reached (up to **+100% Crit DMG** at 120 Conviction), which is maintained until Blade of Howling Squall is cast.
- **Priority:** High — the Crit DMG scaling with Conviction massively amplifies the finisher's damage

## Cartethyia: Resonance Chain Level 2 (S2): Prisoner Hanged in the Tower (Part 1)
After casting Resonance Liberation — Blade of Howling Squall, **increase the maximum Aero Erosion stack count by 3** (new max: 8 stacks). Cartethyia's or Fleurdelys's next hit **applies 3 Aero Erosion stacks** and immediately triggers Aero Erosion DMG once.

This effectively makes Cartethyia fully independent from Aero Rover as a stack enabler — at S2, she can self-maintain 6–8 stacks of Aero Erosion without external support, dramatically broadening her team options.
- **Priority:** Very High (gamechanging) — also reduces Resonance Skill cooldown by 1s per Sword Shadow recalled

## Cartethyia: Resonance Chain Level 3 (S3): Sword's Lone Journey
The DMG Multipliers of Cartethyia/Fleurdelys's **Basic Attack, Heavy Attack, Dodge Counter, and Intro Skill** are increased by **+50%**. The DMG Multiplier of the **Mid-air Attack** (all Cartethyia forms) is increased by **+200%**.

Following Mid-air Attack — Cartethyia (3-sword plunge), every Sword Shadow recalled reduces the cooldown of Resonance Skill — Cartethyia by **1 second** (up to 3s total reduction).
- **Priority:** High — the +200% Mid-air Attack multiplier is enormous given the 3-sword plunge's already high base damage; S3 significantly amplifies rotation DPS

## Cartethyia: Resonance Chain Level 4 (S4): Sacrifice Made for Salvation
After Resonators in the team inflict any status condition (Havoc Bane, Fusion Burst, Spectro Frazzle, Electro Flare, Glacio Chafe, or **Aero Erosion**), all Resonators in the team gain **+20% DMG Bonus for all Attributes** for **20 seconds**.
- **Priority:** Moderate — universal +20% DMG Bonus benefits every DPS in the team; straightforward and impactful in mixed-element teams

## Cartethyia: Resonance Chain Level 5 (S5): Hope Reshaped in Storms
When Cartethyia or Fleurdelys takes a fatal blow, they are **not downed**; instead, they gain a **Shield equal to 20% of Cartethyia's Max HP** for 10 seconds. (Trigger: once per 10 minutes.)

Additionally, the **HP cost** for casting Resonance Liberation — A Knight's Heartfelt Prayers is **reduced to 25% of Max HP** (down from 50%).
- **Priority:** Moderate — the survival insurance is valuable in high-difficulty content; the HP cost reduction improves sustainability across multiple Liberation casts

## Cartethyia: Resonance Chain Level 6 (S6): Freedom Found in Storm's Wake
After casting Resonance Liberation — Blade of Howling Squall, **raise the Aero Erosion stacks on the target hit to maximum** and Blade of Howling Squall **no longer removes Aero Erosion stacks**.

Within 30 seconds after casting Intro Skill, Resonance Liberation — A Knight's Heartfelt Prayers, or Resonance Liberation — Blade of Howling Squall: when any Resonator inflicts Aero Erosion on a target at maximum stacks, immediately trigger **1 additional instance of Aero Erosion DMG**. **Targets take +40% more DMG from Fleurdelys.**

- **Priority:** Highest — S6 removes the Aero Erosion consumption downside from Blade of Howling Squall (stacks are no longer destroyed), giving the full amplification benefit perpetually. The +40% DMG on targets is a catastrophic damage multiplier. This is considered one of the strongest S6 upgrades in the game.

## Cartethyia: Optimal Rotation Overview (S0 — Standard)
1. Enter via Intro Skill (Cartethyia): applies 2 Aero Erosion, summons Sword of Discord's Shadow → start Basic Attack combo
2. Complete Basic Attack Stages 1–4: Stage 4 applies 1 Aero Erosion, summons Sword of Divinity's Shadow (total: 3 stacks, 2 swords)
3. Cast Resonance Skill: applies 2 more Aero Erosion, summons Sword of Virtue's Shadow (total: 5 stacks, 3 swords)
4. Jump → Mid-air Plunge Attack (3-sword recall): recalls all 3 shadows, activates all 3 Manifest buffs; this is the highest-damage hit in Cartethyia form
5. Cast Resonance Liberation (A Knight's Heartfelt Prayers): transforms to Fleurdelys; reduces HP to 50%; Manifest begins (12s)
6. In Manifest — use Fleurdelys Resonance Skill (Sword to Answer Waves' Call + May Tempest Break the Tides): groups enemies, deals damage, restores Conviction
7. Fleurdelys Basic Attack combo — Stages 1–5 (do not cancel Stage 4/5 early)
8. Fleurdelys Heavy Attack + Enhanced variant
9. Optionally switch to Cartethyia mid-Manifest (Avatar) and re-use Cartethyia Resonance Skill (separate cooldown) before swapping back
10. When Conviction = 120: cast Resonance Liberation Blade of Howling Squall — consumes 5 Aero Erosion stacks (+100% DMG), restores 50% HP, ends Manifest
11. Swap out → Outro Skill (Wind's Divine Blessing) buffs next character with +17.5% Aero DMG Amp

## Cartethyia: Recommended Weapons
- **Defier's Thorn** (5★ Sword, Signature) — massive HP scaling, Crit DMG substat; best-in-slot by significant margin; provides tons of HP and Crit for maximum finisher damage
- **Lustrous Razor** (5★ Sword, standard) — strong HP substat; good fallback for F2P players who saved standard pulls
- **Sword of Night** (4★) — Energy Regen; helps with Liberation uptime at lower investment
- **Commando of Conviction** (4★) — HP scaling with damage bonus on hit; solid budget alternative
- **Emerald of Genesis** (5★) — ATK weapon but provides ER; usable if HP is already high from echoes

## Cartethyia: Recommended Echo Set and Configuration
**Echo Cost Setup: 4-4-1-1-1** (not 4-3-1-1-1)
- Cartethyia does not need Aero DMG Bonus on a 3-cost echo because she gets abundant Aero DMG from her Inherent Skills and the echo set bonus; the 4-4 setup allows two Crit Rate / Crit DMG echoes for maximum damage

**Best Set: Windward Pilgrimage (5-piece)**
- 2-piece: +10% Aero DMG Bonus
- 5-piece: When hitting enemies with Aero Erosion, gain +10% Crit Rate and +30% Aero DMG for 10 seconds
- This set is specifically designed for Cartethyia; it provides near-guaranteed Crit Rate during combat and massive Aero DMG uptime

**Main Echo: Reminiscence: Fleurdelys** (4-cost)
- Active: Summons Windcleaver for multiple Aero damage hits (use before Liberation)
- Passive: +10% Aero DMG Bonus (+20% specifically for Cartethyia or Aero Rover)
- Best activated immediately before entering Manifest

**Alternative Set: Gusts of Welkin (5-piece)**
- Activates when dealing Aero DMG; grants flat Aero DMG bonus; second-best set if Windward Pilgrimage is unavailable

**Main Stats Priority:**
- 4-cost ×2: Crit Rate and Crit DMG (one each)
- 1-cost ×3: HP flat (1-cost echoes are the only source of flat HP, making them uniquely valuable for HP-scaling)

## Cartethyia: Best Team Compositions
**Core Team (Best — Aero Erosion Burst):**
- Cartethyia (Main DPS) + Ciaccona (Aero Sub-DPS / Erosion Maintainer) + Aero Rover (Aero DMG buffer) or Shorekeeper (Healer/Buffer)
- Ciaccona maintains Aero Erosion stacks off-field passively, allowing Fleurdelys to freely consume them without management anxiety

**Alternative Teams:**
- Cartethyia + Sanhua (Basic Attack buffer via Outro) + Shorekeeper (Healer + Crit buffs)
- Cartethyia + Aalto (Aero Sub-DPS) + Shorekeeper
- S2 Cartethyia can replace Aero Rover entirely and maintain her own 6–8 Erosion stacks, greatly expanding flexibility

---

## Cartethyia: Sources
- wuthering.wiki Cartethyia data (exact skill numbers): https://wuthering.wiki/character_1409.html
- Prydwen.gg Cartethyia Build Guide: https://www.prydwen.gg/wuthering-waves/characters/cartethyia/
- Game8.co Cartethyia Best Builds: https://game8.co/games/Wuthering-Waves/archives/507777
- Wutheringlab.com Cartethyia Build: https://wutheringlab.com/character/cartethyia-build/
- Genshin-Builds Cartethyia Guide: https://genshin-builds.com/en/wuthering-waves/characters/cartethyia
- Steam Community Guide — v2.4 Cartethyia: https://steamcommunity.com/sharedfiles/filedetails/?id=3493689407
- Theria Games Cartethyia Guide: https://theriagames.com/guide/wuthering-waves-cartethyia/
- TheGamer Cartethyia Build and Team Guide: https://www.thegamer.com/wuthering-waves-cartethyia-build-team-weapon-echo-strategy-guide/
- LootBar Cartethyia Build Guide: https://lootbar.gg/blog/en/wuthering-waves-cartethyia-build-guide.html
- LDShop Cartethyia Kit Overview: https://www.ldshop.gg/blog/news/wuwa-cartethyia-kit.html
- Wuthering Waves Fandom Wiki: https://wutheringwaves.fandom.com/wiki/Cartethyia
