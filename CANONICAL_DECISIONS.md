# GAQP Canonical Decisions Record
**Version:** 1.0  
**Status:** Authoritative — repo ground truth  
**Purpose:** This file is the single source of truth for all settled GAQP decisions. It is the governing context artifact for this repository. Every implementation decision that touches GAQP must trace back here. When this file and any other document conflict, this file wins.

This is the IQS/GAQP repository. It defines and governs the standard. Downstream applications that implement the standard — including any named reconstructor or deconstructor product — are out of scope here. They are consumers of this repo, not contributors to it.

---

## 1. Identity and Naming — Settled

| Decision | Canonical Answer |
|---|---|
| Full standard name | Generally Accepted Qualitative Principles |
| Abbreviation | GAQP |
| Standards body name | Institute for Qualitative Standards |
| Standards body abbreviation | IQS |
| "Synthesis" variant of IQS name | Retired. Legacy drift from prior ideation sessions. Do not use. |
| GAQP's relationship to downstream software | GAQP is the parent standard. Any downstream application is a consumer and implementer. The standard stands above any single implementation. |
| Who owns GAQP | IQS. No downstream application owns or controls the standard. |

---

## 2. Three-Entity Hierarchy — Settled

These three entities are not interchangeable. They serve different audiences and must never be conflated.

| Entity | Role |
|---|---|
| **IQS** | Institute for Qualitative Standards. Governs GAQP, publishes releases, adjudicates changes, certifies conformance. Does not need to own every tool to own the standard. |
| **GAQP** | The standard itself. The principles, taxonomy, schema, admission tests, governance rules, and conformance levels. |
| **Standards Package** | The downloadable, versioned artifact bundle. Current machine-readable and human-readable rulebook until replaced by a later versioned package. |

**Prime rule for all compliant implementations:** Build as a GAQP-compliant consumer of the Standards Package. Do not hard-code private logic where the Standards Package defines the governing rule. When the package changes, runtime behavior updates — not core application logic.

---

## 3. The Canonical GAQP Definition — Settled

GAQP governs claims extracted from language. It is not a summarization tool, not an NLP system, and not a prompt library. It is a standards layer that sits above any specific AI implementation, defining the rules by which qualitative material is decomposed, classified, stored, retrieved, and recombined.

**Core axioms — governing doctrine:**

- The document is the vessel. The governed claim is the first usable unit of qualitative intelligence.
- Not every sentence is a nugget. A nugget is a sentence that survives governance.
- AI did not solve the qualitative knowledge problem. It scaled it.
- An ungoverned LLM is a liability dressed as an asset.
- Deconstruction creates the atoms. Reconstruction creates the value. The standard makes the ecosystem interoperable.
- GAQP Core is constitutional. Domain modules are statutory.
- Private prompts do not create markets. Shared standards do.
- GAQP defines the tables. Software turns the tables into value.
- Source locality is sacred.
- Stale intelligence in a governed corpus is worse than no intelligence — it is confidently wrong.
- One read is an opinion. Three independent reads converging is a finding.
- Keyword search finds words. GAQP search finds significance.
- Dot intel does not replace the document. It releases the intelligence trapped inside it.
- IQS does not need to own every tool to own the standard.

**The Three Laws of GAQP:**
1. Ungoverned AI predicts. Governed AI decides.
2. Decision quality is bounded by the granularity of the units being analyzed.
3. The ultimate value of governed AI is not speed — it is the perception of patterns previously invisible to human cognition.

---

## 4. The Three Functions — Settled

These three functions are categorically distinct. They must never be conflated.

| Function | Definition |
|---|---|
| **Harvesting** | Operator-driven preservation. An operator selects and saves text because they perceive value in it. Not governed by GAQP extraction rules. Harvested content must not be treated as GAQP-generated claims. |
| **Deconstruction** | GAQP-driven extraction. Systematic, governed by the Standards Package. Produces source-local atomic claims that pass all seven admission tests. |
| **Reconstruction** | App-driven synthesis. Consumes GAQP-compliant outputs and generates governed synthesis — conclusions, recommendations, risk maps, decision artifacts. |

---

## 5. The Atomic Nugget — Settled

An atomic nugget is a governed claim: the smallest durable unit of qualitative reasoning that can:
- Stand alone outside its source with full retained meaning
- Be classified by one of the 25 canonical claim types
- Be traced to a precise source location
- Be disputed or corroborated by independent sources
- Be tagged and audited under the GAQP schema
- Remain useful beyond the moment of extraction
- Be composed with other claims into larger reasoning structures

**Compression ratio:** Approximately 44:1 noise-to-signal across domains. Range: ~32:1 (private equity) to ~84:1 (technical documentation). Treat as observed working ratio pending formal validation — not a permanent empirical law.

---

## 6. The Seven Admission Tests — Settled

Applied to every candidate claim. A candidate that fails is rejected or flagged needs_review.

| # | Test | Pass Condition |
|---|---|---|
| 1 | Standalone | Retains full meaning outside its source paragraph without surrounding context |
| 2 | Disputability | A serious person can agree, challenge, or qualify it — genuinely contentful |
| 3 | Governance | Can be tagged, sourced, scoped, and audited under the GAQP schema |
| 4 | Activation | A system can determine when and where this claim matters |
| 5 | Durability | Remains useful beyond the moment of utterance |
| 6 | Composability | Can combine with other governed claims into larger judgment structures |
| 7 | Non-Triviality | Carries strategic, interpretive, factual, operational, or diagnostic weight |

**Operational discipline:** Be generous at candidate-identification. Be strict at admission. Optimize for governed admissibility, source fidelity, and boundary discipline — not claim volume.

---

## 7. The 25-Type Closed Claim Register — Settled

**The register is closed.** No implementation may create, infer, rename, abbreviate, pluralize, or substitute claim types. Every admitted claim maps to exactly one of these 25 types. Older 13-type and 19-type registers are retired version history — do not reference them.

| # | claim_type | Operational Definition |
|---|---|---|
| 1 | Axiom | Foundational assertion treated as a first principle within the source's own logic |
| 2 | Definition | A source-local explanation of what a term, category, process, or concept means |
| 3 | Ontological Assertion | A claim that something exists, has a particular nature, or belongs to a stated category |
| 4 | Principle | A general rule, standard, or governing idea that guides judgment or action |
| 5 | Doctrine | A formalized or institutionalized operating belief, policy logic, or governing position |
| 6 | Heuristic | A practical rule of thumb that helps make decisions under uncertainty |
| 7 | Best Practice | A recommended method, discipline, or operational pattern presented as preferable |
| 8 | Tendency | A recurring pattern, propensity, or direction of movement broader than one event |
| 9 | Observation | A source-supported noted fact, condition, or state of affairs without required causal interpretation |
| 10 | Event | A discrete occurrence, action, milestone, transaction, or incident anchored to a moment or sequence |
| 11 | Institutional Precedent | A prior institutional action, decision, practice, or pattern used as a reference point |
| 12 | Constraint | A limitation, boundary, dependency, rule, or operating condition that limits action |
| 13 | Threshold Condition | A minimum condition, trigger, breakpoint, or gating criterion that changes eligibility, status, or action |
| 14 | Objective | A desired end state, goal, target, mandate, or outcome sought by an actor or institution |
| 15 | Tradeoff | A tension or exchange in which pursuing one value or option burdens another |
| 16 | Causal Claim | An assertion that one factor produces, drives, prevents, enables, worsens, or improves another |
| 17 | Declaration of Value | A claim about importance, preference, worth, priority, or what should be valued |
| 18 | Diagnostic Signal | An indicator that suggests an underlying condition, risk, opportunity, weakness, or pattern |
| 19 | Stakeholder Complaint Claim | A complaint, objection, grievance, pain point, or dissatisfaction expressed by a stakeholder |
| 20 | Strength | A favorable internal attribute, capability, position, resource, or advantage |
| 21 | Weakness | An unfavorable internal deficit, vulnerability, limitation, gap, or underperformance |
| 22 | Opportunity | An external or situational upside, opening, favorable condition, or exploitable possibility |
| 23 | Threat | An external or situational downside, adverse force, risk, or harmful development |
| 24 | Asset | A resource, relationship, capability, right, dataset, or item with reusable value |
| 25 | Liability | An obligation, exposure, burden, dependency, or source of downside value |

**Forbidden labels — remap, never admit as claim types:**

| Forbidden Label | Remap To |
|---|---|
| Requirement | Constraint / Threshold Condition / Best Practice |
| Caution | Threat / Weakness / Constraint / Diagnostic Signal |
| Data Point | Observation / Event |
| Trend | Tendency |
| Capability | Strength / Asset / Ontological Assertion |
| Problem | Weakness / Threat / Stakeholder Complaint Claim |
| Risk | Threat / Diagnostic Signal / Constraint |
| Finding | Observation / Causal Claim (reconstruction artifact only) |
| Pattern | Tendency / Observation (reconstruction artifact only) |

---

## 8. The Confidence Ladder — Settled

Confidence advances through independent corroboration only. Same-source or same-tenant repetition does not promote. Structural elevation requires human operator action — never automated.

| Level | Score | Condition |
|---|---|---|
| seed | 0.50 | Extracted from one originating source. No independent corroboration yet. |
| single_source | 0.65 | One credible independent source beyond the origin. |
| developing | 0.72 | Two independent corroborating sources beyond the origin. |
| corroborated | 0.91 | Three or more independent corroborating sources beyond the origin. |
| structural | 1.00 | Operator elevation only. Never automated. |
| disputed | — | Active unresolved contradiction. Score frozen. Promotion blocked. |

**Independence definition:** A unique (tenant_id, actor_id) pair. The originating source is admission, not corroboration. The same actor corroborating a claim twice counts once.

---

## 9. Required Metadata Schema — Settled

Every GAQP-compliant claim record must carry these fields. A claim missing any required field is not GAQP-compliant.

| Field | Required | Definition |
|---|---|---|
| claim_id | Required | Unique record identifier |
| claim_type | Required | One of the exact 25 canonical types. Closed register. No substitution. |
| claim_text | Required | Exact wording of the governed claim as extracted from source |
| admission_status | Required | admitted / needs_review / rejected |
| confidence_level | Required | From the canonical confidence ladder |
| confidence_score | Required | Numeric score per ladder |
| source_document | Required | The document from which the claim was extracted |
| source_location | Required | Specific location within the source — page, paragraph, timestamp, section. A claim attributed only to a document without a location is not GAQP-compliant. |
| source_anchor_id | Required | Links to source anchor record |
| source_hash | Required | SHA-256 hash of source file. Enables stale detection. |
| inference_flag | Required | TRUE if claim involves any deconstructor inference beyond what source explicitly states. Inference must be labeled — never hidden. |
| tags_pipe | Required | Pipe-delimited controlled vocabulary tags |
| primary_sector | Required | Controlled sector vocabulary label |
| standards_package_version | Required | Version of GAQP Standards Package used to generate this record |
| extraction_method | Required | How the claim was produced |
| fingerprint | Required | SHA-256 deterministic identity hash |

**Full operational schema (37 columns per v0.4 reference implementation):**

Additional fields: source_quote, source_section, source_page, source_paragraph, primary_tag, secondary_sectors_pipe, sic_2, sic_4, entities_pipe, relationship_hints_pipe, validation_flags_pipe, review_notes, record_id, record_type, source_id, line_start, line_end, rejection_reason, reason_for_review, standalone_test, disputability_test, governance_test, activation_test, durability_test, composability_test, non_triviality_test, duplicate_check_status, quote_support_status, claim_type_validation_status, deconstructor_note.

---

## 10. Source Anchoring — Settled

Every admitted claim must point to the exact location in its source. The Source Anchoring schema has 20 fields.

| Field | Notes |
|---|---|
| anchor_id | Unique anchor identifier |
| source_id | Links back to source manifest |
| source_sha256 | SHA-256 hash — detects drift and staleness |
| page | Page number (PDF/print formats) |
| section | Heading or section label |
| paragraph | Paragraph number within section |
| sentence | Sentence number within paragraph |
| clause | Contract/legal clause reference |
| slide | Slide number (presentation sources) |
| speaker_turn | Speaker turn ID (transcripts) |
| timestamp | Audio/video timestamp |
| char_start | Character start offset |
| char_end | Character end offset |
| quote_hash | SHA-256 of anchored text span |
| anchor_confidence | high / medium / low |

---

## 11. The Source-Locality Rule — Settled, Non-Negotiable

A source-level .intel file must contain ONLY artifacts that originated from its corresponding source file.

**Forbidden inside a source .intel package:**
- Cross-document conclusions
- Corpus-wide findings
- Role-specific recommendations
- Strategy synthesized from multiple files
- Multi-source pattern conclusions
- Canonical claim families or theme maps derived from multiple sources
- Any synthesis, summary, implication, or next step

The .intel file records what one source contributed. The reconstructor determines what contributions mean together. This boundary is the architectural spine of GAQP's auditability guarantee.

---

## 12. The .intel Package Structure — Settled

14-section structure. Source file remains the canonical human-readable artifact. The .intel sidecar makes it searchable, auditable, and synthesizable.

| Section | Required | Contents |
|---|---|---|
| manifest | Required | Package identity, version, creator, generation date |
| source_binding | Required | Source file identity, name, type, hash |
| source_payload | Required | Native source content or binding pointer |
| schema | Required | Schema and standards versions used |
| anchors | Required | Source anchors for all admitted claims |
| claims | Required | Source-local atomic claims only |
| evidence | Recommended | Evidence records from the source |
| entities | Recommended | Named entities from the source |
| topics | Recommended | Topic tags and concepts |
| controlled_tags | Required | Preferred tags and synonym mappings |
| relationships | Recommended | Local relationships among source claims |
| validation | Required | Validation status and errors/warnings |
| security | Required | Permissions, classification, access policy |
| audit | Required | Generation log and processing metadata |

**Security rule:** A .intel sidecar may be more sensitive than its source document because it concentrates buried intelligence. Sidecars must inherit or exceed source file access controls. Never weaker.

---

## 13. Deconstruction Runtime — Settled

13-step sequence. Every step required.

1. Load current GAQP Standards Package. Verify checksum.
2. Ingest source material. Record all source metadata.
3. Segment source into anchorable units with location identifiers.
4. Identify candidate claims. Be generous at this stage.
5. Apply all seven admission tests. Be strict at this stage.
6. Assign claim type from the closed 25-type register. No substitution.
7. Assign controlled-vocabulary tags from core tag families and domain modules.
8. Attach source anchors including page, paragraph, section, SHA-256 hash.
9. Set inference_flag TRUE for any claim involving judgment beyond explicit source statements.
10. Validate output against schema. Reject records that fail required field checks.
11. Package output into source-local .intel file. No cross-document content.
12. Record standards package version on every generated artifact.
13. Output source-local artifacts only. No summaries, conclusions, or recommendations.

**Three canonical LLM deconstruction failure modes — test for these explicitly:**
1. Summarizing the corpus
2. Producing broad themes
3. Turning the corpus into recommendations

All three are reconstruction behaviors masquerading as deconstruction.

---

## 14. Reconstruction Runtime — Settled

9-step sequence. The only correct home for cross-document synthesis.

1. Load current GAQP Standards Package. Verify version and checksum.
2. Ingest .intel packages or claim records from governed corpus.
3. Query corpus for claims relevant to role, objective, and matter.
4. Group canonical families under shared meaning without losing provenance.
5. Detect and explicitly register contradictions and gaps. Never resolve silently.
6. Apply role context and objective weighting.
7. Generate synthesis artifacts preserving full source lineage.
8. Export conclusions with lineage, inference path, confidence basis, contradictions considered.
9. Record standards version on every synthesis artifact.

**Three-stage reconstruction sequence:**
- Stage 1: Atomic Nuggets — source-local governed claims from deconstruction
- Stage 2: Thought-Train Buckets — thematic groupings under shared subject or strategic question
- Stage 3: Governed Conclusions — cross-document synthesis under role and objective context

**Non-negotiable:** Synthesized conclusions must never masquerade as source claims. The lineage chain from source nugget to synthesis artifact must remain unbroken and auditable.

---

## 15. Governance Architecture — Settled

| Layer | Change Control |
|---|---|
| GAQP Core | Constitutional. Changes rarely, formally, annually, through high-friction process. |
| Domain Modules | Statutory. Change freely to accommodate industry-specific needs. |

**Constitutional elements (high-friction to change):**
Claim types, admission tests, tag families, source anchoring, provenance, .intel structure, validation doctrine, confidence ladder, source-locality rule, deconstruction/reconstruction boundary.

**Statutory elements (change freely):**
Domain vocabularies, industry-specific fields, sector labels, controlled synonym extensions, domain module rows.

---

## 16. Conformance Levels — Settled

Seven staged levels. Compliant tools adopt progressively.

| Level | Capability |
|---|---|
| L1 — Classification | Claims classified using the 25-type GAQP register |
| L2 — Provenance | Claims carry source anchors to specific source locations |
| L3 — Admissibility | Claims pass all seven admission tests before entering corpus |
| L4 — Confidence | Claims carry governed confidence levels based on corroboration |
| L5 — Sidecar-Enabled | Source documents carry .intel sidecar files |
| L6 — Cross-Document Corpus | Multiple .intel files queryable as a governed corpus |
| L7 — Activation | Claims surface at moment of decision in role-aware applications |

---

## 17. The Ten Core GAQP Principles — Settled

| # | Principle | Requirement |
|---|---|---|
| 1 | Materiality of Judgment | Preserve claims that can influence a decision, interpretation, or risk posture. Discard what cannot. |
| 2 | Source Traceability | Every accepted nugget must point back to its precise origin within the source document. |
| 3 | Consistency of Application | Apply the same rules uniformly across all claim processing, regardless of source or context. |
| 4 | Conservatism | Uncertain qualitative claims must be weighted cautiously unless independently corroborated. |
| 5 | Contextual Boundary Disclosure | Disclose when claims are activated in a context different from their source context. |
| 6 | Multi-Source Corroboration | Confidence advances through independent convergence, not repetition. Same-source repetition is not corroboration. |
| 7 | Judgment Independence | Synthesis must not be contaminated by the interests of any single source or actor. |
| 8 | Proportionality | The weight of a claim should be proportional to the strength of its evidence. |
| 9 | Revision Standard | GAQP outputs must remain updateable when better information arrives. |
| 10 | Scenario Completeness | Synthesis should account for alternative scenarios, not just the most likely. |

---

## 18. Controlled Sector Vocabulary — Settled

Use one of these proprietary labels for primary_sector. If none applies, use `General / Cross-Sector`.

Aerospace & Defense · Agribusiness · Automotive · Business Services · Chemicals · Communications · Construction & Engineering · Consumer · Distribution · Education · Energy · Environmental · Financial · Food & Beverage · Franchised Brands · Government Services · Healthcare · Industrials · Insurance · Life Sciences · Logistics & Transportation · Manufacturing · Materials · Media & Entertainment · Real Estate · Retail · Software · Technology · Telecom · Travel & Hospitality

---

## 19. Developer Integration Rules — Settled

- Do not hard-code claim types, admission tests, metadata fields, tag families, or validation rules in application logic. Load them from the Standards Package at runtime.
- Every generated artifact — claim record, .intel package, synthesis artifact — must record `standards_package_version`.
- When the Standards Package changes, runtime behavior updates without rewriting core application logic.
- Core tag families must not be mutated at the user or client level. Domain modules may extend under them.
- Domain modules must be stored in a single consolidated table, not one table per industry.
- A source .intel file that contains cross-document content fails validation. Reject it.
- Stale detection: if source SHA-256 hash changes, downstream .intel status must become stale or trigger regeneration.

**Suggested runtime interface methods for compliant implementations:**
`load_standards_package()`, `get_claim_types()`, `get_admission_tests()`, `get_tag_families()`, `get_metadata_fields()`, `get_source_anchor_fields()`, `get_domain_modules()`, `get_validation_rules()`, `get_vocabulary()`, `get_synonym_map()`

---

## 20. Open Items — Not Yet Settled

| Item | Status |
|---|---|
| License model | TBD. IQS must decide: open, licensed, certified, or hybrid. Recommendation: make Core easy to download; monetize tooling, certification, and domain modules. |
| IQS website domain | Placeholder: www.instituteforqs.org |
| Standards Package version freeze | Must reconcile schema before GAQP v1.0 public release. Current status: 0.1-working. |
| JSON/YAML runtime package | Future delivery format. V1 is xlsx. |
| Trademark and use marks | TBD. "GAQP-compliant" and "GAQP-enabled" marks should likely require conformance certification. |
| Checksum publication | To be generated after standards package freeze. |

---

*GAQP Canonical Decisions Record v1.0 — Produced from full corpus audit of 15+ source documents across all GAQP ideation sessions. This file supersedes all prior partial specifications on every settled item. This is the IQS/GAQP repository. The standard stands above any downstream application.*
