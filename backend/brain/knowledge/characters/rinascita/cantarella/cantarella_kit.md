---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/rinascita/cantarella/cantarella_kit.md
character: Cantarella
group: Rinascita / Ragunna / Fisalia Family
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - havoc
  - rectifier
  - sub-dps
  - healer
  - support
  - trance
  - shiver
  - mirage
  - hazy-dream
  - jolt
  - perception-drain
  - abyssal-rebirth
  - dreamweavers
  - echo-skill
  - phrolova-team
  - version-2-2
---

# Cantarella Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/cantarella/, https://wutheringlab.com/character/cantarella-build/, https://game8.co/games/Wuthering-Waves/archives/500493, https://www.ldshop.gg/blog/guide/wuthering-waves-cantarella-build-guide.html, https://lootbar.gg/blog/en/wuthering-waves-cantarella-build-guide.html, https://www.destructoid.com/best-cantarella-build-in-wuthering-waves-weapons-echoes-team-compositions-and-sequences/, https://wutheringwaves-builds.com/character/cantarella/ -->

## Cantarella: Combat Archetype and Role

- **Element:** Havoc
- **Weapon Type:** Rectifier (combat implementation: coral parasol)
- **Role:** Flexible Sub-DPS / Healer / Support — simultaneously deals meaningful damage, heals the entire team, debuffs enemies, and provides off-field Coordinated Attacks
- **Archetype:** Stance dancer (Outside Mirage → Inside Mirage); Trance accumulator → Mirage entry; Shiver accumulator → Perception Drain finisher; Hazy Dream debuffer; Jolt trigger; Dreamweaver off-field attack distributor; Outro Skill team Havoc + Resonance Skill amplifier
- **Introduced:** Version 2.2 (March 27, 2025); rerun Version 2.5 Phase 2 and Version 2.8 Phase 1

Cantarella occupies a unique position in the Havoc roster as a *"jack-of-all-trades"* unit per Destructoid: she provides team healing, significant off-field Coordinated Attack damage via Dreamweavers, the Hazy Dream debuff (which enables Jolt follow-up damage), meaningful personal damage via Perception Drain, and an Outro Skill that amplifies both the incoming character's Havoc DMG and Resonance Skill DMG simultaneously. Game8 describes her as *"Phrolova's best Sub-DPS due to her kit having multiple Echo Skills that trigger Hecate's attacks"* — her kit's Echo Skill frequency is Phrolova's most important synergy requirement, making Cantarella uniquely irreplaceable in that team rather than merely good.

Her primary weakness is that she is genuinely *not* a Main DPS — while her Perception Drain has an impressive multiplier, her overall damage output is described by Wutheringlab as *"mediocre"* for a 5-star DPS slot, and she should not attempt to replace a dedicated Main DPS. Her correct role is as the second character in a rotation: Sub-DPS, healer, and buff-delivery system who enters, deploys her full combo, and swaps to the Main DPS with her Outro buffs active.

## Cantarella: Key Resources — Trance and Shiver

Cantarella's combat system runs on two sequential resources: Trance (accumulated outside and inside Mirage to enter the state and unlock enhanced attacks) and Shiver (accumulated inside Mirage to reach Perception Drain and provide healing).

**Trance (0 to 5 points)**
- The gate to Mirage entry; also governs how long Mirage lasts once entered
- **Trance Generation:**
  - **Intro Skill (Suite of Quietus or Tidal Surge):** +1 Trance on cast
  - **Basic Attack Stage 3 hit:** +1 Trance (must hit an enemy; if the attack misses, no Trance is generated)
  - **Resonance Skill — Graceful Step hit:** +1 Trance (hits or misses — the Resonance Skill generates Trance whether or not it connects per Wutheringlab; verify with Fandom Wiki)
  - **Resonance Liberation cast:** +2 Trance; this is the fastest single Trance injection outside of the full Intro → Skill → Liberation build sequence
  - **S1 — Midnight's Aria:** +1 additional Trance per Resonance Skill cast (effectively +2 Trance total per Resonance Skill at S1)
- **Maximum:** 5 Trance points
- **Trance Consumption — Heavy Attack: Delusive Dive:** When Cantarella has at least 1 Trance, holding the Heavy Attack button becomes Delusive Dive, which deals Havoc DMG and enters Mirage; **Delusive Dive consumes 1 Trance on activation** (not all Trance — just 1)
- **Trance Consumption in Mirage — Phantom Sting attacks:** Each Basic Attack (Phantom Sting Stage 1, 2, or 3), Mid-air Attack (Abysmal Vortex), or Dodge Counter (Shadowy Sweep) that hits a target in Mirage consumes 1 Trance and grants 1 Shiver plus healing to all nearby Resonators
- **Mirage duration:** 8 seconds if no Trance is used inside it; effectively controlled by how quickly the player spends remaining Trance via Phantom Sting attacks; Mirage ends when all Trance is depleted or the 8-second timer expires

**Shiver (0 to 3 points)**
- Accumulated inside Mirage via Basic Attacks; gates both Perception Drain and healing
- **Shiver Generation (in Mirage only):** Each Phantom Sting (Basic Attack), Abysmal Vortex (Mid-air Attack), or Shadowy Sweep (Dodge Counter) hit → consumes 1 Trance → grants 1 Shiver + team heal
- **Shiver-triggered healing:** Every single Shiver gained provides an immediate heal to all nearby Resonators; Cantarella's primary healing delivery is through this repeated Shiver accumulation loop
- **At 3 Shiver:** Resonance Skill transforms from Flickering Reverie → **Forte Circuit: Perception Drain** (the high-damage finisher); Resonance Skill icon turns purple visually to indicate readiness
- Shiver is consumed entirely by Perception Drain cast; after Perception Drain, Shiver returns to 0 and the cycle can restart if Trance remains

**The Full Resource Loop (per rotation):**
1. Build Trance outside Mirage via Intro Skill, Basic Attack Stage 3, Resonance Skill, Liberation
2. Enter Mirage via Delusive Dive (Heavy Attack with ≥1 Trance)
3. Cast Flickering Reverie (Resonance Skill in Mirage, ≤2 Shiver) → applies Hazy Dream
4. Spend remaining Trance via Phantom Sting attacks (each one → Shiver + team heal)
5. At 3 Shiver, Resonance Skill becomes Perception Drain → cast for high damage + full team heal + Hazy Dream reapplication
6. Swap out with Outro Skill active to deliver +20% Havoc / +25% Resonance Skill buffs to incoming character

## Cantarella: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | ~840 | ~33 | ~91 |
| Lv. 20 | ~2,185 | ~86 | ~237 |
| Lv. 40 | ~4,170 | ~165 | ~453 |
| Lv. 60 | ~6,730 | ~267 | ~731 |
| Lv. 80 | ~9,270 | ~367 | ~1,007 |
| Lv. 90 | ~10,545 | ~418 | ~1,146 |

*Approximate figures; Forte Attribute Bonuses (CRIT DMG) not included. Verify exact values with the Wuthering Waves Fandom Wiki.*

## Cantarella: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | LF Whisperin Core ×4, Seaside Cendrelis ×4, Shell Credits ×5,000 |
| 2 | 40→50 | MF Whisperin Core ×4, Seaside Cendrelis ×8, Shell Credits ×10,000 |
| 3 | 50→60 | HF Whisperin Core ×8, Seaside Cendrelis ×12, Axiom of Creation ×4, Shell Credits ×15,000 |
| 4 | 60→70 | HF Whisperin Core ×8, Seaside Cendrelis ×16, Axiom of Creation ×8, Shell Credits ×20,000 |
| 5 | 70→80 | FF Whisperin Core ×12, Seaside Cendrelis ×20, Axiom of Creation ×12, Shell Credits ×40,000 |
| 6 | 80→90 | FF Whisperin Core ×12, Seaside Cendrelis ×24, Axiom of Creation ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Whisperin Cores (LF/MF/HF/FF):** Dropped by Whisperin Tacet Discord enemies; craftable via Synthesizer; available from Forgery Challenge: Marigold Woods
- **Seaside Cendrelis:** Local specialty gathered from the Rinascita coastline areas; use the Prydwen Interactive Map to locate efficiently; also used by other Rinascita characters; note that these must be gathered in the overworld — no shop purchase option
- **Axiom of Creation:** Weekly boss material from the **Lorelei** boss (Rinascita weekly challenge); Lorelei is both the source of the ascension material and the recommended main echo for Cantarella, creating a thematic and practical alignment

## Cantarella: Skill Upgrade Materials

**Total Forte Shell Credits (all skills):** ~2,030,000
- **Skill Books:** Verify appropriate Forgery Challenge type with Fandom Wiki
- **Weekly Boss Material:** Axiom of Creation from Lorelei

**Skill Upgrade Priority:** Forte Circuit (Perception Drain — highest multiplier + Shiver system + team heal) → Resonance Liberation (Flowing Suffocation / Beneath the Sea — Dreamweaver Coordinated Attack damage) → Resonance Skill (Graceful Step / Flickering Reverie — Trance generation, Hazy Dream application, Echo Skill count) → Basic Attack → Intro Skill. Forte Circuit is the clear first priority as Perception Drain is both the damage peak and the primary sustained healing delivery mechanism; Liberation second for the off-field Dreamweaver attack damage that continues throughout the Main DPS's window.

## Cantarella: Character Kit: Basic Attack — Phantom Sting (Outside Mirage)

**Standard Ground Chain (3 stages)**
- Up to 3 consecutive Havoc DMG attacks classified as Basic Attack DMG
- **Stage 3 hit:** Grants **+1 Trance**; also triggers **3 Coordinated Attacks** dealing Havoc DMG (these are Coordinated Attacks, not Echo Skill DMG; verify classification details with Fandom Wiki)
- Stage 3 must hit an enemy to generate Trance; if the attack misses, no Trance is granted

**Heavy Attack**
- Standard Havoc DMG (Stamina cost) when Cantarella has **no Trance**
- When Cantarella has **≥1 Trance:** replaced by **Heavy Attack — Delusive Dive**

**Heavy Attack — Delusive Dive (Trance required)**
- Deals Havoc DMG to the target
- Cantarella enters **Mirage** on cast
- Consumes 1 Trance
- Cannot be cast again while already in Mirage (re-casting Delusive Dive in Mirage does not re-enter a second Mirage)
- Can be cast in water (exploration utility)

## Cantarella: Character Kit: Basic Attack — Phantom Sting (Inside Mirage)

Inside Mirage, all of Cantarella's attack options change:

**Basic Attack — Phantom Sting Stages 1–3 (in Mirage)**
- Each stage deals Havoc DMG
- **Stage 3** triggers 3 Coordinated Attacks dealing Havoc DMG
- Each of Stage 1, 2, and 3 **on hit:** consumes 1 Trance, grants 1 Shiver, heals all nearby Resonators
- This is the primary Shiver accumulation mechanism; the standard in-Mirage loop is Phantom Sting 1 → 2 → 3 to reach 3 Shiver (consuming 3 Trance points in the process)

**Mid-Air Attack — Abysmal Vortex (in Mirage)**
- Plunging Havoc DMG; on hit: consumes 1 Trance, grants 1 Shiver, heals all nearby Resonators
- Alternative Shiver generation method; can be used in place of Stage 3 for faster Shiver-per-second generation in specific situations

**Dodge Counter — Shadowy Sweep (in Mirage)**
- Havoc DMG after successful Dodge in Mirage; on hit: consumes 1 Trance, grants 1 Shiver, heals all nearby Resonators
- Useful for both Shiver generation and survivability simultaneously

**Mirage Duration and End Conditions:**
- Mirage lasts **8 seconds** base duration; in practice, duration is controlled by how quickly Trance is spent via Phantom Sting/Abysmal Vortex/Shadowy Sweep
- Mirage ends when all Trance is consumed OR the 8-second timer expires, whichever comes first

## Cantarella: Character Kit: Resonance Skill

**Resonance Skill — Graceful Step (Outside Mirage)**
- Attacks the target, dealing Havoc DMG; Havoc DMG classified as Resonance Skill DMG
- Grants **+1 Trance** (this triggers even if the attack misses per Wutheringlab; verify exact condition with Fandom Wiki)
- 12-second cooldown
- The fastest pre-Mirage Trance generator alongside Intro Skill and Liberation

**Resonance Skill — Flickering Reverie (Inside Mirage, Shiver < 3)**
- **This skill is classified as an Echo Skill** when cast — critical distinction for Phrolova team synergy (triggers Hecate's Enhanced Attack when Phrolova is off-field) and for the Abyssal Rebirth mechanic (Intro Skill Echo Skill passive Concerto recovery)
- Attacks the target, dealing Havoc DMG
- Sends the target into **Hazy Dream** for 6.5 seconds:
  - Reduces target's movement speed for 6.5 seconds
  - When the target takes damage while under Hazy Dream, **Jolt** is triggered: removes Hazy Dream, deals Havoc DMG classified as Basic Attack DMG
  - **Only one Jolt triggers per Hazy Dream application** (S2 notably buffs this single Jolt's multiplier by +245%)
- Can be cast in mid-air
- 12-second cooldown

**Forte Circuit — Perception Drain (Inside Mirage, Shiver = 3)**
- **Available only when Cantarella has 3 Shiver and is in Mirage; Resonance Skill icon turns purple when ready**
- Consumes all 3 Shiver
- **Also classified as Echo Skill** — same critical Phrolova/Hecate trigger and Abyssal Rebirth Concerto interaction as Flickering Reverie
- Deals high Havoc DMG classified as **Basic Attack DMG** to target in an AoE
- **Sends target into Hazy Dream** (enabling immediate Jolt follow-up)
- **Heals all nearby Resonators** (major team heal; Destructoid: *"provides a large burst of healing to her entire team"*)
- **Grants Cantarella a large amount of Concerto Energy** (enabling faster Outro rotation or Liberation)
- Can be cast in mid-air
- 18-second cooldown (the longest of her Resonance Skills; per Destructoid: *"her primary goal and should be used on cooldown"*)
- **S3 interaction:** Perception Drain's DMG multiplier is increased by +50% (S1 also grants +50% to both Graceful Step and Flickering Reverie; all three receive the same boost from their respective sequences)
- Wutheringlab: *"This skill deals over 1300% multiplier damage"* at relevant investment levels (verify exact max-level value with Fandom Wiki)

**Skill Upgrade Priority:** Third — both Flickering Reverie and Perception Drain are important, but Perception Drain is covered under Forte Circuit priority; Graceful Step is primarily a Trance generator; the skill level primarily scales the Resonance Skill DMG multipliers

## Cantarella: Character Kit: Resonance Liberation — Beneath the Sea / Diffusion

**Resonance Liberation — Flowing Suffocation (initial hit)**
- Cantarella sweeps the area with Havoc DMG (classified as Resonance Liberation DMG)
- **On cast:** Grants **+2 Trance** immediately; also triggers **Abyssal Rebirth**
- **S2 interaction:** Liberation hit now also sends the target into Hazy Dream (same 6.5s debuff as Flickering Reverie); Jolt multiplier boosted by +245%
- **S3 interaction:** Liberation DMG multiplier increased by +370% (Destructoid: *"turns her Liberation from mediocre damage into a real nuke"*); also automatically enters Cantarella into Mirage after casting (eliminating the need for a separate Delusive Dive)
- **S6 interaction:** Cantarella's DMG ignores 30% DEF for 10 seconds after casting; Hazy Dream has a 1.2s immunity window where the first hit does not trigger Jolt (allowing follow-up DMG to stack before the single Jolt fires)

**Resonance Liberation — Diffusion (sustained effect, 30 seconds)**
- After Flowing Suffocation, all Resonators in the team gain the **Diffusion** effect: each Resonator summons **Dreamweavers** (jellyfish) that perform Coordinated Attacks, dealing Havoc DMG, triggered every second for the duration
- Standard Dreamweaver count: scales with skill level
- **S4 interaction:** Maximum Dreamweavers increased by +5 (additional off-field damage over the 30-second duration)
- Dreamweaver Coordinated Attacks are the primary source of sustained off-field damage that Cantarella contributes during the Main DPS's field window; these attacks continue automatically without Cantarella being on-field
- **Skill Upgrade Priority:** Second — the Dreamweaver Coordinated Attack multipliers and the Liberation hit multiplier both scale significantly with skill level; this is the primary source of Cantarella's off-field damage contribution

**Abyssal Rebirth (Passive triggered by Intro Skill or Liberation)**
- After casting Intro Skill, Cantarella enters **Abyssal Rebirth state for 25 seconds** (once per 25 seconds)
- During Abyssal Rebirth: for up to **6 times**, when any Resonator in the team casts an Echo Skill, Cantarella recovers **6 points of Concerto Energy** per trigger
- **Unique Echo restriction:** Echoes of the same name can only trigger this effect once per Abyssal Rebirth window
- Maximum Concerto recovery per Abyssal Rebirth: 6 triggers × 6 points = **36 Concerto Energy** from team Echo Skills
- This mechanic rewards team compositions with high Echo Skill frequency and diverse echo selections, exactly mirroring the Phrolova/Hecate off-field trigger condition — team echo diversity benefits both Cantarella's Concerto cycling and Phrolova's Hecate activation count simultaneously

## Cantarella: Inherent Passives

**Inherent Skill 1 — Veiled Tempest**
- **+20% Healing Bonus** (unconditional, permanent)
- **Casting Echo Skill gives +6% Havoc DMG Bonus for 10 seconds, stackable up to 2 times** (+12% Havoc DMG Bonus at max stacks)
- Flickering Reverie and Perception Drain are both classified as Echo Skills; in a standard rotation, both fire within the same active window, easily maintaining 2 stacks throughout Cantarella's on-field time
- The Healing Bonus directly amplifies all Shiver-generated heals and the Perception Drain burst heal; IS1 is therefore simultaneously an offensive and defensive passive

**Inherent Skill 2 — Tidal Mastery**
- **+20% Havoc DMG Bonus** (unconditional, permanent)
- IS2 provides the largest unconditional Havoc bonus in Cantarella's kit; it applies to all Havoc DMG regardless of classification (Resonance Skill, Basic Attack, Liberation, Echo Skill)

## Cantarella: Intro/Outro Skills

**Intro Skill — Suite of Quietus (Outside Mirage)**
- Deals Havoc DMG; press Normal Attack shortly after to start the Basic Attack combo from Stage 3 (shortcut into the most Trance-efficient attack immediately)
- Grants **+1 Trance** on cast
- Triggers **Abyssal Rebirth** (25s Echo Skill Concerto recovery window)

**Intro Skill — Tidal Surge (Inside Mirage)**
- When Cantarella is in Mirage and re-enters the field via Intro Skill, the next Intro Skill becomes Tidal Surge
- Tidal Surge triggers **3 Coordinated Attacks** on hit, dealing Havoc DMG
- Resets the combo of Basic Attack Phantom Sting (allowing the Stage 3 Coordinated Attacks to fire immediately)
- Prydwen notes this as a meaningful additional damage source when the rotation allows a Mirage re-entry

**Outro Skill — Unfinished Aria**
- The incoming Resonator gains:
  - **+20% Havoc DMG Amplification for 14 seconds**
  - **+25% Resonance Skill DMG Amplification for 14 seconds**
  - Both effects expire when the receiving character is switched out
- The dual-buff Outro is Cantarella's primary support contribution and the reason she is used in teams beyond Phrolova:
  - For **Phrolova:** +20% Havoc Amplification applies to Phrolova's on-field attacks; +25% Resonance Skill Amplification applies to Phrolova's Reincarnate finishers (Movement of Fate and Finality / Murmurs in a Haunting Dream, both classified as Resonance Skill DMG); this dual amplification is maximally aligned with Phrolova's two primary attack categories
  - For **Jinhsi:** +25% Resonance Skill Amplification applies to Jinhsi's Resonance Skill attacks, which are central to her damage loop (Overflowing Radiance, Illuminous Epiphany)
  - For **Havoc Rover / Camellya:** +20% Havoc Amplification directly enhances their primary elemental damage
- **S2 interaction:** Healing Bonus is increased by +25% during Mirage (timing the Outro from inside Mirage provides additional healing value during the final heal burst of Perception Drain)

## Cantarella: Resonance Chains (Sequences)

**S1 — Dark Tide's Embrace**
- **Casting Resonance Skill recovers +1 Trance** (additional to the +1 already granted by Graceful Step; effectively +2 Trance per Resonance Skill cast)
- **DMG Multiplier of Graceful Step, Flickering Reverie, and Perception Drain increased by +50%** each
- **Immune to interruptions while casting Perception Drain**
- *Impact:* Three simultaneous improvements — faster Trance accumulation (+1 Trance/Skill), meaningful DMG boost to all three Resonance Skill forms (which are Cantarella's primary damage tools), and interruption immunity during the high-commitment Perception Drain cast; one of the most efficient single sequences in the game for the price. Prydwen notes S1 as the most consistent-value first investment.

**S2 — Surrender to the Illusive Reverie**
- **Resonance Liberation — Flowing Suffocation now sends the target into Hazy Dream** (enabling Jolt activation on the Liberation hit itself)
- **DMG Multiplier of Jolt triggered by Cantarella is increased by +245%**
- *Impact:* Destructoid: *"worth going for if you enjoy playing the character. It greatly boosts her personal damage output."* With S2, the Liberation-into-Mirage sequence can immediately apply Hazy Dream, fire a +245% multiplier Jolt on the next hit, and the standard Perception Drain Hazy Dream also becomes a +245% Jolt trigger; the damage ceiling of the full combo roughly doubles per Jolt opportunity

**S3 — Gaze into the Abyss**
- **DMG Multiplier of Resonance Liberation — Flowing Suffocation increased by +370%**
- **After casting Resonance Liberation, automatically enter Mirage** (eliminates the need for a separate Delusive Dive)
- *Impact:* Destructoid: *"By far the best stopping point before S6."* The Liberation hit goes from negligible to a genuine burst event (+370% is one of the largest single-sequence multiplier additions in the game); automatic Mirage entry on Liberation cast removes one entire rotation step and makes the Liberation-to-Perception Drain path one step shorter; S3 is the recommended investment ceiling for players who want to maximize Cantarella's DPS contribution without going to S6

**S4 — Behold Your Own Soul**
- **+25% Healing Bonus while in Mirage** (stacking with the baseline IS1 +20% and Outro S2 interaction)
- **Maximum Dreamweavers from Liberation Diffusion increased by +5**
- *Impact:* Destructoid: *"by far the worst of her Sequences... Cantarella's healing is already great by default, so this is not worth getting at all unless you're going beyond it."* The +5 Dreamweavers do add sustained off-field damage over the 30-second Diffusion window, but the DPS increase is marginal; S4 is correctly the skip sequence

**S5 — Dreams of the Sea**
- **DMG Multiplier of Phantom Sting increased by +80%** (the in-Mirage Basic Attack chain that generates Shiver and healing)
- *Impact:* Phantom Sting is cast frequently inside Mirage (3 times per standard Mirage window); +80% to all three stages is a meaningful personal DPS increase; S5 also makes the Mirage window itself more damage-dense while maintaining the same Shiver generation and healing throughput. A reasonable intermediate sequence between S3 and S6.

**S6 — The Final Descent**
- **Casting Resonance Liberation — Flowing Suffocation makes Cantarella's DMG ignore 30% of the target's DEF for 10 seconds**
- **For the first 1.2 seconds of Hazy Dream, when the target takes an instance of damage that does not inflict Hazy Dream, Jolt will NOT be triggered** (the Hazy Dream immunity window prevents the first hit from consuming the Jolt, allowing damage to accumulate before it fires)
- *Impact:* The 30% DEF Ignore is a multiplicative penetration effect that is most valuable against high-DEF enemies and in content where other amplifications are already stacked; the Hazy Dream immunity window ensures that AoE follow-up attacks from teammates can land on a Hazy Dream target before the single Jolt fires, ensuring all pending damage receives Hazy Dream's benefit before it clears. These two effects combined substantially elevate Cantarella's damage ceiling and damage delivery efficiency at S6. The maximum investment target for dedicated Cantarella players.

**Sequence Pull Priority:** S0 is functional but limited; **S1 is the most consistently recommended first purchase** (Prydwen, Destructoid); S3 as the stopping point for damage-focused investment; S6 for maximum ceiling.

## Cantarella: Recommended Echo Sets

**Primary Recommendation: Midnight Veil (5-piece)**
- The universally recommended set per Prydwen, Wutheringwaves-builds, and LDShop; purpose-matched to Cantarella's Havoc-element identity and Echo Skill frequency
- **Midnight Veil 5-piece full effect:** Increases Havoc DMG; additionally provides a Havoc DMG Bonus to teammates when Cantarella casts an Echo Skill, supporting the team's Havoc characters during Cantarella's rotation and after she swaps out
- **The team support aspect of Midnight Veil is the differentiator:** Unlike a pure personal-DPS set, Midnight Veil extends Cantarella's contribution beyond her own hits to the entire team's Havoc output window; this is why Wutheringwaves-builds specifically recommends it for both Cantarella herself and for Roccia in the Phrolova/Cantarella/Roccia team
- The 5-piece provides full value across both Cantarella's active window (personal Havoc DMG Bonus) and passive window (team Havoc DMG Bonus from her Echo Skill triggers)

**Alternative: Havoc Eclipse (5-piece)**
- Used for maximum personal Havoc DMG Bonus focus; less team support value than Midnight Veil but higher personal ceiling when Cantarella is the primary damage-dealing Sub-DPS
- Wutheringlab recommends this for DPS-oriented Cantarella builds specifically

**Main Echo — Lorelei (4-Cost)**
- The definitive best-in-slot main echo per Prydwen and multiple build guides
- **On activation:** Lorelei's echo skill deals substantial Havoc Echo Skill DMG; the echo is also the source of the weekly boss material (Axiom of Creation) required for Cantarella's ascension, thematically and practically linking her character and her materials
- The echo skill activation counts as an Echo Skill cast for the Abyssal Rebirth Concerto recovery (6 Concerto per unique echo activation while Abyssal Rebirth is active)

**Echo Main Stats Priority**
- 4-Cost Echo (Lorelei): CRIT Rate or CRIT DMG depending on current ratio
- 3-Cost Echoes (×2): CRIT DMG + Havoc DMG Bonus or ATK%
- 1-Cost Echoes: ATK%

**Sub-Stat Priority:** CRIT Rate (to ~75–80% with passives and Inherent Skill bonuses) > CRIT DMG > Havoc DMG Bonus > ATK% > Resonance Skill DMG Bonus. Note: IS2 (+20% Havoc DMG Bonus unconditionally) and IS1 (up to +12% Havoc Bonus from Echo Skill stacks) mean that a moderate amount of Havoc sub-stats on gear provides diminishing returns; CRIT stats are typically the better investment above threshold.

## Cantarella: Recommended Weapons

**Best-in-Slot — Sea of Desire (5-Star Signature Rectifier)**
- Purpose-built for Cantarella's Echo Skill-centric kit and Havoc focus
- **Stat:** CRIT Rate (high base — addresses the primary build requirement)
- **Passive:**
  - After dealing **Basic Attack DMG**: gain **+24% Havoc DMG Bonus** for 10 seconds (stackable up to 2 times = +48% maximum); Cantarella's Phantom Sting Basic Attacks and Perception Drain (classified as Basic Attack DMG) both trigger this
  - After casting an **Echo Skill** (Flickering Reverie, Perception Drain, Liberation): gain **+12% ATK** for 10 seconds (stackable up to 2 times = +24% maximum)
  - The dual buff structure directly matches Cantarella's two primary damage categories (Basic Attack DMG and Echo Skill), and both buffs maintain near-permanent uptime during her active window given how frequently she performs both action types
- LDShop: *"a standout weapon tailored for Havoc-focused Resonators like Cantarella"*

**Best Standard Alternative — Stringmaster (5-Star)**
- The reliable standard-pool fallback; CRIT DMG stat; passive provides general resonance skill/echo skill bonus; functional but below signature ceiling

**Best 4-Star — Jinzhou Keeper / Variation**
- High-refinement 4-star options that provide CRIT Rate or ATK% at competitive values; Game8 documents these as the best non-5-star options; Variation specifically is noted for providing a strong passive for healer-support types

**F2P Option — Rectifier of Night**
- Craftable or obtainable from event/exploration; functional baseline weapon for early investment; verify current availability with the Fandom Wiki

## Cantarella: Best Teams

**Optimal: Phrolova / Cantarella / Roccia**
- The definitive best Cantarella composition (see Phrolova kit documentation for full rotation); Cantarella is specifically *"essential"* in this team (Game8) because her dual Echo Skill activations (Flickering Reverie + Perception Drain) fire 2 of Hecate's allowed 10 Enhanced Attacks per Maestro window, and her Abyssal Rebirth Concerto recovery allows for faster subsequent rotations
- **Cantarella's specific contributions:**
  - Outro: +20% Havoc / +25% Resonance Skill Amplification to Phrolova on re-entry (maximally aligned with Phrolova's two damage categories)
  - Echo Skills: each cast fires Hecate Enhanced Attack during Phrolova's off-field Maestro; Lorelei echo also counts
  - Dreamweaver Coordinated Attacks: sustained off-field Havoc damage during the rotation's passive phases
  - Hazy Dream + Jolt: supplementary damage triggered by Phrolova's and Roccia's hits during Cantarella's Hazy Dream windows
  - Healing: sustained team health via Shiver-generated heals, removing the need for a dedicated healer
- **Rotation overview (Cantarella window):**
  1. Intro Skill (+1 Trance, Abyssal Rebirth active) → Normal Attack shortcut to Basic Attack Stage 3 (+1 Trance) → Resonance Skill Graceful Step (+1 Trance) → Liberation Flowing Suffocation (+2 Trance; now at ≥4 Trance total)
  2. Heavy Attack Delusive Dive → enter Mirage (−1 Trance; now 3 Trance remaining)
  3. Flickering Reverie (Echo Skill → Hazy Dream applied; Hecate fires Enhanced Attack)
  4. Phantom Sting ×3 (Stages 1–2–3, each consuming Trance and granting Shiver + heal; Stage 3 also triggers 3 Coordinated Attacks)
  5. Perception Drain at 3 Shiver (Echo Skill → high DMG + burst heal + Hazy Dream reapplication; Hecate fires Enhanced Attack)
  6. Outro Skill active → swap to Phrolova/Roccia

**Strong Alternative: Jinhsi / Cantarella / Zhezhi (or Verina)**
- Cantarella's Outro +25% Resonance Skill Amplification is extremely valuable for Jinhsi, whose primary DPS skills (Overflowing Radiance, Illuminous Epiphany, Ordination Glow) are all Resonance Skill classified
- OSLink guide notes this as the context where Cantarella becomes *"Jinhsi's best teammate"* — the Resonance Skill amplification provides a greater proportional boost for Jinhsi's kit than almost any other Outro buff available
- Rotation for this team starts with Cantarella, follows with Zhezhi or Verina depending on the third slot, and enters Jinhsi's field window with the Cantarella Outro active for the Incarnation-mode burst

**Havoc DPS Teams: Havoc Rover / Cantarella / Healer; Camellya / Cantarella / Roccia**
- Any Havoc Main DPS benefits from Cantarella's +20% Havoc Amplification Outro, Hazy Dream Jolt follow-up damage, and Dreamweaver sustained Havoc Coordinated Attacks
- Camellya + Cantarella has specific synergy: Cantarella's healing removes the need for a dedicated healer, allowing a more offensive third slot; Roccia groups enemies for both Camellya's AoE and Cantarella's AoE Perception Drain; the team has high combined Havoc Bonus contributions

## Cantarella: Rotation Guide

**Standard Rotation (any team)**
1. Enter via **Intro Skill** (+1 Trance, Abyssal Rebirth window begins)
2. Normal Attack shortcut → **Basic Attack Stage 3** (+1 Trance; if Abyssal Rebirth is active, the Stage 3 Coordinated Attacks may trigger Echo Skill Concerto recovery from teammates' echoes)
3. **Resonance Skill — Graceful Step** (+1 Trance; or +2 at S1)
4. **Resonance Liberation — Flowing Suffocation** (+2 Trance; Dreamweavers summoned for 30-second sustained damage; at S3: automatically enters Mirage; at S2: applies Hazy Dream)
5. **Heavy Attack — Delusive Dive** (if not in Mirage already from S3; consumes 1 Trance; enters Mirage)
6. **Resonance Skill — Flickering Reverie** (Echo Skill: Hazy Dream applied; Jolt armed; Hecate fires Enhanced Attack if Phrolova is off-field)
7. **Basic Attack Phantom Sting ×3** (Stages 1–2–3 in Mirage; each hit: −1 Trance, +1 Shiver, +team heal; Stage 3 triggers 3 Coordinated Attacks)
8. **Forte Circuit — Perception Drain** at 3 Shiver (Echo Skill: high Havoc DMG + burst team heal + Hazy Dream reapplied; Hecate fires Enhanced Attack; large Concerto Energy granted)
9. **Outro Skill** → incoming character receives +20% Havoc Amplification + 25% Resonance Skill Amplification for 14 seconds

**Fast Rotation (reduced field time)**
For teams where Cantarella needs to spend minimal on-field time (e.g., when Phrolova's Maestro window is active and Hecate Enhanced Attack triggers are the priority):
1. Intro Skill (+1 Trance)
2. Resonance Skill Graceful Step (+1 Trance; +2 at S1)
3. Liberation Flowing Suffocation (+2 Trance; Dreamweavers deployed)
4. Delusive Dive (enter Mirage)
5. Flickering Reverie (Hazy Dream; Echo Skill; Hecate trigger)
6. Phantom Sting ×3 (3 Shiver built; 3 heals delivered)
7. Perception Drain (burst damage + heal + Echo Skill; Hecate trigger)
8. Outro → swap immediately
Total field time: approximately 10–12 seconds

**Key Rotation Rules**
- Perception Drain's 18-second cooldown is the primary rotation timer: plan the full Trance accumulation → Mirage → Flickering Reverie → Phantom Sting × 3 → Perception Drain sequence to fit within the 18-second window between Perception Drain casts
- Both Flickering Reverie and Perception Drain count as Echo Skill casts: in Phrolova teams, each fires one Hecate Enhanced Attack; in all teams, each triggers Abyssal Rebirth Concerto recovery (6 Concerto per unique echo cast) and IS1 Havoc DMG Bonus stacking
- Hazy Dream from Flickering Reverie has 6.5 seconds before it expiries; the Jolt fires on the first hit that lands after application; in ideal timing, the first Phantom Sting hit immediately after Flickering Reverie fires the Jolt; S6's 1.2s immunity window prevents this premature firing, allowing more hits to land before the Jolt consumes the debuff

## Cantarella: Sources

- Prydwen Institute — Cantarella build guide, team compositions, Abyssal Rebirth mechanic: https://www.prydwen.gg/wuthering-waves/characters/cantarella/
- Wutheringlab — Cantarella build, Trance/Shiver mechanics, fast rotation: https://wutheringlab.com/character/cantarella-build/
- Game8 — Cantarella best builds, Phrolova team synergy, optimal combo: https://game8.co/games/Wuthering-Waves/archives/500493
- LDShop — Cantarella complete build guide (V2.7/V2.8): https://www.ldshop.gg/blog/guide/wuthering-waves-cantarella-build-guide.html
- Lootbar.gg — Cantarella build guide and weapon comparison: https://lootbar.gg/blog/en/wuthering-waves-cantarella-build-guide.html
- Destructoid — Cantarella build guide with Sequence evaluation: https://www.destructoid.com/best-cantarella-build-in-wuthering-waves-weapons-echoes-team-compositions-and-sequences/
- Wutheringwaves-builds — Cantarella full rotation, team compositions including Phrolova: https://wutheringwaves-builds.com/character/cantarella/
- Wuthering.gg — Cantarella full kit descriptions, stat baseline: https://wuthering.gg/characters/cantarella
- OSLink — Cantarella Phrolova/Jinhsi team guides: https://www.oslink.io/blog/guide/wuthering-waves-cantarella-build-guide.html
