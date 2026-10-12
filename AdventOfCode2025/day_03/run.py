#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3
Runs both parts and times execution
"""

# Import the solve functions
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from part_one import solve_part1 as solve_p1
from part_two import solve_part2 as solve_p2


def main():
    input_file = Path(__file__).parent / "input.txt"

    print("=" * 70)
    print("ADVENT OF CODE 2025 - DAY 3")
    print("=" * 70)

    # Part 1
    print("\n📌 PART 1")
    print("-" * 70)
    start_time = time.perf_counter()
    try:
        answer1 = solve_p1(str(input_file))
        elapsed1 = time.perf_counter() - start_time
        print(f"Answer: {answer1}")
        print(f"Time: {elapsed1:.6f} seconds")
    except Exception as e:
        elapsed1 = time.perf_counter() - start_time
        print(f"Error: {e}")
        print(f"Time: {elapsed1:.6f} seconds")

    # Part 2
    print("\n📌 PART 2")
    print("-" * 70)
    start_time = time.perf_counter()
    try:
        answer2 = solve_p2(str(input_file))
        elapsed2 = time.perf_counter() - start_time
        print(f"Answer: {answer2}")
        print(f"Time: {elapsed2:.6f} seconds")
    except Exception as e:
        elapsed2 = time.perf_counter() - start_time
        print(f"Error: {e}")
        print(f"Time: {elapsed2:.6f} seconds")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    try:
        total_time = elapsed1 + elapsed2
        print(f"Total time: {total_time:.6f} seconds")
    except Exception:
        pass


if __name__ == "__main__":
    main()
