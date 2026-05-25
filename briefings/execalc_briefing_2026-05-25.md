# GAQP Standards Briefing — For Execalc Implementation Team
**From:** IQS Standards (via gaqp-app repo)
**Date:** 2026-05-25
**Re:** v0.2-working changes and proposed confidence modifier framework
**Action requested:** Review and reply with implementation impact assessment

---

## What this briefing is

This document summarizes the changes between the v0.1 GAQP Standards Package and the current v0.2-working state. The consolidated machine-readable artifact (`gaqp_standards_v02.json`) in this repo reflects all of these changes and is the canonical input for your build.

Please read this briefing and reply with your assessment of how each section affects the Execalc build — what needs to change, what's a no-op, what introduces complexity, and what questions you have.

---

## Change 1 — New sector: MIL (Military)

**What changed:** A 32nd sector has been added to the domain vocabulary. MIL covers military operational intelligence — doctrine, readiness, force posture, theater operations, logistics, and intelligence functions.

**Key stats:** 247 subtags across 15 dimensions.

**The one unusual thing:** MIL has a dimension called **GAQP Intelligence Functions** that doesn't exist in any other sector. It classifies the *type of document being deconstructed* — not the subject matter. Subtags include things like OPORD (operations order), SITREP_DOC (situation report), AAR (after action review), NDS_DOC (national defense strategy), CONGRESSIONAL (congressional testimony). This lets a corpus be queried by document type, not just subject.

**Tags vocabulary additions:** A number of new values were added to the four cross-cutting tag prefixes to support military use:
- `func:` — CommandControl, ForceReadiness, Intelligence, Logistics_MIL, AcquisitionMIL, TrainingExercises
- `risk:` — MissionFailure, ReadinessShortfall, IntelFailure, Escalation, AlliedCohesion, ForceSurvivability, StrategicSurprise, CBRNExposure, CyberCompromise, LethalAutonomy, SupplyChain_MIL
- `topic:` — MilitaryReadiness, NationalSecurity, Deterrence, Warfighting, Counterterrorism, WMD
- `geo:` — IndoPacific, NATO_Europe, SouthChinaSea, Taiwan_Strait, Korean_Peninsula, BlackSea, Arctic, Sahel, MiddleEast, PersianGulf, EasternEurope

**Implementation question for Execalc:** Does your sector/tag handling need updating to accommodate these additions, or does your current architecture pick them up from the vocabulary file dynamically?

---

## Change 2 — Confidence modifier framework (proposed, not yet constitutional)

**What changed:** A new document `confidence_modifiers.json` has been added to the standards package, marked `status: proposed`. This is the most architecturally significant addition in this cycle. Here is what it proposes.

### The core idea

The existing confidence ladder (seed → single_source → developing → corroborated → structural) measures one thing: how many independent sources have corroborated a claim. That's the right foundation. But it doesn't capture whether a highly-corroborated claim is *still applicable today*, or whether the sources corroborating it were actually independent, or whether the claim was directly stated versus synthesized from multiple passages.

The modifier framework proposes four additional dimensions that produce an `effective_confidence` by scaling the base ladder score:

```
effective_confidence = ladder_score × recency_factor × source_quality_factor × independence_factor × inferential_distance_factor
```

Each factor is a number between a floor value and 1.0. Unimplemented dimensions default to 1.0 (no effect). Operators can implement any subset.

### Dimension 1 — Recency (the most important one)

This is the dimension with real architectural implications.

Recency decay is a function of **two variables: claim type and domain** — not either one alone. The logic is:

- Some claim types are inherently timeless. An **Axiom** about human nature doesn't degrade with age. Whether it's correct is a corroboration question, not an age question.
- Some claim types are inherently world-state snapshots. An **Observation** about a company's market position, or a **Diagnostic Signal** about a unit's readiness — these were accurate at the moment they were made and become inapplicable as the world moves on.
- In between, every claim type has a default decay class with a reference half-life.

**The five decay classes, with claim type assignments:**

| Decay Class | Default Half-Life | Claim Types |
|-------------|-------------------|-------------|
| timeless | ∞ (no decay) | Axiom, Definition |
| slow_decay | ~20 years | Principle, Ontological Assertion, Declaration of Value |
| moderate_decay | ~5–10 years | Heuristic, Best Practice, Tendency, Tradeoff, Institutional Precedent |
| fast_decay | ~2–5 years | Doctrine, Constraint, Threshold Condition, Causal Claim, Stakeholder Complaint Claim |
| world_state | <2 years | Observation, Event, Diagnostic Signal, Objective, Strength, Weakness, Opportunity, Threat, Asset, Liability |

**Domain multipliers scale the half-life:**

| Rate | Multiplier | Example Sectors |
|------|------------|-----------------|
| aggressive | 0.4× | HC, MIL, FIN — evidence turns over fast |
| standard | 1.0× | Most business sectors |
| conservative | 2.5× | Law, humanities, physical infrastructure |

So a Causal Claim (fast_decay, ~3-year baseline) in HC (aggressive, 0.4×) has an effective half-life of about 14 months. A 10-year-old clinical causal claim may have a recency factor near 0.10.

**The formula:**
```
recency_factor = max(floor, 0.5 ^ (age_years / effective_half_life))
effective_half_life = base_half_life_for_decay_class × domain_multiplier
floor = 0.10 (default)
```

Timeless claims skip the formula entirely: recency_factor = 1.0 always.

### The analyst override

Here's the wrinkle. Claim types are the right starting point, but they don't handle within-type variance perfectly. Doctrine is the clearest example: "Surprise is the decisive force multiplier in offensive operations" and "Company-level UAS swarms will be employed in 4–8 platform packages for urban denial" are both Doctrine-typed claims. The first is as timeless as any Axiom. The second has a half-life measured in years at best.

The resolution is a proposed new field: `temporal_stability_override`.

- Type: string | null
- Allowed values: `timeless`, `slow`, `moderate`, `fast`, `world_state`, null
- null = use claim-type default
- Non-null = analyst's explicit override at extraction time

This field is proposed as **field 30** in the metadata schema (currently 29 fields, constitutionally frozen). Adding it requires a Standards Committee vote. It is **not yet adopted**. But we are flagging it now so you can design for it.

### Dimensions 2–4 (lighter touch)

- **Source quality** — A-D tier multiplier (1.0 → 0.65) based on source_type and source_credibility fields. Peer-reviewed RCT is Tier A. Journalistic account is Tier D.
- **Evidence independence** — Discount when apparent corroborators trace to the same upstream source (same dataset, same briefing). Analyst-applied, not automated.
- **Inferential distance** — Multiplier for how many interpretive steps separate the claim from the source text: direct (1.0) → derived (0.90) → synthesized (0.80) → inferred (0.65).

### Governance status

The modifier framework is `status: proposed`. It is included in `gaqp_standards_v02.json` so you can read and design against it. It is **not yet constitutional**. Operators may implement any or all of it now. When it is adopted, implementations that have already built against the spec will be conformant without rework.

---

## Change 3 — Extraction guidance added to Doctrine claim type

A clarifying `extraction_note` has been added to the Doctrine entry in `claim_types.json`. It is guidance, not a schema change. The note clarifies that claim type assignment is based on the *nature of the claim*, not the *type of document*. A field manual contains Axioms, Principles, Heuristics, and Doctrine — the analyst assigns the type based on how the individual claim functions, not what kind of document it came from. This matters because the recency model behaves very differently depending on which type is assigned.

No implementation change required. Worth knowing for any extraction prompt engineering you're doing.

---

## Change 4 — Legal and institutional formation

IQS is incorporating as a Delaware nonprofit (501(c)(3)). Mission Statement, Articles of Incorporation, and Bylaws are now in the `legal/` directory of this repo. Working drafts for attorney review, not yet filed.

This is not a standards change. It is background context: GAQP is now backed by a formal standards body with a constitutional/statutory governance structure that maps directly to the two-tier change architecture you already know.

No implementation impact.

---

## Summary of what's in gaqp_standards_v02.json now

The consolidated JSON attached to this briefing includes:
- All 3,827 domain subtags (247 MIL, 31 sectors with subtags)
- Updated tags_vocabulary with all military additions
- Full confidence_modifiers document (proposed)
- Updated claim_types with Doctrine extraction note
- All constitutional layer elements unchanged (claim types, admission tests, schema, ladder, conformance levels, principles)

---

## Requested response

Please review this briefing and reply with:

1. **MIL sector** — Does your current sector/tag ingestion handle the new vocabulary dynamically, or does anything need to be wired explicitly?

2. **Confidence modifiers** — How are you currently computing or storing confidence? Is there a `confidence_score` field in your data model today? What would it take to add `effective_confidence` as a derived/computed field alongside the base ladder score?

3. **Recency decay** — Do you have `source_date` captured on nuggets today? That's the required input for the recency factor calculation. If it's missing or sparse, that's the first dependency.

4. **temporal_stability_override (proposed field 30)** — How would this land in your schema? Is your metadata model flexible enough to accept a 30th field when it's adopted, or would that require a migration?

5. **Source quality tiers** — Are `source_type` and `source_credibility` populated in your current extractions? The Tier A–D source quality modifier depends on those fields.

6. **Anything else** — What questions do you have, what creates complexity, and what's a no-op from where you sit?

---

*Consolidated spec file: `gaqp_standards_v02.json` (this repo, `/docs/` and `/releases/`)*
*Standards source: `standards/v0.1-working/` (this repo)*
*Branch: `claude/cool-lamport-IrAUx` (pending merge to main)*
