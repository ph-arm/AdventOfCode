#!/usr/bin/env python3
"""Benchmark AoC solutions (median of N runs) and emit a times-only report.

Each recorded solution in answer_hashes.json is imported and run RUNS times;
the median wall-clock time is kept. The value a solution RETURNS is only
hash-verified against answer_hashes.json — it is never printed or published, so
no puzzle answers are exposed. Outputs:
  - BENCHMARK.md          human-readable table (local)
  - docs/benchmarks.json  machine-readable times for the GitHub Pages site

Run with the project venv so solution dependencies (numpy, ...) are importable:
  .venv/bin/python3 benchmark.py                # all years
  .venv/bin/python3 benchmark.py 2022           # 2022 only
  BENCH_RUNS=3 .venv/bin/python3 benchmark.py   # override runs per part
"""

import json
import os
import platform
import statistics
import sys
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from check_answers import (
    HASH_FILE,
    NO_RETURN,
    TIME_BUDGET,
    TIMEOUT,
    run_solution,
    sha256,
)

ROOT = Path(__file__).parent

# Runs per part; the median is reported. An odd count yields a true middle value.
RUNS = max(1, int(os.environ.get("BENCH_RUNS", "5")))


@dataclass
class Result:
    year: str
    day: int
    part: str
    median_sec: float
    min_sec: float
    max_sec: float
    runs: int
    status: str  # PASS | FAIL | NO-RETURN | TIMEOUT | SKIP


def evaluate(day_dir: Path, part_name: str, expected_hash: str, runs: int):
    """Run a solution up to `runs` times, returning (times, status, detail).

    The answer is hash-checked on the first run only and never returned. Any
    non-PASS outcome short-circuits after one run — repeating a broken or
    missing solution would add nothing.
    """
    times: list[float] = []
    for i in range(runs):
        start = time.perf_counter()
        try:
            value = run_solution(day_dir, part_name)
        except Exception as exc:
            elapsed = time.perf_counter() - start
            return [elapsed], "FAIL", f"ERROR {type(exc).__name__}: {str(exc)[:50]}"
        elapsed = time.perf_counter() - start

        if value is None:
            return [elapsed], "SKIP", "no file"
        if value is TIMEOUT:
            return [elapsed], "TIMEOUT", f">{TIME_BUDGET}s"
        if value is NO_RETURN:
            return [elapsed], "NO-RETURN", "main() returned None"
        if i == 0 and sha256(value) != expected_hash:
            return [elapsed], "FAIL", "hash mismatch"
        times.append(elapsed)
    return times, "PASS", ""


def _make_result(
    year: str, day_num: int, part_name: str, times: list[float], status: str
) -> Result:
    return Result(
        year=year,
        day=day_num,
        part=part_name,
        median_sec=statistics.median(times),
        min_sec=min(times),
        max_sec=max(times),
        runs=len(times),
        status=status,
    )


MARKS = {
    "PASS": "\u2713",
    "FAIL": "\u2717",
    "NO-RETURN": "\u2717 no return",
    "TIMEOUT": "TIMEOUT",
    "SKIP": "SKIP",
}

# Internal status -> compact status used in the published JSON (no answers).
STATUS_JSON = {
    "PASS": "ok",
    "FAIL": "fail",
    "NO-RETURN": "fail",
    "TIMEOUT": "timeout",
    "SKIP": "skip",
}


def run_year(year_name: str, stored: dict, runs: int) -> list[Result]:
    results: list[Result] = []
    year_dir = ROOT / year_name
    if not year_dir.exists():
        return results
    print(f"\n{year_name}")
    # Days and parts come straight from the hash file keys — nothing hard-coded.
    for day_key in sorted(stored[year_name]):
        day_dir = year_dir / day_key
        if not day_dir.exists():
            continue
        day_num = int(day_key.split("_")[-1])
        for part_key in sorted(stored[year_name][day_key]):
            part_name = part_key.removeprefix("part_")
            expected = stored[year_name][day_key][part_key]
            times, status, detail = evaluate(day_dir, part_name, expected, runs)
            result = _make_result(year_name, day_num, part_name, times, status)
            results.append(result)
            mark = MARKS[status]
            suffix = f"  {detail}" if detail and status != "PASS" else ""
            print(
                f"  Day {day_num:02d} Part {part_name}: "
                f"{result.median_sec:8.3f}s median  {mark}{suffix}"
            )
    return results


def write_report(results: list[Result], year_filter: str | None, runs: int) -> None:
    passed = sum(r.status == "PASS" for r in results)
    failed = sum(r.status in ("FAIL", "NO-RETURN") for r in results)
    skipped = sum(r.status in ("SKIP", "TIMEOUT") for r in results)
    total_time = sum(r.median_sec for r in results)

    lines = ["# Advent of Code - Benchmark & Verification", ""]
    scope = year_filter if year_filter else "all years"
    lines.append(
        f"Scope: **{scope}** - median of {runs} runs per part. Answers are "
        "hash-verified against `answer_hashes.json` and never shown."
    )
    lines.append("")
    lines.append(
        f"**{passed} passed, {failed} failed, {skipped} skipped / {len(results)} "
        f"total** - sum of medians {total_time:.2f}s"
    )
    lines.append("")

    by_year: dict[str, list[Result]] = {}
    for r in results:
        by_year.setdefault(r.year, []).append(r)

    for year_name, year_results in by_year.items():
        lines.append(f"## {year_name}")
        lines.append("")
        lines.append("| Day | Part | Median (s) | Min (s) | Max (s) | Status |")
        lines.append("|-----|------|------------|---------|---------|--------|")
        for r in year_results:
            lines.append(
                f"| {r.day:02d} | {r.part} | {r.median_sec:.3f} | "
                f"{r.min_sec:.3f} | {r.max_sec:.3f} | {r.status} |"
            )
        lines.append("")

    ran = [r for r in results if r.status in ("PASS", "FAIL", "NO-RETURN")]
    if ran:
        slowest = sorted(ran, key=lambda r: r.median_sec, reverse=True)[:5]
        lines.append("## Slowest solutions")
        lines.append("")
        for r in slowest:
            lines.append(
                f"- {r.year} Day {r.day:02d} Part {r.part}: {r.median_sec:.3f}s"
            )
        lines.append("")

    (ROOT / "BENCHMARK.md").write_text("\n".join(lines))


def write_json(results: list[Result], runs: int) -> None:
    """Emit docs/benchmarks.json with times and verification status only."""
    years: dict[str, dict] = {}
    for r in results:
        day_key = f"day_{r.day:02d}"
        years.setdefault(r.year, {}).setdefault(day_key, {})[f"part_{r.part}"] = {
            "median_ms": round(r.median_sec * 1000, 3),
            "min_ms": round(r.min_sec * 1000, 3),
            "max_ms": round(r.max_sec * 1000, 3),
            "runs": r.runs,
            "status": STATUS_JSON.get(r.status, "fail"),
        }

    ok = [r for r in results if r.status == "PASS"]
    payload = {
        "generated_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "runs_per_part": runs,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "totals": {
            "parts": len(results),
            "verified": len(ok),
            "median_sum_sec": round(sum(r.median_sec for r in ok), 3),
        },
        "years": years,
    }

    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "benchmarks.json").write_text(json.dumps(payload, indent=2) + "\n")


def main() -> None:
    if not HASH_FILE.exists():
        print(f"Missing {HASH_FILE.name}. Run fetch_answers.py first.")
        sys.exit(1)
    with open(HASH_FILE) as f:
        stored = json.load(f)

    year_filter = sys.argv[1] if len(sys.argv) > 1 else None
    results: list[Result] = []
    for year_name in sorted(stored):
        if year_filter and year_filter not in year_name:
            continue
        results.extend(run_year(year_name, stored, RUNS))

    passed = sum(r.status == "PASS" for r in results)
    failed = sum(r.status in ("FAIL", "NO-RETURN") for r in results)
    skipped = sum(r.status in ("SKIP", "TIMEOUT") for r in results)
    total_time = sum(r.median_sec for r in results)

    print(f"\n{'=' * 48}")
    print(
        f"Results: {passed} passed, {failed} failed, {skipped} skipped / "
        f"{len(results)} total  (median of {RUNS} runs/part)"
    )
    print(f"Sum of medians: {total_time:.2f}s")

    write_report(results, year_filter, RUNS)
    write_json(results, RUNS)
    print("Wrote BENCHMARK.md and docs/benchmarks.json")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
