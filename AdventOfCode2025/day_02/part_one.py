"""Advent of Code 2025 - Day 02 - Part One"""


def is_invalid_id(num):
    """
    Check if a number is invalid (made of a sequence repeated twice).
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(num)
    length = len(s)

    # Can only be repeated if even length
    if length % 2 != 0:
        return False

    # Check if first half equals second half
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half == second_half


def solve_part1(input_file):
    """
    Find all invalid IDs in the given ranges and sum them.
    """
    with open(input_file) as f:
        content = f.read().strip()

    # Parse the ranges
    ranges = content.split(",")

    total = 0
    invalid_ids = []

    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue

        start, end = map(int, range_str.split("-"))

        # Check each ID in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
                total += num

    return total, invalid_ids


def test_example():
    """Test with the example from the problem."""
    example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    ranges = example.split(",")
    total = 0

    print("Testing example ranges:")
    print("-" * 60)

    for range_str in ranges:
        range_str = range_str.strip()
        start, end = map(int, range_str.split("-"))

        invalid_in_range = []
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_in_range.append(num)
                total += num

        if invalid_in_range:
            print(f"{range_str}: {invalid_in_range}")
        else:
            print(f"{range_str}: no invalid IDs")

    print("-" * 60)
    print(f"Total sum: {total}")
    print("Expected: 1227775554")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
