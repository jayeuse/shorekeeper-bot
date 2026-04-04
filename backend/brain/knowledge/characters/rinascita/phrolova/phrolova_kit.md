---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/rinascita/phrolova/phrolova_kit.md
character: Phrolova
group: Rinascita / Fractsidus (former) / Lost Beyond
document_type: character_kit
importance: high
tags:
  - character
  - kit
  - combat
  - havoc
  - rectifier
  - main-dps
  - off-field-dps
  - volatile-notes
  - aftersound
  - reincarnate
  - scarlet-coda
  - resolving-chord
  - maestro
  - hecate
  - zero-energy-liberation
  - dream-of-the-lost
  - lethean-elegy
  - cantarella
  - roccia
  - version-2-5
---

# Phrolova Kit Documentation
<!-- Sources: https://www.prydwen.gg/wuthering-waves/characters/phrolova/, https://wutheringlab.com/character/phrolova-build/, https://game8.co/games/Wuthering-Waves/archives/524877, https://www.ldshop.gg/blog/guide/phrolova-build-wuthering-waves.html, https://gamingpromax.com/wuwa-phrolova/, https://wuthering.gg/characters/phrolova -->

## Phrolova: Combat Archetype and Role

- **Element:** Havoc
- **Weapon Type:** Rectifier (Lycoris baton)
- **Role:** Havoc Hypercarry Main DPS; dual on-field / off-field damage dealer via Hecate during Maestro state
- **Archetype:** Volatile Note accumulator → Scarlet Coda → Resolving Chord → zero-energy Liberation → Maestro (Hecate summoning) → off-field Echo Skill–triggered Enhanced Attacks; Aftersound CRIT DMG stacker
- **Introduced:** Version 2.5 (July 24, 2025); first half banner; rerun Version 2.8 Phase 1

Phrolova is described across multiple major build resources as the best Havoc DPS in Wuthering Waves at her release, positioned at T0.5 tier with full investment. Her most structurally unique feature — and the feature no future character can replicate — is that her Resonance Liberation costs **zero Resonance Energy**; it is exclusively gated by the Resolving Chord state, which itself requires a specific sequence of Volatile Note accumulation and Scarlet Coda execution. This removes the Energy Regen tax that burdens every other DPS in the game, allowing all gear and build resources to be allocated elsewhere.

Her Maestro Liberation summons Hecate — a Calamity-class Tacet Discord that deals Havoc Echo Skill DMG and continues attacking off-field when Phrolova swaps to teammates. Crucially, Hecate's Enhanced Attacks fire whenever a teammate casts an Echo Skill (up to 10 total per Maestro duration), making Echo Skill-heavy teammates essential multipliers of her off-field damage. This creates a unique team-building requirement: Phrolova is most powerful in dedicated Echo Skill teams, and underperforms when teammates have low Echo Skill frequencies.

The build platform Gamingpromax calls her *"the only character who can exploit the Dream of the Lost 3-PC echo set to its full permanent potential — a genuine structural advantage no future character can take away."*

## Phrolova: Key Resources — Volatile Notes, Aftersound, and Hecate's Echo Skill Trigger

Phrolova's combat system runs on three interconnected mechanics, each serving a distinct role.

**Volatile Notes (0 to 6 stacks)**
- The gate to Scarlet Coda, which is the gate to the Resonance Liberation
- **Six Note types:** Volatile Note – Strings (blue); Volatile Note – Winds (blue); Volatile Note – Cadenza (red/purple); the ratio of red (Cadenza) to blue (Strings/Winds) at the moment of Liberation activation determines whether Phrolova cries or laughs during the Liberation animation — a rare instance of combat mechanics directly expressing emotional state
- **Note generation:**
  - **Basic Attack Stage 3** hit → **+1 Volatile Note – Strings**; Stage 3 also enters the Reincarnate state, which provides access to enhanced follow-up attacks
  - **Resonance Skill – Whispers in a Fleeting Dream** hit → **+1 Volatile Note – Winds**; also sends Phrolova to Reincarnate
  - **Inherent Skill – Accidental (IS2):** After casting Suite of Quietus, Suite of Immortality, or an Echo Skill, the **next Volatile Note becomes Volatile Note – Cadenza** instead of Strings or Winds; this means every Echo Skill cast upgrades one note to Cadenza, which is important because Cadenza notes give Hecate the most powerful Enhanced Attack variant (Strings and pull-in combined)
- **Stack cap and overflow:** Maximum 6 Volatile Notes; if at full capacity, gaining a new Note pushes all existing Notes one slot left and the leftmost Strings or Winds note is removed; Cadenza notes cannot be removed by overflow
- **Out-of-combat recovery:** If Phrolova has fewer than 2 Volatile Notes outside of combat for 4 seconds, she automatically gains Volatile Note – Cadenza until she has at least 2; this prevents starting a new encounter without Notes
- **Cannot accumulate Notes during Resolving Chord state**

**Aftersound (0 to 24 stacks)**
- Phrolova's CRIT DMG stack mechanic; scales Scarlet Coda's DMG multiplier and governs the CRIT DMG build reward system
- **Generation:**
  - **On entering battle:** Gain **10 stacks of Aftersound** automatically (once per 4 seconds after leaving combat)
  - **Hecate's Enhanced Attacks during Maestro state:** Each cast of Enhanced Attack – Hecate: Strings, Enhanced Attack – Hecate: Winds, or Enhanced Attack – Hecate: Cadenza while Phrolova is **not the active Resonator** grants **+1 Aftersound stack**
  - **S2:** Casting Scarlet Coda grants **+14 Aftersound stacks** directly (the largest single Aftersound injection, transforming the warmup issue entirely)
- **CRIT DMG scaling:**
  - For every 1 Aftersound stack: **+2.5% CRIT DMG** (to a maximum of 24 × 2.5% = **+60% CRIT DMG** at baseline cap)
  - When Aftersound exceeds maximum (24): each additional stack grants **+1% CRIT DMG**, up to a further **+100% CRIT DMG** bonus (verified via S2-related discussion in Prydwen and Gamingpromax guides)
  - **Aftersound is cleared when Phrolova exits combat** — after 30 seconds out of combat, all stacks reset; the combat-entry 10-stack grant ensures she re-enters with a head start
- **Scarlet Coda scaling:** Each Aftersound stack increases the DMG Multiplier of Scarlet Coda by a base amount (41.53% at skill level 1, up to 82.55% at level 10 per stack); at S2, this is additionally augmented by another 75% per Aftersound stack on top of the base; S2 effectively more than doubles Scarlet Coda's Aftersound scaling contribution

**Hecate's Echo Skill Trigger (the off-field damage multiplier)**
- When Phrolova is **not the active Resonator** and a teammate casts an Echo Skill, Hecate casts an **Enhanced Attack – Hecate** (fired by whichever Volatile Note type is currently queued)
- This effect can trigger a maximum of **10 times per Maestro state**
- **Unique Echo restriction:** Echoes of the same name can only trigger this effect **1 time per Maestro duration** — team composition must use differently-named echoes to maximize the 10 triggers
- The type of Enhanced Attack – Hecate fired depends on the current Volatile Note being played:
  - **Strings note → Enhanced Attack – Hecate: Strings:** Havoc Echo Skill DMG + Stagnation
  - **Winds note → Enhanced Attack – Hecate: Winds:** Havoc Echo Skill DMG + pull-in
  - **Cadenza note → Enhanced Attack – Hecate: Cadenza:** Havoc Echo Skill DMG + Stagnation + pull-in simultaneously
- **Cadenza is most valuable** because it provides both crowd control effects; Inherent Skill 2 (Accidental) ensures that every Echo Skill cast converts one upcoming Note to Cadenza, making the team's Echo Skills function as note upgrades in addition to Hecate trigger sources
- Gamingpromax: *"Her Hecate off-field system rewards team building with Echo Skill casters — a synergy no other character offers in the same way."*

## Phrolova: Stats Baseline

| Level | HP | ATK | DEF |
|-------|----|-----|-----|
| Lv. 1 | 862 | 35 | 93 |
| Lv. 20 | 2,242 | 91 | 238 |
| Lv. 40 | 4,269 | 176 | 452 |
| Lv. 60 | 6,871 | 287 | 725 |
| Lv. 80 | 9,473 | 390 | 999 |
| Lv. 90 | 10,775 | 437 | 1,136 |

*Exact figures from wuthering.wiki; Forte Attribute Bonuses not included.*

## Phrolova: Ascension Materials

| Ascension | Level Cap | Key Materials |
|-----------|-----------|---------------|
| 1 | 20→40 | LF Whisperin Core ×4, [Specialty] ×4, Shell Credits ×5,000 |
| 2 | 40→50 | MF Whisperin Core ×4, [Specialty] ×8, Shell Credits ×10,000 |
| 3 | 50→60 | HF Whisperin Core ×8, [Specialty] ×12, Boss Material ×4, Shell Credits ×15,000 |
| 4 | 60→70 | HF Whisperin Core ×8, [Specialty] ×16, Boss Material ×8, Shell Credits ×20,000 |
| 5 | 70→80 | FF Whisperin Core ×12, [Specialty] ×20, Boss Material ×12, Shell Credits ×40,000 |
| 6 | 80→90 | FF Whisperin Core ×12, [Specialty] ×24, Boss Material ×16, Shell Credits ×80,000 |

**Total Ascension Shell Credits:** ~170,000
- **Whisperin Cores (LF/MF/HF/FF):** Dropped by Whisperin Tacet Discord enemies; craftable via Synthesizer; available from Forgery Challenge: Marigold Woods
- **Local Specialty:** Verify exact Rinascita specialty required for Phrolova with the Fandom Wiki
- **Boss Material:** Verify exact weekly boss source for Phrolova's Axiom of Creation or equivalent material with the Fandom Wiki

## Phrolova: Skill Upgrade Materials

- **Total Forte Shell Credits (all skills):** ~2,030,000
- **Skill Books:** Verify appropriate Forgery Challenge tier with Fandom Wiki
- **Weekly Boss Material:** Verify exact drop with Fandom Wiki

**Skill Upgrade Priority:** Forte Circuit (Volatile Notes / Scarlet Coda / Aftersound scaling) → Resonance Liberation (Maestro duration and Hecate Enhanced Attack multipliers) → Resonance Skill (Whispers in a Fleeting Dream — Note generation and Reincarnate enhanced attacks) → Intro Skill → Basic Attack. The Forte Circuit and Liberation are where Phrolova's primary damage multipliers live; Resonance Skill is the secondary priority as it generates Notes and enables Reincarnate enhanced attacks; Basic Attack and Intro Skill are lower priority but still contribute to Note generation and the rotation.

## Phrolova: Character Kit — Basic Attack: Movement of Life and Death

**Ground Chain (3 stages)**
- Up to 3 consecutive Havoc DMG attacks
- **Stage 3** — the critical attack in the chain: on hitting a target, Stage 3 grants **+1 Volatile Note – Strings** AND sends Phrolova into **Reincarnate** state
- Pressing Normal Attack after Heavy Attack performs Stage 2 directly (skipping Stage 1 and Stage 3 for speed); this is the shortcut used in quickswap rotations

**Reincarnate State**
- Entered by: Basic Attack Stage 3 hit, or Resonance Skill – Whispers in a Fleeting Dream hit
- **In Reincarnate, two enhanced attack options replace standard attacks:**
  - **Normal Attack press on ground → Movement of Fate and Finality:** Havoc DMG classified as **Resonance Skill DMG**; Stagnates target; ends Reincarnate; grants **+1 Volatile Note – Strings**
  - **Resonance Skill press on ground → Murmurs in a Haunting Dream:** Havoc DMG classified as **Resonance Skill DMG**; ends Reincarnate; grants **+1 Volatile Note – Winds**
- Both Reincarnate finishers grant Notes AND are classified as Resonance Skill DMG, making them scale with Resonance Skill DMG Bonus from weapons and passives
- **S1:** Movement of Fate and Finality and Murmurs in a Haunting Dream DMG multipliers are each increased by **+80%**, making these the two highest-value individual hits in the Note-building phase
- **S6:** During Movement of Fate and Finality and Murmurs in a Haunting Dream, command Hecate to cast **1 Apparition of Beyond** (Echo Skill DMG, 216.42% ATK) and grant **+8 Aftersound**

**Heavy Attack**
- Standard Havoc DMG (Stamina cost); press Normal Attack shortly after to cast Basic Attack Stage 2
- When conditions are met (6 Volatile Notes + Compose state + not Resolving Chord): heavy attack input becomes **Scarlet Coda** instead

**Mid-Air Attack and Dodge Counter**
- Standard Havoc DMG; Dodge Counter press after dodge → Havoc DMG; Normal Attack after Dodge Counter → Basic Attack Stage 3

## Phrolova: Character Kit — Scarlet Coda (Forte-Enhanced Heavy Attack)

**Activation conditions (all three must be true simultaneously):**
- Has **6 Volatile Notes**
- In the **Compose state** (Compose state is entered every 25 seconds; it is a passive timer, not an activated skill)
- **Not** in the **Resolving Chord** state

**Effect:**
- Consume Stamina to deal Havoc DMG to all nearby targets; Stagnation and pull-in on hit
- **DMG Classification:** Resonance Skill DMG; also counts as casting an Echo Skill (enabling IS2 Volatile Note Cadenza conversion on the next Note)
- **Aftersound scaling:** Each Aftersound stack increases the DMG Multiplier of Scarlet Coda by the base rate (41.53%–82.55% per stack depending on skill level); S2 adds another 75% per Aftersound stack on top; this makes Scarlet Coda's total damage multiplier heavily variable based on Aftersound accumulation — a fully stacked Aftersound Scarlet Coda is orders of magnitude more powerful than a 0-stack cast
- **After casting:** Compose state goes on cooldown (25 seconds before next Compose state); **Resolving Chord state activates**

**The 25-second Compose cooldown**
The 25-second Compose cooldown is the primary structural constraint on Phrolova's rotation frequency: she can only cast Scarlet Coda and enter the Liberation cycle once every 25 seconds at minimum. This is the reason her rotation is designed as a single extended 24-second Maestro window followed by efficient Note rebuilding for the next cycle, rather than frequent shorter rotations.

## Phrolova: Character Kit — Resolving Chord State

- Entered by casting Scarlet Coda
- **In Resolving Chord:** Cannot gain new Volatile Notes; existing Notes are locked and queued for Maestro playback
- **Resolving Chord enables Resonance Liberation (Waltz of Forsaken Depths):** the Liberation skill button becomes available; pressing it exits Resolving Chord and enters Maestro
- **Resolving Chord can be exited early** by Curtain Call (see Liberation section); doing so removes all Volatile Notes

**The locked Notes during Resolving Chord**
The "locking" of Notes during Resolving Chord is narratively and mechanically appropriate: this is the moment where the composition is finalized before the performance. The Notes on the Forte Circuit bar literally cannot change — the score is set. The ratio of red (Cadenza) to blue (Strings/Winds) at this locked state is what determines the Liberation's emotional register.

## Phrolova: Character Kit — Resonance Liberation: Waltz of Forsaken Depths

**Unique liberation mechanic:**
- **Zero Resonance Energy cost** — Phrolova has no Resonance Energy whatsoever; the Liberation is gated exclusively by the Resolving Chord state
- **Available only while in Resolving Chord state**
- **Curtain Call (alternative entry):** Holding Resonance Liberation in Resolving Chord activates Curtain Call instead, which removes all Volatile Notes and exits Resolving Chord without entering Maestro; only used when a full Maestro cycle would interfere with team rotation timing

**On casting Waltz of Forsaken Depths:**
- Exits Resolving Chord state
- Phrolova enters **Maestro state for 24 seconds**
- Initial hit: Havoc DMG (Liberation DMG classification)
- **Emotional animation:** More Cadenza (red) notes at time of casting → Phrolova cries during the Liberation; more Strings/Winds (blue) notes → Phrolova laughs in madness during the Liberation; the animation is the most cited emotional feature of her characterization among players

**Maestro State (24 seconds):**
- Phrolova gains **+120% ATK** (passive during the entire Maestro duration)
- Phrolova floats in the air and commands Hecate to fight
- Hecate shares Phrolova's stats and statuses; all damage dealt by Hecate is treated as coming from Phrolova
- **Hecate's attacks do NOT remove the target's Hazy Dream state** — a specific compatibility note for Cantarella teams (Cantarella's Hazy Dream debuff enables specific team combo chains; Hecate's presence does not disrupt it)
- Phrolova plays the queued Volatile Notes in turn; each Volatile Note is held for **4 seconds** before playing
- **While Phrolova is active (on-field during Maestro):**
  - Normal Attack → Hecate casts **Basic Attack – Hecate** (Havoc Echo Skill DMG, 2 stages)
  - Every 2nd Basic Attack – Hecate: the next one is replaced by **Enhanced Attack – Hecate** (fires the queued Note type's variant)
  - Dodge → Hecate dodges; Hecate takes no damage from a successfully dodged hit
  - Jump → Resets Hecate's position
  - Resonance Liberation → Curtain Call (ends Maestro)
- **While Phrolova is not active (off-field during Maestro):**
  - Hecate automatically casts Basic Attack – Hecate on target
  - When **any teammate casts an Echo Skill:** Hecate casts **Enhanced Attack – Hecate** (using the current queued Note type); this trigger can fire up to **10 times total** per Maestro duration; echoes of the same name can only trigger it **once**
  - Hecate takes no damage when Phrolova is off-field

**Curtain Call (Maestro exit)**
Five trigger methods exist: active on-field end; switching to Phrolova without Intro Skill while in Maestro; Maestro ending while Phrolova is off-field (then switching); pressing Liberation while in Maestro; holding Liberation in Resolving Chord. Effect: Stagnates targets + Havoc DMG; ends Maestro state. In Resolving Chord: Curtain Call removes all Volatile Notes.

**Skill Upgrade Priority:** Second — the Hecate Enhanced Attack multipliers (Strings/Winds/Cadenza at 100% ATK + 243% ATK for two-hit variants), Curtain Call multiplier (234%–465%), and the Maestro's 120% ATK boost all scale with level.

## Phrolova: Inherent Passives

**Inherent Skill 1 — Cadence (Combat Entry Aftersound)**
- **On entering battle:** Gain **10 stacks of Aftersound** (+25% CRIT DMG from the baseline 2.5%/stack rate); this effect cannot trigger again within 4 seconds of exiting combat
- Additionally: **Casting Echo Skill** grants **increased interruption resistance and −30% damage taken for 15 seconds**
- The combat-entry Aftersound ensures Phrolova starts every encounter with a CRIT DMG foundation; the Echo Skill survivability effect makes the Echo Skill cast timing important for both offense (IS2 Note upgrade) and defense (+30% damage reduction)

**Inherent Skill 2 — Accidental (Cadenza Note Conversion)**
- After casting **Suite of Quietus, Suite of Immortality, or an Echo Skill**, the **next Volatile Note gained becomes Volatile Note – Cadenza** instead of Strings or Winds
- **Practical impact:** Every Echo Skill cast upgrades one future Note to Cadenza; since Cadenza Notes trigger the most powerful Hecate Enhanced Attack variant (Cadenza: Stagnation + pull-in combined) and are not removed by the stack overflow mechanic, IS2 makes the team's Echo Skill frequency directly translate to an increase in the proportion of high-value Notes in Phrolova's Forte Circuit

## Phrolova: Intro/Outro Skills

**Intro Skill — Suite of Quietus**
- Standard: Deals Havoc DMG; press Normal Attack after to cast Basic Attack Stage 3; 10 Concerto Energy generated
- **Suite of Immortality (Maestro-state variant):** When Phrolova is in the Maestro state, the next Suite of Quietus is replaced with Suite of Immortality — deals significantly higher Havoc DMG (300%–596% ATK at level 1–10), classified as **Resonance Skill DMG**, and Stagnates targets; 10 Concerto Energy generated
- Suite of Immortality is cancelled if Curtain Call fires during the Maestro window before re-entry
- **This is the mechanic that makes re-entering during Maestro rewarding:** if the team rotation allows Phrolova to re-enter via Intro Skill while Maestro is still active, she lands Suite of Immortality (a ~596% ATK Resonance Skill hit at max level) instead of the standard Suite of Quietus; this is the primary reason the full team rotation is designed to complete within 24 seconds

**Outro Skill — Unfinished Piece**
- The incoming Resonator gains **+20% Havoc DMG Amplification** AND **+25% Heavy Attack DMG Amplification** for **14 seconds** (or until they switch out)
- **Additionally, if Phrolova is still in Maestro state when she casts this Outro:** Hecate casts **Enhanced Attack – Hecate 2 additional times** upon Phrolova switching off
- This additional 2-hit trigger from the Outro during Maestro is the reason Phrolova should Outro while still in Maestro whenever possible — the Outro both delivers dual buffs to the incoming character AND generates two more Hecate Enhanced Attacks before the Maestro window closes
- **Primary Outro recipients:**
  - **Roccia:** receives both +20% Havoc Amplification AND +25% Heavy Attack Amplification simultaneously (Roccia's plunging attacks are both Havoc and Heavy Attack type); this dual benefit is the strongest single-character Outro interaction in the available Havoc team
  - **Cantarella:** receives Havoc DMG Amplification for her active field window; also contributes Echo Skills back to Hecate

## Phrolova: Resonance Chains (Sequences)

**S1 — Aria of Distant Echoes**
- DMG Multiplier of **Movement of Fate and Finality** increased by **+80%**
- DMG Multiplier of **Murmurs in a Haunting Dream** increased by **+80%**
- *Impact:* Both Reincarnate enhanced finishers — the primary on-field Note-building attacks — nearly double in individual hit damage; since these are the two most frequently cast Resonance Skill DMG hits during Phrolova's on-field window, S1 is a clean, consistent DPS increase across every rotation; Gamingpromax rates S1 as the standard first-sequence investment

**S2 — Chromatic Scale (THE defining sequence)**
- **Scarlet Coda DMG Multiplier increased by +75%** (base multiplier boost before Aftersound scaling)
- **Aftersound now additionally increases Scarlet Coda's DMG Multiplier by +75% per stack** (on top of the base rate from skill level, which ranges from 41.53%–82.55% per stack; S2 approximately doubles the Aftersound-per-stack contribution to Scarlet Coda)
- **Casting Scarlet Coda grants +14 stacks of Aftersound** (eliminating the multi-rotation Aftersound warmup problem entirely)
- *Impact:* Gamingpromax: *"S2 is the single strongest sequence node upgrade in the game at time of writing, transforming Aftersound warmup from a multi-rotation issue to a non-issue"* and *"S2 alone generates +37% DPS."* At S0, Phrolova must accumulate Aftersound gradually over Hecate's off-field attacks (1 stack per Enhanced Attack × up to 10 per Maestro = slow); at S2, each Scarlet Coda cast immediately grants 14 stacks, beginning the rotation with full CRIT DMG scaling from the first cycle. This is the strongly recommended first sequence investment beyond S0.

**S3 — Discordant Symphony**
- **Echo Skill DMG is Amplified by 80%**
- **Casting Scarlet Coda converts all Volatile Notes to Volatile Notes – Cadenza in turn** (every Note becomes Cadenza before the Maestro window; every Hecate Enhanced Attack during that Maestro fires the Cadenza variant with Stagnation + pull-in)
- **Targets hit by Enhanced Attack – Hecate: Cadenza have ATK reduced by 20% for 15 seconds** (team-wide survivability and damage mitigation contribution)
- *Impact:* The most complex sequence — the 80% Echo Skill Amplification applies to all of Hecate's Enhanced Attacks and to Phrolova's own Scarlet Coda (which is Echo Skill–typed); the universal Cadenza conversion means all 10 Hecate trigger slots fire the most powerful variant; the ATK reduction debuff adds team utility; LDShop describes this as the threshold where Phrolova shifts from personal DPS investment to team-wide synergy enhancement. Gamingpromax: recommended pull target for players who want to invest in Phrolova as a DPS main (S3R0)

**S4 — Eternal Maestro**
- **Casting Echo Skill grants +20% Attribute DMG Bonus for all Resonators in the team for 30 seconds**
- **Upon entering Maestro state:** generates a stagnation field around Phrolova for 4 seconds; leaving Maestro or switching Resonators ends it early
- **During Maestro state:** damage taken is reduced by 30%
- *Impact:* The team-wide buff is S4's primary value — 20% Attribute DMG Bonus for 30 seconds on every Echo Skill cast affects the entire team and substantially amplifies both Cantarella and Roccia's damage during their field windows; the survivability contributions (30% damage reduction in Maestro, 4s Stagnation on Maestro entry) are meaningful quality-of-life improvements for challenging content

**S5 — Lost Requiem**
- Enhanced Attack – Hecate DMG Multiplier increased by **+24%** (verify exact application scope with Fandom Wiki — whether this applies to all Enhanced Attack variants or only specific ones)
- *Impact:* Gamingpromax: *"Skip S5 as a standalone goal — it only provides utility, not damage"*; the Enhanced Attack multiplier increase is real but modest compared to S2's transformative effect; S5 is worth having but not worth targeting independently

**S6 — A Night to Depart From Eternal Rest**
- During Movement of Fate and Finality and Murmurs in a Haunting Dream: command Hecate to cast **1 Apparition of Beyond – Hecate** (Havoc Echo Skill DMG = **216.42% ATK**) and grant **+8 stacks of Aftersound** per cast
- **If Phrolova is the active Resonator during Maestro:** gain **+60% Havoc DMG Bonus**
- **If Phrolova is not the active Resonator during Maestro:** targets take **+40% more DMG from Hecate and Phrolova**
- *Impact:* The maximum sequence; S6 adds Aftersound generation to every Reincarnate finisher and introduces a DEF-penetration-like condition (either Phrolova herself gets +60% Havoc Bonus, or enemies take +40% more damage from her off-field attacks, depending on whether she is on-field); Gamingpromax recommends S6 as the max hypercarry investment target (S6R0 designation)

**Sequence Pull Priority:** S0 for standard DPS; **S2 is the most transformative single investment in the game** (Gamingpromax) and the primary recommended additional sequence; S1 for on-field damage boost; S3 for advanced team synergy and the Cadenza conversion; S6 for maximum hypercarry ceiling. Path: S0R1 → S2R0 → S3R0 → S6R0 per Gamingpromax.

## Phrolova: Recommended Echo Sets

**Best-in-Slot — Dream of the Lost (3-piece) + Havoc Eclipse (2-piece)**
- The universally recommended primary set per Prydwen, Wutheringlab, Wutheringwaves-builds, and Gamingpromax
- **Dream of the Lost 3-piece:** Provides unconditional CRIT Rate bonus; Phrolova is the only character who can exploit this set's condition for **permanent** maximum effect, because her zero-energy Liberation removes the Energy Regen requirement that forces other DPS characters to compromise; the CRIT Rate from the 3-piece feeds Phrolova's CRIT DMG scaling (Aftersound converts CRIT DMG; she wants high CRIT Rate to maximize the value of every CRIT DMG stack)
- **Havoc Eclipse 2-piece:** +10% Havoc DMG Bonus; the most efficient 2-piece complement; unconditional Havoc DMG amplification on all her attacks
- **Why this beats 5-piece Havoc Eclipse:** The Dream of the Lost CRIT Rate contribution is more stat-efficient per slot than the Havoc Eclipse 4th and 5th piece effects at typical gear quality

**Main Echo — Nightmare: Hecate (3-Cost)**
- The definitive best-in-slot main echo per Prydwen, wutheringwaves-builds, and Gamingpromax
- **On activation:** deals Havoc Echo Skill DMG; provides **+Resonance Skill DMG Bonus and +Echo Skill DMG** amplification to Phrolova for a duration
- Both bonuses directly amplify Phrolova's two primary damage categories (Resonance Skill and Echo Skill)
- The fact that the echo is named Hecate — the same Tacet Discord Phrolova summons in Liberation — makes this echo narratively and mechanically the definitive Phrolova echo; it is not merely optimal but purpose-built

**Alternative Main Echo — Nightmare: Dreamless (in 5-piece Havoc Eclipse builds)**
- Used when the player is running a full 5-piece Havoc Eclipse set rather than the 3+2 split; Nightmare: Dreamless provides Havoc DMG Bonus buffs that align with the Havoc Eclipse set's bonuses; Wutheringwaves-builds rates this as *"good alternative when using a 5-piece Havoc Eclipse set; best option within that set but generally suboptimal compared to Nightmare: Hecate"*

**Echo Main Stats Priority**
- 4-Cost Echo: CRIT Rate (aim for ~80%+ total; **do not exceed 100% CRIT Rate** due to bonuses from Lethean Elegy signature and Dream of the Lost set — per wutheringwaves-builds)
- 3-Cost Echoes (×2): CRIT DMG + Havoc DMG Bonus or ATK%
- 1-Cost Echoes: ATK%

**Sub-Stat Priority:** CRIT Rate (to cap) > CRIT DMG > Havoc DMG Bonus > ATK% > Resonance Skill DMG Bonus. Note: The Aftersound mechanic rewards building high CRIT DMG through gear in addition to the CRIT DMG provided by Aftersound stacks; the two stack multiplicatively. Avoid going over 100% CRIT Rate.

## Phrolova: Recommended Weapons

**Best-in-Slot — Lethean Elegy (5-Star Signature Rectifier)**
- Purpose-built for Phrolova with direct synergy on her two primary damage categories
- **Stat:** ATK% (high base) — verify exact bonus value with Fandom Wiki
- **Passive:**
  - **+12% ATK** (unconditional)
  - Within 12 seconds after dealing **Echo Skill DMG**: gain **+32% Resonance Skill DMG Bonus** and **+32% Echo Skill DMG Amplification**; **+8% DEF Ignore** (applies when dealing damage after the trigger window)
  - The DEF Ignore penetration stacks multiplicatively with all amplifications; particularly impactful for Phrolova because both her Maestro window attacks (Hecate's Echo Skill classified strikes) and her Reincarnate finishers (Resonance Skill classified) receive both the Echo Skill and Resonance Skill bonuses within the same active window
- Gamingpromax: *"mandatory for T0.5"*; the signature weapon enables the highest single-rotation damage output by maintaining both DMG bonuses simultaneously throughout her active window

**Best Standard 5-Star / Alternative — Stringmaster (5-Star, Standard Pool)**
- Same weapon as used by multiple caster DPS in the game; provides CRIT DMG and a meaningful passive for Echo Skill or Resonance Skill emphasis
- Gamingpromax lists this as the *"fallback"* when Lethean Elegy is unavailable; substantial gap in ceiling vs. signature but fully functional
- Wutheringlab notes it as the recommended non-signature 5-star option

**Battle Pass Alternative**
- Verify current Battle Pass Rectifier options with Fandom Wiki for V2.8 and beyond; a high-refinement Battle Pass weapon can approach 4-star ceilings

**F2P Alternative**
- Verify craftable Rectifiers available in the Rinascita crafting system; a Spectro or Havoc DMG Bonus Rectifier at high refinement is the recommended F2P starting point

## Phrolova: Best Teams

**Premier Team — Phrolova / Cantarella / Roccia**
- The definitive optimal team per Prydwen, Game8, LDShop, and Gamingpromax; all mechanics align at every interaction point
- **Phrolova (Maestro/Main DPS):** Summons Hecate off-field; Hecate fires Enhanced Attacks on every Echo Skill by Cantarella and Roccia; the Outro delivers +20% Havoc Amplification + 25% Heavy Attack Amplification to the incoming character
- **Cantarella (Sub-DPS / Echo Skill caster):** Cantarella's playstyle involves frequent Echo Skill activations; every one fires an Enhanced Attack – Hecate during Phrolova's off-field window; **Cantarella's Outro delivers +Havoc DMG and +Resonance Skill DMG Amplification to Phrolova** on re-entry; Hecate's attacks do NOT remove Cantarella's Hazy Dream debuff, preserving the combo enabler; Cantarella heals the team, removing the need for a dedicated healer
- **Roccia (Sub-DPS / Buffer):** Generates Concerto Energy quickly via plunge attacks; provides party-wide ATK buff via Liberation; Echo Skills trigger Hecate; receives Phrolova's Outro dual buffs (Havoc + Heavy Attack) on entry, which directly amplify her plunging damage; groups enemies for Phrolova's AoE attacks
- *Full team rotation (per game8 and genshin-builds Phrolova guide):*
  1. Start with Phrolova; build 6 Volatile Notes via Basic Attack Stage 3 and Resonance Skill combos
  2. In Compose state: cast Scarlet Coda → Resolving Chord activates
  3. Cast Resonance Liberation → Maestro + Hecate summoned (24s window starts)
  4. Outro to Roccia with Phrolova still in Maestro (Hecate fires 2 additional Enhanced Attacks on Outro)
  5. Roccia performs plunge rotation; generates Concerto; casts Liberation for team ATK buff; switches to Cantarella
  6. Cantarella casts Resonance Skill and Liberation; enters Mirage; uses combos; preserves Hazy Dream state
  7. Cantarella Outro to Phrolova; Phrolova enters with Cantarella's Havoc + Resonance Skill buffs active
  8. If Maestro is still active: enter via Suite of Immortality (not Intro Skill) for the ~596% ATK Resonance Skill hit
  9. Repeat; Echo Skill activations from Roccia and Cantarella throughout charge Hecate's trigger count

**Alternative — Phrolova / Qiuyuan / Cantarella**
- Used when Roccia is unavailable; replaces Roccia's Heavy Attack buffing with Qiuyuan's Echo Skill DMG support
- **Qiuyuan:** His Bamboo's Shade (+30% Echo Skill DMG Bonus) applies to Phrolova's active-character window but **not** to Hecate's off-field attacks (per the Qiuyuan kit documentation: *"Bamboo's Shade only applies to the active on-field character"*); however, his Liberation CRIT DMG buff (up to +30%) and Outro (+50% Echo Skill DMG Amplification for 14s) do benefit Phrolova; the Echo Skill DMG synergy is real but partially hampered by Bamboo's Shade's on-field restriction
- **Cantarella:** Same role as in the Roccia team; provides Hazy Dream, Echo Skills for Hecate, healing, and Outro buffs for Phrolova
- Lootbar.gg and the genshin-builds guide both document this rotation as a viable alternative that maximizes the Havoc attribute and Echo Skill usage

**Hypercarry with Support — Phrolova / Cantarella / Shorekeeper**
- Replaces Roccia with Shorekeeper for survivability-first content
- **Shorekeeper:** Universal healer; CRIT Rate + CRIT DMG Stellarealm buff for Phrolova and Cantarella; the CRIT buffs are multiplicatively valuable given Phrolova's Aftersound CRIT DMG stacking
- Prydwen notes this as the hypercarry setup where Phrolova is the main damage source supported specifically by Cantarella's Echo Skill casts and Shorekeeper's buffs and healing

## Phrolova: Rotation Guide

**Standard Rotation (Cantarella + Roccia team)**
1. **On Phrolova (Note building):** Intro Skill → Basic Attack chain (Stage 1 → 2 → 3, gaining Volatile Note – Strings) → Resonance Skill (Reincarnate) → Movement of Fate and Finality OR Murmurs in a Haunting Dream (gaining second Note) → repeat Basic Attack Stage 3 + Reincarnate finisher combos until 6 Volatile Notes
2. **Scarlet Coda** (Heavy Attack at 6 Notes in Compose state): Havoc Resonance Skill DMG; Aftersound-scaled multiplier; Resolving Chord activates
3. **Resonance Liberation: Waltz of Forsaken Depths**: exits Resolving Chord; Maestro begins (24s); +120% ATK; Hecate summoned; Liberation DMG hit
4. **Outro to Roccia** (while in Maestro): Unfinished Piece delivers +20% Havoc + 25% Heavy Attack Amplification; Hecate casts 2 additional Enhanced Attacks; **Maestro continues off-field**
5. **Roccia window**: plunge attack rotation; Liberation for team ATK buff; Echo Skills trigger Hecate Enhanced Attacks; Outro to Cantarella
6. **Cantarella window**: Resonance Skill + Liberation; Mirage combos; Hazy Dream maintained (Hecate does not remove it); Echo Skills trigger Hecate Enhanced Attacks; Outro to Phrolova
7. **Re-enter Phrolova** (while Maestro still active): **Suite of Immortality** (not standard Intro Skill) for ~596% ATK Resonance Skill hit + Stagnation; Maestro ends on return; Curtain Call fires automatically
8. Rebuild Notes for next 25s Compose cycle

**Key Rotation Rules**
- The **25-second Compose cooldown** defines the minimum rotation cycle length; design the full team rotation to complete within 24 seconds (Maestro duration) so Phrolova can re-enter via Suite of Immortality
- **Never use Liberation in Curtain Call mode** (Resolving Chord + Liberation hold) unless deliberately skipping a Maestro window for rotation timing; Curtain Call removes all Volatile Notes without granting Maestro
- **Outro while still in Maestro** is mandatory for the 2 extra Hecate Enhanced Attacks from the Outro Maestro trigger
- **Maximize Echo Skill activations** from teammates during the off-field Maestro window; each teammate Echo Skill fires one Hecate Enhanced Attack (up to 10 total); prioritize teammates with multiple Echo Skill-triggering moves
- **Do not exceed 100% CRIT Rate** — beyond 100%, CRIT Rate is wasted; build exactly to cap with Dream of the Lost, Lethean Elegy, and gear sub-stats combined

## Phrolova: Sources

- Prydwen Institute — Phrolova build guide, Volatile Notes mechanics, Aftersound CRIT DMG detail: https://www.prydwen.gg/wuthering-waves/characters/phrolova/
- Wutheringlab — Phrolova build, Maestro rotation, note-type analysis: https://wutheringlab.com/character/phrolova-build/
- Game8 — Phrolova best builds, teams, skill priority, Compose state mechanic: https://game8.co/games/Wuthering-Waves/archives/524877
- LDShop — Phrolova complete build guide, S2 investment analysis: https://www.ldshop.gg/blog/guide/phrolova-build-wuthering-waves.html
- Gamingpromax — Phrolova detailed build guide (V2.5/V2.8 rerun), tier placement, sequence pull priority, full rotation: https://gamingpromax.com/wuwa-phrolova/
- Wuthering.gg — Phrolova kit descriptions, stat tables, Forte Circuit text: https://wuthering.gg/characters/phrolova
- Wuthering.wiki — Phrolova full skill data including multiplier tables and damage type classifications: https://wuthering.wiki/character_1608.html
- Lootbar.gg — Phrolova build guide (V2.8 rerun): https://lootbar.gg/blog/en/wuthering-waves-phrolova-build-guide.html
- Genshin-builds (WuWa) — Phrolova team rotation guides including Qiuyuan/Cantarella: https://genshin-builds.com/en/wuthering-waves/characters/phrolova
