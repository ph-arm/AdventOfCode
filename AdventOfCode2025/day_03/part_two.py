"""Advent of Code 2025 - Day 03 - Part Two"""


def find_max_joltage_12(bank):
    """
    Find the maximum joltage possible from a bank by turning on exactly 12 batteries.
    We need to select 12 digits from the bank to form the largest 12-digit number.

    Strategy: Greedily pick the largest digit at each position, ensuring we have
    enough remaining digits to complete the 12-digit number.
    """
    # Filter to only digits
    bank = "".join(c for c in bank if c.isdigit())

    if len(bank) < 12:
        raise ValueError(f"Bank has only {len(bank)} batteries, need at least 12")

    result = []
    n = len(bank)
    needed = 12

    i = 0
    while needed > 0:
        # We need 'needed' more digits
        # We can look ahead up to position (n - needed) to find the best digit
        # because we need to leave at least 'needed-1' digits after our choice
        max_digit = "0"
        max_pos = i

        # Find the largest digit in the valid range
        for j in range(i, n - needed + 1):
            if bank[j] > max_digit:
                max_digit = bank[j]
                max_pos = j

        result.append(max_digit)
        i = max_pos + 1
        needed -= 1

    return int("".join(result))


def solve_part2(input_file):
    """
    Find the maximum 12-digit joltage from each bank and sum them.
    """
    with open(input_file) as f:
        content = f.read()
        lines = [line.strip() for line in content.split("\n") if line.strip()]

    total_joltage = 0
    bank_results = []

    for bank in lines:
        max_joltage = find_max_joltage_12(bank)
        bank_results.append(max_joltage)
        total_joltage += max_joltage

    print(f"Processed {len(lines)} banks")

    return total_joltage


def test_example():
    """Test with the example from the problem."""
    example = """987654321111111
811111111111119
234234234234278
818181911112111"""

    lines = example.strip().split("\n")
    total = 0

    print("Testing example banks (Part 2):")
    print("-" * 60)

    expected = [987654321111, 811111111119, 434234234278, 888911112111]

    for i, bank in enumerate(lines):
        max_joltage = find_max_joltage_12(bank)
        total += max_joltage
        status = "✓" if max_joltage == expected[i] else "✗"
        print(f"{status} {bank}: {max_joltage} (expected {expected[i]})")

    print("-" * 60)
    print(f"Total: {total}")
    print("Expected: 3121910778619")


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
