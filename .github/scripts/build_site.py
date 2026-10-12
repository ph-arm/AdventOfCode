"""Build a static GitHub Pages site from docs/benchmarks.json.

Renders median solution times per day and part. Puzzle answers are never read
or shown here; only timings and a verification badge. benchmarks.json sits next
to index.html so it stays directly downloadable from the site.
"""

import json
import math
from pathlib import Path

DOCS = Path(__file__).parents[2] / "docs"
BENCH_FILE = DOCS / "benchmarks.json"

data: dict = json.loads(BENCH_FILE.read_text())
years: dict = data.get("years", {})
totals: dict = data.get("totals", {})

STAR = "&#11088;"
MARKS = {"ok": "&#10003;", "fail": "&#10007;", "timeout": "&#8987;", "skip": "&#8211;"}


def fmt_ms(ms: float) -> str:
    if ms < 1:
        return f"{ms:.3f} ms"
    if ms < 1000:
        return f"{ms:.2f} ms"
    return f"{ms / 1000:.2f} s"


def day_num(day_key: str) -> str:
    return day_key.removeprefix("day_").lstrip("0") or "0"


# Flatten once for global bar scaling and the "slowest" list.
flat: list[tuple[str, str, str, dict]] = []
for year_name, day_map in years.items():
    for day_key, part_map in day_map.items():
        for part_key, info in part_map.items():
            flat.append((year_name, day_key, part_key, info))

max_ms = max((info["median_ms"] for *_, info in flat), default=1.0)
log_max = math.log10(max_ms + 1) or 1.0


def bar_pct(ms: float) -> float:
    # Log scale so sub-millisecond and multi-second bars are both visible.
    return max(2.0, math.log10(ms + 1) / log_max * 100)


def bar_class(ms: float) -> str:
    if ms >= 5000:
        return "bar slow"
    if ms >= 1000:
        return "bar warn"
    return "bar"


sections: list[str] = []
for year_name in sorted(years):
    label = year_name.replace("AdventOfCode", "")
    rows: list[str] = []
    for day_key in sorted(years[year_name]):
        for part_key in sorted(years[year_name][day_key]):
            info = years[year_name][day_key][part_key]
            ms = info["median_ms"]
            status = info.get("status", "ok")
            mark = MARKS.get(status, "")
            part_label = part_key.replace("part_", "Part ")
            rng = f"{fmt_ms(info['min_ms'])} &ndash; {fmt_ms(info['max_ms'])}"
            rows.append(
                f'<tr class="s-{status}">'
                f'<td class="day">Day {day_num(day_key)}</td>'
                f"<td>{part_label}</td>"
                f'<td class="time">{fmt_ms(ms)}</td>'
                f'<td class="range">{rng}</td>'
                f'<td class="barcell"><span class="{bar_class(ms)}" '
                f'style="width:{bar_pct(ms):.1f}%"></span></td>'
                f'<td class="status">{mark}</td>'
                "</tr>"
            )
    sections.append(
        f'<section class="year"><h2>{STAR} {label}</h2>'
        "<table><thead><tr>"
        "<th>Day</th><th>Part</th><th>Median</th><th>Range</th>"
        '<th class="barhead">Relative</th><th>OK</th>'
        f"</tr></thead><tbody>{''.join(rows)}</tbody></table></section>"
    )

slowest = sorted(flat, key=lambda t: t[3]["median_ms"], reverse=True)[:5]
slow_items = "".join(
    f"<li><strong>{fmt_ms(info['median_ms'])}</strong> &mdash; "
    f"{year_name.replace('AdventOfCode', '')} Day {day_num(day_key)} "
    f"{part_key.replace('part_', 'Part ')}</li>"
    for year_name, day_key, part_key, info in slowest
)

generated = data.get("generated_utc", "")
runs = data.get("runs_per_part", "")
python_ver = data.get("python", "")
chips = [
    f"{totals.get('parts', 0)} parts",
    f"{totals.get('verified', 0)} verified",
    f"median of {runs} runs",
    f"~{totals.get('median_sum_sec', 0):.1f}s total",
    f"Python {python_ver}",
]
meta_chips = "".join(f'<span class="chip">{c}</span>' for c in chips)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Advent of Code &mdash; Benchmarks</title>
<style>
  :root {{ --bg:#0f0f23; --panel:#10101a; --line:#23233a; --txt:#cfd2dc;
           --accent:#ffff66; --green:#44dd77; --warn:#e3b341; --slow:#e5534b; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:"Segoe UI",system-ui,sans-serif; background:var(--bg);
          color:var(--txt); margin:0; padding:2rem 1.25rem 4rem; }}
  .wrap {{ max-width:920px; margin:0 auto; }}
  h1 {{ color:var(--accent); margin:0 0 .25rem; font-size:1.9rem; }}
  p.subtitle {{ color:#9aa0b4; margin:.2rem 0 1.25rem; max-width:40rem; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:.5rem; margin-bottom:1rem; }}
  .chip {{ background:var(--panel); border:1px solid var(--line); color:#b9c0d4;
           padding:.3rem .7rem; border-radius:999px; font-size:.82rem; }}
  .actions {{ margin:0 0 1.75rem; }}
  .btn {{ display:inline-block; background:#1b2b22; border:1px solid #2f6f4a;
          color:var(--green); padding:.5rem .9rem; border-radius:8px;
          text-decoration:none; font-size:.9rem; }}
  .btn:hover {{ background:#203a2b; }}
  section.year {{ margin:0 0 2rem; }}
  h2 {{ color:var(--green); font-size:1.15rem;
        border-bottom:1px solid var(--line); padding-bottom:.4rem; margin:0 0 .5rem; }}
  table {{ border-collapse:collapse; width:100%; }}
  th {{ text-align:left; color:#8b93ab; font-weight:600; font-size:.78rem;
        text-transform:uppercase; letter-spacing:.04em; padding:.4rem .6rem; }}
  td {{ padding:.35rem .6rem; border-top:1px solid var(--line); font-size:.9rem; }}
  td.day {{ color:#aeb4c8; white-space:nowrap; }}
  td.time {{ font-family:ui-monospace,monospace; color:#fff; text-align:right;
             white-space:nowrap; }}
  td.range {{ font-family:ui-monospace,monospace; color:#7b84a0; font-size:.82rem;
              white-space:nowrap; }}
  tr:hover td {{ background:#161627; }}
  .barcell {{ width:34%; }}
  .bar {{ display:block; height:9px; border-radius:5px; background:var(--green);
          min-width:4px; }}
  .bar.warn {{ background:var(--warn); }}
  .bar.slow {{ background:var(--slow); }}
  td.status {{ color:var(--green); text-align:center; }}
  tr.s-fail td.status, tr.s-timeout td.status {{ color:var(--slow); }}
  .slow-list {{ list-style:none; padding:0; margin:.25rem 0 0; }}
  .slow-list li {{ padding:.3rem 0; border-top:1px solid var(--line);
                   font-size:.9rem; color:#b9c0d4; }}
  .slow-list strong {{ font-family:ui-monospace,monospace; color:#fff; }}
  footer {{ margin-top:2.5rem; color:#6f7691; font-size:.8rem; }}
  a {{ color:var(--green); }}
</style>
</head>
<body>
<div class="wrap">
  <h1>{STAR} Advent of Code &mdash; Benchmarks</h1>
  <p class="subtitle">Median solution times, measured automatically by GitHub
  Actions. Puzzle inputs are encrypted; answers are verified by hash and never
  shown.</p>
  <div class="chips">{meta_chips}</div>
  <div class="actions"><a class="btn" href="benchmarks.json">&#8681; benchmarks.json</a></div>
  {"".join(sections)}
  <section>
    <h2>Slowest solutions</h2>
    <ul class="slow-list">{slow_items}</ul>
  </section>
  <footer>Generated {generated} &middot; median of {runs} runs/part &middot; Python {python_ver}</footer>
</div>
</body>
</html>
"""

(DOCS / "index.html").write_text(html)
print(
    f"Built docs/index.html ({len(years)} years, "
    f"{sum(len(d) for d in years.values())} days, {len(flat)} parts)"
)
