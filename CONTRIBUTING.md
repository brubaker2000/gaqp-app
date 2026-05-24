# Contributing to the GAQP Standards Package

The GAQP Standards Package is maintained by the **Institute for Qualitative Standards (IQS)**. This document describes how to propose changes.

---

## What can be changed by community contribution

The schematic has two tiers with different change friction.

### Statutory layer — open for rapid addition
These can be updated at any time without a version bump:

- **Domain subtags** (`domain_modules.json`) — new subtag codes within an existing sector
- **tags_pipe values** (`tags_vocabulary.json`) — new values within an existing prefix (`func:`, `risk:`, `topic:`, `geo:`)
- **Sector crossref notes** (`sector_vocabulary.json`) — corrections to GICS/SIC/NAICS mapping notes

Statutory additions are reviewed and published quickly. GAQP is a living vocabulary. There is no mandatory waiting period. A Standards Committee member reviews your proposal and either accepts, modifies, or declines it. Accepted additions go into the next release, which may happen the same week.

### Constitutional layer — IQS-controlled only
These require a formal version increment and Standards Committee review:

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

3. IQS reviews and either accepts, modifies, or declines. No mandatory waiting period.
4. Accepted subtags are published in the next release.

### New tags_pipe value

1. Open an issue titled: `[TAG] prefix:Value — Label`
   - Example: `[TAG] func:DataEngineering — Data Engineering`
2. Include:
   - **Prefix** — must be one of: `func`, `risk`, `topic`, `geo`
   - **Proposed value** — PascalCase, no spaces
   - **Justification** — one sentence explaining the gap

### New sector

A new sector is a larger addition — it requires a new entry in `sector_vocabulary.json` and a populated dimension/subtag structure in `domain_modules.json`. Open an issue titled `[SECTOR] SectorCode — Sector Name` with:

- **Proposed sector code** — short, all caps
- **Proposed sector name** — plain English
- **Rationale** — why this sector is operationally distinct from existing sectors
- **Proposed dimensions** — the organizing categories within the sector (typically 8–15)
- **Sample subtags** — at least 20 proposed subtags to demonstrate coverage

New sectors are IQS-reviewed and either accepted, modified, or declined. If accepted, IQS will work with the proposer to complete the full subtag taxonomy before publication.

---

## What we do not accept

- New claim types — the 25-type register is constitutional
- New admission tests — the seven tests are constitutional
- New schema fields — the 29-field schema is constitutional
- New prefixes for tags_pipe — the four prefixes (func, risk, topic, geo) are constitutional
- Proprietary deconstruction profiles or instruction sets — those are operator IP and do not belong in this repository

---

## Constitutional change proposals

If you believe a constitutional element needs to change, open an issue titled `[CONSTITUTIONAL] ...` with a full written rationale. Constitutional changes are made by the IQS Standards Committee. Registered implementers receive 14 days notice before any constitutional change takes effect.

GAQP governs language synthesis and qualitative knowledge classification. It does not touch financial transactions, safety systems, or any domain where a bad change creates risk to persons or institutions. Constitutional change proposals are evaluated on technical merit, not subjected to extended comment periods. If the argument is sound, the change happens.
