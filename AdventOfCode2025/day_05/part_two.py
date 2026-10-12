"""Advent of Code 2025 - Day 05 - Part Two"""


def parse_ranges(input_file):
    """
    Parse just the ranges from the input file.
    Returns: list of (start, end) tuples
    """
    with open(input_file) as f:
        content = f.read().strip()

    # Split by blank line and get only the ranges section
    ranges_section = content.split("\n\n")[0]

    # Parse ranges
    ranges = []
    for line in ranges_section.strip().split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping ranges and return a list of non-overlapping ranges.
    """
    if not ranges:
        return []

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)

    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if current range overlaps with last merged range
        if current_start <= last_end + 1:
            # Merge by extending the end if needed
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))

    return merged


def count_fresh_ids(ranges):
    """
    Count total number of fresh ingredient IDs covered by the ranges.
    """
    merged = merge_ranges(ranges)

    total = 0
    for start, end in merged:
        total += end - start + 1

    return total


def solve_part2(input_file):
    """
    Count how many ingredient IDs are considered fresh by the ranges.
    """
    ranges = parse_ranges(input_file)
    return count_fresh_ids(ranges)


def test_example():
    """Test with the example from the problem."""
    example_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]

    print("Testing example (Part 2):")
    print("-" * 60)
    print(f"Original ranges: {example_ranges}")

    merged = merge_ranges(example_ranges)
    print(f"Merged ranges: {merged}")

    # List all fresh IDs
    fresh_ids = []
    for start, end in merged:
        fresh_ids.extend(range(start, end + 1))

    print(f"Fresh IDs: {fresh_ids}")
    print(f"Total fresh: {len(fresh_ids)}")
    print("Expected: 14")
    print("-" * 60)


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
