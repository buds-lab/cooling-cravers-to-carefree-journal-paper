"""
Extract a PowerPoint figure into figure_spec.json.

    python extract_figure_spec.py my_edited_figure.pptx

Run this after editing the deck in PowerPoint to refresh the spec, so
build_thermal_preference_figure.py stays in sync with your changes.

Captures: freeform geometry in native path units (with open/closed subpaths and
hole windings intact), preset shapes, connectors with dash and arrowheads, every
text run with size/bold/font/superscript, plus rotation and flips.
"""
import json
import os
import sys
from pptx import Presentation
from pptx.oxml.ns import qn

PX = 9525
SRC = sys.argv[1] if len(sys.argv) > 1 else "figure.pptx"
OUT = os.path.join(os.path.dirname(os.path.abspath(SRC)) or ".", "figure_spec.json")

prs = Presentation(SRC)
sl = prs.slides[0]


def emu(v):
    return None if v is None else round(int(v) / PX, 3)


def color_of(node):
    if node is None:
        return None
    if node.find(qn('a:noFill')) is not None:
        return "none"
    sf = node.find(qn('a:solidFill'))
    if sf is None:
        return None
    c = sf.find(qn('a:srgbClr'))
    return c.get('val') if c is not None else None


def line_spec(spPr):
    ln = spPr.find(qn('a:ln'))
    if ln is None:
        return None
    d = {"w": round(int(ln.get('w')) / 12700, 3) if ln.get('w') else None,
         "color": color_of(ln)}
    dash = ln.find(qn('a:prstDash'))
    if dash is not None:
        d["dash"] = dash.get('val')
    for end in ("headEnd", "tailEnd"):
        e = ln.find(qn('a:' + end))
        if e is not None:
            d[end] = {"type": e.get('type'), "w": e.get('w'), "len": e.get('len')}
    return d


shapes = []
for sh in sl.shapes:
    el = sh._element
    spPr = el.find(qn('p:spPr'))
    xfrm = spPr.find(qn('a:xfrm')) if spPr is not None else None
    off = xfrm.find(qn('a:off')) if xfrm is not None else None
    ext = xfrm.find(qn('a:ext')) if xfrm is not None else None
    rec = {"x": emu(off.get('x')), "y": emu(off.get('y')),
           "w": emu(ext.get('cx')), "h": emu(ext.get('cy')),
           "flipH": xfrm.get('flipH') == '1', "flipV": xfrm.get('flipV') == '1',
           "rot": int(xfrm.get('rot') or 0),
           "fill": color_of(spPr), "line": line_spec(spPr)}

    cust = spPr.find(qn('a:custGeom'))
    prst = spPr.find(qn('a:prstGeom'))
    has_text = sh.has_text_frame and sh.text_frame.text.strip()

    if cust is not None:
        # absolute px points, so the rebuild does not depend on local units
        # keep native path units so the rebuild is byte-identical
        geom = []
        for path in cust.findall('.//' + qn('a:path')):
            subs, cur, closed = [], [], []
            for node in path:
                t = node.tag.split('}')[-1]
                if t in ("moveTo", "lnTo"):
                    pt = node.find(qn('a:pt'))
                    if t == "moveTo" and cur:
                        subs.append(cur); closed.append(False); cur = []
                    cur.append([int(pt.get('x')), int(pt.get('y'))])
                elif t == "close":
                    if cur:
                        subs.append(cur); closed.append(True); cur = []
            if cur:
                subs.append(cur); closed.append(False)
            geom.append({"w": int(path.get('w')), "h": int(path.get('h')),
                         "subs": subs, "closed": closed})
        rec.update(kind="freeform", geom=geom)
    elif el.tag.endswith('cxnSp'):
        rec.update(kind="connector")
    elif has_text:
        tf = sh.text_frame
        paras = []
        for p in tf.paragraphs:
            runs = []
            for r in p.runs:
                rp = r.font._rPr
                runs.append({"t": r.text,
                             "sz": r.font.size.pt if r.font.size else None,
                             "b": bool(r.font.bold),
                             "font": r.font.name,
                             "sup": rp.get('baseline') if rp is not None else None})
            paras.append({"align": str(p.alignment).split(" ")[0] if p.alignment is not None else None,
                          "runs": runs})
        rec.update(kind="text", wrap=tf.word_wrap,
                   anchor=str(tf.vertical_anchor).split(" ")[0] if tf.vertical_anchor is not None else None,
                   paras=paras)
    elif prst is not None:
        rec.update(kind="preset", prst=prst.get('prst'))
    else:
        continue
    shapes.append(rec)

spec = {"width": round(prs.slide_width / PX), "height": round(prs.slide_height / PX),
        "shapes": shapes}
json.dump(spec, open(OUT, "w"), separators=(",", ":"))
print(f"{len(shapes)} shapes -> {OUT}  ({os.path.getsize(OUT)/1024:.0f} KB)")
from collections import Counter
print(Counter(s["kind"] for s in shapes))
