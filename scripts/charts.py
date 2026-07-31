"""Generate README charts as SVG directly from the corpus.

Hand-rolled SVG rather than matplotlib: no extra dependency, a few KB per
chart, and colours chosen to read on both GitHub themes (no background fill,
mid-tone text that survives light and dark).
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "img"
DOCS.mkdir(parents=True, exist_ok=True)

FG, MUTED, ACCENT, ACCENT2 = "#8b949e", "#6e7681", "#e5484d", "#3fb950"
FONT = "ui-monospace,SFMono-Regular,Menlo,monospace"

recs = [i for f in sorted((ROOT / "data" / "incidents").glob("*.json"))
        for i in json.load(open(f))]

# ---------- timeline ----------
months = collections.Counter()
for r in recs:
    if r.get("created_at"):
        months[r["created_at"][:7]] += 1

keys = sorted(k for k in months if k >= "2023-01")
vals = [months[k] for k in keys]
peak = max(vals)
W, H, PAD_L, PAD_B, PAD_T = 900, 240, 44, 34, 18
bw = (W - PAD_L - 12) / len(keys)

bars, ticks = [], []
for i, (k, v) in enumerate(zip(keys, vals, strict=True)):
    h = (v / peak) * (H - PAD_B - PAD_T)
    x = PAD_L + i * bw
    y = H - PAD_B - h
    bars.append(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw*0.78:.1f}" height="{h:.1f}" '
        f'rx="1.5" fill="{ACCENT}" opacity="0.82"><title>{k}: {v} incidents</title></rect>'
    )
    if k.endswith("-01"):
        ticks.append(
            f'<text x="{x:.1f}" y="{H-PAD_B+16:.0f}" fill="{MUTED}" '
            f'font-size="11" font-family="{FONT}">{k[:4]}</text>'
        )

grid = []
for frac in (0.25, 0.5, 0.75, 1.0):
    y = H - PAD_B - frac * (H - PAD_B - PAD_T)
    grid.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W-12}" y2="{y:.1f}" '
                f'stroke="{MUTED}" stroke-width="0.5" opacity="0.22"/>')
    grid.append(f'<text x="6" y="{y+4:.1f}" fill="{MUTED}" font-size="10" '
                f'font-family="{FONT}">{int(peak*frac)}</text>')

(DOCS / "timeline.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
    f'<text x="6" y="12" fill="{FG}" font-size="12" font-family="{FONT}">'
    f'incidents per month &#183; {len(recs):,} total &#183; {keys[0]} to {keys[-1]}</text>'
    + "".join(grid) + "".join(bars) + "".join(ticks) + "</svg>"
)

# ---------- MTTR ----------
summary = json.load(open(ROOT / "data" / "summary.json"))
rows = [(v["provider_name"], v["incident_count"], v["mttr_minutes_median"])
        for v in summary["by_provider"].values() if v["mttr_minutes_median"]]
rows.sort(key=lambda r: r[2])
rows = rows[:12]

W2, RH, LBL = 900, 26, 168
H2 = len(rows) * RH + 34
mx = max(r[2] for r in rows)
out = []
for i, (name, n, med) in enumerate(rows):
    y = 26 + i * RH
    bl = (med / mx) * (W2 - LBL - 96)
    out.append(f'<text x="6" y="{y+11}" fill="{FG}" font-size="11.5" '
               f'font-family="{FONT}">{name}</text>')
    out.append(f'<rect x="{LBL}" y="{y+1}" width="{bl:.1f}" height="14" rx="2" '
               f'fill="{ACCENT2}" opacity="0.72"><title>{name}: n={n}</title></rect>')
    out.append(f'<text x="{LBL+bl+8:.1f}" y="{y+12}" fill="{MUTED}" font-size="10.5" '
               f'font-family="{FONT}">{med/60:.1f}h &#183; n={n}</text>')

(DOCS / "mttr.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" width="{W2}" height="{H2}">'
    f'<text x="6" y="13" fill="{FG}" font-size="12" font-family="{FONT}">'
    f'median time to resolution &#183; lower is better</text>'
    + "".join(out) + "</svg>"
)

print(f"  timeline.svg  {len(keys)} months, peak {peak}")
print(f"  mttr.svg      {len(rows)} providers")
print(f"  corpus        {len(recs):,} incidents")


# ---------- logo ----------
LOGO = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 76" width="76" height="76">
  <circle cx="38" cy="38" r="35" fill="none" stroke="{MUTED}" stroke-width="1" opacity="0.35"/>
  <circle cx="38" cy="38" r="25" fill="none" stroke="{MUTED}" stroke-width="1" opacity="0.25"/>
  <circle cx="38" cy="38" r="15" fill="none" stroke="{MUTED}" stroke-width="1" opacity="0.18"/>
  <circle cx="38" cy="10" r="3.4" fill="{ACCENT}"/>
  <circle cx="62" cy="30" r="2.6" fill="{ACCENT}" opacity="0.75"/>
  <circle cx="53" cy="60" r="3.0" fill="{ACCENT2}" opacity="0.8"/>
  <circle cx="20" cy="57" r="2.4" fill="{ACCENT2}" opacity="0.6"/>
  <circle cx="14" cy="27" r="2.8" fill="{ACCENT}" opacity="0.55"/>
  <circle cx="38" cy="38" r="4.5" fill="{FG}"/>
</svg>'''
(DOCS / "logo.svg").write_text(LOGO)

# ---------- architecture ----------
BOX = f'fill="none" stroke="{MUTED}" stroke-width="1" opacity="0.5" rx="4"'
def box(x, y, w, h, label, sub=""):
    t = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {BOX}/>',
        (
            f'<text x="{x+w/2}" y="{y+(20 if sub else h/2+4)}" fill="{FG}" '
            f'font-size="12" font-family="{FONT}" text-anchor="middle">{label}</text>'
        ),
    ]
    if sub:
        for i, line in enumerate(sub.split("|")):
            t.append(f'<text x="{x+w/2}" y="{y+36+i*14}" fill="{MUTED}" font-size="10" '
                     f'font-family="{FONT}" text-anchor="middle">{line}</text>')
    return "".join(t)

def arrow(x1, y, x2):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-6}" y2="{y}" stroke="{MUTED}" '
            f'stroke-width="1" opacity="0.55"/>'
            f'<path d="M{x2-6},{y-3.5} L{x2},{y} L{x2-6},{y+3.5}" fill="{MUTED}" opacity="0.55"/>')

ARCH = (
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" width="900" height="260">'
  + box(8, 96, 128, 56, "providers.yaml", "25 entries")
  + arrow(136, 124, 176)
  + box(176, 60, 150, 128, "adapters", "statuspage &#215;22|gcp|azure_rss|aws")
  + arrow(326, 124, 366)
  + box(366, 96, 146, 56, "normalize", "one schema")
  + arrow(512, 124, 552)
  + box(552, 96, 132, 56, "corpus", "dedup by key")
  + arrow(684, 124, 724)
  + box(724, 22, 168, 42, "incidents/YYYY.json")
  + box(724, 76, 168, 42, "summary.json")
  + box(724, 130, 168, 42, "daily/*.json")
  + box(724, 184, 168, 42, "docs/ &#8594; site")
  + f'<text x="8" y="248" fill="{MUTED}" font-size="10.5" font-family="{FONT}">'
    f'a failing provider degrades itself only &#183; if all fail, the run aborts without writing</text>'
  + '</svg>')
(DOCS / "architecture.svg").write_text(ARCH)
print("  logo.svg, architecture.svg")
