# Contributing to the GAQP Standards Package

The GAQP Standards Package is maintained by the **Institute for Qualitative Standards (IQS)**. This document describes how to propose changes.

---

## What can be changed by community contribution

The schematic has two tiers with different change friction.

### Statutory layer — open for suggestions
These can be updated at any time without a version bump:

- **Domain subtags** (`domain_modules.json`) — new subtag codes within an existing sector
- **tags_pipe values** (`tags_vocabulary.json`) — new values within an existing prefix (`func:`, `risk:`, `topic:`, `geo:`)
- **Sector crossref notes** (`sector_vocabulary.json`) — corrections to GICS/SIC/NAICS mapping notes

### Constitutional layer — IQS-controlled only
These require a formal version increment and IQS review:

- Claim types (`claim_types.json`)
- Admission tests (`admission_tests.json`)
- Nugget schema fields (`metadata_schema.json`)
- Source anchor schema (`source_anchor_schema.json`)
- .intel file structure (`intel_file_spec.json`, `intel_package_structure.json`)
- Conformance levels (`conformance_levels.json`)
- Core principles (`principles.json`)

---

## How to propose a statutory addition

### New domain subtag

1. Open an issue titled: `[SUBTAG] SectorCode:SubtagCode — Name`
   - Example: `[SUBTAG] HC:GLP1 — GLP-1 Receptor Agonists`
2. Include:
   - **Sector code** — must be an existing sector in `sector_vocabulary.json`
   - **Proposed subtag code** — all caps, no spaces, no special characters
   - **Proposed subtag name** — plain English label
   - **Dimension** — which dimension grouping it belongs to within the sector
   - **Justification** — one sentence: why this concept appears frequently enough in real documents to warrant a controlled tag

3. IQS reviews and either accepts, modifies, or declines within 30 days.
4. Accepted subtags are added in the next scheduled schematic update.

### New tags_pipe value

1. Open an issue titled: `[TAG] prefix:Value — Label`
   - Example: `[TAG] func:DataEngineering — Data Engineering`
2. Include:
   - **Prefix** — must be one of: `func`, `risk`, `topic`, `geo`
   - **Proposed value** — PascalCase, no spaces
   - **Justification** — one sentence explaining the gap

---

## What we do not accept

- New claim types — the 25-type register is closed
- New admission tests — the seven tests are constitutional
- New schema fields — the 29-field schema is frozen at v1.0
- Proprietary deconstruction profiles or instruction sets — those are operator IP and do not belong in this repository

---

## Constitutional change proposals

If you believe a constitutional element needs to change, open an issue titled `[CONSTITUTIONAL] ...` with a full written rationale. IQS will review it as part of the next major version cycle. These are high-friction by design.
