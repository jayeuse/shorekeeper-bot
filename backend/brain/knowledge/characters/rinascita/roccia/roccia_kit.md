---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/ragunna_characters/roccia/roccia_kit.md
character: Roccia
group: Ragunna
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - havoc
  - gauntlets
  - sub-dps
  - buffer
  - enabler
  - imagination
  - beyond-imagination
  - real-fantasy
  - flat-atk-buff
  - grouping
  - magic-box
---

# Roccia Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/roccia/, https://game8.co/games/Wuthering-Waves/archives/486246, https://wuthering.gg/characters/roccia, https://lootbar.gg/blog/en/wuthering-waves-roccia-kit.html, https://genshin-builds.com/en/wuthering-waves/characters/roccia -->

## Roccia: Combat Archetype and Role
- **Element/Attribute:** Havoc
- **Weapon Type:** Gauntlets
- **Role:** Sub-DPS / Havoc Enabler — deals personal Havoc Heavy Attack DMG through three aerial bounce attacks (Real Fantasy) while providing a Flat ATK team buff (up to 200 ATK) from Resonance Liberation, enemy grouping via Resonance Skill and Inherent Skill (Magic Box), and 25% Basic Attack DMG + 20% Havoc DMG Amplification via Outro; the best grouping unit in the game by most community consensus
- **Scaling:** ATK (standard ATK-based Havoc damage; CRIT DMG is the Forte node sub-stat, making CRIT Rate the primary gap to fill through gear)
- **Damage Profile:** Heavy Attack DMG — the "Real Fantasy" bounce attacks are labeled Basic Attacks but count as Heavy Attack DMG; Liberation is also Heavy Attack DMG; personal damage is concentrated in the Beyond Imagination window
- **Best-fit Teams:** Havoc-focused mono-element teams; Camellya + Roccia (S-tier); Havoc Rover + Roccia; any Basic Attack-focused Havoc DPS who benefits from +25% Basic Attack DMG Amplification; strong in AoE-heavy content due to unmatched grouping
- **Key distinction:** First character in WuWa to provide a Flat ATK buff (additive ATK points post-calculation rather than an ATK% multiplier), making her buff more valuable in builds with high ATK% investment

## Roccia: Key Resources (Forte Mechanics Overview)

Roccia's entire gameplay revolves around a single resource: **Imagination** (0–300). It is generated through Normal Attacks, the Heavy Attack charge (hold duration increases generation), Resonance Skill — Acrobatic Trick (+100 on cast), and Intro Skill — Pero, Help (+100 on cast). The threshold for accessing her aerial attack mode is 100 Imagination: at 100+, she can enter **Beyond Imagination** and execute **Basic Attack — Real Fantasy**, her signature aerial bounce sequence.

Beyond Imagination is the airborne state entered after the Resonance Skill or a sufficiently charged Heavy Attack. In this state, each Real Fantasy bounce consumes 100 Imagination and sends Roccia into a weighted aerial plunge — she lands, immediately launches back airborne, and the next bounce is available. Up to 3 consecutive Real Fantasy bounces are possible per full Imagination bar. The first two bounces re-enter Beyond Imagination if Imagination remains; the third is a finisher that does not.

The resource challenge is building to 300 Imagination per rotation. Intro Skill provides 100, Resonance Skill provides 100, and Normal Attacks (specifically BA4 after the Intro Skill) provide the remaining 100 needed. At S1, the Resonance Skill provides 200 Imagination total (100 base + 100 additional), allowing the BA4 Normal Attack step to be skipped entirely — reducing field time while maintaining full 3-bounce output.

## Roccia Forte Circuit: Imagination / Beyond Imagination

**Imagination (0–300):**
- Normal Attacks: restore Imagination on hit
- Heavy Attack (hold to charge): restores Imagination while charging; continues charging even after STA is depleted
- Resonance Skill — Acrobatic Trick: +100 Imagination on cast
- Intro Skill — Pero, Help: +100 Imagination on cast
- At 100+ Imagination with a target hit by Heavy Attack: enters **Beyond Imagination** state

**Beyond Imagination state:**
- Roccia is airborne; exits if she lands without triggering a bounce or is switched off field
- At 100+ Imagination: press Basic Attack to cast **Basic Attack — Real Fantasy** (consumes 100 Imagination)
- After Real Fantasy Stage 1 and Stage 2: if over 100 Imagination remain, Roccia relaunches into mid-air and re-enters Beyond Imagination
- 3 consecutive bounces maximum per Beyond Imagination window (300 Imagination consumed total)

**Basic Attack — Real Fantasy multipliers (Lv. 1; all Heavy Attack DMG):**
- Stage 1: 162.00%
- Stage 2: 171.00%
- Stage 3: 180.00%
- Concerto Regen: 10 / 16 / 25 (total: 51 per full 3-bounce sequence)

*The 51 Concerto Regen from a full 3-bounce Real Fantasy sequence is the primary mechanism for reaching full Concerto Energy in time to use Outro Skill after Liberation.*

## Roccia: Stats Baseline

| Stat | Lv. 1 | Lv. 90 |
|------|-------|--------|
| HP | ~920 | 12,250 |
| ATK | ~27 | 375 |
| DEF | ~88 | 1,198 |
| CRIT Rate | 5% | 5% |
| CRIT DMG | 150% | 150% (+16% from Forte nodes) |
| Energy Regen | 100% | 100% |
| Max Resonance Energy | 125 | 125 |

Forte minor nodes add: +16% CRIT DMG and +12% ATK% at full unlock.
Target stats: CRIT Rate **70%+ minimum** (gates max Liberation ATK buff) | CRIT DMG 220%+ | ATK 2,000+

*Critical build note: The Resonance Liberation flat ATK buff scales directly off Roccia's CRIT Rate — every 0.1% CRIT Rate over 50% adds 1 ATK to the team buff (up to 200 ATK at 70%+ CRIT Rate). Reaching 70% CRIT Rate is therefore a hard performance threshold, not a soft optimization target.*

## Roccia: Ascension Materials

| Ascension | Level Cap | Materials |
|-----------|-----------|-----------|
| 1 | 20 → 40 | Firecracker Jewelweed ×4, LF Tidal Residuum ×4, Shell Credits ×5,000 |
| 2 | 40 → 50 | Firecracker Jewelweed ×8, MF Tidal Residuum ×4, Cleansing Conch ×2, Shell Credits ×10,000 |
| 3 | 50 → 60 | Firecracker Jewelweed ×12, MF Tidal Residuum ×8, Cleansing Conch ×4, Shell Credits ×15,000 |
| 4 | 60 → 70 | Firecracker Jewelweed ×16, HF Tidal Residuum ×4, Cleansing Conch ×8, Shell Credits ×20,000 |
| 5 | 70 → 80 | Firecracker Jewelweed ×20, HF Tidal Residuum ×8, Cleansing Conch ×12, Shell Credits ×40,000 |
| 6 | 80 → 90 | Firecracker Jewelweed ×24, FF Tidal Residuum ×4, Cleansing Conch ×16, Shell Credits ×80,000 |

**Total Ascension:** 60× Firecracker Jewelweed, 4× LF + 12× MF + 12× HF + 4× FF Tidal Residuum, 46× Cleansing Conch, 170,000 Shell Credits
- **Firecracker Jewelweed:** Field-gathered in Rinascita; use interactive map (prydwen.gg) to locate efficiently
- **Cleansing Conch:** Boss drop from a Rinascita boss (cross-reference in-game boss index for location)
- **Tidal Residuum:** Rinascita Forgery Challenges

## Roccia: Character Kit: Basic Attack — Pero, Easy

**Basic Attack (4-hit chain; all Havoc DMG):**
- Stage 1: 36.81%
- Stage 2: 19.19%×3
- Stage 3: 17.00%×2 + 51.00%
- Stage 4: 52.41%×2

*In optimized rotations, only Stage 4 is used (triggered immediately after Intro Skill — Pero, Help, which chains directly into Stage 4).*

**Heavy Attack** (baseline; STA Cost 10 + 15/s while charging): 85.00% Havoc DMG
- Hitting a target with ≥100 Imagination activates **Beyond Imagination**
- Hold to charge for more Imagination generation; charging continues after STA depletes

**Mid-air Attack** (STA Cost 30): 52.70% Havoc DMG (standard plunge)
**Dodge Counter:** 34.66%×3 Havoc DMG

## Roccia: Character Kit: Resonance Skill — Acrobatic Trick

Roccia projects her creativity into reality, generating a **tornado vortex** that pulls in nearby targets and deals **30.92%×8 Havoc DMG**. She then launches into mid-air and activates the Beyond Imagination state.
- Cooldown: 10s; Concerto Regen: 20
- **+100 Imagination** on cast
- The pull-in effect is Roccia's primary on-field grouping tool — targets are drawn to the center of the vortex, enabling AoE concentrated damage

**Inherent Passive — Immersive Performance:**
- Casting Resonance Skill or Heavy Attack increases Roccia's ATK by **20%** for 12s
- Reliable uptime — activates on every rotation entry via Skill

**Inherent Passive — Super Attractive Magic Box (Unique Mechanic):**
- After casting Outro Skill, the incoming Resonator's **Utility button** is replaced with **Magic Box**
- Pressing Utility (T/gadget key) as the next character deploys a mini-tornado at their position, dealing 100 points of Havoc DMG (Echo Skill / Utility DMG); pulls nearby targets toward it; lasts 14s or until Resonator switch
- This makes Roccia the only character in the game who can transfer a grouping tool to her Main DPS — the active Resonator can group enemies themselves without swapping back to Roccia

## Roccia: Character Kit: Resonance Liberation — Commedia Improvviso!

*"Roccia's improvised comedy begins!"*

Roccia strikes the target for **140.00%×3 Havoc DMG** (Heavy Attack DMG tag).
- Cooldown: 20s; Resonance Energy Cost: 125; Concerto Regen: 20
- For every **0.1% of Roccia's CRIT Rate over 50%**, increases the ATK of all Resonators in the team by **1 flat ATK point** for **30s**, up to **200 flat ATK**
- At 70%+ CRIT Rate: full +200 flat ATK buff is guaranteed
- **This is the first and only flat ATK buff in Wuthering Waves** — it adds directly to the post-calculation ATK total rather than as a percentage multiplier, making it uniquely valuable in builds where ATK% stacking would face diminishing returns

## Roccia: Inherent Passives

**Immersive Performance**
- Casting Resonance Skill or Heavy Attack increases Roccia's ATK by 20% for 12s
- Activates reliably at the start of every rotation via the Resonance Skill — Acrobatic Trick cast; covers the entire Real Fantasy + Liberation window

**Super Attractive Magic Box**
- After Outro Skill, the incoming Resonator's Utility button deploys a Magic Box (mini-vortex)
- Havoc DMG tag; Echo Skill category; 14s duration (or until swap)
- This is one of the most unique passive effects in the game: it lets the Main DPS character group enemies on demand without losing field time. In AoE content (Whimpering Wastes, multi-target Tower of Adversity), this is a tier-defining capability advantage over competing hybrid Sub-DPS characters

## Roccia: Intro/Outro Skills

**Intro Skill — Pero, Help**
- Deals **85.00% Havoc DMG** to the target; Concerto Regen: 10
- **+100 Imagination** on cast
- Press Basic Attack immediately after to execute **Basic Attack Stage 4** directly, skipping Stages 1–3
- Critical rotation entry: Intro Skill → BA4 → Resonance Skill is the standard Imagination build sequence to reach 300

**Outro Skill — Applause, Please!**
- The incoming Resonator gains for **14s** (ends on switch-out):
  - **20% Havoc DMG Amplification**
  - **25% Basic Attack DMG Amplification**
- Additionally triggers the **Magic Box** utility transfer via Inherent Passive — Super Attractive Magic Box
- Combined buff value (20% Havoc + 25% BA DMG) is among the highest Outro pairings in the game for Havoc Basic Attack DPS characters

## Roccia: Skill Upgrade Materials

Requires: **Cadence Seed/Bud/Leaf/Blossom** (Forgery Challenge), **The Netherworld's Stare** (weekly boss drop), and **Tidal Residuum** (LF/MF/HF/FF).

| Skill Level | Cadence Material | Netherworld's Stare | Tidal Residuum | Shell Credits |
|-------------|-----------------|---------------------|----------------|---------------|
| 2 | Seed ×3 | — | LF ×2 | 5,000 |
| 3 | Seed ×5 | — | LF ×4 | 10,000 |
| 4 | Bud ×4 | — | MF ×3 | 15,000 |
| 5 | Bud ×6 | — | MF ×5 | 20,000 |
| 6 | Leaf ×5 | Stare ×1 | HF ×3 | 30,000 |
| 7 | Leaf ×8 | Stare ×1 | HF ×5 | 45,000 |
| 8 | Blossom ×5 | Stare ×2 | FF ×3 | 60,000 |
| 9 | Blossom ×8 | Stare ×2 | FF ×5 | 75,000 |
| 10 | Blossom ×10 | Stare ×3 | FF ×6 | 90,000 |

**Total Skill Upgrade (all skills):** 25× Seed, 28× Bud, 55× Leaf, 67× Blossom, 26× The Netherworld's Stare, 25× LF + 28× MF + 40× HF + 57× FF Tidal Residuum, 2,030,000 Shell Credits

**Skill Priority:** Forte Circuit > Resonance Liberation > Intro Skill > Resonance Skill > Basic Attack

## Roccia: Resonance Chains (Sequences)

**S1**
Casting Resonance Skill — Acrobatic Trick grants **100 additional Imagination** and **10 Concerto Energy**. Immune to interruptions when casting Basic Attack — Real Fantasy.
*Value: The rotation-defining Sequence Node. Skill now provides 200 total Imagination instead of 100 — combined with the Intro Skill's 100, Roccia has exactly 300 Imagination for all three bounces without needing the BA4 intermediate step. This removes one action from her rotation, reducing field time and simplifying execution. Interruption immunity on Real Fantasy is meaningful in high-difficulty content where aerial attacks are punished. S0→S1 is the only investment most players need.*

**S2**
Casting Basic Attack — Real Fantasy grants all Resonators in the team **10% Havoc DMG Bonus** for 30s, stacking up to 3 times. Upon reaching max 3 stacks, grants an additional **10% Havoc DMG Bonus** for 30s (total: **40% Havoc DMG Bonus** at full stacks).
*Value: Strong team-wide Havoc buff — 40% Havoc DMG Bonus sustained for 30s stacks multiplicatively with her Outro's Havoc DMG Amplification for a compounding effect. In a full Havoc team this is a meaningful ceiling raise, particularly for Camellya whose damage is overwhelmingly Havoc-typed.*

**S3**
Casting Intro Skill — Pero, Help increases Roccia's Crit. Rate by **10%** and Crit. DMG by **30%** for 15s.
*Value: Personal CRIT stat bump that applies during her entire active window (the buff from Intro covers the Skill → Real Fantasy → Liberation sequence). The +10% CRIT Rate also helps ensure the 70% threshold for max Liberation ATK buff is reached more easily with less echo sub-stat investment.*

**S4**
Casting Resonance Skill — Acrobatic Trick increases Basic Attack — Real Fantasy's DMG Multiplier by **60%** for 12s.
*Value: Largest single-sequence personal damage increase. +60% to all three Real Fantasy stages is substantial; the buff timing (12s post-Skill, covering the entire Real Fantasy window) is ideal.*

**S5**
Increase Resonance Liberation — Commedia Improvviso!'s DMG Multiplier by **20%** and Heavy Attack's DMG Multiplier by **80%**.
*Value: Both Liberation (her nuke) and standard Heavy Attacks are boosted. Less impactful per rotation than S4 but adds a meaningful multiplier to the Liberation's team-wide buff trigger window.*

**S6**
Casting Resonance Liberation — Commedia Improvviso! grants for 12s: Basic Attack — Real Fantasy ignores enemies' DEF by **60%**. When Roccia lands after Real Fantasy Stage 3, she launches back into mid-air and enters Beyond Imagination, enabling **Basic Attack — Reality Recreation** (100% of Real Fantasy Stage 3 DMG, Heavy Attack DMG tag; immune to interruption). Subsequent Reality Recreation bounces continue the loop until the 12s window expires.
*Value: Transformational — S6 turns Roccia into a pseudo-Main DPS who can chain aerial bounces continuously for 12s post-Liberation, with 60% DEF ignore on every hit. The loop of Stage 3 → Reality Recreation → re-enter Beyond Imagination → repeat is a devastating sustained-airborne damage window. S6 Roccia in Havoc AoE content is among the game's highest personal DPS outputs.*

## Roccia: Recommended Echo Sets

**Best: Midnight Veil (5-pc)**
Midnight Veil (Version 2.0 Havoc set): 2-pc bonus provides Havoc DMG Bonus; 5-pc bonus provides a substantial Havoc DMG Bonus burst on Resonance Liberation cast and transfers a Havoc DMG Bonus buff to the incoming Resonator. Roccia's rotation is centered on Liberation → Outro, making the 5-pc timing ideal — the buff transfers cleanly to the Main DPS who enters immediately after her Outro.

**Alternative: 4-pc Midnight Veil + 2-pc Moonlit Clouds**
When full 5-pc Midnight Veil pieces have poor substats, the 2-pc Moonlit Clouds provides an ATK Bonus to the incoming Resonator as a fallback team buff. Less optimal for Roccia's personal damage but acceptable as a transitional setup.

**Main Echo:** Nightmare: Impermanence Heron (4-cost Havoc)
The best main Echo for Roccia. Provides Heavy Attack DMG Bonus (her primary damage type) and Havoc DMG Bonus, both passively by equipping. The Nightmare variant specifically gives a higher stat allocation for Roccia's kit than the standard Impermanence Heron. Belongs to the Midnight Veil set.

**Alternative Main Echo:** Standard Impermanence Heron (4-cost)
For the Moonlit Clouds support build. Provides Energy Regen sub-stat and the Moonlit Clouds set bonus while still delivering some Heavy Attack DMG synergy. Not recommended once Nightmare Heron is accessible.

**Echo Main Stats:**
- 4-cost: CRIT Rate (the hard priority — must reach 70% for max Liberation ATK buff)
- 3-cost #1: Havoc DMG Bonus
- 3-cost #2: Havoc DMG Bonus or ATK%
- 1-cost ×2: ATK%

**Sub-stat Priority:** CRIT Rate (to 70% minimum) > CRIT DMG > ATK% > Heavy Attack DMG Bonus > Energy Regen > Flat ATK
**Hard target:** 70%+ CRIT Rate before investing in CRIT DMG ceiling

## Roccia: Best Weapon

**Signature — Tragicomedy (5★ Gauntlets)**
CRIT Rate sub-stat (24.3%). Passive: ATK +12%; every time Basic Attack or Intro Skill is cast, Heavy Attack DMG Bonus increases by +48% for 3s. Since her Intro Skill cast and BA4 both trigger the passive, it is effectively permanently active throughout her rotation. The 24.3% CRIT Rate sub-stat makes reaching the 70% Liberation threshold dramatically easier with subpar echo sub-rolls. Prydwen rates it at 116.72% performance.

**Alternative — Blazing Justice (5★ Gauntlets)**
CRIT DMG sub-stat (48.6%); ATK +12%; 8% DEF Shred permanently active; no additional conditions. Strong alternative with Roccia's elevated base CRIT DMG from Forte nodes. Prydwen rates at 105.51%.

**Alternative — Verity's Handle (5★ Gauntlets)**
CRIT Rate sub-stat (24.3%); 12% generic DMG Bonus permanently; 48% Resonance Liberation DMG Bonus for 8s on Liberation cast, extendable by Skill uses. Excellent CRIT Rate delivery and Liberation window timing. Prydwen rates at 104.91%.

**Standard — Abyss Surges (5★ Gauntlets)**
ATK sub-stat (36.4%); high base ATK; Energy Regen passive helps rotation consistency; conditional Basic Attack and Resonance Skill DMG bonus. Reliable non-limited alternative. Prydwen rates at 100% (benchmark).

**4-Star Options:** Celestial Spiral provides reasonable Havoc utility; Stonard or Marcato for rotation smoothing when 5-star Gauntlets are unavailable.

## Roccia: Best Teams

**S-Tier: Camellya + Roccia + Shorekeeper**
- **Camellya** (Main DPS): The definitive pairing for Roccia. Camellya is a Basic Attack-heavy Havoc DPS; Roccia's Outro (+25% BA DMG + 20% Havoc DMG Amplification), +200 flat ATK buff, and S2 40% Havoc DMG Bonus stack multiplicatively for an enormous net buff. Magic Box grouping enables Camellya to hit all enemies simultaneously during her extensive field window
- **Roccia** (Sub-DPS/Enabler): Low field time, high buff density, and the only grouping toolkit in the game transferable to the Main DPS
- **Shorekeeper** (Support): Universal buff platform; CRIT Rate buff, DMG Amplification, and healing cover Roccia's only weakness (she requires ~70% CRIT Rate investment)
*The canonical Roccia team for single-target through AoE content.*

**S-Tier: Camellya + Roccia + Verina**
- **Verina** (Support/Healer): ATK% buff and healing; Outro adds ATK to all Resonators; less ceiling than Shorekeeper but strong sustained support
*Best for players without Shorekeeper.*

**A-Tier: Havoc Rover + Roccia + Support**
- **Havoc Rover** (Main DPS): Free-to-play accessible strong Havoc DPS with coordinated attack Dreamless synergy; benefits from all of Roccia's buff suite and grouping
- Best support option: Shorekeeper or Verina
*Strong F2P-accessible Havoc composition.*

**A-Tier: Phrolova + Cantarella + Roccia**
- **Phrolova** (Main DPS): Off-field Havoc DPS whose puppet Hecate benefits from Roccia's Havoc DMG buff and Magic Box grouping; the mono-Havoc Echo Skill chain synergy between the three characters is documented as a high-performance team variant (genshin-builds.com Phrolova page)
- **Cantarella** (Sub-DPS/Buffer): Buffs Phrolova; Roccia buffs both

**General notes on team composition:**
- Roccia requires a Havoc Main DPS to deliver full buff value from Outro, Liberation ATK, and S2 Havoc DMG Bonus
- Outside Havoc teams she competes with Sanhua — who has no element restriction on her Basic Attack Amplification Outro, is free, and requires less investment — and typically loses that comparison in mixed teams
- Her absolute advantage over all competitors is the Magic Box grouping + Resonance Skill vortex pairing, which no other character in the game replicates for AoE content

## Roccia: DPS Benchmarks

Roccia is rated **T3 Hybrid in Tower of Adversity** and **T1.5 Hybrid in Whimpering Wastes** (Prydwen, Patch 2.6 update). Game8 rates her as a high-performing Havoc Sub-DPS, SS-Tier in Havoc compositions. The divergence between ToA and Whimpering Wastes ratings reflects her AoE specialization: she genuinely is the best grouper in the game and her value compounds proportionally with enemy count.

**Key performance notes:**
- Maximum Liberation ATK buff (+200 flat ATK) requires ≥70% CRIT Rate; this is a gear investment threshold, not an automatic outcome
- Prydwen rates Tragicomedy at 116.72% of Abyss Surges baseline — the signature weapon is a meaningful gap, though not required to clear content
- S1 is her rotation QoL inflection point (eliminates BA4 step, adds interruption immunity); S2 is her team DPS ceiling inflection point (40% Havoc DMG Bonus); S4 is her largest personal damage spike
- Full 3-bounce Real Fantasy sequence generates 51 Concerto Energy — essential for reaching full Concerto before Outro

**Standard Rotation Outline (Camellya team, S0):**
1. Shorekeeper: full rotation including Liberation → Outro to Roccia
2. Roccia enters via **Intro Skill — Pero, Help** → +100 Imagination; chain into **BA Stage 4** → +additional Imagination (reaches ~200)
3. **Resonance Skill — Acrobatic Trick** → +100 Imagination (total: ~300); tornado vortex groups enemies; Roccia launches airborne into Beyond Imagination
4. **Real Fantasy Stage 1** (−100 Imagination; 162%) → re-enter airborne; **Stage 2** (−100; 171%) → re-enter; **Stage 3** (−100; 180%) → 51 Concerto Regen accumulated
5. **Resonance Liberation — Commedia Improvviso!** (3× 140%; +200 flat ATK to team for 30s if CRIT Rate ≥70%)
6. Echo Skill (if applicable)
7. **Outro Skill — Applause, Please!** → Camellya enters with +20% Havoc + 25% BA DMG Amplification + Magic Box utility
8. Camellya presses Utility to deploy Magic Box (groups remaining enemies); executes full rotation under all Roccia's active buffs

## Roccia: Sources
- Prydwen Build Guide — https://www.prydwen.gg/wuthering-waves/characters/roccia/
- Game8 Build Guide — https://game8.co/games/Wuthering-Waves/archives/486246
- Wuthering.gg Character Data — https://wuthering.gg/characters/roccia
- Wuthering Waves Fandom Wiki — https://wutheringwaves.fandom.com/wiki/Roccia
- LootBar Kit Guide — https://lootbar.gg/blog/en/wuthering-waves-roccia-kit.html
- Genshin-Builds Character Build — https://genshin-builds.com/en/wuthering-waves/characters/roccia
- TheGamer Build Guide — https://www.thegamer.com/wuthering-waves-roccia-best-build-teams-weapons-and-more/
