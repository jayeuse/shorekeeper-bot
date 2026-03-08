---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/rinascita/phrolova/phrolova_kit.md
character: Phrolova
group: Rinascita
document_type: character_kit
importance: high
tags:
- character
- kit
- combat
---

# Phrolova Kit Documentation
<!-- Sources: Wuthering Waves Fandom Wiki, Prydwen.gg, Game8.co, Wutheringlab.com, Wuthering.gg, LDShop.gg, LootBar.gg, Sportskeeda, XboxPlay.games -->

## Phrolova: Combat Archetype and Role
- **Attribute:** Havoc
- **Weapon:** Rectifier
- **Primary Scaling:** ATK (with secondary Crit Rate scaling from passive and signature weapon)
- **Combat Role:** Main DPS / Off-Field DPS hybrid — on-field burst rotation into sustained off-field Hecate summon attacks
- **Key Resources:**
  - **Volatile Notes** (Forte Gauge, max 6): Generated via Basic Attack Stage 3, Resonance Skill, and their enhanced derivatives. Three types: Strings (red, from Basic Attack path), Winds (blue, from Resonance Skill path), Cadenza (multicolored, from Echo Skill/Intro/Inherent Skill). Red ≥ Multicolored > Blue in damage output.
  - **Aftersound** (max 24 stacks): A buff resource that increases Phrolova's Crit DMG and scales Scarlet Coda's DMG Multiplier. Gained through Hecate's Enhanced Attacks during Maestro state. At S0, 1 stack = +2.5% Crit DMG (up to 60%). Each stack beyond max adds +1% Crit DMG, up to +100% bonus.
  - **Compose State (25s cooldown):** Periodically enters this state. Required alongside 6 Volatile Notes and non-Resolving Chord state to activate Scarlet Coda.
  - **Resolving Chord State:** Activated by casting Scarlet Coda. Required to unlock and cast Resonance Liberation (Waltz of Forsaken Depths).
  - **Maestro State (24s duration):** Activated upon casting Waltz of Forsaken Depths. Grants +120% ATK, causes Phrolova to float and command Hecate. Can be maintained on-field or off-field.
  - **Resonance Energy:** Phrolova's max Resonance Energy is 0. She generates no Resonance Energy for herself and cannot use Resonance Liberation via standard Energy. Her Liberation is exclusively unlocked by the Resolving Chord state. She does generate a small amount of Energy for teammates (comparable to Cantarella).

## Phrolova: Stats Baseline
Stats listed at base (no echoes, no forte bonuses). These are base character stats only.

| Level | HP     | ATK | DEF  |
|-------|--------|-----|------|
| 1     | ~800   | ~29 | ~80  |
| 10    | ~1,620 | ~57 | ~160 |
| 20    | ~2,814 | ~99 | ~277 |
| 30    | ~3,918 | ~138| ~385 |
| 40    | ~5,121 | ~180| ~503 |
| 50    | ~6,519 | ~229| ~640 |
| 60    | ~7,908 | ~278| ~776 |
| 70    | ~9,197 | ~323| ~903 |
| 80    | ~10,418| ~367| ~1,022|
| 90    | ~10,570| ~372| ~1,035|

*Note: Exact per-level figures for Phrolova are not publicly listed in a complete table by official sources as of Version 2.8. The above are approximate figures extrapolated from community sources and the known Lv.90 stat block. Confirmed Lv.90 base ATK from Prydwen: approximately 372 (before Forte bonuses). Stat calculations do not include Attribute Bonuses from Phrolova's Forte.*

**Lv.90 Confirmed Stats (S0, no echoes, with Forte minor bonuses):**
- HP: ~10,825 (Prydwen community reference)
- ATK: ~413 (with minor Forte bonuses: Havoc DMG +12%, ATK% +12%)
- DEF: ~1,259
- Max Energy: 0
- CRIT Rate: 5% (base)
- CRIT DMG: 150% (base)

**Base Weapon (Lethean Elegy, Signature):**
- Base ATK: 588
- Secondary Stat: Crit Rate 24.3% (at max refinement R1)
- Effect R1: ATK +12%. Within 12s after dealing Echo Skill DMG, gain 32% Resonance Skill DMG Bonus + 32% Echo Skill DMG Amplification + ignore 8% of target DEF.
- Effect R5 (max): ATK +24%. Echo Skill DMG → 64% Res. Skill DMG Bonus + 64% Echo Skill DMG Amplification + ignore 16% DEF.

**Analysis:**
Phrolova's stat profile leans heavily into ATK scaling, with her kit further amplified by Aftersound-stacking Crit DMG and the unique 120% ATK self-buff granted during her Maestro state — effectively nearly doubling her own ATK for the entire duration Hecate is active off-field. At S0 with signature weapon, her base Crit Rate is approximately 57.3% before echoes, making overcapping a genuine concern when using Dream of the Lost.

## Phrolova: Ascension Materials
Full Ascension (Lv.1 → Lv.90):

- **Afterlife** (overworld flower): ~60 total — found in Fabricatorium of the Deep (Fallen Grave, Anima Cradle, Shards of the Beyond areas); also available in The Silver Helmet
- **Truth in Lies** (boss drop): Obtained from Fenrico — located in Lumen Tower, Fabricatorium of the Deep
- **Polygon Core Series** (echo drops from Rinascita):
  - LF Polygon Core (common)
  - MF Polygon Core (uncommon)
  - HF Polygon Core (rare)
  - FF Polygon Core (epic — synthesizable)
- **Shell Credits:** 170,000 total for full ascension to Lv.90

## Phrolova: Game Kit

## Phrolova Basic Attack: Elegy of the Fallen
Perform up to 3 consecutive attacks, dealing Havoc DMG.
- **Stage 1:** Single hit, Havoc DMG
- **Stage 2:** Single hit, Havoc DMG
- **Stage 3:** Phrolova launches Hecate outward; Hecate spins and groups nearby enemies. On hit, grants 1 Volatile Note – Strings (red). Entering Reincarnate state after Stage 3 completion.
- **Heavy Attack:** Consumes STA to attack target, dealing Havoc DMG. Press Normal Attack shortly after to cast Basic Attack Stage 2.
- **Scarlet Coda (Heavy Attack replacement):** When Phrolova has 6 Volatile Notes, is in Compose state, and is NOT in Resolving Chord state, Heavy Attack is replaced with Scarlet Coda. Consumes STA to deal Havoc DMG to nearby targets, Stagnating and pulling them in. This is considered Resonance Skill DMG. Each stack of Aftersound additionally increases the DMG Multiplier of Scarlet Coda. Casting this skill is considered casting an Echo Skill. Triggers Resolving Chord state and puts Compose state on cooldown.
- **Mid-Air Attack:** Consume STA for a Plunging Attack, dealing Havoc DMG.
- **Dodge Counter:** Press Normal Attack after a successful Dodge for a Havoc DMG counter. Press Normal Attack shortly after to chain into Basic Attack Stage 3.

**Basic Attack Attribute Scaling (% of ATK, Level 1 → Level 10):**

| Level | Stage 1 | Stage 2 | Stage 3 | Heavy Attack |
|-------|---------|---------|---------|--------------|
| 1     | ~34.8%  | ~37.3%  | ~82.2%  | ~87.5%       |
| 5     | ~45.1%  | ~48.5%  | ~107.1% | ~113.9%      |
| 10    | ~68.0%  | ~72.9%  | ~161.2% | ~171.5%      |

*Note: Exact per-level scaling tables for Phrolova are not officially published in a standardized format. Figures above are community approximations based on available data at Lv.1 and Lv.10; consult the in-game skill screen or Wuthering Waves Wiki for confirmed values per level.*

## Phrolova Resonance Skill: Whispers in a Fleeting Dream
Phrolova leaps backward and summons Hecate, which after a brief delay pulls surrounding enemies toward her, dealing Havoc DMG. After casting, Phrolova enters Reincarnate state.
- Grants 1 Volatile Note – Winds (blue) on enemy hit.
- Empowers the next Basic Attack and next Resonance Skill cast (Enhanced variants).
- **Cooldown:** Moderate (exact CD to be confirmed in game; approximately 8–10s based on community reports).

**Reincarnate State Abilities (derived from Basic Attack Stage 3 or Resonance Skill):**
- **Movement of Fate and Finality** (Enhanced Basic Attack in Reincarnate): Press Normal Attack on the ground to deal Havoc DMG (considered Resonance Skill DMG) and Stagnate the target. Grants 1 Volatile Note – Strings. Ends Reincarnate.
- **Murmurs in a Haunting Dream** (Enhanced Resonance Skill in Reincarnate): Press Resonance Skill on the ground to deal Havoc DMG (considered Resonance Skill DMG) and pull nearby enemies. Grants 1 Volatile Note – Winds. Ends Reincarnate.

**Resonance Skill Attribute Scaling (% of ATK, estimated Level 1 → Level 10):**

| Level | Whispers in a Fleeting Dream | Movement of Fate & Finality | Murmurs in a Haunting Dream |
|-------|------------------------------|-----------------------------|-----------------------------|
| 1     | ~80–90%                      | ~130–140%                   | ~120–130%                   |
| 10    | ~155–175%                    | ~260–280%                   | ~240–260%                   |

*These figures are community-estimated ranges based on available sources. Consult the in-game skill screen for official values.*

## Phrolova Resonance Liberation: Waltz of Forsaken Depths
- **Resonance Energy Cost:** 0 (Phrolova has no Resonance Energy system)
- **Activation Requirement:** Must be in Resolving Chord state (entered via Scarlet Coda)
- **Cooldown:** Effectively 25 seconds (tied to the Compose state cooldown which gates Scarlet Coda)

Casting Waltz of Forsaken Depths ends the Resolving Chord state and enters the **Maestro state** for 24 seconds.

**Maestro State:**
- Gain 120% ATK increase.
- Phrolova floats in the air and commands Hecate to fight.
- Hecate shares Phrolova's stats and statuses; all Hecate damage is considered Phrolova's damage.
- Hecate's attacks will NOT remove the target's Hazy Dream state.
- The 6 Volatile Notes on the Forte bar are locked; Hecate plays them in sequence, left to right, each note lasting 4 seconds (6 notes × 4s = 24s total duration).
- Each note type determines Hecate's enhanced attack pattern during that note's window.

**On-Field Cues (if Phrolova is the active Resonator):**
- Cue – Basic Attack: Press Normal Attack → Hecate casts Basic Attack – Hecate. For every 2 basic Hecate attacks, the 3rd becomes Enhanced Attack – Hecate (note-type dependent).
- Cue – Dodge: Press Dodge → Hecate dodges. Hecate takes no damage from a successfully dodged hit.
- Cue – Reset: Press Jump → resets Hecate's position.
- Cue – Curtain Call: Press Resonance Liberation → Hecate casts Curtain Call, ending Maestro state early.

**Off-Field Behavior (if Phrolova is NOT the active Resonator):**
- Hecate takes no damage.
- Hecate automatically casts Basic Attack – Hecate against targets.
- When any Resonator in the team casts an Echo Skill, Hecate casts Enhanced Attack – Hecate. This effect can be triggered up to 10 times total during Maestro. Echoes of the same name trigger this only 1 time.
- Switching back to Phrolova ends Maestro state.

**Hecate Enhanced Attack Types:**
- **Strings (red note):** Havoc DMG + Stagnates target. ~347.9% ATK multiplier.
- **Winds (blue note):** Havoc DMG + Pulls targets. ~330.5% ATK multiplier (slightly lower but negligible difference).
- **Cadenza (multicolored note):** Havoc DMG + Pulls + Stagnates. ~347.9% ATK multiplier (same as Strings).

**Maestro State Bonuses (depending on active/inactive Resonator):**
- If Phrolova IS the active Resonator during Maestro: gain **60% Havoc DMG Bonus** (S6 effect).
- If Phrolova is NOT the active Resonator during Maestro: targets take **40% more DMG** from Hecate and Phrolova (S6 effect).

**Liberation Attribute Scaling (Hecate Enhanced Attacks, estimated Level 1 → Level 10):**

| Level | Strings Multiplier | Winds Multiplier | Cadenza Multiplier |
|-------|--------------------|------------------|--------------------|
| 1     | ~220%              | ~209%            | ~220%              |
| 5     | ~290%              | ~275%            | ~290%              |
| 10    | ~347.9%            | ~330.5%          | ~347.9%            |

*Lv.10 figures confirmed by Wutheringlab and community sources. Lower levels are approximations.*

## Phrolova Forte Circuit: Symphonic Surge
Phrolova's Forte Circuit is the musical note system — a gauge holding up to 6 Volatile Notes simultaneously. Adding a 7th note replaces the oldest note from the left.

**Note Acquisition:**
- Basic Attack Stage 3 hit → 1 Volatile Note – Strings (red)
- Movement of Fate and Finality hit → 1 Volatile Note – Strings (red)
- Whispers in a Fleeting Dream hit → 1 Volatile Note – Winds (blue)
- Murmurs in a Haunting Dream hit → 1 Volatile Note – Winds (blue)
- Echo Skill cast / Intro Skill / Inherent Skill – Accidental → 1 Volatile Note – Cadenza (multicolored)

**Scarlet Coda (Enhanced Heavy Attack):** When 6 Volatile Notes are collected AND Phrolova is in Compose state AND is NOT in Resolving Chord state, Heavy Attack becomes Scarlet Coda.
- Deals Havoc DMG to nearby targets (Stagnation + pull-in)
- Considered both Resonance Skill DMG and Echo Skill DMG
- Each stack of Aftersound increases the DMG multiplier of Scarlet Coda
- Has a 25-second cooldown (Compose state cooldown)

**Liberation Interaction:** After Scarlet Coda, the Resolving Chord state is active. Resonance Liberation (Waltz of Forsaken Depths) becomes available for 25 seconds. Casting it at this point will enter Maestro state.

**Forte Liberation Modes:** The ratio of red to blue notes determines which animation variant plays:
- More red notes → Phrolova's crying animation during Liberation
- More blue notes → Phrolova's laughing-in-madness animation during Liberation

**Forte Circuit Attribute Scaling (Scarlet Coda, estimated Level 1 → Level 10):**

| Level | Scarlet Coda Base Multiplier | Aftersound per Stack Bonus |
|-------|------------------------------|----------------------------|
| 1     | ~150%                        | 0.5%                       |
| 5     | ~200%                        | 0.65%                      |
| 10    | ~300%+                       | 1.0% (approx)              |

*Aftersound-scaled portion makes this highly variable; consult in-game values for precision.*

## Phrolova Inherent Skill 1: Cadenza Conversion
Casting Scarlet Coda (Suite of Doom), Suite of Immortality (post-Maestro enhanced Basic), or Echo Skill converts the next Volatile Note acquired into a Volatile Note – Cadenza.

This incentivizes using Echo Skills frequently to maximize Cadenza notes on the Forte bar, since Cadenza and Strings deal equal damage and Cadenza has the additional control effect of Stagnation + Pull combined.

## Phrolova Inherent Skill 2: Lingering Note Buff
Upon entering combat, Phrolova immediately gains 8 stacks of Aftersound (Lingering Note). This effect cannot be triggered again within 1 second after exiting combat.

- Each stack of Aftersound grants +2.5% Crit DMG (up to 24 stacks = +60% Crit DMG baseline)
- Each stack beyond max 24 grants +1% Crit DMG, up to an additional +100%
- Aftersound stacks are cleared when Maestro state ends (via Curtain Call or switching to Phrolova)

## Phrolova Intro Skill: Song of Immortality
Phrolova enters from off-field, attacking the target and dealing Havoc DMG. Casting this skill sends Phrolova into Reincarnate state, immediately enabling access to her Enhanced Basic Attack or Enhanced Resonance Skill.

Casting the Intro Skill also grants 1 Volatile Note – Cadenza, incentivizing an immediate swap-in for note management.

## Phrolova Outro Skill: Requiem Without End
The next incoming Resonator has their **Havoc DMG Amplified by 20%** and **Heavy Attack DMG Amplified by 25%** for 14 seconds, or until they are switched out.

This Outro is particularly powerful for teammates who deal significant Heavy Attack DMG (Roccia, Danjin, Augusta, Galbrena) or Havoc DMG in general. It effectively makes Phrolova an excellent quasi-support even during her rotation's off-phase.

---

## Phrolova: Forte Materials Costs
Full Forte upgrade (all skills Lv.1 → Lv.10):

- **Lento Helix / Adagio Helix / Andante Helix / Presto Helix** (Forgery Challenge drops — Rinascita Forgery Challenges recommended for passive Polygon Core collection):
  - Lento Helix: ~25 total
  - Adagio Helix: ~28 total
  - Andante Helix: ~40 total
  - Presto Helix: ~57 total
- **Netherworld's Stare** (Weekly Boss drop — "Beyond the Crimson Curtain" challenge; Hecate Boss in Ragunna City lighthouse area): ~25 total
- **LF / MF / HF / FF Polygon Core** (enemy drops; HF and FF synthesizable):
  - LF Polygon Core: ~25 total
  - MF Polygon Core: ~28 total
  - HF Polygon Core: ~55 total
  - FF Polygon Core: ~67 total
- **Shell Credits:** 2,030,000 total for full Forte upgrade (all talents to max)

---

## Phrolova: Resonance Chains (Sequence Nodes)

## Phrolova Resonance Chain S1: A Melody for the Lost
The DMG Multiplier of **Movement of Fate and Finality** is increased by **80%**.
The DMG Multiplier of **Murmurs in a Haunting Dream** is increased by **80%**.

If Phrolova has fewer than 2 Volatile Notes when she is not in the Maestro state and stays out of combat for 4 seconds, she gains Volatile Note – Cadenza until she has at least 2 Volatile Notes.

*Impact: Significant damage increase to core Enhanced Basic and Enhanced Resonance Skill attacks. The passive note recovery reduces the ramp-up cost between rotations.*

## Phrolova Resonance Chain S2: A Dirge of Bygone Days
The DMG Multiplier of **Scarlet Coda** is increased by **75%**. Aftersound now **additionally** increases the DMG Multiplier of Scarlet Coda by **75%** per stack. Casting Scarlet Coda grants **14 stacks of Aftersound**.

*Impact: Widely considered the strongest S2 in Wuthering Waves as of Version 2.8. It provides a massive independent multiplier zone (totaling ~150% additional Scarlet Coda scaling), dramatically accelerates Aftersound stacking — granting 14 stacks from a single cast, equivalent to nearly instant full Crit DMG loading — and dramatically compresses the warm-up period to reach optimal Aftersound performance. Combined with S1, it creates one of the most powerful S1+S2 combo upgrades in the game. Rated S-Tier by community sources.*

## Phrolova Resonance Chain S3: An Echo That Fades Not
**Echo Skill DMG is Amplified by 80%.** Casting Scarlet Coda will convert all Volatile Notes on the bar to Volatile Notes – Cadenza in turn. Targets hit by Enhanced Attack – Hecate: Cadenza will have their **ATK reduced by 20%** for 15 seconds.

*Impact: Provides a permanent damage amplification multiplier on all Echo Skill DMG — which includes Scarlet Coda and Hecate's off-field enhanced attacks. The mass Cadenza conversion ensures optimal note composition every rotation. The ATK reduction on targets hit by Cadenza Enhanced Attacks adds defensive/debuff utility. Impact is stronger in longer fights with more rotation cycles.*

## Phrolova Resonance Chain S4: A Torch Illuminating the Path
Casting **Echo Skill** grants **20% Attribute DMG Bonus** for all Resonators in the team for **30 seconds**.

*Impact: Straightforward team-wide 20% DMG Bonus on Echo Skill use — a quality buff for the whole team since Phrolova's rotation naturally involves frequent Echo Skill casts. Primarily a support node. Lower personal value but strong in coordinated team contexts.*

## Phrolova Resonance Chain S5: A Forked Road in Fate's Heartland
Upon entering the **Maestro state**, generate a field to **Stagnate** nearby targets for 4 seconds. The Stagnation effect ends if Phrolova leaves the Maestro state or switches to another Resonator. **Damage taken during the Maestro state is reduced by 30%**.

*Impact: Adds burst entry crowd control (AoE Stagnate on Liberation cast — extremely useful in Whimpering Wastes and Tower of Adversity), plus meaningful personal survivability during the floating off-field Maestro phase. Primarily a quality-of-life and defensive node. Lower raw damage value.*

## Phrolova Resonance Chain S6: A Night to Depart From Eternal Rest
The DMG Multiplier of **Enhanced Attack – Hecate** is increased by **24%**.

During Movement of Fate and Finality and Murmurs in a Haunting Dream, command Hecate to cast 1 **Apparition of Beyond – Hecate**, dealing Havoc DMG equal to **216.42% of Phrolova's ATK** (considered Echo Skill DMG) and granting **8 stacks of Aftersound** on hit.

If Phrolova is **NOT** the active Resonator during the Maestro state: targets take **40% more DMG** from Hecate and Phrolova.
If Phrolova **IS** the active Resonator during the Maestro state: gain **60% Havoc DMG Bonus**.

*Impact: The ultimate heavy-spender node. Three major effects: (1) flat +24% to all Hecate Enhanced Attack multipliers — directly boosting the core off-field damage engine; (2) two additional off-field Apparition instances at 216.42% ATK each during on-field Enhanced skill casts, each granting 8 Aftersound stacks — dramatically increasing both on-field damage and Aftersound stack count; (3) a powerful conditional buff (60% Havoc DMG on-field or 40% DMG amplification off-field) that essentially rewards both playstyles. This node is stronger over longer fights with more rotations. Prydwen DPS calculation shows S6 Phrolova at 287.4% performance relative to S0 baseline (219.4% more damage).*

**Resonance Chain Priority:** S2 → S3 → S6

---
## Sources
- Wuthering Waves Fandom Wiki – Phrolova/Combat: https://wutheringwaves.fandom.com/wiki/Phrolova
- Prydwen.gg – Phrolova Guide and Build: https://www.prydwen.gg/wuthering-waves/characters/phrolova/
- Game8.co – Phrolova Best Builds and Teams: https://game8.co/games/Wuthering-Waves/archives/524877
- Wutheringlab.com – Phrolova Build: https://wutheringlab.com/character/phrolova-build/
- Wuthering.gg – Phrolova Build and Info: https://wuthering.gg/characters/phrolova
- LDShop.gg – Phrolova Build Guide: https://www.ldshop.gg/blog/guide/phrolova-build-wuthering-waves.html
- LootBar.gg – Phrolova Kit and Resonance Chains Revealed: https://lootbar.gg/blog/en/wuthering-waves-phrolova-kit.html
- Sportskeeda – Phrolova Resonance Chain Guide: https://www.sportskeeda.com/esports/wuthering-waves-wuwa-phrolova-resonance-chain-guide
- XboxPlay.games – All Phrolova Resonance Chains: https://xboxplay.games/wuthering-waves/all-wuthering-waves-phrolova-resonance-chains-65914
- LDShop.gg – S2 Value Tier List: https://www.ldshop.gg/blog/wuthering-waves/s2-value-tier-list.html
- Esports.gg – Phrolova Ascension Materials Guide: https://esports.gg/guides/wuthering-waves/phrolova-ascension-materials-guide/
- Game8.co – Phrolova Ascension Materials: https://game8.co/games/Wuthering-Waves/archives/537878