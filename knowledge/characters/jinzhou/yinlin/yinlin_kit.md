---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/huanglong/yinlin/yinlin_kit.md
character: Yinlin
group: Huanglong / Jinzhou
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - electro
  - rectifier
  - sub-dps
  - off-field
  - coordinated-attack
  - punishment-mark
  - buffer
---

# Yinlin Kit Documentation
<!-- Sources: https://wuthering.gg/characters/yinlin, https://www.prydwen.gg/wuthering-waves/characters/yinlin/, https://wutheringlab.com/character/yinlin-build/, https://game8.co/games/Wuthering-Waves/archives/454218, https://wutheringwaves.gg/yinlin-guide/ -->

## Yinlin: Combat Archetype and Role

- **Element:** Electro
- **Weapon Type:** Rectifier
- **Role:** Sub-DPS — off-field Punishment Mark damage dealer and Electro buffer
- **Archetype:** Mark-application specialist; Coordinated Attack off-field DPS; Electro Liberation amplifier
- **Introduced:** Version 1.1 (first half); banner alongside Jinhsi

Yinlin is the premier Electro Sub-DPS in Wuthering Waves — a character who front-loads her entire value into a tight on-field burst window, then exits the field to deal sustained Electro Coordinated Attacks passively while the Main DPS operates. Her kit revolves around a two-tier mark system: **Sinner's Mark** (applied during her on-field phase) upgrades to **Punishment Mark** (via her Forte Heavy Attack), which then autonomously triggers **Judgment Strike** — a repeating Coordinated Electro attack that fires once per second on any marked enemy that is hit — for the full 18-second duration of the mark, entirely without Yinlin being present. Her Outro Skill delivers one of the strongest offensive buffs in the game: +20% Electro DMG Amplification and +25% Resonance Liberation DMG Amplification, making her the mandatory pair for Electro Liberation-focused Main DPS characters like Calcharo and Xiangli Yao. As of Version 1.1–1.x, Yinlin is effectively synonymous with the optimal Electro team archetype.

## Yinlin: Key Resources (Forte Mechanics Overview)

Yinlin's Forte Circuit is governed by three interacting systems that must be executed in the correct sequence: **Judgment Points** (her Forte gauge, 0–100), **Sinner's Mark** (the initial enemy debuff), and **Punishment Mark** (the upgraded debuff that triggers autonomous off-field Coordinated Attacks).

**Judgment Points (0–100)**
- Accumulated by: Intro Skill cast, Basic Attack Zapstring's Dance hits, Resonance Skill Magnetic Roar cast, Resonance Skill Electromagnetic Blast hits, Resonance Skill Lightning Execution cast
- At 100 Judgment Points: Heavy Attack input is replaced by **Chameleon Cipher**

**Sinner's Mark (Enemy Debuff — Prerequisite)**
- Applied by: Basic Attack Zapstring's Dance on hit, Resonance Liberation Thundering Wrath on hit, Intro Skill Roaring Storm on hit
- Duration: **Infinite** — Sinner's Mark does not expire over time; it is removed only when Yinlin leaves the field OR when Chameleon Cipher converts it to Punishment Mark
- Sinner's Mark has no damage component of its own; it enables Electromagnetic Blast (multi-target Electro hit that hits all Sinner's-Marked enemies simultaneously) and is a prerequisite for Punishment Mark conversion
- **Critical rule:** Chameleon Cipher must hit a Sinner's-Marked target to produce Punishment Mark; if no marks exist when Chameleon Cipher is cast, no Punishment Marks are created

**Chameleon Cipher (Heavy Attack at 100 Judgment Points)**
- Consumes all 100 Judgment Points; deals Electro DMG to the target
- If it hits a target bearing Sinner's Mark: that Sinner's Mark is converted to **Punishment Mark** (duration: 18 seconds)
- Deals Heavy Attack damage type; can be swap-canceled to shorten the long animation without canceling the mark conversion

**Punishment Mark (Off-Field Coordinated Attack Engine)**
- Duration: 18 seconds from application
- Mechanic: Whenever any team member deals damage to a Punishment-Marked enemy, **Judgment Strike** is triggered — a Coordinated Electro Attack that hits all Punishment-Marked enemies simultaneously
- Trigger rate: **Once per second** (internal cooldown of 1s)
- Judgment Strike deals Resonance Skill DMG (benefits from Resonance Skill DMG Bonus)
- Crucially: Yinlin does **not** need to be on the field for Judgment Strike to trigger; any damage from any teammate that hits the marked enemy activates it
- Punishment Mark persists through Yinlin's absence; it is the primary source of her off-field value

## Yinlin Forte Circuit: Judgment Points, Marks, and Execution Mode

**Standard Mark Application Sequence (Full Rotation Entry)**
1. Intro Skill Roaring Storm → applies Sinner's Mark on hit; grants Judgment Points
2. Resonance Liberation Thundering Wrath → applies Sinner's Mark to all nearby enemies; bonus damage to already-marked targets
3. Resonance Skill: Magnetic Roar → enters **Execution Mode** (10s); grants Judgment Points
4. Execution Mode: Basic Attacks (up to 4 stages) → each stage triggers **Electromagnetic Blast** on all Sinner's-Marked enemies (Electro DMG); grants Judgment Points per hit
5. Resonance Skill: Lightning Execution (follow-up after Magnetic Roar) → AoE Electro nuke; grants Judgment Points; deals +10% DMG to Sinner's-Marked targets (Inherent Skill 1 interaction)
6. At 100 Judgment Points → cast Chameleon Cipher (Heavy Attack) → converts all Sinner's Marks to Punishment Marks → swap to Main DPS

**Execution Mode Detail**
- Triggered by Resonance Skill Magnetic Roar; lasts 10 seconds or until Yinlin swaps / another Skill is used
- During Execution Mode: each Basic Attack stage and Dodge Counter triggers one instance of **Electromagnetic Blast**
- Electromagnetic Blast: hits all targets currently bearing Sinner's Mark simultaneously; deals Electro DMG; generates Judgment Points and Resonance Energy
- Maximum of 4 Electromagnetic Blast triggers per Execution Mode window (one per Basic Attack stage)

**Judgment Points Generation Summary**
- Intro Skill: +30 Judgment Points flat on cast
- Basic Attack hit (per hit, in Execution Mode generating Electromagnetic Blast): Judgment Points gained per stage
- Magnetic Roar cast: Judgment Points gained
- Electromagnetic Blast hit: Judgment Points gained
- Lightning Execution cast: Judgment Points gained
- **Full rotation from 0:** Intro (+30) → Magnetic Roar + Basic Attacks → Lightning Execution → reaches 100 within one standard on-field rotation

**Key Rotation Rule**
- Liberation should be cast before Chameleon Cipher to maximize the number of enemies bearing Sinner's Mark when the mark conversion fires — Liberation applies Sinner's Mark to all nearby enemies simultaneously
- If all enemies die before Chameleon Cipher is used, Sinner's Marks reset on Yinlin's next entry; reapply them before using Chameleon Cipher again or no Punishment Marks will be created

## Yinlin: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | ~810 | ~36 | ~90 |
| Lv. 20 | ~2,100 | ~93 | ~234 |
| Lv. 40 | ~4,000 | ~177 | ~446 |
| Lv. 60 | ~6,460 | ~286 | ~720 |
| Lv. 80 | ~8,890 | ~394 | ~991 |
| Lv. 90 | ~10,120 | ~449 | ~1,128 |

*Note: Approximate figures before Forte Attribute Bonuses and equipment. Verify exact values with the Wuthering Waves Fandom Wiki.*

## Yinlin: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | LF Howler Core ×4, Coriolus ×4, Shell Credits ×5,000 |
| 2 | 40→50 | MF Howler Core ×4, Coriolus ×8, Shell Credits ×10,000 |
| 3 | 50→60 | HF Howler Core ×8, Coriolus ×12, Roaring Rock Fist ×4, Shell Credits ×15,000 |
| 4 | 60→70 | HF Howler Core ×8, Coriolus ×16, Roaring Rock Fist ×8, Shell Credits ×20,000 |
| 5 | 70→80 | FF Howler Core ×12, Coriolus ×20, Roaring Rock Fist ×12, Shell Credits ×40,000 |
| 6 | 80→90 | FF Howler Core ×12, Coriolus ×24, Roaring Rock Fist ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Howler Cores (LF/MF/HF/FF):** Dropped by Whisperin Tacet Discord enemies throughout the map; craftable via Synthesizer
- **Coriolus:** Local specialty plant; gathered from the overworld — Prydwen's guide recommends using the Interactive Map to locate clusters quickly
- **Roaring Rock Fist:** Dropped by Thundering Mephis boss — the large Electro variant of the Mephis enemy type found in Huanglong's storm zones

## Yinlin: Character Kit: Basic Attack — Zapstring's Dance

**Standard Ground Chain (4 stages)**
- Yinlin directs Zapstring through up to 4 attack stages, each dealing Electro DMG
- Applies **Sinner's Mark** to hit targets
- Generates **Judgment Points** per hit
- Each stage in **Execution Mode** additionally triggers one **Electromagnetic Blast** (hits all Sinner's-Marked enemies with Electro DMG)
- In standard Sub-DPS play, Basic Attacks are used primarily as Judgment Point generators during the on-field window, not as primary damage dealers

**Heavy Attack**
- Consumes Stamina; Zapstring deals Electro DMG
- At 100 Judgment Points: replaced by **Chameleon Cipher** (see Forte Circuit section)

**Mid-Air Attack:** Zapstring plunges, dealing Electro DMG; Stamina cost

**Dodge Counter:** Electro DMG after successful Dodge; counts as a Basic Attack stage for Electromagnetic Blast triggering during Execution Mode

**S6 Interaction — Furious Thunder**
In the 30s after casting Liberation Thundering Wrath, each Basic Attack hit additionally triggers **Furious Thunder** (419.59% ATK Electro DMG, counted as Resonance Skill DMG; up to 4 triggers). This transforms Yinlin's post-Liberation Basic Attacks from Judgment Point generators into significant damage events — the primary reason S6 enables Yinlin as a Main DPS.

## Yinlin: Character Kit: Resonance Skill — Magnetic Roar / Lightning Execution / Electromagnetic Blast

Yinlin's Resonance Skill has three distinct components that interact with each other:

**Magnetic Roar (First Press)**
- Zapstring deals Electro DMG to the target
- Enters **Execution Mode** for 10 seconds
- Generates Judgment Points on cast
- In Execution Mode: each Basic Attack and Dodge Counter stage triggers one Electromagnetic Blast (max 4 times total during Execution Mode window)

**Electromagnetic Blast (Execution Mode Passive Trigger)**
- Fires automatically on each Basic Attack / Dodge Counter stage during Execution Mode
- Hits all targets currently bearing Sinner's Mark with Electro DMG simultaneously — excellent AoE value
- Generates additional Judgment Points per hit
- S2 enhancement: each Electromagnetic Blast hit also restores 5 additional Judgment Points and 5 Resonance Energy

**Lightning Execution (Second Skill Press — Follow-up)**
- Available after casting Magnetic Roar; must be used within a time window or it goes on cooldown if Yinlin is switched
- Deals AoE Electro DMG to all enemies in range
- Generates Judgment Points on cast
- Inherent Skill 1: Deals +10% DMG to Sinner's-Marked targets; grants Yinlin +10% ATK for 4s on trigger

**Skill Priority Note:** The standard rotation uses Magnetic Roar → Basic Attack chain (Electromagnetic Blasts) → Lightning Execution in sequence. Lightning Execution should not be used before Magnetic Roar, as Execution Mode has not been entered yet.

## Yinlin: Character Kit: Resonance Liberation — Thundering Wrath

- **Activation:** Commands Zapstring to call for thunder across a wide area, dealing Electro DMG to all nearby targets
- **Sinner's Mark Application:** Applies Sinner's Mark to all hit targets — this is the most efficient mass Sinner's Mark application in Yinlin's kit; using Liberation before Chameleon Cipher ensures maximum enemy coverage for Punishment Mark conversion
- **Bonus Damage to Marked Targets:** Inherent Skill 2 causes Liberation to deal **+100% extra DMG** to any targets already bearing Sinner's Mark or Punishment Mark — the ideal sequence enters with Intro Skill (applying Sinner's Mark to one target), then casts Liberation (which hits the already-marked target for double damage while also marking everything else)
- **Cooldown:** 20 seconds
- **Resonance Energy Cost:** 125
- **Concerto Generation:** 20 per cast

## Yinlin: Inherent Passives

**Inherent Skill 1 — Eye of the Storm**
- When Resonance Skill **Lightning Execution** hits a target with Sinner's Mark: Lightning Execution deals **+10% DMG** and Yinlin's ATK is increased by **+10%** for 4 seconds
- Both effects activate simultaneously, incentivizing correct skill sequencing (Magnetic Roar → Basic Attacks → Lightning Execution with marks pre-applied)

**Inherent Skill 2 — Thunderous Judgment (combined name for Liberation and Judgment Strike interactions)**
- **Liberation Component:** Resonance Liberation Thundering Wrath deals **+100% extra DMG** to targets already bearing Sinner's Mark or Punishment Mark — making Liberation nearly always deal double its listed damage against already-processed targets in a smooth rotation
- **Judgment Strike Component:** When Forte Circuit Judgment Strike hits a target, all team members' **ATK is increased by +20%** for **12 seconds** — this fires every time Judgment Strike triggers (once per second off-field), effectively maintaining near-permanent +20% ATK for the entire team while Punishment Marks are active

## Yinlin: Intro/Outro Skills

**Intro Skill — Roaring Storm**
- Triggered when Yinlin enters the field via swap
- Zapstring dashes forward and attacks the target, dealing Electro DMG
- Applies **Sinner's Mark** to the target on hit
- Generates **+30 Judgment Points** flat on cast — the single largest per-event Judgment Point gain; makes entering via Intro Skill the optimal rotation start, as it immediately advances the Forte gauge by 30% of the cap
- This is why Yinlin's rotation is designed around receiving a swap-in: the Intro's combined Sinner's Mark application and Judgment Point generation provides the fastest path to Chameleon Cipher

**Outro Skill — Tacit Exchange**
- Triggered when Yinlin swaps off-field (Concerto Energy full)
- The incoming Resonator gains:
  - **+20% Electro DMG Amplification** for 14 seconds (or until they swap out)
  - **+25% Resonance Liberation DMG Amplification** for 14 seconds (or until they swap out)
- This is one of the strongest Outro buffs in the game — it amplifies both the element and the damage type most relevant to Electro Liberation DPS characters (Calcharo, Xiangli Yao)
- The Liberation DMG Amplification component makes Yinlin the mandatory partner for any Main DPS whose primary damage source is their Resonance Liberation

## Yinlin: Skill Upgrade Materials

| Skill Level | Key Materials |
|-------------|---------------|
| 1→2 | Whisperin Core ×4, Lv.1 Skill Book ×4, Shell Credits ×1,000 |
| 2→3 | Whisperin Core ×4, Lv.2 Skill Book ×4, Shell Credits ×3,000 |
| 3→4 | Whisperin Core ×8, Lv.3 Skill Book ×8, Shell Credits ×8,000 |
| 4→5 | Whisperin Core ×12, Weekly Boss Material ×2, Lv.4 Skill Book ×4, Shell Credits ×20,000 |
| 5→6 | Whisperin Core ×16, Weekly Boss Material ×3, Lv.4 Skill Book ×4, Shell Credits ×40,000 |
| 6→7 | Whisperin Core ×20, Weekly Boss Material ×5, Lv.4 Skill Book ×8, Shell Credits ×80,000 |
| 7→8 | Whisperin Core ×24, Weekly Boss Material ×8, Lv.4 Skill Book ×8, Shell Credits ×120,000 |
| 8→9 | Whisperin Core ×28, Weekly Boss Material ×12, Lv.4 Skill Book ×16, Shell Credits ×160,000 |
| 9→10 | Whisperin Core ×40, Weekly Boss Material ×16, Lv.4 Skill Book ×16, Shell Credits ×200,000 |

**Total Forte Shell Credits (all skills):** ~2,030,000
- **Skill Books (Rectifier Forgery):** Rectifier Forgery Challenge rewards
- **Weekly Boss Material:** Verify exact drop and boss name with the Fandom Wiki — sourced from a Version 1.x weekly boss
- **Whisperin Cores:** Whisperin Tacet Discord enemy drops throughout the map

**Skill Upgrade Priority:** Forte Circuit (Judgment Strike multiplier) = Resonance Skill (Magnetic Roar / Lightning Execution / Electromagnetic Blast) → Resonance Liberation → Basic Attack → Intro Skill

## Yinlin: Resonance Chains (Sequences)

**S1 — Ensnarled by Rapport**
- When Resonance Skill **Lightning Execution** hits a target, Yinlin's **CRIT Rate increases by +8%**
- *Impact:* Reduces CRIT Rate investment pressure on Echoes and sub-stats; approximately +5–8% personal DPS increase. The trigger fires every time Lightning Execution is used correctly. Solid first sequence but modest; does not alter rotation.

**S2 — Devoted Fervor**
- Resonance Skill **Electromagnetic Blast** additionally restores **5 Judgment Points** and **5 Resonance Energy** on hit
- *Impact:* Four Electromagnetic Blast procs in a single Execution Mode window = +20 Judgment Points and +20 Resonance Energy. This meaningfully reduces the time needed to reach 100 Judgment Points AND helps with Liberation uptime — two of Yinlin's most important resource constraints simultaneously. Approximately +8–12% overall DPS increase through faster rotation cycling. High practical value.

**S3 — Righteous Pursuit**
- Resonance Skill Magnetic Roar and Lightning Execution deal **+70% more DMG**
- *Impact:* A flat multiplier amplification on both components of the two-part Resonance Skill. Both deal Electro DMG directly; the +70% applies to meaningful base multipliers. Approximately +15–20% personal DPS increase. One of the largest single-sequence DPS gains for Yinlin.

**S4 — Steadfast Conviction**
- When Forte Circuit **Judgment Strike** hits a target, all team members' **ATK increases by +20%** for **12 seconds**
- *Impact:* Judgment Strike fires once per second while Punishment Marks are active on-field. The 12-second duration means this buff is effectively permanent during the Main DPS's field window after Yinlin rotates out. This was later promoted to an Inherent Passive effect in updated game versions — cross-reference the Fandom Wiki to confirm whether S4 or Inherent Skill 2 currently holds this effect. Approximately +10–15% team DPS increase.

**S5 — Resounding Will**
- Resonance Liberation **Thundering Wrath** deals **+100% extra DMG** to targets with Sinner's Mark or Punishment Mark
- *Impact:* This was similarly promoted to Inherent Skill in updated game versions — verify current placement with the Fandom Wiki. If still a sequence: effectively doubles Liberation damage against pre-marked targets, which covers all enemies in a properly executed rotation. Approximately +15–20% personal DPS increase.

**S6 — Pursuit of Justice**
- In the **first 30 seconds** after casting Resonance Liberation Thundering Wrath: each Basic Attack hit triggers **Furious Thunder**, dealing Electro DMG equal to **419.59% of Yinlin's ATK** (counted as Resonance Skill DMG)
- Furious Thunder triggers once per Basic Attack hit; up to **4 times total** per 30-second window
- Maximum Furious Thunder damage per Liberation cycle: 4 × 419.59% ATK = **1,678.36% ATK** Electro DMG (Resonance Skill type), spread across 4 hits
- *Impact:* Transforms Yinlin's post-Liberation Basic Attacks from incidental resource generation into major damage events. Unlocks Yinlin as a legitimate Main DPS option by giving her enormous on-field output within the Liberation window. Approximately +31% overall DPS increase — the largest single-sequence gain in her chain. Full S6 Yinlin is referenced by Wutheringlab as approaching the damage output of a S0+1 limited DPS character.

**Sequence Pull Priority:** S3 (largest single DPS gain for personal damage) and S6 (Main DPS unlock) are the standout sequences. For Sub-DPS role, S2 (rotation speed) and S3 are most impactful. Full S6 investment is recommended only for players who wish to run Yinlin as a primary carry.

## Yinlin: Recommended Echo Sets

**Best-in-Slot (Sub-DPS): Void Thunder (5-piece) — Thundering Mephis**
- Void Thunder's 5-piece provides Electro DMG Bonus that multiplies with Judgment Strike's Resonance Skill typing and all of Yinlin's Electro abilities
- **Main Echo: Thundering Mephis** — transforms into the Mephis boss; claw multi-hit deals Electro DMG; on completion, grants the current Resonator **+10% Electro DMG Bonus** and **+10% Heavy Attack DMG Bonus** for 15 seconds; both bonuses are relevant: the Electro DMG buff applies to Judgment Strike, and the Heavy Attack DMG buff applies to Chameleon Cipher
- The Mephis Echo can be swap-canceled after the claw animation begins (before full completion) for faster execution at the cost of the buff — maintaining the buff by waiting for the full animation is recommended for damage

**Best-in-Slot (Buffer / Moonlit Support): Moonlit Clouds (5-piece) — Impermanence Heron**
- Used when Yinlin's primary value is her Outro buff rather than personal damage
- Moonlit Clouds 4-piece bonus: when Resonator casts Outro Skill, the incoming character gains +22.5% ATK for 15 seconds — stacking on top of Yinlin's +20% Electro DMG Outro Amplification for the Main DPS
- **Main Echo: Impermanence Heron** — generates additional Resonance Energy on cast; useful for maintaining Thundering Wrath cooldown; provides ATK buff to the team
- Requires nearly perfect rotation execution to outperform Void Thunder in total team DPS; recommended only for advanced players in premium team compositions with Calcharo or Xiangli Yao

**Echo Main Stats Priority**
- 4-Cost Echo (Mephis or Heron): CRIT Rate or CRIT DMG (whichever completes 1:2 ratio)
- 3-Cost Echoes (×2): Electro DMG Bonus (primary) or ATK% (secondary); double Electro DMG Bonus preferred
- 1-Cost Echoes: ATK% (sub-stats outweigh main stats at this cost tier)

**Sub-Stat Priority:** Energy Regen (to 120–130% breakpoint, estimated in Xiangli Yao + Shorekeeper team) ≥ CRIT Rate = CRIT DMG > ATK% > Flat ATK = Resonance Skill DMG Bonus

## Yinlin: Best Weapon

**Signature — Stringmaster (5-Star Rectifier)**
- Best-in-slot by a meaningful margin; purpose-built for Yinlin's kit
- **Stat:** CRIT Rate — highly efficient; reduces CRIT Rate sub-stat pressure
- **Effect:**
  - Unconditional **+12% All DMG Bonus**
  - When dealing Resonance Skill DMG: ATK increases by **+12%** (stacks up to **2 times**, lasting 5 seconds) — Judgment Strike (Resonance Skill type) and Electromagnetic Blast trigger this on nearly every proc
  - When Yinlin is **off-field**: ATK is additionally increased by **+12%** — dramatically amplifies her damage during the Punishment Mark phase where she is not the active character; this off-field bonus is the primary reason Stringmaster is so well-suited to a Sub-DPS rotation

**Best Standard 5-Star — Cosmic Ripples**
- Available on the standard banner; strong long-term option
- Provides ATK stat + Energy Regen passive — reduces ER investment needed on Echo sub-stats; a notable build-efficiency gain
- Underperforms Stringmaster but outperforms all 4-star options by a meaningful margin

**Best 4-Star — Augment**
- CRIT Rate main stat (significant value at higher refinements)
- Passive: ATK% bonus while Resonance Liberation is active — fires during the liberation burst window when Yinlin's damage is highest
- Clearly superior to other 4-star Rectifiers; accessible via in-game event and gacha sources

**Secondary 4-Star — Jinzhou Keeper**
- Decent alternative at higher refinements; falls behind Augment at lower refinement levels
- Worth using if Augment is unavailable

**F2P Option — Rectifier of Night**
- 3-star baseline weapon; use until a 4-star or better is available
- Does not approach the performance of any recommended 4-star option; replace as soon as possible

## Yinlin: Best Teams

**Premium Sub-DPS — Yinlin / Calcharo / Verina**
- **Yinlin** (Sub-DPS / Buffer): Applies Punishment Marks; Outro buffs Calcharo with +20% Electro DMG + 25% Liberation DMG Amplification
- **Calcharo** (Main DPS): The primary beneficiary of Yinlin's Outro; his Resonance Liberation (Death Messenger state) generates most of his damage and scales directly with both Electro DMG and Liberation DMG Amplification from Yinlin's Outro; Yinlin's Judgment Strike also fills AoE gaps in his single-target focus
- **Verina** (Support/Healer): Universal healer at Version 1.x launch; +20% ATK buff from Liberation stacks with Yinlin's team ATK buff from Judgment Strike; sustain ensures survivability during rotation windows
- *Rotation:* Verina Liberation + Outro → Yinlin Intro → Liberation (marks all enemies) → Magnetic Roar → Electromagnetic Blast Basic chain → Lightning Execution → Chameleon Cipher (Punishment Mark) → Outro → Calcharo Intro → Death Messenger Liberation burst (receives both Outro buffs and Punishment Mark Judgment Strike procs throughout)

**Standard Premium — Yinlin / Xiangli Yao / Shorekeeper**
- **Yinlin** (Sub-DPS / Buffer): Same mark cycle; Outro now feeds Xiangli Yao
- **Xiangli Yao** (Main DPS): Free Limited 5-star Electro character released Version 1.3; his Resonance Liberation (Intuition state) benefits from both Electro DMG and Liberation DMG Amplification; Yinlin's Judgment Strike augments his single-target damage with multi-target Electro procs; Prydwen notes this pairing is *"easy to use, effective, and natural"*
- **Shorekeeper** (Support): CRIT Rate and CRIT DMG Stellarealm buff for both DPS characters; Verina alternative with stronger CRIT scaling; recommended over Verina in most Xiangli Yao compositions
- *Note:* Prydwen explicitly recommends this team for Xiangli Yao optimization, noting that stacking Verina + Yinlin Outros before his Liberation is *"very potent"*

**Non-Electro Utility — Yinlin / Jinhsi / Healer**
- **Yinlin** in Jinhsi compositions: Punishment Mark Judgment Strikes count as Coordinated Attacks from Yinlin's Eras in Unity interaction — contributing Electro-type Incandescence stacks for Jinhsi; the Electro Outro buff does not help Jinhsi directly, but the Coordinated Attack frequency adds meaningful Incandescence generation alongside a Spectro Coordinated Attack character
- **Best use case:** Jinhsi teams where a second coordinated-attack Spectro character is unavailable; the Incandescence contribution is lower than a native Spectro pairing but functional

**Budget — Yinlin / Rover (Havoc) / Baizhi**
- **Yinlin** (Sub-DPS): Mark cycle and off-field Judgment Strike; Outro is less efficiently used without an Electro or Liberation-focused Main DPS
- **Rover (Havoc)** (Main DPS): Strong Basic Attack DPS in Dark Surge state; does not benefit from Electro DMG Outro but does trigger Judgment Strike procs via sustained dark-surge attacks
- **Baizhi** (Support/Healer): F2P best healer; provides ATK buff and healing
- *Limitation:* This team does not exploit Yinlin's Outro buff fully; it is a functional composition for players without Calcharo or Xiangli Yao but meaningfully below her optimal pairing DPS ceiling

## Yinlin: DPS Benchmarks

- Yinlin is rated as an S-tier Sub-DPS for the entirety of Version 1.x and into Version 2.x, remaining highly relevant due to the strength of her Outro Skill and the absence of a direct Electro Sub-DPS replacement with equivalent buff value
- Her personal damage contribution (on-field Skill combos + off-field Judgment Strike + Liberation) accounts for a meaningful share of team DPS in Calcharo and Xiangli Yao compositions, even without field time after the rotation is established
- Wutheringlab notes that Resonance Skill DMG constitutes approximately **50% of her total damage** due to the Punishment Mark / Judgment Strike classification as Resonance Skill DMG — making Skill DMG Bonus a relevant sub-stat for invested players
- At S0 with Stringmaster, in a Calcharo or Xiangli Yao premium team, Yinlin's Punishment Mark Judgment Strikes proc reliably every second, and her Outro's dual Electro DMG + Liberation DMG Amplification represents a team DPS increase that no other character in Version 1.x matches for the same archetype
- At S6, Yinlin becomes viable as a Main DPS: the Furious Thunder 419.59% × 4 procs (1,678.36% ATK Electro Skill DMG per Liberation cycle) in addition to her standard rotation creates output comparable to S0 limited DPS characters
- **Primary operational constraint:** Her Punishment Mark disappears if Yinlin leaves the field before Chameleon Cipher is cast, or if the enemy dies and she re-enters without reapplying Sinner's Mark; rotation discipline around mark application is the main skill requirement

## Yinlin: Sources

- Wuthering.gg — Yinlin kit, Forte mechanics, full skill descriptions: https://wuthering.gg/characters/yinlin
- Prydwen Institute — Yinlin build guide, team analysis, sub-stat priorities: https://www.prydwen.gg/wuthering-waves/characters/yinlin/
- Wutheringlab — Yinlin build, rotation, Forte breakdown: https://wutheringlab.com/character/yinlin-build/
- Game8 — Yinlin best builds, teams, skill priority, combos: https://game8.co/games/Wuthering-Waves/archives/454218
- WutheringWaves.gg — Yinlin guide (builds, rotations, echo tier list): https://wutheringwaves.gg/yinlin-guide/
- GamesRadar — Yinlin build guide including sequence breakdown: https://www.gamesradar.com/games/action-rpg/wuthering-waves-yinlin-build-guide/
- MisterMenPlays — Yinlin combo and rotation guide: https://www.mistermenplays.com/wutheringwaves/builds/yinlin
- Pocket Tactics — Yinlin build and echo guide: https://www.pockettactics.com/wuthering-waves/yinlin
- ClutchPoints — Yinlin kit and resonance chains: https://clutchpoints.com/gaming/wuthering-waves-yinlin-kit-skills-resonance-chains-more
