# Camellya — Kit & Mechanics Knowledge File

<!-- RAG-optimized: each ## section is a standalone searchable chunk -->

## Camellya: Combat Archetype and Role
- **Attribute (Element):** Havoc
- **Weapon:** Sword
- **Primary Role:** Main Damage Dealer (S-Tier) — the first limited Havoc DPS in Wuthering Waves; benchmark for all Havoc DPS characters
- **Secondary Roles:** Self-buffing burst DPS; aerial/vine-based combat specialist
- **Scaling:** ALL damage scales off **ATK** (not HP); ~80% of total damage output is classified as Basic Attack DMG
- **Key Resources:**
  - **Crimson Pistils** (Forte Resource, max 100) — fuels the Forte system; grants Crimson Buds on consumption
  - **Crimson Buds** (max 10) — each Bud amplifies Budding Mode attacks by +5% per Bud consumed (up to +50% additional), stacking on top of the flat +50% Budding Mode bonus
  - **Concerto Energy** (max 100) — standard team resource; Camellya's Ephemeral ability requires 100 Concerto to activate (consuming 70 and leaving 30 unspent); her rotation requires 170 total Concerto generated per cycle
  - **Blossom Mode** — entered via standard Resonance Skill; suspends Camellya on vines; enables aerial attack chain; drains STA; persists through character swaps
  - **Budding Mode** — entered via Forte Circuit Ephemeral (requires 100 Concerto + Ephemeral off cooldown); the primary burst damage window; enhances all relevant attacks by 50% base (+5% per Crimson Bud consumed, max +50% additional); ends when all Crimson Pistils are consumed or on field swap

## Camellya: Stats Baseline (Approximate — Level-by-Level)
Camellya is an ATK-focused Main DPS with high HP and DEF scaling. Her ATK is the primary damage stat.

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | ~1,000 | ~22 | ~55 |
| Lv. 10 | ~2,600 | ~57 | ~142 |
| Lv. 20 | ~4,200 | ~92 | ~230 |
| Lv. 20+ (Asc.) | ~5,200 | ~114 | ~283 |
| Lv. 30 | ~6,100 | ~134 | ~333 |
| Lv. 40 | ~7,600 | ~167 | ~415 |
| Lv. 40+ | ~8,600 | ~188 | ~467 |
| Lv. 50 | ~9,800 | ~215 | ~533 |
| Lv. 50+ | ~10,800 | ~236 | ~586 |
| Lv. 60 | ~12,100 | ~264 | ~656 |
| Lv. 60+ | ~13,100 | ~286 | ~708 |
| Lv. 70 | ~14,400 | ~314 | ~779 |
| Lv. 70+ | ~15,350 | ~332 | ~825 |
| Lv. 80 | ~16,600 | ~358 | ~891 |
| Lv. 80+ | ~17,550 | ~376 | ~937 |
| Lv. 90 | ~18,800 | ~402 | ~1,003 |

*Forte Attribute Bonus nodes add additional HP%, ATK%, and Crit Rate at unlockable milestones. Exact values verified against Wuthering Waves Fandom Wiki combat page.*

## Camellya: Stats Baseline: Analysis
Camellya's ATK stat at Lv.90 is competitive but not exceptionally high — she relies on ATK% stacking from echoes, weapons, and team buffs to push her absolute ATK into the 2,000+ range needed for optimal performance. Her HP and DEF scaling is notably above average, giving her better natural survivability than most DPS characters.

**Target Build Stats (S0, ideal endgame):**
- ATK: 2,000+ (combined with buffs)
- Crit Rate: ~70%
- Crit DMG: ~250%
- Havoc DMG Bonus: ~60%
- Basic Attack DMG Bonus: ~25%
- Energy Regen: 110–115% (base 100% + 10–15% for safety net)

## Camellya: Ascension Materials (Total — Level 1 to Level 90)
- **Shell Credits:** 170,000 (ascension) + ~2,030,000 (all Forte upgrades) = **~2,200,000 total**
- **Topological Confinement** (all 4 rarity tiers) — drops from the **Fallacy of No Return** boss in Tethys' Deep of the Black Shores (Forgery Challenge style); 46 total for full ascension:
  - LF Topological Confinement: 4
  - MF Topological Confinement: 12
  - HF Topological Confinement: 12
  - FF Topological Confinement: 4
- **Nova** — world material from Black Shores area exploration; 60 total for full ascension
- **Whisperin Cores** (LF / MF / HF / FF tiers) — enemy drops from Tacet Discord enemies in Huanglong and Black Shores areas; 4 + 12 + 12 + 4 for ascension
- **Forte Upgrade Materials (Per Skill, Levels 1–10):**
  - Shell Credits: 280,000
  - Inert Metallic Drip: 5
  - Reactive Metallic Drip: 5
  - Polarized Metallic Drip: 8
  - Heterized Metallic Drip: 11
  - Topological Confinement (skill level material): 4

## Camellya: Basic Attack: Sanguine Blossom (5-Hit Chain)
Performs up to 5 consecutive attacks dealing Havoc DMG. After Basic Attack Stage 3 **or** Heavy Attack Pruning, hold the Normal Attack Button to continuously spin and strike the target (this spin is **Basic Attack Vining Waltz** or **Blazing Waltz** in Blossom Mode), dealing Havoc DMG. Basic Attack Stage 4 automatically flows into Stage 5 without additional input.

All Basic Attack variants deal **Basic Attack DMG type** — the single most important distinction in her kit, since the majority of buffs that stack on Camellya target this damage type specifically.

**Approximate ATK-based scaling per stage at Lv.1 and Lv.10:**

| Stage | Lv.1 (% ATK) | Lv.10 (% ATK) |
|-------|--------------|---------------|
| Stage 1 | ~60% | ~100% |
| Stage 2 | ~55%+55% | ~92%+92% |
| Stage 3 | ~75% | ~125% |
| Stage 4 | ~70% | ~115% |
| Stage 5 | ~85% | ~140% |
| Vining Waltz (Spin, per tick) | ~30–35% per hit | ~50–58% per hit |
| Dodge Counter (Atonement) | ~80% | ~130% |

*Note: In Budding Mode, all above attacks gain a flat +50% DMG Multiplier bonus on top of these base values, plus an additional +5% per Crimson Bud consumed at Ephemeral cast (max +50%), for a total possible bonus of +100% to all multipliers.*

## Camellya: Basic Attack: Heavy Attack — Pruning
Consumes STA to attack the target, dealing Havoc DMG. Can be performed in mid-air. Normally counts as Heavy Attack DMG, but **Inherent Skill 1 reclassifies it as Basic Attack DMG** — a critical change enabling it to receive all Basic Attack-focused buffs.

In Blossom Mode, becomes a **horizontal spin attack** (Basic Attack Blazing Waltz) with broader AoE hit coverage.

## Camellya: Resonance Skill: Crimson Blossom / Floral Ravage (Blossom Mode Entry/Exit)
**Crimson Blossom** (standard Resonance Skill, ground or mid-air):
- Camellya suspends herself using her vines, entering **Blossom Mode**
- In Blossom Mode:
  - Normal movement is disabled; she can only dodge (STA cost) to reposition
  - Her Basic Attack chain shortens to 4 hits (Stage 1–4)
  - Her spin attack becomes horizontal (wider AoE)
  - All attacks while in Blossom Mode deal slightly increased damage vs. out-of-Blossom
  - STA drains continuously while suspended
  - She can cast skills and build Concerto Energy normally
  - Blossom Mode persists through character swaps (she re-enters it when swapping back)
- **Cooldown:** ~5s from entering/exiting

**Floral Ravage** (second Resonance Skill press in Blossom Mode):
- Releases from vines; deals Havoc DMG; exits Blossom Mode
- Provides concerto energy; follow with Basic Attack to continue chain

| | Lv.1 | Lv.5 | Lv.10 |
|-|------|------|-------|
| Crimson Blossom DMG (% ATK) | ~100% | ~130% | ~170% |
| Floral Ravage DMG (% ATK) | ~80% | ~104% | ~136% |

## Camellya: Forte Circuit: Crimson Pistil, Crimson Bud, and Ephemeral
**Crimson Pistil Resource (max 100):**
- +100 Crimson Pistils: casting Intro Skill Everblooming
- +100 Crimson Pistils: activating Forte Circuit Ephemeral
- +50 Crimson Pistils: casting S6 Forte skill Perennial

**Crimson Bud Generation:**
- Each time a Crimson Pistil-consuming attack hits and passes certain thresholds (via Normal Attacks or Vining Waltz), Camellya generates 1 Crimson Bud (maximum 10)
- Crimson Buds accumulate passively during Blossom Mode and normal combat; the goal is to enter Ephemeral with as many Buds as possible (ideally 10 for the maximum +50% Sweet Dream bonus)

**Forte Circuit: Ephemeral (Core Burst Ability):**
- Requires: 100 Concerto Energy + Ephemeral not on cooldown
- When both conditions are met, the Resonance Skill button is replaced with Ephemeral
- **Cost:** Consumes 70 Concerto Energy (leaves 30)
- **Effect:** Deals massive Havoc DMG to all targets in a large AoE; this damage is counted as **Basic Attack DMG**; considered Forte Circuit damage
- **Cooldown:** 25 seconds from cast
- Entering Ephemeral immediately restores all 100 Crimson Pistils
- All accumulated Crimson Buds are consumed immediately on cast; each Bud consumed increases **Sweet Dream** bonus by +5% (max 10 Buds = +50% bonus)
- Camellya enters **Budding Mode** after Ephemeral

**Budding Mode — Sweet Dream:**
- Base effect: +50% DMG Multiplier to Normal Attack, Basic Attack Vining Waltz, Basic Attack Blazing Waltz, Basic Attack Vining Ronde, Dodge Counter Atonement, Resonance Skill Crimson Blossom, and Resonance Skill Floral Ravage
- Additional: +5% per Crimson Bud consumed at Ephemeral cast, up to +50% (total max: +100% on top of all base multipliers = effectively doubled damage from these skills)
- Crimson Pistils are consumed by the attacks listed above while in Budding Mode
- **Energy Regen is set to 0% for all listed attacks** during Budding Mode — this is the price paid; she cannot gain Resonance Energy while her burst window is active
- Budding Mode ends when: all Crimson Pistils consumed OR Camellya swaps off-field

**Ephemeral Scaling (% ATK, approximate):**
| Level | Lv.1 | Lv.2 | Lv.3 | Lv.5 | Lv.8 | Lv.10 |
|-------|------|------|------|------|------|-------|
| Ephemeral DMG | ~560% | ~605% | ~651% | ~743% | ~882% | ~1,000%+ |

*Exact Ephemeral multipliers at Lv.10 from in-game data approach ~1,000–1,100% ATK across all hits combined. Verify against Wuthering Waves Fandom Wiki Combat page for precise values.*

## Camellya: Resonance Liberation: Fervor Efflorescent
**Energy Cost:** 125 | Cooldown: 25s | Concerto Regen: 20

Camellya summons her vines and flowers in a dramatic AoE burst around herself, dealing Havoc DMG. This is a significant nuke — in optimal rotations it is cast immediately after or alongside Ephemeral to maximize the Budding Mode bonus window. The Liberation also provides a substantial amount of Concerto Energy (20), helping to rebuild toward the next Ephemeral cycle.

**Attribute Scaling (% ATK, approximate per hit):**
| Level | Lv.1 | Lv.3 | Lv.5 | Lv.7 | Lv.10 |
|-------|------|------|------|------|-------|
| Liberation Total DMG | ~450% | ~540% | ~640% | ~756% | ~900%+ |

*S3 Resonance Chain increases this multiplier by +50%, making Liberation a substantially larger damage contribution at S3+.*

## Camellya: Inherent Skill 1: Sanguine Bloom (Havoc + Basic Reclassification)
- Increases Camellya's **Havoc DMG Bonus by +15%**
- **Heavy Attack Pruning is now counted as Basic Attack DMG** (instead of Heavy Attack DMG)
- This reclassification means every Basic Attack buff in the game — from Sanhua's Outro, S4 team buff, and weapon passives — also applies to her Heavy Attack, massively increasing it

## Camellya: Inherent Skill 2: Eternal Blossom (Havoc + Interruption Resistance)
- Increases Camellya's **Havoc DMG Bonus by +15%** (total from both Inherent Skills: **+30% Havoc DMG Bonus** passively)
- Grants **increased resistance to interruption** while casting Basic Attack, Basic Attack Vining Waltz, and Basic Attack Blazing Waltz
- This interruption resistance is meaningful at S0; at S1, the Resonance Skill (Ephemeral) additionally gains interrupt immunity

## Camellya: Intro Skill: Everblooming
When swapping to Camellya with full Concerto Energy, she dashes in and deals Havoc DMG.

**Critical mechanic:** Casting Everblooming instantly recovers **100 Crimson Pistils** — the full Forte resource in a single activation. This is why beginning every rotation with the Intro Skill is essential: it immediately enables Crimson Bud generation and the path to Ephemeral in the shortest possible window.

**Scaling (% ATK):**
| Level | Lv.1 | Lv.5 | Lv.10 |
|-------|------|------|-------|
| Everblooming DMG | ~329% | ~420% | ~550%+ |

*S5 increases Intro Skill multiplier by +303% — transforming Everblooming from an energy-refill tool into a serious nuke in its own right.*

## Camellya: Outro Skill: Twining
When Camellya exits the field, she strikes the target dealing Havoc DMG.
- Base damage: **329.24% of ATK**
- If Forte Circuit Ephemeral was activated during the current field session (activating the "Ephemeral Twining" trigger), the next Outro Skill **Twining** deals **additional Havoc DMG equal to 459.02% of ATK**
- Combined Outro (Ephemeral Twining active): **329.24% + 459.02% = 788.26% ATK total** from the Outro alone

This makes properly triggering Ephemeral before Outro mandatory for maximum damage output.

*S5 increases Outro Skill multiplier by +68%, transforming Twining into an enormous burst hit.*

## Camellya: Materials Costs: Forte Skill Upgrade Summary
Per skill to Level 10:
- 280,000 Shell Credits
- 5 Inert Metallic Drip + 5 Reactive Metallic Drip + 8 Polarized Metallic Drip + 11 Heterized Metallic Drip
- 4 Topological Confinement (boss drop from Fallacy of No Return)

**Skill Leveling Priority:**
1. Resonance Skill (governs Ephemeral multiplier — most impactful single upgrade)
2. Forte Circuit (governs Sweet Dream bonus and Ephemeral mechanics)
3. Resonance Liberation (direct nuke; high value at S3)
4. Intro Skill (high damage at S5; strong at base for Pistil refill utility)
5. Basic Attack (least priority — base multipliers are comparatively low)

## Camellya: Resonance Chain Level 1 (S1): Crimson Dream
- Casting Intro Skill Everblooming increases Camellya's **Crit DMG by +28%** for 18 seconds (trigger cooldown: once every 25s)
- While casting Forte Circuit Ephemeral, Camellya is **immune to interruptions**
- **Priority:** Very High — the +28% Crit DMG boost is free and unconditional during her burst window, and interrupt immunity on Ephemeral removes her biggest vulnerability at S0

## Camellya: Resonance Chain Level 2 (S2): Radiant Bloom
- The **DMG Multiplier of Resonance Skill Ephemeral is increased by +120%**
- **Priority:** Highest single value node — approximately +23% total real damage improvement for Camellya. Ephemeral is her primary burst ability; doubling its multiplier is transformative

## Camellya: Resonance Chain Level 3 (S3): Blossom's Edge
- The **DMG Multiplier of Resonance Liberation Fervor Efflorescent is increased by +50%**
- When in **Budding Mode**, Camellya's ATK is increased by **+58%**
- **Priority:** Very High — the +58% ATK during Budding Mode stacks multiplicatively with all other ATK% sources and applies to all Budding Mode attacks; the Liberation buff is a direct 50% increase to a major nuke

## Camellya: Resonance Chain Level 4 (S4): Thornbound Promise
- Casting Everblooming (Intro Skill) gives **all team members +25% Basic Attack DMG Bonus** for 30 seconds
- **Priority:** High — the 30-second duration covers the full rotation cycle for every DPS character on the team; makes Camellya a genuine team-wide Basic Attack buffer in addition to her personal DPS role; particularly impactful in teams with a secondary Basic Attack DPS

## Camellya: Resonance Chain Level 5 (S5): Eternal Garden
- The **DMG Multiplier of Intro Skill Everblooming is increased by +303%**
- The **DMG Multiplier of Outro Skill Twining is increased by +68%**
- **Priority:** Moderate — the Intro and Outro damage are secondary to her main rotation (Ephemeral + Budding Mode); +303% on Intro is absurd in isolation but Intro is not a priority damage source at S0; becomes relevant in speedclear contexts

## Camellya: Resonance Chain Level 6 (S6): Undying Crimson
- The **DMG Multiplier of Forte Circuit Sweet Dream is additionally increased by +150%** (stacking on all Budding Mode bonuses)
- Unlocks **Forte Circuit Perennial**: within 15 seconds after casting Ephemeral, if Concerto Energy is full and Perennial is not on cooldown, the Resonance Skill is replaced with Perennial
  - Perennial **costs 50 Concerto Energy** and recovers 50 Crimson Pistils
  - Deals Havoc DMG equal to **100% of Ephemeral's DMG** (counted as Basic Attack DMG)
  - Cooldown: once per 25 seconds
  - Camellya enters Budding Mode after casting Perennial and removes all Crimson Buds
  - **Sweet Dream bonus when casting Perennial increases to +250%** (from the base +100% at max Buds)
  - Immune to interruptions while casting Perennial
- **Priority:** Theoretically very high (+80% theoretical DPS improvement) but rotation length extension reduces practical uptime of existing buffs, making real improvement closer to +55–60%. S6 Camellya is exceptionally powerful but requires rotation adaptation

## Camellya: Optimal Rotation Overview (S0, Full Concerto from Outro Swap)
1. Character 2/3 builds full Concerto → swap to **Camellya** → triggers **Intro Skill Everblooming** (+100 Crimson Pistils, +28% Crit DMG at S1)
2. Use **Echo Skill** (Crownless or Dreamless) — animation cancel with jump if using Nightmare: Crownless
3. Cast **Resonance Skill** (Crimson Blossom) → enter **Blossom Mode**
4. Basic Attack chain: BA1 → BA2 → BA3 → **Hold BA3** (Vining Waltz spin) → BA4 — building Concerto Energy and Crimson Buds
5. Once Concerto hits 100, **Forte Circuit Ephemeral** activates — use it to enter **Budding Mode** (+50% to +100% damage multiplier)
6. Immediately cast **Resonance Liberation Fervor Efflorescent** (Liberation provides concerto and counts during Budding window)
7. Continue BA chain: BA1 → BA2 → BA3 → Hold → BA4 while consuming Crimson Pistils under Budding Mode bonus
8. Once Concerto rebuilds to 100 again, **Outro Skill Twining** triggers (with Ephemeral Twining buff = **788.26% ATK** combined Outro)
9. Swap out → repeat with supporting characters → swap back on next rotation

**Key timing notes:**
- Entire on-field window for Camellya: ~25–35 seconds per rotation
- She is one of the longest on-field DPS characters in the game; team selection should minimize field time needed for support characters
- STA management during Blossom Mode requires positioning pre-commitment

## Camellya: Recommended Weapons
- **Red Spring** (5★ Sword, Signature — Base ATK: 588, Crit Rate substat 24.3%) — the definitive best-in-slot; tailored entirely to her kit: +12% ATK base, +10% Basic Attack DMG Bonus per hit (×3 stacks, per second), **+80% Basic DMG Bonus** for 10 seconds when Concerto Energy is consumed; only character in the game who can efficiently trigger the Concerto consumption passive multiple times per rotation
- **Emerald of Genesis** (5★ Standard) — Crit Rate substat; +12.8% ER; +6% ATK stacking ×2 on Resonance Skill cast; provides safety net for rotation and good raw stats; best non-signature 5★ option
- **Blazing Brilliance** (5★ Standard) — Crit DMG substat; higher raw damage ceiling than Emerald at higher refinements; "stat stick" but effective
- **Somnoire Anchor** (4★ Event Sword) — Best F2P option post-event; high base ATK; passive grants +2% ATK per stack (up to 10 = 20% ATK) and +6% Crit Rate at max stacks; pairs well with Camellya's long on-field time to naturally reach max stacks
- **Commando of Conviction** (4★ Convene) — +15% ATK for 15s on Intro Skill cast; simple and reliable; slightly outclassed by Somnoire Anchor but broadly available

## Camellya: Recommended Echo Sets
**Best Set: Sun-Sinking Eclipse / Havoc Eclipse (5-piece)**
- 2-piece: +10% Havoc DMG Bonus
- 5-piece: After releasing Basic Attack or Heavy Attack, gain +7.5% Havoc DMG Bonus per stack (×4 stacks, each lasts 15s) = **+30% additional Havoc DMG Bonus at full stacks** — total set bonus: **+40% Havoc DMG Bonus**
- Fully ramping takes ~6 seconds of Basic Attack spam — trivially easy in Camellya's rotation

**Alternative Set: Lingering Tunes (5-piece)**
- 2-piece: +10% ATK
- 5-piece: While on field, ATK increases by +5% every 1.5s (×4 stacks max = +20% ATK), plus +60% Outro Skill DMG
- Better if Camellya's Outro is a major rotation damage contributor (S5)

**Main Echo Options:**
- **Nightmare: Crownless** — Best-in-slot main echo for Havoc Eclipse set; passively provides +12% Havoc DMG and +12% Basic Attack DMG when in main echo slot; Active: jump-cancel after animation for instant cast
- **Dreamless** — Strong alternative main echo; active skill provides 6 consecutive Havoc hits (5×54.08% + 1×270.40% ATK = 540.8% total) with easy cast; no animation cancel required; consistent and simple

**Echo Cost Pattern:** 4-3-3-1-1 (standard DPS setup; avoids 4-4-1-1-1 which underperforms)

**Main Stats:**
- 4-cost: Crit Rate OR Crit DMG (whichever is lower)
- 3-cost ×2: Havoc DMG Bonus + ATK% (or double ATK% if using Red Spring in Tower of Adversity with mismatched element bonus — margin is under 1%)
- 1-cost ×2: ATK flat

## Camellya: Best Team Compositions
**Optimal (Premium):** Camellya + Sanhua + Shorekeeper
- Sanhua (Outro: +38% Basic Attack DMG Amplification for incoming Resonator, 14s) provides the single most impactful external buff for Camellya; her entire kit takes ~8–10 seconds on field, maximizing Camellya's on-field time
- Shorekeeper (Outro: 15% all DMG Amp + Crit Rate/Crit DMG buffs from Supernal Stellarealm) — stacks multiplicatively with Sanhua's Basic Attack buff

**Optimal (Premium Alt):** Camellya + Lynae + Mornye/Shorekeeper
- Lynae provides massive generalist buffs; considered equal or better to Sanhua at high investment

**Standard F2P:** Camellya + Sanhua + Verina/Baizhi
- Verina: Outro +10% All DMG Bonus for team; +10% ATK; broader buff toolkit
- Baizhi: ATK buffs and healing; slightly lower ceiling than Verina but accessible

**Alternative:** Camellya + Danjin + Verina
- Danjin Outro: Havoc DMG Amplification for incoming Resonator; supplements Camellya's naturally high Havoc DMG Bonus for double-stacking Havoc bonuses

---

## Camellya: Sources
- Wuthering Waves Fandom Wiki — Camellya/Combat: https://wutheringwaves.fandom.com/wiki/Camellya/Combat
- wuthering.gg Camellya Kit Data: https://wuthering.gg/characters/camellya
- Prydwen.gg Camellya Build Guide: https://www.prydwen.gg/wuthering-waves/characters/camellya/
- Game8.co Camellya Best Build: https://game8.co/games/Wuthering-Waves/archives/473332
- Wutheringlab Camellya Build: https://wutheringlab.com/character/camellya-build/
- GuildJen Camellya Character Guide: https://guildjen.com/camellya-character-guide/
- Theria Games Ultimate Camellya Guide: https://theriagames.com/guide/wuthering-waves-ultimate-camellya-guide/
- wutheringwaves.gg Camellya Guide: https://wutheringwaves.gg/camellya-guide/
- Genshin-Builds Camellya Guide: https://genshin-builds.com/en/wuthering-waves/characters/camellya
- MisterMenPlays Camellya Build: https://www.mistermenplays.com/wutheringwaves/builds/camellya
- LootBar Camellya Kit Overview: https://lootbar.gg/blog/en/wuthering-waves-camellya-kit.html
- TheGamer Camellya Build Guide: https://www.thegamer.com/wuthering-waves-camellya-build-guide/
