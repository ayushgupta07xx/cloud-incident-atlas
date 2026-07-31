"""Generate README charts as SVG directly from the corpus.

Hand-rolled SVG rather than matplotlib: no extra dependency, a few KB per
chart, and every colour has to hold up on both GitHub themes — these render
on white and on #0d1117, so there is no background fill anywhere and no
near-black or near-white ink.
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "img"
DOCS.mkdir(parents=True, exist_ok=True)

INK = "#adbac7"
FG = "#8b949e"
MUTED = "#6e7681"
FAINT = "#484f58"
CRIMSON = "#e5484d"
AMBER = "#d29922"
GREEN = "#3fb950"

SANS = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"


def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def blend(c1, c2, t):
    """Blend two hex colours. Used to grade bars by value, not by position."""
    t = max(0.0, min(1.0, t))
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02x}" for i in range(3))


recs = [i for f in sorted((ROOT / "data" / "incidents").glob("*.json"))
        for i in json.load(open(f))]
summary = json.load(open(ROOT / "data" / "summary.json"))

# --------------------------------------------------------------- timeline
months = collections.Counter()
for r in recs:
    if r.get("created_at"):
        months[r["created_at"][:7]] += 1

keys = sorted(k for k in months if k >= "2023-01")
vals = [months[k] for k in keys]
peak = max(vals)
peak_i = vals.index(peak)

W, H = 900, 300
L, R, TOP, BOT = 52, 20, 62, 46
plot_w, plot_h = W - L - R, H - TOP - BOT
bw = plot_w / len(keys)

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">',
    '<defs>',
    '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0%" stop-color="{CRIMSON}" stop-opacity="0.95"/>',
    f'<stop offset="65%" stop-color="{CRIMSON}" stop-opacity="0.55"/>',
    f'<stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.18"/>',
    '</linearGradient>',
    '<linearGradient id="pk" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0%" stop-color="{AMBER}" stop-opacity="1"/>',
    f'<stop offset="100%" stop-color="{AMBER}" stop-opacity="0.25"/>',
    '</linearGradient>',
    '</defs>',
    f'<text x="{L}" y="26" fill="{INK}" font-size="15" font-family="{SANS}" font-weight="600">Incidents per month</text>',
    f'<text x="{L}" y="44" fill="{MUTED}" font-size="11.5" font-family="{MONO}">{len(recs):,} incidents &#183; {keys[0]} &#8594; {keys[-1]}</text>',
]

for frac in (0.25, 0.5, 0.75, 1.0):
    y = TOP + plot_h - frac * plot_h
    parts.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{FAINT}" stroke-width="1" stroke-dasharray="2 4" opacity="0.5"/>')
    parts.append(f'<text x="{L-10}" y="{y+3.5:.1f}" fill="{FAINT}" font-size="10" font-family="{MONO}" text-anchor="end">{int(peak*frac)}</text>')

parts.append(f'<line x1="{L}" y1="{TOP+plot_h}" x2="{W-R}" y2="{TOP+plot_h}" stroke="{MUTED}" stroke-width="1" opacity="0.55"/>')

for i, (k, v) in enumerate(zip(keys, vals, strict=True)):
    h = (v / peak) * plot_h
    x = L + i * bw
    y = TOP + plot_h - h
    fill = "url(#pk)" if i == peak_i else "url(#bg)"
    parts.append(f'<rect x="{x+bw*0.13:.1f}" y="{y:.1f}" width="{bw*0.74:.1f}" height="{h:.1f}" rx="2" fill="{fill}"><title>{k}: {v} incidents</title></rect>')
    if k.endswith("-01"):
        parts.append(f'<line x1="{x:.1f}" y1="{TOP}" x2="{x:.1f}" y2="{TOP+plot_h}" stroke="{FAINT}" stroke-width="1" opacity="0.35"/>')
        parts.append(f'<text x="{x:.1f}" y="{TOP+plot_h+20:.0f}" fill="{FG}" font-size="11" font-family="{MONO}">{k[:4]}</text>')

px = L + peak_i * bw + bw / 2
parts.append(f'<text x="{px:.1f}" y="{TOP + plot_h - (peak/peak)*plot_h - 8:.1f}" fill="{AMBER}" font-size="10.5" font-family="{MONO}" text-anchor="middle">peak {peak}</text>')
parts.append('</svg>')
(DOCS / "timeline.svg").write_text("".join(parts))

# ------------------------------------------------------------------- mttr
rows = [(v["provider_name"], v["incident_count"], v["mttr_minutes_median"])
        for v in summary["by_provider"].values() if v["mttr_minutes_median"]]
rows.sort(key=lambda r: r[2])
rows = rows[:12]

RH, LBL, TOP2 = 30, 176, 62
W2 = 900
H2 = TOP2 + len(rows) * RH + 22
track = W2 - LBL - 132
mx = max(r[2] for r in rows)

m = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" width="{W2}" height="{H2}" role="img">',
    f'<text x="24" y="28" fill="{INK}" font-size="15" font-family="{SANS}" font-weight="600">Median time to resolution</text>',
    f'<text x="24" y="46" fill="{MUTED}" font-size="11.5" font-family="{MONO}">fastest 12 providers &#183; lower is better &#183; n = incidents with a measured duration</text>',
]

for i, (name, n, med) in enumerate(rows):
    y = TOP2 + i * RH
    hours = med / 60
    grade = blend(GREEN, AMBER, (hours - 0.5) / 2.5)
    bl = max(6.0, (med / mx) * track)
    if i % 2 == 0:
        m.append(f'<rect x="16" y="{y-6}" width="{W2-32}" height="{RH-4}" rx="4" fill="{MUTED}" opacity="0.055"/>')
    m.append(f'<text x="30" y="{y+11}" fill="{FAINT}" font-size="10" font-family="{MONO}">{i+1:02d}</text>')
    m.append(f'<text x="56" y="{y+12}" fill="{INK}" font-size="12.5" font-family="{SANS}">{esc(name)}</text>')
    m.append(f'<rect x="{LBL}" y="{y+1}" width="{track}" height="13" rx="6.5" fill="{MUTED}" opacity="0.11"/>')
    m.append(f'<rect x="{LBL}" y="{y+1}" width="{bl:.1f}" height="13" rx="6.5" fill="{grade}" opacity="0.9"><title>{esc(name)}: {hours:.1f}h median over {n} incidents</title></rect>')
    m.append(f'<text x="{LBL+track+16:.0f}" y="{y+12}" fill="{INK}" font-size="12" font-family="{MONO}" text-anchor="end">{hours:.1f}h</text>')
    m.append(f'<text x="{LBL+track+26:.0f}" y="{y+12}" fill="{FAINT}" font-size="10.5" font-family="{MONO}">n={n:,}</text>')

m.append('</svg>')
(DOCS / "mttr.svg").write_text("".join(m))

# --------------------------------------------------------------- pipeline
def node(x, y, w, h, title, sub=None, accent=False):
    stroke = CRIMSON if accent else MUTED
    op = "0.55" if accent else "0.4"
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{MUTED}" opacity="0.05"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="none" stroke="{stroke}" stroke-width="1.1" opacity="{op}"/>',
    ]
    ty = y + (22 if sub else h / 2 + 4.5)
    out.append(f'<text x="{x+w/2}" y="{ty}" fill="{INK}" font-size="12.5" font-family="{MONO}" text-anchor="middle">{title}</text>')
    for j, line in enumerate(sub or []):
        out.append(f'<text x="{x+w/2}" y="{y+40+j*14.5}" fill="{MUTED}" font-size="10.5" font-family="{MONO}" text-anchor="middle">{line}</text>')
    return "".join(out)


def link(x1, y1, x2, y2=None):
    """Bezier connector. Omit y2 for a straight horizontal link."""
    if y2 is None:
        y2 = y1
    mid = x1 + (x2 - x1) * 0.5
    return "".join([
        f'<path d="M{x1},{y1} C{mid},{y1} {mid},{y2} {x2-7},{y2}" fill="none" stroke="{MUTED}" stroke-width="1.1" opacity="0.45"/>',
        f'<path d="M{x2-7},{y2-3.6} L{x2},{y2} L{x2-7},{y2+3.6}" fill="{MUTED}" opacity="0.45"/>',
    ])


n_sp = sum(1 for p in __import__("yaml").safe_load(
    open(ROOT / "providers.yaml"))["providers"] if p["adapter"] == "statuspage")

W3, H3 = 900, 320
a = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W3} {H3}" width="{W3}" height="{H3}" role="img">',
    f'<text x="24" y="28" fill="{INK}" font-size="15" font-family="{SANS}" font-weight="600">Pipeline</text>',
]

for lx, label in ((24, "SOURCE"), (172, "ADAPT"), (382, "NORMALIZE"), (556, "STORE"), (724, "PUBLISH")):
    a.append(f'<text x="{lx}" y="62" fill="{FAINT}" font-size="9.5" font-family="{SANS}" letter-spacing="1.4">{label}</text>')

a.append(node(24, 130, 128, 58, "providers.yaml", ["25 entries"]))
a.append(link(152, 159, 172))
a.append(node(172, 96, 156, 126, "adapters", [f"statuspage &#215;{n_sp}", "gcp", "azure_rss", "aws"], accent=True))
a.append(link(328, 159, 382))
a.append(node(382, 130, 142, 58, "normalize", ["one schema"]))
a.append(link(524, 159, 556))
a.append(node(556, 130, 136, 58, "corpus", ["dedup by key"]))

outs = ["incidents/YYYY.json", "summary.json", "daily/*.json", "docs/ &#8594; site"]
for j, label in enumerate(outs):
    oy = 78 + j * 54
    a.append(link(692, 159, 724, oy + 20))
    a.append(node(724, oy, 160, 40, label))

a.append(f'<text x="24" y="304" fill="{FAINT}" font-size="10.5" font-family="{MONO}">a failing provider degrades itself only &#183; if every provider fails, the run aborts without writing</text>')
a.append('</svg>')
(DOCS / "architecture.svg").write_text("".join(a))

# ------------------------------------------------------------------- logo
# Globe graticule + cloud + incident waveform. The lower parallel arc is
# deliberately absent: it sat within a pixel of the waveform baseline and the
# two collided into a smudge. The waveform is the lower feature.
LOGO_PARTS = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80" role="img">',
    '<title>Cloud Incident Atlas</title>',
    '<desc>A globe of graticule lines containing a cloud above an incident spike</desc>',
    f'<circle cx="40" cy="40" r="31" fill="none" stroke="{CRIMSON}" stroke-width="1.7"/>',
    f'<ellipse cx="40" cy="40" rx="13" ry="31" fill="none" stroke="{MUTED}" stroke-width="0.9" opacity="0.42"/>',
    f'<path d="M13 27 Q40 21 67 27" fill="none" stroke="{MUTED}" stroke-width="0.9" opacity="0.4"/>',
    f'<path d="M21 34 A10.5 10.5 0 0 1 31 19 A13.5 13.5 0 0 1 55 22 A9.5 9.5 0 0 1 59 39 L23 39 A7.5 7.5 0 0 1 21 34Z" fill="{MUTED}" fill-opacity="0.16" stroke="{MUTED}" stroke-width="1.2"/>',
    f'<polyline points="14,54 25,54 30,46 35,64 40,49 45,54 66,54" fill="none" stroke="{CRIMSON}" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round"/>',
    '</svg>',
]
(DOCS / "logo.svg").write_text("".join(LOGO_PARTS))

print(f"  timeline.svg   {len(keys)} months, peak {peak}")
print(f"  mttr.svg       {len(rows)} providers")
print("  architecture.svg, logo.svg")
print(f"  corpus         {len(recs):,} incidents")
