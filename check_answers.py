# \!/usr/bin/env python3
"""
Verify all AoC solutions against expected answers.

Loads:
  answer_hashes.json   — SHA-256 hashes of correct answers (committed)
  answers_clear.json   — plaintext answers for reference (gitignored, optional)

For each solution, imports the module and calls main(). The value RETURNED by
main() (or solve_partN()) is the answer — stdout is ignored entirely. Solutions
must `return` their answer, never rely on print().

Usage: python3 check_answers.py [year_filter]
  python3 check_answers.py            # all years
  python3 check_answers.py 2022       # 2022 only
"""

import hashlib
import importlib.util
import io
import json
import os
import signal
import sys
from pathlib import Path

ROOT = Path(__file__).parent
HASH_FILE = ROOT / "answer_hashes.json"

# Sentinel: solution ran but main() returned None (missing `return`).
NO_RETURN = object()
# Sentinel: solution exceeded the time budget.
TIMEOUT = object()
# Per-solution time budget (seconds) enforced via SIGALRM.
TIME_BUDGET = 30


def sha256(text: str) -> str:
    return hashlib.sha256(text.strip().encode()).hexdigest()


# BaseException so a solution's own `except Exception` can't swallow the timeout.
class _Timeout(BaseException):
    pass


def _alarm(signum, frame):
    raise _Timeout


def run_solution(day_dir: Path, part_name: str):
    """Import the solution and return main()'s return value as a string.

    Returns:
      - str: the answer returned by main()/solve_partN()
      - None: solution file does not exist (not solved)
      - NO_RETURN: solution ran but returned None (needs a `return`)
      - TIMEOUT: solution exceeded TIME_BUDGET seconds
    """
    script = day_dir / f"part_{part_name}.py"
    if not script.exists():
        return None

    mod_name = f"_aoc_{day_dir.parent.name}_{day_dir.name}_{part_name}"
    sys.modules.pop(mod_name, None)
    spec = importlib.util.spec_from_file_location(mod_name, script)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load solution module from {script}")
    loader = spec.loader
    mod = importlib.util.module_from_spec(spec)

    orig_dir = os.getcwd()
    os.chdir(day_dir)
    # Some solutions do `from shared import *`, where shared.py lives beside the
    # solution. Put the day dir on sys.path so that import resolves; each day has
    # its own shared.py, so drop any cached one first.
    sys.path.insert(0, str(day_dir))
    sys.modules.pop("shared", None)
    # Suppress module-level/debug prints; the answer comes from the return value.
    orig_stdout = sys.stdout
    sys.stdout = io.StringIO()
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(TIME_BUDGET)
    try:
        loader.exec_module(mod)
        part_num = 1 if part_name == "one" else 2
        fn = getattr(mod, "main", None) or getattr(mod, f"solve_part{part_num}", None)
        if fn is None:
            return NO_RETURN
        # main() takes no args; solve_partN(input_file) takes the filename.
        if getattr(fn, "__name__", "").startswith("solve_part"):
            result = fn("input.txt")
        else:
            result = fn()
    except _Timeout:
        return TIMEOUT
    finally:
        signal.alarm(0)
        sys.stdout = orig_stdout
        os.chdir(orig_dir)
        if sys.path and sys.path[0] == str(day_dir):
            sys.path.pop(0)
        sys.modules.pop("shared", None)

    # Unwrap tuples/lists: some solvers return (answer, debug_data)
    if isinstance(result, list | tuple) and result:
        result = result[0]
    if result is None:
        return NO_RETURN
    return str(result).strip()


def main():
    if not HASH_FILE.exists():
        print(f"Missing {HASH_FILE.name}. Run fetch_answers.py first.")
        sys.exit(1)

    with open(HASH_FILE) as f:
        stored = json.load(f)

    year_filter = sys.argv[1] if len(sys.argv) > 1 else None
    total = passed = failed = skipped = 0

    # Days and parts come straight from the hash file keys — nothing is
    # hard-coded, so recording an answer in answer_hashes.json is enough.
    for year_name in sorted(stored):
        if year_filter and year_filter not in year_name:
            continue
        year_dir = ROOT / year_name
        if not year_dir.exists():
            continue
        print(f"\n{year_name}")

        for day_key in sorted(stored[year_name]):
            day_dir = year_dir / day_key
            if not day_dir.exists():
                continue
            day_num = int(day_key.split("_")[-1])

            for part_key in sorted(stored[year_name][day_key]):
                part_name = part_key.removeprefix("part_")
                total += 1
                expected_hash = stored[year_name][day_key][part_key]

                try:
                    result = run_solution(day_dir, part_name)
                except Exception as e:
                    failed += 1
                    print(
                        f"  Day {day_num:02d} Part {part_name}: \u2717  ERROR {type(e).__name__}: {str(e)[:50]}"
                    )
                    continue

                if result is None:
                    skipped += 1
                    print(f"  Day {day_num:02d} Part {part_name}: SKIP")
                elif result is TIMEOUT:
                    skipped += 1
                    print(
                        f"  Day {day_num:02d} Part {part_name}: TIMEOUT (>{TIME_BUDGET}s)"
                    )
                elif result is NO_RETURN:
                    failed += 1
                    print(
                        f"  Day {day_num:02d} Part {part_name}: \u2717  main() returned None (no `return`)"
                    )
                elif sha256(result) == expected_hash:
                    passed += 1
                    print(f"  Day {day_num:02d} Part {part_name}: ✓")
                else:
                    failed += 1
                    print(
                        f"  Day {day_num:02d} Part {part_name}: \u2717  got={result[:60]!r}"
                    )

    print(f"\n{'=' * 40}")
    print(
        f"Results: {passed} passed, {failed} failed, {skipped} skipped / {total} total"
    )
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
