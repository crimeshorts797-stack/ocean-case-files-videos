import json
END = 63.0
def load(v): return {s["id"]: s["start"] for s in json.load(open(f"/home/claude/out/{v}/timings.json"))["segments"]}
def cap(text, y, t0=0, size=38, **k): return {"type": "caption", "text": text, "y": y, "t0": round(max(0, t0), 2), "size": size, **k}
def tag(text): return {"type": "tag", "text": text, "x": 690, "y": 112, "size": 22, "box": True}
class Scene:
    def __init__(s, v, tagtext, cuts): s.v, s.tag, s.cuts, s.shots = v, tag(tagtext), cuts, []
    def shot(s, i, bg, els, **k):
        d = {"start": round(s.cuts[i], 3), "end": round(s.cuts[i+1], 3), "bg": bg, "elements": [s.tag]+els}; d.update(k); s.shots.append(d)
    def save(s, events, preset="abyss"):
        json.dump({"preset": preset, "fps": 30, "grain": .04, "tokens": {"hl": "#f5a623"}, "shots": s.shots}, open(f"/home/claude/out/{s.v}/scene.json", "w"), indent=1)
        json.dump(events, open(f"/home/claude/out/{s.v}/events.json", "w"), indent=1)
        print(s.v, [round(c, 2) for c in s.cuts])

def rorqual(x, y, s=1.0, body="#5f7f93", belly="#c9d6dd", flip=False, t0=0, opacity=1.0, **k):
    """Own baleen-whale drawing (slender body, small dorsal fin far back) for blue and fin whales."""
    sil = belly == body
    m = (f"<g transform='translate({x} {y}) scale({-s if flip else s} {s})' opacity='{opacity}'>"
         f"<path fill='{body}' d='M-190,0 L-246,-34 L-228,0 L-246,34 Z'/>"
         f"<path fill='{body}' d='M-80,-22 L-104,-42 L-114,-17 Z'/>"
         f"<path fill='{body}' d='M220,6 C200,-22 120,-34 20,-30 C-70,-27 -150,-14 -196,-3 L-196,5 C-150,16 -70,30 20,32 C120,34 196,26 220,6 Z'/>"
         f"<path fill='{belly}' d='M214,10 C190,28 120,34 20,32 C60,24 130,20 214,10 Z'/>"
         f"<path fill='{body}' d='M80,22 L40,64 L30,26 Z'/>"
         + ("" if sil else "<circle cx='172' cy='-4' r='3.5' fill='#0b0b0b'/>") + "</g>")
    return {"type": "svg", "markup": m, "t0": round(max(0, t0), 2), **k}
SIL = "#05090d"

# ---- extra hand-made drawings (own art, flat vector) ----
def svg(markup, t0=0, layer=None, **k):
    d = {"type": "svg", "markup": markup, "t0": round(max(0, t0), 2), **k}
    if layer: d["layer"] = layer
    return d
def humpback(x, y, s=1.0, flip=False, t0=0, opacity=1.0, body="#2d3a44", belly="#c9d3d8", **k):
    m = (f"<g transform='translate({x} {y}) scale({-s if flip else s} {s})' opacity='{opacity}'>"
         f"<path fill='{body}' d='M-200,0 L-262,-44 L-236,0 L-262,44 Z'/>"
         f"<path fill='{body}' d='M-70,-34 Q-86,-58 -100,-36 Z'/>"
         f"<path fill='{body}' d='M210,10 C190,-30 110,-46 10,-42 C-80,-38 -160,-16 -205,-2 L-205,6 C-160,22 -80,44 10,46 C110,48 196,34 210,10 Z'/>"
         f"<path fill='{belly}' d='M204,16 C180,36 110,44 20,42 C70,32 140,26 204,16 Z'/>"
         f"<path fill='{belly}' d='M70,30 C50,90 -10,150 -60,170 C-40,140 10,80 40,32 Z'/>"
         + "".join(f"<circle cx='{150+i*14}' cy='{-26+i*3}' r='4' fill='#1b242b'/>" for i in range(4))
         + "<circle cx='170' cy='4' r='3.5' fill='#0b0b0b'/></g>")
    return svg(m, t0, opacity=1, **k)
def seal(x, y, s=1.0, t0=0, col="#7a6f66", **k):
    m = (f"<g transform='translate({x} {y}) scale({s})'><path fill='{col}' d='M-90,10 C-60,-30 40,-36 80,-8 C96,4 92,18 74,20 C30,26 -40,30 -90,10 Z'/>"
         f"<path fill='{col}' d='M-88,8 L-120,-8 L-112,12 L-122,28 Z'/><circle cx='70' cy='-6' r='4' fill='#111'/></g>")
    return svg(m, t0, **k)
def jelly(x, y, s=1.0, t0=0, glow=False, col="#f2b8c6", **k):
    tent = "".join(f"<path d='M{-46+i*12},18 q6,40 -4,80 q-8,30 4,60' fill='none' stroke='{col}' stroke-width='3' opacity='.7'/>" for i in range(9))
    m = (f"<g transform='translate({x} {y}) scale({s})' {'filter=\"url(#glow)\"' if glow else ''}>{tent}"
         f"<path fill='{col}' opacity='.55' d='M-62,20 C-62,-60 62,-60 62,20 C30,10 -30,10 -62,20 Z'/>"
         f"<ellipse cx='0' cy='-6' rx='20' ry='16' fill='#c2453b' opacity='.85'/></g>")
    return svg(m, t0, **k)
def polyp(x, y, s=1.0, t0=0, col="#e8b4a0", **k):
    stems = "".join(f"<path d='M{dx},0 q{dx//3},-60 {dx//2},-120' fill='none' stroke='{col}' stroke-width='6'/><circle cx='{dx+dx//2}' cy='-126' r='14' fill='{col}'/>" for dx in (-60, -20, 20, 60))
    m = f"<g transform='translate({x} {y}) scale({s})'><rect x='-90' y='0' width='180' height='14' rx='7' fill='#5a4a3e'/>{stems}</g>"
    return svg(m, t0, **k)
def satellite(x, y, s=1.0, t0=0, **k):
    m = (f"<g transform='translate({x} {y}) scale({s}) rotate(-12)'><rect x='-30' y='-22' width='60' height='44' rx='6' fill='#d9dee2'/>"
         f"<rect x='-150' y='-16' width='110' height='32' fill='#2f5d8a' stroke='#9fc3e6' stroke-width='2'/><rect x='40' y='-16' width='110' height='32' fill='#2f5d8a' stroke='#9fc3e6' stroke-width='2'/>"
         f"<circle cx='0' cy='30' r='10' fill='#f5a623'/></g>")
    return svg(m, t0, **k)
def coin(text, x, y, t0, col="#f5a623", r=34):
    return svg(f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='{col}' stroke-width='4'/><text x='{x}' y='{y+11}' text-anchor='middle' font-family='Poppins' font-weight='800' font-size='30' fill='{col}'>{text}</text>", t0, layer="overlay")
def greenland(x, y, s=1.0, t0=0, body="#5b5550", belly="#8a827b", **k):
    m = (f"<g transform='translate({x} {y}) scale({s})'>"
         f"<path fill='{body}' d='M-190,-4 L-246,-58 L-232,0 L-240,40 Z'/>"
         f"<path fill='{body}' d='M10,-48 L-14,-84 L-46,-44 Z'/><path fill='{body}' d='M-90,-34 L-112,-62 L-136,-28 Z'/>"
         f"<path fill='{body}' d='M200,4 C196,-34 120,-56 20,-52 C-80,-48 -160,-26 -196,-6 L-196,4 C-160,26 -80,52 20,54 C120,56 196,40 200,4 Z'/>"
         f"<path fill='{belly}' d='M196,14 C170,40 110,50 20,48 C80,36 150,30 196,14 Z'/>"
         f"<path fill='{body}' d='M70,36 L40,90 L22,40 Z'/>"
         f"<circle cx='160' cy='-12' r='6' fill='#1a1a1a'/><path d='M166,-8 q6,18 -2,34' stroke='#cfd8b0' stroke-width='3' fill='none' opacity='.8'/></g>")
    return svg(m, t0, **k)
