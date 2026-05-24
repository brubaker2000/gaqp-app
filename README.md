# GAQP — Generally Accepted Qualitative Principles

**Governed by:** Institute for Qualitative Standards (IQS)  
**Standards Package Version:** 0.1-working  
**Status:** Active Development — pre-release

---

## What This Repo Is

This is the IQS/GAQP repository. It defines and governs the GAQP standard. It is not a software application. It is the source of truth for the standard itself.

Downstream applications that implement GAQP — deconstructors, reconstructors, corpus tools — are consumers of this repo. They are not contributors to the standard.

**When this repo and any other document conflict, this repo wins.**

---

## What GAQP Is

GAQP governs claims extracted from language. It is not a summarization tool, not an NLP system, and not a prompt library. It is a standards layer that sits above any specific AI implementation, defining the rules by which qualitative material is decomposed, classified, stored, retrieved, and recombined.

**The Three Laws of GAQP:**
1. Ungoverned AI predicts. Governed AI decides.
2. Decision quality is bounded by the granularity of the units being analyzed.
3. The ultimate value of governed AI is not speed — it is the perception of patterns previously invisible to human cognition.

---

## The Three Functions

| Function | Definition |
|---|---|
| **Harvesting** | Operator-driven preservation. An operator selects and saves text because they perceive value in it. Not governed by GAQP extraction rules. |
| **Deconstruction** | GAQP-driven extraction. Systematic, governed by the Standards Package. Produces source-local atomic claims that pass all seven admission tests. |
| **Reconstruction** | App-driven synthesis. Consumes GAQP-compliant outputs and generates governed synthesis — conclusions, recommendations, risk maps, decision artifacts. |

---

## Repo Structure

```
/
├── CANONICAL_DECISIONS.md        # Authoritative settled decisions — repo ground truth
├── standards/
│   └── v0.1-working/
│       ├── manifest.json                # Package identity and file registry
│       ├── claim_types.json             # 25-type closed claim register
│       ├── admission_tests.json         # 7 admission tests
│       ├── confidence_ladder.json       # Confidence levels and scores
│       ├── metadata_schema.json         # Required claim record fields (37 columns)
│       ├── source_anchor_schema.json    # Source anchor fields (20 fields)
│       ├── intel_package_structure.json # .intel sidecar 14-section structure
│       ├── conformance_levels.json      # L1–L7 conformance ladder
│       ├── sector_vocabulary.json       # Controlled sector labels
│       ├── validation_rules.json        # Forbidden labels, remap table, rules
│       ├── principles.json              # 10 core GAQP principles
│       └── runtime_interface.json       # Suggested runtime interface methods
├── scripts/
│   ├── generate_xlsx.py          # Generates xlsx distribution artifact from JSON
│   └── requirements.txt
└── docs/
    └── intel_package_structure.md
```

---

## The Standards Package

The Standards Package is the downloadable, versioned artifact bundle that governs compliant implementations. It is the current machine-readable and human-readable rulebook until replaced by a later versioned package.

**Prime rule for all compliant implementations:** Build as a GAQP-compliant consumer of the Standards Package. Do not hard-code private logic where the Standards Package defines the governing rule. When the package changes, runtime behavior updates — not core application logic.

### Suggested Runtime Interface

Compliant implementations should expose these methods, loading from the Standards Package:

```
load_standards_package()
get_claim_types()
get_admission_tests()
get_tag_families()
get_metadata_fields()
get_source_anchor_fields()
get_domain_modules()
get_validation_rules()
get_vocabulary()
get_synonym_map()
```

---

## Governance

| Layer | Change Control |
|---|---|
| **GAQP Core** | Constitutional. Changes rarely, formally, annually, through high-friction process. |
| **Domain Modules** | Statutory. Change freely to accommodate industry-specific needs. |

**Constitutional elements:** Claim types, admission tests, tag families, source anchoring, provenance, .intel structure, validation doctrine, confidence ladder, source-locality rule, deconstruction/reconstruction boundary.

**Statutory elements:** Domain vocabularies, industry-specific fields, sector labels, controlled synonym extensions, domain module rows.

---

## Conformance Levels

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

*Institute for Qualitative Standards — www.instituteforqs.org (placeholder)*
