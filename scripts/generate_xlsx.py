#!/usr/bin/env python3
"""
Generate GAQP Standards Package xlsx distribution artifact from JSON source files.
JSON is the source of truth. This script produces the xlsx output.

Usage:
    pip install -r requirements.txt
    python generate_xlsx.py [--version v0.1-working] [--out ./dist]
"""

import argparse
import hashlib
import json
import os
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    raise SystemExit("Missing dependency: pip install openpyxl")


STANDARDS_ROOT = Path(__file__).parent.parent / "standards"

HEADER_FILL = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
SUBHEADER_FILL = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
SUBHEADER_FONT = Font(color="FFFFFF", bold=True)
NOTE_FILL = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ALT_FILL = PatternFill(start_color="EEF3FF", end_color="EEF3FF", fill_type="solid")
THIN_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)


def load_json(version_dir: Path, filename: str) -> dict:
    path = version_dir / filename
    with open(path) as f:
        return json.load(f)


def style_header(cell, sub=False):
    cell.font = SUBHEADER_FONT if sub else HEADER_FONT
    cell.fill = SUBHEADER_FILL if sub else HEADER_FILL
    cell.alignment = Alignment(wrap_text=True, vertical="top")
    cell.border = THIN_BORDER


def style_cell(cell, alt=False):
    cell.fill = ALT_FILL if alt else PatternFill()
    cell.alignment = Alignment(wrap_text=True, vertical="top")
    cell.border = THIN_BORDER


def set_col_widths(ws, widths: list[int]):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def write_claim_types(wb, data: dict):
    ws = wb.create_sheet("Claim Types")
    ws.freeze_panes = "A2"

    headers = ["#", "claim_type", "Operational Definition"]
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=1, column=col, value=h)
        style_header(c)

    for i, ct in enumerate(data["claim_types"]):
        row = i + 2
        alt = i % 2 == 1
        for col, val in enumerate([ct["id"], ct["claim_type"], ct["definition"]], 1):
            c = ws.cell(row=row, column=col, value=val)
            style_cell(c, alt)

    note_row = len(data["claim_types"]) + 3
    ws.cell(row=note_row, column=1, value="Register Status:").font = Font(bold=True)
    ws.cell(row=note_row, column=2, value=data["register_status"].upper())
    ws.cell(row=note_row + 1, column=1, value="Note:").font = Font(bold=True)
    c = ws.cell(row=note_row + 1, column=2, value=data["register_note"])
    c.fill = NOTE_FILL
    c.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f"B{note_row + 1}:C{note_row + 1}")

    forbidden_start = note_row + 3
    ws.cell(row=forbidden_start, column=1, value="FORBIDDEN LABELS").font = Font(bold=True, color="C00000")
    ws.cell(row=forbidden_start + 1, column=1, value="Forbidden Label")
    ws.cell(row=forbidden_start + 1, column=2, value="Remap To")
    ws.cell(row=forbidden_start + 1, column=3, value="Note")
    style_header(ws.cell(row=forbidden_start + 1, column=1), sub=True)
    style_header(ws.cell(row=forbidden_start + 1, column=2), sub=True)
    style_header(ws.cell(row=forbidden_start + 1, column=3), sub=True)

    for i, fl in enumerate(data["forbidden_labels"]):
        r = forbidden_start + 2 + i
        ws.cell(row=r, column=1, value=fl["forbidden"])
        ws.cell(row=r, column=2, value=" / ".join(fl["remap_to"]))
        ws.cell(row=r, column=3, value=fl.get("note", ""))

    set_col_widths(ws, [6, 30, 70])


def write_admission_tests(wb, data: dict):
    ws = wb.create_sheet("Admission Tests")
    ws.freeze_panes = "A2"

    headers = ["#", "Test", "Pass Condition"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, t in enumerate(data["tests"]):
        row = i + 2
        alt = i % 2 == 1
        for col, val in enumerate([t["id"], t["name"], t["pass_condition"]], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    note_row = len(data["tests"]) + 3
    ws.cell(row=note_row, column=1, value="Operational Discipline:").font = Font(bold=True)
    c = ws.cell(row=note_row, column=2, value=data["operational_discipline"])
    c.fill = NOTE_FILL
    c.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f"B{note_row}:C{note_row}")

    set_col_widths(ws, [6, 25, 80])


def write_confidence_ladder(wb, data: dict):
    ws = wb.create_sheet("Confidence Ladder")
    ws.freeze_panes = "A2"

    headers = ["Level", "Score", "Condition"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, lvl in enumerate(data["levels"]):
        row = i + 2
        alt = i % 2 == 1
        score = lvl["score"] if lvl["score"] is not None else "frozen"
        for col, val in enumerate([lvl["level"], score, lvl["condition"]], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    note_row = len(data["levels"]) + 3
    for label, key in [("Promotion Rule:", "promotion_rule"), ("Independence:", "independence_definition")]:
        ws.cell(row=note_row, column=1, value=label).font = Font(bold=True)
        c = ws.cell(row=note_row, column=2, value=data[key])
        c.fill = NOTE_FILL
        c.alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"B{note_row}:C{note_row}")
        note_row += 1

    set_col_widths(ws, [18, 10, 75])


def write_metadata_schema(wb, data: dict):
    ws = wb.create_sheet("Metadata Schema")
    ws.freeze_panes = "A2"

    headers = ["Field", "Required", "Definition"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, f in enumerate(data["required_fields"]):
        row = i + 2
        alt = i % 2 == 1
        req = "Required" if f["required"] else "Optional"
        definition = f["definition"]
        if "enum" in f:
            definition += f" [enum: {', '.join(f['enum'])}]"
        for col, val in enumerate([f["field"], req, definition], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    add_row = len(data["required_fields"]) + 3
    ws.cell(row=add_row, column=1, value="ADDITIONAL FIELDS (37-column reference)").font = Font(bold=True)
    add_row += 1
    ws.cell(row=add_row, column=1, value=", ".join(data["additional_fields"]))
    ws.cell(row=add_row, column=1).alignment = Alignment(wrap_text=True)
    ws.merge_cells(f"A{add_row}:C{add_row}")
    ws.row_dimensions[add_row].height = 60

    set_col_widths(ws, [35, 12, 75])


def write_source_anchor_schema(wb, data: dict):
    ws = wb.create_sheet("Source Anchor Schema")
    ws.freeze_panes = "A2"

    headers = ["Field", "Notes"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, f in enumerate(data["fields"]):
        row = i + 2
        alt = i % 2 == 1
        notes = f["notes"]
        if "enum" in f:
            notes += f" [enum: {', '.join(f['enum'])}]"
        for col, val in enumerate([f["field"], notes], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    set_col_widths(ws, [25, 70])


def write_conformance_levels(wb, data: dict):
    ws = wb.create_sheet("Conformance Levels")
    ws.freeze_panes = "A2"

    headers = ["Level", "Name", "Capability"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, lvl in enumerate(data["levels"]):
        row = i + 2
        alt = i % 2 == 1
        for col, val in enumerate([lvl["level"], lvl["name"], lvl["capability"]], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    set_col_widths(ws, [10, 28, 70])


def write_sector_vocabulary(wb, data: dict):
    ws = wb.create_sheet("Sector Vocabulary")
    ws.freeze_panes = "A2"

    style_header(ws.cell(row=1, column=1, value="primary_sector"))
    style_header(ws.cell(row=1, column=2, value="Notes"))

    for i, sector in enumerate(sorted(data["sectors"])):
        row = i + 2
        alt = i % 2 == 1
        style_cell(ws.cell(row=row, column=1, value=sector), alt)
        note = "Fallback — use when no specific sector applies" if sector == data["fallback"] else ""
        style_cell(ws.cell(row=row, column=2, value=note), alt)

    set_col_widths(ws, [35, 45])


def write_principles(wb, data: dict):
    ws = wb.create_sheet("Principles")
    ws.freeze_panes = "A2"

    headers = ["#", "Principle", "Requirement"]
    for col, h in enumerate(headers, 1):
        style_header(ws.cell(row=1, column=col, value=h))

    for i, p in enumerate(data["principles"]):
        row = i + 2
        alt = i % 2 == 1
        for col, val in enumerate([p["id"], p["name"], p["requirement"]], 1):
            style_cell(ws.cell(row=row, column=col, value=val), alt)

    set_col_widths(ws, [6, 35, 75])


def write_cover(wb, manifest: dict):
    ws = wb.create_sheet("Cover", 0)

    title_cell = ws.cell(row=1, column=1, value=manifest["standard_name"])
    title_cell.font = Font(size=18, bold=True, color="1F3864")
    ws.merge_cells("A1:C1")

    rows = [
        ("Abbreviation", manifest["standard_abbreviation"]),
        ("Standards Body", manifest["standards_body"]),
        ("Package Version", manifest["version"]),
        ("Status", manifest["status"].upper()),
        ("Release Date", manifest["release_date"] or "TBD"),
        ("Checksum (SHA-256)", manifest["checksum_sha256"] or "TBD — set at version freeze"),
        ("Description", manifest["description"]),
    ]

    for i, (label, value) in enumerate(rows, 3):
        ws.cell(row=i, column=1, value=label).font = Font(bold=True)
        c = ws.cell(row=i, column=2, value=value)
        c.alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"B{i}:C{i}")

    for label, value in manifest["notes"].items():
        i += 1
        ws.cell(row=i, column=1, value=f"Note — {label}").font = Font(bold=True, color="7F6000")
        c = ws.cell(row=i, column=2, value=value)
        c.fill = NOTE_FILL
        c.alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"B{i}:C{i}")

    set_col_widths(ws, [28, 55, 20])


def compute_package_checksum(version_dir: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(version_dir.glob("*.json")):
        if f.name == "manifest.json":
            continue
        h.update(f.read_bytes())
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Generate GAQP Standards Package xlsx from JSON source.")
    parser.add_argument("--version", default="v0.1-working", help="Standards package version directory name")
    parser.add_argument("--out", default="./dist", help="Output directory for xlsx file")
    args = parser.parse_args()

    version_dir = STANDARDS_ROOT / args.version
    if not version_dir.exists():
        raise SystemExit(f"Version directory not found: {version_dir}")

    manifest = load_json(version_dir, "manifest.json")
    claim_types = load_json(version_dir, "claim_types.json")
    admission_tests = load_json(version_dir, "admission_tests.json")
    confidence_ladder = load_json(version_dir, "confidence_ladder.json")
    metadata_schema = load_json(version_dir, "metadata_schema.json")
    source_anchor = load_json(version_dir, "source_anchor_schema.json")
    conformance = load_json(version_dir, "conformance_levels.json")
    sectors = load_json(version_dir, "sector_vocabulary.json")
    principles = load_json(version_dir, "principles.json")

    checksum = compute_package_checksum(version_dir)
    manifest["checksum_sha256"] = checksum

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    write_cover(wb, manifest)
    write_claim_types(wb, claim_types)
    write_admission_tests(wb, admission_tests)
    write_confidence_ladder(wb, confidence_ladder)
    write_metadata_schema(wb, metadata_schema)
    write_source_anchor_schema(wb, source_anchor)
    write_conformance_levels(wb, conformance)
    write_sector_vocabulary(wb, sectors)
    write_principles(wb, principles)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    version_slug = args.version.replace("/", "-")
    out_path = out_dir / f"GAQP_Standards_Package_{version_slug}.xlsx"
    wb.save(out_path)

    print(f"Generated: {out_path}")
    print(f"Package checksum (SHA-256): {checksum}")


if __name__ == "__main__":
    main()
