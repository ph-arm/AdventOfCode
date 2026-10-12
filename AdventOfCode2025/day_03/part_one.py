"""Advent of Code 2025 - Day 03 - Part One"""


def find_max_joltage(bank):
    """
    Find the maximum joltage possible from a bank of batteries.
    Turn on exactly two batteries to form the largest 2-digit number.
    """
    # Filter to only digits
    bank = "".join(c for c in bank if c.isdigit())

    max_joltage = 0

    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a 2-digit number from batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


def solve_part1(input_file):
    """
    Find the maximum joltage from each bank and sum them.
    """
    with open(input_file) as f:
        content = f.read()
        lines = [line.strip() for line in content.split("\n") if line.strip()]

    total_joltage = 0
    bank_results = []

    for bank in lines:
        max_joltage = find_max_joltage(bank)
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

    print("Testing example banks:")
    print("-" * 60)

    expected = [98, 89, 78, 92]

    for i, bank in enumerate(lines):
        max_joltage = find_max_joltage(bank)
        total += max_joltage
        status = "✓" if max_joltage == expected[i] else "✗"
        print(f"{status} {bank}: {max_joltage} (expected {expected[i]})")

    print("-" * 60)
    print(f"Total: {total}")
    print("Expected: 357")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
