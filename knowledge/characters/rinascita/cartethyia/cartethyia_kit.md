---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/rinascita/cartethyia/cartethyia_kit.md
character: Cartethyia
group: Rinascita
document_type: character_kit
importance: high
tags:
- character
- kit
- combat
---

# Cartethyia Kit & Mechanics Knowledge File
<!-- RAG-formatted knowledge file. Each ## heading = one retrievable chunk. -->

## Cartethyia: Combat Archetype and Role
- **Element/Attribute:** Aero
- **Weapon Type:** Sword
- **Role:** Main DPS (Hypercarry; capable of Quickswap)
- **Scaling Stat:** HP (unique — first DPS in Wuthering Waves to scale entirely off Max HP rather than ATK)
- **Damage Type:** Aero DMG, Aero Erosion DMG, Basic Attack DMG
- **Combat Style:** Dual-form melee burst fighter — cycles between Cartethyia form (fast attacks, Sword Shadow summoning, Aero Erosion application) and Fleurdelys form (high-burst AoE, enemy grouping, Conviction-fueled ultimate)
- **Specialty:** Aero Erosion stack management; self-heal on Ultimate; enemy stagnation (crowd control); wide AoE damage; air-combat prowess (large portion of rotation spent airborne)
- **Tier:** T0 in Tower of Adversity (ToA); T1 in Whimpering Wastes (per Prydwen patch 3.0 assessment)
- **Overall:** Considered the highest single-team damage dealer in Wuthering Waves in her best conditions as of Patch 3.0

## Cartethyia: Key Resources (Forte Mechanics Overview)
Cartethyia's gameplay is built around three interconnected resources:

**Sword Shadows (Cartethyia Form)**
- Three distinct Sword Shadows: Sword of Divinity (summoned by Basic Attack Stage 4), Sword of Discord (summoned by Heavy Attack or Intro Skill), Sword of Virtue (summoned by Resonance Skill)
- Only 1 of each type may exist at once; each lasts 20 seconds
- Performing Mid-air Attack recalls all active Sword Shadows; the type and number recalled determine the form of Plunging Attack and grant corresponding buffs (Heart of Virtue, Mandate of Divinity, Power of Discord)
- Recall multiplier scales significantly: 1 sword = 2.84% HP, 2 swords = 1.66%×3 HP, 3 swords = 5.68%×3 HP

**Forte Gauges — Heart of Virtue / Mandate of Divinity / Power of Discord**
- Granted upon recalling specific Sword Shadow types via Mid-air Attack
- **Heart of Virtue:** In Fleurdelys form, Basic Attack Stage 4 creates a force field to stagnate enemies; increases Fleurdelys's resistance to interruption; removed when Manifest ends
- **Mandate of Divinity:** In Fleurdelys form, Aero Erosion DMG Amplified by 50% and damage interval halved for enemies within range; removed when Manifest ends
- **Power of Discord:** In Fleurdelys form, certain attacks raise Aero Erosion stacks on all nearby targets to the highest count among them; removed when Manifest ends

**Conviction (Fleurdelys Form)**
- A secondary gauge that only exists when Fleurdelys is active in Manifest state
- Fleurdelys restores Conviction on hit with her attacks
- At 120 Conviction, the Resonance Liberation changes from "A Knight's Heartfelt Prayers" to "Blade of Howling Squall"
- Can freely swap back to Cartethyia form (pausing Manifest timer) while below 120 Conviction

## Cartethyia: Stats Baseline: Level 1 – 90
All values are base stats (without Minor Fortes or Echo bonuses):

| Level | HP      | ATK | DEF |
|-------|---------|-----|-----|
| 1     | ~1,710  | ~36 | ~71 |
| 10    | ~3,710  | ~79 | ~153|
| 20    | ~5,740  | ~122| ~237|
| 30    | ~7,530  | ~160| ~310|
| 40    | ~9,320  | ~198| ~384|
| 50    | ~10,840 | ~230| ~447|
| 60    | ~12,090 | ~257| ~498|
| 70    | ~13,220 | ~281| ~546|
| 80    | ~14,020 | ~298| ~579|
| 90    | 14,800  | 313 | 611 |

- Max Energy: 125
- Base CRIT Rate: 5%
- Base CRIT DMG: 150%
- Base Healing Bonus: 0%
- Base Aero DMG: 0%

## Cartethyia: Stats Baseline: Max Analysis
At Level 90 with all Minor Fortes unlocked:
- HP: 14,800 base → +12% from Minor Forte HP bonus → ~16,576 HP
- CRIT Rate: 5% base → +8% from Minor Forte → 13% base
- For optimal endgame performance, targets: ~50,000 HP total, ~70% CRIT Rate, ~270% CRIT DMG
- Energy Regen: Requires 115%–120% to comfortably execute full rotation
- Recommended final stat spread per Prydwen: Energy Regen (until ~115–120%) → CRIT Rate = CRIT DMG → HP% → Basic Attack DMG% = Liberation DMG%
- All of Cartethyia's abilities scale off HP, not ATK — this makes ATK-scaling echoes, weapons, and buffs largely wasted on her

## Cartethyia: Ascension Materials
Total materials required for full character ascension (Level 1 → 90):
- 4× LF Tidal Residuum
- 12× MF Tidal Residuum
- 12× HF Tidal Residuum
- 4× FF Tidal Residuum
- 46× Unfading Glory
- 60× Bamboo Iris (gathered from open world map in Rinascita)
- 170,000 Shell Credits

## Cartethyia: Basic Attack — Sword to Carve My Forms
**Basic Attack – Cartethyia:**
Performs up to 4 consecutive attacks dealing Aero DMG. Following Stage 4, inflicts 1 stack of Aero Erosion on targets and summons Sword of Divinity's Shadow (1 max, lasts 20s).

**Heavy Attack – Cartethyia:**
Consumes STA to attack, dealing Aero DMG and summoning Sword of Discord's Shadow (1 max, lasts 20s). Considered Basic Attack DMG. Can be performed mid-air.

**Mid-air Attack – Cartethyia:**
Plunging Attack costing STA, dealing Aero DMG (also Aero Erosion DMG). Recalls all Sword Shadows. Number and type recalled determines Plunging Attack form and grants Heart of Virtue, Mandate of Divinity, or Power of Discord. Next Normal Attack after Plunging begins at Stage 2.

**Dodge Counter – Cartethyia:**
Press Normal Attack after a successful dodge to deal Aero DMG.

**Attribute Scaling (Level 1 → Level 10 at Lv.1 values):**
- Stage 1 DMG: 2.41% HP
- Stage 2 DMG: 1.98% + 1.98% + 2.64% HP
- Stage 3 DMG: 2.15% + 2.15% + 2.15% + 2.15% HP
- Stage 4 DMG: 1.27%×3 + 3.80% HP
- Dodge Counter DMG: 3.45% + 3.45% + 3.45% + 3.45% HP
- Heavy Attack DMG: 1.05%×3 + 3.14% HP
- Mid-air Attack (0 swords): 2.84% HP
- Mid-air Attack (1 sword): 2.84% HP
- Mid-air Attack (2 swords): 1.66%×3 HP
- Mid-air Attack (3 swords): 5.68%×3 HP
- Mid-air Attack STA Cost: 30 | Heavy Attack STA Cost: 20

## Cartethyia: Resonance Skill — Sword to Bear Their Names
**Resonance Skill – Cartethyia:**
Attacks the target, launches nearby enemies, then plunges them to the ground, dealing Aero DMG and inflicting 2 stacks of Aero Erosion on targets hit. Considered Basic Attack DMG. Can be performed mid-air. Summons Sword of Virtue's Shadow upon use (1 max, lasts 20s).

**Attribute Scaling (Level 1 values):**
- Skill DMG: 3.47%×3 + 4.46% HP
- Concerto Energy Regen: 10
- Cooldown: 14 seconds

Note: This is a critical rotation skill — it simultaneously deals damage, inflicts 2 Aero Erosion stacks, and summons Sword of Virtue, enabling all three Sword Shadows to be active simultaneously.

## Cartethyia: Resonance Liberation — A Knight's Heartfelt Prayers (Transformation)
**A Knight's Heartfelt Prayers:**
Reduces HP to 50% of Max HP and transforms Cartethyia into Fleurdelys, entering the Manifest state for 12 seconds. (No HP cost if HP is already below 50%.) Clears all Conviction upon entry. Ending the Manifest state does NOT clear Resonance Energy.

While in Manifest, certain Fleurdelys attacks instantly trigger 1 instance of Aero Erosion DMG and reduce target's Aero Erosion stack by 1 (affected attacks: Basic Attack Stage 5, Mid-air Attack Stage 2, Resonance Skill May Tempest Break the Tides).

**Attribute Scaling (Level 1 values):**
- Resonance Energy Cost: 125
- Cooldown: 25 seconds
- Concerto Regen: 20

Note: This is Cartethyia's primary ultimate — it is not the damage dealing ultimate but the transformation ability. Its real function is enabling access to Fleurdelys form and setting up for Blade of Howling Squall.

## Cartethyia: Resonance Liberation — Blade of Howling Squall (Main DPS Ultimate)
**Resonance Liberation – Blade of Howling Squall:**
Activated when Fleurdelys has 120 Conviction. Removes all Conviction, ends Manifest, restores 50% of Max HP, then deals Aero DMG to all targets in an area along a straight line in front. Upon hitting targets, removes all Aero Erosion stacks; each stack removed Amplifies the DMG taken by targets by 20% (up to 5 stacks maximum, for a total of up to 100% amplification against a fully stacked target).

Can be cast mid-air.

**Attribute Scaling (Level 1 values):**
- Blade of Howling Squall DMG: 6.60%×7 HP (per Prydwen)
- Cooldown: 25 seconds
- Concerto Regen: 20

This is Cartethyia's primary burst window. With 5 Aero Erosion stacks consumed, it effectively amplifies itself by 100%, making pre-loading Erosion stacks before casting essential.

## Cartethyia: Forte Circuit — Tempest (Fleurdelys Form)
When Cartethyia transforms into Fleurdelys, the following attacks replace or supplement her base kit:

**Basic Attack – Fleurdelys:** Up to 5 consecutive attacks dealing Aero DMG, restoring Conviction on hit.
- Stage 5 DMG: 3.63% + 14.49% HP (enormous hit)
- Stage 4 (with Heart of Virtue): creates stagnation force field + increases interruption resistance

**Mid-air Attack – Fleurdelys:** Up to 3 consecutive air attacks costing STA, dealing Aero DMG and restoring Conviction. Hold Normal Attack to cast Stage 3. Can chain into Basic Attack Stage 3 afterward.

**Heavy Attack – Fleurdelys:** Thrust forward for focused strike dealing Aero DMG; restores Conviction. Considered Basic Attack DMG.

**Enhanced Heavy Attack – Fleurdelys:** While casting Heavy Attack, press Normal Attack to fall back and blast forward in a straight line, dealing Aero DMG + restoring Conviction. Considered Basic Attack DMG. Follow up with Basic Attack for Upward Cut – Fleurdelys.

**Upward Cut – Fleurdelys:** While on the ground, Jump to cast, dealing Aero DMG and restoring Conviction.

**Dodge Counter – Fleurdelys:** After successful dodge, press Normal Attack to deal Aero DMG + restore Conviction. Can follow up with Basic Attack Stage 4.

**Resonance Skill – Sword to Answer Waves' Call:** Summons a force field near target that continuously pulls in nearby enemies. Deals Aero DMG and restores Conviction. Can be cast mid-air.

**Resonance Skill – May Tempest Break the Tides:** Follow-up to the above. Calls down a giant Sword Shadow to crush an area around the target, creating a pull force field. Deals Aero DMG to ground targets and restores Conviction. Can be cast mid-air.

**Forte Multipliers (Level 1 values):**
- Basic Stage 1: 3.27% HP
- Basic Stage 2: 1.83% + 0.92%×3 HP
- Basic Stage 3: 1.08%×3 + 2.15% HP
- Basic Stage 4: 1.38%×5 HP
- Basic Stage 5: 3.63% + 14.49% HP
- Dodge Counter: 1.61%×3 + 3.22% HP
- Upward Cut: 2.29%×2 HP
- Heavy Attack: 2.15% + 5.02% HP
- Enhanced Heavy Attack: 3.91%×2 + 1.96% HP
- Mid-air Attack 1: 1.50% + 1.50% + 1.55% HP
- Mid-air Attack 2: 3.72% + 3.72% + 7.43% HP
- Mid-air Attack 3: 1.11% HP
- Sword to Answer Waves' Call: 0.94%×4 + 8.73% HP
- May Tempest Break the Tides: 0.94%×2 + 3.54%×3 HP
- Skill Cooldown: 14s | Heavy Attack STA: 20 | Mid-air Attack 1 STA: 5 | Mid-air Attack 2 STA: 5 | Mid-air Attack 3 STA: 30

## Cartethyia: Inherent Skill 1 — A Heart's Truest Wishes
The healing received by all Resonators other than Cartethyia/Fleurdelys in the team is increased by 20%, and their resistance to interruption is enhanced.

If Rover: Aero is in the team, Rover: Aero additionally restores 25 Windstrings upon casting Omega Storm.

This passive makes Cartethyia an excellent support for her own team — her presence alone improves healer efficiency and makes rotations safer.

## Cartethyia: Inherent Skill 2 — Wind's Indelible Imprint
Targets with 1 to 3 stacks of Aero Erosion take 30% more DMG from Cartethyia and Fleurdelys.

Targets with more than 3 stacks of Aero Erosion additionally take 10% more DMG from Cartethyia and Fleurdelys per extra stack of Aero Erosion, up to 3 additional stacks (i.e., at 6 stacks: 30% + 30% = 60% more DMG).

This is the core damage amplification passive. It creates the mathematical incentive to maintain maximum Aero Erosion stacks throughout the rotation — and why Ciaccona (off-field Erosion applier) and Aero Rover (Erosion stack cap increaser) are so integral to her best teams.

## Cartethyia: Intro Skill — Sword to Mark Tide's Trace / Sword to Call for Freedom
**Cartethyia – Sword to Mark Tide's Trace:**
Deals Aero DMG and inflicts 2 stacks of Aero Erosion on targets hit. Summons Sword of Discord's Shadow. Press Normal Attack shortly after to perform Basic Attack Stage 2.

**Fleurdelys – Sword to Call for Freedom:**
Thrusts forward to impale the target, dealing Aero DMG and restoring Conviction. Press Normal Attack shortly after to cast Basic Attack Stage 2.

**Attribute Scaling (Level 1 values):**
- Sword to Mark Tide's Trace DMG: 1.05%×3 + 3.14% HP
- Sword to Call for Freedom DMG: 2.15% + 5.02% HP
- Concerto Energy Regen (both): 10

## Cartethyia: Outro Skill — Wind's Divine Blessing
Aero DMG dealt by the active Resonator in the team (other than Cartethyia/Fleurdelys) to targets with Negative Statuses is Amplified by 17.5% for 20 seconds.

This is a meaningful buff for any Aero-damage teammate that benefits from the Negative Status condition, particularly valuable in Aero-heavy compositions.

## Cartethyia: Skill Upgrade Materials
Total materials required to level all skills to max:
- 25× LF Tidal Residuum
- 28× MF Tidal Residuum
- 40× HF Tidal Residuum
- 57× FF Tidal Residuum
- 25× Inert Metallic Drip
- 28× Reactive Metallic Drip
- 55× Polarized Metallic Drip
- 67× Heterized Metallic Drip
- 26× When Irises Bloom
- 2,030,000 Shell Credits

**Skill Priority (recommended order):**
1. Forte Circuit (Fleurdelys moves) — drives the majority of her burst damage
2. Resonance Liberation — increases Blade of Howling Squall multiplier directly
3. Basic Attack — improves Cartethyia form damage and Mid-air Attack values
4. Resonance Skill — secondary damage contributor
5. Intro Skill / Outro Skill — lowest priority

## Cartethyia: Resonance Chains (S1 – S6)
**S1 – Sequence Node 1:** Gain Zeal for 10s when attacks defeat Aero Erosion-afflicted targets. In Zeal state, upon defeating enemies the next damaging move raises Aero Erosion on targets to the highest count among defeated enemies (within stack cap; Zeal consumed after). Also: when Fleurdelys's Conviction hits 30/60/90/120, increase Fleurdelys's CRIT DMG by 25% for 15s (up to 4 stacks, max +100% CRIT DMG). Stacks do not reset on new gains. Cleared after Blade of Howling Squall.

**S2 – Sequence Node 2:** Upon casting A Knight's Heartfelt Prayers, increases the max stack limit of Aero Erosion by 3 stacks within range. The next attack inflicts 3 stacks of Aero Erosion on all targets in range and immediately triggers Aero Erosion DMG once (without consuming stacks). Also: Cartethyia form Basic Attack, Heavy Attack, Dodge Counter, and Intro Skill DMG Multipliers increased by 50%; Mid-air Attack DMG Multiplier increased by 200%. After Mid-air Attack, every 1 type of Sword Shadow recalled reduces Resonance Skill cooldown by 1s (up to 3s with all three recalled).

**S3 – Sequence Node 3:** Basic Attack Stage 5, Mid-air Attack Stage 2, Enhanced Heavy Attack, and Resonance Skill May Tempest Break the Tides (Fleurdelys) now inflict 2 stacks of Aero Erosion on targets. Also: Blade of Howling Squall DMG Multiplier increased by 100%.

**S4 – Sequence Node 4:** After any Resonator in the team inflicts Havoc Bane, Fusion Burst, Spectro Frazzle, Electro Flare, Glacio Chafe, or Aero Erosion, all Resonators in the team gain 20% DMG Bonus for all Attributes for 20 seconds.

**S5 – Sequence Node 5:** When Cartethyia or Fleurdelys takes a fatal blow, they survive and gain a Shield equal to 20% of Max HP for 10s (once every 10 minutes). Also: HP cost for A Knight's Heartfelt Prayers reduced to 25% of Max HP (from 50%).

**S6 – Sequence Node 6:** After casting Blade of Howling Squall, raise all Aero Erosion stacks on the target hit to maximum. Blade of Howling Squall no longer removes Aero Erosion stacks on hit. Within 30s after casting either Intro Skill, A Knight's Heartfelt Prayers, or Blade of Howling Squall, when any Resonator in the team inflicts Aero Erosion on targets already at maximum Erosion stacks, immediately trigger Aero Erosion DMG once. Additionally: Fleurdelys receives a 40% unique DMG Bonus multiplier (confirmed post-launch — this is a unique multiplier type, not a standard DMG Bonus).

**Pull Priority Recommendations (per Wutheringlab and Prydwen):**
- S1R1: Strong damage upgrade; CRIT DMG stacking makes Fleurdelys form devastating
- S2R1: Removes dependence on Aero Rover for stack cap; massive Cartethyia form damage boost; ~45% DPS increase for double Mid-air Attack rotations
- S3: Worthwhile if no Ciaccona (adds self-stacking in Fleurdelys); doubles Blade of Howling Squall multiplier
- S6R1: Endgame investment — Fleurdelys receives 40% unique DMG boost; Erosion stacks are refilled and no longer consumed; Erosion triggers become frequent

## Cartethyia: Echo Sets — Best Sets
**Best Set:** Windward Pilgrimage (5-piece) — tailor-made for Cartethyia
- Reason: The set provides Aero DMG bonuses that scale with Aero Erosion interactions. Since Cartethyia scales off HP rather than ATK, she uniquely benefits from the 4-4-1-1-1 echo cost setup (2× 4-cost, 3× 1-cost) which maximizes flat HP from 1-cost echoes (+22.8% HP + 2,280 flat HP per piece)
- Using the standard 4-3-3-1-1 setup instead costs approximately 7% damage output

**Alternative Set:** Gusts of Welkin (for Aero-focused non-Ciaccona compositions)
- Note: Only applicable if running a composition that still needs additional Aero DMG provision; normally outclassed by Windward Pilgrimage for Cartethyia herself

## Cartethyia: Echo Sets — Best Main Echo
**Best Main Echo (4-cost slot 1):** Reminiscence: Fleurdelys
- Grants the equipped Resonator 10% unconditional Aero DMG Bonus; Aero Resonators or Cartethyia gain an additional 10% Aero DMG Bonus
- Total: +20% Aero DMG Bonus exclusively for Cartethyia
- Echo Skill also deals good personal damage

**Second 4-cost Slot:** Nightmare: Kelpie
- Synergizes with Aero Erosion

## Cartethyia: Echo Sets — Echo Stat Priority
**Echo Main Stats (4-4-1-1-1 configuration):**
- 4-cost Slot 1 (Main): Reminiscence: Fleurdelys → Aero DMG Bonus main stat preferred
- 4-cost Slot 2: CRIT Rate or CRIT DMG (whichever is needed to balance ratio)
- 3× 1-cost Slots: HP% main stat on all three (maximizes total HP)

**Substat Priority:**
Energy Regen (until 115–120%) → CRIT Rate = CRIT DMG → HP% → Basic Attack DMG% = Liberation DMG% → HP flat

## Cartethyia: Weapons — Best Weapon
**Defier's Thorn (5-star Sword — Signature):**
- Sub-stat: HP% (the ONLY sword in the game with HP% as sub-stat — uniquely suited to Cartethyia)
- R1 Effect: HP +12%; after using Intro Skill or Basic Attack, ignores 8% of target's DEF; when target has 1+ stack Aero Erosion, damage is increased by 20%; at R1 full: ignores 16% DEF, and if target has Aero Erosion, the DMG taken by the target is Amplified by 40%
- This weapon directly synergizes with every aspect of Cartethyia's kit — HP scaling, DEF ignore, and Aero Erosion exploitation

## Cartethyia: Weapons — Alternative Weapons
**Red Spring (5-star):** Strong alternative with high Base ATK and useful CRIT DMG; increases Basic Attack DMG which covers a large portion of Cartethyia's rotation.

**Unflickering Valor (5-star):** Increases Basic Attack DMG; viable in the absence of Defier's Thorn.

**Guardian Sword (4-star — Best F2P Option):** The only 4-star or otherwise accessible sword with HP% main stat. An excellent free-to-play alternative that still leverages Cartethyia's HP-scaling identity.

Note: Most swords with CRIT Rate or CRIT DMG sub-stats (such as standard 5-star options) remain functional but do not maximally exploit the HP-scaling design. A good CRIT-stat sword is still viable when the signature is unavailable.

## Cartethyia: Team Composition Guide — Best Team (with Chisa, patch 2.8+)
**Cartethyia / Ciaccona / Chisa** (Current Best Team as of Patch 2.8+)
- Chisa replaced Aero Rover in the #1 team: provides DEF reduction (Havoc Bane), significant DMG buffs, consistent healing, and +3 maximum Negative Status stacks via Outro, directly increasing the Aero Erosion stack limit
- Ciaccona: quintessential Sub-DPS; low field time; provides multi-wave AoE off-field Aero Erosion application, multiple Aero DMG Bonus buffs throughout her kit, and Gusts of Welkin set bonus
- Chisa uses: 3pc Thread of Severed Fate + 2pc Havoc Eclipse (or similar); Cartethyia uses: 5pc Windward Pilgrimage; Ciaccona uses: 5pc Gusts of Welkin

**Team Rotation (Chisa/Ciaccona/Cartethyia):**
1. Chisa: Resonance Skill → Basic Attack (Death Snip cancel) → Resonance Liberation → Outro (swap)
2. Ciaccona: Essence generation → Solo attack → Heavy Attack → Resonance Liberation → Outro (swap)
3. Cartethyia: Intro Skill → Basic Attack ×3 → Resonance Skill → Mid-air Attack → Resonance Liberation (transform) → Fleurdelys combos → Build Conviction to 120 → Blade of Howling Squall

## Cartethyia: Team Composition Guide — Premium Team (Aero Rover)
**Cartethyia / Ciaccona / Rover (Aero)** (Original Best Team at launch, still viable)
- Aero Rover's Outro increases maximum Aero Erosion stack capacity by 3 (bringing total to 6) which enables Cartethyia's full Inherent Skill 2 damage bonus (up to +60% DMG at 6 stacks)
- Aero Rover generates 25 bonus Windstrings when they cast Omega Storm if Cartethyia is in the team (from Cartethyia's Inherent Skill 1), slightly smoothing rotation
- Rotation: Aero Rover → Ciaccona → Cartethyia (Intro → Basic Attack → Skill → Mid-air → Ult transform → Fleurdelys combo → Blade of Howling Squall)

## Cartethyia: Team Composition Guide — F2P / Budget Team
**Cartethyia / Sanhua / Rover (Aero)** (Free-to-Play / Non-Ciaccona Option)
- Sanhua (free 5-star) provides 38% Basic Attack DMG deepening buff — covers Cartethyia's largest damage source
- Aero Rover raises Erosion stack cap and provides healing
- Without Ciaccona, Cartethyia must build Erosion stacks herself by weaving between Cartethyia and Fleurdelys form mid-rotation — more complex but viable
- Echo configuration changes to 4-3-3-1-1 if no Ciaccona (3-cost slot takes Aero DMG Bonus main stat)

**Alternative Support Options:**
- Shorekeeper: Provides 15% All DMG Amplify + crit buffs + sustained healing; generalist option
- Verina: 15% All DMG Amplify + ATK buff; does not benefit from ATK scaling on Cartethyia but DMG amplify is universal
- Aalto (S6): Provides 23% Aero Deepen + extra Crit Rate buff through portal; limited uptime but accessible
- Lupa: Fusion DMG buff synergy with Cartethyia's multi-hit attack pattern

## Cartethyia DPS Benchmarks: S0 to S6 (Source: Prydwen.gg — Primary)
*All benchmarks at full Lv.90, Defier's Thorn R1, 5pc Windward Pilgrimage, Reminiscence: Fleurdelys main echo (4-cost CRIT Rate / 4-cost CRIT DMG / 1-cost HP / 1-cost HP / 1-cost HP), substats HP 45% / CRIT Rate 42% / CRIT DMG 84%. Solo damage — personal output only, does not include teammate damage contributions. Rotation time: 13.23s.*

**Rotation used for benchmarks (Prydwen — Standard Rotation, 1 Target scenario):**
Intro - Cartethyia → Basic P2 → Basic P3 → Basic P4 → Skill: Sword to Bear Their Names → Mid-air Attack - Cartethyia → Ultimate: A Knight's Heartfelt Prayers → (Skill 1) Forte: Sword to Answer Waves' Call → Forte: Fleurdelys Mid-air Attack P3 (Hold Basic during Resonance Skill) → Forte: Fleurdelys Basic P3 → Forte: Fleurdelys Basic P4 → Forte: Fleurdelys Basic P5 → (Skill 2) Forte: May Tempest Break the Tides → Forte: Fleurdelys Basic P3 → Forte: Fleurdelys Basic P4 → Forte: Fleurdelys Basic P5 → Ultimate: Blade of Howling Squall → Outro

| Sequence | Total DMG       | DPS         | Relative to S0 |
|----------|-----------------|-------------|----------------|
| S0       | 1,092,186 DMG   | 82,553 DPS  | 100.00%        |
| S1       | 1,281,482 DMG   | 96,861 DPS  | 117.33%        |
| S2       | 1,609,951 DMG   | 121,689 DPS | 147.41%        |
| S3       | 2,075,703 DMG   | 156,893 DPS | 190.05%        |
| S4       | 2,228,889 DMG   | 168,472 DPS | 204.08%        |
| S5       | 2,228,889 DMG   | 168,472 DPS | 204.08%        |
| S6       | 2,826,809 DMG   | 213,666 DPS | 258.82%        |

*Source: Prydwen.gg — Cartethyia Guide and Build, Calculations tab (https://www.prydwen.gg/wuthering-waves/characters/cartethyia/). Note: S4 and S5 show identical damage because S5's survivability passive (fatal blow shield + HP cost reduction on transformation) does not directly increase Cartethyia's personal damage output. Benchmarks are solo personal damage only; team composition multiplies real-world performance significantly. Do not compare raw numbers between characters or use them as a pull metric — see Prydwen's disclaimer above the chart.*

**Damage Profile Breakdown (per Prydwen pie chart):**
- Basic Attack DMG: **51.6%** — the largest share by far; Basic Attack scaling (both Cartethyia and Fleurdelys forms) drives the majority of her output
- Liberation DMG: **23.6%** — Blade of Howling Squall is a massive single hit but occupies a smaller slice due to the long rotation time
- Skill DMG: **12.5%** — Resonance Skill hits in both Cartethyia and Fleurdelys forms contribute meaningfully
- Intro / Echo / Debuff: remaining ~12.3% split across Intro Skill hits, Echo procs, and Aero Erosion debuff ticks

**Calculations build used (Prydwen):**
- Weapon: Defier's Thorn R1
- Echo Set: 5pc Windward Pilgrimage
- Main Echo: Reminiscence: Fleurdelys
- Echo Config: 4-cost (CRIT Rate) / 4-cost (CRIT DMG) / 1-cost (HP) / 1-cost (HP) / 1-cost (HP)
- Substats: HP 45% / CRIT Rate 42% / CRIT DMG 84%

**Teammate buffs included in calculations:**
- Ciaccona + Woodland Aria + 5pc Gusts of Welkin + Nightmare: Kelpie
- Rover (Aero) + Bloodpact's Pledge + 5pc Windward Pilgrimage + Reminiscence: Fleurdelys

## Cartethyia: Character Strengths and Weaknesses in Actual Gameplay
**Strengths:**
- Highest damage ceiling in WuWa as of Patch 3.0 in optimal conditions
- Built-in interruption resistance once rotation is learned; near-uninterruptable rotation inputs
- Self-sufficient: heals herself on Blade of Howling Squall cast (restores 50% Max HP); self-applies Aero Erosion; self-amplifies Erosion via Inherent Skill 2
- Extremely difficult to hit: a large portion of her rotation is spent airborne
- Enemy stagnation and grouping in Fleurdelys form (Heart of Virtue force field)
- Lots of swap-cancel windows — rewards skilled players with optimized quickswap
- Even without signature weapon or best team, her raw damage is exceptional with good Echoes
- Passively buffs teammates: improves healing received by 20%, gives resistance to interruption, funnels Windstrings to Aero Rover — makes whole team smoother

**Weaknesses:**
- Very expensive to fully optimize: best performance requires Ciaccona (limited), Chisa/Aero Rover (additional resources), and ideally signature weapons across the board
- Lack of viable HP-scaling weapon alternatives — most swords don't serve her scaling
- Without Ciaccona at S0, she cannot self-sustain full Erosion stacks or reach max stack cap for bonus amp on her Ultimate
- Struggles in Whimpering Wastes (multi-wave content) when full enemy waves die simultaneously, resetting Erosion stacks and requiring ramp-up again
- Complex kit: the Sword Shadow system, dual-form swapping, Conviction management, and Erosion stack micromanagement create a steep learning curve
- HP cost on Transformation ultimate (50% of Max HP) can be dangerous in punishing content without good Echoes or healer support
- Power fluctuations when far from Rinascita (lore-stated in Resonance Evaluation Report)

---

## Cartethyia Kit Sources
- Prydwen – Cartethyia Build and Guide (Primary): https://www.prydwen.gg/wuthering-waves/characters/cartethyia/
- Game8 – Cartethyia Best Builds and Teams: https://game8.co/games/Wuthering-Waves/archives/507777
- Wutheringlab – Cartethyia Build: https://wutheringlab.com/character/cartethyia-build/
- Wuthering.gg Character Page: https://wuthering.gg/characters/cartethyia
- Steam Guide – Version 2.4 Cartethyia Build: https://steamcommunity.com/sharedfiles/filedetails/?id=3493689407
- Lootbar Build Guide (V3.0): https://lootbar.gg/blog/en/wuthering-waves-cartethyia-build-guide.html
- LDShop Cartethyia Build Guide (2.8): https://www.ldshop.gg/blog/guide/cartethyia-build-guide.html
- Buffget – Chisa Havoc Team 2.8 DPS Benchmark: https://buffget.com/news/wuthering-waves-best-chisa-havoc-teams-28-cartethyia-and-zhezhi-comps-1ohau94
- Wutheringwaves.fandom.com – Cartethyia: https://wutheringwaves.fandom.com/wiki/Cartethyia
- Prydwen – Tier List (patch context): https://www.prydwen.gg/wuthering-waves/tier-list/
