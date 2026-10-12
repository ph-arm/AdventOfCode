"""Advent of Code 2025 - Day 05 - Part One"""


def parse_input(input_file):
    """
    Parse the input file into ranges and ingredient IDs.
    Returns: (list of (start, end) tuples, list of ingredient IDs)
    """
    with open(input_file) as f:
        content = f.read().strip()

    # Split by blank line
    parts = content.split("\n\n")
    ranges_section = parts[0]
    ids_section = parts[1]

    # Parse ranges
    ranges = []
    for line in ranges_section.strip().split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    # Parse ingredient IDs
    ingredient_ids = [int(line.strip()) for line in ids_section.strip().split("\n")]

    return ranges, ingredient_ids


def is_fresh(ingredient_id, ranges):
    """
    Check if an ingredient ID is fresh (falls within any range).
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def solve_part1(input_file):
    """
    Count how many of the available ingredient IDs are fresh.
    """
    ranges, ingredient_ids = parse_input(input_file)

    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1

    return fresh_count


def test_example():
    """Test with the example from the problem."""
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    # Parse example
    parts = example.strip().split("\n\n")
    ranges_section = parts[0]
    ids_section = parts[1]

    ranges = []
    for line in ranges_section.strip().split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    ingredient_ids = [int(line.strip()) for line in ids_section.strip().split("\n")]

    print("Testing example:")
    print("-" * 60)
    print(f"Ranges: {ranges}")
    print(f"Ingredient IDs: {ingredient_ids}")
    print()

    fresh_count = 0
    for ingredient_id in ingredient_ids:
        is_it_fresh = is_fresh(ingredient_id, ranges)
        status = "fresh" if is_it_fresh else "spoiled"
        print(f"ID {ingredient_id}: {status}")
        if is_it_fresh:
            fresh_count += 1

    print("-" * 60)
    print(f"Total fresh: {fresh_count}")
    print("Expected: 3")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
