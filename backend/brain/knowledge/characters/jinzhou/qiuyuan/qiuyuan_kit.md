---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/huanglong/qiuyuan/qiuyuan_kit.md
character: Qiuyuan
group: Huanglong / Mingting / Chongzhou
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - aero
  - sword
  - sub-dps
  - echo-skill-amplifier
  - crit-dmg-buffer
  - swordsters-soliloquy
  - inksplash-of-mind
  - bamboos-shade
  - version-2-7
---

# Qiuyuan Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/qiuyuan/, https://wutheringlab.com/character/qiuyuan-build/, https://game8.co/games/Wuthering-Waves/archives/524882, https://lootbar.gg/blog/en/wuthering-waves-qiuyuan-build-guide.html, https://www.ldshop.gg/blog/wuthering-waves/qiuyuan-build-guide.html -->

## Qiuyuan: Combat Archetype and Role

- **Element:** Aero
- **Weapon Type:** Sword
- **Role:** Sub-DPS / Echo Skill DMG Amplifier / Critical DMG Buffer
- **Archetype:** Forte-stack accumulator; Bamboo's Shade team buff (30% Echo Skill DMG Bonus); Inksplash of Mind burst; Liberation Crit DMG team buff (up to 30%); Outro 50% Echo Skill DMG Amplification to incoming Resonator
- **Availability:** Limited 5-star; Version 2.7 second-half banner (Wanderer Knows No Far and Near)

Qiuyuan is the premier and currently unique Echo Skill DMG amplifier in Wuthering Waves as of Version 2.7. No other character in the game provides both a team-wide Echo Skill DMG Bonus (30% via Bamboo's Shade at 400 Swordster's Soliloquy) and a personal Echo Skill DMG Amplification Outro (50% to the incoming Resonator for 14 seconds). His Resonance Liberation additionally scales a Crit DMG buff off his own Crit Rate — for every 1% of his Crit Rate over 50%, all active Resonators gain 2% Crit DMG, up to 30% — making him a dual-vector team buffer for Echo Skill-focused teams.

His optimal team archetype is narrower than generalist buffers: he excels specifically in compositions where the Main DPS deals a meaningful portion of their damage through Echo Skills (Galbrena, Phrolova, Cantarella). Outside this archetype, his buffing profile loses most of its distinctive value and he functions as a generic Aero Sub-DPS with modest personal damage at baseline sequences. His rotations are fast — Intro into full Forte bar is the default path — which means he occupies minimal field time and the buffs he provides are active before the Main DPS begins their highest-damage phase.

## Qiuyuan: Key Resource — Swordster's Soliloquy

Qiuyuan's entire kit is gated through a single Forte gauge: **Swordster's Soliloquy**, with a maximum of 600 points, internally divided into three 200-point thirds. The gauge determines his current capability tier and drives the team buffing events.

**Swordster's Soliloquy Generation**

| Source | Points Granted |
|--------|---------------|
| Basic Attack Stage 3 (ground chain final hit) | +100 |
| Each stage of Thus Spoke the Blade: Inkwash (Enhanced Basic) | +100 per stage |
| Dodge Counter | +100 |
| **Intro Skill: Attack the Must-Defend** | **+400 (instant)** |

Generation is **not possible** during the Inksplash of Mind state (600-point consumption phase) — the gauge is locked while being spent.

**Threshold Effects**

**At 200 points — Enhanced Basic Attacks (Inkwash)**
Basic Attack chain is replaced by Thus Spoke the Blade: Inkwash — up to 4 enhanced consecutive Aero strikes classified as **Heavy Attack DMG**. Each stage of Inkwash generates +100 Swordster's Soliloquy on hit. Stages 1–4 carry increasing multipliers, with Stage 4 (86.70% per Prydwen Lv.1) as the heaviest single-hit.

**At 400 points — Bamboo's Shade (Team Buff)**
Qiuyuan gains the Bamboo's Shade effect: all nearby active Resonators in the team receive **+30% Echo Skill DMG Bonus for 30 seconds**. This buff fires automatically on reaching 400 points and does not require any additional action. In the Intro Skill entry path, this threshold is crossed instantly on entry — the team buff is active from the moment Qiuyuan arrives.

**At 600 points — Inksplash of Mind (Burst Phase)**
Qiuyuan enters the Inksplash of Mind state for **8 seconds**. During this window, Heavy Attack is replaced by the three-hit Thus Spoke the Blade sequence: To Teach → To Save → To Sacrifice. Each of these three attacks is classified as **both Heavy Attack DMG and Echo Skill DMG** simultaneously — they count as Echo Skills for all set, weapon, and buff triggers. Performing the full sequence expends all 600 Swordster's Soliloquy and ends the Inksplash of Mind state.

**Inherent Skill 1 (Quietude Within)** amplifies the Inksplash of Mind sequence: on entering the state (once per 22s), To Teach, To Save, and To Sacrifice deal **+50% DMG** for 10 seconds; To Sacrifice additionally restores **30 Concerto Energy on hit**. The effect ends early if Qiuyuan swaps off before completing the sequence.

## Qiuyuan: Stats at Lv. 90

| Stat | Value (including Forte Attribute Bonuses) |
|------|------------------------------------------|
| HP | 12,238 |
| ATK | 375 (base) + 12% Forte bonus |
| DEF | 1,198 |
| CRIT Rate | 8% Forte bonus (additive with equipped sources) |
| Max Resonance Energy | 125 |

*Base ATK 375 is competitive for a 5-star sub-DPS. The Forte Attribute Bonuses (+8% Crit Rate, +12% ATK) help reach the 65% Crit Rate requirement for the full Liberation Crit DMG buff.*

## Qiuyuan: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | LF Whisperin Core ×4, Wintry Bell ×4, Shell Credits ×5,000 |
| 2 | 40→50 | MF Whisperin Core ×4, Wintry Bell ×8, Shell Credits ×10,000 |
| 3 | 50→60 | MF Whisperin Core ×8, Wintry Bell ×12, Truth in Lies ×4, Shell Credits ×15,000 |
| 4 | 60→70 | HF Whisperin Core ×8, Wintry Bell ×16, Truth in Lies ×8, Shell Credits ×20,000 |
| 5 | 70→80 | FF Whisperin Core ×4, Wintry Bell ×20, Truth in Lies ×12, Shell Credits ×40,000 |
| 6 | 80→90 | FF Whisperin Core ×4, Wintry Bell ×24, Truth in Lies ×22, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** 170,000

- **Whisperin Cores (LF/MF/HF/FF):** Dropped by Whisperin Tacet Discords (wind-aligned enemies found across Huanglong); available from Forgery Challenge; totals: LF×4, MF×12, HF×12, FF×4
- **Wintry Bells:** Local specialty flowers found in the Gorges of Spirits region (same as Jiyan and Yangyang); gathered from the overworld; use the Interactive Map; 60 total required
- **Truth in Lies:** Weekly boss material; source is the relevant weekly challenge boss in Huanglong — verify current boss name with the Fandom Wiki as of Version 2.7; 46 total required

## Qiuyuan: Skill Upgrade Materials

Forte skills are leveled using **Curse of the Abyss** skill books (Huanglong Forgery Challenge tier). Weekly boss material and Shell Credits follow the standard Forte level-up cost curve. Verify exact per-level breakdowns with the Fandom Wiki.

**Skill Upgrade Priority:** Forte Circuit (Verdant Edge) → Resonance Liberation (Sundering Strike) → Resonance Skill (Through the Groves) → Intro Skill → Basic Attack

- **Forte Circuit first:** Unlocks the Bamboo's Shade team buff (400 pts), the Inksplash of Mind burst phase (600 pts), the Inkwash enhanced attacks (200 pts), and the classification of To Teach/Save/Sacrifice as Echo Skill DMG — essentially the entire kit
- **Liberation second:** Scales the Crit DMG team buff; at 65%+ Crit Rate, the full 30% Crit DMG bonus to active Resonators is a significant multiplier; also counts as Echo Skill DMG so it is amplified by Bamboo's Shade if cast in the same window
- **Resonance Skill third:** Both variants deal Echo Skill DMG; contribute to rotation and Concerto Energy; the tap variant's parry window provides damage immunity on correct timing
- **Basic Attack lowest priority:** Used primarily as a Swordster's Soliloquy generator in the standard rotation; the Inkwash enhanced form (after 200 pts) scales with Forte Circuit level rather than Basic Attack level

## Qiuyuan: Character Kit: Basic Attack — Inkwash

**Standard Ground Chain (3 stages)**
- Up to 3 consecutive Aero DMG attacks
- **Stage 3 hit — on hit:** +100 Swordster's Soliloquy
- Stage 3 is the only standard Basic Attack stage that grants Soliloquy; stages 1 and 2 do not; in practice, only Stage 3 is relevant to the rotation

**Heavy Attack**
- Consumes Stamina; Aero DMG; pressing Normal Attack within a short window after Heavy Attack chains into Thus Spoke the Blade: Inkwash Stage 4 (86.70% multiplier at Lv.1)
- Standard Heavy Attack is primarily used to chain into Inkwash Stage 4 for additional Soliloquy generation when the enhanced attack chain is active

**Mid-Air Attack**
- Plunging Aero DMG; Stamina cost; standard mid-air plunge with no Forte interactions

**Dodge Counter**
- Normal Attack immediately after a successful Dodge; Aero DMG; classified as **Heavy Attack DMG**; grants **+100 Swordster's Soliloquy**
- The Dodge Counter is one of the two ground-level Soliloquy generators (alongside Basic Attack Stage 3); useful for filling the gauge when Intro Skill is not available

**Auto-Parry Mechanic (Passive)**
After performing any Basic Attack or Heavy Attack, Qiuyuan enters a brief window (~1 second after animation begins) during which he automatically nullifies the next instance of incoming DMG and casts a Dodge Counter. Key limitation: this window does not activate immediately on button press — being hit within the first second cancels the effect. Additionally, any other input cancels the parry state. In continuous attacking, this mechanic is effectively inactive as subsequent attack inputs prevent the parry window from activating. It is primarily relevant in specific situations where Qiuyuan attacks once and then pauses.

**Thus Spoke the Blade: Inkwash — Enhanced Basic (at ≥200 Swordster's Soliloquy)**
4-stage enhanced Basic Attack chain; classified as **Heavy Attack DMG**; each stage grants **+100 Swordster's Soliloquy on hit**:
- Stage 1: 30%+30% per Lv.1
- Stage 2: 27.99%+27.99%+37.32% per Lv.1
- Stage 3: 7.33%+7.33%×4+36.65% per Lv.1
- Stage 4: 86.70% per Lv.1

In the Intro Skill rotation, Qiuyuan enters the field at 400 points and immediately chains from Inkwash Stage 3 (the Intro Skill grants this direct access). Completing Stages 3 and 4 generates +100+100 = +200 Swordster's Soliloquy, reaching 600 points and triggering Inksplash of Mind.

## Qiuyuan: Character Kit: Resonance Skill — Through the Groves

**Tap Variant: Through the Groves**
- Dashes forward for a distance; Aero DMG to target; classified as **Echo Skill DMG**
- If cast upon being attacked by an enemy, Qiuyuan becomes immune to that instance of DMG, **stagnates nearby enemies** (freezes them briefly), and gains **interruption immunity** during the Resonance Skill animation
- This tap-variant parry is the most reliable counter window in his kit — unlike the Basic/Heavy Attack auto-parry, this explicitly activates on the frame of being attacked and cannot be accidentally cancelled by other inputs
- Enemy stagnation ends if Qiuyuan swaps off-field
- Generates 10 Concerto Energy
- Cooldown: 14 seconds

**Hold Variant: Undaunted Wayfarer**
- Holds Resonance Skill; Qiuyuan dashes forward consuming Stamina; deals Aero DMG to targets along the path, classified as **Echo Skill DMG**
- If no targets are nearby when held, Qiuyuan leaps up and dashes through the air continuously (consuming Stamina) until Stamina runs out or Resonance Skill is released; on landing near targets, deals additional Aero Echo Skill DMG to nearby targets
- Available in mid-air
- Generates 10 Concerto Energy
- Primarily used for traversal and for the animation-cancel optimization: the hold variant's landing damage can be animation-cancelled, while the tap variant cannot; therefore if planning to end the rotation with Resonance Skill before Outro, hold variant is preferred to minimize field time

**S3 Enhancement: Straw Cape in Drizzly Rain**
At S3, when Concerto Energy is full and Qiuyuan is not in Inksplash of Mind, Resonance Skill is replaced by Straw Cape in Drizzly Rain (available once per 20 seconds). On cast: consumes 60 Concerto Energy, deals 500% Aero ATK Echo Skill DMG, restores 400 Swordster's Soliloquy, and chains the next Basic Attack into Inkwash Stage 3. The subsequent Inksplash of Mind (if triggered) loses the Quietude Within buff on that cycle, but To Teach/Save/Sacrifice gain +600% DMG multipliers and each restores 30 Concerto Energy on hit. The Outro Skill is also replaced with the enhanced Sheath Fallen, New Shoots Revealed (500% ATK Echo Skill DMG).

## Qiuyuan: Character Kit: Resonance Liberation — Sundering Strike

- Qiuyuan performs a wide-range Aero strike to all targets within range; classified as **Echo Skill DMG**
- **Team Crit DMG Buff:** For every 1% of Qiuyuan's Crit Rate over 50%, increases Crit DMG of all nearby active Resonators by **2% for 30 seconds**, up to a maximum of **+30% Crit DMG**
  - Requires: ≥65% Crit Rate for the full +30% buff
  - At 65% Crit Rate (15% over 50%), the formula gives: 15 × 2% = +30% Crit DMG
  - This buff applies to all active Resonators — unlike Bamboo's Shade's Echo Skill DMG Bonus, the Crit DMG buff applies to all damage types, not only Echo Skills
  - Buff does **not** apply to coordinated attacks or off-field characters
- Base DMG multiplier: 400% at Lv.1 (scales with Liberation level; enormously amplified at S3 which adds +500%)
- Resonance Energy cost: 125
- Cooldown: 25 seconds

**Important Timing Notes:**
- Liberation is classified as Echo Skill DMG, meaning it is amplified by Bamboo's Shade (+30% Echo Skill DMG Bonus, active from 400 Swordster's Soliloquy); casting Liberation while Bamboo's Shade is active is the optimal window
- The Crit DMG buff scales strictly off Qiuyuan's Crit Rate, so building him to ≥65% Crit Rate is a team-performance requirement, not just a personal damage choice
- In the standard Intro entry rotation, Bamboo's Shade is active before Liberation; Liberation should be cast before the To Teach/Save/Sacrifice chain so that the Crit DMG buff and Echo Skill DMG Bonus are both active for the entire burst sequence

## Qiuyuan: Inherent Passives

**Inherent Skill 1 — Quietude Within**
- Triggers on entering **Inksplash of Mind** state (once per 22 seconds)
- Grants Quietude Within buff for 10 seconds: To Teach, To Save, and To Sacrifice deal **+50% DMG**; To Sacrifice additionally **restores 30 Concerto Energy on hit**
- Effect ends early if Qiuyuan swaps off-field during the Inksplash sequence
- Practical implication: every full rotation that uses Inksplash of Mind benefits from the +50% bonus on all three To Sacrifice chain hits (22-second ICD aligns well with the rotation cycle time); the 30 Concerto Energy from To Sacrifice on hit assists in building back toward Outro

**Inherent Skill 2 — Drink Away Woes Age-Old**
- On casting **any Echo Skill** (Resonance Skill variants, To Teach/Save/Sacrifice, Liberation, Outro), Qiuyuan's bamboo flask absorbs the overflowing energy and creates Flowing Panacea
- The next time Swordster's Soliloquy is obtained, Flowing Panacea is consumed: Qiuyuan gains **+10% ATK for 20 seconds**
- Provides a reliable ATK buff that fires on the first Soliloquy generation after each Echo Skill use; since multiple Echo Skills fire per rotation, this buff is generally maintained throughout active field time

## Qiuyuan: Intro/Outro Skills

**Intro Skill — Attack the Must-Defend**
- Triggered when Qiuyuan enters the field via swap with full Concerto Energy
- Deals Aero DMG to the target; classified as **Heavy Attack DMG**
- **Grants +400 Swordster's Soliloquy instantly** — crossing both the 200-point (Inkwash) and 400-point (Bamboo's Shade) thresholds simultaneously, on the frame of entry
- **Chains directly into Thus Spoke the Blade: Inkwash Stage 3** — the next Normal Attack input immediately performs Inkwash Stage 3, skipping Stages 1 and 2; this saves 2 hits' worth of field time
- Generates 10 Concerto Energy
- This Intro Skill is the fastest possible path to the full rotation: entry → Stage 3 (+100) → Stage 4 (+100) → 600 points → Inksplash of Mind; total Inkwash inputs required after Intro: just 2

**Outro Skill — Strike Before Ready**
- Triggered when Qiuyuan swaps off-field with full Concerto Energy
- Deals Aero DMG to the target equal to **100% of Qiuyuan's ATK**; classified as **Echo Skill DMG**
- Grants the incoming Resonator **+50% Echo Skill DMG Amplification for 14 seconds** (or until they swap off-field)
- This is the most impactful single-skill buff in an Echo Skill-focused team: +50% Amplification stacks multiplicatively with the +30% Echo Skill DMG Bonus from Bamboo's Shade (Bonus and Amplification are separate multipliers)
- The Outro fires on Qiuyuan's swap-out animation; its Echo Skill DMG classification means it also triggers any Echo set bonuses that activate on Echo Skill use (e.g., Impermanence Heron's +10 Energy grant fires when the Outro lands)
- 14-second duration is sufficient for most Main DPS rotations before a second character needs to swap in

## Qiuyuan: Resonance Chains (Sequences)

**S1 — Sequence Node 1**
- Thus Spoke the Blade: To Teach, To Save, and To Sacrifice can **no longer be interrupted** during execution
- Qiuyuan gains **+20% Crit Rate increase**
- *Impact:* S1 is widely considered the highest-value first node in his chain. The +20% Crit Rate directly addresses the 65% threshold requirement for his full Liberation Crit DMG buff — with S1, only ~45% Crit Rate from gear is needed (compared to ~57% at S0); this is a significant reduction in echo/weapon stat pressure. The interruption immunity on all three To Sacrifice chain hits means the full Inksplash burst can complete safely in challenging content without being knocked out of the state. Prydwen and multiple build guides specifically flag S1 as competing with or exceeding the signature weapon for immediate performance value.

**S2 — Sequence Node 2**
- Bamboo's Shade additionally grants **+30% Echo Skill DMG Amplification** to all nearby Resonators in the team (in addition to the existing +30% Echo Skill DMG Bonus)
- *Impact:* Bamboo's Shade at S2 now provides a dual buff: +30% Echo Skill DMG Bonus (additive with other Bonus sources) AND +30% Echo Skill DMG Amplification (a separate multiplicative multiplier). Together with the Outro's +50% Amplification, an S2 Qiuyuan can stack +30% Bonus + up to +80% Amplification on an incoming DPS who arrives on the back of the Outro. This substantially elevates his support ceiling for Echo Skill-focused teams.

**S3 — Sequence Node 3**
- Liberation Sundering Strike DMG Multiplier increased by **+500%** (from 400% to 2,400% total at Lv.1)
- Adds new enhanced Resonance Skill: **Straw Cape in Drizzly Rain** — when not in Inksplash of Mind and Concerto is full, once per 20 seconds, consuming 60 Concerto to deal 500% ATK Aero Echo Skill DMG and restore 400 Swordster's Soliloquy; next Basic Attack chains into Inkwash Stage 3; the subsequent Inksplash cycle loses Quietude Within but gains +600% DMG on To Teach/Save/Sacrifice with each hit restoring 30 Concerto; Outro is replaced with Sheath Fallen, New Shoots Revealed (500% ATK Echo Skill DMG)
- *Impact:* The Liberation multiplier increase makes his personal damage genuinely competitive. Straw Cape in Drizzly Rain allows a second full Inksplash cycle per rotation when conditions are met, with massively amplified multipliers. S3 is the sequence where Qiuyuan transitions from pure team buffer to meaningful personal DPS contributor.

**S4 — Sequence Node 4**
- **ATK increased by +20%**
- *Impact:* A flat ATK amplification affecting all his ATK-scaling attacks; provides moderate damage improvement across the entire kit.

**S5 — Sequence Node 5**
- Qiuyuan now ignores **15% of the target's DEF** when dealing damage
- *Impact:* Defense penetration; particularly valuable in high-defense content where the multiplier amplification on final damage is larger; pairs well with S3's expanded damage output.

**S6 — Sequence Node 6**
- Casting Thus Spoke the Blade: To Sacrifice **stagnates nearby targets for 5 seconds** (ends on damage to target or Qiuyuan swapping off; not available in Co-op)
- Upon **exiting Inksplash of Mind**, deal Aero DMG equal to **600% of Qiuyuan's ATK** to all targets within range, classified as Echo Skill DMG — an automatic area burst on state exit
- Casting **Straw Cape in Drizzly Rain** (S3 skill) increases Qiuyuan's **Crit DMG by +100% for 6 seconds**; ends on swap
- *Impact:* S6 substantially increases total output per Inksplash cycle through the exit burst. The +100% Crit DMG window from Straw Cape is a massive personal multiplier for the 6-second window. The stagnation on To Sacrifice is a strong grouping and safety tool in solo content. Full S6 Qiuyuan is a high-ceiling DPS and support hybrid, though reaching S6 requires significant banner investment.

## Qiuyuan: Recommended Echo Sets

**Best-in-Slot (Echo Support Build): Sierra Gale (5-piece) + Nightmare Feilian Beringal or Feilian Beringal**
- **Sierra Gale 5-piece:** Aero DMG Bonus; amplifies all of Qiuyuan's Aero skills including the Inkwash chain, Thus Spoke the Blade sequence, Liberation, and Resonance Skill — the consistent elemental bonus for an Aero-primary damage dealer
- **Main Echo: Nightmare Feilian Beringal (preferred) or Feilian Beringal:** On use, deals Aero DMG and grants Qiuyuan +12% Aero DMG Bonus + 12% Heavy Attack DMG Bonus for 15 seconds; both bonuses directly amplify his Inkwash chain (Aero Heavy Attack DMG) and Thus Spoke the Blade attacks (Aero Heavy Attack DMG); Nightmare variant is the upgraded form with higher multipliers if available
- Prydwen recommends this set as the primary damage build for Qiuyuan operating as a Sub-DPS

**Alternative (General Sub-DPS / Moonlit Clouds Support): Moonlit Clouds (4-piece) + Impermanence Heron**
- Used when Qiuyuan's role is purely team support and personal damage is secondary
- **Moonlit Clouds 4-piece:** When the current Resonator casts an Outro Skill, the incoming Resonator gains +22.5% ATK for 15 seconds; Qiuyuan's Outro fires on every swap-out with full Concerto, applying this ATK buff to the incoming Main DPS on top of the +50% Echo Skill DMG Amplification
- **Moonlit Clouds 2-piece:** Energy Regen +10%; assists the 125-Energy Liberation cycling
- **Main Echo: Impermanence Heron:** On cast, flies and dives for Aero DMG; on hit, grants +10 Resonance Energy to Qiuyuan and causes his next Outro to additionally give the incoming character +12% DMG Bonus for 15 seconds; three-layer Outro benefit: +50% Echo Skill Amplification + +22.5% ATK (Moonlit Clouds) + +12% DMG (Heron); the 10 Energy grant on Heron hit assists Liberation cycling
- Game8 and multiple build guides flag this as the optimal set when running Qiuyuan as a Galbrena support where his own damage is not the priority

**Echo Main Stats Priority**
- 4-Cost Echo: CRIT Rate (to reach ≥65% for full Liberation buff, or ≥45% at S1); alternatively Aero DMG Bonus after the threshold is reached
- 3-Cost Echoes (×2): Aero DMG Bonus (Sierra Gale build) or ATK% (Moonlit Clouds build)
- 1-Cost Echoes (×2): ATK%

**Sub-Stat Priority:** CRIT Rate (to ≥65% threshold) → CRIT DMG → ATK% → Heavy Attack DMG Bonus. The 65% Crit Rate threshold is a hard requirement for team buffing purposes; building around it is non-negotiable in teams where the Liberation Crit DMG buff is the primary team contribution. At S1, only ≈45% Crit Rate from gear is needed.

## Qiuyuan: Recommended Weapons

**Best-in-Slot — Emerald Sentence (Signature 5★ Sword)**
- Stat: CRIT Rate; directly assists the 65% threshold requirement
- Passive (When a Heart Settles): ATK +12%; Echo Skills grant 1 stack of Bamboo Cleaver (up to 2 stacks), each granting +30% Heavy Attack DMG Bonus to Qiuyuan (total up to +60%); when at max Bamboo Cleaver stacks, casting Resonance Skill refreshes duration; additionally: casting Intro Skill grants all team Resonators +20% Echo Skill DMG Bonus for 30 seconds
- This signature weapon simultaneously addresses Crit Rate (reducing gear pressure), amplifies Heavy Attack DMG (directly boosting Inkwash and Thus Spoke the Blade chain), and provides a team-wide Echo Skill DMG Bonus on Intro — synergizing with and extending Bamboo's Shade's duration and scope
- The team +20% Echo Skill DMG Bonus on Intro stacks with Bamboo's Shade for a combined +50% Echo Skill DMG Bonus (Bonus, not Amplification) to all active Resonators from Qiuyuan's kit alone

**Strong 5-Star Alternative — Emerald of Genesis**
- Stat: Energy Regen (+12.8%); assists reaching the Energy threshold for reliable Liberation cycling with 125 Energy cost
- Passive: ATK increases on Resonance Skill cast (up to +12% stacking); provides a useful secondary ATK buff on skill use
- Recommended when Liberation cycling is difficult without the Energy Regen primary stat; available from the standard banner and not limited

**4-Star Options**
- **Lumingloss (Battle Pass, R5 preferred):** Passive amplifies Heavy Attack and Basic Attack DMG on Resonance Skill cast by up to +64% at R5; directly relevant to Inkwash and To Sacrifice chain; competitive with Emerald of Genesis at R5 for personal DPS builds; requires Battle Pass investment
- **Somnoire Anchor:** Builds stacking ATK and Crit Rate over time; at maximum stacks reaches +40% ATK and +12% Crit Rate; usable but requires time to stack
- **Red Spring:** ATK primary stat; Basic Attack DMG Bonus stacking; less synergistic with Qiuyuan's Echo Skill focus than the above options but accessible

**Build Note:**
Multiple sources (Prydwen, Tacter) specifically flag S1 vs Emerald Sentence as the primary investment comparison: S1 provides +20% Crit Rate (reducing gear pressure significantly) plus interruption immunity on the burst chain; the signature weapon provides more raw damage output. For players who do not have S1, the signature is the clear weapon choice; for S1 holders, non-signature weapons remain fully viable while reducing the echo-building investment required.

## Qiuyuan: Best Teams

**Primary Team — Echo Skill Core: Qiuyuan / Galbrena / Shorekeeper (or Verina)**
- **Qiuyuan** (Sub-DPS / Buffer): Outro applies +50% Echo Skill DMG Amplification + Moonlit Clouds +22.5% ATK to Galbrena; Bamboo's Shade active (+30% Echo Skill DMG Bonus) during Galbrena's on-field time; Liberation provides up to +30% Crit DMG to Galbrena; all three buffing layers active simultaneously during Galbrena's rotation
- **Galbrena** (Main DPS): Primary beneficiary; deals a significant portion of her damage through Echo Skills; all three Qiuyuan buffs are relevant to her kit; considered the best current pairing for Qiuyuan in Version 2.7
- **Shorekeeper** (Support/Healer): Universal healing, damage amplification from Outro; Spectro DMG amplification; recommended for premium account; Verina is a strong alternative for ATK buffing and sustain

**Echo Skill Alternative — Havoc: Qiuyuan / Phrolova / Cantarella**
- Game8 describes this composition as Qiuyuan effectively replacing Roccia in the Mono Havoc team to provide team-wide Echo Skill DMG buffs; each member buffs the next in rotation
- **Phrolova:** Liberation with Hecate scales off Echo Skill DMG; Outro grants Heavy Attack DMG amplification (complementary with Qiuyuan's Heavy Attack Inkwash chain)
- **Cantarella:** Multiple Echo Skill casts via abilities; Coordinated Attacks from Liberation; provides Havoc DMG and Resonance Skill DMG amplification; benefits significantly from Qiuyuan's Echo Skill buffs
- Limitation noted by lootbar.gg: since Phrolova leaves the field after her Liberation, Qiuyuan's Outro Echo Skill Amplification (which applies only to the active character) is less effective for her specifically — Cantarella is the primary intended Outro recipient in this composition

**General Sub-DPS Support: Qiuyuan / [Echo-focused DPS] / [Healer]**
- Any DPS whose primary damage output is meaningfully weighted toward Echo Skills benefits from Qiuyuan's Outro and Bamboo's Shade
- Characters without significant Echo Skill damage (e.g., Jiyan, Encore, Changli) do not fully utilize Qiuyuan's buffing profile; in these compositions he functions primarily as an Aero Sub-DPS with Crit DMG buffing from Liberation, which is useful but no longer unique

## Qiuyuan: Rotation Guide

**Standard Intro Entry Rotation (Optimal)**
1. Enter via Intro Skill: Attack the Must-Defend
   → +400 Swordster's Soliloquy instantly (200 threshold: Inkwash active; 400 threshold: Bamboo's Shade active → team +30% Echo Skill DMG Bonus for 30s)
   → Next Normal Attack chains directly into Inkwash Stage 3
2. Basic Attack (Inkwash Stage 3): +100 Swordster's Soliloquy → at 500 pts
3. Basic Attack (Inkwash Stage 4): +100 Swordster's Soliloquy → at 600 pts → **Inksplash of Mind triggered**
4. Resonance Liberation: Sundering Strike
   → Echo Skill DMG (amplified by Bamboo's Shade); team Crit DMG buff (up to +30% for 30s if ≥65% CR)
   → Cast Liberation before the Thus Spoke the Blade chain so the Crit DMG buff is active during the burst
5. Echo Skill use (Main Echo): cast Impermanence Heron or Feilian Beringal just before or after Liberation to sync buffs with the burst window; Heron grants +10 Energy to Qiuyuan on hit
6. Hold Normal Attack (Inksplash of Mind): To Teach → To Save → To Sacrifice
   → All three classified as Heavy Attack DMG + Echo Skill DMG
   → All three amplified by Bamboo's Shade (+30% Echo Skill Bonus)
   → All three boosted by Quietude Within (+50% DMG if IS1 fired)
   → To Sacrifice restores 30 Concerto Energy on hit
7. Optional: Resonance Skill: Through the Groves (hold variant) for additional Echo Skill DMG hit and Concerto Energy; animation-cancel for speed
8. Swap out → Outro Skill: Strike Before Ready fires
   → Aero Echo Skill DMG to target (100% ATK)
   → Incoming Main DPS receives +50% Echo Skill DMG Amplification for 14s
   → Moonlit Clouds set fires (if equipped): incoming character also gets +22.5% ATK for 15s

**Total on-field time:** Approximately 5–7 seconds in the optimized Intro path; the most efficient Sub-DPS field window in current Version 2.7 for his support role.

**Energy Management**
- Qiuyuan's Liberation costs 125 Energy; without investment in Energy Regen, reaching this threshold each rotation requires additional planning
- Target ~130% Energy Regen (via sub-stats or Emerald of Genesis) to ensure reliable Liberation casting each rotation
- To Sacrifice (Inherent Skill 1) restores 30 Concerto Energy on hit; the S3 enhanced chain has each hit restore 30 Concerto Energy
- Impermanence Heron main echo grants +10 Resonance Energy on hit; useful for closing Liberation energy gaps
- Resonance Skill (hold variant) generates 10 Concerto Energy at the cost of field time; optional inclusion at the end of the rotation

**Bamboo's Shade Duration Management**
- Bamboo's Shade lasts 30 seconds from the moment 400 Swordster's Soliloquy is reached
- In the Intro entry rotation, the buff is active from the moment Qiuyuan arrives; 30 seconds is generally sufficient to cover: the rest of Qiuyuan's rotation (~5–7s) + the Main DPS's rotation (~15–20s) + a second character's rotation if needed
- The 30-second window means the buff is typically refreshed once per full team rotation cycle if the rotation is kept tight

## Qiuyuan: Sources

- Prydwen Institute — Qiuyuan build guide, full skill multipliers, rotation analysis: https://www.prydwen.gg/wuthering-waves/characters/qiuyuan/
- Wutheringlab — Qiuyuan build guide, auto-parry mechanic explanation: https://wutheringlab.com/character/qiuyuan-build/
- Game8 — Qiuyuan best builds, teams, skill priority, echo sets: https://game8.co/games/Wuthering-Waves/archives/524882
- Lootbar.gg — Qiuyuan build guide, team analysis: https://lootbar.gg/blog/en/wuthering-waves-qiuyuan-build-guide.html
- LDShop build guide — Qiuyuan weapon comparison and rotation tips: https://www.ldshop.gg/blog/wuthering-waves/qiuyuan-build-guide.html
- Tacter — Qiuyuan S0 guide, S1 vs Emerald Sentence analysis: https://www.tacter.com/wuthering-waves/guides/best-s0-qiuyuan-guide-and-build-best-echoes-weapons-and-teams-wuthering-waves-27-6e2a4605
- TopUpLive — Qiuyuan full kit with Resonance Chain details: https://www.topuplive.com/news/wuwa-2-7-qiuyuan-best-build.html
