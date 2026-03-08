---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/black_shores/chisa/chisa_kit.md
character: Chisa
group: Black Shores
document_type: character_kit
importance: high
tags:
- character
- kit
- combat
---

# Chisa Kit & Mechanics Knowledge File
<!-- RAG-formatted knowledge file. Each ## heading = one retrievable chunk. -->

## Chisa: Combat Archetype and Role
- **Element/Attribute:** Havoc
- **Weapon Type:** Broadblade (scissors-form that transforms into a chainsaw)
- **Role:** Support (primary role) — provides team-wide DEF reduction, Havoc Bane stacking, healing, Shield generation, AoE grouping, and Resonance Skill Cooldown reset utility. Also deals meaningful personal Havoc DMG in the 3rd-slot teammate position
- **Scaling Stat:** ATK (standard ATK scaling; Minor Fortes grant +8% CRIT Rate and +12% ATK%)
- **Damage Type:** Havoc DMG; most major damage skills are classified as **Resonance Liberation DMG** (Sawring - Blitz, Chainsaw Mode - Dodge Counter, Sawring - Eradication, Death Snip)
- **Combat Style:** Two-phase: out-of-Chainsaw-Mode normal phase (builds Ring of Chainsaw via Basic Attacks and Skill; applies Unseen Snare mark for DEF ignore) → enters Chainsaw Mode via Serrated Loop → unleashes Sawring combo chains for burst damage while maintaining DEF shred and buff application; exits Chainsaw Mode via Sawring - Eradication
- **Specialty:** The definitive Havoc Bane support — stacks Havoc Bane on marked enemies, provides 18% DEF ignore via Thread of Bane, heals the team at multiple points in rotation, generates team-wide Shield on Sawring - Eradication, applies grouping via Serrated Loop and Lifethread - Glide
- **Tier (Prydwen, Patch 2.8):** T0.5 Tower of Adversity (with signature); T1.5 Whimpering Wastes
- **Best use case:** Third slot in Cartethyia / Ciaccona / Chisa — described by Prydwen as the best ToA team in the game (Patch 2.8 onward, with Chisa signature)

## Chisa: Key Resources (Forte Mechanics Overview)
Chisa's Forte Circuit operates on two parallel gauges: Ring of Chainsaw and Lifethread - Jetstream.

**Ring of Chainsaw (max 100 points):**
- Restored by: hitting targets with Normal Attacks and Resonance Skill Eye of Unraveling; +40 from Resonance Liberation; +20 from Intro Skill
- When Ring of Chainsaw is full (100 points), Resonance Skill changes from Eye of Unraveling to **Serrated Loop** — entering Chainsaw Mode
- In Chainsaw Mode: unlocks Sawring - Blitz (3-stage combo), Chainsaw Mode - Dodge Counter, and Sawring - Eradication
- Sawring - Blitz and Chainsaw Mode - Dodge Counter consume Ring of Chainsaw on hit
- Each point of Ring of Chainsaw consumed increases Sawring - Eradication's DMG by 1.30% (up to 100 points counted) — making full Ring consumption before Eradication critical for maximum burst
- Casting Sawring - Eradication: consumes all Ring of Chainsaw, grants team Shield (2000 + 80% ATK), generates 45 Concerto Energy, and exits Chainsaw Mode

**Lifethread - Jetstream (max 100 points):**
- Restored continuously over time (passive); restored to max on exiting Chainsaw Mode; gains 100 points instantly on defeating a target
- At more than 10 points: can consume 50 points to cast **Lifethread - Glide** — an aerial movement/grouping skill; pulls in nearby enemies marked by Unseen Snare
- Allows Chisa to maintain mobility and grouping between Chainsaw Mode windows

**Chainsaw Fever:**
- Active only during Chainsaw Mode; begins at 100% by default
- If Chisa goes too long without dealing damage, Chainsaw Fever rapidly depletes → Burnout State → exits Chainsaw Mode
- Reset by: dealing damage, casting Ultimate, casting Intro Skill, casting Sawring - Blitz Stage 3: Falltone
- In Burnout State: Ring of Chainsaw rapidly depletes until 0 → exits Burnout State; exited by dealing damage, casting Ultimate, or Intro Skill

**Unseen Snare (core support mechanic):**
- Applied to targets by: Resonance Skill hit, post-Serrated Loop window, Dodge Counter - Eye of Unraveling: Retraction, or by locking onto a target
- Duration: 30 seconds; lasts through rotations
- Effect: when marked targets take direct damage from any Resonator, Chisa inflicts 1 stack of Havoc Bane (once per 2 seconds; 1 second at S4)
- **Thread of Bane (18% DEF ignore):** while dealing damage to Unseen Snare targets, ignore 18% of their DEF — this applies to ALL Resonators dealing damage to the marked target

## Chisa: Stats Baseline: Level 1 – 90
All values are base stats (without Minor Fortes or Echo bonuses):

| Level | HP     | ATK  | DEF   |
|-------|--------|------|-------|
| 1     | ~1,248 | ~50  | ~131  |
| 10    | ~2,705 | ~109 | ~285  |
| 20    | ~4,186 | ~169 | ~441  |
| 30    | ~5,486 | ~222 | ~578  |
| 40    | ~6,787 | ~275 | ~715  |
| 50    | ~7,899 | ~320 | ~832  |
| 60    | ~8,804 | ~357 | ~927  |
| 70    | ~9,628 | ~390 | ~1,014|
| 80    | ~10,213| ~414 | ~1,076|
| 90    | 10,775 | 438  | 1,137 |

- Max Energy: 125
- Base CRIT Rate: 5%
- Base CRIT DMG: 150%
- Base Healing Bonus: 0%
- Base Havoc DMG: 0%

## Chisa: Stats Baseline: Max Analysis
At Level 90 with all Minor Fortes unlocked:
- ATK: 438 base → +12% ATK from Minor Forte → ~491 effective ATK at base
- CRIT Rate: 5% base → +8% from Minor Forte → 13% base (before Echoes/substats)
- HP: 10,775 — moderate HP pool sufficient for her healing/shield formulas which scale off ATK
- Chisa has the **highest base ATK of any support/healer in Wuthering Waves** at release (438), reflecting her hybrid offensive support role
- Recommended final stat spread: CRIT Rate ~70% / CRIT DMG ~250%+ / ATK% / Havoc DMG% / Energy Regen (if sub-130%)
- Key note: Chisa's healing scales off ATK, so stacking ATK benefits both her personal damage and her team sustain simultaneously

## Chisa: Ascension Materials
Total materials required for full character ascension (Level 1 → 90):
- 4× LF Polygon Core
- 12× MF Polygon Core
- 12× HF Polygon Core
- 4× FF Polygon Core
- 46× Abyssal Husk
- 60× Summer Flower (open-world gather, Ashinohara region)
- 170,000 Shell Credits

## Chisa: Basic Attack — Reign of Silence
**Basic Attack:**
Performs up to 2 consecutive attacks, dealing Havoc DMG. Press Normal Attack shortly after Stage 2 to cast Rending Lunge.

**Rending Lunge:** Deals Havoc DMG. On ground: press Normal Attack to cast Death Snip; in mid-air: press Normal Attack to cast Hanging Finality.

**Death Snip:** Opens the scissors (Havoc DMG), then after a brief delay, snips (Havoc DMG) and restores HP for all nearby Resonators. Additional Normal Attack input during the skill deals bonus Havoc DMG; another Normal Attack immediately snips. Death Snip DMG is considered **Resonance Liberation DMG**. Press Normal Attack after to cast Thread Withdrawn.

**Thread Withdrawn:** Deals Havoc DMG. Can trigger successful Dodges within a time window after being cast.

**Heavy Attack:** Leap into the air, consume STA, attack the target (Havoc DMG). Cannot cast in Chainsaw Mode. Follow-up options: press Normal Attack → Hanging Finality; hold Normal Attack before landing → Severed Facet.

**Mid-air Attack:** Consume STA for Plunging Attack (Havoc DMG). Not in Chainsaw Mode: press Normal Attack shortly after to cast Basic Attack Stage 2.

**Severed Facet:** Deals Havoc DMG. Press Normal Attack shortly after → Hanging Finality.

**Hanging Finality:** Consume STA for Plunging Attack (Havoc DMG). Press Normal Attack after landing → Death Snip.

**Dodge Counter:** Deals Havoc DMG. Press Normal Attack shortly after → Rending Lunge.

**Dodge Counter - Eye of Unraveling: Retraction:** Hold Dodge after successful Dodge on the ground → attacks and Stagnates target (Havoc DMG). Not in Chainsaw Mode: press Normal Attack → Rending Lunge (removed on entering Chainsaw Mode). In Chainsaw Mode: press Normal Attack → Sawring - Blitz Stage 3.

**Attribute Scaling (Level 1 values, ATK-based):**
- Stage 1 DMG: 8.40%×2
- Stage 2 DMG: 4.80% + 9.60% + 33.60%
- Death Snip DMG: 15.00% + 7.50% + 52.48% (Liberation-type)
- Death Snip Additional DMG: 24.03%
- Death Snip Healing: 600 + 24.00% ATK
- Thread Withdrawn DMG: 5.11%×2 + 23.82%
- Rending Lunge DMG: 7.61%×4 + 45.61%
- Heavy Attack DMG: 18.00%×2
- Mid-air Attack DMG: 37.20%
- Severed Facet DMG: 22.50%×2
- Hanging Finality DMG: 6.00% + 12.00%×2 + 30.00%
- Dodge Counter DMG: 12.00% + 24.00% + 84.00%
- Eye of Unraveling Retraction DMG: 90.00%
- STA Costs: Heavy Attack 20; Mid-air Attack 30; Severed Facet 10; Hanging Finality 10

## Chisa: Resonance Skill — Fractured Composition
**Eye of Unraveling:**
Stagnates and deals Havoc DMG to the target.
- Not in Chainsaw Mode: press Normal Attack after → Rending Lunge (removed on entering Chainsaw Mode)
- In Chainsaw Mode (on ground): press Normal Attack → Sawring - Blitz Stage 2
- Can be cast in mid-air
- Hitting a target with this skill applies Unseen Snare (30s DEF ignore mark)

**Serrated Loop:**
Available when Ring of Chainsaw is full (100 points) and on the ground; replaces Eye of Unraveling. Stagnates targets, deals Havoc DMG, and pulls in nearby targets. Sends Chisa into **Chainsaw Mode**; replaces Resonance Skill with Eye of Unraveling.
- Press Normal Attack after → Sawring - Blitz Stage 2
- Hold Resonance Skill during cast to continuously attack and pull in nearby targets; release or hold for set duration → Sawring - Blitz Stage 1

**Attribute Scaling (Level 1 values):**
- Eye of Unraveling DMG: 18.00%
- Serrated Loop DMG: 8.78%×8
- Serrated Loop Hold DMG: 3.76%×16
- Eye of Unraveling Cooldown: 12 seconds

## Chisa: Resonance Liberation — Moment of Nihility
Deals Havoc DMG and recovers HP for all nearby Resonators in the team. Sends Chisa into **Woven Myriad - Convergence** for 15 seconds.

**Woven Myriad - Convergence (Ultimate buff state):**
- DMG Multipliers of Sawring - Blitz, Chainsaw Mode - Dodge Counter, and Sawring - Eradication are increased by **120%**
- The per-Ring-of-Chainsaw bonus DMG Multiplier for Sawring - Eradication (normally 1.30% per point) additionally increases by **120%** in this state
- Casting Sawring - Eradication ends Woven Myriad - Convergence

This means the optimal rotation is: cast Ultimate (120% buff + heal) → immediately execute Sawring - Blitz chain → Sawring - Eradication for maximum burst under the Ultimate buff window.

**Attribute Scaling (Level 1 values):**
- Moment of Nihility DMG: 480.00%
- Healing: 1,400 + 56.00% ATK
- Cooldown: 25 seconds | Energy Cost: 125 | Concerto Regen: 20

## Chisa: Forte Circuit — Sight of Unraveling: Oblivion
**Unseen Snare (mark application):**
Applied by: hitting targets with Resonance Skill; hitting target post-Serrated Loop window; hitting with Dodge Counter - Eye of Unraveling: Retraction; locking onto a target.
Duration: 30 seconds.
Effect: when marked target takes direct damage from any Resonator, inflicts 1 stack of **Havoc Bane** (once per 2s baseline; 1s at S4).

**Thread of Bane (DEF ignore):**
When dealing damage to Unseen Snare targets, ignore **18%** of their DEF. This effect applies to all Resonators attacking the marked target.

**Chainsaw Mode:**
Unlocked via Serrated Loop. Replaces normal moveset with Sawring - Blitz (3 stages), Chainsaw Mode - Dodge Counter, and Sawring - Eradication. Maintained by Chainsaw Fever gauge; exits via Sawring - Eradication or Burnout State.

**Sawring - Blitz (3-stage, all considered Resonance Liberation DMG):**
- Stage 1: 6 hits; Stage 2: 8 hits (hold = 10 hits) + Discordance follow-up (3 hits); Stage 3: 8 hits (hold = 6 hits) + Falltone follow-up (3 hits)
- Each Sawring attack consumes Ring of Chainsaw on hit

**Chainsaw Mode - Dodge Counter (Liberation DMG):**
- 8 hits (hold = 10 hits) + Discordance follow-up option
- Also consumes Ring of Chainsaw

**Sawring - Eradication (Liberation DMG):**
- Triggered after: Sawring - Blitz Stage 3: Falltone + Normal Attack; or all Ring of Chainsaw consumed
- Deals Havoc DMG and grants **Shield to all nearby Resonators** (2000 + 80.00% ATK) for 30 seconds
- Generates 45 Concerto Energy on cast — the primary Concerto Energy source for Chisa's Outro
- Each point of Ring of Chainsaw consumed before Eradication: +1.30% bonus DMG Multiplier (up to 100 points = +130% bonus)
- Ends Chainsaw Mode

**Attribute Scaling (Level 1 values):**
- Sawring - Blitz Stage 1 DMG: 5.78%×6
- Sawring - Blitz Stage 2 DMG: 5.35%×8
- Sawring - Blitz Stage 2 Hold DMG: 5.35%×10
- Sawring - Blitz Stage 2: Discordance DMG: 1.80%×3
- Sawring - Blitz Stage 3 DMG: 8.04%×8
- Sawring - Blitz Stage 3 Hold DMG: 8.04%×6
- Sawring - Blitz Stage 3: Falltone DMG: 1.80%×3
- Chainsaw Mode - Dodge Counter DMG: 5.35%×8
- Chainsaw Mode - Dodge Counter Hold DMG: 5.35%×10
- Sawring - Eradication DMG: 25.92% + 103.68%
- Sawring - Eradication Ring of Chainsaw bonus per point: 1.30%
- Sawring - Eradication Shield: 2,000 + 80.00% ATK
- Sawring - Eradication Concerto Regen: 45

## Chisa: Inherent Skill 1 — Inescapable Fate
When a Resonator in the team defeats a target marked by **Unseen Snare**, the Cooldown of Chisa's Resonance Skill Eye of Unraveling is reset.
Triggered up to **once every 3 seconds**.

This passive makes Chisa's Resonance Skill spammable in multi-enemy content — each kill on a marked target resets the 12s cooldown, allowing continuous Unseen Snare application and Ring of Chainsaw generation.

## Chisa: Inherent Skill 2 — All Ends Here
Casting Intro Skill Reverberance - Return or Resonance Liberation Moment of Nihility grants:
- **20% Havoc DMG Bonus** for 12 seconds
- **20% Healing Bonus** for 12 seconds

Additionally: when Resonators in the team with Thread of Bane defeat a target marked by Unseen Snare, Chisa gains **Sight of Unraveling** for 3 seconds.
During Sight of Unraveling: Chisa inflicts Unseen Snare (30s duration) on targets damaged by Resonators in the team with Thread of Bane — meaning kills refreshed Unseen Snare automatically during this window.

## Chisa: Intro Skill — Reverberance - Return
Attacks the target, dealing Havoc DMG. Grants **20 Ring of Chainsaw**.
- Not in Chainsaw Mode: press Normal Attack shortly after → Basic Attack Stage 2
- In Chainsaw Mode: press Normal Attack shortly after → Sawring - Blitz Stage 2

**Attribute Scaling (Level 1 values):**
- Intro Skill DMG: 48.00%
- Concerto Regen: 10

## Chisa: Outro Skill — Unraveling - Law Zero
Grants **Resonant Thread of Closure** to all nearby Resonators in the team for 20 seconds.

While in Resonant Thread of Closure:
- When an attack hits: increase the max stacks of Negative Status and Electro Rage the target can receive by **3** for 15 seconds (unstackable)
- Inflicting Negative Status or dealing Negative Status DMG grants **Thread of Bane** for 15 seconds — critically, this extends Thread of Bane availability to Resonators who wouldn't otherwise have it

**Key implication:** Chisa's Outro enables non-Chisa characters to carry Thread of Bane (and thus benefit from Havoc Bane stacking) by connecting Negative Status application to the Thread of Bane effect. This is especially relevant for increasing Cartethyia's Aero Erosion interaction with Havoc Bane stacks.

## Chisa: Skill Upgrade Materials
Total materials required to max all skills:
- 25× LF Polygon Core
- 28× MF Polygon Core
- 40× HF Polygon Core
- 57× FF Polygon Core
- 25× Waveworn Residue 210
- 28× Waveworn Residue 226
- 55× Waveworn Residue 235
- 67× Waveworn Residue 239
- 26× When Irises Bloom
- 2,030,000 Shell Credits

**Skill Priority (recommended order):**
1. Forte Circuit (Sawring - Eradication scaling; core burst skill)
2. Resonance Liberation (Moment of Nihility DMG + healing)
3. Resonance Skill (Eye of Unraveling / Serrated Loop; Ring of Chainsaw generation and grouping)
4. Intro Skill (Reverberance - Return; consistent DMG + Ring generation)
5. Basic Attack (Death Snip healing; situationally useful, lowest priority overall)

## Chisa: Resonance Chains (S1 – S6)
**S1 – Sequence Node 1:**
- Immunity to interruption during Sawring - Blitz, Sawring - Eradication, and Chainsaw Mode - Dodge Counter
- Inflicting Unseen Snare grants:
  - Chisa's ATK increased by **30%** for 15 seconds
  - Deals fixed **61,803 Havoc DMG** (Basic Attack classified; cannot exceed target-specific HP reduction rules; this instance bears no damage bonus effects). Target's HP can be reduced to 61.80% at most from this single instance per target
- This is Chisa's best individual sequence: massive ATK boost + a fixed Havoc DMG burst on Snare application

**S2 – Sequence Node 2:**
- Ignore **10%** of target's Havoc RES when dealing damage
- Nearby Resonators in the team with Thread of Bane gain **50% All-Attribute DMG Bonus**
- The 50% All-DMG Bonus is an enormous team-wide buff — the most impactful support sequence after S1

**S3 – Sequence Node 3:**
- DMG Multipliers of Sawring - Blitz, Chainsaw Mode - Dodge Counter, and Sawring - Eradication increased by **120%** (mutually stackable with Woven Myriad - Convergence's 120%)
- Ring of Chainsaw bonus per point for Sawring - Eradication increased by **120%** (also stackable with Woven Myriad)
- Vibration Strength Reduction Rate of Sawring attacks increased by **50%** (improved stagger application)
- At S3: total Sawring DMG multiplier is **240%** bonus during Ultimate (120% + 120%); Eradication bonus per Ring of Chainsaw point scales to 2.60% + another 2.60% bonus from ultimate = 5.20% per point under optimal conditions

**S4 – Sequence Node 4:**
- Unseen Snare Havoc Bane stacking trigger changes from once per **2 seconds** to once per **1 second** — effectively doubles the rate of Havoc Bane application to marked targets

**S5 – Sequence Node 5:**
- Resonance Liberation Moment of Nihility gains **100% DMG Bonus**
- Lifethread - Glide costs **50% less** Lifethread - Jetstream (from 50 to 25 points per cast)

**S6 – Sequence Node 6:**
- Survival: when Chisa takes a fatal blow during Sawring - Blitz, Sawring - Eradication, or Chainsaw Mode - Dodge Counter, she survives with at least 1 HP
- Unseen Snare becomes **Unseen Snare - Finality**:
  - Has all effects of Unseen Snare
  - Targets take **30% Amplified DMG** from Negative Statuses
  - Targets take **40% increased DMG from Chisa** — a massive personal damage multiplier upgrade

**Key investment notes:**
- S0: Already provides 18% DEF ignore, healing, Shield, and Havoc Bane stacking — viable at S0
- S1+S2 (Signature pairing): the 30% ATK boost + 50% All-DMG Bonus are Chisa's most impactful early sequences for team buffing
- S3: transforms her Chainsaw phase into extreme personal burst
- S6: makes her the highest personal-damage support in Havoc team context

## Chisa: Echo Sets — Best Sets
**Best Set: Nightmare: Tempest Mephis (5-piece)**
- Provides Havoc DMG Bonus (2-piece) and an additional conditional Havoc DMG Bonus when using Liberation skills (5-piece)
- Recommended by Game8 and WuWaLabo as Chisa's primary Echo set
- Alternative: **Midnight Veil (5-piece)** — a dedicated Havoc-amplification set that provides both personal Havoc DMG and team-relevant buffs

**Situational: Chaos Blaze Set** — older Havoc set; still viable if Nightmare: Tempest Mephis is unavailable

## Chisa: Echo Sets — Best Main Echo
**Best 4-cost Main Echo:**
- **Nightmare: Tempest Mephis** — Havoc DMG Bonus + Resonance Liberation DMG Bonus; directly relevant to Chisa's Liberation-classified damage
- **Nightmare: Thundering Mephis** — alternative if Tempest Mephis is unfarmed; provides similar Liberation DMG bonuses

**Best Havoc-specific Echo effects:** prioritize Echo skills that provide ATK buffs, Havoc DMG Bonus, or additional healing scaling to maximize both her damage and support utility simultaneously

## Chisa: Echo Sets — Echo Stat Priority
**Recommended Echo Configuration (4-4-3-3-1):**
- 4-cost slot (main): CRIT Rate or CRIT DMG
- Second 4-cost: CRIT DMG or CRIT Rate (balance to ~70% CRIT Rate)
- 3-cost slots: Havoc DMG% main stat (personal damage) or ATK% (scales healing + damage)
- 1-cost slot: ATK% main stat

**Substat Priority:**
CRIT Rate = CRIT DMG (balance to ~70/250) → ATK% → Energy Regen (if sub-125%) → Liberation DMG% → Havoc DMG%

**Note:** Since Chisa's healing scales off ATK, ATK% substats benefit both her DPS and her team sustain simultaneously — stacking ATK% is never wasted on her.

## Chisa: Weapons — Best Weapon
**Kumokiri (5-star Broadblade — Signature):**
- Sub-stat: CRIT DMG (48.6% at max level)
- R1 Effect: when casting Resonance Liberation or Resonance Skill, increases Resonance Liberation DMG Bonus. Since virtually all of Chisa's major damage skills are Liberation-classified (Sawring series, Death Snip), this is an enormous personal damage multiplier
- The signature weapon also adds team-relevant buffs that interact with her Outro and Havoc Bane stacking
- Per Prydwen: Chisa is *"only stronger than Aero Rover in the Cartethyia team third slot with her Signature"* — the signature weapon is a significant investment unlock

## Chisa: Weapons — Alternative Weapons
**Stonard (5-star Standard Broadblade):** High CRIT DMG secondary; Liberation DMG bonus effects; the best standard-banner alternative for Chisa.

**Lustrous Razor (5-star Standard):** ATK% secondary; reliable stat stick with Liberation DMG bonus; strong alternative if Stonard is unavailable.

**Discord's Beckon (5-star Standard):** ATK% secondary with Energy Regen effect via Resonance Skill — eases rotations if Energy generation is tight.

**Verdant Summit (5-star Limited):** CRIT DMG secondary; if obtained from prior banners, works well on Chisa due to Liberation DMG amplification.

**Dauntless Evernight (4-star):** Solid ATK increase and Energy Regen on Resonance Skill use; best accessible 4-star for Chisa's rotation needs.

**Comet Flare (4-star Battle Pass):** CRIT DMG secondary; quick ATK% increase after casting Ultimate; a strong 4-star investment for players who cannot access 5-star alternatives.

## Chisa: Team Composition Guide — Best Team (Cartethyia/Ciaccona/Chisa)
**Cartethyia / Ciaccona / Chisa** (Best ToA Team, Patch 2.8, per Prydwen)
- Cartethyia: primary carry; Aero HP-scaling hypercarry; generates Aero Erosion stacks for massive Erosion explosion damage
- Ciaccona: Aero buffer/support; increases Erosion stack cap; provides Aero DMG Bonus amplification; Ciaccona's Outro enables Cartethyia's Erosion interaction at maximum efficiency
- Chisa: third slot support; provides 18% DEF ignore (Thread of Bane), Havoc Bane stacking, healing (critical since Cartethyia consumes HP on Liberation), Shield (Sawring - Eradication), grouping (Serrated Loop), and via Outro increases Negative Status stack capacity on targets

**Why Chisa over Aero Rover (the standard third slot):**
- Chisa provides unique DEF shred (DEF ignore via Thread of Bane) that Aero Rover cannot match
- Chisa's healing and Shield directly sustain Cartethyia through her HP-consumption mechanic
- At S0 with signature weapon: Chisa is the superior third slot by a meaningful margin
- Without signature weapon: Aero Rover may outperform Chisa — investment threshold is important

**Standard Rotation (Cartethyia/Ciaccona/Chisa):**
Chisa: Intro → Eye of Unraveling (apply Unseen Snare) → Basic Attacks (build Ring of Chainsaw) → Serrated Loop (enter Chainsaw Mode) → Ultimate → Sawring - Blitz chain → Sawring - Eradication (Shield + Concerto) → Outro
Ciaccona: Intro → Ciaccona rotation → Outro
Cartethyia: Intro → Full Cartethyia rotation (Resonance Skill → Liberation → Fleurdelys form → Blade of Howling Squall)

## Chisa: Team Composition Guide — Alternative Teams
**Cartethyia / Aero Rover / Chisa** (budget Cartethyia team, no Ciaccona):
- Chisa fills the third slot providing DEF ignore and sustain; Aero Rover takes Ciaccona's buffing role
- Weaker than the optimal trio but still viable; recommended for players who have Cartethyia and Chisa but not Ciaccona

**Rotation:** Chisa rotation → Aero Rover rotation → Cartethyia rotation; prioritize Cartethyia's Ultimate window above all

**Havoc DPS / Buffer / Chisa** (generic Havoc carry + Chisa support):
- Chisa's Thread of Bane DEF ignore and Havoc Bane stacking are relevant to any Havoc DPS
- Danjin, Xiangli Yao, or Rover (Havoc) as the primary carry; Chisa as third slot support
- Chisa's Outro increases Negative Status stack cap which can synergize with Electro Rage effects if team includes an Electro character

**Rotation (generic Havoc team):** Support quick rotation → Chisa rotation → Havoc DPS full window

## Chisa: DPS Benchmarks: S0 to S6 (Source: Prydwen.gg — Primary)
*Note: Chisa's benchmarks are primarily calculated in team context as a support character. Her personal damage contribution in the Cartethyia team is secondary to her buff value (DEF ignore, Havoc Bane, healing, Shield). For exact numerical benchmarks, refer directly to Prydwen's Calculations tab: https://www.prydwen.gg/wuthering-waves/characters/chisa/*

**Team benchmarks (Cartethyia / Ciaccona / Chisa, per Prydwen Patch 2.8):**
- This team is listed as the highest-DPS team in Tower of Adversity in Patch 2.8 on Prydwen's tier list
- S0 Chisa (with Signature): enables T0.5 ToA rating for the team
- S0 Chisa (without Signature): T1.5 ToA; Aero Rover may outperform as third slot at this investment level

**Sequence-by-sequence qualitative assessment (Prydwen review):**
- S0: Provides 18% DEF ignore, healing, Shield, Havoc Bane stacking — fully functional support baseline
- S1: +30% Chisa ATK + fixed 61,803 Havoc DMG on Snare application — meaningful personal damage spike; best early sequence
- S2: +10% Havoc RES ignore + 50% All-Attribute DMG Bonus to team with Thread of Bane — exceptional team damage increase; top-priority sequence after S1
- S3: +120% Sawring multipliers (stacks with Ultimate's +120%) — transforms her Chainsaw phase into extreme burst; primarily personal damage
- S4: Havoc Bane tick rate doubles (2s → 1s) — increases team DEF-shred interaction speed
- S5: +100% Liberation DMG + Lifethread - Glide cost halved — personal damage and mobility improvement
- S6: Survival passive + 30% Amplified Negative Status DMG + 40% increased DMG from Chisa — the highest personal damage sequence; turns her into a genuine semi-DPS

**Build used for Prydwen benchmarks:**
- Kumokiri (Signature) R1
- 5pc Nightmare: Tempest Mephis
- Nightmare: Tempest Mephis main Echo
- CRIT Rate ~70% / CRIT DMG ~250% / ATK% substats
- Teammates: Cartethyia (Defier's Thorn R1) + Ciaccona at Lv.90 max ascension

## Chisa: Character Strengths and Weaknesses in Actual Gameplay
**Strengths:**
- Best support for the best Tower of Adversity team in the game (Patch 2.8) — provides a completely unique DEF reduction mechanic (18% DEF ignore via Thread of Bane) that no other support character replicates
- Healing at multiple points in rotation (Death Snip, Moment of Nihility) — essential for Cartethyia who actively consumes HP
- Team-wide Shield generation from Sawring - Eradication protects all characters during long rotations
- AoE grouping via Serrated Loop and Lifethread - Glide — pulls enemies into melee range for AOE DPS characters
- Resonance Skill Cooldown reset on marked-target kills (Inescapable Fate) — near-infinite Skill uptime in multi-enemy content
- Charismatic Intro Skill provides +20 Ring of Chainsaw immediately — fast rotation entry
- Extremely long Chainsaw Mode burst windows with Woven Myriad - Convergence making all Sawring attacks 120% stronger — high personal damage floor despite support role
- Relatively straightforward rotation execution despite visual complexity; Chainsaw Fever management is the main mechanical requirement

**Weaknesses:**
- Strongly signature-dependent for her best-in-slot role: without Kumokiri, Aero Rover may outperform her in the Cartethyia team (per Prydwen)
- Chainsaw Fever management: must continue dealing damage in Chainsaw Mode or risk Burnout State and losing the entire buff window; requires consistent engagement with the enemy
- DEF ignore and Havoc Bane are only optimal against enemies vulnerable to multi-hit DMG interactions; against single-phase, single-hit enemies the benefits are more modest
- T1.5 in Whimpering Wastes (mobile arena) — her grouping and tanky playstyle favor stationary enemies; Wastes benefits less from her DEF shred mechanics
- Investment threshold is high: optimal performance requires signature weapon, leveled Forte Circuit, and specific Echo set; F2P players may find Aero Rover more accessible for similar team performance
- Cannot provide traditional off-element buffs (ATK%, DMG% in the way Sanhua or Aero Rover can); her buffs are Havoc-intrinsic (Bane stacking, DEF ignore, Negative Status cap)

---

## Chisa Kit Sources
- Prydwen – Chisa Guide and Build (Primary): https://www.prydwen.gg/wuthering-waves/characters/chisa/
- Prydwen – Cartethyia Guide (team context): https://www.prydwen.gg/wuthering-waves/characters/cartethyia/
- Wuthering Waves Fandom Wiki – Chisa Combat: https://wutheringwaves.fandom.com/wiki/Chisa/Combat
- Game8 – Chisa Best Builds and Teams: https://game8.co/games/Wuthering-Waves/archives/chisa
- WuWaLabo – Chisa Build Guide: https://wuwalabo.com/en/characters/chisa-guide/
- Wuthering.gg – Chisa Character Page: https://wuthering.gg/characters/chisa
- LDShop – Chisa Build Guide: https://www.ldshop.gg/blog/guide/wuwa-chisa-build.html
- Lootbar – Chisa Build Guide: https://lootbar.gg/blog/en/wuthering-waves-chisa-build-guide.html
- Pocket Tactics – Chisa Build Guide: https://www.pockettactics.com/wuthering-waves/chisa
