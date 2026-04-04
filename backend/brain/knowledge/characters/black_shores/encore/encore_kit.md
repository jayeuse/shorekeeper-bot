---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/new_federation/encore/encore_kit.md
character: Encore
group: New Federation / Black Shores
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - fusion
  - rectifier
  - main-dps
  - cosmos-rave
  - permanent-banner
  - beginner-friendly
---

# Encore Kit Documentation
<!-- Sources: https://wuthering.gg/characters/encore, https://www.prydwen.gg/wuthering-waves/characters/encore/, https://wutheringlab.com/character/encore-build/, https://game8.co/games/Wuthering-Waves/archives/454221, https://www.pockettactics.com/wuthering-waves/encore -->

## Encore: Combat Archetype and Role

- **Element:** Fusion
- **Weapon Type:** Rectifier
- **Role:** Main DPS — dual-state Cosmos Rave hypercarry
- **Archetype:** Liberation-empowered Basic Attack DPS; transformed-state sustained damage dealer
- **Introduced:** Version 1.0 (launch); Permanent Banner and Beginner's Choice Convene

Encore is Wuthering Waves' most beginner-accessible 5-star Main DPS, available to every player from day one on the permanent banner. Her combat identity is built around a clean two-phase structure: a standard phase where she builds Resonance Energy and Mayhem via Basic Attacks and Resonance Skill, and a **Cosmos Rave** phase (entered via Resonance Liberation) where Cosmos runs wild, her Basic Attacks are fully replaced by enhanced versions, and approximately 70% of her total damage is generated in a tight 10-second window. She does not require swap-cancel expertise or complex state management — her rotation is legible, her feedback is immediate, and her ceiling is meaningfully higher with good play but not locked behind it. She can be run as a Hyper Carry with maximum field time or in Quick Swap compositions where she receives buffs, fires her Liberation window, and rotates out efficiently.

## Encore: Key Resources (Forte Mechanics Overview)

Encore's Forte Circuit tracks one resource: **Mayhem** (also called Dissonance in some sources), capping at 100. It is generated during normal combat and consumed to access her finishing move — **Cloudy Frenzy** (outside Liberation) or **Cosmos Rupture** (inside Cosmos Rave). Both are Liberation-counted damage events, meaning they benefit from Liberation DMG Bonus buffs.

- **Mayhem** is generated when Normal Attack: Wooly Attack hits a target and when Resonance Skill Flaming Woolies hits a target
- When Mayhem is full (100), the Heavy Attack input changes into **Heavy Attack: Cloudy Frenzy** (outside Liberation) or **Heavy Attack: Cosmos Rupture** (inside Cosmos Rave)
- During both Mayhem-consuming states, Encore takes **70% reduced damage** — a meaningful defensive bonus for a glass-cannon DPS
- Switching characters does NOT interrupt the Mayhem state — she finishes the animation regardless of roster swap
- **Cosmos Rupture** (in-Liberation version) additionally triggers an S4 effect: all team members gain +20% Fusion DMG Bonus for 30 seconds, making the Cosmos Rupture finish a team-wide buff delivery

## Encore Forte Circuit: Mayhem

**Mayhem Generation**
- **Normal Attack: Wooly Attack hits:** Restores Mayhem per hit (rate confirmed by wuthering.gg; specific per-hit value should be verified with Fandom Wiki)
- **Resonance Skill Flaming Woolies hits:** Restores Mayhem on hit
- **Cap:** 100 Mayhem

**Mayhem Consumption Paths**

*Outside Cosmos Rave:*
- At 100 Mayhem → Heavy Attack input becomes **Heavy Attack: Cloudy Frenzy**
- Summons Cloudy for a finishing attack; deals Fusion DMG counted as Resonance Liberation DMG
- 70% DMG reduction while charging; completes even if Encore swaps off during animation

*Inside Cosmos Rave:*
- At 100 Mayhem → Heavy Attack input becomes **Heavy Attack: Cosmos Rupture**
- Higher multiplier than Cloudy Frenzy; deals Fusion DMG counted as Resonance Liberation DMG
- 70% DMG reduction while charging; completes even if Encore swaps off during animation
- **S4 effect on trigger:** All team members gain +20% Fusion DMG Bonus for 30s

**Rotation Principle:** In the standard Cosmos Rave burst window (10 seconds), Encore should accumulate Mayhem as fast as possible via the enhanced Cosmos: Frolicking chain and Cosmos: Rampage, then fire Cosmos Rupture at the end before the window closes. Never fire the Mayhem Heavy Attack at the start of Liberation — it truncates the Cosmos Rave state.

## Encore: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | ~762 | ~35 | ~80 |
| Lv. 20 | ~1,980 | ~91 | ~208 |
| Lv. 40 | ~3,770 | ~173 | ~397 |
| Lv. 60 | ~6,090 | ~279 | ~641 |
| Lv. 80 | ~8,380 | ~384 | ~882 |
| Lv. 90 | ~9,540 | ~437 | ~1,004 |

*Note: Approximate figures before Forte Attribute Bonuses and equipment. Cross-reference Wuthering Waves Fandom Wiki for confirmed values.*

## Encore: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | Whisperin Core (Lv.1) ×4, Pecok Flower ×4, Shell Credits ×5,000 |
| 2 | 40→50 | Whisperin Core (Lv.2) ×4, Pecok Flower ×8, Shell Credits ×10,000 |
| 3 | 50→60 | Whisperin Core (Lv.3) ×8, Pecok Flower ×12, Rage Tacet Core ×4, Shell Credits ×15,000 |
| 4 | 60→70 | Whisperin Core (Lv.3) ×8, Pecok Flower ×16, Rage Tacet Core ×8, Shell Credits ×20,000 |
| 5 | 70→80 | Whisperin Core (Lv.4) ×12, Pecok Flower ×20, Rage Tacet Core ×12, Shell Credits ×40,000 |
| 6 | 80→90 | Whisperin Core (Lv.4) ×12, Pecok Flower ×24, Rage Tacet Core ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Whisperin Cores (Tier 1–4):** Dropped by Whisperin Tacet Discords throughout the map; also purchasable from the store or via Synthesis
- **Pecok Flower:** Found in the wild around Taoyuan Village and Tiderise Cliff; also purchasable from Shifang Pharmacy in Jinzhou
- **Rage Tacet Core:** Dropped by the **Inferno Rider** boss (Sea of Flames, Port City of Guixu, Huanglong)

## Encore: Character Kit: Basic Attack — Wooly Attack

**Standard Phase (4-stage chain)**
- Encore performs up to 4 consecutive attacks with her Rectifier, dealing Fusion DMG
- Stage 4 has a notably long animation that can be cancel-shortened via Dodge or Resonance Skill input — important for advanced play to maintain DPS during long channels
- Each hit restores Mayhem on contact
- **Heavy Attack:** Hold Basic Attack to charge; deals Fusion DMG at Stamina cost; triggers Cloudy Frenzy if Mayhem is at 100 (outside Liberation)
- **Dodge Counter:** After successful Dodge, attack the target dealing Fusion DMG

**Normal Attack: Wooly Strike** (variant triggering Inherent Skill 2 bonus)
- When Wooly Strike hits: additionally restores 10 Resonance Energy — once per 10 seconds
- This bonus Energy restore is an important factor in Liberation uptime calculations; it reduces reliance on external Energy Regen support

**Cosmos Rave Phase — Basic Attack Replacement**
All standard Basic Attack inputs are replaced by **Cosmos: Frolicking** during Cosmos Rave:
- Up to 4 consecutive attacks, dealing Fusion DMG counted as Basic Attack DMG
- Higher multipliers than standard Wooly Attack; approximately 70% of total DPS is generated here
- **Cosmos: Heavy Attack:** Replaces Heavy Attack inside Liberation; consumes Stamina; triggers Cosmos Rupture if Mayhem at 100
- **Cosmos: Dodge Counter:** Replaces standard Dodge Counter inside Liberation; Fusion DMG, counted as Basic Attack DMG

## Encore: Character Kit: Resonance Skill — Flaming Woolies / Energetic Welcome

Encore's Resonance Skill operates in two sequential triggers:

**Flaming Woolies (First Press)**
- Encore summons Cloudy and Cosmos to attack the target with burning rays, dealing Fusion DMG
- Restores Mayhem on hit
- Triggers **Inherent Skill 1 buff:** +10% Fusion DMG Bonus for 10s after cast
- Triggers **Inherent Skill 1 Basic Attack buff:** +3% Fusion DMG Bonus per Basic Attack hit, stacking up to 4 times for 6s
- The second press triggers Energetic Welcome — Encore can swap off immediately after the first press animation begins and return to trigger the follow-up (a useful swap-cancel window)

**Energetic Welcome (Second Press / Follow-up)**
- After casting Flaming Woolies, a second Resonance Skill press launches Energetic Welcome — a follow-up attack dealing Fusion DMG
- Triggers **Inherent Skill 2 Energy restore** (if applicable)
- Does NOT apply in Cosmos Rave (replaced by Cosmos: Rampage)

**Cosmos Rave Replacement — Cosmos: Rampage**
- During Cosmos Rave, Flaming Woolies is replaced by **Cosmos: Rampage**: Cosmos attacks the target with uncontrollable flames, dealing Fusion DMG counted as Resonance Skill DMG
- Cooldown for Cosmos: Rampage is **independent** from normal Flaming Woolies cooldown — both can be used in the same rotation cycle
- Triggers Inherent Skill 1 Fusion DMG bonus on cast

## Encore: Character Kit: Resonance Liberation — Cosmos Rave

- **Activation:** Consumes 125 Resonance Energy
- **Effect:** Encore loses control and Cosmos breaks free, wreaking havoc; all Basic Attacks, Heavy Attacks, Resonance Skill, and Dodge Counter are replaced with enhanced Cosmos versions
- **Duration:** 10 seconds of active Cosmos Rave state
- **Key damage window:** All enhanced Cosmos attacks during this 10s window; the standard rotation targets approximately 3 Basic Attack chains + 1–2 Cosmos: Rampage uses + Cosmos Rupture Heavy Attack before the window closes
- **Generating more damage:** Dodge Counter after Liberation → links directly to Cosmos: Frolicking Stage 3 (no loss in chain progression), allowing recovery from interrupted attack strings without restarting the chain from Stage 1

**Liberation Damage**
- Cosmos Rave activation itself deals Fusion DMG on cast (AoE)
- All Cosmos: Frolicking attacks deal Fusion DMG counted as Basic Attack DMG
- Cosmos Rupture (at full Mayhem) deals Fusion DMG counted as Resonance Liberation DMG — one of the largest single-hit events in Encore's kit

**Inherent Skill Interaction**
- S6 interaction: During Cosmos Rave, every damage event grants Encore 1 stack of "Lost Lamb" (+5% ATK per stack, up to 5–6 stacks, 10s duration) — stacks very rapidly during the active Cosmos Rave window, effectively granting up to +25–30% ATK during the burst phase

## Encore: Inherent Passives

**Inherent Skill 1 — Flaming Heart**
- When Flaming Woolies or Cosmos: Rampage is cast: Encore gains **+10% Fusion DMG Bonus** for 10 seconds
- When Basic Attack hits a target: Encore gains **+3% Fusion DMG Bonus** per hit, stacking up to **4 times** for 6 seconds (max +12%)
- Cumulative potential from both effects: +22% Fusion DMG Bonus when fully stacked alongside an active Flaming Woolies cast — persistent across most of her active combat time

**Inherent Skill 2 — Energetic**
- When casting Basic Attack Wooly Strike or Resonance Skill Energetic Welcome: Encore additionally restores **10 Resonance Energy**
- Trigger: Once every 10 seconds
- This passive meaningfully reduces Liberation cooldown in longer rotations and is the main reason Encore does not require extreme Energy Regen investment compared to some other DPS characters

## Encore: Intro/Outro Skills

**Intro Skill — Little Devil**
- Triggered when Encore enters the field via swap
- Deals Fusion DMG to the target on entry
- Provides a small burst of Resonance Energy and/or Concerto Energy on activation
- The Intro Skill gives Encore an immediate combat entry in Quick Swap compositions without needing to build into the chain first

**Outro Skill — Woolies Go!**
- Triggered when Encore swaps off-field (Concerto Energy full)
- Effect: The next Resonator that enters gains a **+20% Fusion DMG Amplification** for 14 seconds (or until they swap off)
- This Outro makes Encore unexpectedly functional as a buffer in Dual DPS compositions: Changli, Brant, and any other Fusion or skill-heavy DPS character benefits directly from this 14-second window

## Encore: Skill Upgrade Materials

| Skill Level | Key Materials |
|-------------|---------------|
| 1→2 | Cadence Bead (Lv.1) ×4, Whisperin Core ×2, Shell Credits ×1,000 |
| 2→3 | Cadence Bead (Lv.2) ×4, Whisperin Core ×4, Shell Credits ×3,000 |
| 3→4 | Cadence Bead (Lv.3) ×8, Whisperin Core ×8, Shell Credits ×8,000 |
| 4→5 | Cadence Bead (Lv.4) ×4, Ring of Echos ×2, Whisperin Core ×12, Shell Credits ×20,000 |
| 5→6 | Cadence Bead (Lv.4) ×4, Ring of Echos ×3, Whisperin Core ×16, Shell Credits ×40,000 |
| 6→7 | Cadence Bead (Lv.4) ×8, Ring of Echos ×5, Whisperin Core ×20, Shell Credits ×80,000 |
| 7→8 | Cadence Bead (Lv.4) ×8, Ring of Echos ×8, Whisperin Core ×24, Shell Credits ×120,000 |
| 8→9 | Cadence Bead (Lv.4) ×16, Ring of Echos ×12, Whisperin Core ×28, Shell Credits ×160,000 |
| 9→10 | Cadence Bead (Lv.4) ×16, Ring of Echos ×16, Whisperin Core ×40, Shell Credits ×200,000 |

**Total Forte Shell Credits (all skills):** ~2,030,000
- **Cadence Beads:** Rectifier Forgery Challenge rewards
- **Ring of Echos (weekly boss material):** Verify exact drop source via the Fandom Wiki
- **Whisperin Cores:** General Tacet Discord drops throughout the map

**Skill Leveling Priority:** Resonance Liberation first (scales all Cosmos Rave damage directly) → Resonance Skill second (Flaming Woolies multipliers and Cosmos: Rampage) → Forte Circuit third (Mayhem Heavy Attack multipliers) → Basic Attack last (lowest proportion of total damage)

## Encore: Resonance Chains (Sequences)

**S1 — Fluffy Arsonist**
- When Normal Attack (Basic Attack) hits a target: Encore's **Fusion DMG Bonus is increased by +3%** for 6 seconds, stacking up to **4 times** (max +12%)
- *Impact:* Stacks quickly during her Basic Attack chain inside Cosmos Rave; the +12% Fusion DMG Bonus is meaningful but modest. Approximately +5–7% personal DPS increase. Solid first sequence; the stacking nature means it benefits heavily from consistent Basic Attack chains in Liberation.

**S2 — Little Sheep Running**
- When Encore casts a Basic Attack or Resonance Skill: additionally restores **Resonance Energy** (exact amount per cast should be verified with the Fandom Wiki)
- *Impact:* Reduces Liberation downtime between rotations; Encore's greatest weakness outside Cosmos Rave is limited damage — S2 gets her back into Liberation faster. Approximately +8–12% overall DPS increase due to higher Liberation frequency. High practical value.

**S3 — Woolie's Fury**
- Increases the DMG Multiplier of **Heavy Attack: Cloudy Frenzy** and **Heavy Attack: Cosmos Rupture** by **+40%**
- *Impact:* Cosmos Rupture is one of the highest single-hit events in Encore's kit; a +40% multiplier amplification is substantial. Approximately +10–14% personal DPS increase. Notably valuable in rotations that reliably reach full Mayhem inside Cosmos Rave.

**S4 — Rosy Cheeks**
- After casting **Heavy Attack: Cosmos Rupture**: all team members gain **+20% Fusion DMG Bonus** for 30 seconds
- *Impact:* Transforms Encore into a team-wide Fusion buffer. The 30-second duration covers most full rotation cycles, meaning every teammate with Fusion scaling benefits. Changli, Brant, and Encore herself gain from this. Approximately +10–15% team DPS increase in Fusion-heavy compositions. The standout support-value sequence.

**S5 — Wildfire**
- **Resonance Skill DMG Bonus is increased by +35%**
- *Impact:* A flat amplification to all Flaming Woolies and Cosmos: Rampage damage. Both scale off ATK; +35% to their multiplier is a meaningful boost. Approximately +8–12% personal DPS increase. Good stopping point for invested players.

**S6 — Blazing Heart**
- During Resonance Liberation Cosmos Rave: Encore gains **1 stack of "Lost Lamb"** every time she deals damage, each stack increasing her **ATK by +5%** for 10 seconds, stacking up to **5 times** (some sources say 6 times — cross-reference Fandom Wiki for confirmed cap)
- *Impact:* She deals damage extremely rapidly during Cosmos Rave — stacks fill within the first few seconds, granting up to +25–30% ATK before the window closes. This ATK bonus multiplicatively amplifies everything in the Cosmos Rave window simultaneously. Approximately +15–20% personal DPS increase. Full S6 transforms her Liberation window into a self-sustaining damage escalator.

**Sequence Pull Priority:** S0 is competitive for a permanent banner character. S2 (Liberation uptime) and S3 (Cosmos Rupture multiplier) are the standout practical upgrades. S4 for team-wide Fusion buff value. Since Encore is on the permanent banner, sequences accumulate naturally over time — no emergency investment required.

## Encore: Recommended Echo Sets

**Best-in-Slot: Molten Rift (5-piece)**
- Standard best-in-slot for Encore; provides Fusion DMG Bonus that scales with her Liberation-empowered attacks
- Simple activation requirement; reliable across all play styles and compositions
- **Main Echo: Inferno Rider** — transforms into the Inferno Rider for 3-hit combo dealing Fusion DMG; on completion, increases current Resonator's **Fusion DMG Bonus by +12%** and **Basic Attack DMG Bonus by +12%** for 15 seconds; both bonuses directly amplify Cosmos: Frolicking (her main Basic Attack damage in Liberation)
- The Inferno Rider Echo is the ideal main Echo choice because it buffs the two exact damage types that constitute the majority of Encore's Cosmos Rave output: Fusion and Basic Attack

**Echo Main Stats Priority**
- 4-Cost Echo: CRIT Rate or CRIT DMG (whichever closes the 1:2 ratio); CRIT Rate preferred if using Cosmic Ripples or non-CRIT weapon
- 3-Cost Echoes (×2): Fusion DMG Bonus (primary) or ATK% (secondary); double Fusion DMG Bonus is optimal; the gap vs. Fusion + ATK% hybrid is small — prioritize sub-stat quality
- 1-Cost Echoes: ATK% (sub-stats are more valuable than main stats at this tier)

**Sub-Stat Priority:** Energy Regen (to ~130% breakpoint) ≥ CRIT Rate = CRIT DMG > ATK% > Fusion DMG Bonus > Flat ATK

**Note on Energy Regen:** Encore has an internal Energy Regen source (Inherent Skill 2) that reduces her ER threshold compared to characters without it. Avoid over-investing in ER substats at the expense of CRIT stats once the breakpoint is reached.

## Encore: Best Weapon

**Best-in-Slot (Limited) — Stringmaster (5-Star Rectifier, Yinlin's Signature)**
- Highest DPS output for Encore despite being another character's signature
- Stat: CRIT Rate (efficient for build targeting)
- Effect: +12% DMG bonus to all damage; ATK buff stacking on Resonance Skill use — both conditions are trivially met in Encore's rotation; the CRIT Rate stat reduces Echo sub-stat pressure

**Best-in-Slot (Standard) — Cosmic Ripples (5-Star Rectifier)**
- Available on the standard banner; excellent long-term investment
- Stat: ATK% or Energy Regen (verify specific stat with Fandom Wiki)
- Effect: Stacking **Basic Attack DMG Bonus** on Basic Attack hits — directly amplifies Cosmos: Frolicking, which constitutes ~70% of Encore's Liberation window damage; also provides Energy Regen to support Liberation uptime
- Recommended as the primary target for players who do not have or want Stringmaster

**Top 4-Star Alternative — Augment (4-Star Rectifier)**
- Provides CRIT Rate as a base stat (especially valuable at higher refinements)
- Passive: Massive ATK buff while Resonance Liberation is active — perfectly timed for the Cosmos Rave window
- Best 4-star option by a clear margin; accessible from in-game sources

**F2P Alternative — Variation (4-Star Rectifier)**
- ATK% stat with a passive that provides CRIT Rate stacks on Resonance Skill use
- Viable for early game; outperformed by Augment but accessible without event or limited pulls

## Encore: Best Teams

**Premium Hyper Carry — Encore / Lupa / Shorekeeper**
- **Encore** (Main DPS): Full Cosmos Rave burst cycle; maximum field time
- **Lupa** (Sub DPS / Buffer): Provides Fusion DMG Amplification and significant personal damage; introduced in later versions as one of Encore's strongest teammates
- **Shorekeeper** (Support): CRIT Rate + CRIT DMG Stellarealm buff; healing; universal best-in-slot support
- *Rotation:* Shorekeeper Liberation → Shorekeeper Outro → Lupa rotation + Outro → Encore Intro → Normal attacks to build Energy → Liberation → Cosmos Rave burst → Cosmos Rupture finish → Outro (feeds +20% Fusion DMG to next character)

**Best F2P Duo — Encore / Sanhua / Verina (or Baizhi)**
- **Encore** (Main DPS): Core damage dealer; Liberation burst primary window
- **Sanhua** (Sub DPS / Buffer): Best practical teammate for Encore; her Outro provides **+38% Basic Attack DMG Amplification** — which directly amplifies Cosmos: Frolicking (~70% of Encore's DPS); extremely fast rotation ensures Encore always enters field with Sanhua's buff active; Sanhua + Encore is widely cited as the strongest accessible F2P duo in Version 1.x
- **Verina** (Support/Healer): Best healer at launch; provides ATK buff and sustain; Baizhi is the F2P alternative
- *Rotation:* Verina/Baizhi → Sanhua rotation + Outro → Encore Intro → build Energy → Liberation + Cosmos Rave → Cosmos Rupture → Outro (Sanhua re-enters or support re-enters)

**Dual DPS — Encore / Changli / Shorekeeper**
- **Changli** (Sub DPS): Delivers Liberation + Flaming Sacrifice burst first; Outro provides **+20% Fusion DMG + 25% Liberation DMG Amplification** feeding directly into Encore's Liberation entry
- **Encore** (Main DPS): Enters on Changli's Outro; the Fusion DMG Amplification amplifies the entire Cosmos Rave window; Liberation DMG Amplification amplifies Cosmos Rupture finish
- **Shorekeeper** (Support): Universal buffs and CRIT stats
- *Challenge:* More mechanically demanding than Sanhua team; Changli's rotation is complex; Encore benefits most from Fusion DMG portion of Outro; requires coordinating two short burst windows

**Dual DPS — Encore / Brant / Healer**
- **Brant** (Sub DPS): Delivers his Forte ability (Returned from Ashes); Outro provides **Resonance Skill DMG + Fusion DMG Amplification** — Encore benefits from both buffs during Cosmos Rave (Cosmos: Rampage is Skill DMG; Cosmos: Frolicking and Rupture are Fusion DMG)
- **Encore** (Main DPS): Full Liberation window amplified by Brant Outro
- **Healer (Verina/Shorekeeper):** Sustain and additional buffs
- *Note:* Encore must follow Brant in the swap order to receive the Outro buff; rotation sequencing matters more here than in Sanhua team

## Encore: DPS Benchmarks

- Encore is evaluated as a solid A-tier to S-tier Main DPS across Version 1.x, with her rating improving at higher Resonance Chain investments and in compositions built around her
- Her primary strength is **accessibility and reliability**: zero execution barrier for basic play; very high damage ceiling in Liberation; always available to every player on the permanent banner
- Her primary weakness is **Liberation dependency**: outside Cosmos Rave, her damage is significantly lower than on-field alternatives, making Energy Regen a critical stat and Liberation downtime a notable DPS loss
- At S0 with Stringmaster or Cosmic Ripples, paired with Sanhua or Lupa and a strong support, she clears all Version 1.x endgame content comfortably
- At S6 with full investment and premium team, her Liberation window output is competitive with limited 5-stars; the S6 "Lost Lamb" ATK stacking rapidly amplifies the entire Cosmos Rave burst
- As noted in Wutheringlab's analysis: her single-cycle multiplier output in Liberation is comparable to Jiyan and other premier carries at equivalent investment levels
- Her reputation as a "beginner character" is accurate in terms of accessibility, but misleading as a ceiling assessment — she rewards investment with strong returns

## Encore: Sources

- Wuthering.gg — Encore kit, Forte mechanics, and full skill descriptions: https://wuthering.gg/characters/encore
- Prydwen Institute — Encore build guide, DPS analysis, team recommendations: https://www.prydwen.gg/wuthering-waves/characters/encore/
- Wutheringlab — Encore build, rotation, damage breakdown: https://wutheringlab.com/character/encore-build/
- Game8 — Encore best builds, teams, combos: https://game8.co/games/Wuthering-Waves/archives/454221
- Pocket Tactics — Encore weapon, echo, and material guide: https://www.pockettactics.com/wuthering-waves/encore
- DBLTAP — Encore full build guide including resonance chains: https://www.dbltap.com/guides/wuthering-waves-encore-build-guide
- LDShop — Encore best full build guide: https://www.ldshop.gg/blog/wuthering-waves/encore-build.html
- SI.com Video Games — Encore build (resonance chain breakdown): https://videogames.si.com/guides/wuthering-waves-encore
