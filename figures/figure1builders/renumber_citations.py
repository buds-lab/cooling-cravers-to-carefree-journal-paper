#!/usr/bin/env python3
"""
Swap the author-year tokens in the figure for numbered citations.

    # placeholder pass, for checking layout before the bibliography is fixed
    python renumber_citations.py --placeholder

    # once LaTeX has assigned numbers, fill in citation_numbers.csv and run
    python renumber_citations.py --map citation_numbers.csv

Reads figure_spec.json, writes figure_spec_numbered.json plus a .pptx.
Also emits citation_keys.csv listing every element, its tokens and its BibTeX
keys, which is the sheet you fill in with the numbers LaTeX assigns.

Numbers inside one bracket are sorted ascending, per Elsevier style.
"""
import argparse
import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "figure_spec.json")

# token -> BibTeX key, so the numbering sheet is unambiguous
KEYS = {
    "Otsu21": "Otsuka2021-ty", "Sawk01": "Sawka2001-sz", "Su23": "Su2023-tg",
    "Gill12": "Gillingham2012-nf", "Caba71": "Cabanac1971-mg", "Fran99": "Frank1999-ju",
    "Huan10": "Huang2010-hy", "Karj12": "Karjalainen2012-ag", "Zhan14": "Zhang2014-im",
    "John10": "Johnson2010-eh", "Have15": "Havenith2015-yn", "Gaes75": "Gaesser1975-jn",
    "Fang72": "Fanger1972-xq", "Tiku96": "Tikuisis1996-fd", "King12": "Kingma2012-lm",
    "Swam85": "Swaminathan1985-ca", "Fuka09": "Fukazawa2009-nx", "Hala14": "Halawa2014-ek",
    "Chin19": "Chinazzo2019-ye", "Krau02": "Krauchi2002-aq", "Schi17": "Schiavon2017-fx",
    "Hodd07": "Hodder2007-qo", "Dear98": "Dear1998-va", "Shov03": "Shove2003-lf",
    "Hitc11": "Hitchings2011-eo", "Roaf26": "Roaf2026-kt", "Good20": "Goodchild2020-ew",
    "Stre11": "Strengers2011-bm", "Will25": "Williamson2025-nt", "Cole23": "Colelli2023-fy",
    "Zhan26": "Zhang2026-cx", "Falc24": "Falchetta2024-ao", "He22": "He2022-rg",
    "Nahe21": "Naheed2021-ce", "Atma19": "Atmaca2019-ur", "Wint13": "Winter2013-tm",
    "Shov14": "Shove2014-fx", "Hitc08": "Hitchings2008-ky", "Osun20": "Osunmuyiwa2020-fr",
    "Heal08": "Healy2008-hk", "Noon15": "Noonan2015-uz", "Davi15": "Davis2015-po",
    "Lund18": "Lundgren-Kownacki2018-bv", "Yun11": "Yun2011-nu", "Chin22": "Chinazzo2022-dt",
    "Porr24": "Porras-Salazar2024-mo",
}


def cite_runs(spec):
    """Yield (element label, run dict) for every superscript citation run."""
    for sh in spec["shapes"]:
        if sh["kind"] != "text":
            continue
        label = " ".join(r["t"] for p in sh["paras"] for r in p["runs"]
                         if not r.get("sup")).strip()
        for p in sh["paras"]:
            for r in p["runs"]:
                if r.get("sup") and "[" in r["t"]:
                    yield label, r


def tokens(run):
    m = re.search(r"\[([^\]]*)\]", run["t"])
    return [t.strip() for t in m.group(1).split(",")] if m else []


def write_keysheet(spec, path):
    rows = []
    for label, r in cite_runs(spec):
        for tok in tokens(r):
            rows.append({"element": label, "token": tok,
                         "bibtex_key": KEYS.get(tok, ""), "number": ""})
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, ["element", "token", "bibtex_key", "number"])
        w.writeheader()
        w.writerows(rows)
    return rows


def apply(spec, mapping, placeholder="XX"):
    """mapping: token -> number (int). Anything missing becomes the placeholder."""
    changed = 0
    for _, r in cite_runs(spec):
        toks = tokens(r)
        nums, unresolved = [], []
        for t in toks:
            if t in mapping:
                nums.append(int(mapping[t]))
            else:
                unresolved.append(placeholder)
        body = ",".join([str(n) for n in sorted(nums)] + unresolved)
        r["t"] = " [" + body + "]"
        changed += 1
    return changed


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--placeholder", action="store_true",
                    help="write every citation as [XX] / [XX,XX]")
    ap.add_argument("--map", help="CSV with token,number columns")
    ap.add_argument("--out", default=os.path.join(HERE, "figure_spec_numbered.json"))
    a = ap.parse_args()

    spec = json.load(open(SPEC))
    sheet = write_keysheet(spec, os.path.join(HERE, "citation_keys.csv"))
    print(f"citation_keys.csv: {len(sheet)} citation slots "
          f"across {len(set(r['element'] for r in sheet))} elements, "
          f"{len(set(r['token'] for r in sheet))} distinct sources")

    mapping = {}
    if a.map:
        for row in csv.DictReader(open(a.map)):
            if row.get("number", "").strip():
                mapping[row["token"].strip()] = int(row["number"])
        print(f"mapped {len(mapping)} tokens from {a.map}")

    n = apply(spec, mapping)
    json.dump(spec, open(a.out, "w"), separators=(",", ":"))
    print(f"rewrote {n} citation brackets -> {a.out}")

    try:
        from build_thermal_preference_figure import build
        pptx = a.out.replace(".json", "").replace("figure_spec_", "figure_") + ".pptx"
        build(spec, pptx)
        print("built", pptx)
    except ImportError:
        print("(put build_thermal_preference_figure.py alongside to build the pptx too)")
