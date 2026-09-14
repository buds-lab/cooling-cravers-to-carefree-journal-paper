#!/usr/bin/env python3
"""Render numbered citations into the clean 190 mm placeholder PDF.

Usage:
    python render_numbered_pdf.py \
        --map citation_numbers.csv \
        --out ../thermal_preference_elements_v15_190mm_1.pdf

The placeholder PDF is the clean PowerPoint export supplied with this builder.
Citation groups are read in element order from the CSV, sorted numerically within
each bracket, and inserted only where a [XX] placeholder occurs.
"""
import argparse
import csv
import re
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
DEFAULT_TEMPLATE = HERE / "thermal_preference_placeholder_XX_190mm.pdf"
DEFAULT_FONT = Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf")


def citation_groups(path):
    rows = list(csv.DictReader(open(path, newline="")))
    groups = []
    for row in rows:
        element = row["element"]
        number = row.get("number", "").strip()
        if not number:
            raise ValueError(f"Missing citation number for {row['bibtex_key']}")
        if not groups or groups[-1][0] != element:
            groups.append((element, []))
        groups[-1][1].append(int(number))
    return [(element, " [" + ",".join(map(str, sorted(numbers))) + "]")
            for element, numbers in groups]


def placeholder_spans(page):
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if re.fullmatch(r" \[XX(?:,XX)*\]", span["text"]):
                    spans.append(span)
    return spans


def render(template, mapping, output, fontfile):
    groups = citation_groups(mapping)
    doc = fitz.open(template)
    if doc.page_count != 1:
        raise ValueError("Expected a one-page figure template")
    page = doc[0]
    spans = placeholder_spans(page)
    if len(spans) != len(groups):
        raise ValueError(f"Found {len(spans)} placeholders for {len(groups)} citation groups")

    for span in spans:
        page.add_redact_annot(fitz.Rect(span["bbox"]), fill=False, cross_out=False)
    page.apply_redactions(images=0, graphics=0, text=0)

    fontfile = str(fontfile)
    for (element, text), span in zip(groups, spans):
        rect = fitz.Rect(span["bbox"])
        # Keep the original left edge and baseline but allow long numeric groups
        # to use the full remaining page width.
        rect.x1 = page.rect.x1 - 1
        rect.y1 += 1
        result = page.insert_textbox(
            rect,
            text,
            fontname="TimesNewRoman",
            fontfile=fontfile,
            fontsize=span["size"],
            color=(0, 0, 0),
            overlay=True,
        )
        if result < 0:
            raise ValueError(f"Citation did not fit for {element}: {text}")

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output, garbage=4, deflate=True)
    doc.close()
    return len(groups)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--map", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--font", type=Path, default=DEFAULT_FONT)
    args = parser.parse_args()
    count = render(args.template, args.map, args.out, args.font)
    print(f"rendered {count} numbered citation brackets -> {args.out}")
